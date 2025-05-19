import os
from lxml import etree
import sys

try:
    if os.path.exists(sys.argv[1]) and os.path.isdir(sys.argv[1]):
        working_dir = sys.argv[1]
    else:
        print('\n\nEnter the full path to the working directory.')
        sys.exit(1)

except IndexError:
    print('\n\nUsage: python pretty_print_xml.py <path/to/working_dir>')
    sys.exit(1)

# Define input and output directories
input_dir = os.path.join(working_dir, 'unprocessed')
output_dir = os.path.join(working_dir, 'processed')

# Ensure output directory exists
os.makedirs(output_dir, exist_ok=True)

# Loop through XML files in the input directory
for filename in os.listdir(input_dir):
    if filename.lower().endswith('.xml'):
        input_path = os.path.join(input_dir, filename)
        output_path = os.path.join(output_dir, filename)

        try:
            # Parse and pretty-print
            parser = etree.XMLParser(remove_blank_text=True)
            tree = etree.parse(input_path, parser)
            tree.write(output_path, pretty_print=True, encoding='UTF-8', xml_declaration=True)
            print(f"Processed: {filename}")
        except Exception as e:
            print(f"Failed to process {filename}: {e}")
