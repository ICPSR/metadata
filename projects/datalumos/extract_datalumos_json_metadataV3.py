import json
import sys
from pathlib import Path
from datetime import datetime, UTC
import csv

# ----------------------------------------------------------------------
# DataLumos JSON Metadata Extractor
#
# Purpose:
#   Extract selected metadata from one JSON file or a folder of JSON files
#   and write the results to a CSV spreadsheet.
#
# Usage Example:
#   python extract_datalumos_json_metadata.py <path_to_json_file_or_folder>
#
# ----------------------------------------------------------------------

# ----------------------------------------------------------------------
# USER CONFIGURATION
#   1. Add/remove top-level JSON fields in FIELDS
#   2. Add/remove nested study-level metadata fields in ATTRIBUTE_FIELDS (use the machine-readable "attribute" value.)
#   3. Identify any fields that use UNIX time stamps
#   3. Modify date formatting 
#   4. Change the character used to delimit metadata values presented as a list/array.
# ----------------------------------------------------------------------

FIELDS = [
    "projectTitle",
    "doi",
    "dateCreated",
    "creators"
]

ATTRIBUTE_FIELDS = [
    "sourceURL",
    "keyword"
]

UNIX_DATE_FIELDS = [
    "dateCreated"
]

DATE_FORMAT = "%Y-%m-%d"

LIST_DELIMITER = "|"

# ----------------------------------------------------------------------
# EXTRACT NESTED ATTRIBUTE VALUES
# This method will recursively search for a target_attribute -- e.g.:
#         {
#             "attribute": target_attribute,
#             "resourceProperty": {
#                 "value": ...
#             }
#         }
#     and return the value.
# It accommodates both dictionaries and lists.
# ----------------------------------------------------------------------

def find_attribute_value(obj, target_attribute):

    if isinstance(obj, dict):

        if (
            obj.get("attribute") == target_attribute
            and isinstance(obj.get("resourceProperty"), dict)
        ):
            return obj["resourceProperty"].get("value")

        for value in obj.values():
            result = find_attribute_value(value, target_attribute)
            if result is not None:
                return result

    elif isinstance(obj, list):

        for item in obj:
            result = find_attribute_value(item, target_attribute)
            if result is not None:
                return result

    return None

def find_version_value(data, target_label, target_field):
    """
    Find a version object with the requested versionLabel and return
    the requested field from that object.

    For example:
        find_version_value(data, "V1", "versionDate")
    """

    versions = data.get("versions", [])

    if not isinstance(versions, list):
        return None

    for version in versions:
        if not isinstance(version, dict):
            continue

        version_label = version.get("versionLabel")

        if (
            isinstance(version_label, str)
            and version_label.strip().casefold() == target_label.casefold()
        ):
            return version.get(target_field)

    return None

def main():

    # ----------------------------------------------------------------------
    # VALIDATE INPUT PATH
    # This script expects either the path for a JSON file or a folder of JSON files. 
    # If there is any space in the path, it must be enclosed in quotation marks.
    # If no path is provided, the script will immediately exit
    # ----------------------------------------------------------------------

    if len(sys.argv) != 2:
        print("Usage:")
        print("  python C:/Users/jkubale/Documents/GitHub/DL_metadata_py/extract_datalumos_json_metadata.py C:/Users/jkubale/Documents/GitHub/DL_metadata_py/data")
        sys.exit(1)

    input_path = Path(sys.argv[1])

    # ----------------------------------------------------------------------
    # DISCOVER JSON FILES / SET OUTPUT PATH
    # The target file(s) are made into a list and assigned to the json_files variable
    # If the path was entered incorrectly, the script exits with an error message.
    # The input_path will also be used to set the path for the output file.
    # ----------------------------------------------------------------------

    if input_path.is_file():
        json_files = [input_path]
    elif input_path.is_dir():
        json_files = sorted(input_path.glob("*.json"))
    else:
        print(f"ERROR: {input_path} does not exist")
        sys.exit(1)

    output_dir = input_path if input_path.is_dir() else input_path.parent
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_file = output_dir / f"json_metadata{timestamp}.csv"

    # ----------------------------------------------------------------------
    # EXTRACT METADATA FROM EACH FILE
    # The script will:
    #    1. Create an empty list to hold information parsed from the JSON file(s)
    #    2. Use a for loop to iterate through the target JSON file(s)
    #    3. Provide a status update on the job progress
    #    4. Extract values for the FIELDS and ATTRIBUTE_FIELDS as defined in the config section
    #    5. Add extracted values to the main list
    #
    # Each file is wrapped in a try/except block so that:
    #    - Files with missing attributes are included with empty cells and a warning
    #    - Files that are malformed or unreadable are skipped with an error message
    #    - All successfully parsed files are written to the output CSV
    # ----------------------------------------------------------------------

    rows = []

    file_count = len(json_files)
    counter = 0
   
    for json_file in json_files:

        counter += 1
        print(f"Working on {json_file} ({counter} of {file_count})")

        try:
            with open(json_file, "r", encoding="utf-8") as f:
                data = json.load(f)

            row = {"FILE": json_file.name}

            for field in FIELDS:

                if field == "dateCreated":
                    version_date = find_version_value(
                        data,
                        target_label="V1",
                        target_field="versionDate"
                    )

                    if version_date is None:
                        top_level_date = data.get("dateCreated")

                        if top_level_date is not None:
                            row[field] = top_level_date
                        else:
                            print(
                                f"  WARNING: neither versionDate for versionLabel 'V1' "
                                f"nor top-level 'dateCreated' was found in {json_file.name}"
                            )
                            row[field] = ""
                    else:
                        row[field] = version_date

                else:
                    row[field] = data.get(field, "")

            for attr in ATTRIBUTE_FIELDS:
                raw_value = find_attribute_value(data, attr)

                if raw_value is None:
                    print(f"  WARNING: attribute '{attr}' not found in {json_file.name}")
                    row[attr] = []
                elif isinstance(raw_value, list):
                    row[attr] = raw_value
                else:
                    row[attr] = raw_value.split('~~')

            rows.append(row)

        except Exception as e:
            print(f"  ERROR processing {json_file.name}: {e}")

    # ----------------------------------------------------------------------
    # NORMALIZE EXTRACTED VALUES
    # This step will:
    #   1. Convert UNIX timestamps to ISO 8601 dates (using the DATE_FORMAT defined in the config section)
    #   2. Delimit metadata values that are lists (using the LIST_DELIMITER defined in the config section)
    # ---------------------------------------------------------------------- 

    output_rows = []

    for row in rows:
        clean_row = {}

        for k, v in row.items():

            if isinstance(v, list):
                clean_row[k] = LIST_DELIMITER.join(x for x in v if x)
            
            elif k in UNIX_DATE_FIELDS and v:
                clean_row[k] = datetime.fromtimestamp(v/1000, UTC).strftime(DATE_FORMAT)
            
            else:
                clean_row[k] = v
            
            # Uncomment the following line to print extracted values to console
            # print(f"{k}:\t\t{clean_row[k]}")

        output_rows.append(clean_row)

    # ----------------------------------------------------------------------
    # WRITE OUTPUT TO FILE
    # If no files were successfully processed, the script exits with an error.
    # Otherwise, the output is written to a CSV file and a success message is printed.
    # ----------------------------------------------------------------------

    if not output_rows:
        print("ERROR: No data was successfully extracted. No output file written.")
        sys.exit(1)

    with open(output_file, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=output_rows[0].keys())
        writer.writeheader()
        writer.writerows(output_rows)

    print(f"\nDone. Output written to: {output_file}")

if __name__ == "__main__":
    main()