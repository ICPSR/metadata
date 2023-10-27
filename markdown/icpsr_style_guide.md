# ICPSR Metadata Style Guide

Last updated: October 27, 2023

These guidelines outline current ICPSR style, grammar, and general usage conventions for writing and editing metadata records.  

## Completeness

Provide complete and self-explanatory information for as many metadata elements as possible. Complete metadata significantly improves data discoverability. While we rely on depositors to supply as much metadata as possible upon deposit, metadata can be augmented and improved by ICPSR curators with the help of the data and documentation.  

## URLs

Full Uniform Resource Locators (URLs) should not be spelled out in the metadata record when referring to an online resource; instead, hyperlink the descriptive text, as this is friendlier to screen readers and web scrapers. For example, use "more information is available at the [ICPSR website](https://www.icpsr.umich.edu/)" rather than "more information is available at the ICPSR website: https://www.icpsr.umich.edu/".  

*Note:* formal citations (e.g., in Data Source or, with extreme rarity, Collection Notes elements) are an important exception to this rule; the URL (preferably a persistent identifier, like a Digital Object Identifier) should always be included for the cited resource.  

## Referencing ICPSR Data Collections

When referencing ICPSR data collections within metadata records, use the ICPSR identifier preceded by "ICPSR," hyperlinked using the study Digital Object Identifier (DOI). For example, "This collection continues the work of [ICPSR 3577](https://doi.org/10.3886/ICPSR03577)."  

Unless referencing a specific version of an ICPSR data collection, use the unversioned DOI (e.g., https://doi.org/10.3886/ICPSR06425 rather than https://doi.org/10.3886/ICPSR06425.v1) since the unversioned DOI resolves to the latest version of an archived ICPSR data collection.  

## Authority Control

The [ICPSR Personal Name Authority List](https://www.icpsr.umich.edu/web/ICPSR/thesaurus/10002) and the [ICPSR Organization Names Authority List](https://www.icpsr.umich.edu/web/ICPSR/thesaurus/10004) are the primary authority control sources for names in ICPSR metadata records.  

If names are not present in ICPSR lists, the [Virtual International Authority File](https://viaf.org/) (VIAF) serves as a secondary resource. VIAF is a name authority service that links multiple national authority files (i.e., catalogs of authoritative names such as the [Library of Congress Name Authority File](https://id.loc.gov/authorities/names.html)) into a single international resource. Once the record for an entity is found in VIAF, click on the link next to the American flag to access the Library of Congress entry and use the name in the 100 field (for personal names) or 110 field (for organizational names) of the record. If there are only foreign catalog entries, use of those are acceptable.  

When entering the name of a person or organization, the following hierarchy of authority control sources should be used to make sure the name conforms to best practices within ICPSR and the broader academic community:  

  1. If the person or organization has published/distributed/sponsored data for ICPSR in the past, use the name as it has been displayed previously within the ICPSR catalog.  
  2. If the person or organization is in the [ICPSR Personal Name Authority List](https://www.icpsr.umich.edu/web/ICPSR/thesaurus/10002) or the [ICPSR Organization Names Authority List](https://www.icpsr.umich.edu/web/ICPSR/thesaurus/10004), conform to the listed name form.
  3. If the person or organization is not available in an ICPSR authority list, consult [VIAF](https://viaf.org).  
  4. If the person or organization does not have a VIAF record, consult another authoritative source, such as an organization's website, Google Scholar, or a personal C.V. published on an institutional website.  

## Grammar

### Commas

  - If the text of a field contains a list of three or more items, separate the last two items with a comma followed by the word "and". This is called a serial (or Oxford) comma, and it is used in a series or list.  

    - Example:  "… Demographic information includes race, sex, education, income, and political affiliation."  

  - Use a comma to offset state names when they follow a city name.  

    - Example:  "…in Tallahassee, Florida, the survey was…"  

  - Use a comma to offset the year when following a date.  

    - Example:  "…on December 20, 1996, follow-up surveys were…"

  - Do *not* use a comma before a personal name extension such as "Sr" (senior), "Jr" (junior), "II" (the second), or "III" (the third).  

    - Example:  "Lawrence F. Travis III"

### Spacing

  - Use a single space following periods, colons, and question marks.

  - When a personal name includes two initials do not add a space between them.  

    - Examples:  "Smith, John L.S.", "R.A. Silverman"

### Definite and Indefinite Articles

  - Do not use articles such as "The", "An", "A", to begin a title of a data collection.

  - Do not use "The" to begin an organization name listed in the Principal Investigator, Distributor, or Funding Source Agency elements.

### Capitalization

  - Racial and ethnic designations are always capitalized.  

    - Examples:  "Blacks", "Whites", "Hispanic", "Asian"

  - Use lower-case for the following words:  

    - congressional
    - election day
    - inauguration day 
    - metropolitan areas
    - metropolitan statistical areas

  - Use lower-case for the following words *except* when associated with an 
individual’s name:

    - "president" vs. "President Bill Clinton"
    - "vice president" vs. "Vice President Al Gore"
    - "first lady" vs. "First Lady Hillary Clinton"

  - Use all upper-case for the following:

    - RAND (without the word 'corporation')
    - acronyms (see [Abbreviations and Acronyms](#-abbreviations-and-acronyms))

### Abbreviations and Acronyms  

  - Use "Washington, DC" (without periods in DC)

  - Acronyms can be used only after first presenting the full spelling followed by the acronym in parentheses. For example: "The Treatment Episode Data Set (TEDS) is a continuation of the former Client Data System (CDS) that was originally developed by the Alcohol, Drug Abuse and Mental Health Services Administration. …The TEDS data collection effort began in 1989…"

### Numbers  

  - Spell out numbers one through ten and use numeric notation for numbers higher than ten.

  - Use numeric notation with "percent" (e.g., 68 percent, 5 percent).

  - If a number starts a sentence, spell it out or re-write the sentence.

  - If there is a mix of higher and lower numbers in the same sentence, use numeric notation for all of the numbers. Example: "The study surveyed 9-14 year-olds".

### Singular and Plural Nouns

  - The word "data" is always plural (e.g. "data are included", "data were processed").

  - For the plural form of "index", use "indices".

  - For the plural form of "appendix", use "appendices".

### Verb Tense 

  - Use past tense when describing the process of collecting the data. 

  - Use present tense when necessary, such as when you are describing the data: "The MIDUS Refresher collection is split into two datasets."

