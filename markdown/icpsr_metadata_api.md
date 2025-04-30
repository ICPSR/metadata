# ICPSR Metadata Export API

ICPSR has developed a new application programming interface (API) to help researchers and data users:

  - **Search** data collections by specific metadata fields such as study identifier, subject terms, geographic coverage area, original release date -- and even run more advanced queries.
  - **Export** metadata about those collections in widely used formats such as DCAT-US, MARCXML, and Dublin Core, making it easier to share and integrate with other systems.

## Getting Started

If you're interested in using the API, please read the [ICPSR Object-Export API User Guide](https://docs.google.com/document/d/1fkr7SBnpl9hX_xClajnpNxwC67JCEUvPhD_VQjKJ_SM/edit?usp=sharing). 

This guide offers step-by-step instructions, including how to:

  - Get a temporary University of Michigan account (if you're not already affiliated with U-M).
  - Request API credentials.
  - Build and submit queries to search metadata.
  - Download and understand metadata records.

If you have questions or feedback about the API, please contact ICPSR-help [at] umich.edu.

## API Metadata Mappings

Metadata records produced by the ICPSR Object Export API are available in the following formats (with more to be added in the future): 

  - [DCAT-US](https://resources.data.gov/resources/dcat-us/): A U.S. government extension of the Data Catalog Vocabulary (DCAT), designed to make federal data easier to find and use. It provides a standardized way to describe datasets, data services, and distributions using RDF-based metadata, ensuring consistency across data catalogs like data.gov. DCAT-US aligns with international standards while meeting U.S. government requirements for data publishing. 

    > _Note: ICPSR's DCAT-US metadata exports conform to [this local extension of the DCAT-US standard](assets/dcat-us.json)._

  - [MARCXML](https://www.loc.gov/standards/marcxml/): An XML version of the MARC (Machine-Readable Cataloging) standard used by libraries to organize and share bibliographic data. This format helps libraries and archives exchange and integrate catalog data with modern systems and digital repositories.

  - [Dublin Core](https://www.dublincore.org/specifications/dublin-core/dcmi-terms/): A flexible and simple schema for describing digital and physical resources.  It's widely used in libraries, data repositories, and web-based applications to imrpove the discoverability and sharing of metadata. 

For more details on how ICPSR metadata map to these standards, check out this [Metadata API Mappings](https://docs.google.com/spreadsheets/d/1Avw212FfzxRjsUFvlJOLtsJclKeL8VJc0pbhLQevXg8/edit?usp=sharing) spreadsheet. 

## Element-Specific Mapping Notes  

This section explains how ICPSR's metadata elements are mapped to various export formats in the API, including non-standard mappings.

### Geographic Coverage Area

DCAT-US currently only permits a single value for the [spatial](https://resources.data.gov/resources/dcat-us/#spatial) metadata element. If a study has multiple Geographic Coverage Area entries, ICPSR will use the term "Multiple" in the 'spatial' property and list all geographic areas in an array under the 'spatialExt' property.  This is an ICPSR-specific extension to the DCAT-US schema.

### Time Period: Dates

*Dublin Core and MARCXML Date Expressions:* While ICPSR's [Time Period](https://icpsr.github.io/metadata/icpsr_study_schema/#18-time-period) element can have multiple date values, not all metadata standards allow this. To align better with Dublin Core and MARCXML, ICPSR combines multiple time periods into a single date range representing the earliest and latest dates to which the data refer.

*DCAT-US Date Expressions:* DCAT-US currently supports only one date for the [temporal](https://resources.data.gov/resources/dcat-us/#temporal) element. If a study has multiple Time Period entries, ICPSR will combine them into a single date range (showing the earliest and latest dates to which the data refer). These individual time periods will be added to an array under the 'temporalExt' property, which is an ICPSR-specific extension to the DCAT-US schema.

### Restrictions

ICPSR tracks _data availability_ (i.e., the availability of data for members-only vs. the general public) and _restriction type_ (i.e., restricted use vs. public use) in systems-level metadata, not at the study level. These details are combined with Restriction statements in the relevant metadata elements for different export formats, using the following conventions: 

  - If ICPSR membership is required, the property value will start with "Available to ICPSR member institutions."
    
  - If there's no membership requirement, it will start with "Available to the general public."

  - If there are additional use restrictions, the content of the Restrictions metadata field will be appended, along with a hyperlink to the study's homepage for more information. 

#### Example Conditions and Values

| Conditions | Example Values |
|----------- | -------------- |
| No membership requirement and no use restriction | "Available to the general public." |
| Membership requirement and no use restriction | "Available to ICPSR member institutions." |
| No membership requirement with a use restriction | "Available to the general public. Access to these data is restricted. Users interested in obtaining these data must complete a Restricted Data Use Agreement, specify the reason for the request, and obtain IRB approval or notice of exemption for their research. Visit [https://doi.org/10.3886/ICPSR37328.v1](https://doi.org/10.3886/ICPSR37328.v1) to apply for access to restricted data." |
| Membership requirement with a use restriction | "Available to ICPSR member institutions. This data collection may not be used for any purpose other than statistical reporting and analysis. Use of these data to learn the identity of any person or establishment is prohibited. To protect respondent privacy, all data files in this collection are restricted from general dissemination. To obtain these restricted files, researchers must agree to the terms and conditions of a Restricted Data Use Agreement. Visit [https://doi.org/10.3886/ICPSR37229.v1](https://doi.org/10.3886/ICPSR37229.v1) to apply for access to restricted data."</restrctn>

### Title

*MARCXML Expression:* According to [MARC guidelines for Field 245](https://www.loc.gov/marc/bibliographic/bd245.html), "subfield $a includes all the information up to and including the first mark of ISBD punctuation (e.g., an equal sign (=), a colon (:), a semicolon (;), or a slash (/)) or the medium designator (e.g., [microform])" and that "subfield $b contains all the data following the first mark of ISBD punctuation." Given the variation in how colons have been used in ICPSR's study titles over the past 60+ years, all title information will be placed in subfield $a. 