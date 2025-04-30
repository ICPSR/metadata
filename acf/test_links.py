from lxml import etree
import requests
import sys
import os
import time
import csv

if len(sys.argv) < 3:
    print('Add the state and an xml file as arguments!')
    sys.exit(1)

state = sys.argv[1].lower().replace(' ', '_')
xml_file = sys.argv[2]
out_dir = os.path.dirname(xml_file)
bad_link_log = os.path.join(out_dir, f"{state}_bad_links.csv")

tree = etree.parse(xml_file)
root = tree.getroot()

# Extract all hyperlinks in <source> tags at various levels of hierarchy
xml_hyperlinks = set()

# Find all <source> elements at different levels of the XML hierarchy
for source in root.xpath('.//source'):
    if source.text:
        xml_hyperlinks.add(source.text.strip())

bad_links = []
for url in xml_hyperlinks:
    try:
        response = requests.get(url, timeout=10)  # 10-second timeout
        # Return True for 200 status, False otherwise
        if response.status_code != 200:
            print(f"{url} returned code {response.status_code}")
            bad_links.append(url)
        else:
            print(f"{url} is good!")

        time.sleep(1.5)

    except requests.RequestException:
        print(f"\n{url} request encountered an error: {requests.RequestException}")
        bad_links.append(url)

if len(bad_links) > 0:
    with open(bad_link_log, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Bad URL', 'Corrected URL'])
        for url in bad_links:
            writer.writerow([url, ''])

    print(f'\n\nERRORS! Please consult {bad_link_log}')

else:
    print('\n\nNo errors!')