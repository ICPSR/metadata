import json
import os
from pathlib import Path
from datetime import datetime

def create_anchor(title):
    """Create an anchor link from a title.
    
    Args:
        title: The title to convert to an anchor
    
    Returns:
        A URL-safe anchor string
    """
    # Convert to lowercase, replace spaces with hyphens, remove special chars
    anchor = title.lower()
    anchor = anchor.replace(' ', '-')
    # Keep only alphanumeric characters and hyphens
    anchor = ''.join(c for c in anchor if c.isalnum() or c == '-')
    # Remove consecutive hyphens
    while '--' in anchor:
        anchor = anchor.replace('--', '-')
    # Remove leading/trailing hyphens
    anchor = anchor.strip('-')
    return anchor


def json_schema_to_markdown(schema, property_name=None, required_fields=None):
    """Convert a JSON Schema object to Markdown documentation.
    
    Args:
        schema: The JSON schema object
        property_name: The name of this property (for checking required status)
        required_fields: List of required field names from parent schema
    
    Returns:
        A tuple of (markdown_string, toc_entry_dict)
    """
    
    markdown = []
    repeatable = "No"  # Default
    is_required = "No"  # Default
    
    # Check if this property is required
    if property_name and required_fields and property_name in required_fields:
        is_required = "Yes"
    
    # Title with anchor using HTML
    title = schema.get('title', 'Untitled')
    anchor = create_anchor(title)
    markdown.append(f'<a id="{anchor}"></a>')
    markdown.append(f"### {title}\n")
    
    # Description
    description = schema.get('description', '')
    if description:
        markdown.append(f"**Description:** {description}\n")
    
    # Determine repeatable and type
    if 'type' in schema:
        type_mapping = {
            'string': 'Text',
            'integer': 'Number',
            'boolean': 'Boolean',
            'object': 'Multi-part element; see subfield definitions for more information.'
        }
        
        # Handle arrays specially
        if schema['type'] == 'array':
            repeatable = "Yes"
            # Look for the type in items
            if 'items' in schema and 'type' in schema['items']:
                items_type = schema['items']['type']
                readable_type = type_mapping.get(items_type, items_type)
            else:
                readable_type = 'Array'
        else:
            readable_type = type_mapping.get(schema['type'], schema['type'])
    
    markdown.append(f"**Repeatable**: {repeatable}\n")
    markdown.append(f"**Accepted Values**: {readable_type}\n")
    
    # Create TOC entry for this schema
    toc_entry = {
        'title': title,
        'anchor': anchor,
        'required': is_required,
        'repeatable': repeatable,
        'accepted_values': readable_type,
        'description': description
    }
    
    # Check if this is an array of objects with properties (complex nested structure)
    has_subfields = (schema.get('type') == 'array' and 
                     schema.get('items', {}).get('type') == 'object' and
                     'properties' in schema.get('items', {}))
    
    if has_subfields:
        # Generate subfields table
        markdown.append("#### Subfields:\n")
        markdown.append("| Property | Required? | Repeatable? | Accepted Values | Description |")
        markdown.append("| -------- | --------- | ----------- | --------------- | ----------- |")
        
        items = schema['items']
        properties = items.get('properties', {})
        item_required = items.get('required', [])
        
        for prop_name, prop_schema in properties.items():
            prop_title = prop_schema.get('title', prop_name)
            prop_required = "Yes" if prop_name in item_required else "No"
            prop_repeatable = "No"  # Subfields are not repeatable unless they're arrays themselves
            
            # Get the type
            if prop_schema.get('type') == 'array':
                prop_repeatable = "Yes"
                if 'items' in prop_schema and 'type' in prop_schema['items']:
                    prop_type = type_mapping.get(prop_schema['items']['type'], prop_schema['items']['type'])
                else:
                    prop_type = 'Array'
            else:
                prop_type = type_mapping.get(prop_schema.get('type', ''), prop_schema.get('type', ''))
            
            prop_description = prop_schema.get('description', '')
            
            markdown.append(f"| {prop_title} | {prop_required} | {prop_repeatable} | {prop_type} | {prop_description} |")
        
        markdown.append("")  # Empty line after table
        
        # Now generate detailed sections for each subfield
        for prop_name, prop_schema in properties.items():
            prop_title = prop_schema.get('title', prop_name)
            prop_required = "Yes" if prop_name in item_required else "No"
            prop_description = prop_schema.get('description', '')
            
            markdown.append(f"##### {prop_title}\n")
            markdown.append(f"**Description:** {prop_description}\n")
            markdown.append(f"**Required**: {prop_required}\n")
            markdown.append(f"**Repeatable**: No\n")
            
            # Get accepted values for subfield
            if prop_schema.get('type') == 'array':
                if 'items' in prop_schema and 'type' in prop_schema['items']:
                    subfield_type = type_mapping.get(prop_schema['items']['type'], prop_schema['items']['type'])
                else:
                    subfield_type = 'Array'
            else:
                subfield_type = type_mapping.get(prop_schema.get('type', ''), prop_schema.get('type', ''))
            
            markdown.append(f"**Accepted Values**: {subfield_type}\n")
            
            # Usage notes for subfield
            if 'usageNotes' in prop_schema:
                markdown.append(f"**Usage Notes:** {prop_schema['usageNotes']}\n")
            
            # Examples for subfield
            if 'examples' in prop_schema and prop_schema['examples']:
                markdown.append("**Examples:**\n")
                for example in prop_schema['examples']:
                    # Format as JSON code block
                    markdown.append("```json")
                    markdown.append(f'"{example}"' if isinstance(example, str) else json.dumps(example, indent=2))
                    markdown.append("```\n")
        
        # Complete examples section - formatted as readable text
        if 'examples' in schema and schema['examples']:
            markdown.append("###### Complete Examples (with Subfields):\n")
            
            for example_group in schema['examples']:
                # Handle if examples is a list of objects
                if isinstance(example_group, list):
                    for example_obj in example_group:
                        markdown.append("```")
                        for key, value in example_obj.items():
                            # Get the title for this property
                            prop_title = properties.get(key, {}).get('title', key)
                            markdown.append(f"    {prop_title}: {value}")
                        markdown.append("```\n")
                # Handle if example is a single object
                elif isinstance(example_group, dict):
                    markdown.append("```")
                    for key, value in example_group.items():
                        prop_title = properties.get(key, {}).get('title', key)
                        markdown.append(f"    {prop_title}: {value}")
                    markdown.append("```\n")
    
    else:
        # Simple type (not nested object) - use original format
        if is_required != "No":
            markdown.append(f"**Required**: {is_required}\n")
        
        # Usage Notes
        if 'usageNotes' in schema:
            markdown.append(f"**Usage Notes:** {schema['usageNotes']}\n")
        
        # Examples - wrap in code blocks
        if 'examples' in schema and schema['examples']:
            markdown.append("**Examples:**\n")
            for example in schema['examples']:
                markdown.append("```")
                markdown.append(f"{example}")
                markdown.append("```\n")
    
    return '\n'.join(markdown), toc_entry


def process_json_folder(input_folder, output_file):
    """Process all JSON files in a folder and output to a single Markdown file.
    
    Args:
        input_folder: Path to folder containing JSON schema files
        output_file: Path to output Markdown file
    """
    
    # List of files to skip
    skip_files = [
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
    ]
    
    # Get all JSON files in the folder
    json_files = sorted(Path(input_folder).glob('*.json'))
    
    if not json_files:
        print(f"No JSON files found in {input_folder}")
        return
    
    # Filter out files in the skip list
    json_files = [f for f in json_files if f.name not in skip_files]
    
    if not json_files:
        print(f"No JSON files to process after applying skip list")
        return
    
    print(f"Skipping {len(skip_files)} files")
    print(f"Processing {len(json_files)} files\n")
    
    all_markdown = []
    toc_entries = []
    
    # Add a header to the document
    all_markdown.append("# DRAFT ICPSR RDE Metadata Schema Documentation\n")
    current_date = datetime.now().strftime('%B %d, %Y')
    all_markdown.append(f"Last updated: {current_date}\n")
    all_markdown.append("This metadata schema was developed as part of the Inter-university Consortium for Political and Social Research (ICPSR) as part of the NSF-funded [Research Data Ecosystem (RDE)](https://www.icpsr.umich.edu/sites/icpsr/find-data/working-together/projects/rde) project. The schema is used to describe ICPSR data collections; these rules and definitions are intended to (a) assist ICPSR staff with metadata entry, and (b) help ICPSR users – including data depositors and researchers accessing data – understand how to use and interpret our metadata.\n")
    
    # Process each JSON file first to collect TOC entries
    schema_markdowns = []
    for json_file in json_files:
        print(f"Processing: {json_file.name}")
        
        try:
            with open(json_file, 'r', encoding='utf-8') as f:
                schema = json.load(f)
            
            # Convert schema to markdown and get TOC entry
            markdown_output, toc_entry = json_schema_to_markdown(schema)
            schema_markdowns.append(markdown_output)
            toc_entries.append(toc_entry)
            
        except json.JSONDecodeError as e:
            print(f"Error parsing {json_file.name}: {e}")
            continue
        except Exception as e:
            print(f"Error processing {json_file.name}: {e}")
            continue
    
    # Generate Table of Contents
    all_markdown.append("## Metadata Elements: Overview\n")
    all_markdown.append("| Property | Required? | Repeatable? | Accepted Values | Description |")
    all_markdown.append("| -------- | --------- | ----------- | --------------- | ----------- |")
    
    for entry in toc_entries:
        title_link = f"[{entry['title']}](#{entry['anchor']})"
        # Abbreviate the accepted values for TOC display
        accepted_values_display = entry['accepted_values']
        if accepted_values_display == "Multi-part element; see subfield definitions for more information.":
            accepted_values_display = "Multi-part element; see subfield"
        
        all_markdown.append(
            f"| {title_link} | {entry['required']} | {entry['repeatable']} | "
            f"{accepted_values_display} | {entry['description']} |"
        )
    
    all_markdown.append("\n---\n")

    all_markdown.append("## Metadata Elements: Detailed Information\n")
    
    # Add all schema documentation
    for schema_md in schema_markdowns:
        all_markdown.append(schema_md)
        all_markdown.append("\n---\n")
    
    # Write all markdown to a single file
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write('\n'.join(all_markdown))
    
    print(f"\nSuccessfully generated: {output_file}")
    print(f"Processed {len(json_files)} JSON files")

# Example usage
if __name__ == "__main__":
    # Specify your input folder and output file
    input_folder = "C:/icpsr_github/metadata/rde_schema/property_bank"  # Change this to your folder path
    output_file = "C:/icpsr_github/metadata/rde_schema/icpsr_rde_schema.md"
    
    # Process all JSON files in the folder
    process_json_folder(input_folder, output_file)