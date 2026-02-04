# DRAFT ICPSR RDE Metadata Schema Documentation

Last updated: February 04, 2026

## Metadata Elements: Overview

| Property | Required? | Repeatable? | Accepted Values | Description |
| -------- | --------- | ----------- | --------------- | ----------- |
| [Alternate Titles](#alternate-titles) | No | Yes | Text | The alternate name(s) or acronym(s) commonly used to refer to the data collection. |
| [Citation](#citation) | No | No | Text | The official way to reference the data collection in writing. |
| [Collection Dates](#collection-dates) | No | Yes | Multi-part element; see subfields | The date(s) when the data were physically collected. |
| [Collection Modes](#collection-modes) | No | Yes | Multi-part element; see subfields | The method(s) or procedure(s) used to collect the data. |
| [Data Management Plan](#data-management-plan) | No | No | Text | A link to the data management plan (preferably a persistent identifier such as a DOI). |
| [Data Source Types](#data-source-types) | No | Yes | Multi-part element; see subfields | The source(s) of the data as collected by the Principal Investigators. |
| [Distributors](#distributors) | No | Yes | Multi-part element; see subfields | The organization(s) responsible for distributing the data collection. |
| [External Data Sources](#external-data-sources) | No | Yes | Text | The source of the data, when that source is external to the data collection and can be independently cited. |
| [Funding Sources](#funding-sources) | No | Yes | Multi-part element; see subfields | The sources of funding that supported the data collection. |
| [General Data Formats](#general-data-formats) | No | Yes | Multi-part element; see subfields | The file format types present in the data collection. |
| [Geographic Coverage Areas](#geographic-coverage-areas) | No | Yes | Multi-part element; see subfields | The geographic locations where the data refer or are related. |
| [ICPSR Subject Terms](#icpsr-subject-terms) | No | Yes | Multi-part element; see subfields | A controlled list of social science terms maintained by ICPSR and used to indicate topics related to the data collection. |
| [Journal of Economic Literature (JEL) Classification Codes](#journal-of-economic-literature-jel-classification-codes) | No | Yes | Multi-part element; see subfields | Classification codes used to categorize economic research. |
| [License](#license) | No | No | Multi-part element; see subfields | A license governing the data's use. |
| [Medical Subject Headings (MeSH) Terms](#medical-subject-headings-mesh-terms) | No | Yes | Multi-part element; see subfields | Biomedical and health-related terms from the National Library of Medicine that describe the data collection's topics. |
| [Nationally Representative Sample](#nationally-representative-sample) | No | No | Text | Indicates whether the data collection uses a sampling design intended to represent the demographics, behaviors, and/or characteristics of the entire nation. This typically involves probability-based methods that allow generalization. It does not include convenience samples that appear similar to the nation by chance. |
| [Notes](#notes) | No | Yes | Text | Important details about the data collection (like unique authoring, discrepancies, or processing information) that can't be recorded in other metadata elements. |
| [Organization](#organization) | No | No | Multi-part element; see subfields | An organization associated with an ICPSR data collection or service. |
| [Person](#person) | No | No | Multi-part element; see subfields | A person associated with an ICPSR data collection or service. |
| [Preregistration](#preregistration) | No | No | Text | A link to a research plan for the data collection (preferably a persistent identifier such as a DOI). |
| [Principal Investigators](#principal-investigators) | No | Yes | Multi-part element; see subfields | The key people or organizations responsible for the data collection, listed by importance. Each data collection requires at least one PI, either a person or an organization. |
| [Response Rates](#response-rates) | No | No | Text | The percentage of respondents in the sample who participated in the data collection. |
| [Sampling Note](#sampling-note) | No | No | Text | Supplemental information about the sampling process that does not fit neatly into the Sampling Procedure field. |
| [Sampling Procedures](#sampling-procedures) | No | Yes | Text | The type(s) of sample and sample design used to select survey respondents to represent the population. |
| [Scales](#scales) | No | No | Text | Any commonly known scales used to collect data for the data collection (e.g., MMPI, CPI, the Census Occupational Codes, etc.). |
| [Smallest Geographic Unit](#smallest-geographic-unit) | No | No | Multi-part element; see subfields | The smallest geographic unit (e.g., state or census tract) used in the dataset. |
| [Software Applications](#software-applications) | No | Yes | Multi-part element; see subfields | Software used by the principal investigator(s) to collect or analyze data, required to understand how the data were obtained or to reproduce results. |
| [Study Design](#study-design) | No | No | Text | The procedures used to contact participants and gather data. |
| [Summary](#summary) | No | No | Text | A description of the data collection that helps users understand its purpose, substance, and key topics. |
| [Time Methods](#time-methods) | No | Yes | Multi-part element; see subfields | The methods used to collect data over time, like snapshots at one point (cross-sectional) or repeatedly (longitudinal) to study changes or trends |
| [Time Periods](#time-periods) | No | Yes | Multi-part element; see subfields | The time period(s) to which the data refer, regardless of when the data were collected. |
| [Title](#title) | No | No | Text | The official title that describes what the data collection is about, its geographic scope, and the time period it covered. |
| [Units of Analysis](#units-of-analysis) | No | Yes | Multi-part element; see subfields | The object(s) of analysis for the data collection, such as an organization, individual, or household. |
| [Universe](#universe) | No | No | Text | The total group of persons or other entities (e.g., households or organizations) that were the object of research and to which analytic results refer. |
| [Variable Description](#variable-description) | No | No | Text | Significant variables (particularly demographic variables) in the data files. |
| [Version History](#version-history) | No | Yes | Multi-part element; see subfields | A record of how the data collection has changed over time. |
| [Weights](#weights) | No | No | Text | The weight variables and the criteria for using them in data analysis or other information about how the data are weighted if no weight variables are present. |

---
## Metadata Elements: Detailed Information

<a id="alternate-titles"></a>
### Alternate Titles

**Description:** The alternate name(s) or acronym(s) commonly used to refer to the data collection.

**Repeatable**: Yes

**Accepted Values**: Text

**Examples:**

```
[
  "Add Health Parent Study"
]
```

```
[
  "FACES 2009"
]
```

```
[
  "Survey of Consumers"
]
```

```
[
  "Eurobarometer 85.2"
]
```

**Examples:**
```
    Add Health Parent Study
```

```
    FACES 2009
```

```
    Survey of Consumers
```

```
    Eurobarometer 85.2
```


---

<a id="citation"></a>
### Citation

**Description:** The official way to reference the data collection in writing.

**Repeatable**: No

**Accepted Values**: Text

**Usage Notes:** The Citation is dynamically assembled from other entry fields in this format: PI (list). Title. Distributor (list), Issued Date. DOI. Note: ICPSR 'union catalog' records (i.e., external resource to which ICPSR links as a courtesy) do not have citations.

**Examples:**

```
    University of Michigan. Survey Research Center. Economic Behavior Program. Survey of Consumer Attitudes and Behavior, September 2018. Inter-university Consortium for Political and Social Research [distributor], 2021-11-18. https://doi.org/10.3886/ICPSR38121.v1
```

```
    United States Department of Justice. Office of Justice Programs. Office of Juvenile Justice and Delinquency Prevention. Juvenile Residential Facility Census, 2020 [United States]. Inter-university Consortium for Political and Social Research [distributor], 2024-07-15. https://doi.org/10.3886/ICPSR38914.v1
```

**Examples:**
```
    University of Michigan. Survey Research Center. Economic Behavior Program. Survey of Consumer Attitudes and Behavior, September 2018. Inter-university Consortium for Political and Social Research [distributor], 2021-11-18. https://doi.org/10.3886/ICPSR38121.v1
```

```
    United States Department of Justice. Office of Justice Programs. Office of Juvenile Justice and Delinquency Prevention. Juvenile Residential Facility Census, 2020 [United States]. Inter-university Consortium for Political and Social Research [distributor], 2024-07-15. https://doi.org/10.3886/ICPSR38914.v1
```


---

<a id="collection-dates"></a>
### Collection Dates

**Description:** The date(s) when the data were physically collected.

**Repeatable**: Yes

**Accepted Values**: Multi-part element; see subfield definitions for more information.

#### Subfields:

| Property | Required? | Repeatable? | Accepted Values | Description |
| -------- | --------- | ----------- | --------------- | ----------- |
| Start Date | Yes | No | Text | The start date of the data collection period. Must be in YYYY-MM-DD, YYYY-MM, or YYYY format with no spaces. |
| End Date | Yes | No | Text | The end date of the data collection period. Must be in YYYY-MM-DD, YYYY-MM, or YYYY format with no spaces. |
| Time Frame | No | No | Text | An optional free-text description of the data collection period, used for non-numeric dates (e.g., 'Fall 2012') or to add context when multiple dates are present. |

##### Start Date

**Description:** The start date of the data collection period. Must be in YYYY-MM-DD, YYYY-MM, or YYYY format with no spaces.

**Required**: Yes

**Repeatable**: No

**Accepted Values**: Text

**Examples:**

```json
"2000"
```

```json
"2019-10"
```

```json
"2021-03-01"
```

##### End Date

**Description:** The end date of the data collection period. Must be in YYYY-MM-DD, YYYY-MM, or YYYY format with no spaces.

**Required**: Yes

**Repeatable**: No

**Accepted Values**: Text

**Examples:**

```json
"2000"
```

```json
"2019-10"
```

```json
"2021-03-01"
```

##### Time Frame

**Description:** An optional free-text description of the data collection period, used for non-numeric dates (e.g., 'Fall 2012') or to add context when multiple dates are present.

**Required**: No

**Repeatable**: No

**Accepted Values**: Text

**Usage Notes:** The Time Frame should not simply restate the date(s) in words. For example, if the Collection Date starts in 2020-01, the Time Frame should repeat 'January 2020'.

**Examples:**

```json
"Fall 2001"
```

```json
"Student data"
```

###### Complete Examples (with Subfields):
```
    start_date: 2018
    end_date: 2018
    time_frame: Summer and Fall 2018
```

```
    start_date: 2020-10
    end_date: 2020-10
```


---

<a id="collection-modes"></a>
### Collection Modes

**Description:** The method(s) or procedure(s) used to collect the data.

**Repeatable**: Yes

**Accepted Values**: Multi-part element; see subfield definitions for more information.

#### Subfields:

| Property | Required? | Repeatable? | Accepted Values | Description |
| -------- | --------- | ----------- | --------------- | ----------- |
| Collection Mode | Yes | No | Text | A human-readable form of the term. |
| Collection Mode Code | Yes | No | Text | A machine-readable/-actionable form of the term. |
| Collection Mode URI | Yes | No | Text | The URI for the term. |

##### Collection Mode

**Description:** A human-readable form of the term.

**Required**: Yes

**Repeatable**: No

**Accepted Values**: Text

**Examples:**

```json
"Face-to-face interview: Computer-assisted (CAPI/CAMI)"
```

```json
"Measurements and tests"
```

```json
"Computer-based observation"
```

##### Collection Mode Code

**Description:** A machine-readable/-actionable form of the term.

**Required**: Yes

**Repeatable**: No

**Accepted Values**: Text

**Examples:**

```json
"Interview.FaceToFace.CAPIorCAMI"
```

```json
"MeasurementsAndTests"
```

```json
"Observation.ComputerBased"
```

##### Collection Mode URI

**Description:** The URI for the term.

**Required**: Yes

**Repeatable**: No

**Accepted Values**: Text

###### Complete Examples (with Subfields):
```
    label: Face-to-face interview: Computer-assisted (CAPI/CAMI)
    code: Interview.FaceToFace.CAPIorCAMI
    uri: https://example.com/collection_modes/234
```

```
    label: Measurements and tests
    code: MeasurementsAndTests
    uri: https://example.com/collection_modes/972
```

```
    label: Computer-based observation
    code: Observation.ComputerBased
    uri: https://example.com/collection_modes/113
```


---

<a id="data-management-plan"></a>
### Data Management Plan

**Description:** A link to the data management plan (preferably a persistent identifier such as a DOI).

**Repeatable**: No

**Accepted Values**: Text

**Examples:**

```
    https://doi.org/10.1000/182
```

**Examples:**
```
    https://doi.org/10.1000/182
```


---

<a id="data-source-types"></a>
### Data Source Types

**Description:** The source(s) of the data as collected by the Principal Investigators.

**Repeatable**: Yes

**Accepted Values**: Multi-part element; see subfield definitions for more information.

#### Subfields:

| Property | Required? | Repeatable? | Accepted Values | Description |
| -------- | --------- | ----------- | --------------- | ----------- |
| Data Source Type | Yes | No | Text | A human-readable form of the term. |
| Data Source Type Code | Yes | No | Text | A machine-readable/-actionable form of the term. |
| Data Source Type URI | Yes | No | Text | The URI for the term. |

##### Data Source Type

**Description:** A human-readable form of the term.

**Required**: Yes

**Repeatable**: No

**Accepted Values**: Text

**Examples:**

```json
"Registers/Records/Accounts: Medical/Clinical"
```

```json
"Events/Interactions"
```

```json
"Other"
```

##### Data Source Type Code

**Description:** A machine-readable/-actionable form of the term.

**Required**: Yes

**Repeatable**: No

**Accepted Values**: Text

**Examples:**

```json
"RegistersRecordsAccounts.MedicalClinical"
```

```json
"EventsInteractions"
```

```json
"Other"
```

##### Data Source Type URI

**Description:** The URI for the term.

**Required**: Yes

**Repeatable**: No

**Accepted Values**: Text

###### Complete Examples (with Subfields):
```
    label: Registers/Records/Accounts: Medical/Clinical
    code: RegistersRecordsAccounts.MedicalClinical
    uri: https://example.com/data_source_type/123
```

```
    label: Events/Interactions
    code: EventsInteractions
    uri: https://example.com/data_source_type/234
```

```
    label: Other
    code: Other
    uri: https://example.com/data_source_type/737
```


---

<a id="distributors"></a>
### Distributors

**Description:** The organization(s) responsible for distributing the data collection.

**Repeatable**: Yes

**Accepted Values**: Multi-part element; see subfield definitions for more information.

#### Subfields:

| Property | Required? | Repeatable? | Accepted Values | Description |
| -------- | --------- | ----------- | --------------- | ----------- |
| Organization | Yes | No | Multi-part element; see subfields | An organization associated with an ICPSR data collection or service. |
| Order | Yes | No | Number | The order of importance for the distributors of the data collection. |

##### Organization

**Description:** An organization associated with an ICPSR data collection or service.

**Required**: Yes

**Repeatable**: No

**Accepted Values**: Multi-part element; see subfield definitions for more information.

**Examples:**

```json
{
  "name": "Urban Institute",
  "name_code": "1234",
  "name_uri": "https://icpsr.example.com/organizations/1234",
  "ror": "https://ror.org/017pz3h73",
  "email": "info@urban.institute"
}
```

##### Order

**Description:** The order of importance for the distributors of the data collection.

**Required**: Yes

**Repeatable**: No

**Accepted Values**: Number

**Usage Notes:** A value of '0' indicates the primary distributor, '1' the second, and so forth.

**Examples:**

```json
0
```

```json
1
```

```json
2
```

```json
3
```

###### Complete Examples (with Subfields):
```
    organization: {'name': 'Inter-university Consortium for Political and Social Research', 'name_code': '1234', 'name_uri': 'https://icpsr.example.com/organizations/1234', 'ror': 'https://ror.org/017pz3h73'}
    order: 0
```

```
    organization: {'name': 'GESIS', 'name_code': '2345', 'name_uri': 'https://icpsr.example.com/organizations/2345', 'ror': 'https://ror.org/018afyw53'}
    order: 1
```

```
    organization: {'name': 'Roper Center for Public Opinion Research', 'name_code': '1234', 'name_uri': 'https://icpsr.example.com/organizations/1234'}
    order: 0
```


---

<a id="external-data-sources"></a>
### External Data Sources

**Description:** The source of the data, when that source is external to the data collection and can be independently cited.

**Repeatable**: Yes

**Accepted Values**: Text

**Usage Notes:** External data sources include books, journal articles, administrative records, agency-sponsored surveys, and machine-readable files. Each source includes at minimum the title, author, publication year, and journal (if applicable). Any citation format is accepted.

**Examples:**

```
[
  "'Voting Scores.' Congressional Quarterly Almanac 33 (1977), 487-498"
]
```

```
[
  "United States Bureau of the Census Economic Surveys, 1998-2000",
  "United States Congressional Record, 1989"
]
```

```
[
  "Annual Company Organization Survey, 2003"
]
```

**Examples:**
```
    'Voting Scores.' Congressional Quarterly Almanac 33 (1977), 487-498
```

```
    United States Bureau of the Census Economic Surveys, 1998-2000
```

```
    United States Congressional Record, 1989
```

```
    Annual Company Organization Survey, 2003
```


---

<a id="funding-sources"></a>
### Funding Sources

**Description:** The sources of funding that supported the data collection.

**Repeatable**: Yes

**Accepted Values**: Multi-part element; see subfield definitions for more information.

#### Subfields:

| Property | Required? | Repeatable? | Accepted Values | Description |
| -------- | --------- | ----------- | --------------- | ----------- |
| Organization | Yes | No | Multi-part element; see subfields | An organization associated with an ICPSR data collection or service. |
| Funding Awards | No | Yes | Multi-part element; see subfields | Financial support for the data collection. |
| Order | Yes | No | Number | Internal ICPSR field used to determine the order of importance for the funders associated with the data collection. |

##### Organization

**Description:** An organization associated with an ICPSR data collection or service.

**Required**: Yes

**Repeatable**: No

**Accepted Values**: Multi-part element; see subfield definitions for more information.

**Examples:**

```json
{
  "name": "Urban Institute",
  "name_code": "1234",
  "name_uri": "https://icpsr.example.com/organizations/1234",
  "ror": "https://ror.org/017pz3h73",
  "email": "info@urban.institute"
}
```

##### Funding Awards

**Description:** Financial support for the data collection.

**Required**: No

**Repeatable**: No

**Accepted Values**: Multi-part element; see subfield definitions for more information.

##### Order

**Description:** Internal ICPSR field used to determine the order of importance for the funders associated with the data collection.

**Required**: Yes

**Repeatable**: No

**Accepted Values**: Number

**Examples:**

```json
0
```

```json
1
```

```json
2
```

```json
3
```

###### Complete Examples (with Subfields):
```
    organization: {'name': 'Robert Wood Johnson Foundation', 'name_code': '5643', 'name_uri': 'https://icpsr.example.com/organizations/5643', 'ror': 'https://ror.org/02ymmdj85'}
    grants: [{'grant_number': 'MDR-8550085'}, {'grant_number': 'MDR-8550204'}]
    order: 0
```

```
    organization: {'name': 'United States Department of Justice. Office of Justice Programs. Bureau of Justice Statistics', 'name_code': '2342', 'name_uri': 'https://icpsr.example.com/organizations/2342', 'ror': 'https://ror.org/0006s4z66'}
    grants: [{'grant_number': 'SES-1835721', 'grant_uri': 'https://doi.org/10.35802/000000'}]
    order: 1
```

```
    organization: {'name': 'Acme Foundation'}
    order: 0
```


---

<a id="general-data-formats"></a>
### General Data Formats

**Description:** The file format types present in the data collection.

**Repeatable**: Yes

**Accepted Values**: Multi-part element; see subfield definitions for more information.

#### Subfields:

| Property | Required? | Repeatable? | Accepted Values | Description |
| -------- | --------- | ----------- | --------------- | ----------- |
| General Data Format | Yes | No | Text | A human-readable form of the term. |
| General Data Format Code | Yes | No | Text | A machine-readable/-actionable form of the term. |
| General Data Format URI | Yes | No | Text | The URI for the term. |

##### General Data Format

**Description:** A human-readable form of the term.

**Required**: Yes

**Repeatable**: No

**Accepted Values**: Text

**Examples:**

```json
"Text"
```

```json
"Still image"
```

```json
"Numeric"
```

##### General Data Format Code

**Description:** A machine-readable/-actionable form of the term.

**Required**: Yes

**Repeatable**: No

**Accepted Values**: Text

**Examples:**

```json
"Text"
```

```json
"StillImage"
```

```json
"Numeric"
```

##### General Data Format URI

**Description:** The URI for the term.

**Required**: Yes

**Repeatable**: No

**Accepted Values**: Text

###### Complete Examples (with Subfields):
```
    label: Text
    code: Text
    uri: https://example.com/general_data_format/972
```

```
    label: Still image
    code: StillImage
    uri: https://example.com/general_data_format/234
```

```
    label: Numeric
    code: Numeric
    uri: https://example.com/general_data_format/563
```


---

<a id="geographic-coverage-areas"></a>
### Geographic Coverage Areas

**Description:** The geographic locations where the data refer or are related.

**Repeatable**: Yes

**Accepted Values**: Multi-part element; see subfield definitions for more information.

#### Subfields:

| Property | Required? | Repeatable? | Accepted Values | Description |
| -------- | --------- | ----------- | --------------- | ----------- |
| City | No | No | Text | A town, city, or similar political entity covered in a data collection |
| County | No | No | Text | A county or similar administrative area covered in a data collection |
| State | No | No | Text | A state, province, canton or similar political entity covered in a data collection |
| Country | Yes | No | Text | A country covered in a data collection |
| Geographic Coverage Area URI | No | No | Text | The unique identifier for the geographic coverage area. |

##### City

**Description:** A town, city, or similar political entity covered in a data collection

**Required**: No

**Repeatable**: No

**Accepted Values**: Text

**Examples:**

```json
"Ann Arbor"
```

```json
"Hanover"
```

```json
"Chongqing"
```

##### County

**Description:** A county or similar administrative area covered in a data collection

**Required**: No

**Repeatable**: No

**Accepted Values**: Text

**Examples:**

```json
"Monroe County"
```

```json
"Washtenaw County"
```

```json
"Cuyahoga County"
```

##### State

**Description:** A state, province, canton or similar political entity covered in a data collection

**Required**: No

**Repeatable**: No

**Accepted Values**: Text

**Examples:**

```json
"Michigan"
```

```json
"Manitoba"
```

```json
"Yunnan"
```

##### Country

**Description:** A country covered in a data collection

**Required**: Yes

**Repeatable**: No

**Accepted Values**: Text

**Examples:**

```json
"United States"
```

```json
"China"
```

```json
"Ghana"
```

##### Geographic Coverage Area URI

**Description:** The unique identifier for the geographic coverage area.

**Required**: No

**Repeatable**: No

**Accepted Values**: Text

**Examples:**

```json
"https://www.geonames.org/4990729/"
```

```json
"https://www.geonames.org/6269554"
```

###### Complete Examples (with Subfields):
```
    city: Cleveland
    state: Ohio
    country: United States
    uri: https://www.geonames.org/5150529
```

```
    city: Pittsburgh
    state: Pennsylvania
    country: United States
    uri: https://www.geonames.org/5206379
```

```
    country: Germany
```


---

<a id="icpsr-subject-terms"></a>
### ICPSR Subject Terms

**Description:** A controlled list of social science terms maintained by ICPSR and used to indicate topics related to the data collection.

**Repeatable**: Yes

**Accepted Values**: Multi-part element; see subfield definitions for more information.

#### Subfields:

| Property | Required? | Repeatable? | Accepted Values | Description |
| -------- | --------- | ----------- | --------------- | ----------- |
| ICPSR Subject Term | Yes | No | Text | A human-readable form of the subject term. |
| ICPSR Subject Term Code | Yes | No | Text | A machine-readable/-actionable form of the subject term. |
| ICPSR Subject Term URI | Yes | No | Text | The URI for the subject term. |

##### ICPSR Subject Term

**Description:** A human-readable form of the subject term.

**Required**: Yes

**Repeatable**: No

**Accepted Values**: Text

**Examples:**

```json
"abduction"
```

```json
"ability"
```

```json
"Abolition movement"
```

##### ICPSR Subject Term Code

**Description:** A machine-readable/-actionable form of the subject term.

**Required**: Yes

**Repeatable**: No

**Accepted Values**: Text

**Examples:**

```json
"20391"
```

```json
"24123"
```

```json
"23632"
```

##### ICPSR Subject Term URI

**Description:** The URI for the subject term.

**Required**: Yes

**Repeatable**: No

**Accepted Values**: Text

**Examples:**

```json
"https://www.icpsr.umich.edu/web/ICPSR/thesaurus/10001/terms/20391"
```

```json
"https://www.icpsr.umich.edu/web/ICPSR/thesaurus/10001/terms/24040"
```

###### Complete Examples (with Subfields):
```
    label: biographical data
    code: 20391
    uri: https://www.icpsr.umich.edu/web/ICPSR/thesaurus/10001/terms/20391
```

```
    label: age
    code: 24123
    uri: https://www.icpsr.umich.edu/web/ICPSR/thesaurus/10001/terms/24123
```

```
    label: happiness
    code: 25624
    uri: https://www.icpsr.umich.edu/web/ICPSR/thesaurus/10001/terms/25624
```


---

<a id="journal-of-economic-literature-jel-classification-codes"></a>
### Journal of Economic Literature (JEL) Classification Codes

**Description:** Classification codes used to categorize economic research.

**Repeatable**: Yes

**Accepted Values**: Multi-part element; see subfield definitions for more information.

#### Subfields:

| Property | Required? | Repeatable? | Accepted Values | Description |
| -------- | --------- | ----------- | --------------- | ----------- |
| JEL Classification Term | Yes | No | Text | A human-readable form of the term. |
| JEL Classification Code | No | No | Text | A machine-readable/-actionable form of the term. |
| JEL Classification URI | No | No | Text | The URI for the JEL classification code. |

##### JEL Classification Term

**Description:** A human-readable form of the term.

**Required**: Yes

**Repeatable**: No

**Accepted Values**: Text

**Examples:**

```json
"A12 Relation of Economics to Other Disciplines"
```

```json
"B00 History of Economic Thought, Methodology, and Heterodox Approaches"
```

##### JEL Classification Code

**Description:** A machine-readable/-actionable form of the term.

**Required**: No

**Repeatable**: No

**Accepted Values**: Text

**Examples:**

```json
"a12"
```

```json
"b00"
```

```json
"n22"
```

##### JEL Classification URI

**Description:** The URI for the JEL classification code.

**Required**: No

**Repeatable**: No

**Accepted Values**: Text

**Examples:**

```json
"http://example.com/jel/a12"
```

```json
"http://example.com/jel/b00"
```

###### Complete Examples (with Subfields):
```
    label: A12 Relation of Economics to Other Disciplines
    code: a12
    uri: http://example.com/jel/a12
```

```
    label: B00 History of Economic Thought, Methodology, and Heterodox Approaches
    code: b00
    uri: http://example.com/jel/b00
```

```
    label: N22 Economic History: Financial Markets and Institutions: U.S.; Canada: 1913-
    code: n22
    uri: http://example.com/jel/n22
```


---

<a id="license"></a>
### License

**Description:** A license governing the data's use.

**Repeatable**: No

**Accepted Values**: Multi-part element; see subfield definitions for more information.

**Examples:**

```
{
  "name": "Creative Commons Attribution Non Commercial 4.0 International",
  "code": "CC-BY-NC-4.0",
  "uri": "https://creativecommons.org/licenses/by-nc/4.0/"
}
```

**Examples:**
```
    name: Creative Commons Attribution Non Commercial 4.0 International
    code: CC-BY-NC-4.0
    uri: https://creativecommons.org/licenses/by-nc/4.0/
```


---

<a id="medical-subject-headings-mesh-terms"></a>
### Medical Subject Headings (MeSH) Terms

**Description:** Biomedical and health-related terms from the National Library of Medicine that describe the data collection's topics.

**Repeatable**: Yes

**Accepted Values**: Multi-part element; see subfield definitions for more information.

#### Subfields:

| Property | Required? | Repeatable? | Accepted Values | Description |
| -------- | --------- | ----------- | --------------- | ----------- |
| MeSH Subject Term | Yes | No | Text | A human-readable form of the subject term. |
| MeSH Subject Term Code | Yes | No | Text | A machine-readable/-actionable form of the subject term. |
| MeSH Subject Term URI | Yes | No | Text | The URI for the subject term as maintained in MeSH. |

##### MeSH Subject Term

**Description:** A human-readable form of the subject term.

**Required**: Yes

**Repeatable**: No

**Accepted Values**: Text

**Examples:**

```json
"anxiety"
```

```json
"brain waves"
```

##### MeSH Subject Term Code

**Description:** A machine-readable/-actionable form of the subject term.

**Required**: Yes

**Repeatable**: No

**Accepted Values**: Text

**Examples:**

```json
"D001007"
```

```json
"D058256"
```

##### MeSH Subject Term URI

**Description:** The URI for the subject term as maintained in MeSH.

**Required**: Yes

**Repeatable**: No

**Accepted Values**: Text

**Usage Notes:** Enter the MeSH RDF Unique Identifier.

**Examples:**

```json
"http://id.nlm.nih.gov/mesh/D001007"
```

```json
"http://id.nlm.nih.gov/mesh/D058256"
```

###### Complete Examples (with Subfields):
```
    label: anxiety
    code: D001007
    uri: http://id.nlm.nih.gov/mesh/D001007
```

```
    label: brain waves
    code: D058256
    uri: http://id.nlm.nih.gov/mesh/D058256
```


---

<a id="nationally-representative-sample"></a>
### Nationally Representative Sample

**Description:** Indicates whether the data collection uses a sampling design intended to represent the demographics, behaviors, and/or characteristics of the entire nation. This typically involves probability-based methods that allow generalization. It does not include convenience samples that appear similar to the nation by chance.

**Repeatable**: No

**Accepted Values**: Text

**Examples:**

```
    Yes
```

```
    No
```

**Examples:**
```
    Yes
```

```
    No
```


---

<a id="notes"></a>
### Notes

**Description:** Important details about the data collection (like unique authoring, discrepancies, or processing information) that can't be recorded in other metadata elements.

**Repeatable**: Yes

**Accepted Values**: Text

**Examples:**

```
[
  "Information on the Index of Consumer Sentiment, the Index of Current Economic Conditions, and the Index of Consumer Expectations and how they were created can be found in the P.I. Codebook",
  "Dataset 1 should be attributed to Jane Doe while datasets 2-6 should be attributed to John Doe"
]
```

```
[
  "Additional information on the Survey of Consumers can be found by visiting the Survey of Consumers Website"
]
```

**Examples:**
```
    Information on the Index of Consumer Sentiment, the Index of Current Economic Conditions, and the Index of Consumer Expectations and how they were created can be found in the P.I. Codebook
```

```
    Dataset 1 should be attributed to Jane Doe while datasets 2-6 should be attributed to John Doe
```

```
    Additional information on the Survey of Consumers can be found by visiting the Survey of Consumers Website
```


---

<a id="organization"></a>
### Organization

**Description:** An organization associated with an ICPSR data collection or service.

**Repeatable**: No

**Accepted Values**: Multi-part element; see subfield definitions for more information.

**Examples:**

```
{
  "name": "Urban Institute",
  "name_code": "1234",
  "name_uri": "https://icpsr.example.com/organizations/1234",
  "ror": "https://ror.org/017pz3h73",
  "email": "info@urban.institute"
}
```

**Examples:**
```
    name: Urban Institute
    name_code: 1234
    name_uri: https://icpsr.example.com/organizations/1234
    ror: https://ror.org/017pz3h73
    email: info@urban.institute
```


---

<a id="person"></a>
### Person

**Description:** A person associated with an ICPSR data collection or service.

**Repeatable**: No

**Accepted Values**: Multi-part element; see subfield definitions for more information.

**Examples:**

```
{
  "name": {
    "given": "Jane Q.",
    "family": "Doe II"
  },
  "orcid": "https://orcid.org/0000-0001-6666-5717",
  "researcher_passport_profile_id": "1234",
  "affiliations": [
    {
      "name": "Urban Institute",
      "name_code": "2342",
      "name_uri": "https://icpsr.example.com/organizations/2342",
      "ror": "https://ror.org/017pz3h73",
      "icpsr_org_id": "xyz123"
    },
    {
      "name": "Example University"
    }
  ],
  "email": "jane.doe@example.com"
}
```

```
{
  "name": {
    "given": "Joe"
  }
}
```

**Examples:**
```
    name: {'given': 'Jane Q.', 'family': 'Doe II'}
    orcid: https://orcid.org/0000-0001-6666-5717
    researcher_passport_profile_id: 1234
    affiliations: [{'name': 'Urban Institute', 'name_code': '2342', 'name_uri': 'https://icpsr.example.com/organizations/2342', 'ror': 'https://ror.org/017pz3h73', 'icpsr_org_id': 'xyz123'}, {'name': 'Example University'}]
    email: jane.doe@example.com
```

```
    name: {'given': 'Joe'}
```


---

<a id="preregistration"></a>
### Preregistration

**Description:** A link to a research plan for the data collection (preferably a persistent identifier such as a DOI).

**Repeatable**: No

**Accepted Values**: Text

**Examples:**

```
    https://doi.org/10.1000/182
```

**Examples:**
```
    https://doi.org/10.1000/182
```


---

<a id="principal-investigators"></a>
### Principal Investigators

**Description:** The key people or organizations responsible for the data collection, listed by importance. Each data collection requires at least one PI, either a person or an organization.

**Repeatable**: Yes

**Accepted Values**: Multi-part element; see subfield definitions for more information.

#### Subfields:

| Property | Required? | Repeatable? | Accepted Values | Description |
| -------- | --------- | ----------- | --------------- | ----------- |
| Person | No | No | Multi-part element; see subfields | A person associated with an ICPSR data collection or service. |
| Organization | No | No | Multi-part element; see subfields | An organization associated with an ICPSR data collection or service. |
| Order | No | No | Number | The order or rank of importance for the PIs associated with the data collection, typically provided to ICPSR by the lead PI. |

##### Person

**Description:** A person associated with an ICPSR data collection or service.

**Required**: No

**Repeatable**: No

**Accepted Values**: Multi-part element; see subfield definitions for more information.

**Examples:**

```json
{
  "name": {
    "given": "Jane Q.",
    "family": "Doe II"
  },
  "orcid": "https://orcid.org/0000-0001-6666-5717",
  "researcher_passport_profile_id": "1234",
  "affiliations": [
    {
      "name": "Urban Institute",
      "name_code": "2342",
      "name_uri": "https://icpsr.example.com/organizations/2342",
      "ror": "https://ror.org/017pz3h73",
      "icpsr_org_id": "xyz123"
    },
    {
      "name": "Example University"
    }
  ],
  "email": "jane.doe@example.com"
}
```

```json
{
  "name": {
    "given": "Joe"
  }
}
```

##### Organization

**Description:** An organization associated with an ICPSR data collection or service.

**Required**: No

**Repeatable**: No

**Accepted Values**: Multi-part element; see subfield definitions for more information.

**Examples:**

```json
{
  "name": "Urban Institute",
  "name_code": "1234",
  "name_uri": "https://icpsr.example.com/organizations/1234",
  "ror": "https://ror.org/017pz3h73",
  "email": "info@urban.institute"
}
```

##### Order

**Description:** The order or rank of importance for the PIs associated with the data collection, typically provided to ICPSR by the lead PI.

**Required**: No

**Repeatable**: No

**Accepted Values**: Number

**Examples:**

```json
0
```

```json
1
```

```json
2
```

```json
3
```

###### Complete Examples (with Subfields):
```
    <p><b>Personal Principal Investigator</b></p><p><table><thead><tr><th>First Name</th><th>Last Name</th><th>Affiliation</th></tr></thead><tbody><tr><td>Veronica</td><td>Martinez-Ebers</td><td>National Institute for Law and Equity</td></tr><tr><td>Lawrence F.</td><td>Travis III</td><td>University of Cincinnati</td></tr></tbody></table></p>
```

```
    <p><b>Organizational Principal Investigator</b></p><p><table><thead><tr><th>Name</th></tr></thead><tbody><tr><td>United States Department of Labor. Bureau of Labor Statistics</td></tr><tr><td>The Washington Post</td></tr></tbody></table></p>
```


---

<a id="response-rates"></a>
### Response Rates

**Description:** The percentage of respondents in the sample who participated in the data collection.

**Repeatable**: No

**Accepted Values**: Text

**Usage Notes:** This field is only applicable if the data were collected with a survey instrument and the response rates are provided.

**Examples:**

```
    The overall response rate for this survey was 20.22%; 72.6% for existing panelists and 10.4% for new panelists, using AAPOR Response Rate 1.
```

```
    Not applicable.
```

**Examples:**
```
    The overall response rate for this survey was 20.22%; 72.6% for existing panelists and 10.4% for new panelists, using AAPOR Response Rate 1.
```

```
    Not applicable.
```


---

<a id="sampling-note"></a>
### Sampling Note

**Description:** Supplemental information about the sampling process that does not fit neatly into the Sampling Procedure field.

**Repeatable**: No

**Accepted Values**: Text

**Usage Notes:** A detailed discussion of such things as sampling error or other limitations of the sampling methodology is not required here.

**Examples:**

```
    National sample of telephone numbers from cell (RDD) sampling frame.
```

```
    The probability sample selected to represent the universe consists of approximately 71,000 households.
```

**Examples:**
```
    National sample of telephone numbers from cell (RDD) sampling frame.
```

```
    The probability sample selected to represent the universe consists of approximately 71,000 households.
```


---

<a id="sampling-procedures"></a>
### Sampling Procedures

**Description:** The type(s) of sample and sample design used to select survey respondents to represent the population.

**Repeatable**: Yes

**Accepted Values**: Text

**Usage Notes:** The sample is a selection out of the universe of all possible relevant cases (e.g., adults in the United States, housing units in three counties of Michigan, etc.) that could have been included in the data collection. Note that some studies, such as censuses, do not utilize samples but include all members of the universe. This controlled vocabulary was taken from the DDI Alliance. Source: DDI Alliance CV SamplingProcedure https://rdf-vocabulary.ddialliance.org/ddi-cv/SamplingProcedure/1.1.4/SamplingProcedure.html.

**Examples:**

```
[
  {
    "label": "Probability: Systematic random",
    "code": "Probability.SystematicRandom",
    "uri": "https://example.com/sampling_procedures/123"
  },
  {
    "label": "Other",
    "code": "Other",
    "uri": "https://example.com/sampling_procedures/737"
  }
]
```

```
[
  {
    "label": "Total universe/Complete enumeration",
    "code": "TotalUniverseCompleteEnumeration",
    "uri": "https://example.com/sampling_procedures/234"
  }
]
```

**Examples:**
```
    label: Probability: Systematic random
    code: Probability.SystematicRandom
    uri: https://example.com/sampling_procedures/123
```

```
    label: Other
    code: Other
    uri: https://example.com/sampling_procedures/737
```

```
    label: Total universe/Complete enumeration
    code: TotalUniverseCompleteEnumeration
    uri: https://example.com/sampling_procedures/234
```


---

<a id="scales"></a>
### Scales

**Description:** Any commonly known scales used to collect data for the data collection (e.g., MMPI, CPI, the Census Occupational Codes, etc.).

**Repeatable**: No

**Accepted Values**: Text

**Usage Notes:** Include common scales that can be readily identified from the data, documentation, or other related materials. ICPSR curators are not expected to infer or research scales that are not explicitly indicated. The scales can be cited either as a list or described in full sentences. If the questionnaire used has a finite list of responses (e.g., 'Always, Sometimes, Rarely, Never' or Strongly Agree, Agree, Disagree, Strongly Disagree'), it is acceptable for this element to note 'A Likert-type scale was used,' or 'Several Likert-type scales were used.' However, it is not required to note Likart-type scales in situations where only such scales were used, given their ubiquity.

**Examples:**

```
[
  "The baseline data collection included one scale - the CES-D index for maternal depression [Cole, J. C., Rabin, A. S., Smith, T. L., and Kaufman, A. S. (2004). Development and validation of a Rasch-derived CES-D short form. Psychological assessment, 16(4), 360]. All scales used for outcomes at ages 1 through 3 are listed in Appendix Tables 1 and 2 in the User Guide. Please refer to the User Guide and P.I. Codebook, available under the 'Data and Documentation' tab, for details."
]
```

```
[
  "Squires, J., Bricker, D. D., and Twombly, E. (2009). Ages and stages questionnaires. Baltimore, MD: Paul H. Brookes.",
  "Briggs-Gowan, M. J., Carter, A. S., Irwin, J. R., Wachtel, K., and Cicchetti, D. V. (2004). The Brief Infant-Toddler Social and Emotional Assessment: screening for social-emotional problems and delays in competence. Journal of pediatric psychology, 29(2), 143-155.",
  "Yu, L., Buysse, D. J., Germain, A., Moul, D. E., Stover, A., Dodds, N. E., ... and Pilkonis, P. A. (2012). Development of short forms from the PROMIS sleep disturbance and sleep-related impairment item banks. Behavioral sleep medicine, 10(1), 6-24."
]
```

**Examples:**
```
    The baseline data collection included one scale - the CES-D index for maternal depression [Cole, J. C., Rabin, A. S., Smith, T. L., and Kaufman, A. S. (2004). Development and validation of a Rasch-derived CES-D short form. Psychological assessment, 16(4), 360]. All scales used for outcomes at ages 1 through 3 are listed in Appendix Tables 1 and 2 in the User Guide. Please refer to the User Guide and P.I. Codebook, available under the 'Data and Documentation' tab, for details.
```

```
    Squires, J., Bricker, D. D., and Twombly, E. (2009). Ages and stages questionnaires. Baltimore, MD: Paul H. Brookes.
```

```
    Briggs-Gowan, M. J., Carter, A. S., Irwin, J. R., Wachtel, K., and Cicchetti, D. V. (2004). The Brief Infant-Toddler Social and Emotional Assessment: screening for social-emotional problems and delays in competence. Journal of pediatric psychology, 29(2), 143-155.
```

```
    Yu, L., Buysse, D. J., Germain, A., Moul, D. E., Stover, A., Dodds, N. E., ... and Pilkonis, P. A. (2012). Development of short forms from the PROMIS sleep disturbance and sleep-related impairment item banks. Behavioral sleep medicine, 10(1), 6-24.
```


---

<a id="smallest-geographic-unit"></a>
### Smallest Geographic Unit

**Description:** The smallest geographic unit (e.g., state or census tract) used in the dataset.

**Repeatable**: No

**Accepted Values**: Multi-part element; see subfield definitions for more information.

**Usage Notes:** Geographic Unit is intended to represent specific, known geography -- e.g., county, census district, FIPS code, electoral district, and any other conveyor of specific geography that is represented by a variable. If the data do not include a geographic variable by which the data can be analyzed, this element is not indicated. If all the cases are from a single state, but the cases are not subdivided geographically within that state, then 'state' is not indicated. This element is only meant to convey specific, known, geography. If there is a variable indicating which testing site a survey was taken at, but the locations of the testing sites were masked by the PI, this element is likely not indicated.

**Examples:**

```
{
  "label": "state",
  "code": "123",
  "uri": "https://example.com/smallest_geographic_unit/123"
}
```

```
{
  "label": "Census tract",
  "code": "234",
  "uri": "https://example.com/smallest_geographic_unit/234"
}
```

```
{
  "label": "precinct",
  "code": "345",
  "uri": "https://example.com/smallest_geographic_unit/345"
}
```

**Examples:**
```
    label: state
    code: 123
    uri: https://example.com/smallest_geographic_unit/123
```

```
    label: Census tract
    code: 234
    uri: https://example.com/smallest_geographic_unit/234
```

```
    label: precinct
    code: 345
    uri: https://example.com/smallest_geographic_unit/345
```


---

<a id="software-applications"></a>
### Software Applications

**Description:** Software used by the principal investigator(s) to collect or analyze data, required to understand how the data were obtained or to reproduce results.

**Repeatable**: Yes

**Accepted Values**: Multi-part element; see subfield definitions for more information.

#### Subfields:

| Property | Required? | Repeatable? | Accepted Values | Description |
| -------- | --------- | ----------- | --------------- | ----------- |
| Software Name | Yes | No | Text | The name of the software application. |
| Software Version | No | No | Text | The version of the application. |
| Software Description | No | No | Text | Short description or overview of the application and its intended purpose |
| Programming Languages | No | Yes | Text | The programming language(s) used in the development of the application |
| Operating Systems | No | Yes | Text | Computer operating systems supported by the application |
| Memory Requirements | No | No | Text | Minimum memory (e.g., RAM) requirements to operate the application |
| Processor Requirements | No | No | Text | Processor architecture required to run the application |
| Software Requirements | No | No | Text | Required components for the application, like runtime environments and shared libraries not included in the package but needed to run it. |
| Storage Requirements | No | No | Text | Amount of storage space required by the application |
| Device Requirements | No | No | Text | Device required to run the application. Used in cases where a specific make/model is required to run the application |
| License | No | No | Text | The license associated with the application, preferably expressed as a URL. |
| Download URL | No | No | Text | A direct link to a downloadable software artifact (e.g., executable, package, archive, or single script file) that retrieves the application itself, without additional navigation or instructions. |
| Installation URL | No | No | Text | A link to a repository or project landing page where users can obtain resources and instructions to install the application (as opposed to directly downloading a single file). |

##### Software Name

**Description:** The name of the software application.

**Required**: Yes

**Repeatable**: No

**Accepted Values**: Text

**Examples:**

```json
"JHOVE"
```

```json
"ffmpeg"
```

```json
"json-schema-for-humans"
```

##### Software Version

**Description:** The version of the application.

**Required**: No

**Repeatable**: No

**Accepted Values**: Text

**Examples:**

```json
"1"
```

```json
"2.0.4"
```

```json
"Auto-Build 2023-01-15 12:36"
```

##### Software Description

**Description:** Short description or overview of the application and its intended purpose

**Required**: No

**Repeatable**: No

**Accepted Values**: Text

**Examples:**

```json
"JHOVE, the JSTOR/Harvard Object Validation Environment, is an extensible software framework for performing format identification, validation, and characterization of digital objects."
```

```json
"ffmpeg is a very fast video and audio converter that can also grab from a live audio/video source. It can also convert between arbitrary sample rates and resize video on the fly with a high quality polyphase filter."
```

##### Programming Languages

**Description:** The programming language(s) used in the development of the application

**Required**: No

**Repeatable**: No

**Accepted Values**: Text

**Examples:**

```json
[
  "python"
]
```

```json
[
  "shell",
  "r"
]
```

```json
[
  "other"
]
```

##### Operating Systems

**Description:** Computer operating systems supported by the application

**Required**: No

**Repeatable**: No

**Accepted Values**: Text

**Examples:**

```json
[
  "windows"
]
```

```json
[
  "windows",
  "mac",
  "linux"
]
```

```json
[
  "other"
]
```

##### Memory Requirements

**Description:** Minimum memory (e.g., RAM) requirements to operate the application

**Required**: No

**Repeatable**: No

**Accepted Values**: Text

**Examples:**

```json
"4 GB"
```

```json
"1GB of RAM (2GB for a 64-bit version)"
```

```json
"4 GB of GPU memory for HD and some 4K media; 6 GB or more for 4K and higher"
```

##### Processor Requirements

**Description:** Processor architecture required to run the application

**Required**: No

**Repeatable**: No

**Accepted Values**: Text

**Examples:**

```json
"Intel i5/ i7/ Ryzen 7"
```

```json
"Minimum 1 GHz; Recommended 2GHz or more"
```

```json
"2.5–2.9 GHz or faster processor"
```

##### Software Requirements

**Description:** Required components for the application, like runtime environments and shared libraries not included in the package but needed to run it.

**Required**: No

**Repeatable**: No

**Accepted Values**: Text

**Examples:**

```json
"Java runtime environment"
```

```json
"Requires additional Python libraries: numpy, v1.11.2; scipy, v0.18.1, and pandas, v0.19.0"
```

```json
"Compile with GNU auto tools"
```

##### Storage Requirements

**Description:** Amount of storage space required by the application

**Required**: No

**Repeatable**: No

**Accepted Values**: Text

**Examples:**

```json
"3.5 GB for new installations, 5 GB for upgrades (including temporary files required during installation)"
```

```json
"15 GB of free disk space"
```

```json
"8 GB of available hard-disk space for installation; additional free space required during installation"
```

##### Device Requirements

**Description:** Device required to run the application. Used in cases where a specific make/model is required to run the application

**Required**: No

**Repeatable**: No

**Accepted Values**: Text

##### License

**Description:** The license associated with the application, preferably expressed as a URL.

**Required**: No

**Repeatable**: No

**Accepted Values**: Text

**Examples:**

```json
"https://www.apache.org/licenses/LICENSE-2.0"
```

```json
"https://opensource.org/licenses/LGPL-2.0"
```

##### Download URL

**Description:** A direct link to a downloadable software artifact (e.g., executable, package, archive, or single script file) that retrieves the application itself, without additional navigation or instructions.

**Required**: No

**Repeatable**: No

**Accepted Values**: Text

**Examples:**

```json
"https://github.com/richardlehane/siegfried/archive/refs/heads/main.zip"
```

```json
"https://cdn.nationalarchives.gov.uk/documents/droid-binary-6.5.2-bin-win32-with-jre.zip"
```

##### Installation URL

**Description:** A link to a repository or project landing page where users can obtain resources and instructions to install the application (as opposed to directly downloading a single file).

**Required**: No

**Repeatable**: No

**Accepted Values**: Text

**Examples:**

```json
"https://github.com/richardlehane/siegfried"
```

```json
"https://www.nationalarchives.gov.uk/information-management/manage-information/preserving-digital-records/droid/"
```

###### Complete Examples (with Subfields):
```
    name: siegfried
    software_version: 1.11.1
    description: Siegfried is a signature-based file format identification tool, implementing the National Archives UK's PRONOM file format signatures; freedesktop.org's MIME-info file format signatures; the Library of Congress's FDD file format signatures (beta); and Wikidata (beta).
    programming_languages: ['go', 'javascript', 'other']
    operating_systems: ['mac', 'linux', 'windows']
    license: https://www.apache.org/licenses/LICENSE-2.0
    download_url: https://github.com/richardlehane/siegfried/archive/refs/heads/main.zip
```


---

<a id="study-design"></a>
### Study Design

**Description:** The procedures used to contact participants and gather data.

**Repeatable**: No

**Accepted Values**: Text

**Usage Notes:** The Study Design provides more detailed information than the Summary, including how surveys were prepared and administered, how interviews were conducted, or how the data were obtained and compiled, as well as information about deadlines and follow-ups to respondents.

**Examples:**

```
    Data on organizational culture in each of the 12 courts (Part 1) were obtained by administering the Court Culture Assessment Instrument (CCAI) to all judges with a felony criminal court docket and to all senior court administrators. A total of 224 respondents completed the questionnaire. The CCAI was used to assess five key dimensions of current court culture orientation: (1) dominant case management style, (2) judicial and court staff relations, (3) change management, (4) courthouse leadership, and (5) internal organization. The determination of what culture judges and court administrators desired to establish in the near future was also obtained through the application of the same instrument (CACI) as practitioners were asked to indicate the type of culture in each work area (or content dimension) they would like to see in their court in the next five years.
```

**Examples:**
```
    Data on organizational culture in each of the 12 courts (Part 1) were obtained by administering the Court Culture Assessment Instrument (CCAI) to all judges with a felony criminal court docket and to all senior court administrators. A total of 224 respondents completed the questionnaire. The CCAI was used to assess five key dimensions of current court culture orientation: (1) dominant case management style, (2) judicial and court staff relations, (3) change management, (4) courthouse leadership, and (5) internal organization. The determination of what culture judges and court administrators desired to establish in the near future was also obtained through the application of the same instrument (CACI) as practitioners were asked to indicate the type of culture in each work area (or content dimension) they would like to see in their court in the next five years.
```


---

<a id="summary"></a>
### Summary

**Description:** A description of the data collection that helps users understand its purpose, substance, and key topics.

**Repeatable**: No

**Accepted Values**: Text

**Usage Notes:** The Summary may include information about the different parts of the data collection not adequately conveyed by the Fileset names or found elsewhere in the metadata. Other important components include a listing of major variables or categories of variables (with examples) as well as an indication of the data collection's unit of analysis (i.e., who or what is being studied: individuals, housing units, courts, criminal acts, etc.). Most often the unit of analysis is the individual; where it is not, it is particularly important to make this clear.

The Summary is written in the third person and avoids attempting to address issues of how the data might be used, who might be interested in the data, or any evaluative comments about the worth or usefulness of the data collection. The Summary uses past tense when describing the process of collecting the data and present tense when necessary, such as when describing the data (e.g., 'The MIDUS Refresher collection is split into two datasets.'). Numerals are used instead of spelling them out; if a number is spelled out for emphasis, the number is attached in parentheses (e.g. 'Two thousand (2,000)').


**Examples:**

```
    In 2014, Chicago Public Schools, looking to reduce the possibility of gun violence among school-aged youth, applied for a grant through the National Institute of Justice. CPS was awarded the Comprehensive School Safety Initiative grant and use said grant to establish the 'Connect and Redirect to Respect' program. This program used student social media data to identify and intervene with students thought to be at higher risk for committing violence. At-risk behaviors included brandishing a weapon, instigating conflict online, signaling gang involvement, and threats towards others. Identified at-risk students would be contacted by a member of the CPS Network Safety Team or the Chicago Police Department's Gang School Safety Team, depending on the risk level of the behavior. To evaluate the efficacy of CRR, the University of Chicago Crime Lab compared outcomes for students enrolled in schools that received the program to outcomes for students enrolled in comparison schools, which did not receive the program. 32 schools were selected for the study, with a total of 44,503 students. Demographic variables included age, race, sex, and ethnicity. Misconduct and academic variables included arrest history, in-school suspensions, out-of-school suspensions, GPA, and attendance days.
```

```
    The Health and Relationship Project is a study of both spouses in same-sex and different-sex marriages who were legally married and aged 35 to 65 at the time of data collection (2015). There are two parts of this study: a baseline questionnaire and a daily diary questionnaire completed for 10 consecutive days; both components were completed online and spouses were asked to complete the surveys separately. The baseline questionnaire asks participants about a number of topics related to marriage and health, including stress, health status and health behaviors, relationship quality, and how they have approached health problems in the past. The diary questionnaire asks participants a number of questions about the past 24 hours, including daily stress experiences, social interactions, and health behaviors.
```

**Examples:**
```
    In 2014, Chicago Public Schools, looking to reduce the possibility of gun violence among school-aged youth, applied for a grant through the National Institute of Justice. CPS was awarded the Comprehensive School Safety Initiative grant and use said grant to establish the 'Connect and Redirect to Respect' program. This program used student social media data to identify and intervene with students thought to be at higher risk for committing violence. At-risk behaviors included brandishing a weapon, instigating conflict online, signaling gang involvement, and threats towards others. Identified at-risk students would be contacted by a member of the CPS Network Safety Team or the Chicago Police Department's Gang School Safety Team, depending on the risk level of the behavior. To evaluate the efficacy of CRR, the University of Chicago Crime Lab compared outcomes for students enrolled in schools that received the program to outcomes for students enrolled in comparison schools, which did not receive the program. 32 schools were selected for the study, with a total of 44,503 students. Demographic variables included age, race, sex, and ethnicity. Misconduct and academic variables included arrest history, in-school suspensions, out-of-school suspensions, GPA, and attendance days.
```

```
    The Health and Relationship Project is a study of both spouses in same-sex and different-sex marriages who were legally married and aged 35 to 65 at the time of data collection (2015). There are two parts of this study: a baseline questionnaire and a daily diary questionnaire completed for 10 consecutive days; both components were completed online and spouses were asked to complete the surveys separately. The baseline questionnaire asks participants about a number of topics related to marriage and health, including stress, health status and health behaviors, relationship quality, and how they have approached health problems in the past. The diary questionnaire asks participants a number of questions about the past 24 hours, including daily stress experiences, social interactions, and health behaviors.
```


---

<a id="time-methods"></a>
### Time Methods

**Description:** The methods used to collect data over time, like snapshots at one point (cross-sectional) or repeatedly (longitudinal) to study changes or trends

**Repeatable**: Yes

**Accepted Values**: Multi-part element; see subfield definitions for more information.

#### Subfields:

| Property | Required? | Repeatable? | Accepted Values | Description |
| -------- | --------- | ----------- | --------------- | ----------- |
| Time Method | Yes | No | Text | A human-readable form of the term. |
| Time Method Code | Yes | No | Text | A machine-readable/-actionable form of the term. |
| Time Method URI | Yes | No | Text | The URI for the term. |

##### Time Method

**Description:** A human-readable form of the term.

**Required**: Yes

**Repeatable**: No

**Accepted Values**: Text

**Examples:**

```json
"Cross-section"
```

```json
"Longitudinal: Cohort/Event-based"
```

```json
"Time series"
```

##### Time Method Code

**Description:** A machine-readable/-actionable form of the term.

**Required**: Yes

**Repeatable**: No

**Accepted Values**: Text

**Examples:**

```json
"CrossSection"
```

```json
"Longitudinal.CohortEventBased"
```

```json
"Other"
```

##### Time Method URI

**Description:** The URI for the term.

**Required**: Yes

**Repeatable**: No

**Accepted Values**: Text

###### Complete Examples (with Subfields):
```
    label: Registers/Records/Accounts: Medical/Clinical
    code: RegistersRecordsAccounts.MedicalClinical
    uri: https://example.com/time_methods/123
```

```
    label: Events/Interactions
    code: EventsInteractions
    uri: https://example.com/time_methods/234
```

```
    label: Other
    code: Other
    uri: https://example.com/time_methods/737
```


---

<a id="time-periods"></a>
### Time Periods

**Description:** The time period(s) to which the data refer, regardless of when the data were collected.

**Repeatable**: Yes

**Accepted Values**: Multi-part element; see subfield definitions for more information.

#### Subfields:

| Property | Required? | Repeatable? | Accepted Values | Description |
| -------- | --------- | ----------- | --------------- | ----------- |
| Start Date | Yes | No | Text | The start date for the time period the data refer to, formatted as YYYY, YYYY-MM, or YYYY-MM-DD, with no spaces in date expressions. |
| End Date | Yes | No | Text | The end date for the time period the data refer to, formatted as YYYY, YYYY-MM, or YYYY-MM-DD, with no spaces in date expressions. |
| Time Frame | No | No | Text | An optional free-text description of the time period, used for non-numeric dates (e.g., 'Fall 2012') or to add context when multiple dates are present. |

##### Start Date

**Description:** The start date for the time period the data refer to, formatted as YYYY, YYYY-MM, or YYYY-MM-DD, with no spaces in date expressions.

**Required**: Yes

**Repeatable**: No

**Accepted Values**: Text

**Examples:**

```json
"2000"
```

```json
"2019-10"
```

```json
"2021-03-01"
```

##### End Date

**Description:** The end date for the time period the data refer to, formatted as YYYY, YYYY-MM, or YYYY-MM-DD, with no spaces in date expressions.

**Required**: Yes

**Repeatable**: No

**Accepted Values**: Text

**Examples:**

```json
"2000"
```

```json
"2019-10"
```

```json
"2021-03-01"
```

##### Time Frame

**Description:** An optional free-text description of the time period, used for non-numeric dates (e.g., 'Fall 2012') or to add context when multiple dates are present.

**Required**: No

**Repeatable**: No

**Accepted Values**: Text

**Usage Notes:** The Time Frame should not simply restate the date(s) in words. For example, if the Time Period starts in 2020-01, the Time Frame should repeat 'January 2020'.

**Examples:**

```json
"Fall 2001"
```

```json
"Winter Semester 2019"
```

###### Complete Examples (with Subfields):
```
    start_date: 2018
    end_date: 2018
    time_frame: Summer and Fall 2018
```

```
    start_date: 2020-10
    end_date: 2020-10
```


---

<a id="title"></a>
### Title

**Description:** The official title that describes what the data collection is about, its geographic scope, and the time period it covered.

**Repeatable**: No

**Accepted Values**: Text

**Examples:**

```
    Bridge of Faith: Aim4Peace Community-Based Violence Prevention Project, Kansas City, Missouri, 2014-2017
```

```
    Health and Relationships Project, United States, 2014-2015
```

```
    Targeted Interventions to Prevent Chronic Low Back Pain in High Risk Patients: A Multi-Site Pragmatic Randomized Controlled Trial (TARGET Trial), 4 U.S. cities, 2016-2019
```

```
    Aid Like A Paycheck (ALAP), Texas and California, 2014-2017
```

```
    COVID-19 Disruptions Disproportionately Affect Female Academics, Global, 2020
```

**Examples:**
```
    Bridge of Faith: Aim4Peace Community-Based Violence Prevention Project, Kansas City, Missouri, 2014-2017
```

```
    Health and Relationships Project, United States, 2014-2015
```

```
    Targeted Interventions to Prevent Chronic Low Back Pain in High Risk Patients: A Multi-Site Pragmatic Randomized Controlled Trial (TARGET Trial), 4 U.S. cities, 2016-2019
```

```
    Aid Like A Paycheck (ALAP), Texas and California, 2014-2017
```

```
    COVID-19 Disruptions Disproportionately Affect Female Academics, Global, 2020
```


---

<a id="units-of-analysis"></a>
### Units of Analysis

**Description:** The object(s) of analysis for the data collection, such as an organization, individual, or household.

**Repeatable**: Yes

**Accepted Values**: Multi-part element; see subfield definitions for more information.

#### Subfields:

| Property | Required? | Repeatable? | Accepted Values | Description |
| -------- | --------- | ----------- | --------------- | ----------- |
| label | Yes | No | Text | A human-readable form of the term. |
| code | Yes | No | Text | A machine-readable/-actionable form of the term. |
| uri | Yes | No | Text | The URI for the term. |

##### label

**Description:** A human-readable form of the term.

**Required**: Yes

**Repeatable**: No

**Accepted Values**: Text

**Examples:**

```json
"Organization/Institution"
```

```json
"Individual"
```

```json
"Household"
```

##### code

**Description:** A machine-readable/-actionable form of the term.

**Required**: Yes

**Repeatable**: No

**Accepted Values**: Text

**Examples:**

```json
"OrganizationOrInstitution"
```

```json
"Individual"
```

```json
"Household"
```

##### uri

**Description:** The URI for the term.

**Required**: Yes

**Repeatable**: No

**Accepted Values**: Text

###### Complete Examples (with Subfields):
```
    label: Organization/Institution
    code: OrganizationOrInstitution
    uri: https://example.com/units_of_analysis/123
```

```
    label: Individual
    code: Individual
    uri: https://example.com/units_of_analysis/234
```

```
    label: Household
    code: Household
    uri: https://example.com/units_of_analysis/737
```


---

<a id="universe"></a>
### Universe

**Description:** The total group of persons or other entities (e.g., households or organizations) that were the object of research and to which analytic results refer.

**Repeatable**: No

**Accepted Values**: Text

**Usage Notes:** Age, nationality, and residence commonly help to delineate a given universe, but any of a number of factors may be involved, such as sex, race, income, veteran status, criminal convictions, etc. The Universe may consist of elements other than persons, such as housing units, court cases, deaths, countries, etc. It should be possible to tell from the description of the universe whether a given individual or element (hypothetical or real) is a member of the population under study. Typically, the Universe statement is about one sentence or shorter, and reflects the entire possible population a data collection sought to study.

**Examples:**

```
    All households in the United States with phones.
```

```
    Part 1: Thirty cities in Massachusetts during 1980-1986. Parts 2-4: All residents in Massachusetts during 1986.
```

```
    Individuals self-identified as transgender, trans, genderqueer, non-binary, or other identities on the transgender identity spectrum aged 18 and older residing in the fifty U.S. states, the District of Columbia, American Samoa, Guam, Puerto Rico, and U.S. military bases overseas.
```

```
    Jihadists from the United States and Canada, along with Incels from Germany, Canada, the United States, and United Kingdom.
```

```
    All publicly funded medical examiner and coroner offices.
```

```
    Uncertified ballots for the 2000 United States presidential election in Florida.
```

**Examples:**
```
    All households in the United States with phones.
```

```
    Part 1: Thirty cities in Massachusetts during 1980-1986. Parts 2-4: All residents in Massachusetts during 1986.
```

```
    Individuals self-identified as transgender, trans, genderqueer, non-binary, or other identities on the transgender identity spectrum aged 18 and older residing in the fifty U.S. states, the District of Columbia, American Samoa, Guam, Puerto Rico, and U.S. military bases overseas.
```

```
    Jihadists from the United States and Canada, along with Incels from Germany, Canada, the United States, and United Kingdom.
```

```
    All publicly funded medical examiner and coroner offices.
```

```
    Uncertified ballots for the 2000 United States presidential election in Florida.
```


---

<a id="variable-description"></a>
### Variable Description

**Description:** Significant variables (particularly demographic variables) in the data files.

**Repeatable**: No

**Accepted Values**: Text

**Usage Notes:** The Variable Description provides more detailed information than the Summary, including a review of variables that are important for users to know about. The codebook, setup files, and variable groups are appropriate sources of information for Variable Description.

**Examples:**

```
    The data includes variables about participants' and their parents' moods, interviewer observations, families' activities, families' health history, participants' school records, and parents' substance use. Demographic variables include race, religion, annual household income, and the participants' parents' employment statuses.
```

```
    The LGBTQ Hate Crimes Interviews dataset contains more in-depth information, including victim demographic information, substance abuse history, information on whether the victim is open about their LGBTQ identification, the victim's job status, and information about how the victim reacted to the crime, such as whether or not they reported the crime to the police and their level of cooperation with the police and prosecution.
```

**Examples:**
```
    The data includes variables about participants' and their parents' moods, interviewer observations, families' activities, families' health history, participants' school records, and parents' substance use. Demographic variables include race, religion, annual household income, and the participants' parents' employment statuses.
```

```
    The LGBTQ Hate Crimes Interviews dataset contains more in-depth information, including victim demographic information, substance abuse history, information on whether the victim is open about their LGBTQ identification, the victim's job status, and information about how the victim reacted to the crime, such as whether or not they reported the crime to the police and their level of cooperation with the police and prosecution.
```


---

<a id="version-history"></a>
### Version History

**Description:** A record of how the data collection has changed over time.

**Repeatable**: Yes

**Accepted Values**: Multi-part element; see subfield definitions for more information.

#### Subfields:

| Property | Required? | Repeatable? | Accepted Values | Description |
| -------- | --------- | ----------- | --------------- | ----------- |
| version_number | No | No | Text | A version number for a study. |
| version_date | No | No | Text | The date on which a given version of a data collection was released. |
| version_note | No | No | Text | Provenance information about a given version of the data collection. |

##### version_number

**Description:** A version number for a study.

**Required**: No

**Repeatable**: No

**Accepted Values**: Text

**Usage Notes:** Versioning should follow ICPSR conventions

**Examples:**

```json
"V1"
```

```json
"V2"
```

```json
"V3"
```

##### version_date

**Description:** The date on which a given version of a data collection was released.

**Required**: No

**Repeatable**: No

**Accepted Values**: Text

**Examples:**

```json
"2020-07-20"
```

```json
"2022-01-31"
```

##### version_note

**Description:** Provenance information about a given version of the data collection.

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
"The codebook descriptions of variables TANSUP, EMOSUP, and SOCSUP were corrected."
```

###### Complete Examples (with Subfields):
```
    version_number: V2
    version_date: 2023-08-12
    version_note: The data producer provided additional data files.
```

```
    version_number: V1
    version_date: 2021-03-01
    version_note: Initial release
```

```
    version_number: V1
    version_date: 2024-06-28
    version_note: Initial release
```


---

<a id="weights"></a>
### Weights

**Description:** The weight variables and the criteria for using them in data analysis or other information about how the data are weighted if no weight variables are present.

**Repeatable**: No

**Accepted Values**: Text

**Usage Notes:** Weight includes any information about weighting variables in the data, as well as any other weight information provided by the Principal Investigator. If a weighting formula or coefficient was developed, provide this formula, define its elements, and indicate how the formula is applied to the data. It is acceptable to summarize additional documentation and refer users to those resources for more information.

**Examples:**

```
    Both the TransPop and Cisgender datasets have the same variable named WEIGHT as the weighting variable. The combination datasets have a set of three weight variables (WEIGHT_TRANSPOP, WEIGHT_CISGENDER, WEIGHT_CISGENDER_TRANSPOP)
```

```
    A weight variable with two implied decimal places has been included and must be used in any analysis.
```

**Examples:**
```
    Both the TransPop and Cisgender datasets have the same variable named WEIGHT as the weighting variable. The combination datasets have a set of three weight variables (WEIGHT_TRANSPOP, WEIGHT_CISGENDER, WEIGHT_CISGENDER_TRANSPOP)
```

```
    A weight variable with two implied decimal places has been included and must be used in any analysis.
```


---
