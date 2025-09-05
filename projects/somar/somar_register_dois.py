import sys
import pandas as pd
import requests
import json
import base64
import os
from datetime import datetime

# set variables.
working_dir = os.path.dirname(os.path.abspath(__file__))
draft_dois = os.path.join(working_dir, "draft_dois.csv")
xml_dir = os.path.join(working_dir, "XML")

#check 'test' vs. 'prod'
try:
    if sys.argv[1].lower() == 'test':
        credentials = os.path.join(working_dir, "test_credentials.json")
        minted_dois = os.path.join(working_dir, "test_minted_dois.csv")
    elif sys.argv[1].lower() == 'prod':
        credentials = os.path.join(working_dir, "prod_credentials.json")
        minted_dois = os.path.join(working_dir, "minted_dois.csv")
    else:
        print('\n\nWARNING: script only accepts "prod" or "test" as first argument.')
        sys.exit(1)

except IndexError:
    print('\n\nUsage: python somar_dois.py <prod OR test> <draft or publish>')
    sys.exit(1)

#check 'draft' vs. 'publish'
try:
    if sys.argv[2].lower() == 'publish':
        event_status = 'publish'
    elif sys.argv[2].lower() == 'draft':
        event_status = ''
    else:
        print('\n\nWARNING: script only accepts "publish" or "draft" as first argument.')
        sys.exit(1)
except IndexError:
    print('\n\nUsage: python somar_dois.py <prod OR test> <draft or publish>')
    sys.exit(1)

#make sure we have our draft_dois CSV in our working dir
for fi in [credentials, draft_dois, xml_dir]:
    if not os.path.exists(fi):
        print(f'\n\nWARNING: "{fi}" does not exist. Please add and then re-run script.')
        sys.exit(1)

#read in our credential info
with open(credentials, "r") as file:
    credential_info = json.load(file)

#set auth variables
try:
    user = credential_info['user']
    password = credential_info['password']
    prefix = credential_info['prefix']
    datacite_url = credential_info['url']
except KeyError:
    print(f'\n\nWARNING: make sure that {credentials} includes "user", "password", "prefix", and "url" values.')
    sys.exit(1)

#Read in data.
somar = pd.read_csv(draft_dois)

# Clean up dataframe by removing 'Unnamed' columns
somar = somar.loc[:, ~somar.columns.str.contains('^Unnamed')]

# Set up additional columns, if needed
if 'DOI' in somar.columns and somar['DOI'].dtype != 'object':
    somar['DOI'] = somar['DOI'].astype('object')
elif 'DOI' not in somar.columns:
    somar['DOI'] = pd.Series(dtype='object')

if 'Result' not in somar.columns:
    somar['Result'] = pd.Series(dtype='object')
else:
    somar['Result'] = somar['Result'].astype("string")

#Additional vars: an empty list for suffixes and an index counter, set to 0 
new_doi_suffixes = []

# loop through the dataframe
print('Gathering info and minting DOIs...')

for index, row in somar.iterrows():

    print(f'\n - Working on {row["StudyTitle"]}')

    # skip item if it has already been added
    if pd.notna(row['Result']) and 'Success' in str(row['Result']):
        print('\tAlready added to DataCite; moving on to next item!')
        continue

    #extract the item ID from its SOMAR URL
    item_url = row['URL']
    item_id =item_url.rsplit('/', 1)[1]

    #set up our JSON data to mint the DOI
    print('\n\tMinting DOI...')
    data_content = {
        "data": {
            "type": "dois",
            "attributes": {
                "prefix": prefix,
                "titles": [
                    {
                        "title": row['StudyTitle']
                    }
                ],
                "publisher": "ICPSR - Interuniversity Consortium for Political and Social Research",
                "publicationYear": str(datetime.now().year),
                "url": item_url,
                "schemaVersion": "http://datacite.org/schema/kernel-4"
            }
        }
    }

    data = json.dumps(data_content).replace('\n', '').replace('\r', '').encode()
    headers = {
        'content-type': 'application/vnd.api+json',
    }

    response = requests.post(
        datacite_url,
        headers=headers,
        data=data,
        auth=(user, password)
    )
    
    #Check to make sure we got a successful ('201') response code.
    if str(response.status_code) == '201':
        print('\t  - DOI succeeded!')

        # assign variables: locally and in our dataframe
        item_doi = response.json()['data']['attributes']['doi']
        somar.loc[index, 'DOI'] = item_doi

    else:
        print(f'\t  - DOI failed; code {response.status_code}')
        print(f'\t  - {response.json()}')
        somar.loc[index, 'Result'] = str('Failure')
        continue

    # proceed to update the metadata for our new DataCite object
    print('\n\tUpdating metadata...')

    # First, make sure the XML file exists; if not, provide error message and move on to next item
    xml_file = os.path.join(xml_dir, row['XMLFile'])
    if not os.path.exists(xml_file):
        print(f'\t  - WARNING: {xml_file} does not exist; verify file and associated name (and update draft_dois.csv, if necessary).')
        somar.loc[index, 'Result'] = 'Failure'
        continue

    # base64 encode the XML so it can be included in our API call
    with open(xml_file, 'rb') as file:
        xml_encoded = base64.b64encode(file.read()).decode('utf-8')
        
    #create update json. Key things here: we have to pass the doi, we have to have a publish event, we have to pass the now-encoded xml.
    payload = {
        'data': {
            'type': 'dois', 
            'attributes': {
                'event': event_status, 
                'identifiers': {
                    'identifier': item_doi, 
                    'identifierType': 'DOI'
                }, 
                'doi': item_doi, 
                'xml': xml_encoded
            }
        }
    }

    #set up vars
    data = json.dumps(payload).replace('\n', '').replace('\r', '').encode()
    headers = {
        'Content-Type': 'application/vnd.api+json',
    }

    # submit API request
    response = requests.put(
        f'{datacite_url}/{item_doi}',
        headers=headers,
        data=data,
        auth=(user, password),
    )
    
    #Response code should be 200; document outcome in dataframe
    if str(response.status_code) == "200":
        print('\t  - Metadata update succeeded!')
        somar.loc[index, 'Result'] = str("Success")
    else:
        print(f'\t  - Metadata update failed; code {response.status_code}')
        print(f'\t  - {response.json()}')
        somar.loc[index, 'Result'] = str('Failure')
        continue

#Save the dataframe as a csv, for easiest copy/pasting into the google sheet. MAKE SURE TO KEEP THIS, YOU WILL NEED IT WHEN YOU UPDATE.
somar.to_csv(minted_dois, index=False)
