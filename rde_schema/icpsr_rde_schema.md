# ICPSR RDE Metadata Schema

Last updated: March 10, 2026

## Overview

| Property | Required? | Repeatable? | Accepted Values | Description |
|---|---|---|---|---|
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
| [Geographic Coverage Areas](#geographic-coverage-areas) | Yes | Yes | Multi-part element; see subfields | The geographic locations where the data refer or are related. |
| [ICPSR Subject Terms](#icpsr-subject-terms) | Yes | Yes | Multi-part element; see subfields | A controlled list of social science terms maintained by ICPSR and used to indicate topics related to the data collection. |
| [Journal of Economic Literature (JEL) Classification Codes](#journal-of-economic-literature-(jel)-classification-codes) | No | Yes | Multi-part element; see subfields | Classification codes used to categorize economic research. |
| [License](#license) | No | No | Multi-part element; see subfields | A license governing the data's use. |
| [Medical Subject Headings (MeSH) Terms](#medical-subject-headings-(mesh)-terms) | No | Yes | Multi-part element; see subfields | Biomedical and health-related terms from the National Library of Medicine that describe the data collection's topics. |
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
| [Summary](#summary) | Yes | No | Text | A description of the data collection that helps users understand its purpose, substance, and key topics. |
| [Time Methods](#time-methods) | No | Yes | Multi-part element; see subfields | The methods used to collect data over time, like snapshots at one point (cross-sectional) or repeatedly (longitudinal) to study changes or trends |
| [Time Periods](#time-periods) | Yes | Yes | Multi-part element; see subfields | The time period(s) to which the data refer, regardless of when the data were collected. |
| [Title](#title) | Yes | No | Text | The official title that describes what the data collection is about, its geographic scope, and the time period it covered. |
| [Units of Analysis](#units-of-analysis) | No | Yes | Multi-part element; see subfields | The object(s) of analysis for the data collection, such as an organization, individual, or household. |
| [Universe](#universe) | No | No | Text | The total group of persons or other entities (e.g., households or organizations) that were the object of research and to which analytic results refer. |
| [Variable Description](#variable-description) | No | No | Text | Significant variables (particularly demographic variables) in the data files. |
| [Version History](#version-history) | No | Yes | Multi-part element; see subfields | A record of how the data collection has changed over time. |
| [Weights](#weights) | No | No | Text | The weight variables and the criteria for using them in data analysis or other information about how the data are weighted if no weight variables are present. |

---
## Properties

<a id="alternate-titles"></a>
### Alternate Titles

**Description:** The alternate name(s) or acronym(s) commonly used to refer to the data collection.  
**Required:** No  
**Repeatable:** Yes  
**Accepted Values:** Text  

**Examples:**

```text
"Add Health Parent Study"
```

```text
"FACES 2009"
```

```text
"Survey of Consumers"
```

```text
"Eurobarometer 85.2"
```


---

<a id="citation"></a>
### Citation

**Description:** The official way to reference the data collection in writing.  
**Required:** No  
**Repeatable:** No  
**Accepted Values:** Text  
**Usage Notes:** The Citation is dynamically assembled from other entry fields in this format: PI (list). Title. Distributor (list), Issued Date. DOI. Note: ICPSR 'union catalog' records (i.e., external resource to which ICPSR links as a courtesy) do not have citations.  

**Examples:**

```text
"University of Michigan. Survey Research Center. Economic Behavior Program. Survey of Consumer Attitudes and Behavior, September 2018. Inter-university Consortium for Political and Social Research [distributor], 2021-11-18. https://doi.org/10.3886/ICPSR38121.v1"
```

```text
"United States Department of Justice. Office of Justice Programs. Office of Juvenile Justice and Delinquency Prevention. Juvenile Residential Facility Census, 2020 [United States]. Inter-university Consortium for Political and Social Research [distributor], 2024-07-15. https://doi.org/10.3886/ICPSR38914.v1"
```


---

<a id="collection-dates"></a>
### Collection Dates

**Description:** The date(s) when the data were physically collected.  
**Required:** No  
**Repeatable:** Yes  
**Accepted Values:** Multi-part element; see subfields  
#### Subfields:

| Property | Required? | Repeatable? | Accepted Values | Description |
|---|---|---|---|---|
| [Start Date](#collection-dates_start_date) | Yes | No | Text | The start date of the data collection period. Must be in YYYY-MM-DD, YYYY-MM, or YYYY format with no spaces. |
| [End Date](#collection-dates_end_date) | Yes | No | Text | The end date of the data collection period. Must be in YYYY-MM-DD, YYYY-MM, or YYYY format with no spaces. |
| [Time Frame](#collection-dates_time_frame) | No | No | Text | An optional free-text description of the data collection period, used for non-numeric dates (e.g., 'Fall 2012') or to add context when multiple dates are present. |

<a name="collection-dates_start_date"></a>
##### Start Date

**Description:** The start date of the data collection period. Must be in YYYY-MM-DD, YYYY-MM, or YYYY format with no spaces.  
**Required:** Yes  
**Repeatable:** No  
**Accepted Values:** Text  

**Examples:**

```text
"2000"
```

```text
"2019-10"
```

```text
"2021-03-01"
```

<a name="collection-dates_end_date"></a>
##### End Date

**Description:** The end date of the data collection period. Must be in YYYY-MM-DD, YYYY-MM, or YYYY format with no spaces.  
**Required:** Yes  
**Repeatable:** No  
**Accepted Values:** Text  

**Examples:**

```text
"2000"
```

```text
"2019-10"
```

```text
"2021-03-01"
```

<a name="collection-dates_time_frame"></a>
##### Time Frame

**Description:** An optional free-text description of the data collection period, used for non-numeric dates (e.g., 'Fall 2012') or to add context when multiple dates are present.  
**Required:** No  
**Repeatable:** No  
**Accepted Values:** Text  
**Usage Notes:** The Time Frame should not simply restate the date(s) in words. For example, if the Collection Date starts in 2020-01, the Time Frame should repeat 'January 2020'.  

**Examples:**

```text
"Fall 2001"
```

```text
"Student data"
```

###### Complete Collection Dates Examples (with Subfields):

```yaml
- "Start Date": "2018"
  "End Date": "2018"
  "Time Frame": "Summer and Fall 2018"

- "Start Date": "2020-10"
  "End Date": "2020-10"
```


---

<a id="collection-modes"></a>
### Collection Modes

**Description:** The method(s) or procedure(s) used to collect the data.  
**Required:** No  
**Repeatable:** Yes  
**Accepted Values:** Multi-part element; see subfields  
**Usage Notes:** This controlled vocabulary was taken from the DDI Alliance. Source: DDI Alliance CV ModeOfCollection https://rdf-vocabulary.ddialliance.org/ddi-cv/ModeOfCollection/4.0.3/ModeOfCollection.html.  
#### Subfields:

| Property | Required? | Repeatable? | Accepted Values | Description |
|---|---|---|---|---|
| [Collection Mode](#collection-modes_label) | Yes | No | Text | A human-readable form of the term. |
| [Collection Mode Code](#collection-modes_code) | Yes | No | Text | A machine-readable/-actionable form of the term. |
| [Collection Mode URI](#collection-modes_uri) | Yes | No | Text | The URI for the term. |

<a name="collection-modes_label"></a>
##### Collection Mode

**Description:** A human-readable form of the term.  
**Required:** Yes  
**Repeatable:** No  
**Accepted Values:** Text  

**Examples:**

```text
"Face-to-face interview: Computer-assisted (CAPI/CAMI)"
```

```text
"Measurements and tests"
```

```text
"Computer-based observation"
```

<a name="collection-modes_code"></a>
##### Collection Mode Code

**Description:** A machine-readable/-actionable form of the term.  
**Required:** Yes  
**Repeatable:** No  
**Accepted Values:** Text  

**Examples:**

```text
"Interview.FaceToFace.CAPIorCAMI"
```

```text
"MeasurementsAndTests"
```

```text
"Observation.ComputerBased"
```

<a name="collection-modes_uri"></a>
##### Collection Mode URI

**Description:** The URI for the term.  
**Required:** Yes  
**Repeatable:** No  
**Accepted Values:** Text  
###### Complete Collection Modes Examples (with Subfields):

```yaml
- "Collection Mode": "Face-to-face interview: Computer-assisted (CAPI/CAMI)"
  "Collection Mode Code": "Interview.FaceToFace.CAPIorCAMI"
  "Collection Mode URI": "https://example.com/collection_modes/234"
```

```yaml
- "Collection Mode": "Measurements and tests"
  "Collection Mode Code": "MeasurementsAndTests"
  "Collection Mode URI": "https://example.com/collection_modes/972"

- "Collection Mode": "Computer-based observation"
  "Collection Mode Code": "Observation.ComputerBased"
  "Collection Mode URI": "https://example.com/collection_modes/113"
```


---

<a id="data-management-plan"></a>
### Data Management Plan

**Description:** A link to the data management plan (preferably a persistent identifier such as a DOI).  
**Required:** No  
**Repeatable:** No  
**Accepted Values:** Text  

**Examples:**

```text
"https://doi.org/10.1000/182"
```


---

<a id="data-source-types"></a>
### Data Source Types

**Description:** The source(s) of the data as collected by the Principal Investigators.  
**Required:** No  
**Repeatable:** Yes  
**Accepted Values:** Multi-part element; see subfields  
**Usage Notes:** This controlled vocabulary was taken from the DDI Alliance. Source: DDI Alliance CV DataSourceType https://rdf-vocabulary.ddialliance.org/ddi-cv/DataSourceType/1.0.2/DataSourceType.html.  
#### Subfields:

| Property | Required? | Repeatable? | Accepted Values | Description |
|---|---|---|---|---|
| [Data Source Type](#data-source-types_label) | Yes | No | Text | A human-readable form of the term. |
| [Data Source Type Code](#data-source-types_code) | Yes | No | Text | A machine-readable/-actionable form of the term. |
| [Data Source Type URI](#data-source-types_uri) | Yes | No | Text | The URI for the term. |

<a name="data-source-types_label"></a>
##### Data Source Type

**Description:** A human-readable form of the term.  
**Required:** Yes  
**Repeatable:** No  
**Accepted Values:** Text  

**Examples:**

```text
"Registers/Records/Accounts: Medical/Clinical"
```

```text
"Events/Interactions"
```

```text
"Other"
```

<a name="data-source-types_code"></a>
##### Data Source Type Code

**Description:** A machine-readable/-actionable form of the term.  
**Required:** Yes  
**Repeatable:** No  
**Accepted Values:** Text  

**Examples:**

```text
"RegistersRecordsAccounts.MedicalClinical"
```

```text
"EventsInteractions"
```

```text
"Other"
```

<a name="data-source-types_uri"></a>
##### Data Source Type URI

**Description:** The URI for the term.  
**Required:** Yes  
**Repeatable:** No  
**Accepted Values:** Text  
###### Complete Data Source Types Examples (with Subfields):

```yaml
- "Data Source Type": "Registers/Records/Accounts: Medical/Clinical"
  "Data Source Type Code": "RegistersRecordsAccounts.MedicalClinical"
  "Data Source Type URI": "https://example.com/data_source_type/123"

- "Data Source Type": "Events/Interactions"
  "Data Source Type Code": "EventsInteractions"
  "Data Source Type URI": "https://example.com/data_source_type/234"
```

```yaml
- "Data Source Type": "Other"
  "Data Source Type Code": "Other"
  "Data Source Type URI": "https://example.com/data_source_type/737"
```


---

<a id="distributors"></a>
### Distributors

**Description:** The organization(s) responsible for distributing the data collection.  
**Required:** No  
**Repeatable:** Yes  
**Accepted Values:** Multi-part element; see subfields  
#### Subfields:

| Property | Required? | Repeatable? | Accepted Values | Description |
|---|---|---|---|---|
| [Organization](#distributors_organization) | Yes | No | Object | See the [Organization](#organization) property. |
| [Order](#distributors_order) | Yes | No | Number | The order of importance for the distributors of the data collection. |

<a name="distributors_organization"></a>
##### Organization

**Description:** See the [Organization](#organization) property.  
**Required:** Yes  
**Repeatable:** No  
**Accepted Values:** See the [Organization](#organization) property  
<a name="distributors_order"></a>
##### Order

**Description:** The order of importance for the distributors of the data collection.  
**Required:** Yes  
**Repeatable:** No  
**Accepted Values:** Number  
**Usage Notes:** A value of '0' indicates the primary distributor, '1' the second, and so forth.  

**Examples:**

```text
"0"
```

```text
"1"
```

```text
"2"
```

```text
"3"
```

###### Complete Distributors Examples (with Subfields):

```yaml
- "Organization":
    "Name": "Inter-university Consortium for Political and Social Research"
    "Name Code": "1234"
    "Name Uri": "https://icpsr.example.com/organizations/1234"
    "Ror": "https://ror.org/017pz3h73"
  "Order": 0

- "Organization":
    "Name": "GESIS"
    "Name Code": "2345"
    "Name Uri": "https://icpsr.example.com/organizations/2345"
    "Ror": "https://ror.org/018afyw53"
  "Order": 1
```

```yaml
- "Organization":
    "Name": "Roper Center for Public Opinion Research"
    "Name Code": "1234"
    "Name Uri": "https://icpsr.example.com/organizations/1234"
  "Order": 0
```


---

<a id="external-data-sources"></a>
### External Data Sources

**Description:** The source of the data, when that source is external to the data collection and can be independently cited.  
**Required:** No  
**Repeatable:** Yes  
**Accepted Values:** Text  
**Usage Notes:** External data sources include books, journal articles, administrative records, agency-sponsored surveys, and machine-readable files. Each source includes at minimum the title, author, publication year, and journal (if applicable). Any citation format is accepted.  

**Examples:**

```text
"'Voting Scores.' Congressional Quarterly Almanac 33 (1977), 487-498"
```

```text
"United States Bureau of the Census Economic Surveys, 1998-2000"
"United States Congressional Record, 1989"
```

```text
"Annual Company Organization Survey, 2003"
```


---

<a id="funding-sources"></a>
### Funding Sources

**Description:** The sources of funding that supported the data collection.  
**Required:** No  
**Repeatable:** Yes  
**Accepted Values:** Multi-part element; see subfields  
#### Subfields:

| Property | Required? | Repeatable? | Accepted Values | Description |
|---|---|---|---|---|
| [Organization](#funding-sources_organization) | Yes | No | Object | See the [Organization](#organization) property. |
| [Funding Awards](#funding-sources_grants) | No | Yes | Multi-part element; see subfields | Financial support for the data collection. |
| [Order](#funding-sources_order) | Yes | No | Number | Internal ICPSR field used to determine the order of importance for the funders associated with the data collection. |

<a name="funding-sources_organization"></a>
##### Organization

**Description:** See the [Organization](#organization) property.  
**Required:** Yes  
**Repeatable:** No  
**Accepted Values:** See the [Organization](#organization) property  
<a name="funding-sources_grants"></a>
##### Funding Awards

**Description:** Financial support for the data collection.  
**Required:** No  
**Repeatable:** Yes  
**Accepted Values:** Multi-part element; see subfields  
##### Subfields:

| Property | Required? | Repeatable? | Accepted Values | Description |
|---|---|---|---|---|
| [Funding Identifier](#funding-sources_grants_grant_number) | Yes | No | Text | The unique identifier for the funding (e.g., ABC-0123456. |
| [Funding URL](#funding-sources_grants_grant_uri) | No | No | Text | A unique identifier (URL), preferably a persistent one like a DOI,  linking to a landing page with funding information. |

<a name="funding-sources_grants_grant_number"></a>
###### Funding Identifier

**Description:** The unique identifier for the funding (e.g., ABC-0123456.  
**Required:** Yes  
**Repeatable:** No  
**Accepted Values:** Text  

**Examples:**

```text
"SES-1835721"
```

```text
"MDR-8550085"
```

```text
"40791"
```

<a name="funding-sources_grants_grant_uri"></a>
###### Funding URL

**Description:** A unique identifier (URL), preferably a persistent one like a DOI,  linking to a landing page with funding information.  
**Required:** No  
**Repeatable:** No  
**Accepted Values:** Text  

**Examples:**

```text
"https://doi.org/10.35802/212242"
```

<a name="funding-sources_order"></a>
##### Order

**Description:** Internal ICPSR field used to determine the order of importance for the funders associated with the data collection.  
**Required:** Yes  
**Repeatable:** No  
**Accepted Values:** Number  

**Examples:**

```text
"0"
```

```text
"1"
```

```text
"2"
```

```text
"3"
```

###### Complete Funding Sources Examples (with Subfields):

```yaml
- "Organization":
    "Name": "Robert Wood Johnson Foundation"
    "Name Code": "5643"
    "Name Uri": "https://icpsr.example.com/organizations/5643"
    "Ror": "https://ror.org/02ymmdj85"
  "Funding Awards":
  - "Funding Identifier": "MDR-8550085"
  - "Funding Identifier": "MDR-8550204"
  "Order": 0

- "Organization":
    "Name": "United States Department of Justice. Office of Justice Programs. Bureau\
      \ of Justice Statistics"
    "Name Code": "2342"
    "Name Uri": "https://icpsr.example.com/organizations/2342"
    "Ror": "https://ror.org/0006s4z66"
  "Funding Awards":
  - "Funding Identifier": "SES-1835721"
    "Funding URL": "https://doi.org/10.35802/000000"
  "Order": 1
```

```yaml
- "Organization":
    "Name": "Acme Foundation"
  "Order": 0
```


---

<a id="general-data-formats"></a>
### General Data Formats

**Description:** The file format types present in the data collection.  
**Required:** No  
**Repeatable:** Yes  
**Accepted Values:** Multi-part element; see subfields  
**Usage Notes:** This controlled vocabulary was taken from the DDI Alliance. Source: DDI Alliance CV GeneralDataFormat https://rdf-vocabulary.ddialliance.org/ddi-cv/GeneralDataFormat/2.0.3/GeneralDataFormat.html.  
#### Subfields:

| Property | Required? | Repeatable? | Accepted Values | Description |
|---|---|---|---|---|
| [General Data Format](#general-data-formats_label) | Yes | No | Text | A human-readable form of the term. |
| [General Data Format Code](#general-data-formats_code) | Yes | No | Text | A machine-readable/-actionable form of the term. |
| [General Data Format URI](#general-data-formats_uri) | Yes | No | Text | The URI for the term. |

<a name="general-data-formats_label"></a>
##### General Data Format

**Description:** A human-readable form of the term.  
**Required:** Yes  
**Repeatable:** No  
**Accepted Values:** Text  

**Examples:**

```text
"Text"
```

```text
"Still image"
```

```text
"Numeric"
```

<a name="general-data-formats_code"></a>
##### General Data Format Code

**Description:** A machine-readable/-actionable form of the term.  
**Required:** Yes  
**Repeatable:** No  
**Accepted Values:** Text  

**Examples:**

```text
"Text"
```

```text
"StillImage"
```

```text
"Numeric"
```

<a name="general-data-formats_uri"></a>
##### General Data Format URI

**Description:** The URI for the term.  
**Required:** Yes  
**Repeatable:** No  
**Accepted Values:** Text  
###### Complete General Data Formats Examples (with Subfields):

```yaml
- "General Data Format": "Text"
  "General Data Format Code": "Text"
  "General Data Format URI": "https://example.com/general_data_format/972"

- "General Data Format": "Still image"
  "General Data Format Code": "StillImage"
  "General Data Format URI": "https://example.com/general_data_format/234"
```

```yaml
- "General Data Format": "Numeric"
  "General Data Format Code": "Numeric"
  "General Data Format URI": "https://example.com/general_data_format/563"
```


---

<a id="geographic-coverage-areas"></a>
### Geographic Coverage Areas

**Description:** The geographic locations where the data refer or are related.  
**Required:** Yes  
**Repeatable:** Yes  
**Accepted Values:** Multi-part element; see subfields  
**Usage Notes:** In addition to the total geographic scope of the data, may include any additional levels of geographic coding provided in the variables.  
#### Subfields:

| Property | Required? | Repeatable? | Accepted Values | Description |
|---|---|---|---|---|
| [City](#geographic-coverage-areas_city) | No | No | Text | A town, city, or similar political entity covered in a data collection |
| [County](#geographic-coverage-areas_county) | No | No | Text | A county or similar administrative area covered in a data collection |
| [State](#geographic-coverage-areas_state) | No | No | Text | A state, province, canton or similar political entity covered in a data collection |
| [Country](#geographic-coverage-areas_country) | Yes | No | Text | A country covered in a data collection |
| [Geographic Coverage Area URI](#geographic-coverage-areas_uri) | No | No | Text | The unique identifier for the geographic coverage area. |

<a name="geographic-coverage-areas_city"></a>
##### City

**Description:** A town, city, or similar political entity covered in a data collection  
**Required:** No  
**Repeatable:** No  
**Accepted Values:** Text  

**Examples:**

```text
"Ann Arbor"
```

```text
"Hanover"
```

```text
"Chongqing"
```

<a name="geographic-coverage-areas_county"></a>
##### County

**Description:** A county or similar administrative area covered in a data collection  
**Required:** No  
**Repeatable:** No  
**Accepted Values:** Text  

**Examples:**

```text
"Monroe County"
```

```text
"Washtenaw County"
```

```text
"Cuyahoga County"
```

<a name="geographic-coverage-areas_state"></a>
##### State

**Description:** A state, province, canton or similar political entity covered in a data collection  
**Required:** No  
**Repeatable:** No  
**Accepted Values:** Text  

**Examples:**

```text
"Michigan"
```

```text
"Manitoba"
```

```text
"Yunnan"
```

<a name="geographic-coverage-areas_country"></a>
##### Country

**Description:** A country covered in a data collection  
**Required:** Yes  
**Repeatable:** No  
**Accepted Values:** Text  

**Examples:**

```text
"United States"
```

```text
"China"
```

```text
"Ghana"
```

<a name="geographic-coverage-areas_uri"></a>
##### Geographic Coverage Area URI

**Description:** The unique identifier for the geographic coverage area.  
**Required:** No  
**Repeatable:** No  
**Accepted Values:** Text  

**Examples:**

```text
"https://www.geonames.org/4990729/"
```

```text
"https://www.geonames.org/6269554"
```

###### Complete Geographic Coverage Areas Examples (with Subfields):

```yaml
- "City": "Cleveland"
  "State": "Ohio"
  "Country": "United States"
  "Geographic Coverage Area URI": "https://www.geonames.org/5150529"

- "City": "Pittsburgh"
  "State": "Pennsylvania"
  "Country": "United States"
  "Geographic Coverage Area URI": "https://www.geonames.org/5206379"
```

```yaml
- "Country": "Germany"
```


---

<a id="icpsr-subject-terms"></a>
### ICPSR Subject Terms

**Description:** A controlled list of social science terms maintained by ICPSR and used to indicate topics related to the data collection.  
**Required:** Yes  
**Repeatable:** Yes  
**Accepted Values:** Multi-part element; see subfields  
**Usage Notes:** This controlled vocabulary was taken from the ICPSR Subject Terms Thesaurus. Source: https://www.icpsr.umich.edu/web/ICPSR/thesaurus/10001.  
#### Subfields:

| Property | Required? | Repeatable? | Accepted Values | Description |
|---|---|---|---|---|
| [ICPSR Subject Term](#icpsr-subject-terms_label) | Yes | No | Text | A human-readable form of the subject term. |
| [ICPSR Subject Term Code](#icpsr-subject-terms_code) | Yes | No | Text | A machine-readable/-actionable form of the subject term. |
| [ICPSR Subject Term URI](#icpsr-subject-terms_uri) | Yes | No | Text | The URI for the subject term. |

<a name="icpsr-subject-terms_label"></a>
##### ICPSR Subject Term

**Description:** A human-readable form of the subject term.  
**Required:** Yes  
**Repeatable:** No  
**Accepted Values:** Text  

**Examples:**

```text
"abduction"
```

```text
"ability"
```

```text
"Abolition movement"
```

<a name="icpsr-subject-terms_code"></a>
##### ICPSR Subject Term Code

**Description:** A machine-readable/-actionable form of the subject term.  
**Required:** Yes  
**Repeatable:** No  
**Accepted Values:** Text  

**Examples:**

```text
"20391"
```

```text
"24123"
```

```text
"23632"
```

<a name="icpsr-subject-terms_uri"></a>
##### ICPSR Subject Term URI

**Description:** The URI for the subject term.  
**Required:** Yes  
**Repeatable:** No  
**Accepted Values:** Text  

**Examples:**

```text
"https://www.icpsr.umich.edu/web/ICPSR/thesaurus/10001/terms/20391"
```

```text
"https://www.icpsr.umich.edu/web/ICPSR/thesaurus/10001/terms/24040"
```

###### Complete ICPSR Subject Terms Examples (with Subfields):

```yaml
- "ICPSR Subject Term": "biographical data"
  "ICPSR Subject Term Code": "20391"
  "ICPSR Subject Term URI": "https://www.icpsr.umich.edu/web/ICPSR/thesaurus/10001/terms/20391"

- "ICPSR Subject Term": "age"
  "ICPSR Subject Term Code": "24123"
  "ICPSR Subject Term URI": "https://www.icpsr.umich.edu/web/ICPSR/thesaurus/10001/terms/24123"
```

```yaml
- "ICPSR Subject Term": "happiness"
  "ICPSR Subject Term Code": "25624"
  "ICPSR Subject Term URI": "https://www.icpsr.umich.edu/web/ICPSR/thesaurus/10001/terms/25624"
```


---

<a id="journal-of-economic-literature-(jel)-classification-codes"></a>
### Journal of Economic Literature (JEL) Classification Codes

**Description:** Classification codes used to categorize economic research.  
**Required:** No  
**Repeatable:** Yes  
**Accepted Values:** Multi-part element; see subfields  
**Usage Notes:** This controlled vocabulary was taken from the American Economic Association's JEL Classifications Codes. Source: https://www.aeaweb.org/jel/guide/jel.php  
#### Subfields:

| Property | Required? | Repeatable? | Accepted Values | Description |
|---|---|---|---|---|
| [JEL Classification Term](#journal-of-economic-literature-(jel)-classification-codes_label) | Yes | No | Text | A human-readable form of the term. |
| [JEL Classification Code](#journal-of-economic-literature-(jel)-classification-codes_code) | No | No | Text | A machine-readable/-actionable form of the term. |
| [JEL Classification URI](#journal-of-economic-literature-(jel)-classification-codes_uri) | No | No | Text | The URI for the JEL classification code. |

<a name="journal-of-economic-literature-(jel)-classification-codes_label"></a>
##### JEL Classification Term

**Description:** A human-readable form of the term.  
**Required:** Yes  
**Repeatable:** No  
**Accepted Values:** Text  

**Examples:**

```text
"A12 Relation of Economics to Other Disciplines"
```

```text
"B00 History of Economic Thought, Methodology, and Heterodox Approaches"
```

<a name="journal-of-economic-literature-(jel)-classification-codes_code"></a>
##### JEL Classification Code

**Description:** A machine-readable/-actionable form of the term.  
**Required:** No  
**Repeatable:** No  
**Accepted Values:** Text  

**Examples:**

```text
"a12"
```

```text
"b00"
```

```text
"n22"
```

<a name="journal-of-economic-literature-(jel)-classification-codes_uri"></a>
##### JEL Classification URI

**Description:** The URI for the JEL classification code.  
**Required:** No  
**Repeatable:** No  
**Accepted Values:** Text  

**Examples:**

```text
"http://example.com/jel/a12"
```

```text
"http://example.com/jel/b00"
```

###### Complete Journal of Economic Literature (JEL) Classification Codes Examples (with Subfields):

```yaml
- "JEL Classification Term": "A12 Relation of Economics to Other Disciplines"
  "JEL Classification Code": "a12"
  "JEL Classification URI": "http://example.com/jel/a12"

- "JEL Classification Term": "B00 History of Economic Thought, Methodology, and Heterodox\
    \ Approaches"
  "JEL Classification Code": "b00"
  "JEL Classification URI": "http://example.com/jel/b00"
```

```yaml
- "JEL Classification Term": "N22 Economic History: Financial Markets and Institutions:\
    \ U.S.; Canada: 1913-"
  "JEL Classification Code": "n22"
  "JEL Classification URI": "http://example.com/jel/n22"
```


---

<a id="license"></a>
### License

**Description:** A license governing the data's use.  
**Required:** No  
**Repeatable:** No  
**Accepted Values:** Multi-part element; see subfields  
#### Subfields:

| Property | Required? | Repeatable? | Accepted Values | Description |
|---|---|---|---|---|
| [License Name](#license_name) | No | No | Text |  |
| [License Code](#license_code) | No | No | Text |  |
| [License URI](#license_uri) | No | No | Text |  |

<a name="license_name"></a>
##### License Name

**Description:**   
**Required:** No  
**Repeatable:** No  
**Accepted Values:** Text  
<a name="license_code"></a>
##### License Code

**Description:**   
**Required:** No  
**Repeatable:** No  
**Accepted Values:** Text  
<a name="license_uri"></a>
##### License URI

**Description:**   
**Required:** No  
**Repeatable:** No  
**Accepted Values:** Text  
###### Complete License Examples (with Subfields):

```yaml
"License Name": "Creative Commons Attribution Non Commercial 4.0 International"
"License Code": "CC-BY-NC-4.0"
"License URI": "https://creativecommons.org/licenses/by-nc/4.0/"
```


---

<a id="medical-subject-headings-(mesh)-terms"></a>
### Medical Subject Headings (MeSH) Terms

**Description:** Biomedical and health-related terms from the National Library of Medicine that describe the data collection's topics.  
**Required:** No  
**Repeatable:** Yes  
**Accepted Values:** Multi-part element; see subfields  
**Usage Notes:** This controlled vocabulary was taken from the National Library of Medicine's Medical Subject Headings (MeSH). Source: https://www.ncbi.nlm.nih.gov/mesh/  
#### Subfields:

| Property | Required? | Repeatable? | Accepted Values | Description |
|---|---|---|---|---|
| [MeSH Subject Term](#medical-subject-headings-(mesh)-terms_label) | Yes | No | Text | A human-readable form of the subject term. |
| [MeSH Subject Term Code](#medical-subject-headings-(mesh)-terms_code) | Yes | No | Text | A machine-readable/-actionable form of the subject term. |
| [MeSH Subject Term URI](#medical-subject-headings-(mesh)-terms_uri) | Yes | No | Text | The URI for the subject term as maintained in MeSH. |

<a name="medical-subject-headings-(mesh)-terms_label"></a>
##### MeSH Subject Term

**Description:** A human-readable form of the subject term.  
**Required:** Yes  
**Repeatable:** No  
**Accepted Values:** Text  

**Examples:**

```text
"anxiety"
```

```text
"brain waves"
```

<a name="medical-subject-headings-(mesh)-terms_code"></a>
##### MeSH Subject Term Code

**Description:** A machine-readable/-actionable form of the subject term.  
**Required:** Yes  
**Repeatable:** No  
**Accepted Values:** Text  

**Examples:**

```text
"D001007"
```

```text
"D058256"
```

<a name="medical-subject-headings-(mesh)-terms_uri"></a>
##### MeSH Subject Term URI

**Description:** The URI for the subject term as maintained in MeSH.  
**Required:** Yes  
**Repeatable:** No  
**Accepted Values:** Text  
**Usage Notes:** Enter the MeSH RDF Unique Identifier.  

**Examples:**

```text
"http://id.nlm.nih.gov/mesh/D001007"
```

```text
"http://id.nlm.nih.gov/mesh/D058256"
```

###### Complete Medical Subject Headings (MeSH) Terms Examples (with Subfields):

```yaml
- "MeSH Subject Term": "anxiety"
  "MeSH Subject Term Code": "D001007"
  "MeSH Subject Term URI": "http://id.nlm.nih.gov/mesh/D001007"

- "MeSH Subject Term": "brain waves"
  "MeSH Subject Term Code": "D058256"
  "MeSH Subject Term URI": "http://id.nlm.nih.gov/mesh/D058256"
```


---

<a id="nationally-representative-sample"></a>
### Nationally Representative Sample

**Description:** Indicates whether the data collection uses a sampling design intended to represent the demographics, behaviors, and/or characteristics of the entire nation. This typically involves probability-based methods that allow generalization. It does not include convenience samples that appear similar to the nation by chance.  
**Required:** No  
**Repeatable:** No  
**Accepted Values:** Text  

**Examples:**

```text
"Yes"
```

```text
"No"
```


---

<a id="notes"></a>
### Notes

**Description:** Important details about the data collection (like unique authoring, discrepancies, or processing information) that can't be recorded in other metadata elements.  
**Required:** No  
**Repeatable:** Yes  
**Accepted Values:** Text  

**Examples:**

```text
"Information on the Index of Consumer Sentiment, the Index of Current Economic Conditions, and the Index of Consumer Expectations and how they were created can be found in the P.I. Codebook"
"Dataset 1 should be attributed to Jane Doe while datasets 2-6 should be attributed to John Doe"
```

```text
"Additional information on the Survey of Consumers can be found by visiting the Survey of Consumers Website"
```


---

<a id="organization"></a>
### Organization

**Description:** An organization associated with an ICPSR data collection or service.  
**Required:** No  
**Repeatable:** No  
**Accepted Values:** Multi-part element; see subfields  
#### Subfields:

| Property | Required? | Repeatable? | Accepted Values | Description |
|---|---|---|---|---|
| [Organization Name](#organization_name) | Yes | No | Text | The organization's name. |
| [Organization Name Code](#organization_name_code) | No | No | Text | A machine-readable/-actionable form of the organization's name. |
| [Organization Name URI](#organization_name_uri) | No | No | Text | The URI for the organization's name. |
| [ROR Identifier](#organization_ror) | No | No | Text | The organization's Research Organization Registry (ROR) identifier. |
| [Email Address](#organization_email) | No | No | Text | The organization's email address. |

<a name="organization_name"></a>
##### Organization Name

**Description:** The organization's name.  
**Required:** Yes  
**Repeatable:** No  
**Accepted Values:** Text  

**Examples:**

```text
"Federal Reserve Bank of St. Louis. Research Division"
```

```text
"University of Michigan. Institute for Social Research"
```

<a name="organization_name_code"></a>
##### Organization Name Code

**Description:** A machine-readable/-actionable form of the organization's name.  
**Required:** No  
**Repeatable:** No  
**Accepted Values:** Text  

**Examples:**

```text
"1234"
```

```text
"2345"
```

```text
"3456"
```

<a name="organization_name_uri"></a>
##### Organization Name URI

**Description:** The URI for the organization's name.  
**Required:** No  
**Repeatable:** No  
**Accepted Values:** Text  
<a name="organization_ror"></a>
##### ROR Identifier

**Description:** The organization's Research Organization Registry (ROR) identifier.  
**Required:** No  
**Repeatable:** No  
**Accepted Values:** Text  

**Examples:**

```text
"https://ror.org/02q7mkh03"
```

<a name="organization_email"></a>
##### Email Address

**Description:** The organization's email address.  
**Required:** No  
**Repeatable:** No  
**Accepted Values:** Text  

**Examples:**

```text
"info@example.com"
```

###### Complete Organization Examples (with Subfields):

```yaml
"Organization Name": "Urban Institute"
"Organization Name Code": "1234"
"Organization Name URI": "https://icpsr.example.com/organizations/1234"
"ROR Identifier": "https://ror.org/017pz3h73"
"Email Address": "info@urban.institute"
```


---

<a id="person"></a>
### Person

**Description:** A person associated with an ICPSR data collection or service.  
**Required:** No  
**Repeatable:** No  
**Accepted Values:** Multi-part element; see subfields  
#### Subfields:

| Property | Required? | Repeatable? | Accepted Values | Description |
|---|---|---|---|---|
| [Personal Name](#person_name) | Yes | No | Multi-part element; see subfields | The person's name. |
| [ORCID Identifier](#person_orcid) | No | No | Text | The person's Open Researcher and Contributor ID (ORCID). |
| [Affiliation(s)](#person_affiliations) | No | Yes | Array | The person's affiliated organization(s). |
| [Email Address](#person_email) | No | No | Text | The person's email address. |

<a name="person_name"></a>
##### Personal Name

**Description:** The person's name.  
**Required:** Yes  
**Repeatable:** No  
**Accepted Values:** Multi-part element; see subfields  

**Examples:**

```yaml
"Given Name (First Name)": "Susan B."
"Family Name (Last Name)": "Anthony"
```

```yaml
"Given Name (First Name)": "John"
"Family Name (Last Name)": "Doe IV"
```

##### Subfields:

| Property | Required? | Repeatable? | Accepted Values | Description |
|---|---|---|---|---|
| [Given Name (First Name)](#person_name_given) | Yes | No | Text | The person's first (given) name, which may include a middle name or initial. |
| [Family Name (Last Name)](#person_name_family) | Yes | No | Text | The person's last (family) name, which may include a suffix (e.g., Jr., Sr., IV). |

<a name="person_name_given"></a>
###### Given Name (First Name)

**Description:** The person's first (given) name, which may include a middle name or initial.  
**Required:** Yes  
**Repeatable:** No  
**Accepted Values:** Text  

**Examples:**

```text
"Chantel"
```

```text
"Giannis"
```

```text
"Mary Kate"
```

```text
"John Q."
```

<a name="person_name_family"></a>
###### Family Name (Last Name)

**Description:** The person's last (family) name, which may include a suffix (e.g., Jr., Sr., IV).  
**Required:** Yes  
**Repeatable:** No  
**Accepted Values:** Text  

**Examples:**

```text
"Smith"
```

```text
"Jordan Jr."
```

```text
"Escobar-Vega"
```

<a name="person_orcid"></a>
##### ORCID Identifier

**Description:** The person's Open Researcher and Contributor ID (ORCID).  
**Required:** No  
**Repeatable:** No  
**Accepted Values:** Text  

**Examples:**

```text
"https://orcid.org/0000-0001-6289-1234"
```

<a name="person_affiliations"></a>
##### Affiliation(s)

**Description:** The person's affiliated organization(s).  
**Required:** No  
**Repeatable:** Yes  
**Accepted Values:** Array  
<a name="person_email"></a>
##### Email Address

**Description:** The person's email address.  
**Required:** No  
**Repeatable:** No  
**Accepted Values:** Text  

**Examples:**

```text
"j.doe@example.com"
```

###### Complete Person Examples (with Subfields):

```yaml
"Personal Name":
  "Given Name (First Name)": "Jane Q."
  "Family Name (Last Name)": "Doe II"
"ORCID Identifier": "https://orcid.org/0000-0001-6666-5717"
"Researcher Passport Profile Id": "1234"
"Affiliation(s)":
- "Name": "Urban Institute"
  "Name Code": "2342"
  "Name Uri": "https://icpsr.example.com/organizations/2342"
  "Ror": "https://ror.org/017pz3h73"
  "Icpsr Org Id": "xyz123"
- "Name": "Example University"
"Email Address": "jane.doe@example.com"
```

```yaml
"Personal Name":
  "Given Name (First Name)": "Joe"
```


---

<a id="preregistration"></a>
### Preregistration

**Description:** A link to a research plan for the data collection (preferably a persistent identifier such as a DOI).  
**Required:** No  
**Repeatable:** No  
**Accepted Values:** Text  

**Examples:**

```text
"https://doi.org/10.1000/182"
```


---

<a id="principal-investigators"></a>
### Principal Investigators

**Description:** The key people or organizations responsible for the data collection, listed by importance. Each data collection requires at least one PI, either a person or an organization.  
**Required:** No  
**Repeatable:** Yes  
**Accepted Values:** Multi-part element; see subfields  
#### Subfields:

| Property | Required? | Repeatable? | Accepted Values | Description |
|---|---|---|---|---|
| [Person](#principal-investigators_person) | No | No | Object | See the [Person](#person) property. |
| [Organization](#principal-investigators_organization) | No | No | Object | See the [Organization](#organization) property. |
| [Order](#principal-investigators_order) | No | No | Number | The order or rank of importance for the PIs associated with the data collection, typically provided to ICPSR by the lead PI. |

<a name="principal-investigators_person"></a>
##### Person

**Description:** See the [Person](#person) property.  
**Required:** No  
**Repeatable:** No  
**Accepted Values:** See the [Person](#person) property  
<a name="principal-investigators_organization"></a>
##### Organization

**Description:** See the [Organization](#organization) property.  
**Required:** No  
**Repeatable:** No  
**Accepted Values:** See the [Organization](#organization) property  
<a name="principal-investigators_order"></a>
##### Order

**Description:** The order or rank of importance for the PIs associated with the data collection, typically provided to ICPSR by the lead PI.  
**Required:** No  
**Repeatable:** No  
**Accepted Values:** Number  

**Examples:**

```text
"0"
```

```text
"1"
```

```text
"2"
```

```text
"3"
```

###### Complete Principal Investigators Examples (with Subfields):

```text
"<p><b>Personal Principal Investigator</b></p><p><table><thead><tr><th>First Name</th><th>Last Name</th><th>Affiliation</th></tr></thead><tbody><tr><td>Veronica</td><td>Martinez-Ebers</td><td>National Institute for Law and Equity</td></tr><tr><td>Lawrence F.</td><td>Travis III</td><td>University of Cincinnati</td></tr></tbody></table></p>"
```

```text
"<p><b>Organizational Principal Investigator</b></p><p><table><thead><tr><th>Name</th></tr></thead><tbody><tr><td>United States Department of Labor. Bureau of Labor Statistics</td></tr><tr><td>The Washington Post</td></tr></tbody></table></p>"
```


---

<a id="response-rates"></a>
### Response Rates

**Description:** The percentage of respondents in the sample who participated in the data collection.  
**Required:** No  
**Repeatable:** No  
**Accepted Values:** Text  
**Usage Notes:** This field is only applicable if the data were collected with a survey instrument and the response rates are provided.  

**Examples:**

```text
"The overall response rate for this survey was 20.22%; 72.6% for existing panelists and 10.4% for new panelists, using AAPOR Response Rate 1."
```

```text
"Not applicable."
```


---

<a id="sampling-note"></a>
### Sampling Note

**Description:** Supplemental information about the sampling process that does not fit neatly into the Sampling Procedure field.  
**Required:** No  
**Repeatable:** No  
**Accepted Values:** Text  
**Usage Notes:** A detailed discussion of such things as sampling error or other limitations of the sampling methodology is not required here.  

**Examples:**

```text
"National sample of telephone numbers from cell (RDD) sampling frame."
```

```text
"The probability sample selected to represent the universe consists of approximately 71,000 households."
```


---

<a id="sampling-procedures"></a>
### Sampling Procedures

**Description:** The type(s) of sample and sample design used to select survey respondents to represent the population.  
**Required:** No  
**Repeatable:** Yes  
**Accepted Values:** Text  
**Usage Notes:** The sample is a selection out of the universe of all possible relevant cases (e.g., adults in the United States, housing units in three counties of Michigan, etc.) that could have been included in the data collection. Note that some studies, such as censuses, do not utilize samples but include all members of the universe. This controlled vocabulary was taken from the DDI Alliance. Source: DDI Alliance CV SamplingProcedure https://rdf-vocabulary.ddialliance.org/ddi-cv/SamplingProcedure/1.1.4/SamplingProcedure.html.  

**Examples:**

```yaml
- "Label": "Probability: Systematic random"
  "Code": "Probability.SystematicRandom"
  "Uri": "https://example.com/sampling_procedures/123"

- "Label": "Other"
  "Code": "Other"
  "Uri": "https://example.com/sampling_procedures/737"
```

```yaml
- "Label": "Total universe/Complete enumeration"
  "Code": "TotalUniverseCompleteEnumeration"
  "Uri": "https://example.com/sampling_procedures/234"
```


---

<a id="scales"></a>
### Scales

**Description:** Any commonly known scales used to collect data for the data collection (e.g., MMPI, CPI, the Census Occupational Codes, etc.).  
**Required:** No  
**Repeatable:** No  
**Accepted Values:** Text  
**Usage Notes:** Include common scales that can be readily identified from the data, documentation, or other related materials. ICPSR curators are not expected to infer or research scales that are not explicitly indicated. The scales can be cited either as a list or described in full sentences. If the questionnaire used has a finite list of responses (e.g., 'Always, Sometimes, Rarely, Never' or Strongly Agree, Agree, Disagree, Strongly Disagree'), it is acceptable for this element to note 'A Likert-type scale was used,' or 'Several Likert-type scales were used.' However, it is not required to note Likart-type scales in situations where only such scales were used, given their ubiquity.  

**Examples:**

```text
"The baseline data collection included one scale - the CES-D index for maternal depression [Cole, J. C., Rabin, A. S., Smith, T. L., and Kaufman, A. S. (2004). Development and validation of a Rasch-derived CES-D short form. Psychological assessment, 16(4), 360]. All scales used for outcomes at ages 1 through 3 are listed in Appendix Tables 1 and 2 in the User Guide. Please refer to the User Guide and P.I. Codebook, available under the 'Data and Documentation' tab, for details."
```

```text
"Squires, J., Bricker, D. D., and Twombly, E. (2009). Ages and stages questionnaires. Baltimore, MD: Paul H. Brookes."
"Briggs-Gowan, M. J., Carter, A. S., Irwin, J. R., Wachtel, K., and Cicchetti, D. V. (2004). The Brief Infant-Toddler Social and Emotional Assessment: screening for social-emotional problems and delays in competence. Journal of pediatric psychology, 29(2), 143-155."
"Yu, L., Buysse, D. J., Germain, A., Moul, D. E., Stover, A., Dodds, N. E., ... and Pilkonis, P. A. (2012). Development of short forms from the PROMIS sleep disturbance and sleep-related impairment item banks. Behavioral sleep medicine, 10(1), 6-24."
```


---

<a id="smallest-geographic-unit"></a>
### Smallest Geographic Unit

**Description:** The smallest geographic unit (e.g., state or census tract) used in the dataset.  
**Required:** No  
**Repeatable:** No  
**Accepted Values:** Multi-part element; see subfields  
**Usage Notes:** Geographic Unit is intended to represent specific, known geography -- e.g., county, census district, FIPS code, electoral district, and any other conveyor of specific geography that is represented by a variable. If the data do not include a geographic variable by which the data can be analyzed, this element is not indicated. If all the cases are from a single state, but the cases are not subdivided geographically within that state, then 'state' is not indicated. This element is only meant to convey specific, known, geography. If there is a variable indicating which testing site a survey was taken at, but the locations of the testing sites were masked by the PI, this element is likely not indicated.  
#### Subfields:

| Property | Required? | Repeatable? | Accepted Values | Description |
|---|---|---|---|---|
| [Smallest Geographic Unit Term](#smallest-geographic-unit_label) | No | No | Text |  |
| [Smallest Geographic Unit Code](#smallest-geographic-unit_code) | No | No | Text |  |
| [Smallest Geographic Unit URI](#smallest-geographic-unit_uri) | No | No | Text |  |

<a name="smallest-geographic-unit_label"></a>
##### Smallest Geographic Unit Term

**Description:**   
**Required:** No  
**Repeatable:** No  
**Accepted Values:** Text  
<a name="smallest-geographic-unit_code"></a>
##### Smallest Geographic Unit Code

**Description:**   
**Required:** No  
**Repeatable:** No  
**Accepted Values:** Text  
<a name="smallest-geographic-unit_uri"></a>
##### Smallest Geographic Unit URI

**Description:**   
**Required:** No  
**Repeatable:** No  
**Accepted Values:** Text  
###### Complete Smallest Geographic Unit Examples (with Subfields):

```yaml
"Smallest Geographic Unit Term": "state"
"Smallest Geographic Unit Code": "123"
"Smallest Geographic Unit URI": "https://example.com/smallest_geographic_unit/123"
```

```yaml
"Smallest Geographic Unit Term": "Census tract"
"Smallest Geographic Unit Code": "234"
"Smallest Geographic Unit URI": "https://example.com/smallest_geographic_unit/234"
```

```yaml
"Smallest Geographic Unit Term": "precinct"
"Smallest Geographic Unit Code": "345"
"Smallest Geographic Unit URI": "https://example.com/smallest_geographic_unit/345"
```


---

<a id="software-applications"></a>
### Software Applications

**Description:** Software used by the principal investigator(s) to collect or analyze data, required to understand how the data were obtained or to reproduce results.  
**Required:** No  
**Repeatable:** Yes  
**Accepted Values:** Multi-part element; see subfields  
#### Subfields:

| Property | Required? | Repeatable? | Accepted Values | Description |
|---|---|---|---|---|
| [Software Name](#software-applications_name) | Yes | No | Text | The name of the software application. |
| [Software Version](#software-applications_software_version) | No | No | Text | The version of the application. |
| [Software Description](#software-applications_description) | No | No | Text | Short description or overview of the application and its intended purpose |
| [Programming Languages](#software-applications_programming_languages) | No | Yes | Text | The programming language(s) used in the development of the application |
| [Operating Systems](#software-applications_operating_systems) | No | Yes | Text | Computer operating systems supported by the application |
| [Memory Requirements](#software-applications_memory_requirements) | No | No | Text | Minimum memory (e.g., RAM) requirements to operate the application |
| [Processor Requirements](#software-applications_processor_requirements) | No | No | Text | Processor architecture required to run the application |
| [Software Requirements](#software-applications_software_requirements) | No | No | Text | Required components for the application, like runtime environments and shared libraries not included in the package but needed to run it. |
| [Storage Requirements](#software-applications_storage_requirements) | No | No | Text | Amount of storage space required by the application |
| [Device Requirements](#software-applications_device_requirements) | No | No | Text | Device required to run the application. Used in cases where a specific make/model is required to run the application |
| [License](#software-applications_license) | No | No | Text | The license associated with the application, preferably expressed as a URL. |
| [Download URL](#software-applications_download_url) | No | No | Text | A direct link to a downloadable software artifact (e.g., executable, package, archive, or single script file) that retrieves the application itself, without additional navigation or instructions. |
| [Installation URL](#software-applications_install_url) | No | No | Text | A link to a repository or project landing page where users can obtain resources and instructions to install the application (as opposed to directly downloading a single file). |

<a name="software-applications_name"></a>
##### Software Name

**Description:** The name of the software application.  
**Required:** Yes  
**Repeatable:** No  
**Accepted Values:** Text  

**Examples:**

```text
"JHOVE"
```

```text
"ffmpeg"
```

```text
"json-schema-for-humans"
```

<a name="software-applications_software_version"></a>
##### Software Version

**Description:** The version of the application.  
**Required:** No  
**Repeatable:** No  
**Accepted Values:** Text  

**Examples:**

```text
"1"
```

```text
"2.0.4"
```

```text
"Auto-Build 2023-01-15 12:36"
```

<a name="software-applications_description"></a>
##### Software Description

**Description:** Short description or overview of the application and its intended purpose  
**Required:** No  
**Repeatable:** No  
**Accepted Values:** Text  

**Examples:**

```text
"JHOVE, the JSTOR/Harvard Object Validation Environment, is an extensible software framework for performing format identification, validation, and characterization of digital objects."
```

```text
"ffmpeg is a very fast video and audio converter that can also grab from a live audio/video source. It can also convert between arbitrary sample rates and resize video on the fly with a high quality polyphase filter."
```

<a name="software-applications_programming_languages"></a>
##### Programming Languages

**Description:** The programming language(s) used in the development of the application  
**Required:** No  
**Repeatable:** Yes  
**Accepted Values:** Text  

**Examples:**

```text
"python"
```

```text
"shell"
"r"
```

```text
"other"
```

<a name="software-applications_operating_systems"></a>
##### Operating Systems

**Description:** Computer operating systems supported by the application  
**Required:** No  
**Repeatable:** Yes  
**Accepted Values:** Text  

**Examples:**

```text
"windows"
```

```text
"windows"
"mac"
"linux"
```

```text
"other"
```

<a name="software-applications_memory_requirements"></a>
##### Memory Requirements

**Description:** Minimum memory (e.g., RAM) requirements to operate the application  
**Required:** No  
**Repeatable:** No  
**Accepted Values:** Text  

**Examples:**

```text
"4 GB"
```

```text
"1GB of RAM (2GB for a 64-bit version)"
```

```text
"4 GB of GPU memory for HD and some 4K media; 6 GB or more for 4K and higher"
```

<a name="software-applications_processor_requirements"></a>
##### Processor Requirements

**Description:** Processor architecture required to run the application  
**Required:** No  
**Repeatable:** No  
**Accepted Values:** Text  

**Examples:**

```text
"Intel i5/ i7/ Ryzen 7"
```

```text
"Minimum 1 GHz; Recommended 2GHz or more"
```

```text
"2.5–2.9 GHz or faster processor"
```

<a name="software-applications_software_requirements"></a>
##### Software Requirements

**Description:** Required components for the application, like runtime environments and shared libraries not included in the package but needed to run it.  
**Required:** No  
**Repeatable:** No  
**Accepted Values:** Text  

**Examples:**

```text
"Java runtime environment"
```

```text
"Requires additional Python libraries: numpy, v1.11.2; scipy, v0.18.1, and pandas, v0.19.0"
```

```text
"Compile with GNU auto tools"
```

<a name="software-applications_storage_requirements"></a>
##### Storage Requirements

**Description:** Amount of storage space required by the application  
**Required:** No  
**Repeatable:** No  
**Accepted Values:** Text  

**Examples:**

```text
"3.5 GB for new installations, 5 GB for upgrades (including temporary files required during installation)"
```

```text
"15 GB of free disk space"
```

```text
"8 GB of available hard-disk space for installation; additional free space required during installation"
```

<a name="software-applications_device_requirements"></a>
##### Device Requirements

**Description:** Device required to run the application. Used in cases where a specific make/model is required to run the application  
**Required:** No  
**Repeatable:** No  
**Accepted Values:** Text  

**Examples:**

<a name="software-applications_license"></a>
##### License

**Description:** The license associated with the application, preferably expressed as a URL.  
**Required:** No  
**Repeatable:** No  
**Accepted Values:** Text  

**Examples:**

```text
"https://www.apache.org/licenses/LICENSE-2.0"
```

```text
"https://opensource.org/licenses/LGPL-2.0"
```

<a name="software-applications_download_url"></a>
##### Download URL

**Description:** A direct link to a downloadable software artifact (e.g., executable, package, archive, or single script file) that retrieves the application itself, without additional navigation or instructions.  
**Required:** No  
**Repeatable:** No  
**Accepted Values:** Text  

**Examples:**

```text
"https://github.com/richardlehane/siegfried/archive/refs/heads/main.zip"
```

```text
"https://cdn.nationalarchives.gov.uk/documents/droid-binary-6.5.2-bin-win32-with-jre.zip"
```

<a name="software-applications_install_url"></a>
##### Installation URL

**Description:** A link to a repository or project landing page where users can obtain resources and instructions to install the application (as opposed to directly downloading a single file).  
**Required:** No  
**Repeatable:** No  
**Accepted Values:** Text  

**Examples:**

```text
"https://github.com/richardlehane/siegfried"
```

```text
"https://www.nationalarchives.gov.uk/information-management/manage-information/preserving-digital-records/droid/"
```

###### Complete Software Applications Examples (with Subfields):

```yaml
- "Software Name": "siegfried"
  "Software Version": "1.11.1"
  "Software Description": "Siegfried is a signature-based file format identification\
    \ tool, implementing the National Archives UK's PRONOM file format signatures;\
    \ freedesktop.org's MIME-info file format signatures; the Library of Congress's\
    \ FDD file format signatures (beta); and Wikidata (beta)."
  "Programming Languages":
  - "go"
  - "javascript"
  - "other"
  "Operating Systems":
  - "mac"
  - "linux"
  - "windows"
  "License": "https://www.apache.org/licenses/LICENSE-2.0"
  "Download URL": "https://github.com/richardlehane/siegfried/archive/refs/heads/main.zip"
```


---

<a id="study-design"></a>
### Study Design

**Description:** The procedures used to contact participants and gather data.  
**Required:** No  
**Repeatable:** No  
**Accepted Values:** Text  
**Usage Notes:** The Study Design provides more detailed information than the Summary, including how surveys were prepared and administered, how interviews were conducted, or how the data were obtained and compiled, as well as information about deadlines and follow-ups to respondents.  

**Examples:**

```text
"Data on organizational culture in each of the 12 courts (Part 1) were obtained by administering the Court Culture Assessment Instrument (CCAI) to all judges with a felony criminal court docket and to all senior court administrators. A total of 224 respondents completed the questionnaire. The CCAI was used to assess five key dimensions of current court culture orientation: (1) dominant case management style, (2) judicial and court staff relations, (3) change management, (4) courthouse leadership, and (5) internal organization. The determination of what culture judges and court administrators desired to establish in the near future was also obtained through the application of the same instrument (CACI) as practitioners were asked to indicate the type of culture in each work area (or content dimension) they would like to see in their court in the next five years."
```


---

<a id="summary"></a>
### Summary

**Description:** A description of the data collection that helps users understand its purpose, substance, and key topics.  
**Required:** Yes  
**Repeatable:** No  
**Accepted Values:** Text  
**Usage Notes:** The Summary may include information about the different parts of the data collection not adequately conveyed by the Fileset names or found elsewhere in the metadata. Other important components include a listing of major variables or categories of variables (with examples) as well as an indication of the data collection's unit of analysis (i.e., who or what is being studied: individuals, housing units, courts, criminal acts, etc.). Most often the unit of analysis is the individual; where it is not, it is particularly important to make this clear.

The Summary is written in the third person and avoids attempting to address issues of how the data might be used, who might be interested in the data, or any evaluative comments about the worth or usefulness of the data collection. The Summary uses past tense when describing the process of collecting the data and present tense when necessary, such as when describing the data (e.g., 'The MIDUS Refresher collection is split into two datasets.'). Numerals are used instead of spelling them out; if a number is spelled out for emphasis, the number is attached in parentheses (e.g. 'Two thousand (2,000)').  

**Examples:**

```text
"In 2014, Chicago Public Schools, looking to reduce the possibility of gun violence among school-aged youth, applied for a grant through the National Institute of Justice. CPS was awarded the Comprehensive School Safety Initiative grant and use said grant to establish the 'Connect and Redirect to Respect' program. This program used student social media data to identify and intervene with students thought to be at higher risk for committing violence. At-risk behaviors included brandishing a weapon, instigating conflict online, signaling gang involvement, and threats towards others. Identified at-risk students would be contacted by a member of the CPS Network Safety Team or the Chicago Police Department's Gang School Safety Team, depending on the risk level of the behavior. To evaluate the efficacy of CRR, the University of Chicago Crime Lab compared outcomes for students enrolled in schools that received the program to outcomes for students enrolled in comparison schools, which did not receive the program. 32 schools were selected for the study, with a total of 44,503 students. Demographic variables included age, race, sex, and ethnicity. Misconduct and academic variables included arrest history, in-school suspensions, out-of-school suspensions, GPA, and attendance days."
```

```text
"The Health and Relationship Project is a study of both spouses in same-sex and different-sex marriages who were legally married and aged 35 to 65 at the time of data collection (2015). There are two parts of this study: a baseline questionnaire and a daily diary questionnaire completed for 10 consecutive days; both components were completed online and spouses were asked to complete the surveys separately. The baseline questionnaire asks participants about a number of topics related to marriage and health, including stress, health status and health behaviors, relationship quality, and how they have approached health problems in the past. The diary questionnaire asks participants a number of questions about the past 24 hours, including daily stress experiences, social interactions, and health behaviors."
```


---

<a id="time-methods"></a>
### Time Methods

**Description:** The methods used to collect data over time, like snapshots at one point (cross-sectional) or repeatedly (longitudinal) to study changes or trends  
**Required:** No  
**Repeatable:** Yes  
**Accepted Values:** Multi-part element; see subfields  
**Usage Notes:** This controlled vocabulary was taken from the DDI Alliance. Source: DDI Alliance CV TimeMethod https://rdf-vocabulary.ddialliance.org/ddi-cv/TimeMethod/1.2.3/TimeMethod.html.  
#### Subfields:

| Property | Required? | Repeatable? | Accepted Values | Description |
|---|---|---|---|---|
| [Time Method](#time-methods_label) | Yes | No | Text | A human-readable form of the term. |
| [Time Method Code](#time-methods_code) | Yes | No | Text | A machine-readable/-actionable form of the term. |
| [Time Method URI](#time-methods_uri) | Yes | No | Text | The URI for the term. |

<a name="time-methods_label"></a>
##### Time Method

**Description:** A human-readable form of the term.  
**Required:** Yes  
**Repeatable:** No  
**Accepted Values:** Text  

**Examples:**

```text
"Cross-section"
```

```text
"Longitudinal: Cohort/Event-based"
```

```text
"Time series"
```

<a name="time-methods_code"></a>
##### Time Method Code

**Description:** A machine-readable/-actionable form of the term.  
**Required:** Yes  
**Repeatable:** No  
**Accepted Values:** Text  

**Examples:**

```text
"CrossSection"
```

```text
"Longitudinal.CohortEventBased"
```

```text
"Other"
```

<a name="time-methods_uri"></a>
##### Time Method URI

**Description:** The URI for the term.  
**Required:** Yes  
**Repeatable:** No  
**Accepted Values:** Text  
###### Complete Time Methods Examples (with Subfields):

```yaml
- "Time Method": "Registers/Records/Accounts: Medical/Clinical"
  "Time Method Code": "RegistersRecordsAccounts.MedicalClinical"
  "Time Method URI": "https://example.com/time_methods/123"

- "Time Method": "Events/Interactions"
  "Time Method Code": "EventsInteractions"
  "Time Method URI": "https://example.com/time_methods/234"
```

```yaml
- "Time Method": "Other"
  "Time Method Code": "Other"
  "Time Method URI": "https://example.com/time_methods/737"
```


---

<a id="time-periods"></a>
### Time Periods

**Description:** The time period(s) to which the data refer, regardless of when the data were collected.  
**Required:** Yes  
**Repeatable:** Yes  
**Accepted Values:** Multi-part element; see subfields  
#### Subfields:

| Property | Required? | Repeatable? | Accepted Values | Description |
|---|---|---|---|---|
| [Start Date](#time-periods_start_date) | Yes | No | Text | The start date for the time period the data refer to, formatted as YYYY, YYYY-MM, or YYYY-MM-DD, with no spaces in date expressions. |
| [End Date](#time-periods_end_date) | Yes | No | Text | The end date for the time period the data refer to, formatted as YYYY, YYYY-MM, or YYYY-MM-DD, with no spaces in date expressions. |
| [Time Frame](#time-periods_time_frame) | No | No | Text | An optional free-text description of the time period, used for non-numeric dates (e.g., 'Fall 2012') or to add context when multiple dates are present. |

<a name="time-periods_start_date"></a>
##### Start Date

**Description:** The start date for the time period the data refer to, formatted as YYYY, YYYY-MM, or YYYY-MM-DD, with no spaces in date expressions.  
**Required:** Yes  
**Repeatable:** No  
**Accepted Values:** Text  

**Examples:**

```text
"2000"
```

```text
"2019-10"
```

```text
"2021-03-01"
```

<a name="time-periods_end_date"></a>
##### End Date

**Description:** The end date for the time period the data refer to, formatted as YYYY, YYYY-MM, or YYYY-MM-DD, with no spaces in date expressions.  
**Required:** Yes  
**Repeatable:** No  
**Accepted Values:** Text  

**Examples:**

```text
"2000"
```

```text
"2019-10"
```

```text
"2021-03-01"
```

<a name="time-periods_time_frame"></a>
##### Time Frame

**Description:** An optional free-text description of the time period, used for non-numeric dates (e.g., 'Fall 2012') or to add context when multiple dates are present.  
**Required:** No  
**Repeatable:** No  
**Accepted Values:** Text  
**Usage Notes:** The Time Frame should not simply restate the date(s) in words. For example, if the Time Period starts in 2020-01, the Time Frame should repeat 'January 2020'.  

**Examples:**

```text
"Fall 2001"
```

```text
"Winter Semester 2019"
```

###### Complete Time Periods Examples (with Subfields):

```yaml
- "Start Date": "2018"
  "End Date": "2018"
  "Time Frame": "Summer and Fall 2018"

- "Start Date": "2020-10"
  "End Date": "2020-10"
```


---

<a id="title"></a>
### Title

**Description:** The official title that describes what the data collection is about, its geographic scope, and the time period it covered.  
**Required:** Yes  
**Repeatable:** No  
**Accepted Values:** Text  

**Examples:**

```text
"Bridge of Faith: Aim4Peace Community-Based Violence Prevention Project, Kansas City, Missouri, 2014-2017"
```

```text
"Health and Relationships Project, United States, 2014-2015"
```

```text
"Targeted Interventions to Prevent Chronic Low Back Pain in High Risk Patients: A Multi-Site Pragmatic Randomized Controlled Trial (TARGET Trial), 4 U.S. cities, 2016-2019"
```

```text
"Aid Like A Paycheck (ALAP), Texas and California, 2014-2017"
```

```text
"COVID-19 Disruptions Disproportionately Affect Female Academics, Global, 2020"
```


---

<a id="units-of-analysis"></a>
### Units of Analysis

**Description:** The object(s) of analysis for the data collection, such as an organization, individual, or household.  
**Required:** No  
**Repeatable:** Yes  
**Accepted Values:** Multi-part element; see subfields  
**Usage Notes:** This controlled vocabulary was taken from the DDI Alliance. Source: DDI Alliance CV AnalysisUnit https://rdf-vocabulary.ddialliance.org/ddi-cv/AnalysisUnit/2.1.3/AnalysisUnit.html.  
#### Subfields:

| Property | Required? | Repeatable? | Accepted Values | Description |
|---|---|---|---|---|
| [Label](#units-of-analysis_label) | Yes | No | Text | A human-readable form of the term. |
| [Code](#units-of-analysis_code) | Yes | No | Text | A machine-readable/-actionable form of the term. |
| [Uri](#units-of-analysis_uri) | Yes | No | Text | The URI for the term. |

<a name="units-of-analysis_label"></a>
##### Label

**Description:** A human-readable form of the term.  
**Required:** Yes  
**Repeatable:** No  
**Accepted Values:** Text  

**Examples:**

```text
"Organization/Institution"
```

```text
"Individual"
```

```text
"Household"
```

<a name="units-of-analysis_code"></a>
##### Code

**Description:** A machine-readable/-actionable form of the term.  
**Required:** Yes  
**Repeatable:** No  
**Accepted Values:** Text  

**Examples:**

```text
"OrganizationOrInstitution"
```

```text
"Individual"
```

```text
"Household"
```

<a name="units-of-analysis_uri"></a>
##### Uri

**Description:** The URI for the term.  
**Required:** Yes  
**Repeatable:** No  
**Accepted Values:** Text  
###### Complete Units of Analysis Examples (with Subfields):

```yaml
- "Label": "Organization/Institution"
  "Code": "OrganizationOrInstitution"
  "Uri": "https://example.com/units_of_analysis/123"

- "Label": "Individual"
  "Code": "Individual"
  "Uri": "https://example.com/units_of_analysis/234"
```

```yaml
- "Label": "Household"
  "Code": "Household"
  "Uri": "https://example.com/units_of_analysis/737"
```


---

<a id="universe"></a>
### Universe

**Description:** The total group of persons or other entities (e.g., households or organizations) that were the object of research and to which analytic results refer.  
**Required:** No  
**Repeatable:** No  
**Accepted Values:** Text  
**Usage Notes:** Age, nationality, and residence commonly help to delineate a given universe, but any of a number of factors may be involved, such as sex, race, income, veteran status, criminal convictions, etc. The Universe may consist of elements other than persons, such as housing units, court cases, deaths, countries, etc. It should be possible to tell from the description of the universe whether a given individual or element (hypothetical or real) is a member of the population under study. Typically, the Universe statement is about one sentence or shorter, and reflects the entire possible population a data collection sought to study.  

**Examples:**

```text
"All households in the United States with phones."
```

```text
"Part 1: Thirty cities in Massachusetts during 1980-1986. Parts 2-4: All residents in Massachusetts during 1986."
```

```text
"Individuals self-identified as transgender, trans, genderqueer, non-binary, or other identities on the transgender identity spectrum aged 18 and older residing in the fifty U.S. states, the District of Columbia, American Samoa, Guam, Puerto Rico, and U.S. military bases overseas."
```

```text
"Jihadists from the United States and Canada, along with Incels from Germany, Canada, the United States, and United Kingdom."
```

```text
"All publicly funded medical examiner and coroner offices."
```

```text
"Uncertified ballots for the 2000 United States presidential election in Florida."
```


---

<a id="variable-description"></a>
### Variable Description

**Description:** Significant variables (particularly demographic variables) in the data files.  
**Required:** No  
**Repeatable:** No  
**Accepted Values:** Text  
**Usage Notes:** The Variable Description provides more detailed information than the Summary, including a review of variables that are important for users to know about. The codebook, setup files, and variable groups are appropriate sources of information for Variable Description.  

**Examples:**

```text
"The data includes variables about participants' and their parents' moods, interviewer observations, families' activities, families' health history, participants' school records, and parents' substance use. Demographic variables include race, religion, annual household income, and the participants' parents' employment statuses."
```

```text
"The LGBTQ Hate Crimes Interviews dataset contains more in-depth information, including victim demographic information, substance abuse history, information on whether the victim is open about their LGBTQ identification, the victim's job status, and information about how the victim reacted to the crime, such as whether or not they reported the crime to the police and their level of cooperation with the police and prosecution."
```


---

<a id="version-history"></a>
### Version History

**Description:** A record of how the data collection has changed over time.  
**Required:** No  
**Repeatable:** Yes  
**Accepted Values:** Multi-part element; see subfields  
#### Subfields:

| Property | Required? | Repeatable? | Accepted Values | Description |
|---|---|---|---|---|
| [Version Number](#version-history_version_number) | No | No | Text | A version number for a study. |
| [Version Date](#version-history_version_date) | No | No | Text | The date on which a given version of a data collection was released. |
| [Version Note](#version-history_version_note) | No | No | Text | Provenance information about a given version of the data collection. |

<a name="version-history_version_number"></a>
##### Version Number

**Description:** A version number for a study.  
**Required:** No  
**Repeatable:** No  
**Accepted Values:** Text  
**Usage Notes:** Versioning should follow ICPSR conventions  

**Examples:**

```text
"V1"
```

```text
"V2"
```

```text
"V3"
```

<a name="version-history_version_date"></a>
##### Version Date

**Description:** The date on which a given version of a data collection was released.  
**Required:** No  
**Repeatable:** No  
**Accepted Values:** Text  

**Examples:**

```text
"2020-07-20"
```

```text
"2022-01-31"
```

<a name="version-history_version_note"></a>
##### Version Note

**Description:** Provenance information about a given version of the data collection.  
**Required:** No  
**Repeatable:** No  
**Accepted Values:** Text  

**Examples:**

```text
"File CB3025.ALL.PDF was removed from any previous datasets and flagged as a study-level file, so that it will accompany all downloads."
```

```text
"The data producer provided additional data files."
```

```text
"The codebook descriptions of variables TANSUP, EMOSUP, and SOCSUP were corrected."
```

###### Complete Version History Examples (with Subfields):

```yaml
- "Version Number": "V2"
  "Version Date": "2023-08-12"
  "Version Note": "The data producer provided additional data files."

- "Version Number": "V1"
  "Version Date": "2021-03-01"
  "Version Note": "Initial release"
```

```yaml
- "Version Number": "V1"
  "Version Date": "2024-06-28"
  "Version Note": "Initial release"
```


---

<a id="weights"></a>
### Weights

**Description:** The weight variables and the criteria for using them in data analysis or other information about how the data are weighted if no weight variables are present.  
**Required:** No  
**Repeatable:** No  
**Accepted Values:** Text  
**Usage Notes:** Weight includes any information about weighting variables in the data, as well as any other weight information provided by the Principal Investigator. If a weighting formula or coefficient was developed, provide this formula, define its elements, and indicate how the formula is applied to the data. It is acceptable to summarize additional documentation and refer users to those resources for more information.  

**Examples:**

```text
"Both the TransPop and Cisgender datasets have the same variable named WEIGHT as the weighting variable. The combination datasets have a set of three weight variables (WEIGHT_TRANSPOP, WEIGHT_CISGENDER, WEIGHT_CISGENDER_TRANSPOP)"
```

```text
"A weight variable with two implied decimal places has been included and must be used in any analysis."
```


---
