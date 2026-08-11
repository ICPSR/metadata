import json
import re
import string
import sys
from html import unescape
from http import HTTPStatus
from pathlib import Path
from urllib.parse import urlparse
from datetime import datetime
import pandas as pd
import requests
from bs4 import BeautifulSoup
from rapidfuzz import fuzz
from playwright.sync_api import sync_playwright


# ------------------------------------
# CONFIG
# ------------------------------------
input_file = "C:/testing/datalumos/json_metadata20260708_142430.csv"
timeout = 10
max_html_bytes = 2_000_000
playwright_timeout = 30000


# ------------------------------------
# GENERAL HELPERS
# ------------------------------------

def clean_url(url):
    if url is None:
        return None

    try:
        if pd.isna(url):
            return None
    except Exception:
        pass

    url = str(url).strip()

    if not url or url.lower() == "nan":
        return None

    trailing_punctuation = string.punctuation.replace("/", "")
    url = url.rstrip(trailing_punctuation).strip()

    return url or None


def prepare_url(url):
    url = clean_url(url)

    if not url:
        return None, None

    parsed = urlparse(url)

    if parsed.scheme:
        return url, None

    first_part = url.split("/")[0]

    if "." in first_part and " " not in first_part:
        return "https://" + url, None

    return None, "Invalid URL: does not look like a web address"


def clean_text(value):
    if value is None:
        return None

    try:
        if pd.isna(value):
            return None
    except Exception:
        pass

    if isinstance(value, list):
        value = " ".join(str(v) for v in value)

    value = str(value).strip()

    if not value or value.lower() == "nan":
        return None

    return " ".join(value.split())


def normalize_for_match(value):
    value = clean_text(unescape(str(value)))

    if not value:
        return ""

    return value.casefold()


def as_list(value):
    if value is None:
        return []

    if isinstance(value, list):
        return value

    return [value]


def get_key_case_insensitive(obj, *possible_keys):
    if not isinstance(obj, dict):
        return None

    wanted = {key.lower() for key in possible_keys}

    for key, value in obj.items():
        if key.lower() in wanted:
            return value

    return None


def get_headers():
    return {
        "User-Agent": "Mozilla/5.0",
        "Accept-Language": "en-US,en;q=0.9",
    }


def get_host(value):
    try:
        return urlparse(value).hostname or "the host"
    except Exception:
        return "the host"


def http_status_message(status_code):

    try:
        return f"HTTP {status_code} {HTTPStatus(status_code).phrase}"
    except ValueError:
        return f"HTTP {status_code}"


def humanize_error(exc, checked_url):
    host = get_host(checked_url)
    msg = str(exc)
    msg_lower = msg.lower()

    if isinstance(exc, requests.exceptions.MissingSchema):
        return "Invalid URL: missing http:// or https://"

    if isinstance(exc, requests.exceptions.InvalidSchema):
        return "Invalid URL: unsupported URL scheme"

    if isinstance(exc, requests.exceptions.InvalidURL):
        return "Invalid URL"

    if isinstance(exc, requests.exceptions.TooManyRedirects):
        return f"Too many redirects while trying to reach {host}"

    if isinstance(exc, requests.exceptions.SSLError):
        if "hostname mismatch" in msg_lower:
            return f"SSL certificate error: certificate hostname does not match {host}"
        if "certificate verify failed" in msg_lower:
            return f"SSL certificate verification failed for {host}"
        return f"SSL error while connecting to {host}"

    if isinstance(exc, requests.exceptions.ConnectTimeout):
        return f"Connection timed out: could not connect to {host} within {timeout} seconds"

    if isinstance(exc, requests.exceptions.ReadTimeout):
        return f"Read timed out: {host} connected but did not respond within {timeout} seconds"

    if isinstance(exc, requests.exceptions.Timeout):
        return f"Request timed out while trying to reach {host} within {timeout} seconds"

    if isinstance(exc, requests.exceptions.ConnectionError):
        if (
            "failed to resolve" in msg_lower
            or "nameresolutionerror" in msg_lower
            or "getaddrinfo failed" in msg_lower
        ):
            return f"DNS lookup failed: could not resolve {host}"

        if "connection refused" in msg_lower:
            return f"Connection refused by {host}"

        if "connect timeout" in msg_lower or "timed out" in msg_lower:
            return f"Connection timed out: could not reach {host} within {timeout} seconds"

        if "max retries exceeded" in msg_lower:
            return f"Connection failed: could not reach {host}"

        return f"Connection error while trying to reach {host}"

    return f"Request failed while trying to reach {host}"


def get_response_encoding(response):
    """
    Avoid response.apparent_encoding because it may consume the full streamed body.
    """

    if response.encoding:
        return response.encoding

    content_type = response.headers.get("Content-Type", "")

    match = re.search(r"charset=([^;]+)", content_type, flags=re.IGNORECASE)

    if match:
        return match.group(1).strip()

    return "utf-8"


def decode_response_bytes(response, data):
    encoding = get_response_encoding(response)
    return data.decode(encoding, errors="replace")


# ------------------------------------
# URL STATUS CHECK
# ------------------------------------

def check_url(url):
    """
    Returns:
        status_code, error_message, resolved_url
    """

    url, prep_error = prepare_url(url)

    if prep_error:
        return None, prep_error, None

    if not url:
        return None, None, None

    attempts = [
        ("headers", get_headers()),
        ("plain", None),
    ]

    last_status_code = None
    last_resolved_url = None
    last_error_message = None

    for label, headers in attempts:
        try:
            kwargs = {
                "allow_redirects": True,
                "timeout": timeout,
                "stream": True,
            }

            if headers is not None:
                kwargs["headers"] = headers

            with requests.get(url, **kwargs) as response:
                status_code = response.status_code
                resolved_url = response.url

                last_status_code = status_code
                last_resolved_url = resolved_url

                if status_code < 400:
                    return status_code, None, resolved_url

                last_error_message = http_status_message(status_code)

        except requests.exceptions.RequestException as e:
            last_status_code = None
            last_resolved_url = None
            last_error_message = humanize_error(e, url)

    return last_status_code, last_error_message, last_resolved_url


# ------------------------------------
# FILE RESOURCE DETECTION
# ------------------------------------

def get_url_extension(url):
    try:
        path = urlparse(url).path
        return Path(path).suffix.lower()
    except Exception:
        return None


def classify_file_resource(response, resolved_url):
    """
    Identifies resources that appear to be files rather than HTML pages.

    Returns:
        file_type, reason

    If not a file:
        None, None
    """

    file_extensions = {
        ".zip": "ZIP archive",
        ".pdf": "PDF",
        ".xlsx": "Excel workbook",
        ".xls": "Excel spreadsheet",
        ".csv": "CSV file",
        ".tsv": "TSV file",
        ".json": "JSON file",
        ".xml": "XML file",
        ".txt": "text file",
        ".sav": "SPSS file",
        ".dta": "Stata file",
        ".sas7bdat": "SAS data file"
    }

    content_types = {
        "application/pdf": "PDF",
        "application/zip": "ZIP archive",
        "application/x-zip-compressed": "ZIP archive",
        "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet": "Excel workbook",
        "application/vnd.ms-excel": "Excel spreadsheet",
        "text/csv": "CSV file",
        "text/tab-separated-values": "TSV file",
        "application/json": "JSON file",
        "application/xml": "XML file",
        "text/xml": "XML file",
        "application/octet-stream": "downloadable file"
    }

    extension = get_url_extension(resolved_url)

    if extension in file_extensions:
        return file_extensions[extension], f"file extension {extension}"

    content_type = response.headers.get("Content-Type", "")
    content_type = content_type.split(";")[0].strip().lower()

    if content_type in content_types:
        return content_types[content_type], f"Content-Type {content_type}"

    content_disposition = response.headers.get("Content-Disposition", "").lower()

    if "attachment" in content_disposition:
        return "downloadable file", "Content-Disposition attachment"

    return None, None


# ------------------------------------
# EXACT TITLE MATCHING
# ------------------------------------

def build_title_search_terms(project_title):
    """
    Builds search terms from projectTitle.

    If the title contains ':', the whole title and each colon-separated part
    are searched.

    Example:
        "Population Data: County-Level Estimates"

    Produces:
        whole = "Population Data: County-Level Estimates"
        part1 = "Population Data"
        part2 = "County-Level Estimates"
    """

    title = clean_text(project_title)

    if not title:
        return []

    terms = []
    seen = set()

    def add_term(label, text):
        text = clean_text(text)

        if not text:
            return

        normalized = normalize_for_match(text)

        if not normalized or normalized in seen:
            return

        seen.add(normalized)

        terms.append({
            "label": label,
            "text": text,
            "normalized": normalized
        })

    add_term("whole", title)

    if ":" in title:
        parts = title.split(":")

        for i, part in enumerate(parts, start=1):
            add_term(f"part{i}", part)

    return terms


def text_contains_term(text, normalized_term):
    return normalized_term in normalize_for_match(text)


def find_first_match_for_term(soup, term):
    """
    Finds the first useful text snippet where a search term appears.
    Returns only the matched snippet.
    """

    normalized_term = term["normalized"]

    # Check meta content first.
    for meta in soup.find_all("meta"):
        content = meta.get("content")

        if content and text_contains_term(content, normalized_term):
            return clean_text(content)

    preferred_tags = [
        "title",
        "h1",
        "h2",
        "h3",
        "h4",
        "caption",
        "th",
        "td",
        "tr",
        "p",
        "li",
        "a",
        "span",
        "div"
    ]

    for tag_name in preferred_tags:
        for tag in soup.find_all(tag_name):
            text = tag.get_text(" ", strip=True)

            if text and text_contains_term(text, normalized_term):
                return clean_text(text)

    excluded_tags = {
        "html",
        "head",
        "body",
        "script",
        "style",
        "noscript"
    }

    for tag in soup.find_all(True):
        if tag.name in excluded_tags:
            continue

        text = tag.get_text(" ", strip=True)

        if text and text_contains_term(text, normalized_term):
            return clean_text(text)

    return None


def find_title_matches(html, terms, existing_matches=None):
    """
    Finds the first matched snippet for each whole/subtitle term.

    Returns:
        {
            "whole": "Matched snippet",
            "part1": "Matched snippet",
            "part2": "Matched snippet"
        }
    """

    matches = dict(existing_matches or {})

    if not terms:
        return matches

    soup = BeautifulSoup(html, "html.parser")

    for noisy in soup.find_all(["script", "style", "noscript"]):
        noisy.decompose()

    for term in terms:
        label = term["label"]

        if label in matches:
            continue

        snippet = find_first_match_for_term(soup, term)

        if snippet:
            matches[label] = snippet

    return matches


def format_title_match_details(matches):
    if not matches:
        return None

    snippets = []
    seen = set()

    for label, snippet in matches.items():
        snippet = clean_text(snippet)

        if not snippet:
            continue

        if len(snippet) > 250:
            snippet = snippet[:247] + "..."

        if snippet not in seen:
            seen.add(snippet)
            snippets.append(snippet)

    if not snippets:
        return None

    return json.dumps(snippets, ensure_ascii=False)


# ------------------------------------
# FALLBACK PAGE TITLE EXTRACTION
# ------------------------------------
def walk_jsonld(value):
    if isinstance(value, dict):
        yield value

        for child in value.values():
            yield from walk_jsonld(child)

    elif isinstance(value, list):
        for item in value:
            yield from walk_jsonld(item)


def type_matches(node_types, target):
    target = target.lower()

    for value in node_types:
        value = str(value).lower()

        if (
            value == target
            or value.endswith(":" + target)
            or value.endswith("/" + target)
            or value.endswith("#" + target)
        ):
            return True

    return False


def extract_schema_org_title(html):
    """
    Attempts to get a page/dataset title from schema.org JSON-LD.
    Prefers Dataset-like objects, then falls back to any JSON-LD name/headline/title.
    """

    soup = BeautifulSoup(html, "html.parser")

    scripts = soup.find_all(
        "script",
        attrs={"type": lambda value: value and "ld+json" in value.lower()}
    )

    fallback_name = None

    for script in scripts:
        raw = script.string or script.get_text()

        if not raw or not raw.strip():
            continue

        try:
            data = json.loads(raw)
        except json.JSONDecodeError:
            continue

        for node in walk_jsonld(data):
            if not isinstance(node, dict):
                continue

            node_type = get_key_case_insensitive(node, "@type")
            node_types = {str(t).lower() for t in as_list(node_type)}

            name = get_key_case_insensitive(
                node,
                "name",
                "headline",
                "title"
            )

            name = clean_text(name)

            if not name:
                continue

            is_dataset_like = (
                type_matches(node_types, "Dataset")
                or get_key_case_insensitive(node, "distribution") is not None
            )

            if is_dataset_like:
                return name

            if not fallback_name:
                fallback_name = name

    return fallback_name


def extract_meta_or_html_title(html):
    """
    Falls back to common title fields in the HTML head, then <title>.
    """

    soup = BeautifulSoup(html, "html.parser")

    title_fields = {
        "dc.title",
        "dcterms.title",
        "dcterms:title",
        "citation_title",
        "og:title",
        "twitter:title"
    }

    for meta in soup.find_all("meta"):
        key = meta.get("name") or meta.get("property")
        content = meta.get("content")

        if not key or not content:
            continue

        if key.lower() in title_fields:
            return clean_text(content)

    if soup.title:
        return clean_text(soup.title.get_text(" ", strip=True))

    return None


def extract_fallback_page_title(html):
    """
    Fallback order:
        1. schema.org JSON-LD name/headline/title
        2. dc.title/dcterms.title/etc.
        3. <title>
    """

    schema_title = extract_schema_org_title(html)

    if schema_title:
        return schema_title

    html_title = extract_meta_or_html_title(html)

    if html_title:
        return html_title

    return None


# ------------------------------------
# FUZZY TITLE MATCHING
# ------------------------------------

def normalize_title_for_fuzzy(value):
    """
    Normalizes titles for fuzzy comparison.
    """

    value = clean_text(value)

    if not value:
        return ""

    value = value.casefold()

    # Replace punctuation with spaces.
    value = re.sub(r"[^\w\s]", " ", value)

    # Collapse whitespace.
    value = " ".join(value.split())

    return value

def remove_leading_year_range(value):
    """
    Removes leading year/date-range language.

    Example:
        "2013 to 2016 Picture of Subsidized Housing Data"
        -> "Picture of Subsidized Housing Data"
    """

    value = clean_text(value)

    if not value:
        return ""

    patterns = [
        r"^\d{4}\s+to\s+\d{4}\s+",
        r"^\d{4}\s*-\s*\d{4}\s+",
        r"^\d{4}\s*–\s*\d{4}\s+",
        r"^\d{4}\s*—\s*\d{4}\s+",
    ]

    for pattern in patterns:
        value = re.sub(pattern, "", value, flags=re.IGNORECASE)

    return clean_text(value) or ""

def get_meaningful_tokens(value):
    """
    Returns a set of meaningful tokens for overlap checks.

    Removes very common/generic webpage/title words so that a shared word like
    "data" does not cause an overly confident match.

    Keeps short meaningful tokens like roman numerals, e.g. "ii", because those
    may matter in titles such as "Title II Reports".
    """

    value = normalize_title_for_fuzzy(value)

    if not value:
        return set()

    generic_tokens = {
        "a",
        "an",
        "and",
        "are",
        "as",
        "at",
        "by",
        "for",
        "from",
        "in",
        "into",
        "is",
        "of",
        "on",
        "or",
        "the",
        "to",
        "with",

        # Generic web/data portal terms.
        "data",
        "dataset",
        "datasets",
        "open",
        "portal",
        "catalog",
        "catalogue",
        "home",
        "page",
        "website",
        "site",
        "search",
        "results",
        "welcome"
    }

    tokens = set(value.split())

    return {
        token
        for token in tokens
        if token not in generic_tokens and len(token) > 1
    }
    
def fuzzy_compare_titles(project_title, page_title):
    """
    Compares projectTitle against pageTitle.

    Returns:
        score

    Logic:
        - Avoids partial_token_set_ratio(), which can over-score tiny overlaps.
        - Allows strong overlap across the project title to score highly.
        - Allows short but meaningful phrase overlap, such as "Title II",
          but caps it below a perfect 100.
        - Tiny/generic overlap, such as only "data", should not produce
          an artificially high score.
    """

    if not project_title or not page_title:
        return None

    project_variants = [
        project_title,
        remove_leading_year_range(project_title)
    ]

    page_variants = [
        page_title
    ]

    best_score = 0

    for project_variant in project_variants:
        project_norm = normalize_title_for_fuzzy(project_variant)

        if not project_norm:
            continue

        for page_variant in page_variants:
            page_norm = normalize_title_for_fuzzy(page_variant)

            if not page_norm:
                continue

            project_tokens = get_meaningful_tokens(project_norm)
            page_tokens = get_meaningful_tokens(page_norm)

            shared_tokens = project_tokens & page_tokens
            shared_count = len(shared_tokens)

            if project_tokens:
                project_coverage = shared_count / len(project_tokens)
            else:
                project_coverage = 0

            if page_tokens:
                page_coverage = shared_count / len(page_tokens)
            else:
                page_coverage = 0

            conservative_scores = [
                fuzz.ratio(project_norm, page_norm),
                fuzz.token_sort_ratio(project_norm, page_norm),
            ]

            current_score = max(conservative_scores)

            token_set_score = fuzz.token_set_ratio(project_norm, page_norm)

            if project_coverage >= 0.5:
                # Enough of the project title overlaps that token_set_ratio is safe.
                current_score = max(current_score, token_set_score)

            elif shared_count >= 2 and page_coverage >= 0.8:
                # Short but meaningful page title is mostly contained in the project title.
                # Example:
                #   projectTitle = "US Department of Education Title II Reports"
                #   pageTitle    = "Title II - Welcome"
                #
                # This deserves a meaningful score, but not a perfect 100.
                current_score = max(current_score, min(token_set_score, 84.0))

            if current_score > best_score:
                best_score = current_score

    return round(best_score, 1)


# ------------------------------------
# PLAYWRIGHT FALLBACK TITLE EXTRACTION
# ------------------------------------

def extract_playwright_page_title(url):
    """
    Uses Playwright as a final fallback to get the rendered page title.

    This is useful for more dynamic pages where requests/BeautifulSoup cannot
    find a useful title because content is populated by JavaScript.

    Returns:
        page title string, or None
    """

    if sync_playwright is None:
        return None

    browser = None

    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            page = browser.new_page()

            page.goto(
                url,
                wait_until="domcontentloaded",
                timeout=playwright_timeout
            )

            title = clean_text(page.title())

            browser.close()
            browser = None

            return title

    except Exception:
        return None

    finally:
        if browser is not None:
            try:
                browser.close()
            except Exception:
                pass


# ------------------------------------
# PAGE INSPECTION
# ------------------------------------

def inspect_fetched_page_for_title(page_info, resolved_url, project_title):
    """
    Performs projectTitle-specific inspection using already-fetched page_info.

    This avoids re-downloading the same URL for every row.
    """

    result = {
        "resourceType": page_info.get("resourceType"),
        "matchedProjectTitle": "N",
        "titleMatchDetails": None,
        "pageTitle": None,
        "fuzzyTitleMatchScore": None
    }

    if page_info.get("resourceType") != "web page":
        return result

    html = page_info.get("html") or ""
    terms = build_title_search_terms(project_title)

    matches = find_title_matches(html, terms)

    if matches:
        result["matchedProjectTitle"] = "Y"
        result["titleMatchDetails"] = format_title_match_details(matches)
        return result

    fallback_title = page_info.get("staticPageTitle")

    if not fallback_title:
        if "playwrightPageTitle" not in page_info:
            page_info["playwrightPageTitle"] = extract_playwright_page_title(
                resolved_url
            )

        fallback_title = page_info.get("playwrightPageTitle")

    result["pageTitle"] = fallback_title

    if fallback_title:
        fuzzy_score = fuzzy_compare_titles(
            project_title,
            fallback_title
        )

        result["fuzzyTitleMatchScore"] = fuzzy_score

    return result

def fetch_page_resource_once(resolved_url):
    """
    Fetches a URL once and returns URL-level page/resource information.

    This does not do projectTitle-specific matching.

    Returns:
        {
            "resourceType": None / "web page" / file type,
            "html": "...",
            "staticPageTitle": None / title from schema/meta/<title>,
            "playwrightPageTitle": optional cached Playwright title
        }
    """

    page_info = {
        "resourceType": None,
        "html": "",
        "staticPageTitle": None
    }

    response = None
    data = bytearray()

    try:
        response = requests.get(
            resolved_url,
            headers=get_headers(),
            allow_redirects=True,
            timeout=timeout,
            stream=True
        )

        if response.status_code >= 400:
            return page_info

        file_type, file_reason = classify_file_resource(response, response.url)

        if file_type:
            page_info["resourceType"] = file_type
            return page_info

        page_info["resourceType"] = "web page"

        for chunk in response.iter_content(chunk_size=65_536):
            if not chunk:
                continue

            data.extend(chunk)

            if len(data) > max_html_bytes:
                data = data[:max_html_bytes]
                break

        html = decode_response_bytes(response, data) if data else ""

        page_info["html"] = html
        page_info["staticPageTitle"] = extract_fallback_page_title(html)

        return page_info

    except requests.exceptions.RequestException:
        return page_info

    finally:
        if response is not None:
            response.close()

def inspect_page_for_title(resolved_url, project_title):
    """
    Streams up to max_html_bytes from the resolved URL.

    If the resource appears to be a file, skips title inspection.

    Otherwise:
        1. Attempts exact matching against projectTitle and colon-separated substrings.
        2. If no exact match, extracts fallback pageTitle.
    """

    result = {
        "resourceType": None,
        "matchedProjectTitle": "N",
        "titleMatchDetails": None,
        "pageTitle": None,
        "fuzzyTitleMatchScore": None
    }

    terms = build_title_search_terms(project_title)

    response = None
    data = bytearray()
    matches = {}

    try:
        response = requests.get(
            resolved_url,
            headers=get_headers(),
            allow_redirects=True,
            timeout=timeout,
            stream=True
        )

        if response.status_code >= 400:
            return result

        file_type, file_reason = classify_file_resource(response, response.url)

        if file_type:
            result["resourceType"] = file_type
            return result

        result["resourceType"] = "web page"

        for chunk in response.iter_content(chunk_size=65_536):
            if not chunk:
                continue

            data.extend(chunk)

            if len(data) > max_html_bytes:
                data = data[:max_html_bytes]

            html = decode_response_bytes(response, data)

            if terms:
                matches = find_title_matches(
                    html,
                    terms,
                    existing_matches=matches
                )

                # Stop once every generated term has a first match.
                if len(matches) == len(terms):
                    break

            if len(data) >= max_html_bytes:
                break

    except requests.exceptions.RequestException:
        return result

    finally:
        if response is not None:
            response.close()

    html = decode_response_bytes(response, data) if data else ""

    if matches:
        result["matchedProjectTitle"] = "Y"
        result["titleMatchDetails"] = format_title_match_details(matches)
        return result

    fallback_title = extract_fallback_page_title(html)

    if not fallback_title:
        fallback_title = extract_playwright_page_title(resolved_url)

    result["pageTitle"] = fallback_title

    if fallback_title:
        fuzzy_score = fuzzy_compare_titles(
            project_title,
            fallback_title
        )

        result["fuzzyTitleMatchScore"] = fuzzy_score

    return result

# ------------------------------------
# MAIN
# ------------------------------------

def main():
    in_file = Path(input_file)

    if not in_file.is_file():
        print(
            f"This script is configured to use '{in_file}' as an input, but the file does not exist on this system.",
            "Please review the configuration section of the script and add the path to the appropriate CSV file.",
            sep="\n\n"
        )
        sys.exit(1)

    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    output_file = in_file.with_name(f"{in_file.stem}-UPDATED-{timestamp}{in_file.suffix}")

    df = pd.read_csv(input_file, encoding="utf-8-sig")
    df.columns = df.columns.str.strip()

    required_columns = {"sourceURL", "projectTitle"}
    missing_columns = required_columns - set(df.columns)

    if missing_columns:
        print(
            "This script expects the input CSV to contain these columns:",
            ", ".join(sorted(required_columns)),
            "",
            "Missing column(s):",
            ", ".join(sorted(missing_columns)),
            sep="\n"
        )
        sys.exit(1)

    output_columns = [
        "statusCode",
        "errorMessage",
        "resolvedURL",
        "URLchange?",
        "resourceType",
        "matchedProjectTitle",
        "titleMatchDetails",
        "fuzzyTitleMatchScore",
        "pageTitle"      
    ]

    for col in output_columns:
        df[col] = None

    status_cache = {}
    inspection_cache = {}

    df["_cleanSourceURL"] = df["sourceURL"].apply(clean_url)

    status_cache = {}

    grouped_df = df[df["_cleanSourceURL"].notna()].sort_values(
        "_cleanSourceURL",
        kind="stable"
    )

    for cleaned_url, group in grouped_df.groupby("_cleanSourceURL", sort=False):
        first_raw_url = group.iloc[0]["sourceURL"]

        print(
            f"Checking sourceURL group with {len(group)} row(s): {first_raw_url}"
        )

        if cleaned_url in status_cache:
            status_code, error_message, resolved_url = status_cache[cleaned_url]
        else:
            status_code, error_message, resolved_url = check_url(cleaned_url)
            status_cache[cleaned_url] = status_code, error_message, resolved_url

        page_info = None

        if status_code == 200 and resolved_url:
            page_info = fetch_page_resource_once(resolved_url)

        count = 0
        for index, row in group.iterrows():
            count += 1
            project_title = clean_text(row["projectTitle"])

            print(f"\nRow {count}: '{project_title}'")

            result = {
                "statusCode": status_code,
                "errorMessage": error_message,
                "resolvedURL": resolved_url,
                "URLchange?": None,
                "resourceType": None,
                "matchedProjectTitle": "N",
                "titleMatchDetails": None,
                "fuzzyTitleMatchScore": None,
                "pageTitle": None
            }

            if resolved_url and resolved_url != cleaned_url:
                result["URLchange?"] = "Y"

            if status_code == 200 and resolved_url and page_info is not None:
                title_result = inspect_fetched_page_for_title(
                    page_info,
                    resolved_url,
                    project_title
                )

                result.update(title_result)

            for col in output_columns:
                df.at[index, col] = result[col]

    df = df.drop(columns=["_cleanSourceURL"])
    df.to_csv(output_file, index=False, encoding="utf-8-sig")

    print(f"\nDone. Results saved to: {output_file}")


if __name__ == "__main__":
    main()