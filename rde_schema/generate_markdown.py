import json
from pathlib import Path
from datetime import datetime
import yaml
import sys

class QuoteDumper(yaml.SafeDumper):
    pass

def quoted_str_representer(dumper, data):
    return dumper.represent_scalar("tag:yaml.org,2002:str", data, style='"')

QuoteDumper.add_representer(str, quoted_str_representer)

ROOT = Path("C:/icpsr_github/metadata/schema")
PROPERTY_DIR = ROOT
OUTPUT_FILE = ROOT / "icpsr_legacy_schema-TEST.md"

# ----------------------------
# Configuration
# ----------------------------

TOP_LEVEL_REQUIRED = {
    "title",
    "time_periods",
    "geographic_coverage_areas",
    "icpsr_subject_terms",
    "summary"
}

skip_files = {
    "common_data_elements.json",
    "contributors.json",
    "deposits.json",
    "extent_of_processing.json",
    "external_source_id.json",
    "languages.json",
    "link_title.json",
    "link_url.json",
    "manuscript_number.json",
    "oversamples.json",
    "restrictions.json",
    "study_purpose.json"
}

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

def get_usage_notes(note):
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
            with open(notes_file, "r") as f:
                data = yaml.safe_load(f)
            match = data.get('usageNotes')
            
            return match.strip() if match else None
            
    return None

def check_cvs(short_cv):
    cv_definitions = Path(ROOT, "vocab_preset", "definitions.json")
    with open(cv_definitions, 'r', encoding='utf-8') as cvd:
        cv_data = json.load(cvd)

    match = [d for d in cv_data if d['code'] == short_cv]

    if match:
        if match[0].get('externalURI'):
            external_uri = f" ({match[0]['externalURI']})"
        else:
            external_uri = ""
        return f"{match[0]['description']}{external_uri}"
    else:
        return None

def type_label(t):
    mapping = {
        "string": "Text",
        "integer": "Number",
        "boolean": "Boolean",
        "object": "Multi-part element; see subfields",
        "array": "Array"
    }
    return mapping.get(t, t or "")

def ref_to_link(ref):
    """
    Convert schema $ref → markdown link
    """
    name = ref.split("/")[-3] if "/version/" in ref else ref.split("/")[-1]
    title = name.replace("_", " ").title()
    return title, f"See the [{title}](#{anchor(title)}) property."

# ----------------------------
# Schema loading
# ----------------------------

def load_schemas():
    schemas = {}
    file_list = PROPERTY_DIR.glob("*.json")

    if len(file_list) == 1:
        f = Path(file_list[0])
        data = json.loads(f.read_text(encoding="utf-8"))
        schemas = data['properties']
    
    elif len(file_list) > 1:
        for f in PROPERTY_DIR.glob("*.json"):
            if f.name in skip_files:
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

def render_subfields(properties, required, parent_anchor, level=4):
    """
    Render subfields table AND detailed per-subfield sections with anchors and examples.
    """
    md = []

    md.append(f"{'#' * level} Subfields:\n")

    # Table header
    md.append("| Property | Required? | Repeatable? | Accepted Values | Description |")
    md.append("|---|---|---|---|---|")

    # Table rows
    for name, prop in properties.items():
        try:
            title = prop.get("title", name.replace("_", " ").title())
        except AttributeError:
            print(name, prop)
            sys.exit(1)
        desc = prop.get("description", "")
        if "$ref" in prop and ("property_banks/person/" in prop["$ref"] or "property_banks/organization/" in prop["$ref"]):
            ref_title, desc = ref_to_link(prop["$ref"])
            typ = "Object"
        else:
            typ = get_type(prop)
        anchor_id = f"{parent_anchor}_{name}"
        md.append(f"| [{title}](#{anchor_id}) | {'Yes' if name in required else 'No'} | "
                  f"{get_repeatable(prop)} | {typ} | {desc} |")

    md.append("")

    # ---- Per-subfield detailed sections ----
    for name, prop in properties.items():
        title = prop.get("title", name.replace("_", " ").title())
        rep = get_repeatable(prop)
        req = "Yes" if name in required else "No"

        if "$ref" in prop and ("property_banks/person/" in prop["$ref"] or "property_banks/organization/" in prop["$ref"]):
            ref_title, ref_link = ref_to_link(prop["$ref"])
            desc = f"See the [{ref_title}](#{anchor(ref_title)}) property."
            typ = f"See the [{ref_title}](#{anchor(ref_title)}) property"
        else:
            desc = prop.get("description", "")
            typ = get_type(prop)


        anchor_id = f"{parent_anchor}_{name}"
        md.append(f"<a name=\"{anchor_id}\"></a>")
        md.append(f"{'#' * (level + 1)} {title}\n")

        md.append(f"**Description:** {desc}  ")
        md.append(f"**Required:** {req}  ")
        md.append(f"**Repeatable:** {rep}  ")
        md.append(f"**Accepted Values:** {typ}  ")

        # if "controlledVocab" in prop:
        #     md.append(f"**Controlled Vocabulary:** {check_cvs(prop['controlledVocab'])}  ")

        if "usageNotes" in prop:
            note = get_usage_notes(prop['usageNotes'])
            if note:
                md.append(f"**Usage Notes:** {note}  ")

        # Examples per subfield
        if "examples" in prop:
            md.append("\n**Examples:**\n")
            md.extend(render_yaml_examples(prop["examples"], prop))

        # Recurse for nested subfields
        subprops, subreq = get_subfields(prop)
        if subprops:
            md.extend(render_subfields(subprops, subreq, anchor_id, level + 1))

    return md

def render_property(name, schema):
    md = []

    title = schema.get("title", name.replace("_", " ").title())
    desc = schema.get("description", "")
    required = "Yes" if name in TOP_LEVEL_REQUIRED else "No"
    anchor_id = anchor(title)

    md.append(f"<a id=\"{anchor_id}\"></a>")
    md.append(f"### {title}\n")
    if desc:
        md.append(f"**Description:** {desc}  ")
    md.append(f"**Required:** {required}  ")
    md.append(f"**Repeatable:** {get_repeatable(schema)}  ")
    md.append(f"**Accepted Values:** {get_type(schema)}  ")

    # Check for additional keywords: controlledVocab and usageNotes
    # if "controlledVocab" in schema:
    #     md.append(f"**Controlled Vocabulary:** {check_cvs(schema['controlledVocab'])}  ")

    if "usageNotes" in schema:
        note = get_usage_notes(schema['usageNotes'])
        if note:
            md.append(f"**Usage Notes:** {note}  ")

    properties, required_subfields = get_subfields(schema)
    if properties:
        md.extend(render_subfields(properties, required_subfields, anchor_id))

    # Examples
    schema_type = schema.get("type")
    items_type = schema.get("items", {}).get("type")

    if "examples" in schema:

        schema_type = schema.get("type")
        items_type = schema.get("items", {}).get("type")

        if schema_type == "object" or (schema_type == "array" and items_type == "object"):
            md.append(f"###### Complete {title} Examples (with Subfields):\n")
        else:
            md.append("\n**Examples:**\n")

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
    schemas = load_schemas()
    sections = []
    toc = []

    for name, schema in sorted(schemas.items()):
        try:
            md, entry = render_property(name, schema)
        except TypeError:
            print(name)
            sys.exit(1)
        sections.extend(md)
        sections.append("\n---\n")
        toc.append(entry)

    output = []
    output.append("# ICPSR RDE Metadata Schema\n")
    output.append(f"Last updated: {datetime.now():%B %d, %Y}\n")
    output.append("## Overview\n")

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

    output.append("\n---\n## Properties\n")
    output.extend(sections)

    OUTPUT_FILE.write_text("\n".join(output), encoding="utf-8")
    print(f"Markdown generated: {OUTPUT_FILE}")

if __name__ == "__main__":
    main()