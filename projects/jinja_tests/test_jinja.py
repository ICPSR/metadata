import json
import datetime
import re
from bs4 import BeautifulSoup
from lxml import etree
from jinja2 import Environment, FileSystemLoader, pass_context
import os
import sys
import inspect
from html import escape as html_escape, unescape as html_unescape

templates = ['dublincore', 'dcat-us', 'marc-21', 'datacite', 'ddi', 'schema.org', 'icpsr-schema']

if len(sys.argv) < 2:
    print("\nUsage: python test_jinja.py <'dublincore', 'dcat-us', 'marc-21', 'datacite', 'ddi', 'schema.org', 'icpsr-schema'>")
    sys.exit(1)

if sys.argv[1] not in templates:
    print("\nInvalid template. Usage: python test_jinja.py <'dublincore', 'dcat-us', 'marc-21', 'datacite', 'ddi', 'schema.org', 'icpsr-schema'>")
    sys.exit(1)

# Define paths
template_dir = "C:/icpsr_github/metadata/jinja-tests"

# Determine format based on template argument
fmt = "xml" if sys.argv[1] in ['dublincore', 'marc-21', 'datacite', 'ddi'] else "json"
template_file = f"{sys.argv[1].strip()}_template.{fmt}.jinja"

json_file_path = os.path.join(template_dir, "export_request-1256-20250213T203045.json")
crosswalk_file_path = os.path.join(template_dir, "dcat-us_crosswalk.json")  # Adjust filename as needed
output_file = os.path.join(template_dir, os.path.splitext(template_file)[0].replace('template', 'test'))

# Load JSON data
with open(json_file_path, "r", encoding="utf-8") as json_file:
    data = json.load(json_file)

# Load crosswalk mappings
try:
    with open(crosswalk_file_path, "r", encoding="utf-8") as crosswalk_file:
        crosswalk_dict = json.load(crosswalk_file)
except FileNotFoundError:
    print(f"Warning: Crosswalk file not found at {crosswalk_file_path}. Proceeding without it.")
    crosswalk_dict = {}

# Extract study data (assuming single study per export)
study_key = next(iter(data))  # Get first key (e.g., "pcms_study_5512")
tree = data[study_key]

# Initialize Jinja environment
env = Environment(loader=FileSystemLoader(template_dir))

# === Register Custom Filters ===
def strip_tags(string, strip=False):
    """Strip HTML tags from a string while preserving whitespace."""
    return BeautifulSoup(html_unescape(string), "html.parser").get_text(strip=strip)

def from_iso_date(string):
    """Parse an ISO date and return a datetime object."""
    return datetime.datetime.fromisoformat(string)

def format_date(dttm, format='%Y-%m-%dT%H:%M:%S', length=None):
    """Convert a datetime to a formatted string."""
    result = dttm.strftime(format)
    length = length or len(result)
    return result[:length]

def jsonify(obj):
    """ Converts lists and strings to JSON-compliant strings. """
    if inspect.isgenerator(obj):
        return json.dumps(list(obj))
    return json.dumps(obj)

def split(string, delim='~~'):
    """Splits a string by a delimiter."""
    return string.split(delim)

def flatten_date_ranges(ranges, delimiter='/'):
    """Flatten an array of date range objects into an array of 'startDate/endDate' strings."""
    flattened = [[r.get('startDate'), r.get('endDate')] for r in ranges]
    joined = [delimiter.join(filter(None, f)) for f in flattened]
    return list(filter(None, joined))

def collapse_date_ranges(ranges, delimiter='/'):
    """Collapses an array of date range objects into a single range of the form 'minDate/maxDate'."""
    dates = [r.get('startDate') for r in ranges] + [r.get('endDate') for r in ranges]
    if dates := set(filter(None, dates)):
        return delimiter.join([min(dates), max(dates)])
    return None

def defaultattr(lst, attr, value):
    """Sets an attribute on objects in a list if the attribute is missing."""
    return [{**obj, attr: obj.get(attr, value)} for obj in lst]

# @pass_context
# def crosswalk(context, string, field):
#     """Applies a crosswalk to a field using regex or simple mappings."""
#     field = field.lower()
#     if field not in crosswalk_dict:
#         return string  # No mapping available, return original value

#     mapping_info = crosswalk_dict[field]
#     use_regex = mapping_info.get("regex", False)
#     mapping = mapping_info.get("mapping", {})

#     if use_regex:
#         for pattern, replacement in mapping.items():
#             if re.match(pattern, string, re.IGNORECASE):
#                 return replacement
#         return string  # No match found, return original value
#     else:
#         return mapping.get(string.lower(), string)  # Simple lookup

# @pass_context
# def crosswalk(context, string, field):
#     """Applies a crosswalk mapping to a field using regex or simple mappings."""
#     field = field.lower()
#     if field not in crosswalk_dict:
#         return string  # No mapping found, return original value

#     mapping_info = crosswalk_dict[field]
#     use_regex = mapping_info.get("regex", False)
#     mapping = mapping_info.get("mapping", {})

#     if not string:  # Handle empty values
#         return string

#     if use_regex:
#         for pattern, replacement in mapping.items():
#             if re.search(pattern, string, re.IGNORECASE):  # Use `search()` instead of `match()`
#                 return replacement
#         return string  # No match found, return original value
#     else:
#         return mapping.get(string.lower(), string)  # Simple lookup
@pass_context
def crosswalk(context, string, field):
    """ Applies a crosswalk to a field.

        Assumes the crosswalk is a dict available from context.parent whose keys are field names and
        whose values are dicts of the form {'regex': True/False, 'mapping': {'oldvalue1': 'newvalue1', ...}}.

        When a mapping uses regular expressions, this method will iterate over all values in the mapping
        searching for a match.  Otherwise, this method will perform a simple look-up.

        If either the field or the value is not in the crosswalk, this method returns None.
    """
    field = field.lower()
    crosswalk_dict = context.parent.get('crosswalk', {})
    mapping = crosswalk_dict.get(field, {}).get('mapping', {})
    uses_regex = crosswalk_dict.get(field, {}).get('regex', False)

    if uses_regex:
        for pattern, new_value in mapping.items():
            if re.match(pattern, string, re.IGNORECASE):
                return new_value
        return None
    return mapping.get(string.lower())

# Add filters to Jinja
env.filters["strip_tags"] = strip_tags
env.filters["from_iso_date"] = from_iso_date
env.filters["format_date"] = format_date
env.filters["crosswalk"] = crosswalk
env.filters["jsonify"] = jsonify
env.filters["split"] = split
env.filters["flatten_date_ranges"] = flatten_date_ranges
env.filters["collapse_date_ranges"] = collapse_date_ranges
env.filters["defaultattr"] = defaultattr

# Load template
template = env.get_template(template_file)

# Render template
rendered = template.render(tree=tree, crosswalk=crosswalk_dict)

# === Format XML or JSON ===
def clean_xml(xml_string):
    """Parse and pretty-print XML while removing unnecessary whitespace."""
    parser = etree.XMLParser(remove_blank_text=True)
    root = etree.fromstring(xml_string.encode(), parser)
    return etree.tostring(root, pretty_print=True, encoding="utf-8").decode()

# Clean up the output
if fmt == 'xml':
    formatted_output = clean_xml(rendered)
else:
    formatted_output = json.dumps(json.loads(rendered), indent=4)

# Save output
with open(output_file, "w", encoding="utf-8") as f:
    f.write(formatted_output)

print(f"Rendered {fmt.upper()} saved to {output_file}")
