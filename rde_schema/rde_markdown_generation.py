import json
import yaml
from pathlib import Path
from datetime import datetime
import os

# ----------------------------
# Utilities
# ----------------------------

def create_anchor(title):
    anchor = title.lower().replace(' ', '-')
    anchor = ''.join(c for c in anchor if c.isalnum() or c == '-')
    while '--' in anchor:
        anchor = anchor.replace('--', '-')
    return anchor.strip('-')


def describe_schema_type(schema, type_mapping):
    if not isinstance(schema, dict):
        return "", "No"

    schema_type = schema.get("type")

    if schema_type == "array":
        items = schema.get("items", {})
        item_type = items.get("type")
        accepted = type_mapping.get(item_type, item_type or "Array")
        return accepted, "Yes"

    accepted = type_mapping.get(schema_type, schema_type or "")
    return accepted, "No"


def is_array_of_objects(schema):
    return (
        schema.get("type") == "array"
        and schema.get("items", {}).get("type") == "object"
        and "properties" in schema.get("items", {})
    )


def extract_from_pointer(doc, pointer_path):
    current = doc
    for part in pointer_path.split('/'):
        if isinstance(current, dict) and part in current:
            current = current[part]
        else:
            return None
    return current


def resolve_ref(ref_url, schema_refs):
    if '#/' in ref_url:
        base, pointer = ref_url.split('#/', 1)
        doc = schema_refs.get(base) or schema_refs.get(base.split('/version/')[0])
        if doc:
            return doc, pointer

    return (
        schema_refs.get(ref_url)
        or schema_refs.get(ref_url.split('/version/')[0])
    )


# ----------------------------
# Rendering helpers
# ----------------------------

def render_property_header(schema):
    title = schema.get('title', 'Untitled')
    anchor = create_anchor(title)
    return [
        f'<a id="{anchor}"></a>',
        f"### {title}\n"
    ], title, anchor


def render_core_metadata(schema, type_mapping):
    markdown = []

    description = schema.get('description', '')
    if description:
        markdown.append(f"**Description:** {description}\n")

    accepted, repeatable = describe_schema_type(schema, type_mapping)

    markdown.append(f"**Repeatable**: {repeatable}\n")
    markdown.append(f"**Accepted Values**: {accepted}\n")

    return markdown, accepted, repeatable, description


def build_toc_entry(title, anchor, required, repeatable, accepted_values, description):
    return {
        'title': title,
        'anchor': anchor,
        'required': required,
        'repeatable': repeatable,
        'accepted_values': accepted_values,
        'description': description
    }


def render_subfields(schema, schema_refs, type_mapping):
    markdown = []

    items = schema['items']
    properties = items.get('properties', {})
    required = items.get('required', [])

    markdown.append("#### Subfields:\n")
    markdown.append("| Property | Required? | Repeatable? | Accepted Values | Description |")
    markdown.append("| -------- | --------- | ----------- | --------------- | ----------- |")

    resolved = {}

    for name, prop in properties.items():
        if '$ref' in prop:
            ref = resolve_ref(prop['$ref'], schema_refs)
            if isinstance(ref, tuple):
                doc, pointer = ref
                resolved[name] = extract_from_pointer(doc, pointer) or prop
            elif ref:
                resolved[name] = ref
            else:
                resolved[name] = prop
        else:
            resolved[name] = prop

    for name, prop in resolved.items():
        accepted, repeatable = describe_schema_type(prop, type_mapping)
        markdown.append(
            f"| {prop.get('title', name)} | "
            f"{'Yes' if name in required else 'No'} | "
            f"{repeatable} | "
            f"{accepted} | "
            f"{prop.get('description', '')} |"
        )

    markdown.append("")

    for name, prop in resolved.items():
        accepted, _ = describe_schema_type(prop, type_mapping)

        markdown.extend([
            f"##### {prop.get('title', name)}\n",
            f"**Description:** {prop.get('description', '')}\n",
            f"**Required**: {'Yes' if name in required else 'No'}\n",
            "**Repeatable**: No\n",
            f"**Accepted Values**: {accepted}\n"
        ])

        if 'usageNotes' in prop:
            markdown.append(f"**Usage Notes:** {prop['usageNotes']}\n")

        # Examples for subfield
        if prop.get('examples'):
            markdown.append("**Examples:**\n")
            for example in prop['examples']:
                markdown.append("```json")
                if isinstance(example, str):
                    markdown.append(f'"{example}"')
                else:
                    markdown.append(json.dumps(example, indent=2))
                markdown.append("```\n")

    return markdown


def render_complete_examples(schema, has_subfields):
    examples = schema.get("examples")
    if not examples:
        return []

    markdown = []

    heading = "###### Complete Examples (with Subfields):" if has_subfields else "###### Examples:"
    markdown.append(heading)
    markdown.append("")

    for example_set in examples:
        if isinstance(example_set, list):
            # Array of objects or strings
            for obj in example_set:
                markdown.append("```")
                if isinstance(obj, dict):
                    for k, v in obj.items():
                        markdown.append(f"    {k}: {v}")
                else:
                    markdown.append(f"    {obj}")
                markdown.append("```\n")
        else:
            # Single primitive example
            markdown.append("```")
            markdown.append(f"    {example_set}")
            markdown.append("```\n")

    return markdown


def render_simple_field(schema, required, schema_refs):
    markdown = []

    if required == "Yes":
        markdown.append(f"**Required**: {required}\n")

    usage = schema.get('usageNotes')
    if isinstance(usage, dict) and '$ref' in usage:
        ref = resolve_ref(usage['$ref'], schema_refs)
        if isinstance(ref, tuple):
            doc, pointer = ref
            text = extract_from_pointer(doc, pointer)
            if text:
                markdown.append(f"**Usage Notes:** {text}\n")
    elif isinstance(usage, str):
        markdown.append(f"**Usage Notes:** {usage}\n")

    # Examples for simple fields
    markdown.extend(render_complete_examples(schema, has_subfields=False))

    return markdown


# ----------------------------
# Main conversion
# ----------------------------

def json_schema_to_markdown(schema, property_name=None, required_fields=None, schema_refs=None):
    type_mapping = {
        'string': 'Text',
        'integer': 'Number',
        'boolean': 'Boolean',
        'object': 'Multi-part element; see subfield definitions for more information.'
    }

    schema_refs = schema_refs or {}
    markdown = []

    required = "Yes" if property_name and required_fields and property_name in required_fields else "No"

    header, title, anchor = render_property_header(schema)
    markdown.extend(header)

    core_md, accepted, repeatable, description = render_core_metadata(schema, type_mapping)
    markdown.extend(core_md)

    toc_entry = build_toc_entry(title, anchor, required, repeatable, accepted, description)

    has_subfields = is_array_of_objects(schema)

    if has_subfields:
        markdown.extend(render_subfields(schema, schema_refs, type_mapping))

    # Render main property-level examples after subfields (if any)
    markdown.extend(render_complete_examples(schema, has_subfields))

    # For non-subfield properties, render usageNotes & simple field metadata
    if not has_subfields:
        markdown.extend(render_simple_field(schema, required, schema_refs))

    return '\n'.join(markdown), toc_entry


# ----------------------------
# Folder processing
# ----------------------------

def load_all_schemas(property_folder, skip_files, notes_folder=None):
    refs = {}

    for path in Path(property_folder).glob('*.json'):
        if path.name in skip_files:
            continue
        data = json.loads(path.read_text(encoding='utf-8'))
        if '$id' in data:
            refs[data['$id']] = data
            refs[data['$id'].split('/version/')[0]] = data

    if notes_folder and Path(notes_folder).exists():
        for path in Path(notes_folder).glob('*.yaml'):
            data = yaml.safe_load(path.read_text(encoding='utf-8'))
            if data and '$id' in data:
                refs[data['$id']] = data

    return refs


def process_json_folder(property_folder, output_file, notes_folder=None):
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

    schema_refs = load_all_schemas(property_folder, skip_files, notes_folder)
    json_files = sorted(f for f in Path(property_folder).glob('*.json') if f.name not in skip_files)

    all_md = [
        "# DRAFT ICPSR RDE Metadata Schema Documentation\n",
        f"Last updated: {datetime.now().strftime('%B %d, %Y')}\n"
    ]

    toc = []
    sections = []

    for path in json_files:
        print(f"Processing {os.path.basename(path)}...")
        schema = json.loads(path.read_text(encoding='utf-8'))
        md, entry = json_schema_to_markdown(schema, schema_refs=schema_refs)
        sections.append(md)
        toc.append(entry)

    all_md.append("## Metadata Elements: Overview\n")
    all_md.append("| Property | Required? | Repeatable? | Accepted Values | Description |")
    all_md.append("| -------- | --------- | ----------- | --------------- | ----------- |")

    for e in toc:
        all_md.append(
            f"| [{e['title']}](#{e['anchor']}) | {e['required']} | {e['repeatable']} | "
            f"{e['accepted_values']} | {e['description']} |"
        )

    all_md.append("\n---\n## Metadata Elements: Detailed Information\n")

    for section in sections:
        all_md.append(section)
        all_md.append("\n---\n")

    Path(output_file).write_text('\n'.join(all_md), encoding='utf-8')
    print(f"\nSuccessfully generated: {output_file}")


# ----------------------------
# Entry point
# ----------------------------

if __name__ == "__main__":

    main_dir = "C:/icpsr_github/metadata/rde_schema"

    process_json_folder(
        property_folder = os.path.join(main_dir, "property_bank"),
        notes_folder=os.path.join(main_dir, "notes"),
        output_file=os.path.join(main_dir, "icpsr_rde_schema.md")
    )