import requests
import json
import sys
import os
import csv
import unicodedata

def clean_strings(txt):
    clean_txt = txt.strip().lower().replace(' - ', ' ').replace(' ', '+').replace('&', '%26')
    return ''.join(c for c in unicodedata.normalize('NFKD', clean_txt) if not unicodedata.combining(c))

work_dir = os.path.dirname(os.path.abspath(__file__))

org_csv = os.path.join(work_dir, 'ACTIVE_MEMBER_ORGS.csv')
org_ror_csv = os.path.join(work_dir, 'ACTIVE_MEMBER_ROR_IDs.csv')

#get info from our CSV file
with open(org_csv, mode="r", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    rows = list(reader) 

counter = 0
no_matches = []

for row in rows:
    counter += 1
    found = False

    search_string = clean_strings(row["NAME"])
    print(f'\n\nWorking on #{counter}: {row['NAME']}')

    # Define the API URL
    url = f"https://api.ror.org/v1/organizations?affiliation={search_string}" 

    # Make the API request
    response = requests.get(url)
    response.encoding = 'utf-8'

    # Check if the request was successful
    if response.status_code == 200:
        data = response.json()  # Parse JSON response

        if data['number_of_results'] > 0:
            print('\tFound results...')

            likely_match = data['items'][0]
            if likely_match['chosen'] == True:

                #try to match city/state
                if row["COUNTRY"].strip() == 'USA':
                    country = "United States"

                    if (row["STATE"].strip()s in likely_match['organization']['addresses'][0]['geonames_city']['geonames_admin1']['code']) and (country in likely_match['organization']['country']['country_name']):
                        found = True

                else:
                    country = row["COUNTRY"].strip()

                    if country.lower() in likely_match['organization']['country']['country_name'].lower():
                        found = True
        else:
            print('Found nothing!')

    else:
        print(f"Error: {response.status_code} - {response.text}")

    if found:
        print('\tMatch made!')
        row["ROR_NAME"] = likely_match['organization']['name']
        row["ROR_ID"] = likely_match['organization']['id']
    else:
        print('\tNo match...')
        row["ROR_NAME"] = ''
        row["ROR_ID"] = ''

# Get all field names (preserve existing + add 'ROR_ID')
fieldnames = list(rows[0].keys())

# Write updated data back to a new CSV file
with open(org_ror_csv, mode="w", encoding="utf-8", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)  # Write modified rows

print(f"Updated CSV saved as {org_ror_csv}")