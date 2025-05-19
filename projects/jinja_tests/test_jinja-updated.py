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

templates = ['dublincore', 'dcat-us', 'marc-21']

if len(sys.argv) < 2:
    print("\nUsage: python test_jinja.py <'dublincore', 'dcat-us', 'marc-21'>")
    sys.exit(1)

if sys.argv[1] not in templates:
    print("\nInvalid template. Usage: python test_jinja.py <'dublincore', 'dcat-us', 'marc-21'>")
    sys.exit(1)

# Define paths
template_dir = "C:/icpsr_github/metadata/jinja-tests"

# Determine format based on template argument
if sys.argv[1] in ['dublincore', 'marc-21']:
    fmt = 'xml'
else:
    fmt = 'json'

template_file = f"{sys.argv[1].strip()}_template.{fmt}.jinja"

json_file_path = os.path.join(template_dir, "export_request-1255-20250213T193911.json")
output_file = os.path.join(template_dir, os.path.splitext(template_file)[0].replace('template', 'test'))

# Load JSON data
with open(json_file_path, "r", encoding="utf-8") as json_file:
    data = json.load(json_file)

# Extract study data (assuming single study per export)
study_key = next(iter(data))  # Get first key (e.g., "pcms_study_5512")
tree = data[study_key]

# Initialize Jinja environment
env = Environment(loader=FileSystemLoader(template_dir))

# === Register Custom Filters ===
def strip_tags(string, strip=False):
    """Strip HTML tags from a string while preserving whitespace."""
    string = html_unescape(string)
    return BeautifulSoup(string, "html.parser").get_text(strip=strip)

def from_iso_date(string):
    """Parse an ISO date and return a datetime object."""
    return datetime.datetime.fromisoformat(string)

def format_date(dttm, format='%Y-%m-%dT%H:%M:%S', length=None):
    """ Convert a datetime to a MARC-formatted datetime string. """
    result = dttm.strftime(format)
    length = length or len(result)
    return result[:length]

def jsonify(obj):
    """ Converts lists and strings to JSON-compliant strings. """
    if inspect.isgenerator(obj):
        return json.dumps(list(obj))
    return json.dumps(obj)

def split(string, delim='~~'):
    """ Splits a string by a delimiter. """
    return string.split(delim)

def flatten_date_ranges(ranges, delimiter='/'):
    """ Flatten an array of date range objects into an array of 'startDate/endDate' strings. """
    flattened = [[r.get('startDate'), r.get('endDate')] for r in ranges]
    joined = [delimiter.join(filter(None, f)) for f in flattened]
    return list(filter(None, joined))

def collapse_date_ranges(ranges, delimiter='/'):
    """ Collapses an array of date range objects into a single range of the form 'minDate/maxDate'."""
    dates = [r.get('startDate') for r in ranges] + [r.get('endDate') for r in ranges]
    if dates := set(filter(None, dates)):
        return delimiter.join([min(dates), max(dates)])
    return None

def defaultattr(lst, attr, value):
    """ For each object in a list, sets an attribute on that object to a default value if the attribute is not already set. """
    return [{**obj, attr: obj.get(attr, value)} for obj in lst]

@pass_context
def crosswalk(context, string, field):
    """Applies a crosswalk to a field (dummy implementation)."""
    return string  # Replace with actual logic if needed

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
rendered = template.render(tree=tree)

# === Format XML or JSON ===
def clean_xml(xml_string):
    """Parse and pretty-print XML while removing unnecessary whitespace."""
    parser = etree.XMLParser(remove_blank_text=True)
    root = etree.fromstring(xml_string.encode(), parser)
    return etree.tostring(root, pretty_print=True, encoding="utf-8").decode()

# Clean up the XML or JSON output
if fmt == 'xml':
    formatted_output = clean_xml(rendered)
else:
    formatted_output = json.dumps(json.loads(rendered), indent=4)

# Save output
with open(output_file, "w", encoding="utf-8") as f:
    f.write(formatted_output)

print(f"Rendered {fmt.upper()} saved to {output_file}")
