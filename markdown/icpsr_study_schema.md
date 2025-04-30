# ICPSR Metadata Schema

Last updated: April 11, 2025

This is the metadata schema used to describe data collections at the Inter-university Consortium for Political and Social Research (ICPSR). These rules and definitions represent ICPSR's metadata practices and are intended to (a) assist ICPSR staff with metadata entry, and (b) help ICPSR users -- including data depositors and researchers accessing data -- understand how to use and interpret our metadata.

For a machine-actionable copy of this information, please see the [JSON Schema version](https://github.com/ICPSR/metadata/blob/main/schema/icpsr_study_schema.json).

## Metadata Elements: Overview

| Property                                               | Required? | Repeatable? | Accepted Values           | Description                                                                                                                                                                                           |
| ------------------------------------------------------ | --------- | ----------- | ------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Version](#version )                                   | Yes       | No          | Number                    | The current version number for the data collection.                                                                                                                                                   |
| [Version Date](#version_date )                         | Yes       | No          | Text                      | The date on which the current version of the data collection was released by ICPSR.                                                                                                                   |
| [Original Release Date](#original_release_date )       | No        | No          | Text                      | The date on which the data collection was originally released by ICPSR.                                                                                                                               |
| [Title](#title )                                       | Yes       | No          | Text                      | The official title that describes what the data collection is about, its geographic scope, and the time period it covered.                                                                            |
| [Alternate Title](#alternate_title )                   | No        | Yes         | Text                      | The alternate name(s) or acronym(s) commonly used to refer to the data collection.                                                                                                                    |
| [Link Title](#link_title )                             | No        | No          | Text                      | The title of an external resource that is included in the ICPSR catalog as a courtesy to users.                                                                                                       |
| [Link URL](#link_url )                                 | No        | No          | Text                      | The URL of an external resource that is included in the ICPSR catalog as a courtesy to users.                                                                                                         |
| [Principal Investigator](#principal_investigator )     | Yes       | Yes         | Multi-part; see subfields           | The key people or organizations responsible for the data collection, listed by importance. Each data collection requires at least one PI, either a person or an organization.                         |
| [Citation](#citation )                                 | No        | No          | Text                      | The official way to reference the data collection in writing.                                                                                                                                         |
| [Distributor](#distributor )                           | Yes       | Yes         | Multi-part; see subfields           | The organization(s) responsible for distributing the data collection.                                                                                                                                 |
| [Study Number](#study_number )                         | Yes       | No          | Number                    | A unique, numerical value used by ICPSR to identify and track data collections.                                                                                                                       |
| [Digital Object Identifier (DOI)](#doi )                                           | No        | No          | Text                      | The registered persistent digital object identifier (DOI) associated with the data collection.                                                                                                        |
| [Funding Source](#funding_source )                     | No        | Yes         | Multi-part; see subfields           | The sources of funding that supported the data collection.                                                                                                                                            |
| [External Source ID](#external_source_ID )             | No        | Yes         | Text                      | A unique identifier supplied by the data depositor.                                                                                                                                                   |
| [Summary](#summary )                                   | Yes       | No          | Text                      | A description of the data collection that helps users understand its purpose, substance, and key topics.                                                                                              |
| [Subject Term](#subject_term )                         | Yes       | Yes         | Text                      | A controlled list of social science terms maintained by ICPSR and used to indicate topics related to the data collection.                                                                             |
| [Geographic Coverage Area](#geographic_coverage_area ) | Yes       | Yes         | Text                      | The geographic locations where the data refer or are related.                                                                                                                                         |
| [Time Period](#time_period )                           | Yes       | Yes         | Multi-part; see subfields           | The time period(s) to which the data refer, regardless of when the data were collected.                                                                                                               |
| [Collection Date](#collection_date )                   | No        | Yes         | Multi-part; see subfields           | The date(s) when the data were physically collected.                                                                                                                                                  |
| [Universe](#universe )                                 | No        | No          | Text                      | The total group of persons or other entities (e.g., households or organizations) that were the object of research and to which analytic results refer.                                                |
| [Data Type](#data_type )                               | No        | Yes         | Text                      | The types of data included in the data collection.                                                                                                                                                    |
| [Collection Note](#collection_note )                   | No        | Yes         | Text                      | Important details about the data collection (like unique authoring, discrepencies, or processing information) that can't be recorded in other metadata elements.                                      |
| [Study Purpose](#study_purpose )                       | No        | No          | Text                      | The study's main goals and associated research questions.                                                                                                                                             |
| [Study Design](#study_design )                         | No        | No          | Text                      | The procedures used to contact participants and gather data.                                                                                                                                          |
| [Variable Description](#variable_description )         | No        | No          | Text                      | Significant variables (particularly demographic variables) in the publicly released data files.                                                                                                       |
| [Sampling](#sampling )                                 | No        | No          | Text                      | The methods used to select the subset of the population that data are to be collected from (e.g., simple, systematic, stratified).                                                                    |
| [Time Method](#time_method )                           | No        | Yes         | Text                      | The methods used to collect data over time, like snapshots at one point (cross-sectional) or repeatedly (longitudinal) to study changes or trends.                                                    |
| [Data Source](#data_source )                           | No        | Yes         | Text                      | The source of the data, when that source is external to the data collection and can be independently cited.                                                                                           |
| [Collection Mode](#collection_mode )                   | No        | Yes         | Text                      | The method(s) or procedure(s) used to collect the data.                                                                                                                                               |
| [Extent of Processing](#extent_of_processing )         | No        | Yes         | Text                      | Processing activities and checks performed on the data collection by ICPSR curation staff.                                                                                                            |
| [Weight](#weight )                                     | No        | No          | Text                      | The weight variables and the criteria for using them in data analysis or other information about how the data are weighted if no weight variables are present.                                        |
| [Response Rates](#response_rates )                     | No        | No          | Text                      | The percentage of respondents in the sample who participated in the data collection.                                                                                                                  |
| [Scale](#scale )                                       | No        | No          | Text                      | Any commonly known scales used to collect data for the data collection (e.g., MMPI, CPI, the Census Occupational Codes, etc.).                                                                        |
| [Unit of Observation](#unit_of_observation )           | No        | Yes         | Text                      | The object(s) of analysis for the data collection, such as an organization, individual, or household.                                                                                                 |
| [Smallest Geographic Unit](#smallest_geographic_unit ) | No        | No          | Text                      | The smallest geographic unit (e.g., state or census tract) used in the dataset.                                                                                                                       |
| [Restrictions](#restrictions )                         | No        | No          | Text                      | Rules about how the data collection can be accessed or used.                                                                                                                                          |
| [Membership Required](#membership_required )           | No        | No          | boolean                                      | The availability of the data collection in terms of ICPSR membership. Members-only data may only be downloaded by affiliates of ICPSR member institutions who contribute funding to support the data. |
| [Restricted Access](#restricted_access )               | No        | No          | boolean                                      | General indication of any access restrictions associated with the data collection. More detailed information is provided in the Restrictions element.                                                 |
| [Changes to Collection](#changes_to_collection )       | No        | Yes         | Multi-part; see subfields           | A record of how the data collection has changed over time.                                                                                                                                            |
| [Series](#series )                                     | No        | No          | Text                      | A named collection of related studies.                                                                                                                                                                |
| [Classification](#classification )                     | No        | Yes         | Text                      | Topics used to organize data collections and help users explore the ICPSR catalog.                                                                                                                    |
| [Filesets](#filesets )                                 | No        | Yes         | Multi-part; see subfields           | The grouping of files in the data collection.                                                                                                                                                         |

## Key for Metadata Element Entries

Full information for each ICPSR study metadata element includes the following fields:

- **Description:** A short description of the metadata element and the information it is intended to convey.
- **Required:** Indicates whether the metadata element is mandatory ("Yes") or optional ("No"). Required elements must include at least one value.
- **Repeatable:** Indicates whether the metadata element may be repeated ("Yes") or if it may only occur once ("No").
- **Accepted values:** The type of values that may be used with the metadata element; options include text (with additional requirements, such as date formatting, noted when present) and numbers. Multi-part metadata elements have accepted value information provided in entries for individual subelements.
- **Controlled Vocabulary:** Indicates the specific controlled vocabulary (i.e., a set of standardized terms) that must be used to provide values for the metadata element ('N/A' indicates no controlled vocabulary is required). 
- **Usage Notes:** Additional information about the nature, scope, and conventions for values that may be added to the metadata element.  
- **ICPSR Input Guidance:** Information for ICPSR staff related to using internal tools and resources to create and input metadata values. These notes are made available to the general ICPSR community for transparency.  
- **Examples:** Examples of valid values for the metadata element.
 
## Metadata Elements: Detailed Information

### <a name="version"></a>1. Version         

**Description:** The current version number for the data collection.

**Required**: Yes

**Repeatable**: No

**Accepted Values**: Number

**Controlled Vocabulary:** N/A

**Usage Notes:** Version numbers are integers without leading zeros. Versioning begins when a data collection is first archived. Each subsequent update of the data collection increments the version number by 1. The version number is incremented when modifying or adding:  

  * Data files, including additions of datasets or supplemental data files, additional masking, increasing curation level, or resupplied datasets  
  * Documentation files  
  * SDA (Survey Documentation and Analysis) files  

Metadata-only updates to the data collection do not increment the version number. Changes to the version number require a textual summary to be added to Changes to Collection.  

**Examples:** 

```json
1
```

```json
2
```

### <a name="version_date"></a>2. Version Date         

**Description:** The date on which the current version of the data collection was released by ICPSR.

**Required**: Yes

**Repeatable**: No

**Accepted Values**: Text (formatted as a date)

**Controlled Vocabulary:** N/A

**Usage Notes:** ICPSR automatically generates this date for data collection additions and updates. For metadata-only updates, the date remains unchanged.

**Examples:** 

```json
"2006-03-30"
```

```json
"2019-05-05"
```

### <a name="original_release_date"></a>3. Original Release Date         

**Description:** The date on which the data collection was originally released by ICPSR.

**Required**: No

**Repeatable**: No

**Accepted Values**: Text (formatted as a date)

**Controlled Vocabulary:** N/A

**Usage Notes:** ICPSR automatically generates the release date.

**Examples:** 

```json
"2001-02-07"
```

```json
"2020-08-12"
```

### <a name="title"></a>4. Title         

**Description:** The official title that describes what the data collection is about, its geographic scope, and the time period it covered.

**Required**: Yes

**Repeatable**: No

**Accepted Values**: Text

**Controlled Vocabulary:** N/A

**Usage Notes:** The Title includes three essential parts: the title proper, the geography, and the time period.  

Title Proper:  

  * The title proper is a descriptive string that captures what the data collection contains.   

  * The title proper uses title case: all major words are capitalized, while minor words are lowercased.  

  * For new studies, ICPSR starts with the title proper provided by the data depositor. Most title propers are straightforward about their contents, such as the 'American Community Survey' or the 'Census of Law Enforcement Training Academies.' Some title propers include a more branded description, such as 'Bridge of Faith: Aim4Peace Community-Based Violence Prevention Project or Contents' and 'Contexts of Cyberbullying: An Epidemiologic Study using Electronic Detection and Social Network Analysis.'  

  * For updated studies, ICPSR uses the existing title in production, making changes as necessary to add new years or additional geographical locations. For studies that are part of an ICPSR series, titles remain consistent with the previous series studies.  

Geography:  

  * All titles include the data collection's geography. If the geography is already included in the title proper, it is not repeated.  

  * Cities are paired with state or province names that are spelled out (e.g., Portland, Oregon), unless the city names are unique or well-known.  

  * Studies with more than four geographic locations typically are summarized using, for example, '5 countries,' '8 German cities,' '20 U.S. states' instead of listing all locations. In the latter case, 'U.S.' is used rather than 'United States' or 'American'.  

  * Descriptors that do not have a distinct geographic area, such as 'communities' or 'regions', are not included in titles.   

  * 'Global' may be appropriate for studies where the universe of participants is truly worldwide. Possible examples include online surveys that are not restricted by geography, or studies of organizations, such as NGOs.   

  * Brackets are typically not indicated. They are indicated when a study has National, Federal, Congressional, or American in the title. Brackets can be indicated if a non-United States study has “National” in the title, or a similar word specific to that country.  

Time Period:  

  * All titles include the data collection's time period, which reflects the time period that the data collection covers and should match the Time Period. For example, in the 'Uganda Elite Study, 1964-1968', it is assumed that the Ugandans were surveyed about events in 1964-1968, even if the actual data collection might not have taken place until later.  

  * If the time period is already included in the title proper, it is not repeated.  

  * For most studies, a single year or range of years is acceptable. Years are written as four digits, including when used in a range (e.g., '1999', '2001-2003', or '1999, 2010, 2015').  

  * Months are included only when part of ICPSR series that have multiple releases, which are otherwise identical, each year. In these cases, months are spelled out (e.g., 'September 2020' instead of '9/2020' or 'Sept. 2020').  

**Examples:** 

```json
"Bridge of Faith: Aim4Peace Community-Based Violence Prevention Project, Kansas City, Missouri, 2014-2017"
```

```json
"Health and Relationships Project, United States, 2014-2015"
```

```json
"Targeted Interventions to Prevent Chronic Low Back Pain in High Risk Patients: A Multi-Site Pragmatic Randomized Controlled Trial (TARGET Trial), 4 U.S. cities, 2016-2019"
```

```json
"Aid Like A Paycheck (ALAP), Texas and California, 2014-2017"
```

```json
"COVID-19 Disruptions Disproportionately Affect Female Academics, Global, 2020"
```

### <a name="alternate_title"></a>5. Alternate Title         

**Description:** The alternate name(s) or acronym(s) commonly used to refer to the data collection.

**Required**: No

**Repeatable**: Yes

**Accepted Values**: Text

**Controlled Vocabulary:** N/A

**Usage Notes:** Alternate Title often takes the form of a shortened (by abbreviation or acronym) version of the official title.

**Examples:** 

```json
[
    "Add Health Parent Study"
]
```

```json
[
    "FACES 2009"
]
```

```json
[
    "Surveys of Consumers"
]
```

```json
[
    "Eurobarometer 85.2"
]
```

### <a name="link_title"></a>6. Link Title         

**Description:** The title of an external resource that is included in the ICPSR catalog as a courtesy to users.

**Required**: No

**Repeatable**: No

**Accepted Values**: Text

**Controlled Vocabulary:** N/A

**Usage Notes:** Always appears with the Link URL.

**Example:** 

```json
"Cebu Longitudinal Health and Nutrition Survey"
```

### <a name="link_url"></a>7. Link URL         

**Description:** The URL of an external resource that is included in the ICPSR catalog as a courtesy to users.

**Required**: No

**Repeatable**: No

**Accepted Values**: Text

**Controlled Vocabulary:** N/A

**Usage Notes:** Always appears with the Link Title.

**Example:** 

```json
"https://cebu.cpc.unc.edu/"
```

### <a name="principal_investigator"></a>8. Principal Investigator         

**Description:** The key people or organizations responsible for the data collection, listed by importance. Each data collection requires at least one PI, either a person or an organization.

**Required**: Yes

**Repeatable**: Yes

**Accepted Values**: Multi-part element; see subfield definitions for more information.

**Controlled Vocabulary:** The [ICPSR Personal Names Authority List](https://www.icpsr.umich.edu/web/ICPSR/thesaurus/10002) and [Organization Names Authority List](https://www.icpsr.umich.edu/web/ICPSR/thesaurus/10004) are the primary authority control sources for PI names. The [Virtual International Authority File](https://viaf.org/) (VIAF) serves as a secondary resource if names are not present in ICPSR lists.

**Usage Notes:** A principal investigator (PI) may be a person or an organization; use the Person or Organization element as appropriate. If the PI is identified as a person, their affiliated organization (if applicable) should be included in the Organization element.  

When entering the name of an individual or organizational PI, the following hierarchy of authority control sources should be used to make sure the name conforms to best practices within ICPSR and the broader academic community:    

  1. If the person or organization has published data with ICPSR in the past, use the name as it has been displayed previously within the ICPSR catalog.    
  2. If the person or organization is in the [ICPSR Personal Name Authority List](https://www.icpsr.umich.edu/web/ICPSR/thesaurus/10002) or the [ICPSR Organization Names Authority List](https://www.icpsr.umich.edu/web/ICPSR/thesaurus/10004), conform to the listed name form.  
  3. If the person or organization is not available in an ICPSR authority list, consult [VIAF](https://viaf.org).    
  4. If the person or organization does not have a VIAF record, consult another authoritative source, such as an organization's website, Google Scholar, or a personal C.V. published on an institutional website.    

For the names of people:   

  * The given (i.e., 'first') name may include the middle name or initial. If the person only uses an inital for the given name, do not include a space between first and middle initials (e.g., 'E.V.').  
  * The family (i.e., 'last') name can include any suffixes (such as 'II' or 'Jr.').   
  * Abbreviations are discouraged (especially 'et al.').  

For the names of organizations:  

  * Include the full hierarchy of the organization, going from the highest level down to the most specific. Note that the higher level of the organization must be listed before the lower level, and levels should be separated by a period (e.g., 'University of Michigan. College of Literature, Science, and the Arts'). There is no period following the last level listed.  
  * Abbreviations are discouraged, except 'Inc.' and 'Co.' In particular, governmental PI's are spelled out completely (e.g., 'United States Department of Commerce' rather than 'U.S. Dept. of Commerce').  
  * 'The' is not included at the start of an organization name unless it is actually part of the official name (e.g., 'The New York Times' but not 'The National Institute of Justice')  

Additional points regarding affiliated organizations:  

  * If a PI's organizational affiliation is not known, use the term 'Unknown' in the PI Organization element.  
  * If multiple PIs (people) are affiliated with the same organization, the affiliated organization's name must be included for each person.  

#### <a name="autogenerated_heading_3"></a>8.1. Subfields:

| Property                                                    | Required? | Repeatable? | Accepted Values | Description                                                                                                                                                                                    |
| ----------------------------------------------------------- | --------- | ----------- | --------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Person](#principal_investigator_items_person )             | No        | No          | Multi-part; see subfields          | The name of a person primarily responsible for the data collection.                                                                                                                            |
| [Organization](#principal_investigator_items_organization ) | No        | No          | Text            | The name of the organization primarily responsible for the data collection OR the organization with which an individual PI was affiliated at the time of a data collection's deposit at ICPSR. |
| [Order](#principal_investigator_items_order )               | Yes       | No          | Number          | The order or rank of importance for the PIs associated with the data collection, typically provided to ICPSR by the lead PI.                                                                   |

##### <a name="principal_investigator_items_person"></a>8.1.1. Person

**Description:** The name of a person primarily responsible for the data collection.

**Required**: No

**Repeatable**: No

**Accepted Values**: Multi-part element; see subfield definitions for more information.

| Property                                                         | Required? | Repeatable? | Accepted Values | Description                               |
| ---------------------------------------------------------------- | --------- | ----------- | --------------- | ----------------------------------------- |
| [Given Name](#principal_investigator_items_person_given_name )   | Yes       | No          | Text            | The person's given name.                  |
| [Family Name](#principal_investigator_items_person_family_name ) | Yes       | No          | Text            | The person's family name (e.g., surname). |

**Examples:** 

```json
{
    "given_name": "James A.",
    "family_name": "McCann"
}
```

```json
{
    "given_name": "Warren",
    "family_name": "Winkelstein Jr."
}
```

```json
{
    "given_name": "E.V.",
    "family_name": "Oppenhuis"
}
```

```json
{
    "given_name": "Miner P.",
    "family_name": "Marchbanks III"
}
```

###### <a name="principal_investigator_items_person_given_name"></a>8.1.1.1. Given Name

**Description:** The person's given name.

**Required**: Yes

**Repeatable**: No

**Accepted Values**: Text

###### <a name="principal_investigator_items_person_family_name"></a>8.1.1.2. Family Name

**Description:** The person's family name (e.g., surname).

**Required**: Yes

**Repeatable**: No

**Accepted Values**: Text

##### <a name="principal_investigator_items_organization"></a>8.1.2. Organization

**Description:** The name of the organization primarily responsible for the data collection OR the organization with which an individual PI was affiliated at the time of a data collection's deposit at ICPSR.

**Required**: No

**Repeatable**: No

**Accepted Values**: Text

**Examples:** 

```json
"University of Michigan"
```

```json
"Harvard University. Medical School"
```

```json
"University of California, Irvine"
```

```json
"United States Department of Health and Human Services. Centers for Disease Control and Prevention. Office of Minority Health and Health Disparities"
```

##### <a name="principal_investigator_items_order"></a>8.1.3. Order

**Description:** The order or rank of importance for the PIs associated with the data collection, typically provided to ICPSR by the lead PI.

**Required**: Yes

**Repeatable**: No

**Accepted Values**: Number

**Controlled Vocabulary:** N/A

**Usage Notes:** A value of '1' indicates the primary PI, '2' the second, and so forth.

**Examples:** 

```json
1
```

```json
2
```

```json
3
```

###### Complete Principal Investigator Examples (with Subfields):
```json
[
    {
        "person": {
            "given_name": "Jane",
            "family_name": "Doe"
        },
        "organization": "Urban Institute",
        "order": 1
    },
    {
        "person": {
            "given_name": "John Q.",
            "family_name": "Public"
        },
        "organization": "Harvard University. Medical School",
        "order": 2
    }
]
```

```json
[
    {
        "organization": "Urban Institute",
        "order": 1
    }
]
```

### <a name="citation"></a>9. Citation         

**Description:** The official way to reference the data collection in writing.

**Required**: No

**Repeatable**: No

**Accepted Values**: Text

**Controlled Vocabulary:** N/A

**Usage Notes:** The Citation is dynamically assembled from other entry elements in this format: Principal-Investigator-list. Study-Title. Distributor-list, Version-Date. DOI. ICPSR 'union catalog' records – i.e., external resource to which ICPSR links as a courtesy – do not have citations generated.  

For additional information about how DOIs for citations are generated, see the Digital Object Identifier element usage notes.  

**Examples:** 

```json
[
    "University of Michigan. Survey Research Center. Economic Behavior Program. Survey of Consumer Attitudes and Behavior, September 2018. Inter-university Consortium for Political and Social Research [distributor], 2021-11-18. https://doi.org/10.3886/ICPSR38121.v1"
]
```

```json
[
    "Goldin, Claudia, and Lawrence Katz. The 1915 Iowa State Census Project. ICPSR28501-v1. Ann Arbor, MI: Inter-university Consortium for Political and Social Research [distributor], 2010-12-14. http://doi.org/10.3886/ICPSR28501.v1"
]
```

### <a name="distributor"></a>10. Distributor         

**Description:** The organization(s) responsible for distributing the data collection.

**Required**: Yes

**Repeatable**: Yes

**Accepted Values**: Multi-part element; see subfield definitions for more information.

**ICPSR Input Guidance:** Most data collections list ICPSR as the distributor. As such, the  full name and location of ICPSR are easily accessible in the metadata editor.

If a non-ICPSR distributor is necessary, please confirm the standards with the Metadata Librarian. Please note that external distributors are often appropriate for Union Catalog entries and metadata-only releases.

#### <a name="autogenerated_heading_4"></a>10.1. Subfields:

| Property                                 | Required? | Repeatable? | Accepted Values | Description                                                          |
| ---------------------------------------- | --------- | ----------- | --------------- | -------------------------------------------------------------------- |
| [Name](#distributor_items_name )         | Yes       | No          | Text            | The name of the data distributor.                                    |
| [Location](#distributor_items_location ) | Yes       | No          | Text            | The location of the data distributor.                                |
| [Order](#distributor_items_order )       | Yes       | No          | Number          | The order of importance for the distributors of the data collection. |

##### <a name="distributor_items_name"></a>10.1.1. Name

**Description:** The name of the data distributor.

**Required**: Yes

**Repeatable**: No

**Accepted Values**: Text

**Controlled Vocabulary:** [ICPSR Organization Names Authority List](https://www.icpsr.umich.edu/web/ICPSR/thesaurus/10004)

**Examples:** 

```json
"Inter-university Consortium for Political and Social Research"
```

```json
"Roper Center for Public Opinion Research"
```

##### <a name="distributor_items_location"></a>10.1.2. Location

**Description:** The location of the data distributor.

**Required**: Yes

**Repeatable**: No

**Accepted Values**: Text

**Controlled Vocabulary:** N/A

**Usage Notes:** Include the city and state (or country) where the distributor is located.

**Examples:** 

```json
"Ann Arbor, MI"
```

```json
"Chicago, IL"
```

##### <a name="distributor_items_order"></a>10.1.3. Order

**Description:** The order of importance for the distributors of the data collection.

**Required**: Yes

**Repeatable**: No

**Accepted Values**: Number

**Controlled Vocabulary:** N/A

**Usage Notes:** A value of '1' indicates the primary distributor, '2' the second, and so forth.

**Examples:** 

```json
1
```

```json
2
```

```json
3
```

###### Complete Distributor Examples (with Subfields):
```json
[
    {
        "name": "Inter-university Consortium for Political and Social Research",
        "location": "Ann Arbor, MI",
        "order": 1
    }
]
```

```json
[
    {
        "name": "Inter-university Consortium for Political and Social Research",
        "location": "Ann Arbor, MI",
        "order": 1
    },
    {
        "name": "Roper Center for Public Opinion Research",
        "location": "Princeton, NJ",
        "order": 2
    }
]
```

### <a name="study_number"></a>11. Study Number         

**Description:** A unique, numerical value used by ICPSR to identify and track data collections.

**Required**: Yes

**Repeatable**: No

**Accepted Values**: Number

**Controlled Vocabulary:** N/A

**Usage Notes:** The study number is automatically generated by ICPSR and is unique. Current study numbers are five digits, though four digit numbers were once standard and are still acceptable.

**Examples:** 

```json
2760
```

```json
3025
```

```json
38672
```

### <a name="doi"></a>12. Digital Object Identifier (DOI)         

**Description:** The registered persistent digital object identifier (DOI) associated with the data collection.

**Required**: No

**Repeatable**: No

**Accepted Values**: Text (formatted as a URL)

**Controlled Vocabulary:** N/A

**Usage Notes:** The DOI (digital object identifier) is a persistent identifier provided by DataCite, a DOI registration agency. The DOI name is divided into three parts, separated by slashes ('/'): 'https://doi.org' is the HTTP URL link; followed by '10.3886', a globally unique number that identifies ICPSR as the registrant within the DOI namespace; followed by 'ICPSR', the ICPSR study number, and then the version number. The study number is automatically generated by ICPSR and is unique. Current study numbers are five digits, though four digit numbers were once standard and are still acceptable. Studies with fewer than five digits will have zeroes prepended in the DOI (e.g., '10.3886/ICPSR02760).

**Examples:** 

```json
"https://doi.org/10.3886/ICPSR03025.v2"
```

```json
"https://doi.org/10.3886/ICPSR06425.v1"
```

### <a name="funding_source"></a>13. Funding Source         

**Description:** The sources of funding that supported the data collection.

**Required**: No

**Repeatable**: Yes

**Accepted Values**: Multi-part element; see subfield definitions for more information.

#### <a name="autogenerated_heading_5"></a>13.1. Subfields:

| Property                                            | Required? | Repeatable? | Accepted Values           | Description                                                                |
| --------------------------------------------------- | --------- | ----------- | ------------------------- | -------------------------------------------------------------------------- |
| [Agency](#funding_source_items_agency )             | Yes       | No          | Text                      | An organization that supported the data collection.                        |
| [Grant Number](#funding_source_items_grant_number ) | No        | Yes         | Text                      | A unique identifier associated with the funding.                           |
| [Purpose](#funding_source_items_purpose )           | No        | Yes         | Text                      | The purpose of the funding.                                                |
| [Order](#funding_source_items_order )               | Yes       | No          | Number                    | The relative order of funding sources associated with the data collection. |

##### <a name="funding_source_items_agency"></a>13.1.1. Agency

**Description:** An organization that supported the data collection.

**Required**: Yes

**Repeatable**: No

**Accepted Values**: Text

**Controlled Vocabulary:** The [ICPSR Organization Names Authority List](https://www.icpsr.umich.edu/web/ICPSR/thesaurus/10004) is the primary authority control source for funding agencies. The [Virtual International Authority File](https://viaf.org/) (VIAF) serves as a secondary resource if names are not present in the ICPSR list.

**Usage Notes:** When entering the name of a funding agency, the following hierarchy of authority control sources should be used to make sure the name conforms to best practices within ICPSR and the broader academic community:  

  1. If the funding agency has sponsored archived data at ICPSR, use the name as it has been displayed previously within the ICPSR catalog.    
  2. If the funding agency is in the [ICPSR Organization Names Authority List](https://www.icpsr.umich.edu/web/ICPSR/thesaurus/10004), conform to the listed name form.  
  3. If the funding agency is not available in an ICPSR authority list, consult [VIAF](https://viaf.org).    
  4. If the funding agency does not have a VIAF record, consult another authoritative source, such as the organization's website or Google Scholar.  

**ICPSR Input Guidance:** The Principal Investigator's home institution does not need to be listed as a funding agency unless the PI provides a grant number (or other award information) or makes a specific request.

**Examples:** 

```json
"United States Department of Justice. Office of Justice Programs. Bureau of Justice Statistics"
```

```json
"Institute of Museum and Library Services"
```

```json
"Robert Wood Johnson Foundation"
```

##### <a name="funding_source_items_grant_number"></a>13.1.2. Grant Number

**Description:** A unique identifier associated with the funding.

**Required**: No

**Repeatable**: Yes

**Accepted Values**: Text

**Controlled Vocabulary:** N/A

**Usage Notes:** Internal blanks in the Grant Number are replaced with hyphens. Multiple grants from the same funding agency are separated by a comma.

**Examples:** 

```json
[
    "SES-1835721"
]
```

```json
[
    "MDR-8550085",
    "MDR-8550204"
]
```

```json
[
    "40791"
]
```

##### <a name="funding_source_items_purpose"></a>13.1.3. Purpose

**Description:** The purpose of the funding.

**Required**: No

**Repeatable**: Yes

**Accepted Values**: Text

**Controlled Vocabulary:** Local ICPSR controlled vocabulary. See below for terms and definitions:

| *Term* | *Definition* |
|----------|---------------|
| collection and/or analysis of data | The funder supported the collection and/or analysis of the study's data. |
| secondary analysis of data | The funder supported secondary analysis performed on the data. |
| archiving of data | The funder supported the archiving and preservation of the data. |

**ICPSR Input Guidance:** This is an internal ICPSR element that is not publicly displayed. Certain ICPSR topical archives find this useful as they assemble reports for their funding agencies.

**Examples:** 

```json
[
    "collection and/or analysis of data",
    "secondary analysis of data"
]
```

```json
[
    "archiving of data"
]
```

##### <a name="funding_source_items_order"></a>13.1.4. Order

**Description:** The relative order of funding sources associated with the data collection.

**Required**: Yes

**Repeatable**: No

**Accepted Values**: Number

**Controlled Vocabulary:** N/A

**Usage Notes:** A value of '1' indicates the primary funder, '2' the second, and so forth.

**Examples:** 

```json
1
```

```json
2
```

```json
3
```

###### Complete Funding Source Examples (with Subfields):
```json
[
    {
        "agency": "Robert Wood Johnson Foundation",
        "grant_numbers": [
            "MDR-8550085",
            "MDR-8550204"
        ],
        "purpose": [
            "collection and/or analysis of data"
        ],
        "order": 1
    },
    {
        "agency": "United States Department of Justice. Office of Justice Programs. Bureau of Justice Statistics",
        "grant_numbers": [
            "SES-1835721"
        ],
        "order": 2
    }
]
```

```json
[
    {
        "agency": "Institute of Museum and Library Services",
        "order": 1
    }
]
```

### <a name="external_source_ID"></a>14. External Source ID         

**Description:** A unique identifier supplied by the data depositor.

**Required**: No

**Repeatable**: Yes

**Accepted Values**: Text

**Controlled Vocabulary:** N/A

**ICPSR Input Guidance:** This is an internal ICPSR element that is not publicly displayed. An External Source ID consists of: an ICPSR-defined source organization code, a colon, and a Depositor-supplied ID.

**Examples:** 

```json
[
    "BJS:271"
]
```

```json
[
    "PSC:12345"
]
```

### <a name="summary"></a>15. Summary         

**Description:** A description of the data collection that helps users understand its purpose, substance, and key topics.

**Required**: Yes

**Repeatable**: No

**Accepted Values**: Text

**Controlled Vocabulary:** N/A

**Usage Notes:** The main goal of the Summary is to give the reader a clear sense of what the data collection is about, including substantive information about the different parts of the data collection not adequately conveyed by the Fileset names or found elsewhere in the metadata.   

A listing of major variables or categories of variables with a few examples is also important. It is also salient to indicate the unit of analysis for the data collection, i.e., who or what is being studied: individuals, housing units, courts, criminal acts, etc. Most often the unit of analysis is the individual; where it is not, it is particularly important to make this clear.  

The Summary is written in the third person and avoids attempting to address issues of how the data might be used, who might be interested in the data, or any evaluative comments about the worth or usefulness of the data collection. The Summary uses past tense when describing the process of collecting the data and present tense when necessary, such as when describing the data (e.g., 'The MIDUS Refresher collection is split into two datasets.'). Numerals are used instead of spelling them out; if a number is spelled out for emphasis, the number is attached in parentheses (e.g. 'Two thousand (2,000)').  

**Examples:** 

```json
"In 2014, Chicago Public Schools, looking to reduce the possibility of gun violence among school-aged youth, applied for a grant through the National Institute of Justice. CPS was awarded the Comprehensive School Safety Initiative grant and use said grant to establish the 'Connect and Redirect to Respect' program. This program used student social media data to identify and intervene with students thought to be at higher risk for committing violence. At-risk behaviors included brandishing a weapon, instigating conflict online, signaling gang involvement, and threats towards others. Identified at-risk students would be contacted by a member of the CPS Network Safety Team or the Chicago Police Department's Gang School Safety Team, depending on the risk level of the behavior. To evaluate the efficacy of CRR, the University of Chicago Crime Lab compared outcomes for students enrolled in schools that received the program to outcomes for students enrolled in comparison schools, which did not receive the program. 32 schools were selected for the study, with a total of 44,503 students. Demographic variables included age, race, sex, and ethnicity. Misconduct and academic variables included arrest history, in-school suspensions, out-of-school suspensions, GPA, and attendance days."
```

```json
"The Health and Relationship Project is a study of both spouses in same-sex and different-sex marriages who were legally married and aged 35 to 65 at the time of data collection (2015). There are two parts of this study: a baseline questionnaire and a daily diary questionnaire completed for 10 consecutive days; both components were completed online and spouses were asked to complete the surveys separately. The baseline questionnaire asks participants about a number of topics related to marriage and health, including stress, health status and health behaviors, relationship quality, and how they have approached health problems in the past. The diary questionnaire asks participants a number of questions about the past 24 hours, including daily stress experiences, social interactions, and health behaviors."
```

### <a name="subject_term"></a>16. Subject Term         

**Description:** A controlled list of social science terms maintained by ICPSR and used to indicate topics related to the data collection.

**Required**: Yes

**Repeatable**: Yes

**Accepted Values**: Text

**Controlled Vocabulary:** The [ICPSR Subject Thesaurus](https://www.icpsr.umich.edu/web/ICPSR/thesaurus/10001) and the [ICPSR Personal Names Authority List](https://www.icpsr.umich.edu/web/ICPSR/thesaurus/10002) are preferred sources.

**Usage Notes:** The [Library of Congress Subject Terms](https://authorities.loc.gov) is referenced when adding new terms to the ICPSR Subject Thesaurus.

**ICPSR Input Guidance:** Non-thesaurus terms can be submitted in the metadata editor and will be reviewed by the metadata librarian. If an ICPSR staff member submits a non-thesaurus term, the metadata librarian will gauge the necessity of this term, check it against the Library of Congress Subject Headings to see if a different related term should be used, and consider it for addition to the ICPSR thesaurus.

**Examples:** 

```json
[
    "child care"
]
```

```json
[
    "Social Security",
    "crime",
    "victimization"
]
```

```json
[
    "COVID-19",
    "Biden, Joe"
]
```

### <a name="geographic_coverage_area"></a>17. Geographic Coverage Area         

**Description:** The geographic locations where the data refer or are related.

**Required**: Yes

**Repeatable**: Yes

**Accepted Values**: Text

**Controlled Vocabulary:** [ICPSR Geographic Names Thesaurus](https://www.icpsr.umich.edu/web/ICPSR/thesaurus/10003).

**Usage Notes:**   
Each geographic term's full hierarchy must be included; please note:   

* For a U.S. city, the state and country are listed alongside (e.g., 'Los Angeles, California, United States').   
* Non-U.S. geographic subdivisions need not include hierarchical relations, with the specific exceptions of Canadian provinces and the countries within the United Kingdom.  
* 'Global' may be appropriate for studies where the universe of participants is truly worldwide. Possible examples include online surveys that are not restricted by geography, or studies of organizations, such as NGOs.  
* County-level information is typically not indicated. If a U.S. county will be included, the state name and 'United States' must be listed as well.  

The [Getty Thesaurus of Geographic Names](http://www.getty.edu/research/tools/vocabularies/tgn/index.html) is referenced when introducing new geographic names.  

**ICPSR Input Guidance:** The metadata editor will automatically put this element's values in alphabetical order, regardless of hierarchy.

**Examples:** 

```json
[
    "United States",
    "Maryland",
    "Baltimore"
]
```

```json
[
    "United Kingdom",
    "China"
]
```

```json
[
    "Canada",
    "Alberta"
]
```

### <a name="time_period"></a>18. Time Period         

**Description:** The time period(s) to which the data refer, regardless of when the data were collected.

**Required**: Yes

**Repeatable**: Yes

**Accepted Values**: Multi-part element; see subfield definitions for more information.

#### <a name="autogenerated_heading_11"></a>18.1. Subfields:

| Property                                     | Required? | Repeatable? | Accepted Values | Description                                                                                                                                             |
| -------------------------------------------- | --------- | ----------- | --------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Date](#time_period_items_date )             | Yes       | No          | Text            | The date (or date range) for a time period to which the data refer.                                                                                     |
| [Time Frame](#time_period_items_time_frame ) | No        | No          | Text            | An optional free-text description of the time period, used for non-numeric dates (e.g., 'Fall 2012') or to add context when multiple dates are present. |

##### <a name="time_period_items_date"></a>18.1.1. Date

**Description:** The date (or date range) for a time period to which the data refer.

**Required**: Yes

**Repeatable**: No

**Accepted Values**: Text

**Controlled Vocabulary:** N/A

**Usage Notes:** Time Periods focus on the dates the data are actually about, regardless of when the data were collected.   

Time Periods generally correspond to the dates that appear in the Title; days and months may be included in the Time Period even though they are not in the Title.  

Dates are formatted in accordance with ISO 8601 (YYYY, YYYY-MM, or YYYY-MM-DD). One hyphen separates the parts of a date; two hyphens separate two dates. Ranges may be expressed in years (YYYY--YYYY), months (YYYY-MM--YYYY-MM), or days (YYYY-MM-DD--YYYY-MM-DD). No spaces are permitted in date expressions.  

**Examples:** 

```json
"2020"
```

```json
"2021--2022"
```

```json
"2006-03--2006-04"
```

```json
"2020-01-21--2021-01-21"
```

##### <a name="time_period_items_time_frame"></a>18.1.2. Time Frame

**Description:** An optional free-text description of the time period, used for non-numeric dates (e.g., 'Fall 2012') or to add context when multiple dates are present.

**Required**: No

**Repeatable**: No

**Accepted Values**: Text

**Controlled Vocabulary:** N/A

**Usage Notes:** The textual description ('time frame') is used to add context to the Time Period when multiple time periods exist (e.g., to describe different waves, dataset names, or fiscal year designation) and/or when the date cannot be expressed exclusively through numbers, such as seasons or other units of time where the data producer did not clarify the exact dates they meant.  

The textual description should not simply restate the time period in words. For example, if the Time Period is 2020-01, the Time Frame should not be 'January 2020'.  

**Examples:** 

```json
"Wave 1"
```

```json
"Spring 2013"
```

```json
"Post-Survey Follow-Up"
```

###### Complete Time Period Examples (with Subfields):
```json
[
    {
        "date": "2020-01-21--2020-06-21",
        "time_frame": "Wave 1"
    },
    {
        "date": "2022-01--2023-01",
        "time_frame": "Wave 2"
    }
]
```

```json
[
    {
        "date": "2020"
    }
]
```

### <a name="collection_date"></a>19. Collection Date         

**Description:** The date(s) when the data were physically collected.

**Required**: No

**Repeatable**: Yes

**Accepted Values**: Multi-part element; see subfield definitions for more information.

#### <a name="autogenerated_heading_12"></a>19.1. Subfields:

| Property                                         | Required? | Repeatable? | Accepted Values | Description                                                                                                                                                        |
| ------------------------------------------------ | --------- | ----------- | --------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [Date](#collection_date_items_date )             | Yes       | No          | Text            | The date (or date range) of the data collection period.                                                                                                            |
| [Time Frame](#collection_date_items_time_frame ) | No        | No          | Text            | An optional free-text description of the data collection period, used for non-numeric dates (e.g., 'Fall 2012') or to add context when multiple dates are present. |

##### <a name="collection_date_items_date"></a>19.1.1. Date

**Description:** The date (or date range) of the data collection period.

**Required**: Yes

**Repeatable**: No

**Accepted Values**: Text

**Controlled Vocabulary:** N/A

**Usage Notes:** Dates are formatted in accordance with ISO 8601 (YYYY, YYYY-MM, or YYYY-MM-DD). One hyphen separates the parts of a date; two hyphens separate two dates. Ranges may be expressed in years (YYYY--YYYY), months (YYYY-MM--YYYY-MM), or days (YYYY-MM-DD--YYYY-MM-DD). No spaces are permitted in date expressions.

**Examples:** 

```json
"2020"
```

```json
"2021--2022"
```

```json
"2006-03--2006-04"
```

```json
"2020-01-21--2021-01-21"
```

##### <a name="collection_date_items_time_frame"></a>19.1.2. Time Frame

**Description:** An optional free-text description of the data collection period, used for non-numeric dates (e.g., 'Fall 2012') or to add context when multiple dates are present.

**Required**: No

**Repeatable**: No

**Accepted Values**: Text

**Controlled Vocabulary:** N/A

**Usage Notes:** The textual description ('time frame') is used to add context to the Collection Date when multiple time periods exist (e.g., to describe different study waves, dataset names, or fiscal year designation) and/or when the date cannot be expressed exclusively through numbers, such as seasons or other units of time where the data producer did not clarify the exact dates they meant.  

The textual description should not simply restate the time period in words. For example, if the Time Period is 2020-01, the Time Frame should not be 'January 2020'.  

**Examples:** 

```json
"Wave 1"
```

```json
"Spring 2013"
```

```json
"Post-Survey Follow-Up"
```

###### Complete Collection Date Examples (with Subfields):
```json
[
    {
        "date": "2020-01-21--2020-06-21",
        "time_frame": "Wave 1"
    },
    {
        "date": "2022-01--2023-01",
        "time_frame": "Wave 2"
    }
]
```

```json
[
    {
        "date": "2020"
    }
]
```

### <a name="universe"></a>20. Universe         

**Description:** The total group of persons or other entities (e.g., households or organizations) that were the object of research and to which analytic results refer.

**Required**: No

**Repeatable**: No

**Accepted Values**: Text

**Controlled Vocabulary:** N/A

**Usage Notes:** Age, nationality, and residence commonly help to delineate a given universe, but any of a number of factors may be involved, such as sex, race, income, veteran status, criminal convictions, etc. The Universe may consist of elements other than persons, such as housing units, court cases, deaths, countries, etc. It should be possible to tell from the description of the universe whether a given individual or element (hypothetical or real) is a member of the population under study. Typically, the Universe statement is about one sentence or shorter, and reflects the entire possible population a data collection sought to study.

**ICPSR Input Guidance:** Universe is distinct from Sampling as it describes the population the study seeks to analyze, while Sampling describes how the researchers selected participants among that population. Universe should not contain information about methodology, only general information about the target population.

**Examples:** 

```json
"All households in the United States with phones."
```

```json
"Part 1: Thirty cities in Massachusetts during 1980-1986. Parts 2-4: All residents in Massachusetts during 1986."
```

```json
"Individuals self-identified as transgender, trans, genderqueer, non-binary, or other identities on the transgender identity spectrum aged 18 and older residing in the fifty U.S. states, the District of Columbia, American Samoa, Guam, Puerto Rico, and U.S. military bases overseas."
```

```json
"Jihadists from the United States and Canada, along with Incels from Germany, Canada, the United States, and United Kingdom."
```

```json
"All publicly funded medical examiner and coroner offices."
```

```json
"Uncertified ballots for the 2000 United States presidential election in Florida."
```

### <a name="data_type"></a>21. Data Type         

**Description:** The types of data included in the data collection.

**Required**: No

**Repeatable**: Yes

**Accepted Values**: Text

**Controlled Vocabulary:** Local ICPSR controlled vocabulary. See below for terms and definitions:

| *Term* | *Definition* |
|----------|---------------|
| administrative records data | Information collected on individuals or groups as part of the routine administrative procedures of an agency, business, or institution. Such data are not usually collected with research purposes in mind, may be voluminous, and may require preparation such as coding in order to be usable by researchers. Examples include income tax forms, patent applications, death certificates, etc. |
| aggregate data | Data compiled into summaries or summary reports, typically for the purposes of public reporting or statistical analysis. |
| audio: sound data | Sound data recorded either in analog or digital form. |
| census/enumeration data | Data collected from all members of a population. |
| clinical data | Data related to psychological or medical testing. |
| event/transaction data | Data that deal with a succession of events or transactions occurring over a specified time period. |
| experimental data | Data collected from experiments that are not clinical in nature. |
| geographic information system (GIS) data | Data that captures positions and spatial patterns on Earth's surface. |
| image: photographs, drawings, graphical representations | Data recorded as a still image. |
| medical records | Health-related data that is associated with regular patient care. |
| observational data | Data collected through observation, with the research subject not directly involved in the recording of information. |
| program source code | Human-readable instructions that a programmer writes to specify the actions to be performed bya computer. |
| roll call voting data | Records of votes cast by legislative bodies.
| survey data | Data collected from a sample of respondents, generally through structured interviews or self-administered questionnaires. |
| text | Written work, readable by a machine or human. |
| video: film, animation, etc. | Moving image with, or without sound recorded either in analog or digital form. |

**Examples:** 

```json
[
    "administrative records data"
]
```

```json
[
    "census/enumeration data",
    "survey data",
    "video: film, animation, etc."
]
```

### <a name="collection_note"></a>22. Collection Note         

**Description:** Important details about the data collection (like unique authoring, discrepencies, or processing information) that can't be recorded in other metadata elements.

**Required**: No

**Repeatable**: Yes

**Accepted Values**: Text

**Controlled Vocabulary:** N/A

**Usage Notes:** Collection Notes should include any information that does not fit anywhere else in the metadata, such as: information about unique aspects of the way the data was processed, discrepancies between the metadata and documentation files, information about the research team, or series-specific notes.

**Examples:** 

```json
[
    "Exchange rates are expressed in United States dollars per national currency unit or vice versa, and two rates are given for the special drawing right (SDR) value of the national currency unit."
]
```

```json
[
    "Percentage distributions provided in the codebook were generated using full weights, which are not available on the public use files. Therefore, these results cannot be replicated using the public use files. The differences between results produced using the full weights and those produced using the sampling weights available on the public use files are estimated to be below 1 percent."
]
```

```json
[
    "Information on the Index of Consumer Sentiment, the Index of Current Economic Conditions, and the Index of Consumer Expectations and how they were created can be found in the P.I. Codebook.",
    "Additional information on the Survey of Consumers can be found by visiting the Survey of Consumers Website."
]
```

```json
[
    "At PI request, dataset 1 should be attributed to Anura P. Jayasumana while datasets 2-6 should be attributed to Jytte Klausen. Please refer to the PI user guide for additional information."
]
```

### <a name="study_purpose"></a>23. Study Purpose         

**Description:** The study's main goals and associated research questions.

**Required**: No

**Repeatable**: No

**Accepted Values**: Text

**Controlled Vocabulary:** N/A

**Usage Notes:** The Study Purpose provides more specific information than the Summary element, including the data collection's objectives, intended achievements, and lists of questions it sought to answer. This element can also include historical or background information about the research project. As with the Summary, the text should be written in third person and avoid any commentary on the data collection's outcomes.

**Examples:** 

```json
"The purpose of this study is to advance understanding of the barriers and enablers associated with colorectal cancer (CRC) screening among Somali men ages 50-74 in Minnesota."
```

```json
"The purpose of the study's qualitative phase is to explore veterans' experiences by identifying factors that they believe caused or contributed to their contact with the criminal justice system."
```

```json
"The purpose of the study was to explore the impact of interventions by Sexual Assault Nurse Examiners/Sexual Assault Response Teams (SANE/SART) on the judicial process. The goal of this study was to test the efficacy of SANE/SART programs as a tool in the criminal justice system. The American Prosecutors Research Institute and Boston College tested the hypotheses that SANE/SART exams increase arrest and prosecution rates. In testing this hypothesis, the project team sought to answer five primary research questions: (1) Is the arrest rate higher in cases where a SANE/SART exam is performed as compared with cases in which no exam is performed?, (2) Is the indictment/charging rate higher in such cases?, (3) Are guilty pleas more likely to be entered in such cases, and are pleas likely to be to the existing charge or to a lesser charge?, (4) Is the conviction rate higher in such cases?, and (5) Is the sentence more severe in such cases? In addition, the project team examined the participation of victims in the criminal justice process and the types of services that were offered them. As a large portion of SANE/SART programs focus on understanding victims' reactions to sexual assault and ensuring proper treatment to minimize the chance of further trauma, a central hypothesis to be tested was that improved case outcomes may be a result of increased participation by the victim in the identification, apprehension, and prosecution of the perpetrator. Moreover, the level of services offered and provided to victims, particularly those related to prosecution would likely affect case outcomes as well. Both the victim's participation in the criminal justice system and specifics of SANE/SART services, including evidence collection, were considered in determining the true impact of SANE/SART interventions on case outcomes."
```

### <a name="study_design"></a>24. Study Design         

**Description:** The procedures used to contact participants and gather data.

**Required**: No

**Repeatable**: No

**Accepted Values**: Text

**Controlled Vocabulary:** N/A

**Usage Notes:** The Study Design provides more detailed information than the Summary, including how surveys were prepared and administered, how interviews were conducted, or how the data were obtained and compiled, as well as information about deadlines and follow-ups to respondents.  

**ICPSR Input Guidance:** It is acceptable to summarize information contained in study documentation and point users to that study documentation for more details. If the Summary already contains text that would be appropriate in Study Design, it is acceptable to duplicate that text.

**Example:** 

```json
"Data on organizational culture in each of the 12 courts (Part 1) were obtained by administering the Court Culture Assessment Instrument (CCAI) to all judges with a felony criminal court docket and to all senior court administrators. A total of 224 respondents completed the questionnaire. The CCAI was used to assess five key dimensions of current court culture orientation: (1) dominant case management style, (2) judicial and court staff relations, (3) change management, (4) courthouse leadership, and (5) internal organization. The determination of what culture judges and court administrators desired to establish in the near future was also obtained through the application of the same instrument (CACI) as practitioners were asked to indicate the type of culture in each work area (or content dimension) they would like to see in their court in the next five years. Additionally, surveys were conducted of prosecuting attorneys (Part 2) and public defender attorneys (Part 3) to gauge their views on how well the courts in which they practice achieve the goals of access, fairness, and managerial effectiveness. Every prosecutor and public defender with two years or more experience in representing the state or criminal defendants in felony cases was asked to complete a questionnaire probing their thoughts on how well their court acted to promote access to records through availability and staff cooperation, treating litigants, witnesses, jurors and others fairly, and demonstrating concern for the rights and interests of others in the criminal trial process, including attorney and victims. A total of 334 prosecuting attorneys and 260 public defense attorneys completed the 46-item trial court process survey."
```

### <a name="variable_description"></a>25. Variable Description         

**Description:** Significant variables (particularly demographic variables) in the publicly released data files.

**Required**: No

**Repeatable**: No

**Accepted Values**: Text

**Controlled Vocabulary:** N/A

**Usage Notes:** The Variable Description provides more detailed information than the Summary, including a review of variables that are important for users to know about. The codebook, setup files, and variable groups are appropriate sources of information for Variable Description.

**Examples:** 

```json
"The data includes variables about participants' and their parents' moods, interviewer observations, families' activities, families' health history, participants' school records, and parents' substance use. Demographic variables include race, religion, annual household income, and the participants' parents' employment statuses."
```

```json
"The LGBTQ Hate Crimes Interviews dataset contains more in-depth information, including victim demographic information, substance abuse history, information on whether the victim is open about their LGBTQ identification, the victim's job status, and information about how the victim reacted to the crime, such as whether or not they reported the crime to the police and their level of cooperation with the police and prosecution."
```

### <a name="sampling"></a>26. Sampling         

**Description:** The methods used to select the subset of the population that data are to be collected from (e.g., simple, systematic, stratified).

**Required**: No

**Repeatable**: No

**Accepted Values**: Text

**Controlled Vocabulary:** N/A

**Usage Notes:** The sample is a selection out of the universe of all possible relevant cases (e.g., adults in the United States, housing units in three counties of Michigan, etc.) that could have been included in the data collection. A detailed discussion of such things as sampling error or other limitations of the sampling methodology is not required here. Note that some studies, such as censuses, do not utilize samples but include all members of the universe. In such cases, 'inap.' may be entered in Sampling to indicate it was not omitted in error.

**ICPSR Input Guidance:** Sampling is distinct from Universe as it describes the methods the researcher used to select or recruit participants among the target population, while Universe describes the whole population the researchers sought to analyze. If no information about Sampling methodology is available, it is not appropriate to simply restate the Universe.

**Examples:** 

```json
[
    "National sample of telephone numbers from cell (RDD) sampling frame."
]
```

```json
[
    "The probability sample selected to represent the universe consists of approximately 71,000 households."
]
```

```json
[
    "The data collection is a pooled cross-sectional time-series of bank robberies in 50 states over a period of 6 years (1970-1975), resulting in 300 observations."
]
```

```json
[
    "Three target groups were identified: lawyers 36 years of age and above who were members of the American Bar Association (ABA), all the remaining members of the ABA excluding law students, and all lawyers in the nonmember files kept by the ABA. A systematic random probability sample was drawn to represent each of the three groups. The group of young lawyers was oversampled."
]
```

```json
[
    "The original National Longitudinal Survey of Youth Children and Young Adults 1979 (NLSY79) was a multi-stage, stratified random national sample. Sampling weights are available in the public-use datasets to adjust for minority oversamples and year-to-year attrition. There are mother and child specific weights. Primary Sampling Units (PSUs) were counties and independent cities. PSUs were stratified prior to sampling based on 9 Census divisions and 2 urban/rural classes.",
    "The initial Panel Study of Income Dynamics (PSID) combined two independent samples: a cross-sectional, national sample (based on stratified multistage selection of the civilian noninstitutional population of the U.S.) and a national sample of low-income families. The cross-section sample was an equal probability sample of households in the 48 coterminous states designed to yield about 3,000 completed interviews. The second sample was selected from the Census Bureau's Survey of Economic Opportunity (SEO) using unequal selection probabilities. "
]
```

### <a name="time_method"></a>27. Time Method         

**Description:** The methods used to collect data over time, like snapshots at one point (cross-sectional) or repeatedly (longitudinal) to study changes or trends.

**Required**: No

**Repeatable**: Yes

**Accepted Values**: Text

**Controlled Vocabulary:** [DDI Controlled Vocabulary for Time Method](https://ddialliance.org/Specification/DDI-CV/TimeMethod_1.2.html). See below for terms and definitions:

| *Term* | *Definition* |
|----------|---------------|
| Cross-sectional | Data collected by observing subjects within the study period, without regard to changes over time. May include more than one collection event. Analysis of cross-sectional data often consists in comparing the differences and similarities among subjects. |
| Cross-sectional ad-hoc follow-up | Data collected at one point in time to complete information collected in a previous cross-sectional study; the decision to collect follow-up data was not included in the original study design. |
| Longitudinal | Data collected repeatedly over time to allow studying change in a population. At least some of the questions or modules are repeated over waves. Use the broad term when none of the subterms is suitable. |
| Longitudinal: Cohort / Event-based | Data collected over time from the same cohort of respondents. The individuals in the cohort are connected in some way or have shared some significant experience within a given period. In some cases, the samples may differ between waves but are drawn from the same cohort. Examples: birth year, disease (clinical trials), common problem (intervention studies), education, employment, family formation, participation in an event. |
| Longitudinal: Panel | Data collected over time from, or about, the same sample of respondents. Differs from cohort/event-based data in that the selection of respondents is not based on their being connected in some way or having shared some significant experience. |
| Longitudinal: Panel: Continuous | Data collected from a panel of respondents on a regular basis. |
| Longitudinal: Panel: Interval | Data collected from a panel of respondents only when information is needed. |
| Longitudinal: Trend / Repeated Cross-section | Data collected from different samples or different groups of people from the same population at several points in time, using at least partly the same set of questions/variables. Conclusions are drawn for the population. Examples: European Social Survey (ESS), national longitudinal crime surveys. |
| Time Series | Data collected repeatedly over time to study change in observations. These are typically "objective" measurements of phenomena that can be observed externally, as opposed to attitudes/opinions or feelings. Examples may include economic/financial indicators, natural/meteorological phenomena, vital statistics, etc. |
| Time Series: Continuous | Measurements are taken at every instant in time. Examples: lie detectors, electrocardiograms, etc. |
| Time Series: Discrete | Measurements are taken at (usually regularly) spaced intervals. Examples: macroeconomics (weekly share prices, monthly profits, sales); meteorology (hourly temperature); measurements of individuals (blood pressure, weight, height); sociology (crime figures, employment figures), etc. |

**Examples:** 

```json
[
    "Cross-sectional"
]
```

```json
[
    "Longitudinal: Cohort / Event-based",
    "Time Series"
]
```

### <a name="data_source"></a>28. Data Source         

**Description:** The source of the data, when that source is external to the data collection and can be independently cited.

**Required**: No

**Repeatable**: Yes

**Accepted Values**: Text

**Controlled Vocabulary:** N/A

**Usage Notes:** Data Source includes such source entities as books, journal articles, administrative records, agency-sponsored surveys, or machine-readable files. Each source includes at minimum the title, author, publication year, and journal (if applicable). Any citation format is accepted.

**Examples:** 

```json
[
    "'Voting Scores.' Congressional Quarterly Almanac 33 (1977), 487-498"
]
```

```json
[
    "United States Bureau of the Census Economic Surveys, 1998-2000",
    "United States Congressional Record, 1989"
]
```

```json
[
    "Annual Company Organization Survey, 2003"
]
```

### <a name="collection_mode"></a>29. Collection Mode         

**Description:** The method(s) or procedure(s) used to collect the data.

**Required**: No

**Repeatable**: Yes

**Accepted Values**: Text

**Controlled Vocabulary:** Local ICPSR controlled vocabulary. See below for terms and definitions:

| *Term* | *Definition* |
|----------|---------------|
| audio computer-assisted self interview (ACASI) |  Interview administered by the respondent, without an interviewer, assisted by a computer with audio prompts. |
| audiovisual touch-screen computer-assisted self interview (AVT-CASI) | Interview administered by the respondent, without an interviewer, assisted by a touchscreen computer. |
| coded on-site observation | Observation that is conducted in a natural environment. |
| coded video observation | Observation that is conducted by video. |
| cognitive assessment test | Assessment of knowledge, skills, aptitude, or educational achievement by means of specialized measures or tests. |
| computer-assisted personal interview (CAPI) | Data collection method in which the interviewer reads questions to the respondents from the screen of a computer, laptop, or a mobile device like tablet or smartphone, and enters the answers in the same device. The administration of the interview is managed by a specifically designed program/application. |
| computer-assisted self interview (CASI) | Respondents enter the responses into a computer (desktop, laptop, Palm/PDA, tablet, etc.) by themselves. The administration of the questionnaire is managed by a specifically designed program/application but there is no real-time data transfer as in CAWI, the answers are stored on the device used for the interview. The questionnaire may be fixed form or interactive. Includes VCASI (Video computer-assisted self-interviewing), ACASI (Audio computer-assisted self-interviewing) and TACASI (Telephone audio computer-assisted self-interviewing). |
| computer-assisted telephone interview (CATI) | The interviewer asks questions via telephone as directed by a computer, responses are keyed directly into the computer and the administration of the interview is managed by a specifically designed program. |
| face-to-face interview | Data collection method in which a live interviewer conducts a personal interview, presenting questions and entering the responses. Use this broader term if not CAPI or PAPI, or if not known whether CAPI/PAPI or not. |
| mail questionnaire | Self-administered survey using a traditional paper questionnaire delivered and/or collected by mail (postal services). |
| mixed mode | Two or more modes of data collection are employed. |
| on-site questionnaire | Data collection method in which the information is gathered on-site. |
| paper and pencil interview (PAPI) | The interviewer uses a traditional paper questionnaire to read the questions and enter the answers. |
| record abstracts | Presentation of information in a condensed form, by reducing it to its main points. For example, abstracts of interviews or reports that are published and used as data rather than the full-length interviews or reports. |
| remote sensing | The acquisition of information about an object or phenomenon without making physical contact with the object, especially the Earth. In current usage, the term 'remote sensing' generally refers to the use of satellite- or aircraft-based sensor technologies to detect and classify objects on Earth. |
| self-enumerated questionnaire | Data collection method in which the respondent reads or listens to the questions, and enters the responses by him/herself; no live interviewer is present, or participates in the questionnaire administration. If possible, use a narrower term. Use this broader term if the method is not described by any of the narrower terms - for example, for PDF and diskette questionnaires. |
| telephone audio computer-assisted self interview (TACASI) | Interview administered by the respondent, without an interviewer, on the telephone, assisted by a computer. |
| telephone interview | Interview administered on the telephone. Use this broader term if not CATI, or if not known whether CATI or not. |
| web-based survey | An interview conducted via the Internet. For example, interviews conducted within online forums or using web-based audio-visual technology that enables the interviewer(s) and interviewee(s) to communicate in real time. |
| web scraping | A technique employed to extract large amounts of data from websites whereby the data is extracted and saved to a local file or to a database.|

**Examples:** 

```json
[
    "audio computer-assisted self interview (ACASI)"
]
```

```json
[
    "computer-assisted self interview (CASI)",
    "face-to-face interview"
]
```

### <a name="extent_of_processing"></a>30. Extent of Processing         

**Description:** Processing activities and checks performed on the data collection by ICPSR curation staff.

**Required**: No

**Repeatable**: Yes

**Accepted Values**: Text

**Controlled Vocabulary:** Local ICPSR controlled vocabulary. See below for terms and definitions:

| *Term* | *Definition* |
|----------|---------------|
| Checked for undocumented or out-of-range codes | Selected if the ICPSR curator checked at least half of the variables in the data collection for wild codes and corrected or reported in the codebook any wild codes discovered by these checks. |
| Created online analysis version with question text | Selected if the ICPSR curator created online analysis version with question text. |
| Created variable labels and/or value labels | Selected if the ICPSR curator created variable labels and/or value labels. |
| Performed consistency checks | Selected if the ICPSR curator performed any of the following consistency checks on at least half of the variables in the data collection and corrected or reported in the codebook any inconsistencies discovered by these checks:<br> &nbsp; &nbsp;- Checked to see that skip patterns in questionnaires were followed correctly.  <br> &nbsp; &nbsp;- Checked the logical consistency of response patterns across variables. |
| Performed recodes and/or calculated derived variables | Selected if the ICPSR curator recoded at least one original variable in the data collection and/or produced at least one new variable derived from one or more original variables. The following kinds of recodes DO NOT qualify for this task:<br> &nbsp; &nbsp;- Recodes performed for reasons of confidentiality. This type of recoding may be mentioned in other sections of the metadata description, usually in Restrictions or Collection Notes.  <br> &nbsp; &nbsp;- Recodes performed to correct errors uncovered by consistency checks.  <br> &nbsp; &nbsp;- Recodes performed to correct errors uncovered by checks for undocumented codes.  <br> &nbsp; &nbsp;- Recodes performed by standardized missing data codes.  <br> &nbsp; &nbsp;- When a unique record identifier is created that is not derived from an original variable. |
| Standardized missing values | Selected if the ICPSR curator standardized missing values for at least half of the variables in the data collection. Standardization of missing values means that all 'missing' responses are coded according to a fixed set of rules. There are various ways in which this standardization is typically applied:  <br>&nbsp;&nbsp;- In some data collections, each kind of 'missing response' may be assigned the same code across all variables, e.g., 'inapplicable' cases may be coded -1 for all variables, 'don't know' may be coded -2, and 'no answer' may be coded -3.  <br>&nbsp;&nbsp;- In other instances, standards may be specific to the type of variable involved, e.g., blanks may denote missing data for all alphabetic variables, codes -1, -2, and -3 may denote missing data for all dummy variables, and codes 7, 8, and 9 may represent missing data for all other variables.  <br>&nbsp;&nbsp;- In yet other instances, standard codes may depend on the column width of each variable, e.g., 99 may denote 'no answer' for all two column variables and 999 may denote the same for all three column variables. |

**ICPSR Input Guidance:** This element is displayed to end-users in version history.

**Examples:** 

```json
[
    "Created variable labels and/or value labels.",
    "Standardized missing values.",
    "Checked for undocumented or out-of-range codes."
]
```

```json
[
    "Created online analysis version with question text."
]
```

### <a name="weight"></a>31. Weight         

**Description:** The weight variables and the criteria for using them in data analysis or other information about how the data are weighted if no weight variables are present.

**Required**: No

**Repeatable**: No

**Accepted Values**: Text

**Controlled Vocabulary:** N/A

**Usage Notes:** Weight includes any information about weighting variables in the data, as well as any other weight information provided by the Principal Investigator. If a weighting formula or coefficient was developed, provide this formula, define its elements, and indicate how the formula is applied to the data. It is acceptable to summarize information contained in documentation and refer users to that documentation for more information.

**Examples:** 

```json
"A weight variable with two implied decimal places has been included and must be used in any analysis."
```

```json
"Both the TransPop and Cisgender datasets have the same variable named WEIGHT as the weighting variable. The combination datasets have a set of three weight variables (WEIGHT_TRANSPOP, WEIGHT_CISGENDER, WEIGHT_CISGENDER_TRANSPOP). The results will be representative of the sample when the weight is applied. Pages 41 and 42 of the user guide contain instructions that detail how to apply the final sample weight using Stata or SPSS."
```

```json
"The 1996 NES dataset includes two final person-level analysis weights which incorporate sampling, nonresponse, and post-stratification factors. One weight (variable #4) is for longitudinal micro-level analysis using the 1996 NES Panel. The other weight (variable #3) is for analysis of the 1996 NES combined sample (Panel component cases plus Cross-section supplement cases). In addition, a Time Series Weight (variable #5) which corrects for Panel attrition was constructed. This weight should be used in analyses which compare the 1996 NES to earlier unweighted National Election Study data collections."
```

### <a name="response_rates"></a>32. Response Rates         

**Description:** The percentage of respondents in the sample who participated in the data collection.

**Required**: No

**Repeatable**: No

**Accepted Values**: Text

**Controlled Vocabulary:** N/A

**Usage Notes:** Only applicable if the data were collected with a survey instrument and the response rates are provided.

**Examples:** 

```json
"The overall response rate for this survey was 20.22%; 72.6% for existing panelists and 10.4% for new panelists, using AAPOR Response Rate 1."
```

```json
"The response rate for the pre-election interview was 55.8 percent (66.5 percent for the Panel and 35.2 percent for the Fresh Cross). The response rate for the post-election interview was 89.1 (90.1 percent for the Panel and 85.2 percent for the Fresh Cross)."
```

```json
"Not applicable."
```

### <a name="scale"></a>33. Scale         

**Description:** Any commonly known scales used to collect data for the data collection (e.g., MMPI, CPI, the Census Occupational Codes, etc.).

**Required**: No

**Repeatable**: No

**Accepted Values**: Text

**Controlled Vocabulary:** N/A

**Usage Notes:** The inclusion of a common scale should be identified in the documentation associated with this dataset and confirmed by variable names or labels. The scales can be cited either as a list or described in full sentences. If the questionnaire used has a finite list of responses (e.g., 'Always, Sometimes, Rarely, Never' or Strongly Agree, Agree, Disagree, Strongly Disagree'), it is acceptable for this element to note 'A Likert-type scale was used,' or 'Several Likert-type scales were used.' However, it is not required to note Likart-type scales in situations where only such scales were used, given their ubiquity.  

**Examples:** 

```json
[
    "The baseline data collection included one scale - the CES-D index for maternal depression [Cole, J. C., Rabin, A. S., Smith, T. L., and Kaufman, A. S. (2004). Development and validation of a Rasch-derived CES-D short form. Psychological assessment, 16(4), 360]. All scales used for outcomes at ages 1 through 3 are listed in Appendix Tables 1 and 2 in the User Guide. Please refer to the User Guide and P.I. Codebook, available under the 'Data and Documentation' tab, for details."
]
```

```json
[
    "Squires, J., Bricker, D. D., and Twombly, E. (2009). Ages and stages questionnaires. Baltimore, MD: Paul H. Brookes.",
    "Briggs-Gowan, M. J., Carter, A. S., Irwin, J. R., Wachtel, K., and Cicchetti, D. V. (2004). The Brief Infant-Toddler Social and Emotional Assessment: screening for social-emotional problems and delays in competence. Journal of pediatric psychology, 29(2), 143-155.",
    "Yu, L., Buysse, D. J., Germain, A., Moul, D. E., Stover, A., Dodds, N. E., ... and Pilkonis, P. A. (2012). Development of short forms from the PROMIS sleep disturbance and sleep-related impairment item banks. Behavioral sleep medicine, 10(1), 6-24."
]
```

### <a name="unit_of_observation"></a>34. Unit of Observation         

**Description:** The object(s) of analysis for the data collection, such as an organization, individual, or household.

**Required**: No

**Repeatable**: Yes

**Accepted Values**: Text

**Controlled Vocabulary:** N/A

**Usage Notes:** Use a brief phrase, for example: 'Individual,' 'Family,' 'Household,' or 'Organization'; when possible, conform to the [DDI Controlled Vocabulary for Analysis Unit](https://vocabularies.cessda.eu/vocabulary/AnalysisUnit?v=2.1.3&lang=en).

**Examples:** 

```json
[
    "Organization"
]
```

```json
[
    "Individual, Household"
]
```

```json
[
    "Family"
]
```

### <a name="smallest_geographic_unit"></a>35. Smallest Geographic Unit         

**Description:** The smallest geographic unit (e.g., state or census tract) used in the dataset.

**Required**: No

**Repeatable**: No

**Accepted Values**: Text

**Controlled Vocabulary:** N/A

**Usage Notes:** Geographic Unit is intended to represent specific, known geography -- e.g., county, census district, FIPS code, electoral district, and any other conveyor of specific geography that is represented by a variable.  

If the data do not include a geographic variable by which the data can be analyzed, this element is not indicated. If all the cases are from a single state, but the cases are not subdivided geographically within that state, then 'state' is not indicated.  

This element is only meant to convey specific, known, geography. If there is a variable indicating which testing site a survey was taken at, but the locations of the testing sites were masked by the PI, this element is likely not indicated.  

**ICPSR Input Guidance:** The following is a non-exhaustive list of potential entries: census tract, city, congressional district, Core-Based Statistical Area (CBSA), country, county, Federal Court District, FIPS code, jurisdiction, neighborhood, school district, state, ZIP code.

**Examples:** 

```json
"state"
```

```json
"Census tract"
```

```json
"precinct"
```

### <a name="restrictions"></a>36. Restrictions         

**Description:** Rules about how the data collection can be accessed or used.

**Required**: No

**Repeatable**: No

**Accepted Values**: Text

**Controlled Vocabulary:** N/A

**Usage Notes:** Restrictions informs users that access to certain variables in a collection may be limited, and that they should contact ICPSR directly to inquire about accessing them.

**Example:** 

```json
"These data may not be used for any purpose other than statistical reporting and analysis. Use of these data to learn the identity of any person or establishment is strictly prohibited. To protect respondent privacy, certain files within this data collection are restricted from general dissemination. To obtain these files, researchers must agree to the terms and conditions of a Restricted Data Use Agreement in accordance with existing ICPSR servicing policies."
```

### <a name="membership_required"></a>37. Membership Required         

**Description:** The availability of the data collection in terms of ICPSR membership. Members-only data may only be downloaded by affiliates of ICPSR member institutions who contribute funding to support the data.

**Required**: No

**Repeatable**: No

**Accepted Values**: Text

**Controlled Vocabulary:** N/A

**Usage Notes:** True indicates the data are only available to members; false indicates that the data are available to all users. Additional access restrictions (i.e., due to sensitive data or disclosure risks) may still apply.

**Examples:** 

```json
"True"
```

```json
"False"
```

### <a name="restricted_access"></a>38. Restricted Access         

**Description:** General indication of any access restrictions associated with the data collection. More detailed information is provided in the Restrictions element.

**Required**: No

**Repeatable**: No

**Accepted Values**: Text

**Controlled Vocabulary:** N/A

**Usage Notes:** True indicates that an access restriction is associated with the data collection; false indicates no access restrictions are present. Additional membership requirements may still apply.

**Examples:** 

```json
"True"
```

```json
"False"
```

### <a name="changes_to_collection"></a>39. Changes to Collection         

**Description:** A record of how the data collection has changed over time.

**Required**: No

**Repeatable**: Yes

**Accepted Values**: Multi-part element; see subfield definitions for more information.

**Controlled Vocabulary:** N/A

**Usage Notes:** Textual changes are recorded only when data or documentation files are updated or added to the data collection (and the Version number is incremented).

#### <a name="autogenerated_heading_20"></a>39.1. Subfields:

| Property                                   | Required? | Repeatable? | Accepted Values | Description                                                                    |
| ------------------------------------------ | --------- | ----------- | --------------- | ------------------------------------------------------------------------------ |
| [Date](#changes_to_collection_items_date ) | No        | No          | Text            | The date on which an update occurred. ICPSR automatically generates this date. |
| [Note](#changes_to_collection_items_note ) | No        | No          | Text            | An explanation of the nature of the update.                                    |

##### <a name="changes_to_collection_items_date"></a>39.1.1. Date

**Description:** The date on which an update occurred. ICPSR automatically generates this date.

**Required**: No

**Repeatable**: No

**Accepted Values**: Text (formatted as a date)

**Examples:** 

```json
"2006-03-30"
```

```json
"2019-05-05"
```

##### <a name="changes_to_collection_items_note"></a>39.1.2. Note

**Description:** An explanation of the nature of the update.

**Required**: No

**Repeatable**: No

**Accepted Values**: Text

**Examples:** 

```json
"File CB3025.ALL.PDF was removed from any previous datasets and flagged as a study-level file, so that it will accompany all downloads."
```

```json
"The data producer provided additional data files."
```

```json
"SAS and SPSS setup files were created."
```

```json
"The codebook descriptions of variables TANSUP, EMOSUP, and SOCSUP were corrected."
```

###### Complete Changes to Collection Examples (with Subfields):
```json
[
    {
        "date": "2003-09-10",
        "note": "A variable specifying the date of interview has been added to the collection."
    },
    {
        "date": "2003-12-09",
        "note": "The codebook descriptions of variables TANSUP, EMOSUP, and SOCSUP were corrected."
    }
]
```

### <a name="series"></a>40. Series         

**Description:** A named collection of related studies.

**Required**: No

**Repeatable**: No

**Accepted Values**: Text

**Controlled Vocabulary:** [ICPSR Series](https://www.icpsr.umich.edu/web/ICPSR/search/series)

**Usage Notes:** Typically the studies in an ICPSR series are produced by the same group of investigators, and either explore different facets of the same topic, or repeat the same investigation over time. Each series name is given in title case (all major words are capitalized, while minor words are lowercased) and ends with the word 'Series'.

**Examples:** 

```json
[
    "American National Election Study (ANES) Series"
]
```

```json
[
    "Census of Population and Housing, 1990 [United States] Series"
]
```

```json
[
    "National Black Election Study Series"
]
```

```json
[
    "Study of Women's Health Across the Nation (SWAN) Series"
]
```

### <a name="classification"></a>41. Classification         

**Description:** Topics used to organize data collections and help users explore the ICPSR catalog.

**Required**: No

**Repeatable**: Yes

**Accepted Values**: Text

**Controlled Vocabulary:** [ICPSR Topic Classifications](https://www.icpsr.umich.edu/web/pages/ICPSR/access/subject.html)

**ICPSR Input Guidance:** When there are multiple subclassifications, the smallest (most detailed) one is chosen to represent the data collection. Each data collection must have at least one ICPSR classification, as well as a classification from the collection's home archive. Classifications can also be used to cross-list a study among multiple archives. Curators should choose the topical classifications that best match the study's focus.

**Examples:** 

```json
[
    "I.A.2. Census Enumerations: Historical and Contemporary Population Characteristics, United States, American Housing Survey Series"
]
```

```json
[
    "XVII.C.1. Social Institutions and Behavior, Socialization, Students, and Youth, United States"
]
```

### <a name="filesets"></a>42. Filesets         

**Description:** The grouping of files in the data collection.

**Required**: No

**Repeatable**: Yes

**Accepted Values**: Multi-part element; see subfield definitions for more information.

**Controlled Vocabulary:** N/A

**Usage Notes:** Filesets are used at ICPSR to make a convenient package for description, discovery, preservation and dissemination -- a package that is smaller than the data collection but larger than the individual file. A fileset typically contains a single file of statistical data plus additional files that support the data -- such as setups for statistical software, documentation, and alternative data representations. Every ICPSR data collection with at least one file must have at least one defined Fileset; a data collection may have multiple filesets. Each Fileset has a Number, and may also have a Name and an SDA (Survey Documentation and Analysis) Note.

#### <a name="autogenerated_heading_22"></a>42.1. Subfields:

| Property                              | Required? | Repeatable? | Accepted Values | Description                                                                                               |
| ------------------------------------- | --------- | ----------- | --------------- | --------------------------------------------------------------------------------------------------------- |
| [Number](#filesets_items_number )     | Yes       | No          | Number          | A number that uniquely identifies a 'part' or component file that is associated with the data collection. |
| [Name](#filesets_items_name )         | No        | No          | Text            | A brief title used to distinguish each fileset within a data collection.                                  |
| [SDA Note](#filesets_items_sda_note ) | No        | No          | Text            | Additional information about the fileset for the purpose of helping online analysis users.                |

##### <a name="filesets_items_number"></a>42.1.1. Number

**Description:** A number that uniquely identifies a 'part' or component file that is associated with the data collection.

**Required**: Yes

**Repeatable**: No

**Accepted Values**: Number

**Usage Notes:** Fileset numbers are typically (but not always) consecutive integers beginning with 1. (In some cases, the number may be drawn from an external resource, such as FIPS state and county codes.) The numbers correspond to the 'part numbers' embedded in ICPSR standard filenames.

**Examples:** 

```json
1
```

```json
2
```

```json
3
```

##### <a name="filesets_items_name"></a>42.1.2. Name

**Description:** A brief title used to distinguish each fileset within a data collection.

**Required**: No

**Repeatable**: No

**Accepted Values**: Text

**Controlled Vocabulary:** N/A

**Usage Notes:** Fileset Names are required for data collections that include multiple Filesets. If a data collection includes only one fileset, a Fileset Name is not included. Fileset Names use title case (all main words are capitalized) and do not begin with articles (a, the) or dates.

**Examples:** 

```json
"Each Region, Wealth Summary: Middle Colonies (MIDLCOL)"
```

```json
"Each Region, Wealth Summary: New England (NEWENGL)"
```

```json
"Northbound Public-Use Data"
```

```json
"Northbound Restricted-Use Data"
```

##### <a name="filesets_items_sda_note"></a>42.1.3. SDA Note

**Description:** Additional information about the fileset for the purpose of helping online analysis users.

**Required**: No

**Repeatable**: No

**Accepted Values**: Text

**Controlled Vocabulary:** N/A

**Examples:** 

```json
"Please note that the AABS provides estimates for 32 states. It also supplies arts participation estimates for 11 metropolitan areas. Users are encouraged to review the Data Collection Notes on the Study Description page for specific states and metropolitan areas."
```

```json
"Please note that the replicate weights are needed to obtain accurate standard error estimates. Users are advised to download the data to use the replicate weights. Users should refer to the study description page or User Guide for further details regarding weights."
```

###### Complete Filesets Examples (with Subfields):
```json
[
    {
        "number": 1
    }
]
```

```json
[
    {
        "number": 1,
        "name": "Northbound Public-Use Data"
    },
    {
        "number": 2,
        "name": "Northbound Restricted-Use Data"
    }
]
```

```json
[
    {
        "number": 1,
        "name": "Original File"
    },
    {
        "number": 2,
        "name": "Replicate Weight File",
        "sda_note": "Please note that the replicate weights are needed to obtain accurate standard error estimates. Users are advised to download the data to use the replicate weights. Users should refer to the study description page or User Guide for further details regarding weights."
    }
]
```


## ICPSR Metadata Schema Version History

| Date | Version | Note |
|------|---------|------|
| April 11, 2025 | v1.2 | Updated field definitions to improve clarity. |
| June 28, 2024 | v1.1 | Removed guidance regarding null entries for National Institute of Justice studies. Several fields previously required "None" when otherwise a field would be left blank. Updated internal guidance for 'external source id' and 'funding purpose' elements. Added 'study number' and distributor 'order' elements to address earlier oversights. |
| Oct. 30, 2023 | v1 | Initial release and publication of the ICPSR Metadata Schema. |

