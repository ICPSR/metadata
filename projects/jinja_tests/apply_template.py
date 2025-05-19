""" Tasks to prepare & apply a Jinja template to a metadata tree. """
import re
import os
from os import access, R_OK
import json
import inspect
import datetime
import importlib.resources
from lxml import etree
from bs4 import BeautifulSoup
from jinja2 import Environment, pass_context, TemplateError
from html import escape as html_escape, unescape as html_unescape

from export.orm.model import MetadataFormat
from export.config import Config as server_config
from export.task.task import Task, DatabaseTask, TaskStateError
from export.logger import console_logger

log = console_logger


# === HELPERS ===

# Return pretty traceback string of Jinja2 render
_TEMPLATE_FRAME_PATTERN = re.compile(r"<frame at 0x[a-z0-9]*, file '(.*)', line (\d+), (?:code top-level template code|code template)>")
def jinja2_render_traceback(ex, src_path:str = '<template>'):
    tb = ex.__traceback__

    # Iterate over nested traceback frames
    traceback_print = ""
    while tb:
        tb_frame_match = _TEMPLATE_FRAME_PATTERN.match(str(tb.tb_frame))
        tb_frame_istemplate = False

        # Identify frames corresponding to Jinja2 templates
        if tb.tb_frame.f_code.co_filename == '<template>':
            # Top-most template
            tb_src_path = src_path
            tb_lineno = tb.tb_lineno
            tb_frame_istemplate = True
        elif tb_frame_match:
            # nested child templates
            tb_src_path = tb_frame_match.group(1)
            tb_lineno = tb_frame_match.group(2)
            tb_frame_istemplate = True

        # Factorized string formatting
        if tb_frame_istemplate:
            traceback_print += f"\n    Template {tb_src_path}:{tb_lineno}"

            # Fetch the line raising the exception
            if os.path.isfile(tb_src_path) and access(tb_src_path, R_OK):
                with open(tb_src_path,'r') as tb_src_file:
                    for file_lineno,line in enumerate(tb_src_file, start=1):
                        if file_lineno == int(tb_lineno):
                            traceback_print += "\n        "+line.strip()
                            break


        tb = tb.tb_next
    return traceback_print


# === TASK LOGIC ===

class PrepareTemplateTask(DatabaseTask):
    """ Task to prepare a Jinja template for application to a metadata tree. """

    def __init__(self, state, repo=None, template_pkg='export.template'):
        """ Initialize the task.

            Parameters:
            * state: A dictionary containing the following keys:
              - export_request: An export request instance.  Must contain a field 'format' specifying the desired
                                format URI.  That URI will be used to look up a template name in the formats_t table.
            * repo: (Optional) An instance of a repository.  If not provided, one will be created automatically.
            * template_pkg: (Optional) Name of the package from which to load template resources
        """
        super().__init__(state, repo)
        try:
            self.export_request = self.state['export_request']
            self.template_pkg = template_pkg
        except KeyError as ex:
            raise TaskStateError from ex

    def run(self):
        """ Load a template file and crosswalk corresponding to the format URI specified in the export request. """
        try:
            format_name = self._get_format_name()

            crosswalk_string, _ = self._load_template_resource(format_name, 'crosswalk')
            crosswalk_dict = self._prepare_crosswalk(crosswalk_string)

            template_string, format_type = self._load_template_resource(format_name, 'template', mandatory=True)
            template = self._create_template(template_string, crosswalk_dict)

            log.info(f'Created template for {format_name}')

            return {**self.state, 'format_name': format_name, 'format_type': format_type, 'template': template}
        except TemplateError as ex:
            log.exception(ex)
            log.error(jinja2_render_traceback(ex))
            raise TemplateError(f'An unexpected error occurred while creating the {format_name} template.') from ex

    def _get_format_name(self):
        """ Determine the format name associated with an export request format URI. """
        session = self.repo.session

        if (format_uri := self.export_request.get('format')) is None:
            raise ValueError('No metadata format URI was specified in the export request')

        format_name = session.query(MetadataFormat.format_name) \
            .filter(MetadataFormat.format_uri == format_uri) \
            .scalar()

        if format_name is None:
            raise ValueError(f'{format_uri} is not a known metadata format URI')

        return format_name

    def _load_template_resource(self, name, resource_type, mandatory=False):
        """ Loads template resources from a package. """
        format_type = None
        resource = None
        count = 0

        for file_name in importlib.resources.contents(self.template_pkg):
            if re.match(f'^{name}_{resource_type}', file_name):
                log.debug(f'Loading {resource_type} file {file_name}')
                count += 1
                if not resource: # Only read the first matching resource
                    root, extension = os.path.splitext(file_name)
                    format_type = (os.path.splitext(root)[1] if extension == '.jinja' else extension)[1:]
                    resource = importlib.resources.read_text(self.template_pkg, file_name)

        if count > 1 or (mandatory and count == 0):
            raise ValueError(f"Package {self.template_pkg} contains {count} {resource_type}s for format '{name}'")

        return resource, format_type

    @staticmethod
    def _create_template(template_string, crosswalk_dict):
        """ Create a Jinja template from a template string and a crosswalk. """
        env = Environment()
        for name, obj in globals().items():
            if hasattr(obj, 'is_custom_filter'):
                env.filters[name] = obj
        env.globals['crosswalk'] = crosswalk_dict
        return env.from_string(template_string)

    @staticmethod
    def _prepare_crosswalk(crosswalk_string):
        """ Load the crosswalk string to a dict, validate its format, and make the crosswalk case-insensitive.
            Note, this method does not lowercase regex-based mappings; instead, case-insensitive matching is used
            when the crosswalk is applied via the crosswalk() Jinja filter defined below.
        """
        try:
            crosswalk_dict = {}
            for field, rule in json.loads(crosswalk_string or '{}').items():
                regex = rule['regex']
                mapping = rule['mapping'] if regex else {k.lower(): v for k,v in rule['mapping'].items()}
                crosswalk_dict[field.lower()] = {'regex': regex, 'mapping': mapping}
            return crosswalk_dict
        except json.decoder.JSONDecodeError as ex:
            raise ValueError('Metadata template crosswalk is not a valid JSON file.') from ex
        except KeyError as ex:
            raise ValueError('Metadata template crosswalk does not conform to the expected schema.') from ex


class ApplyTemplateTask(Task):
    """ Task to apply a Jinja template to a metadata tree. """

    def __init__(self, state):
        """ Initialize the task.

            Parameters:
            * state: A dictionary containing the following keys:
              - template: A jinja template to use in rendering a metadata tree
              - format_name: The format name (e.g., dcat-us or marc-21)
              - format_type: The format type (e.g., json or xml)
              - tree: Metadata tree to which template should be applied
        """
        super().__init__(state)
        try:
            self.template = self.state['template']
            self.format_name = self.state['format_name']
            self.format_type = self.state['format_type']

            # PREFILTER TREE TO ESCAPE CHARACTERS
            if self.format_type == 'xml':
                self.tree = _clean_tree(self.state['tree'], html_escape, quote=True)
            else:
                self.tree = self.state['tree']

            self.tree['static_path'] = server_config.static_path()
        except KeyError as ex:
            raise TaskStateError from ex

    def run(self):
        """ Apply the template to a metadata tree. """
        try:
            # Apply the template
            content = self.template.render(tree=self.tree)

            # Prettify the result
            noop = lambda x: x
            prettifier = getattr(self, f'_prettify_{self.format_type}', noop)
            content = prettifier(content)

            return {**self.state, 'content': content}
        except TemplateError as ex:
            log.debug("METADATA TREE DUMP:\n" + json.dumps(self.tree))
            log.exception(ex)
            log.error(jinja2_render_traceback(ex))
            raise TemplateError(f'An unexpected error occurred while processing the {self.format_name} template.') from ex

    @staticmethod
    def _prettify_json(content):
        """ Prettify a JSON string. """
        try:
            return json.dumps(json.loads(content), indent=4)
        except Exception as ex:
            raise ValueError('Unable to prettify JSON.  Content may be malformed.') from ex

    @staticmethod
    def _prettify_xml(content):
        """ Prettify an XML string. """
        try:
            parser = etree.XMLParser(remove_blank_text=True)
            return etree.tostring(etree.fromstring(content, parser), pretty_print=True, encoding=str)
        except Exception as ex:
            raise ValueError('Unable to prettify XML.  Content may be malformed.') from ex

def _clean_tree(data, replace_function: callable, *replace_args, **replace_kwargs):
    """
    Recursive function to filter the deeply-nested strings in a complex data structure.

    Args:
        data: The data structure to be cleaned. It can be a dictionary, a list, a string, or any other type.
        replace_function: A callable function that takes a string and optional arguments and returns a new string.
        *replace_args: Additional positional arguments to be passed to the replace_function.
        **replace_kwargs: Additional keyword arguments to be passed to the replace_function.

    Returns:
        A new data structure where all strings have been processed by the replace_function.
    """

    if isinstance(data, dict):
        return {key: _clean_tree(value, replace_function, *replace_args, **replace_kwargs) for key, value in data.items()}
    elif isinstance(data, list):
        return [_clean_tree(item, replace_function, *replace_args, **replace_kwargs) for item in data]
    elif isinstance(data, str):
        return replace_function(data, *replace_args, **replace_kwargs)
    else:
        return data


#
# Custom Jinja Filters
#
def custom_filter(func):
    """ Decorator to mark functions as custom filters. """
    func.is_custom_filter = True
    return func

@custom_filter
def jsonify(obj):
    """ Converts lists and strings to JSON-compliant strings. """
    if inspect.isgenerator(obj):
        return json.dumps(list(obj))
    return json.dumps(obj)

@custom_filter
def split(string, delim='~~'):
    """ Splits a string by a delimiter. """
    return string.split(delim)

@custom_filter
def strip_tags(string, strip=False):
    """ Strip HTML tags from a string.
        Note: There is a built-in jinja filter named 'striptags', but that filter also
        removes adjacent whitespace, which is not desired for this application.
    """
    string = html_unescape(string)
    return BeautifulSoup(string, 'html.parser').get_text(strip=strip)

@custom_filter
def from_iso_date(string):
    """ Parse an ISO date and return a datetime object. """
    return datetime.datetime.fromisoformat(string)

@custom_filter
def format_date(dttm, format='%Y-%m-%dT%H:%M:%S', length=None):
    """ Convert a datetime to a MARC-formatted datetime string. """
    result = dttm.strftime(format)
    length = length or len(result)
    return result[:length]

@custom_filter
def flatten_date_ranges(ranges, delimiter='/'):
    """ Flatten an array of date range objects into an array of 'startDate/endDate' strings. """
    flattened = [[r.get('startDate'), r.get('endDate')] for r in ranges]
    joined = [delimiter.join(filter(None, f)) for f in flattened]
    return list(filter(None, joined))

@custom_filter
def collapse_date_ranges(ranges, delimiter='/'):
    """ Collapses an array of date range objects into a single range of the form 'minDate/maxDate'.
        Assumes dates are ISO formatted so that min and max methods have the expected effect.
    """
    dates = [r.get('startDate') for r in ranges] + [r.get('endDate') for r in ranges]
    if dates := set(filter(None, dates)):
        return delimiter.join([min(dates), max(dates)])
    return None

@custom_filter
def defaultattr(lst, attr, value):
    """ For each object in a list, sets an attribute on that object to a default value if the attribute is not already set. """
    return [ {**obj, attr: obj.get(attr, value)} for obj in lst ]

@custom_filter
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


