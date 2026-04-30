# ICPSR Metadata Schema

Last updated: April 30, 2026


This metadata schema is used to describe data collections at the Inter-university Consortium for Political and Social Research (ICPSR) after 2026. 

These rules and definitions document ICPSR's metadata practices and are intended to (a) assist ICPSR staff with metadata entry, and (b) help users – including data depositors and researchers – understand and interpret ICPSR metadata.

Machine-actionable copies of metadata field definitions are also available in [JSON Schema](https://github.com/ICPSR/metadata/tree/rde_documentation/rde_schema/property_bank) format.
## Metadata Elements: Overview

| Property | Required? | Repeatable? | Accepted Values | Description |
|---|---|---|---|---|
| [Title](#title) | Yes | No | Text | The official title that describes what the data collection is about, its geographic scope, and the time period it covered. |
| [Alternate Titles](#alternate-titles) | No | Yes | Text | The alternate name(s) or acronym(s) commonly used to refer to the data collection. |
| [Principal Investigators](#principal-investigators) | Yes | Yes | Multi-part element; see subfields | The key people or organizations responsible for the data collection, listed by importance. Each data collection requires at least one PI, either a person or an organization. |
| [Funding Sources](#funding-sources) | No | Yes | Multi-part element; see subfields | The sources of funding that supported the data collection. |
| [Summary](#summary) | Yes | No | Text | A description of the data collection that helps users understand its purpose, substance, and key topics. |
| [ICPSR Subject Terms](#icpsr-subject-terms) | Yes | Yes | Multi-part element; see subfields | A controlled list of social science terms maintained by ICPSR and used to indicate topics related to the data collection. |
| [Journal of Economic Literature (JEL) Classification Codes](#journal-of-economic-literature-(jel)-classification-codes) | No | Yes | Multi-part element; see subfields | Classification codes used to categorize economic research. |
| [Medical Subject Headings (MeSH) Terms](#medical-subject-headings-(mesh)-terms) | No | Yes | Multi-part element; see subfields | Biomedical and health-related terms from the National Library of Medicine that describe the data collection's topics. |
| [Time Periods](#time-periods) | Yes | Yes | Multi-part element; see subfields | The time period(s) to which the data refer, regardless of when the data were collected. |
| [Nationally Representative Sample](#nationally-representative-sample) | No | No | Text | Indicates whether the data collection uses a sampling design intended to represent the demographics, behaviors, and/or characteristics of the entire nation. This typically involves probability-based methods that allow generalization. It does not include convenience samples that appear similar to the nation by chance. |
| [Geographic Coverage Areas](#geographic-coverage-areas) | Yes | Yes | Multi-part element; see subfields | The geographic locations where the data refer or are related. |
| [Smallest Geographic Unit](#smallest-geographic-unit) | No | No | Multi-part element; see subfields | The smallest geographic unit (e.g., state or census tract) used in the dataset. |
| [Study Design](#study-design) | No | No | Text | The procedures used to contact participants and gather data. |
| [Universe](#universe) | No | No | Text | The total group of persons or other entities (e.g., households or organizations) that were the object of research and to which analytic results refer. |
| [Time Methods](#time-methods) | No | Yes | Multi-part element; see subfields | The methods used to collect data over time, like snapshots at one point (cross-sectional) or repeatedly (longitudinal) to study changes or trends. |
| [Units of Analysis](#units-of-analysis) | No | Yes | Multi-part element; see subfields | The object(s) of analysis for the data collection, such as an organization, individual, or household. |
| [Sampling Procedures](#sampling-procedures) | No | Yes | Text | The type(s) of sample and sample design used to select survey respondents to represent the population. |
| [Sampling Note](#sampling-note) | No | No | Text | Supplemental information about the sampling process that does not fit neatly into the Sampling Procedure field. |
| [Weights](#weights) | No | No | Text | The weight variables and the criteria for using them in data analysis, or other information about how the data are weighted if no weight variables are present. |
| [Response Rates](#response-rates) | No | No | Text | The percentage of respondents in the sample who participated in the data collection. |
| [Data Source Types](#data-source-types) | No | Yes | Multi-part element; see subfields | The source(s) of the data as collected by the Principal Investigators. |
| [External Data Sources](#external-data-sources) | No | Yes | Text | The source of the data, when that source is external to the data collection and can be independently cited. |
| [Collection Modes](#collection-modes) | No | Yes | Multi-part element; see subfields | The method(s) or procedure(s) used to collect the data, such as an interview or experiment. |
| [Collection Dates](#collection-dates) | No | Yes | Multi-part element; see subfields | The date(s) data collection took place. |
| [Variable Description](#variable-description) | No | No | Text | Significant variables (particularly demographic variables) in the data files. |
| [Scales](#scales) | No | No | Text | Any commonly known scales, measures, or inventories used in the data collection. |
| [Data Management Plan](#data-management-plan) | No | No | Text | A link to the data management plan (preferably a persistent identifier such as a DOI). |
| [Preregistration](#preregistration) | No | No | Text | A link to a research plan for the data collection (preferably a persistent identifier such as a DOI). |
| [Software Applications](#software-applications) | No | Yes | Multi-part element; see subfields | Software used by the principal investigator(s) to collect or analyze data, required to understand how the data were obtained or to reproduce results. |
| [General Data Formats](#general-data-formats) | No | Yes | Multi-part element; see subfields | The file format types present in the data collection. |
| [Notes](#notes) | No | Yes | Text | Important details about the data collection (like unique authoring, discrepancies, or processing information) that can't be recorded in other metadata elements. |
| [Manuscript Number](#manuscript-number) | No | No | Text | A unique identifier that associates the data collection with a manuscript submitted to a journal. |
| [ADA Accessibility](#ada-accessibility) | No | No | Multi-part element; see subfields | Indicates whether the data collection is ADA accessible, conforming to WCAG 2.1 AA standards, or qualifies for the ADA archival exception. |
| [License](#license) | No | No | Multi-part element; see subfields | A license governing the data's use. |
| [Version History](#version-history) | No | Yes | Multi-part element; see subfields | A record of how the data collection has changed over time. |
| [Distributors](#distributors) | No | Yes | Multi-part element; see subfields | The organization(s) responsible for distributing the data collection. |
| [Study Number](#study-number) | Yes | No | Number | A unique, numerical value used by ICPSR to identify and track data collections. |
| [Digital Object Identifier (DOI)](#digital-object-identifier-(doi)) | Yes | No | Text | The registered persistent digital object identifier (DOI) associated with the data collection. |
| [Citation](#citation) | No | No | Text | The official way to reference the data collection in writing. |
| [Person](#person) | No | No | Multi-part element; see subfields | A person associated with an ICPSR data collection or service. |
| [Organization](#organization) | No | No | Multi-part element; see subfields | An organization associated with an ICPSR data collection or service. |

---

## Key for ICPSR Metadata Schema Entries

Full information for each ICPSR study metadata element includes the following fields:

- **Description:** A short description of the metadata element and the information it is intended to convey.
- **Required:** Indicates whether the metadata element is mandatory ("Yes") or optional ("No"). Required elements must include at least one value.
- **Repeatable:** Indicates whether the metadata element may be repeated ("Yes") or if it may only occur once ("No").
- **Accepted values:** The type of values that may be used with the metadata element; options include text (with additional requirements, such as date formatting, noted when present) and numbers. Multi-part metadata elements have accepted value information provided in entries for individual subelements.
- **Usage Notes:** Additional information about the nature, scope, and conventions for values that may be added to the metadata element.   
- **Examples:** Examples of valid values for the metadata element.
 

---
## Metadata Elements: Detailed Information

<a id="title"></a>
### Title

**Description:** The official title that describes what the data collection is about, its geographic scope, and the time period it covered.

**Required:** Yes

**Repeatable:** No

**Accepted Values:** Text

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

  * Brackets are typically not indicated. They are indicated when a study has National, Federal, Congressional, or American in the title. Brackets can be indicated if a non-United States study has "National" in the title, or a similar word specific to that country.

Time Period:

  * All titles include the data collection's time period, which reflects the time period that the data collection covers and should match the Time Period. For example, in the 'Uganda Elite Study, 1964-1968', it is assumed that the Ugandans were surveyed about events in 1964-1968, even if the actual data collection might not have taken place until later.

  * If the time period is already included in the title proper, it is not repeated.

  * For most studies, a single year or range of years is acceptable. Years are written as four digits, including when used in a range (e.g., '1999', '2001-2003', or '1999, 2010, 2015').

  * Months are included only when part of ICPSR series that have multiple releases, which are otherwise identical, each year. In these cases, months are spelled out (e.g., 'September 2020' instead of '9/2020' or 'Sept. 2020').

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

<a id="alternate-titles"></a>
### Alternate Titles

**Description:** The alternate name(s) or acronym(s) commonly used to refer to the data collection.

**Required:** No

**Repeatable:** Yes

**Accepted Values:** Text

**Usage Notes:** Alternate Title often takes the form of a shortened (by abbreviation or acronym) version of the official title.

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

<a id="principal-investigators"></a>
### Principal Investigators

**Description:** The key people or organizations responsible for the data collection, listed by importance. Each data collection requires at least one PI, either a person or an organization.

**Required:** Yes

**Repeatable:** Yes

**Accepted Values:** Multi-part element; see subfields

#### Subfields:

| Property | Required? | Repeatable? | Accepted Values | Description |
|---|---|---|---|---|
| [Person](#principal-investigators_person) | Conditional | No | Multi-part element; see subfields | Name and other details about the principal investigator, if it is an individual person. |
| [Organization](#principal-investigators_organization) | Conditional | No | Multi-part element; see subfields | Name and other details about the principal investigator, if it is an organization. |
| [Order](#principal-investigators_order) | Yes | No | Number | The order or rank of importance for the PIs associated with the data collection, typically provided to ICPSR by the lead PI. |

<a name="principal-investigators_person"></a>
##### Person

**Description:** Name and other details about the principal investigator, if it is an individual person.

**Required:** Conditional (must include either Person or Organization)

**Repeatable:** No

**Accepted Values:** Multi-part element; for more information, see the [Person](#person) field

**Usage Notes:** When the PI is a person:

  *  Use "Search for a Person" to enter the name, affiliation, and ORCID ID that appear in the person's [ORCID](https://orcid.org/) profile.  
  *  If you can't find an ORCID ID for a PI, enter their full name the way it appears in publications or their curriculum vitae. Enter middle names and initials in the Given Name field and suffixes (e.g. Jr., III) in the Family Name field.  
  *  Enter the PI's affiliation as it appears in the [Research Organization Registry](https://ror.org/) (ROR). If the organization doesn't have a ROR ID, use its full name, avoid acronyms, and do not include departments or colleges.  
  *  Enter a PI's affiliation at the time the research was conducted.

<a name="principal-investigators_organization"></a>
##### Organization

**Description:** Name and other details about the principal investigator, if it is an organization.

**Required:** Conditional (must include either Person or Organization)

**Repeatable:** No

**Accepted Values:** Multi-part element; for more information, see the [Organization](#organization) field

**Usage Notes:** When the PI is an organization, Enter the name as it appears in the [Research Organization Registry](https://ror.org/) (ROR). If the organization doesn’t have a ROR ID, use its full name and avoid acronyms.

<a name="principal-investigators_order"></a>
##### Order

**Description:** The order or rank of importance for the PIs associated with the data collection, typically provided to ICPSR by the lead PI.

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

#### Complete Principal Investigators Examples (with Subfields):

```yaml
- "Person":
    "Name":
      "Given": "Miner P."
      "Family": "Marchbanks III"
  "Order": 0
```

```yaml
- "Person":
    "Name":
      "Given": "Robert J."
      "Family": "Shiller"
    "Orcid": "https://orcid.org/0009-0006-2316-6486"
    "Affiliations":
    - "Name": "Yale University"
      "Ror": "https://ror.org/03v76x132"
    - "Name": "MacroMarkets"
  "Order": 0

- "Person":
    "Name":
      "Given": "Claudia"
      "Family": "Goldin"
    "Orcid": "https://orcid.org/0000-0003-3842-1604"
    "Affiliations":
    - "Name": "Harvard University"
      "Ror": "https://ror.org/03vek6s52"
  "Order": 1

- "Organization":
    "Name": "Bureau of Justice Statistics"
    "Ror": "https://ror.org/0006s4z66"
  "Order": 2
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
| [Funding Organization](#funding-sources_organization) | Yes | No | Multi-part element; see subfields | Name and other details about the organization that provided the funding. |
| [Funding Awards](#funding-sources_grants) | No | Yes | Multi-part element; see subfields | Identifiers and other details about financial support for the data collection. |
| [Order](#funding-sources_order) | Yes | No | Number | Internal ICPSR field used to determine the order of importance for the funders associated with the data collection. |

<a name="funding-sources_organization"></a>
##### Funding Organization

**Description:** Name and other details about the organization that provided the funding.

**Required:** Yes

**Repeatable:** No

**Accepted Values:** Multi-part element; for more information, see the [Organization](#organization) field

**Usage Notes:** Tips for entering the Funding Organization:

  * Whenever possible, enter the organization’s name as it appears in the [Research Organization Registry](https://ror.org/) (ROR).  
  * Enter the name without any organization hierarchy, for example, "National Institute on Aging" instead of "United States Department of Health and Human Services. National Institutes of Health. National Institute on Aging". 
  * If the organization doesn’t have a ROR, use its full name and avoid acronyms.  
  * Whenever possible, include a unique identifier for the funding award. This can be a grant number; a URL, preferably a persistent one like a digital object identifier (DOI); or both.

<a name="funding-sources_grants"></a>
##### Funding Awards

**Description:** Identifiers and other details about financial support for the data collection.

**Required:** No

**Repeatable:** Yes

**Accepted Values:** Multi-part element; see subfields

**Usage Notes:** Whenever possible, include a unique identifier for the funding award. This can be a grant number; a URL, preferably a persistent one like a digital object identifier (DOI); or both.

##### Subfields:

| Property | Required? | Repeatable? | Accepted Values | Description |
|---|---|---|---|---|
| [Funding Identifier](#funding-sources_grants_grant_number) | Yes | No | Text | The unique identifier for the funding (e.g., ABC-0123456). |
| [Funding URL](#funding-sources_grants_grant_uri) | No | No | Text | A unique identifier (URL), preferably a persistent one like a DOI,  linking to a landing page with funding information. |

<a name="funding-sources_grants_grant_number"></a>
###### Funding Identifier

**Description:** The unique identifier for the funding (e.g., ABC-0123456).

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

#### Complete Funding Sources Examples (with Subfields):

```yaml
- "Funding Organization":
    "Name": "Robert Wood Johnson Foundation"
    "Ror": "https://ror.org/02ymmdj85"
  "Funding Awards":
  - "Funding Identifier": "MDR-8550085"
  - "Funding Identifier": "MDR-8550204"
  "Order": 0

- "Funding Organization":
    "Name": "Bureau of Justice Statistics"
    "Ror": "https://ror.org/0006s4z66"
  "Funding Awards":
  - "Funding Identifier": "SES-1835721"
    "Funding URL": "https://doi.org/10.35802/000000"
  "Order": 1
```

```yaml
- "Funding Organization":
    "Name": "Acme Foundation"
  "Order": 0
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
"employment"
```

```text
"marriage"
```

```text
"recidivism"
```

<a name="icpsr-subject-terms_code"></a>
##### ICPSR Subject Term Code

**Description:** A machine-readable/-actionable form of the subject term.

**Required:** Yes

**Repeatable:** No

**Accepted Values:** Text

**Examples:**

```text
"25220"
```

```text
"26180"
```

```text
"26961"
```

<a name="icpsr-subject-terms_uri"></a>
##### ICPSR Subject Term URI

**Description:** The URI for the subject term.

**Required:** Yes

**Repeatable:** No

**Accepted Values:** Text

**Examples:**

```text
"https://www.icpsr.umich.edu/web/ICPSR/thesaurus/10001/terms/25220"
```

```text
"https://www.icpsr.umich.edu/web/ICPSR/thesaurus/10001/terms/26180"
```

#### Complete ICPSR Subject Terms Examples (with Subfields):

```yaml
- "ICPSR Subject Term": "lobbying"
  "ICPSR Subject Term Code": "26131"
  "ICPSR Subject Term URI": "https://www.icpsr.umich.edu/web/ICPSR/thesaurus/10001/terms/26131"

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
| [Label](#journal-of-economic-literature-(jel)-classification-codes_label) | Yes | No | Text | A human-readable form of the term. |
| [Code](#journal-of-economic-literature-(jel)-classification-codes_code) | Yes | No | Text | A machine-readable/-actionable form of the term. |
| [URI](#journal-of-economic-literature-(jel)-classification-codes_uri) | Yes | No | Text | The URI for the JEL classification code. |

<a name="journal-of-economic-literature-(jel)-classification-codes_label"></a>
##### Label

**Description:** A human-readable form of the term.

**Required:** Yes

**Repeatable:** No

**Accepted Values:** Text

**Examples:**

```text
"Relation of Economics to Other Disciplines"
```

```text
"History of Economic Thought, Methodology, and Heterodox Approaches"
```

```text
"Economic History: Financial Markets and Institutions: U.S.; Canada: 1913-"
```

<a name="journal-of-economic-literature-(jel)-classification-codes_code"></a>
##### Code

**Description:** A machine-readable/-actionable form of the term.

**Required:** Yes

**Repeatable:** No

**Accepted Values:** Text

**Examples:**

```text
"A12"
```

```text
"B00"
```

```text
"N22"
```

<a name="journal-of-economic-literature-(jel)-classification-codes_uri"></a>
##### URI

**Description:** The URI for the JEL classification code.

**Required:** Yes

**Repeatable:** No

**Accepted Values:** Text

**Examples:**

```text
"/api/v1/vocab-terms/jelClassifications/terms/A12"
```

```text
"/api/v1/vocab-terms/jelClassifications/terms/B00"
```

```text
"/api/v1/vocab-terms/jelClassifications/terms/N22"
```

#### Complete Journal of Economic Literature (JEL) Classification Codes Examples (with Subfields):

```yaml
- "Label": "Relation of Economics to Other Disciplines"
  "Code": "A12"
  "URI": "/api/v1/vocab-terms/jelClassifications/terms/A12"

- "Label": "History of Economic Thought, Methodology, and Heterodox Approaches"
  "Code": "B00"
  "URI": "/api/v1/vocab-terms/jelClassifications/terms/B00"
```

```yaml
- "Label": "Economic History: Financial Markets and Institutions: U.S.; Canada: 1913-"
  "Code": "N22"
  "URI": "/api/v1/vocab-terms/jelClassifications/terms/N22"
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
| [Label](#medical-subject-headings-(mesh)-terms_label) | Yes | No | Text | A human-readable form of the subject term. |
| [Code](#medical-subject-headings-(mesh)-terms_code) | Yes | No | Text | A machine-readable/-actionable form of the subject term. |
| [URI](#medical-subject-headings-(mesh)-terms_uri) | Yes | No | Text | The URI for the subject term as maintained in MeSH. |

<a name="medical-subject-headings-(mesh)-terms_label"></a>
##### Label

**Description:** A human-readable form of the subject term.

**Required:** Yes

**Repeatable:** No

**Accepted Values:** Text

**Examples:**

```text
"Anxiety"
```

```text
"Diabetes Mellitus"
```

<a name="medical-subject-headings-(mesh)-terms_code"></a>
##### Code

**Description:** A machine-readable/-actionable form of the subject term.

**Required:** Yes

**Repeatable:** No

**Accepted Values:** Text

**Examples:**

```text
"D001007"
```

```text
"T011730"
```

<a name="medical-subject-headings-(mesh)-terms_uri"></a>
##### URI

**Description:** The URI for the subject term as maintained in MeSH.

**Required:** Yes

**Repeatable:** No

**Accepted Values:** Text

**Examples:**

```text
"http://id.nlm.nih.gov/mesh/D001007"
```

```text
"http://id.nlm.nih.gov/mesh/T011730"
```

#### Complete Medical Subject Headings (MeSH) Terms Examples (with Subfields):

```yaml
- "Label": "Anxiety"
  "Code": "D001007"
  "URI": "http://id.nlm.nih.gov/mesh/D001007"

- "Label": "Diabetes Mellitus"
  "Code": "T011730"
  "URI": "http://id.nlm.nih.gov/mesh/T011730"
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

**Usage Notes:** Dates are formatted in accordance with ISO 8601 (YYYY-MM-DD, YYYY-MM, or YYYY). No spaces are permitted in date expressions.

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

**Usage Notes:** Dates are formatted in accordance with ISO 8601 (YYYY-MM-DD, YYYY-MM, or YYYY). No spaces are permitted in date expressions.

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

**Usage Notes:** The textual description ('time frame') is used to add context to the Time Period when multiple time periods exist (e.g., to describe different waves, dataset names, or fiscal year designation) and/or when the date cannot be expressed exclusively through numbers, such as seasons or other units of time where the data producer did not clarify the exact dates they meant.

The textual description should not simply restate the time period in words. For example, if the start and end dates for Time Period are 2020-01, the associated Time Frame should not be 'January 2020'.

**Examples:**

```text
"Fall 2001"
```

```text
"Winter Semester 2019"
```

#### Complete Time Periods Examples (with Subfields):

```yaml
- "Start Date": "2018"
  "End Date": "2018"
  "Time Frame": "Summer and Fall 2018"

- "Start Date": "2020-10"
  "End Date": "2020-10"
```

```yaml
- "Start Date": "2003-01-01"
  "End Date": "2003-12-31"
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

<a id="geographic-coverage-areas"></a>
### Geographic Coverage Areas

**Description:** The geographic locations where the data refer or are related.

**Required:** Yes

**Repeatable:** Yes

**Accepted Values:** Multi-part element; see subfields

**Usage Notes:** In addition to the total geographic scope of the data, may include any additional levels of geographic coding provided in the variables.

Geographic locations are drawn from the GeoNames geographical database. Source: https://www.geonames.org/

When choosing Geographic Coverage Areas: 

* Select the country, state, city, county, region, or continent covered by the study.  
* Spell out place names completely instead of using acronyms. For example, enter "United States" instead of "USA."  
* Type at least four characters to see matches.  
* Choose only the narrowest level of geographic coverage. For example, if you select "Los Angeles, California, United States," do not also add "California, United States" and "United States."  
* For studies with participants from around the world or that are applicable everywhere, select "Earth."

#### Subfields:

| Property | Required? | Repeatable? | Accepted Values | Description |
|---|---|---|---|---|
| [City](#geographic-coverage-areas_city) | No | No | Text | A town, city, or similar populated place covered in the data collection |
| [County](#geographic-coverage-areas_county) | No | No | Text | A United States county or similar administrative area covered in the data collection |
| [State](#geographic-coverage-areas_state) | No | No | Text | A state, province, canton or similar political entity covered in the data collection |
| [Country](#geographic-coverage-areas_country) | No | No | Text | A country covered in the data collection |
| [Region](#geographic-coverage-areas_region) | No | No | Text | An area distinguished by one or more observable physical or cultural characteristics that is covered in the data collection. |
| [Continent](#geographic-coverage-areas_continent) | No | No | Text | A continent covered in the data collection |
| [Other Geographic Area](#geographic-coverage-areas_other_area) | No | No | Text | An area covered in the data collection that cannot be represented using the defined categories above or matched to an appropriate GeoNames record. |
| [URI](#geographic-coverage-areas_uri) | No | No | Text | A local unique identifier for the geographic coverage area. |
| [External URI](#geographic-coverage-areas_externalURI) | No | No | Text | The GeoNames unique identifier for the geographic coverage area. |

<a name="geographic-coverage-areas_city"></a>
##### City

**Description:** A town, city, or similar populated place covered in the data collection

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

**Description:** A United States county or similar administrative area covered in the data collection

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

**Description:** A state, province, canton or similar political entity covered in the data collection

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

**Description:** A country covered in the data collection

**Required:** No

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

<a name="geographic-coverage-areas_region"></a>
##### Region

**Description:** An area distinguished by one or more observable physical or cultural characteristics that is covered in the data collection.

**Required:** No

**Repeatable:** No

**Accepted Values:** Text

**Examples:**

```text
"Sub-Saharan Africa"
```

```text
"Eastern Europe"
```

```text
"Siberia"
```

<a name="geographic-coverage-areas_continent"></a>
##### Continent

**Description:** A continent covered in the data collection

**Required:** No

**Repeatable:** No

**Accepted Values:** Text

**Examples:**

```text
"Africa"
```

```text
"Asia"
```

```text
"South America"
```

<a name="geographic-coverage-areas_other_area"></a>
##### Other Geographic Area

**Description:** An area covered in the data collection that cannot be represented using the defined categories above or matched to an appropriate GeoNames record.

**Required:** No

**Repeatable:** No

**Accepted Values:** Text

**Usage Notes:** Use this for user-provided terms, loosely defined geographic concepts, GeoNames feature types not covered by city/county/state/country/region/continent, or historical geographic entities (e.g., Prussia) not represented in GeoNames.

**Examples:**

```text
"Global"
```

```text
"Eurasia"
```

```text
"13 U.S. states in 3 regions"
```

<a name="geographic-coverage-areas_uri"></a>
##### URI

**Description:** A local unique identifier for the geographic coverage area.

**Required:** No

**Repeatable:** No

**Accepted Values:** Text

**Examples:**

```text
"/api/v1/vocab-terms/geoNames/terms/6252001"
```

```text
"/api/v1/vocab-terms/geoNames/terms/6269554"
```

<a name="geographic-coverage-areas_externalURI"></a>
##### External URI

**Description:** The GeoNames unique identifier for the geographic coverage area.

**Required:** No

**Repeatable:** No

**Accepted Values:** Text

**Examples:**

```text
"https://sws.geonames.org/4990729/"
```

```text
"https://sws.geonames.org/6269554"
```

#### Complete Geographic Coverage Areas Examples (with Subfields):

```yaml
- "City": "Cleveland"
  "State": "Ohio"
  "Country": "United States"
  "Continent": "North America"
  "External URI": "https://sws.geonames.org/5150529"
  "URI": "/api/v1/vocab-terms/geoNames/terms/5150529"

- "County": "Washtenaw County"
  "State": "Michigan"
  "Country": "United States"
  "Continent": "North America"
  "External URI": "https://sws.geonames.org/5014120"
  "URI": "/api/v1/vocab-terms/geoNames/terms/5014120"

- "State": "Pennsylvania"
  "Country": "United States"
  "Continent": "North America"
  "External URI": "https://sws.geonames.org/5206379"
  "URI": "/api/v1/vocab-terms/geoNames/terms/5206379"
```

```yaml
- "Country": "Germany"
  "Continent": "Europe"
  "External URI": "https://sws.geonames.org/2921044"
  "URI": "/api/v1/vocab-terms/geoNames/terms/2921044"

- "Continent": "Africa"
  "External URI": "https://sws.geonames.org/6255146"
  "URI": "/api/v1/vocab-terms/geoNames/terms/6255146"
```

```yaml
- "Other Geographic Area": "Global"
  "External URI": "https://sws.geonames.org/6295630"
  "URI": "/api/v1/vocab-terms/geoNames/terms/6295630"
```

```yaml
- "Other Geographic Area": "13 U.S. states in 3 regions"
```


---

<a id="smallest-geographic-unit"></a>
### Smallest Geographic Unit

**Description:** The smallest geographic unit (e.g., state or census tract) used in the dataset.

**Required:** No

**Repeatable:** No

**Accepted Values:** Multi-part element; see subfields

**Usage Notes:** Smallest Geographic Unit is intended to represent specific, known geography – e.g., county, census district, Zip code, electoral district, etc. – that is represented by a variable. 

If the data do not include a geographic variable by which the data can be analyzed, this element is not indicated. If all the cases are from a single state, but the cases are not subdivided geographically within that state, then 'state' is not indicated. 

If there is a variable indicating which testing site a survey was taken at, but the locations of the testing sites were masked by the PI, this element is likely not indicated.


This field employs a local ICPSR controlled vocabulary; see below for terms and definitions:


| Term | Definition |
|------|------------|
| Basic Geographic Units | Basic geographic units for use with the Smallest Geographic Unit metadata property |
| Geocoded Location | A precise geographic point derived from an address, typically represented as coordinates or address strings. |
| Parcel | A discrete use of land ownership, often defined in property records or tax assessments. |
| Grid Cell | A unit of spatial data that divides an area into rectangular, square intervals (e.g., 1km x 1km grid), typically used in mapping or environmental studies. |
| Local Geographic Units | Local geographic units for use with the Smallest Geographic Unit metadata property |
| Postal Code/Zip Code | A geographic area defined by postal delivery routes or regions, used for organizing mail delivery. |
| Neighborhood/Community Area | An informally defined area within a city, usually based on local recognition rather than official administrative boundaries. |
| City/Municipality | A local government jurisdiction that covers urban areas, which can range from large cities to small towns and villages. |
| County/District/Parish | A geographic area that is part of a state or province (e.g., parishes in Louisiana, boroughs in Alaska). |
| Larger Geographic Units | Larger geographic units for use with the Smallest Geographic Unit metadata property |
| State/Province | A major administrative division within a country.  In the U.S., this includes the 50 states and the District of Columbia.  Other countries, like Canada and Australia, have provinces or states (e.g., Ontario in Canada, New South Wales in Australia). |
| Territory | A region under the jurisdiction of a national government, but not a fully self-governing state or province (e.g., Puerto Rico, Northwest Territories, Falkland Islands). |
| Country | A sovereign nation or territory that is recognized as an independent political entity, such as the United States, Canada, or France. |
| Census Units | Census units for use with the Smallest Geographic Unit metadata property |
| Census Block | The smallest geographic unit used in national censuses, often corresponding to a city block or small neighborhood. |
| Census Block Group | A collection of adjacent census blocks—typically all blocks within part of a census tract. |
| Census Tract | A small geographic unit used in national censuses, typically representing 2,500 to 8,000 people.  Census tracts are designed to provide detailed statistical data for neighborhoods or communities. |
| Census Division | A larger geographic area used for statistical reporting, grouping states or provinces within a country.  Census divisions are smaller than regions but larger than individual states or provinces. |
| Census Region | A broader grouping of census divisions used to organize and report data at a national level (e.g., Northeast, Midwest, South, West). |
| Public Use Microdata Area (PUMA) | A geographic area with a population of 100,000 or more, used for the release of detailed public-use microdata from the U.S. Census. |
| Core-Based Statistical Area (CBSA) | A term that includes both Metropolitan and Micropolitan Statistical Areas.  These areas are based on urban centers and their surrounding communities as defined by the U.S. Office of Management and Budget (OMB). |
| Metropolitan Statistical Area (MSA) | A Core-Based Statistical Area (CBSA) that includes an urban core with a population of 50,000 or more. |
| Micropolitan Statistical Area | A Core-Based Statistical Area (CBSA) that includes an urban core population of at least 10,000 but less than 50,000. |
| ZIP Code Tabulation Area (ZCTA) | A geographic area created by the U.S. Census Bureau to approximate the boundaries of ZIP Codes for demographic analysis. |
| Electoral, Legal, Cross-Jurisdictional, and Educational Districts | Geographic units that represent electoral, legal, cross-jurisdictional, and educational districts for use with the Smallest Geographic Unit metadata property |
| Voting District/Precinct | A geographic area used for organizing elections, often serving as the smallest electoral units where voters cast their ballots. |
| Congressional District | A geographic area used for electing representatives to federal or state legislative offices in the United States. |
| Federal Court District | A geographic area where a U.S. District Court has jurisdiction to hear and decide federal cases. |
| School District | The administrative boundary for local education systems, typically overseeing public schools from elementary through secondary levels. |
| Indigenous/Tribal Lands | An area legally recognized as an Indigenous or tribal nation, often with unique legal, cultural, or sovereignty status. |


#### Subfields:

| Property | Required? | Repeatable? | Accepted Values | Description |
|---|---|---|---|---|
| [Label](#smallest-geographic-unit_label) | No | No | Text | A human-readable form of the term. |
| [Code](#smallest-geographic-unit_code) | No | No | Text | A machine-readable/-actionable form of the term. |
| [URI](#smallest-geographic-unit_uri) | No | No | Text | The URI for the term. |

<a name="smallest-geographic-unit_label"></a>
##### Label

**Description:** A human-readable form of the term.

**Required:** No

**Repeatable:** No

**Accepted Values:** Text

**Examples:**

```text
"Basic Geographic Units"
```

```text
"Postal Code/Zip Code"
```

```text
"State/Province"
```

<a name="smallest-geographic-unit_code"></a>
##### Code

**Description:** A machine-readable/-actionable form of the term.

**Required:** No

**Repeatable:** No

**Accepted Values:** Text

**Examples:**

```text
"BasicUnits"
```

```text
"PostalCodeZipCode"
```

```text
"StateProvince"
```

<a name="smallest-geographic-unit_uri"></a>
##### URI

**Description:** The URI for the term.

**Required:** No

**Repeatable:** No

**Accepted Values:** Text

**Examples:**

```text
"/api/v1/vocab-terms/smallestGeographicUnits/terms/BasicUnits"
```

```text
"/api/v1/vocab-terms/smallestGeographicUnits/terms/PostalCodeZipCode"
```

```text
"/api/v1/vocab-terms/smallestGeographicUnits/terms/StateProvince"
```

#### Complete Smallest Geographic Unit Examples (with Subfields):

```yaml
"Label": "Basic Geographic Units"
"Code": "BasicUnits"
"URI": "/api/v1/vocab-terms/smallestGeographicUnits/terms/BasicUnits"
```

```yaml
"Label": "Postal Code/Zip Code"
"Code": "PostalCodeZipCode"
"URI": "/api/v1/vocab-terms/smallestGeographicUnits/terms/PostalCodeZipCode"
```

```yaml
"Label": "State/Province"
"Code": "StateProvince"
"URI": "/api/v1/vocab-terms/smallestGeographicUnits/terms/StateProvince"
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

<a id="time-methods"></a>
### Time Methods

**Description:** The methods used to collect data over time, like snapshots at one point (cross-sectional) or repeatedly (longitudinal) to study changes or trends.

**Required:** No

**Repeatable:** Yes

**Accepted Values:** Multi-part element; see subfields

**Usage Notes:** This controlled vocabulary was taken from the DDI Alliance. Source: DDI Alliance CV TimeMethod https://rdf-vocabulary.ddialliance.org/ddi-cv/TimeMethod/1.2.3/TimeMethod.html.

#### Subfields:

| Property | Required? | Repeatable? | Accepted Values | Description |
|---|---|---|---|---|
| [Label](#time-methods_label) | Yes | No | Text | A human-readable form of the term. |
| [Code](#time-methods_code) | Yes | No | Text | A machine-readable/-actionable form of the term. |
| [URI](#time-methods_uri) | Yes | No | Text | The URI for the term. |

<a name="time-methods_label"></a>
##### Label

**Description:** A human-readable form of the term.

**Required:** Yes

**Repeatable:** No

**Accepted Values:** Text

**Examples:**

```text
"Cross-section"
```

```text
"Longitudinal: Panel"
```

```text
"Time series"
```

<a name="time-methods_code"></a>
##### Code

**Description:** A machine-readable/-actionable form of the term.

**Required:** Yes

**Repeatable:** No

**Accepted Values:** Text

**Examples:**

```text
"CrossSection"
```

```text
"Longitudinal.Panel"
```

```text
"TimeSeries"
```

<a name="time-methods_uri"></a>
##### URI

**Description:** The URI for the term.

**Required:** Yes

**Repeatable:** No

**Accepted Values:** Text

**Examples:**

```text
"/api/v1/vocab-terms/timeMethods/terms/CrossSection"
```

```text
"/api/v1/vocab-terms/timeMethods/terms/Longitudinal.Panel"
```

```text
"/api/v1/vocab-terms/timeMethods/terms/TimeSeries"
```

#### Complete Time Methods Examples (with Subfields):

```yaml
- "Label": "Cross-section"
  "Code": "CrossSection"
  "URI": "/api/v1/vocab-terms/timeMethods/terms/CrossSection"

- "Label": "Longitudinal: Panel"
  "Code": "Longitudinal.Panel"
  "URI": "/api/v1/vocab-terms/timeMethods/terms/Longitudinal.Panel"
```

```yaml
- "Label": "Time series"
  "Code": "TimeSeries"
  "URI": "/api/v1/vocab-terms/timeMethods/terms/TimeSeries"
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
| [URI](#units-of-analysis_uri) | Yes | No | Text | The URI for the term. |

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
##### URI

**Description:** The URI for the term.

**Required:** Yes

**Repeatable:** No

**Accepted Values:** Text

**Examples:**

```text
"/api/v1/vocab-terms/analysisUnits/OrganizationOrInstitution"
```

```text
"/api/v1/vocab-terms/analysisUnits/Individual"
```

```text
"/api/v1/vocab-terms/analysisUnits/Household"
```

#### Complete Units of Analysis Examples (with Subfields):

```yaml
- "Label": "Organization/Institution"
  "Code": "OrganizationOrInstitution"
  "URI": "/api/v1/vocab-terms/analysisUnits/OrganizationOrInstitution"

- "Label": "Individual"
  "Code": "Individual"
  "URI": "/api/v1/vocab-terms/analysisUnits/Individual"
```

```yaml
- "Label": "Household"
  "Code": "Household"
  "URI": "/api/v1/vocab-terms/analysisUnits/Household"
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
  "Uri": "/api/v1/vocab-terms/samplingProcedures/terms/Probability.SystematicRandom"

- "Label": "Theoretical Sampling"
  "Code": "TheoreticalSampling"
  "Uri": "/api/v1/vocab-terms/samplingProcedures/terms/TheoreticalSampling"
```

```yaml
- "Label": "Total universe/Complete enumeration"
  "Code": "TotalUniverseCompleteEnumeration"
  "Uri": "/api/v1/vocab-terms/samplingProcedures/terms/TotalUniverseCompleteEnumeration"
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

<a id="weights"></a>
### Weights

**Description:** The weight variables and the criteria for using them in data analysis, or other information about how the data are weighted if no weight variables are present.

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
"Of the 1,843 Midlife in the United States (MIDUS) respondents that researchers attempted to contact, 1,483 agreed to participate (8 percent refused participation and 11 percent either moved or were difficult to contact), yielding a response rate of approximately 81 percent."
```


---

<a id="data-source-types"></a>
### Data Source Types

**Description:** The source(s) of the data as collected by the Principal Investigators.

**Required:** No

**Repeatable:** Yes

**Accepted Values:** Multi-part element; see subfields

**Usage Notes:** This controlled vocabulary was taken from the DDI Alliance. Source: DDI Alliance CV DataSourceType https://rdf-vocabulary.ddialliance.org/ddi-cv/DataSourceType/1.0.2/DataSourceType.html. People, things, and other data can all be Data Source Types.

#### Subfields:

| Property | Required? | Repeatable? | Accepted Values | Description |
|---|---|---|---|---|
| [Label](#data-source-types_label) | Yes | No | Text | A human-readable form of the term. |
| [Code](#data-source-types_code) | Yes | No | Text | A machine-readable/-actionable form of the term. |
| [URI](#data-source-types_uri) | Yes | No | Text | The URI for the term. |

<a name="data-source-types_label"></a>
##### Label

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
"Research data: Published"
```

<a name="data-source-types_code"></a>
##### Code

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
"ResearchData.Published"
```

<a name="data-source-types_uri"></a>
##### URI

**Description:** The URI for the term.

**Required:** Yes

**Repeatable:** No

**Accepted Values:** Text

**Examples:**

```text
"/api/v1/vocab-terms/dataSourceTypes/terms/RegistersRecordsAccounts.MedicalClinical"
```

```text
"/api/v1/vocab-terms/dataSourceTypes/terms/EventsInteractions"
```

```text
"/api/v1/vocab-terms/dataSourceTypes/terms/ResearchData.Published"
```

#### Complete Data Source Types Examples (with Subfields):

```yaml
- "Label": "Registers/Records/Accounts: Medical/Clinical"
  "Code": "RegistersRecordsAccounts.MedicalClinical"
  "URI": "/api/v1/vocab-terms/dataSourceTypes/terms/RegistersRecordsAccounts.MedicalClinical"

- "Label": "Events/Interactions"
  "Code": "EventsInteractions"
  "URI": "/api/v1/vocab-terms/dataSourceTypes/terms/EventsInteractions"
```

```yaml
- "Label": "Research data: Published"
  "Code": "ResearchData.Published"
  "URI": "/api/v1/vocab-terms/dataSourceTypes/terms/ResearchData.Published"
```


---

<a id="external-data-sources"></a>
### External Data Sources

**Description:** The source of the data, when that source is external to the data collection and can be independently cited.

**Required:** No

**Repeatable:** Yes

**Accepted Values:** Text

**Usage Notes:** External data sources can include websites, datasets, books, journal articles, and other sources. Each source includes at minimum the title, author, publication year, journal (if applicable), and DOI or URL for online sources. Any citation format is accepted.

**Examples:**

```text
"'Voting Scores.' Congressional Quarterly Almanac 33 (1977), 487-498"
```

```text
"Multi-Resolution Land Characteristics Consortium. "National Land Cover Database (CONUS), All Years," 2016. https://www.mrlc.gov/data/nlcd-land-cover-conus-all-years"
```

```text
"Data file 1: United States Census Bureau (2010). TIGER/Line shapefiles, 2010 census tracts (2010 version) [Data set]. https://www2.census.gov/geo/tiger/TIGER2010/TRACT/2010/tl_2010_01_tract10.zip"
```


---

<a id="collection-modes"></a>
### Collection Modes

**Description:** The method(s) or procedure(s) used to collect the data, such as an interview or experiment.

**Required:** No

**Repeatable:** Yes

**Accepted Values:** Multi-part element; see subfields

**Usage Notes:** This controlled vocabulary was taken from the DDI Alliance. Source: DDI Alliance CV ModeOfCollection https://rdf-vocabulary.ddialliance.org/ddi-cv/ModeOfCollection/4.0.3/ModeOfCollection.html.

#### Subfields:

| Property | Required? | Repeatable? | Accepted Values | Description |
|---|---|---|---|---|
| [Label](#collection-modes_label) | Yes | No | Text | A human-readable form of the term. |
| [Code](#collection-modes_code) | Yes | No | Text | A machine-readable/-actionable form of the term. |
| [URI](#collection-modes_uri) | Yes | No | Text | The URI for the term. |

<a name="collection-modes_label"></a>
##### Label

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
##### Code

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
##### URI

**Description:** The URI for the term.

**Required:** Yes

**Repeatable:** No

**Accepted Values:** Text

**Examples:**

```text
"/api/v1/vocab-terms/collectionModes/terms/Interview.FaceToFace.CAPIorCAMI"
```

#### Complete Collection Modes Examples (with Subfields):

```yaml
- "Label": "Face-to-face interview: Computer-assisted (CAPI/CAMI)"
  "Code": "Interview.FaceToFace.CAPIorCAMI"
  "URI": "/api/v1/vocab-terms/collectionModes/terms/Interview.FaceToFace.CAPIorCAMI"
```

```yaml
- "Label": "Measurements and tests"
  "Code": "MeasurementsAndTests"
  "URI": "/api/v1/vocab-terms/collectionModes/terms/MeasurementsAndTests"

- "Label": "Computer-based observation"
  "Code": "Observation.ComputerBased"
  "URI": "/api/v1/vocab-terms/collectionModes/terms/Observation.ComputerBased"
```


---

<a id="collection-dates"></a>
### Collection Dates

**Description:** The date(s) data collection took place.

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

**Usage Notes:** Dates are formatted in accordance with ISO 8601 (YYYY-MM-DD, YYYY-MM, or YYYY). No spaces are permitted in date expressions.

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

**Usage Notes:** Dates are formatted in accordance with ISO 8601 (YYYY-MM-DD, YYYY-MM, or YYYY). No spaces are permitted in date expressions.

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

**Usage Notes:** The textual description ('time frame') is used to add context to the Collection Date when multiple time periods exist (e.g., to describe different study waves, dataset names, or fiscal year designation) and/or when the date cannot be expressed exclusively through numbers, such as seasons or other units of time where the data producer did not clarify the exact dates they meant.

The textual description should not simply restate the time period in words. For example, if the Collection Date is 2020-01, the Time Frame should not be 'January 2020'.

**Examples:**

```text
"Fall 2001"
```

```text
"Student data"
```

#### Complete Collection Dates Examples (with Subfields):

```yaml
- "Start Date": "2018"
  "End Date": "2018"
  "Time Frame": "Wave 1"

- "Start Date": "2020-10"
  "End Date": "2020-10"
  "Time Frame": "Wave 2"
```

```yaml
- "Start Date": "2003-01-01"
  "End Date": "2003-12-31"
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

<a id="scales"></a>
### Scales

**Description:** Any commonly known scales, measures, or inventories used in the data collection.

**Required:** No

**Repeatable:** No

**Accepted Values:** Text

**Usage Notes:** Include common scales that can be readily identified from the data, documentation, or other related materials. Examples of common scales include the Minnesota Multiphasic Personality Inventory (MMPI) and the Consumer Price Index (CPI). ICPSR curators are not expected to infer or research scales that are not explicitly indicated. The scales can be cited either as a list or described in full sentences and include DOIs or URLs whenever possible. If the questionnaire used has a finite list of responses (e.g., 'Always, Sometimes, Rarely, Never' or 'Strongly Agree, Agree, Disagree, Strongly Disagree'), it is acceptable for this element to note 'A Likert-type scale was used,' or 'Several Likert-type scales were used.' However, it is not required to note Likert-type scales in situations where only such scales were used, given their ubiquity.

**Examples:**

```text
"The baseline data collection included one scale - the CES-D index for maternal depression [Cole, J. C., Rabin, A. S., Smith, T. L., and Kaufman, A. S. (2004). Development and validation of a Rasch-derived CES-D short form. Psychological assessment, 16(4), 360. https://doi.org/10.1037/1040-3590.16.4.360]. All scales used for outcomes at ages 1 through 3 are listed in Appendix Tables 1 and 2 in the User Guide. Please refer to the User Guide and P.I. Codebook, available under the 'Data and Documentation' tab, for details."
```

```text
"Squires, J., Bricker, D. D., and Twombly, E. (2009). Ages and stages questionnaires. Baltimore, MD: Paul H. Brookes."
"Briggs-Gowan, M. J., Carter, A. S., Irwin, J. R., Wachtel, K., and Cicchetti, D. V. (2004). The Brief Infant-Toddler Social and Emotional Assessment: screening for social-emotional problems and delays in competence. Journal of pediatric psychology, 29(2), 143-155. https://doi.org/10.1093/jpepsy/jsh017"
"Yu, L., Buysse, D. J., Germain, A., Moul, D. E., Stover, A., Dodds, N. E., ... and Pilkonis, P. A. (2012). Development of short forms from the PROMIS sleep disturbance and sleep-related impairment item banks. Behavioral sleep medicine, 10(1), 6-24. https://doi.org/10.1080/15402002.2012.636266"
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
"https://doi.org/10.48321/D1EA6EF78D"
```

```text
"https://rdm.mcmaster.ca/dmps/promoting-healthy-families-data-management-plan"
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
"https://doi.org/10.17605/OSF.IO/67DUT"
```

```text
"https://doi.org/10.1257/rct.15789-1.0"
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

#### Complete Software Applications Examples (with Subfields):

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
| [Label](#general-data-formats_label) | Yes | No | Text | A human-readable form of the term. |
| [Code](#general-data-formats_code) | Yes | No | Text | A machine-readable/-actionable form of the term. |
| [URI](#general-data-formats_uri) | Yes | No | Text | The URI for the term. |

<a name="general-data-formats_label"></a>
##### Label

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
##### Code

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
##### URI

**Description:** The URI for the term.

**Required:** Yes

**Repeatable:** No

**Accepted Values:** Text

#### Complete General Data Formats Examples (with Subfields):

```yaml
- "Label": "Text"
  "Code": "Text"
  "URI": "/api/v1/vocab-terms/generalDataFormats/terms/Text"

- "Label": "Still image"
  "Code": "StillImage"
  "URI": "/api/v1/vocab-terms/generalDataFormats/terms/StillImage"
```

```yaml
- "Label": "Numeric"
  "Code": "Numeric"
  "URI": "/api/v1/vocab-terms/generalDataFormats/terms/Numeric"
```


---

<a id="notes"></a>
### Notes

**Description:** Important details about the data collection (like unique authoring, discrepancies, or processing information) that can't be recorded in other metadata elements.

**Required:** No

**Repeatable:** Yes

**Accepted Values:** Text

**Usage Notes:** Collection Notes should include any information that does not fit anywhere else in the metadata, such as: information about unique aspects of the way the data was processed, discrepancies between the metadata and documentation files, information about the research team, or series-specific notes.

**Examples:**

```text
"Information on the Index of Consumer Sentiment, the Index of Current Economic Conditions, and the Index of Consumer Expectations and how they were created can be found in the P.I. Codebook"
"Dataset 1 should be attributed to Jane Doe while datasets 2-6 should be attributed to John Doe"
```

```text
"Additional information on the Survey of Consumers can be found by visiting the Survey of Consumers Website"
```


---

<a id="manuscript-number"></a>
### Manuscript Number

**Description:** A unique identifier that associates the data collection with a manuscript submitted to a journal.

**Required:** No

**Repeatable:** No

**Accepted Values:** Text

**Examples:**


---

<a id="ada-accessibility"></a>
### ADA Accessibility

**Description:** Indicates whether the data collection is ADA accessible, conforming to WCAG 2.1 AA standards, or qualifies for the ADA archival exception.

**Required:** No

**Repeatable:** No

**Accepted Values:** Multi-part element; see subfields

**Usage Notes:** This field employs a local ICPSR controlled vocabulary; see below for terms and definitions:


| Term | Definition |
|------|------------|
| ADA Accessible | The item is ADA accessible, conforming to WCAG 2.1 AA standards. |
| ADA Archival | The item is not ADA accessible, but qualifies for the ADA archival exception. |


#### Subfields:

| Property | Required? | Repeatable? | Accepted Values | Description |
|---|---|---|---|---|
| [Label](#ada-accessibility_label) | Yes | No | Text | A human-readable form of the term. |
| [Code](#ada-accessibility_code) | Yes | No | Text | A machine-readable/-actionable form of the term. |
| [URI](#ada-accessibility_uri) | Yes | No | Text | The URI for the term. |

<a name="ada-accessibility_label"></a>
##### Label

**Description:** A human-readable form of the term.

**Required:** Yes

**Repeatable:** No

**Accepted Values:** Text

**Examples:**

```text
"ADA Accessible"
```

```text
"ADA Archival"
```

<a name="ada-accessibility_code"></a>
##### Code

**Description:** A machine-readable/-actionable form of the term.

**Required:** Yes

**Repeatable:** No

**Accepted Values:** Text

**Examples:**

```text
"ada.accessible"
```

```text
"ada.archival"
```

<a name="ada-accessibility_uri"></a>
##### URI

**Description:** The URI for the term.

**Required:** Yes

**Repeatable:** No

**Accepted Values:** Text

**Examples:**

```text
"/api/v1/vocab-terms/adaAccessibility/terms/ada.accessible"
```

```text
"/api/v1/vocab-terms/adaAccessibility/terms/ada.archival"
```

#### Complete ADA Accessibility Examples (with Subfields):

```yaml
"Label": "ADA Accessible"
"Code": "ada.accessible"
"URI": "/api/v1/vocab-terms/adaAccessibility/terms/ada.accessible"
```

```yaml
"Label": "ADA Archival"
"Code": "ada.archival"
"URI": "/api/v1/vocab-terms/adaAccessibility/terms/ada.archival"
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
| [Label](#license_label) | Yes | No | Text | A human-readable form of the term. |
| [Code](#license_code) | Yes | No | Text | A machine-readable/-actionable form of the term. |
| [URI](#license_uri) | Yes | No | Text | The URI for the term. |

<a name="license_label"></a>
##### Label

**Description:** A human-readable form of the term.

**Required:** Yes

**Repeatable:** No

**Accepted Values:** Text

**Examples:**

```text
"Creative Commons Attribution 4.0 International"
```

```text
"Apache License 1.0"
```

<a name="license_code"></a>
##### Code

**Description:** A machine-readable/-actionable form of the term.

**Required:** Yes

**Repeatable:** No

**Accepted Values:** Text

**Examples:**

```text
"CC-BY-NC-4.0"
```

```text
"Apache-1.0"
```

<a name="license_uri"></a>
##### URI

**Description:** The URI for the term.

**Required:** Yes

**Repeatable:** No

**Accepted Values:** Text

**Examples:**

```text
"/api/v1/vocab-terms/licenses/terms/CC-BY-4.0"
```

```text
"/api/v1/vocab-terms/licenses/terms/Apache-1.0"
```

#### Complete License Examples (with Subfields):

```yaml
"Label": "Creative Commons Attribution 4.0 International"
"Code": "CC-BY-NC-4.0"
"URI": "/api/v1/vocab-terms/licenses/terms/CC-BY-4.0"
```

```yaml
"Label": "Apache License 1.0"
"Code": "Apache-1.0"
"URI": "/api/v1/vocab-terms/licenses/terms/Apache-1.0"
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

**Usage Notes:** Every ICPSR data collection is assigned version 1.0 when it is first published. When the data collection is updated, a new version number is assigned. For substantive changes to the data collection, including changes to data files, title, or principal investigators, a new major version is created, the version number increases by 1 (for example, from 1.0 to 2.0), and a new version-specific digital object identifier (DOI) is created. For all other changes, a new minor version is created, the version number increases by 0.1 (for example, from 2.0 to 2.1), and the DOI does not change.

**Examples:**

```text
"V1"
```

```text
"V2.1"
```

```text
"V3.2"
```

<a name="version-history_version_date"></a>
##### Version Date

**Description:** The date on which a given version of a data collection was released.

**Required:** No

**Repeatable:** No

**Accepted Values:** Text

**Usage Notes:** ICPSR automatically generates this date for data collection additions and updates.

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

#### Complete Version History Examples (with Subfields):

```yaml
- "Version Number": "V2.1"
  "Version Date": "2025-10-03"
  "Version Note": "Updated study summary."

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

<a id="distributors"></a>
### Distributors

**Description:** The organization(s) responsible for distributing the data collection.

**Required:** No

**Repeatable:** Yes

**Accepted Values:** Multi-part element; see subfields

#### Subfields:

| Property | Required? | Repeatable? | Accepted Values | Description |
|---|---|---|---|---|
| [Organization](#distributors_organization) | Yes | No | Multi-part element; see subfields | Name and other details about the organization that distributes the data collection. |
| [Order](#distributors_order) | Yes | No | Number | The order of importance for the distributors of the data collection. |

<a name="distributors_organization"></a>
##### Organization

**Description:** Name and other details about the organization that distributes the data collection.

**Required:** Yes

**Repeatable:** No

**Accepted Values:** Multi-part element; for more information, see the [Organization](#organization) field

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

#### Complete Distributors Examples (with Subfields):

```yaml
- "Organization":
    "Name": "Inter-university Consortium for Political and Social Research"
    "Ror": "https://ror.org/02q7mkh03"
  "Order": 0

- "Organization":
    "Name": "GESIS - Leibniz-Institute for the Social Sciences"
    "Ror": "https://ror.org/018afyw53"
  "Order": 1
```

```yaml
- "Organization":
    "Name": "Roper Center for Public Opinion Research"
  "Order": 0
```


---

<a id="study-number"></a>
### Study Number

**Description:** A unique, numerical value used by ICPSR to identify and track data collections.

**Required:** Yes

**Repeatable:** No

**Accepted Values:** Number

**Usage Notes:** The study number is automatically generated by ICPSR and is unique. Current study numbers are five digits, though four digit numbers were once standard and are still acceptable.

**Examples:**

```text
"2760"
```

```text
"3025"
```

```text
"38672"
```


---

<a id="digital-object-identifier-(doi)"></a>
### Digital Object Identifier (DOI)

**Description:** The registered persistent digital object identifier (DOI) associated with the data collection.

**Required:** Yes

**Repeatable:** No

**Accepted Values:** Text

**Usage Notes:** The DOI (digital object identifier) is a persistent identifier provided by DataCite, a DOI registration agency. The DOI name is divided into three parts, separated by slashes ('/'): 'https://doi.org' is the HTTP URL link; followed by '10.3886', a globally unique number that identifies ICPSR as the registrant within the DOI namespace; followed by 'ICPSR', the ICPSR study number, and then the version number. The study number is automatically generated by ICPSR and is unique. Current study numbers are five digits, though four digit numbers were once standard and are still acceptable. Studies with fewer than five digits will have zeroes prepended in the DOI (e.g., '10.3886/ICPSR02760).

**Examples:**

```text
"https://doi.org/10.3886/ICPSR03025.v2"
```

```text
"https://doi.org/10.3886/ICPSR06425.v1"
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
"Sickmund, Melissa, Hockenberry, Sarah, and Puzzanchera, Charles M. National Juvenile Court Data Archive, United States, 1985-2019. Inter-university Consortium for Political and Social Research [distributor], 2022-07-28. https://doi.org/10.3886/ICPSR38418.v1"
```

```text
"Institute of Museum and Library Services. Public Libraries in the United States Survey, 2016-2018. Inter-university Consortium for Political and Social Research [distributor], 2021-10-07. https://doi.org/10.3886/ICPSR37992.v1"
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
| [Affiliation(s)](#person_affiliations) | No | Yes | Multi-part element; see subfields | The person's affiliated organization(s). |
| [Email Address](#person_email) | No | No | Text | The person's email address. |

<a name="person_name"></a>
##### Personal Name

**Description:** The person's name.

**Required:** Yes

**Repeatable:** No

**Accepted Values:** Multi-part element; see subfields

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

#### Complete Personal Name Examples (with Subfields):

```yaml
"Given Name (First Name)": "Susan B."
"Family Name (Last Name)": "Anthony"
```

```yaml
"Given Name (First Name)": "John"
"Family Name (Last Name)": "Doe IV"
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

**Accepted Values:** Multi-part element; for more information, see the [Organization](#organization) field

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

#### Complete Person Examples (with Subfields):

```yaml
"Personal Name":
  "Given Name (First Name)": "Jane Q."
  "Family Name (Last Name)": "Doe II"
"ORCID Identifier": "https://orcid.org/0000-0001-6666-5717"
"Affiliation(s)":
- "Name": "Urban Institute"
  "Ror": "https://ror.org/017pz3h73"
- "Name": "Example University"
"Email Address": "jane.doe@example.com"
```

```yaml
"Personal Name":
  "Given Name (First Name)": "Joe"
  "Family Name (Last Name)": "Smith"
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
"Federal Reserve Bank of St. Louis"
```

```text
"University of Michigan"
```

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

#### Complete Organization Examples (with Subfields):

```yaml
"Organization Name": "Urban Institute"
"ROR Identifier": "https://ror.org/017pz3h73"
"Email Address": "info@urban.institute"
```


---

## ICPSR Metadata Schema Version History

| Date | Version | Note |
|------|---------|------|
| April 1, 2026 | v1 | Initial release and publication of the ICPSR Metadata Schema. |
