#!/usr/bin/python3
""" Dereferences $ref elements in schema files, replacing the $ref with the contents
    of the referenced schema file. Then generates and cleans up a markdown file

    Assumptions:
    1. $ref elements point only to YAML files.
    2. Every YAML file has a $schema element identifying the file as a JSON Schema.
    3. Every YAML file has an $id element that can serve as the target of any $ref.
"""
import os
import sys
import json
import yaml
import logging
import argparse
import subprocess
import datetime
import shutil
import re

from glob import glob
from urllib.parse import urlparse, parse_qs

logging.basicConfig(format='%(levelname)s: %(message)s', level=logging.INFO)
log = logging.getLogger()

def get_cli_arguments():
    """ Parse command line arguments and return an object whose members contain the argument values. """
    parser = argparse.ArgumentParser(description="Generate markdown from JSON Schema and YAML files")
    parser.add_argument('--source-dir', dest='source_dir', type=str, help='Source directory', required=True)
    return parser.parse_args()

def load_cache(root_dir):
    """ Walks the file system from root_dir and loads any RDE schema files into a dict
        keyed by the $id of the schema.
    """
    cache = {} 
    schema_files = glob(os.path.join(root_dir, 'schema', '*.json'), recursive=True)
    yaml_files  = glob(os.path.join(root_dir, 'schema', 'yaml', '*.yaml'), recursive=True)

    for file_name in schema_files + yaml_files:
        try:
            with open(file_name, "r", encoding="utf-8") as f:
                if ".json" in file_name:
                    content = json.load(f)
                elif ".yaml" in file_name:
                    content = yaml.safe_load(f)
                    if content.get('usageNotes'):
                        content['usageNotes'] = content['usageNotes'].replace('\n', '  \n')
                    if content.get('curatorNotes'):
                        content['curatorNotes'] = content['curatorNotes'].replace('\n', '  \n')

            if '$schema' in content: # Use presence of $schema attribute to identify JSON Schema files
                log.debug(f"Loading {file_name} into schema cache")
                if (ident := content['$id']) not in cache:
                    cache[ident] = content
                else:
                    raise ValueError(f"Schema file {file_name} uses an $id value ({ident}) that is already in use by another schema")
        except KeyError as ex:
            raise KeyError(f"Schema file {file_name} does not contain an $id field") from ex
    return cache

def dereference_cache(cache): 
    """ Deferences $ref values in the cache. """
    for key, schema in cache.items():
        log.debug(f"Dereferencing $ref values in schema: {key}")
        cache[key] = resolve(schema, cache)
    return cache

def resolve(obj, cache):
    """ Recursively deferences $ref values in a schema. """
    if isinstance(obj, dict):
        new = {}
        for key, value in obj.items():
            if key == "$ref":
                try:
                    result = resolve(cache[value], cache)
                    new = {**new, **result} # Assumes that $ref always points to a dict
                except KeyError as ex:
                    raise KeyError(f"Cannot find {value} in the schema cache")
            elif key == "oneOf":
                continue
            else:
                new[key] = resolve(value, cache)
        return new
    elif isinstance(obj, list):
        return [resolve(item, cache) for item in obj]
    else:
        return obj

def persist_cache(cache, temp_dir):
    """ Persist cache to temp_dir """
    for key, schema in cache.items():
        if (title := schema.get('title')) is not None:
            # path_components = urlparse(key).path.split('/')
            # file_path = os.path.join(*path_components[1:]) # Remove first element, which is the base URI template
            file_name = os.path.join(temp_dir, 'icpsr_study_schema.json')
            os.makedirs(os.path.dirname(file_name), exist_ok=True)

            log.debug(f"Writing {title} schema to {file_name}")

            with open(file_name, 'w', encoding='utf-8') as fp:
                json.dump(schema, fp, indent=4)

        elif 'yaml' not in key:
            raise ValueError(f"Cannot persist schema because it does not contain a title element: {key}")

    return file_name

def clean_label(label):

    return label.replace('_', ' ').title().replace("To", "to").replace("Of", "of").replace("Id", "ID").replace("Doi", "Digital Object Identifier (DOI)").replace("IDentifier", "Identifier").replace("Sda ", "SDA ").replace(" Url", " URL")

def check_write(line, fo, processed_lines, index="foo"):
    if isinstance(index, int):
        if index not in processed_lines:
            #write line to file-out (fo)
            fo.write(line)

            #add index to list
            processed_lines.append(index)

        else:
            pass

        return processed_lines

    else:
        fo.write(line)

def fix_arrays(term, content):
    found_targets = found_targets = []
    index = 0  # Initialize the index

    while index < len(content):
        # Check if the line contains 'term'
        if term in content[index]: 
            # Search for 'autogenerated_heading item' after the current index
            for next_index in range(index + 1, len(content)):
                if all(keyword in content[next_index] for keyword in ('autogenerated_heading', 'items')):
                    found_targets.append(next_index)  # Store the index of the target line
                    break  # Exit the inner loop once you've found the target
            # Move the index to the next line
            index += 1
            # If both keywords were found, add the current index too

        else:
            # Move to the next line
            index += 1

    if term in ['**Type**: `array of enum (of string)`', '**Type**: `array of string`']:
        for val in found_targets:
            for i in range(4):
                content[val+i] = 'SKIP\n'

    elif term in ['**Type**: `array of object`']:
        for val in found_targets:
            content[val] = content[val].replace(' items', ' Subfields:')
            content[val+2] = 'SKIP\n'
            content[val+3] = 'SKIP\n'

    return content

def clean_data_type(data_type):
    if 'string' in data_type:
        new_data_type = ' Text'
    elif 'integer' in data_type:
        new_data_type = ' Number'
    elif 'object' in data_type:
        new_data_type = ' Multi-part; see subfields'
    else:
        new_data_type = data_type

    substring_to_replace = data_type.rstrip()

    # Calculate the length of the original substring
    original_length = len(substring_to_replace)

    # Create the replacement string
    adjusted_replacement = new_data_type + ' ' * (original_length - len(new_data_type))

    # Replace the original substring with the adjusted replacement string
    result_string = data_type.replace(substring_to_replace, adjusted_replacement)

    return result_string

def get_schema_description(source_dir):
    # Specify the path to your JSON file
    json_file_path = os.path.join(source_dir, 'schema', 'icpsr_study_schema.json')

    # Open and parse the JSON file
    with open(json_file_path, 'r') as json_file:
        data = json.load(json_file)

    # Access the value of the first 'description' key
    description_value = data.get('description')

    return description_value

def main():
    """ Main entrypoint. """
    # source_dir == the main project directory. Must contain a 'schema' folder
    try:
        args = get_cli_arguments()

        if not os.path.exists(args.source_dir):
            print(f"{args.source_dir} does not exist. Please verify path and try again")
            sys.exit(1)

        #set up variables
        site_dir = os.path.join(args.source_dir, 'site')
        markdown_dir = os.path.join(args.source_dir, 'markdown')
        resource_dir = os.path.join(args.source_dir, 'resources')
        temp_dir = os.path.join(args.source_dir, 'temp')
        mkdocs_yml = os.path.join(resource_dir, 'mkdocs.yml')
        rtd_css = os.path.join(resource_dir, 'readthedocs_theme.css')
        metadata_key = os.path.join(resource_dir, 'key.md')
        
        for folder in [temp_dir, site_dir, markdown_dir]:
            if not os.path.exists(folder):
                os.makedirs(folder)
        
        #produce a dereferenced json file
        print("\tProducing cache...")
        cache = dereference_cache(load_cache(args.source_dir))
        print("\tSaving temp file...")
        dereferenced_file = persist_cache(cache, temp_dir)

        #remove extra $id and $schema values
        print("\tRemoving extra $id and $schema values...")
        with open(dereferenced_file, "r", encoding="utf-8") as f:
            content = json.load(f)

        #remove additional $id and $schema entries
        for k, v in content.items():
            for key, value in content['properties'].items():
                content['properties'][key].pop('$id', None)
                content['properties'][key].pop('$schema', None)
            
        #write back to dereferenced json
        with open(dereferenced_file, "w", encoding="utf-8") as f:
            json.dump(content, f, indent=4)
            
        #generate markdown using modified version of JSON Schema for Humans
        print("\tCreating markdown...")
        md_file = os.path.join(markdown_dir, "icpsr_study_schema.md")

        cmd = "generate-schema-doc --config custom_template_path={} --config show_toc=false --config show_breadcrumbs=false {} {}".format(os.path.join(resource_dir, 'template', 'base.md'), dereferenced_file, md_file)

        subprocess.run(cmd, shell=True, text=True)

        #now read in all our schema markdown to make final improvements 
        print("\tFixing labels...")
        with open(md_file, 'r', encoding='utf-8') as fi:
            content=fi.readlines()

        #update schema description to include date
        current_date=datetime.datetime.now()
        content.insert(2, "Last updated: {}\n\n".format(current_date.strftime('%B %d, %Y')))

        #fix array references
        for term in ['**Type**: `array of enum (of string)`', '**Type**: `array of string`', '**Type**: `array of object`']:
            content = fix_arrays(term, content)

        #set variables
        property_dict = {}
        pattern = r'\[([^\]]+)\]\(#([^\)]+)\)'
        anchor_pattern = r'#+\s*<a name="([^"]+)">'
        processed_lines = []
        description_value = get_schema_description(args.source_dir)
        first_heading = True
        example_count = 0

        #loop through content and fix various issues
        with open(md_file, 'w', encoding='utf-8') as fo:
            for index, line in enumerate(content):
                #need to insert 

                #build dict of components; look for markdown tables that include property definitions
                if line.startswith('| [') and line.count('|') == 6:
                    #split on pipe; [1]=label/anchor, [2]=required?, [3]=repeatable, [4]=data type
                    parts = line.split('|')
                    match = re.search(pattern, parts[1])
                    if match:
                        orig_label = match.group(1)
                        cleaned_label = clean_label(orig_label.strip())
                        prop_name = match.group(2).strip()
                        
                        #create a dictionary entry; use the property name as key and manditoriness as value (yes/no)
                        property_dict[prop_name] = {"mandatory": parts[2].strip(), "repeatable": parts[3].strip(), "data_type": parts[4], "orig_label": orig_label, "cleaned_label": cleaned_label}

                        #clean up data types
                        new_data_type = clean_data_type(property_dict[prop_name]['data_type'])

                        line = line.replace(f'[{orig_label}]', f'[{cleaned_label}]').replace(property_dict[prop_name]['data_type'], new_data_type)
                        processed_lines = check_write(line, fo, processed_lines, index)
                        
                elif "##" in line and "<a name=" in line:
                    #reset our example_count variable--we need to see if there are multiple 'Example' sections under any one heading
                    example_count = 0

                    #if this is the first ## heading, we need to insert our metadata record key
                    if first_heading:

                        with open(metadata_key, 'r', encoding='utf-8') as fi:
                            key_content = fi.readlines()

                        for info in key_content:
                            check_write(info, fo, processed_lines)

                        check_write('\n## Metadata Elements: Detailed Information\n\n', fo, processed_lines)

                        #change our flag so we don't add the key again!
                        first_heading = False

                    #get the name of the current element, for later use with subfield example heading, if needed
                    if line.startswith("## "):
                        current_element = line.split('.')[-1].strip()

                    #verify if line matches our anchor pattern; this means it will be a heading, with an anchor link
                    match = re.search(anchor_pattern, line)
                    if match:
                        name_attr_value = match.group(1)
                        if "autogenerated_heading" in name_attr_value:

                            line = '#' + line
                            processed_lines = check_write(line, fo, processed_lines, index)

                        elif property_dict.get(name_attr_value):
                            entry = property_dict[name_attr_value]
                            text = line.split('</a>')
                            text[1] = text[1].replace(entry['orig_label'], entry['cleaned_label']).replace('[optional]', '').replace('[required]', '')
                            anchor_line = '</a>'.join(text)

                            #we will add an extra '#' to headings
                            anchor_line = '#' + anchor_line

                            processed_lines = check_write(anchor_line, fo, processed_lines, index)
                            check_write("\n", fo, processed_lines)

                            # We are going to assume that there is a description associated with every property; skip 2 index spaces to write description
                            description_line = content[index+2]
                            processed_lines = check_write(description_line, fo, processed_lines, index+2)

                            #account for newline after description
                            processed_lines = check_write("\n", fo, processed_lines, index+3)

                            #add required? statement
                            check_write(f"**Required**: {entry['mandatory']}\n\n", fo, processed_lines)

                            #add repeatable? statement
                            check_write(f"**Repeatable**: {entry['repeatable']}\n", fo, processed_lines)

                            #If this is a main element, get name for later use with subfield example heading, if needed
                            if line.startswith("## "):
                                current_element = entry['cleaned_label']

                elif line.startswith("**Type**"):
                    data_type = line.split(':')[1].strip().replace('`', '')

                    #check for specific format_type rules
                    format_type = ''
                    if content[index+2].startswith("**Format**:"):
                        format_type = content[index+2].split(':')[1].strip().replace('`', '').replace('uri', 'URL')

                        #add format line and following new line to processed_lines
                        processed_lines.extend([index+2, index+3])

                    if 'string' in data_type:
                        accepted_value = 'Text'
                        if len(format_type) > 0:
                            accepted_value += f" (formatted as a {format_type})"
                    elif 'integer' in data_type:
                        accepted_value = 'Number'
                    elif 'object' in data_type:
                        accepted_value = 'Multi-part element; see subfield definitions for more information.'

                    processed_lines = check_write(f"**Accepted Values**: {accepted_value}\n", fo, processed_lines, index)

                elif '**Additional properties**: [[Not allowed]](# "Additional Properties not allowed.")' in line:
                    processed_lines.append(index)
                    processed_lines.append(index+1)

                elif line.startswith('SKIP'):
                    processed_lines.append(index)

                elif description_value in line:
                    processed_lines = check_write(line, fo, processed_lines, index)
                    processed_lines = check_write('\n', fo, processed_lines, index+1)
                    check_write('For a machine-actionable copy of this information, please see the [JSON Schema version](https://github.com/ICPSR/metadata/blob/main/schema/icpsr_study_schema.json).\n\n## Metadata Elements: Overview\n\n', fo, processed_lines)

                #check to see if this is the second 'example' in a given section--if so, change the heading so that it's clear this is a full example with all subfields 
                elif line.startswith('**Example'):
                    #Add one to our example count
                    example_count += 1
                    #if our count is now at 2 it means we have consecutive 'Example' sections under one heading. Adjust the label. If count is at one, just write the line to file-out.
                    if example_count > 1:
                        processed_lines = check_write(f'###### Complete {current_element} Examples (with Subfields):', fo, processed_lines, index)
                    else:
                        processed_lines = check_write(line, fo, processed_lines, index)

                else:
                    processed_lines = check_write(line, fo, processed_lines, index)

            #now let's add our version history; first insert a blank line
            fo.write('\n')
            version_history_file = os.path.join(markdown_dir, "version_history.md")
            with open(version_history_file, 'r', encoding='utf-8') as f:
                version_lines = f.readlines()

                for v in version_lines:
                    fo.write(v)
            
        #remove temp folder
        print("\n\nRemoving temp folder...")
        shutil.rmtree(temp_dir, ignore_errors=True)
        print("\nAll done!")

    except Exception as ex: # pylint: disable=broad-except
        log.error(ex)
        sys.exit(1)

if __name__=='__main__':
    main()
