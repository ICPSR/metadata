import json
from pathlib import Path
from datetime import datetime
import yaml
import sys
import argparse

class QuoteDumper(yaml.SafeDumper):
    pass

def quoted_str_representer(dumper, data):
    return dumper.represent_scalar("tag:yaml.org,2002:str", data, style='"')

QuoteDumper.add_representer(str, quoted_str_representer)

# ----------------------------
# Configuration
# ----------------------------

SKIP_FILES = {
    "common_data_elements.json",
    "contributors.json",
    "deposits.json",
    "extent_of_processing.json",
    "external_source_id.json",
    "languages.json",
    "link_title.json",
    "link_url.json",
    "oversamples.json",
    "restrictions.json",
    "study_purpose.json"
}

PROCESSING_ORDER = [
    "title",
    "alternate_titles",
    "principal_investigators",
    "funding_sources",
    "summary",
    "icpsr_subject_terms",
    "jel_classifications",
    "mesh_subject_terms",
    "time_periods",
    "nationally_representative_sample",
    "geographic_coverage_areas",
    "smallest_geographic_unit",
    "study_design",
    "universe",
    "time_methods",
    "units_of_analysis",
    "sampling_procedures",
    "sampling_note",
    "weight",
    "response_rates",
    "data_source_types",
    "external_data_sources",
    "collection_modes",
    "collection_dates",
    "variable_description",
    "scales",
    "data_management_plan",
    "preregistration",
    "software_applications",
    "general_data_formats",
    "notes",
    "manuscript_number",
    "ada_accessibility",
    "license",
    "version_history",
    "distributors",
    "study_number",
    "doi",
    "citation",
    "person",
    "organization"
]

# ----------------------------
# Utilities
# ----------------------------

def anchor(text):
    return text.lower().replace(" ", "-").replace("_", "-")

def convert_example_to_titles(data, schema):
    """
    Recursively replace property keys with schema 'title' values.
    Works for objects and arrays of objects.
    """
    if isinstance(data, dict):
        props = schema.get("properties", {})
        result = {}

        for key, value in data.items():
            prop_schema = props.get(key, {})
            title = prop_schema.get("title", key.replace("_", " ").title())

            result[title] = convert_example_to_titles(value, prop_schema)

        return result

    elif isinstance(data, list):
        items_schema = schema.get("items", {})
        return [convert_example_to_titles(item, items_schema) for item in data]

    else:
        return data

def render_yaml_examples(examples, schema):
    md = []

    for ex in examples:

        # strings stay unchanged
        if isinstance(ex, (str, int, float)):
            md.append("```text")
            md.append(f'"{ex}"')
            md.append("```\n")
            continue

        # list containing only simple values (strings or numbers)
        if isinstance(ex, list) and all(isinstance(i, (str, int, float)) for i in ex):
            md.append("```text")
            for item in ex:
                md.append(f'"{item}"')
            md.append("```\n")
            continue

        # convert keys to titles
        human_ex = convert_example_to_titles(ex, schema)

        # dump YAML normally
        #yaml_str = yaml.safe_dump(human_ex, sort_keys=False)

        # dump YAML; enclose everything in quotes
        yaml_str = yaml.dump(human_ex, Dumper=QuoteDumper, sort_keys=False)
        yaml_str = yaml_str.replace("\n...\n", "\n").rstrip(".\n")

        # insert a blank line between top-level list items
        if isinstance(human_ex, list):
            lines = yaml_str.splitlines()
            new_lines = []
            for i, line in enumerate(lines):
                new_lines.append(line)
                # if the next line starts a new '- ', insert a blank line
                if i + 1 < len(lines) and lines[i + 1].startswith("- "):
                    new_lines.append("")  # blank line between items
            yaml_str = "\n".join(new_lines)

        md.append("```yaml")
        md.append(yaml_str)
        md.append("```\n")

    return md

def add_table_usageNotes(md_table, old_usage_note):

    # set up header and table for later use
    header = "This field employs a local ICPSR controlled vocabulary; see below for terms and definitions:"
    if old_usage_note:
        usage_notes = [old_usage_note, "\n", header, "\n", *md_table, "\n"]
    else:
        usage_notes = [header, "\n", *md_table, "\n"]

    return usage_notes

def get_schema_values(note, term, ROOT):
    """
    Returns usage notes text for a property.
    Supports either inline string or $ref to local YAML file.
    """
    if isinstance(note, str):
        return note  # inline text

    if isinstance(note, dict) and "$ref" in note:
        ref = note["$ref"]
        # Extract filename from URL, e.g., summary
        filename = ref.split("notes/")[-1].split("#")[0].rstrip("/")
        notes_file = Path(ROOT, "notes", f"{filename}.yaml")
        if notes_file.exists():
            with open(notes_file, "r", encoding="utf-8") as f:
                data = yaml.safe_load(f)
            match = data.get(term)
            
            return match.strip() if match else None
            
    return None

def cv_to_table(cv_name, ROOT):   
    cv_file = Path(ROOT / "vocab_preset" / "data" / f"{cv_name}.json")
    # return None if there is no matching CV
    if not cv_file.is_file():
        return None

    # otherwise, build Markdown table of terms
    with cv_file.open("r", encoding="utf-8") as f:
        cv_data = json.load(f)

    temp_md = []
    temp_md.append("| Term | Definition |")
    temp_md.append("|------|------------|")

    for item in cv_data:
        term = item.get("label", "")
        definition = item.get("description", "")
        temp_md.append(f"| {term} | {definition} |")

    return temp_md

def type_label(t):
    mapping = {
        "string": "Text",
        "integer": "Number",
        "boolean": "Boolean",
        "object": "Multi-part element; see subfields",
        "array": "Array"
    }
    return mapping.get(t, t or "")

def get_ref(prop):
    if "$ref" in prop:
        return prop["$ref"]

    if prop.get("type") == "array":
        items = prop.get("items", {})
        if "$ref" in items:
            return items["$ref"]

    return None

def resolve_ref_property(prop):
    """
    Normalize $ref-based person/organization properties.
    Returns (title, description, type, ref_title)
    """
    ref = get_ref(prop)

    if ref and (
        "property_banks/person/" in ref or
        "property_banks/organization/" in ref
    ):
        name = ref.split("/")[-3] if "/version/" in ref else ref.split("/")[-1]
        
        ref_title = name.replace("_", " ").title()
        ref_desc = f"See the [{ref_title}](#{anchor(ref_title)}) field."

        title = prop.get("title", ref_title)
        desc = prop.get("description", ref_desc)
        typ = "Multi-part element; see subfields"

        return title, desc, typ, ref_title

    return None

def ref_to_link(ref):
    """
    Convert schema $ref → markdown link
    """
    name = ref.split("/")[-3] if "/version/" in ref else ref.split("/")[-1]
    title = name.replace("_", " ").title()
    return title, f"See the [{title}](#{anchor(title)}) field."

# ----------------------------
# Schema loading
# ----------------------------

def load_schemas(PROPERTY_DIR, mode):
    schemas = {}
    file_list = PROPERTY_DIR.glob("*.json")

    if mode == "legacy":
        legacy_file_list = list(file_list)
        if len(legacy_file_list) == 1:
            f = Path(legacy_file_list[0])
            data = json.loads(f.read_text(encoding="utf-8"))
            schemas = data['properties']
    
    else:
        for f in PROPERTY_DIR.glob("*.json"):
            if f.name in SKIP_FILES:
                continue
            data = json.loads(f.read_text(encoding="utf-8"))
            schemas[f.stem] = data

    return schemas

# ----------------------------
# Schema parsing
# ----------------------------

def get_subfields(schema):
    """
    Normalize object + array-of-object schemas
    """
    if schema.get("type") == "object":
        return schema.get("properties", {}), schema.get("required", [])
    if schema.get("type") == "array":
        items = schema.get("items", {})
        if items.get("type") == "object":
            return items.get("properties", {}), items.get("required", [])
    return {}, []

def get_repeatable(schema):
    return "Yes" if schema.get("type") == "array" else "No"

def get_type(schema):
    if schema.get("type") == "array":
        item_type = schema.get("items", {}).get("type")
        return type_label(item_type) if item_type else "Array"
    return type_label(schema.get("type"))

# ----------------------------
# Rendering helpers
# ----------------------------

def get_conditional_required(schema):
    """
    Detect oneOf-based required constraints.
    """
    #Normalize object
    if schema.get("type") == "array":
        schema = schema.get("items", {})

    conditional_map = {}

    for clause in schema.get("allOf", []):
        if "oneOf" in clause:
            options = clause["oneOf"]

            # collect required fields per option
            groups = []
            for opt in options:
                req = opt.get("required", [])
                if req:
                    groups.append(req)

            if groups:
                # flatten unique field names
                all_fields = set(f for group in groups for f in group)

                # build readable label
                label = " or ".join(
                    [", ".join(f.title() for f in g) for g in groups]
                )

                for field in all_fields:
                    conditional_map[field] = f"Conditional (must include either {label})"
        elif "required" in clause:
            # Handle regular required fields
            for field in clause["required"]:
                conditional_map[field] = "Yes"

    return conditional_map

def render_examples(examples):
    md = []
    for ex in examples:
        md.append("```json")
        if isinstance(ex, (dict, list)):
            md.append(json.dumps(ex, indent=2))
        else:
            md.append(str(ex))
        md.append("```\n")
    return md

def render_subfields(ROOT, mode, schema, properties, required, parent_anchor, level=4):
    """
    Render subfields table AND detailed per-subfield sections with anchors and examples.
    """
    md = []

    conditional_required = get_conditional_required(schema)

    md.append(f"{'#' * level} Subfields:\n")

    # Table header
    md.append("| Property | Required? | Repeatable? | Accepted Values | Description |")
    md.append("|---|---|---|---|---|")

    # Table rows
    for name, prop in properties.items():
        resolved = resolve_ref_property(prop)
        if resolved:
            title, desc, typ, _ = resolved
        else:
            title = prop.get("title", name.replace("_", " ").title())
            desc = prop.get("description", "")
            typ = get_type(prop)

        #set variables    
        anchor_id = f"{parent_anchor}_{name}"
        if name in required:
            req_label = "Yes"
        elif name in conditional_required:
            val = conditional_required[name]
            if "Conditional" in val:
                req_label = "Conditional"
            elif val == "Yes":
                req_label = "Yes"
            else:
                req_label = "No"
        else:
            req_label = "No"
        # build out table
        md.append(f"| [{title}](#{anchor_id}) | {req_label} | "
                  f"{get_repeatable(prop)} | {typ} | {desc} |")

    md.append("")

    # ---- Per-subfield detailed sections ----
    for name, prop in properties.items():
        #check if this property is repeatable
        rep = get_repeatable(prop)
        
        #check if this property is required (or conditionally required)
        if name in required:
            req = "Yes"
        elif name in conditional_required:
            req = conditional_required[name]
        else:
            req = "No"

        #check if we have a $ref keyword; handle accordingly
        resolved = resolve_ref_property(prop)
        if resolved:
            title, desc, typ, ref_title = resolved
            typ = f"Multi-part element; for more information, see the [{ref_title}](#{anchor(ref_title)}) field"
        else:
            title = prop.get("title", name.replace("_", " ").title())
            desc = prop.get("description", "")
            typ = get_type(prop)
        
        anchor_id = f"{parent_anchor}_{name}"
        md.append(f"<a name=\"{anchor_id}\"></a>")
        md.append(f"{'#' * (level + 1)} {title}\n")

        md.append(f"**Description:** {desc}\n")
        md.append(f"**Required:** {req}\n")
        md.append(f"**Repeatable:** {rep}\n")
        md.append(f"**Accepted Values:** {typ}\n")

        #check for usage note, but don't write just yet
        usage_note = None
        if "usageNotes" in prop:
            usage_note = get_schema_values(prop['usageNotes'], "usageNotes", ROOT)

        if "controlledVocab" in prop:
            if mode == "legacy":
                controlledVocab = get_schema_values(prop['controlledVocab'], "controlledVocab", ROOT)
                md.append(f"**Controlled Vocabulary:** {controlledVocab}\n")
            else:
                md_table = cv_to_table(prop['controlledVocab'], ROOT)
                #if table, then update usageNote
                if md_table:
                    usage_note = add_table_usageNotes(md_table, usage_note)

        if isinstance(usage_note, str):
            md.append(f"**Usage Notes:** {usage_note}\n")
        elif isinstance(usage_note, list):
            usage_note[0] = "**Usage Notes:** " + usage_note[0]
            md.extend(usage_note)

        if "icpsrGuidance" in prop:
            icpsrGuidance = get_schema_values(prop['icpsrGuidance'], "icpsrGuidance", ROOT)
            md.append(f"**ICPSR Input Guidance:** {icpsrGuidance}\n")

        # Recurse for nested subfields
        subprops, subreq = get_subfields(prop)
        if subprops:
            md.extend(render_subfields(ROOT, mode, prop, subprops, subreq, anchor_id, level + 1))

        # Examples per subfield
        if "examples" in prop:

            schema_type = prop.get("type")
            items_type = prop.get("items", {}).get("type")

            if schema_type == "object" or (schema_type == "array" and items_type == "object"):
                md.append(f"#### Complete {title} Examples (with Subfields):\n")
            else:
                md.append("**Examples:**\n")

            md.extend(render_yaml_examples(prop["examples"], prop))


    return md

def render_property(name, schema, ROOT, mode, TOP_LEVEL_REQUIRED):
    md = []

    title = schema.get("title", name.replace("_", " ").title())
    desc = schema.get("description", "")
    required = "Yes" if name in TOP_LEVEL_REQUIRED else "No"
    anchor_id = anchor(title)

    md.append(f"<a id=\"{anchor_id}\"></a>")
    md.append(f"### {title}\n")
    if desc:
        md.append(f"**Description:** {desc}\n")
    md.append(f"**Required:** {required}\n")
    md.append(f"**Repeatable:** {get_repeatable(schema)}\n")
    md.append(f"**Accepted Values:** {get_type(schema)}\n")

    # Check for additional keywords: controlledVocab and usageNotes
    usage_note = None
    if "usageNotes" in schema:
        usage_note = get_schema_values(schema['usageNotes'], "usageNotes", ROOT)

    if "controlledVocab" in schema:
        if mode == "legacy":
            controlledVocab = get_schema_values(schema['controlledVocab'], "controlledVocab", ROOT)
            md.append(f"**Controlled Vocabulary:** {controlledVocab}\n")
        else:
            md_table = cv_to_table(schema['controlledVocab'], ROOT)
            #if table, then update usageNote
            if md_table:
                usage_note = add_table_usageNotes(md_table, usage_note)

    if isinstance(usage_note, str):
        md.append(f"**Usage Notes:** {usage_note}\n")
    elif isinstance(usage_note, list):
        usage_note[0] = "**Usage Notes:** " + usage_note[0]
        md.extend(usage_note)

    if "icpsrGuidance" in schema:
        icpsrGuidance = get_schema_values(schema['icpsrGuidance'], "icpsrGuidance", ROOT)
        md.append(f"**ICPSR Input Guidance:** {icpsrGuidance}\n")

    properties, required_subfields = get_subfields(schema)
    if properties:
        md.extend(render_subfields(ROOT, mode, schema, properties, required_subfields, anchor_id))

    # Examples
    schema_type = schema.get("type")
    items_type = schema.get("items", {}).get("type")

    if "examples" in schema:

        schema_type = schema.get("type")
        items_type = schema.get("items", {}).get("type")

        if schema_type == "object" or (schema_type == "array" and items_type == "object"):
            md.append(f"#### Complete {title} Examples (with Subfields):\n")
        else:
            md.append("**Examples:**\n")

        md.extend(render_yaml_examples(schema["examples"], schema))

        return md, {
            "title": title,
            "anchor": anchor_id,
            "required": required,
            "repeatable": get_repeatable(schema),
            "type": get_type(schema),
            "description": desc
        }

# ----------------------------
# Main
# ----------------------------

def main():

    parser = argparse.ArgumentParser(description="Generate Markdown from JSON Schema(s).")
    parser.add_argument(
        "--input",
        help="Path to the project directory",
        required=True
    )
    parser.add_argument(
        "--mode",
        choices=["legacy", "current"],
        default="directory",
        help="Whether to process legacy or current ICPSR metadata schema.",
        required=True
    )
    args = parser.parse_args()
    input_path = Path(args.input)
    mode = args.mode
    current_date = datetime.now().strftime('%B %d, %Y')

    if mode == "legacy":
        TOP_LEVEL_REQUIRED = {
            "title", 
            "principal_investigator", 
            "version", 
            "version_date", 
            "distributor", 
            "summary", 
            "subject_term", 
            "time_period", 
            "geographic_coverage_area", 
            "study_number",
            "doi"
        }
        ROOT = input_path / "schema"
        PROPERTY_DIR = ROOT 
        OUTPUT_FILE = input_path / "markdown" / "icpsr_legacy_schema.md"
        version_file = input_path / "markdown" / "legacy_schema_version_history.md"
        key_file = input_path / "markdown" / "legacy_schema_key.md"
        intro_file = input_path / "markdown" / "legacy_schema_intro_text.md"
        main_title = "# ICPSR Legacy Metadata Schema\n"
        
    else:
        TOP_LEVEL_REQUIRED = {
            "title",
            "principal_investigators",
            "time_periods",
            "geographic_coverage_areas",
            "icpsr_subject_terms",
            "summary",
            "study_number",
            "doi"
        }
        ROOT = input_path / "rde_schema"
        PROPERTY_DIR = ROOT / "property_bank"
        OUTPUT_FILE = input_path / "markdown" / "icpsr_metadata_schema.md"
        version_file = input_path / "markdown" / "schema_version_history.md"
        key_file = input_path / "markdown" / "schema_key.md"
        intro_file = input_path / "markdown" / "schema_intro_text.md" 
        main_title = "# ICPSR Metadata Schema\n"

    schemas = load_schemas(PROPERTY_DIR, mode)

    # exit if 'schemas' is empty:
    if not schemas:
        print(f"No schemas found in {PROPERTY_DIR} (using mode {mode})")
        sys.exit(1)
    sections = []
    toc = []

    if mode == "current":
        schema_items = []
        for key in PROCESSING_ORDER:
            if key in schemas:
                schema_items.append((key, schemas[key]))
        # Add any remaining keys not in PROCESSING_ORDER at the end
        for key in schemas:
            if key not in PROCESSING_ORDER:
                schema_items.append((key, schemas[key]))
    else:
        schema_items = schemas.items()

    for name, schema in schema_items:
        try:
            md, entry = render_property(name, schema, ROOT, mode, TOP_LEVEL_REQUIRED)
        except TypeError:
            print(name)
            sys.exit(1)
        sections.extend(md)
        sections.append("\n---\n")
        toc.append(entry)

    # pull in text from files
    intro_text = intro_file.read_text(encoding="utf-8").splitlines()
    key_text = key_file.read_text(encoding="utf-8").splitlines()
    version_text = version_file.read_text(encoding="utf-8").splitlines()

    output = []
    output.append(main_title)
    output.append(f"Last updated: {current_date}\n\n")
    output.extend(intro_text)

    # Add over table
    output.append("## Metadata Elements: Overview\n")
    output.append("| Property | Required? | Repeatable? | Accepted Values | Description |")
    output.append("|---|---|---|---|---|")

    for e in toc:
        output.append(
            f"| [{e['title']}](#{e['anchor']}) | "
            f"{e['required']} | "
            f"{e['repeatable']} | "
            f"{e['type']} | "
            f"{e['description']} |"
        )
    output.append("\n---\n")
    
    # add key to understand documentation
    output.extend(key_text)

    # add detailed metadata information
    output.append("\n---\n## Metadata Elements: Detailed Information\n")
    output.extend(sections)

    # Add version history information
    output.extend(version_text)

    OUTPUT_FILE.write_text("\n".join(output), encoding="utf-8")
    print(f"Markdown generated: {OUTPUT_FILE}")

if __name__ == "__main__":
    main()