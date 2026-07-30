import requests
import string
import pandas as pd
import sys
from pathlib import Path

#------------------------------------
# CONFIG
# Enter the path to the input file
#------------------------------------
input_file = "C:/testing/datalumos/json_metadata20260708_142430.csv"


# clean_url method cleans up the URL and makes sure it is not a Panda 'not a number' (NaN) object
def clean_url(url):
    if url is None:
        return None

    url = str(url).strip()

    if not url or url.lower() == "nan":
        return None

    # Remove trailing punctuation, but preserve trailing slashes
    trailing_punctuation = string.punctuation.replace("/", "")
    url = url.rstrip(trailing_punctuation).strip()

    return url


def check_url(url, timeout=10):
    """
    Returns:
        status_code, error_message, resolved_url

    Examples:
        200, None, "https://example.com/"
        404, "HTTP 404 Not Found", "https://example.com/missing-page"
        None, "DNS lookup failed: could not resolve api.whitehouse.gov", None
    """

    from http import HTTPStatus
    from urllib.parse import urlparse
    import requests

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

    # This method attempts to make any error message more human-readable/understandable
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

    url = clean_url(url)

    if not url:
        return None, None, None

    # Optional convenience:
    # If the value looks like a domain but is missing https://, add it.
    # Example: www.fpeckert.me/cbp -> https://www.fpeckert.me/cbp
    parsed = urlparse(url)
    if not parsed.scheme:
        first_part = url.split("/")[0]

        if "." in first_part and " " not in first_part:
            url = "https://" + url
        else:
            return None, "Invalid URL: does not look like a web address", None

    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/142.0.0.0 Safari/537.36"
        )
    }

    response = None

    try:
        response = requests.head(
            url,
            headers=headers,
            allow_redirects=True,
            timeout=timeout
        )

        # If HEAD fails or is blocked, try GET.
        # Some sites reject HEAD even when a normal browser request works.
        if response.status_code >= 400:
            response.close()

            response = requests.get(
                url,
                headers=headers,
                allow_redirects=True,
                timeout=timeout,
                stream=True
            )

        status_code = response.status_code
        resolved_url = response.url

        response.close()

        if status_code >= 400:
            return status_code, http_status_message(status_code), resolved_url

        return status_code, None, resolved_url

    except requests.exceptions.RequestException as e:
        if response is not None:
            response.close()

        return None, humanize_error(e, url), None

def main():
    in_file = Path(input_file)

    if not in_file.is_file():
        print(
            f"This script is configured to use '{in_file}' as an input, but the file does not exist on this system.",
            f"Please review the configuration section of the script and add the path to the appropriate CSV file.",
            sep="\n\n"
            )
        sys.exit(1)

    output_file = in_file.with_name(f"{in_file.stem}-UPDATED{in_file.suffix}")

    working_dict = {}

    # Load CSV
    df = pd.read_csv(input_file)

    # Add output columns
    df["statusCode"] = None
    df["errorMessage"] = None
    df["resolvedURL"] = None
    df["URLchange?"] = None
 
    # Loop through rows
    for index, row in df.iterrows():
        df.at[index, "URLchange?"] = None 
            
        raw_url = row["sourceURL"]
        url = clean_url(raw_url)

        print(f"Checking row {index + 1}: {raw_url}")

        if not url:
            continue

        if url in working_dict:
            status_code = working_dict[url]["statusCode"]
            error = working_dict[url]["errorMessage"]
            resolved_url = working_dict[url]["resolvedURL"]

        else:
            status_code, error, resolved_url = check_url(url)
            working_dict[url] = {
                "statusCode": status_code,
                "errorMessage": error,
                "resolvedURL": resolved_url
            }

        if resolved_url and resolved_url != raw_url:
            df.at[index, "URLchange?"] = "Y"

        df.at[index, "statusCode"] = status_code
        df.at[index, "errorMessage"] = error
        df.at[index, "resolvedURL"] = resolved_url

        # Optional: print only questionable/bad results
        if error or status_code != 200:
            print(f"  Status code: {status_code}")
            print(f"  Error: {error}")
            print(f"  Resolved URL: {resolved_url}")

    # Save results
    df.to_csv(output_file, index=False)

    print(f"Done. Results saved to: {output_file}")


if __name__ == "__main__":
    main()