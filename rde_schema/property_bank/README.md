# ICPSR Property Bank Entries
Updated on December 17, 2025

The RDE Ingest module presents an important opportunity to revise and refine the RDE Metadata Schema. To facilitate a metadata-driven ingest process, we are pivoting from archive-based schemas (e.g., one schema developed explicitly for the AEA Repository, a separate one for NACJD, etc.) to a 'property bank' model, which involves a collection of individually-defined metadata elements (i.e., the 'property bank') that may be reused (via the JSON Schema [$ref](https://json-schema.org/understanding-json-schema/structuring#dollarref) keyword) in one or more composite metadata schemas. Within the property bank, each metadata element will be defined in its own [JSON Schema](https://json-schema.org/understanding-json-schema) document; Metadata & Preservation will contribute information about how the property may be used (e.g., definition of the term, accepted data type, controlled vocabularies, examples of valid values, etc.), while CNS will contribute technical details (e.g., limits on string lengths, UI components, error messages, etc.).


## Reviewed Metadata Elements
These metadata elements have been reviewed by the Metadata & Preservation team, which has approved the definitions, data types, usage notes, and sample values. Additional technical details will be provided by CNS staff. Metadata elements may also be subject to change based on evolving RDE system needs and requirements.

| Property Title | Description |
| ----- | ----------- |
| [Alternate Titles](alternate_titles.json) | The alternate name(s) or acronym(s) commonly used to refer to the data collection. |
| [Citation](citation.json) | The official way to reference the data collection in writing. |
| [Collection Dates](collection_dates.json) | The date(s) when the data were physically collected. |
| [Collection Modes](collection_modes.json) | The method(s) or procedure(s) used to collect the data. |
| [Common Data Elements](common_data_elements.json) | Common Data Elements (standardized concepts used to ensure consistency and interoperability across datasets) found in the data collection. |
| [Contributors](contributors.json) | The people or organizations (other than the principal investigators) that contributed to the data collection in supporting roles. |
| [Data Management Plan](data_management_plan.json) | A link to the data management plan (preferably a persistent identifier such as a DOI). |
| [Data Source Types](data_source_types.json) | The source(s) of the data as collected by the Principal Investigators. |
| [Deposits](deposits.json) | Information about deposits associated with the data collection. |
| [Distributors](distributors.json) | The organization(s) responsible for distributing the data collection. |
| [External Data Sources](external_data_sources.json) | The source of the data, when that source is external to the data collection and can be independently cited. |
| [External Source ID](external_source_id.json) | A unique identifier supplied by the data depositor |
| [Funding Sources](funding_sources.json) | The sources of funding that supported the data collection. |
| [General Data Formats](general_data_formats.json) | The file format types present in the data collection. |
| [Geographic Coverage Areas](geographic_coverage_areas.json) | The geographic locations where the data refer or are related. |
| [ICPSR Subject Terms](icpsr_subject_terms.json) | A controlled list of social science terms maintained by ICPSR and used to indicate topics related to the data collection. |
| [Journal of Economic Literature (JEL) Classification Codes](jel_classifications.json) | Classification codes used to categorize economic research. |
| [Languages](languages.json) | The language(s) used in the data collection. |
| [License](license.json) | A license governing the data's use. |
| [Link Title](link_title.json) | The title of an external resource that is included in the ICPSR catalog as a courtesy to users. |
| [Link URL](link_url.json) | The URL of an external resource that is included in the ICPSR catalog as a courtesy to users. |
| [Manuscript Number](manuscript_number.json) | A unique identifier that associates the data collection with a manuscript submitted to a journal. |
| [Medical Subject Headings (MeSH) Terms](mesh_subject_terms.json) | Biomedical and health-related terms from the National Library of Medicine that describe the data collection's topics. |
| [Nationally Representative Sample](nationally_representative_sample.json) | Indicates whether the data collection uses a sampling design intended to represent the demographics, behaviors, and/or characteristics of the entire nation. This typically involves probability-based methods that allow generalization. It does not include convenience samples that appear similar to the nation by chance. |
| [Notes](notes.json) | Important details about the data collection (like unique authoring, discrepancies, or processing information) that can't be recorded in other metadata elements. |
| [Organization](organization.json) | An organization associated with an ICPSR data collection or service. |
| [Oversamples](oversamples.json) | Key group(s) given higher odds of selection into a probability sample than would occur by chance, allowing for both within- and between-group comparisons in the resulting data. |
| [Person](person.json) | A person associated with an ICPSR data collection or service. |
| [Preregistration](preregistration.json) | A link to a research plan for the data collection (preferably a persistent identifier such as a DOI). |
| [Principal Investigators](principal_investigators.json) | The key people or organizations responsible for the data collection, listed by importance. Each data collection requires at least one PI, either a person or an organization. |
| [Response Rates](response_rates.json) | The percentage of respondents in the sample who participated in the data collection. |
| [Restrictions](restrictions.json) | Rules about how the data collection can be accessed or used. |
| [Sampling Note](sampling_note.json) | Supplemental information about the sampling process that does not fit neatly into the Sampling Procedure field. |
| [Sampling Procedures](sampling_procedures.json) | The type(s) of sample and sample design used to select survey respondents to represent the population. |
| [Scales](scales.json) | Any commonly known scales used to collect data for the data collection (e.g., MMPI, CPI, the Census Occupational Codes, etc.). |
| [Smallest Geographic Unit](smallest_geographic_unit.json) | The smallest geographic unit (e.g., state or census tract) used in the dataset. |
| [Software Applications](software_applications.json) | Software used by the principal investigator(s) to collect or analyze data, required to understand how the data were obtained or to reproduce results. |
| [Study Design](study_design.json) | The procedures used to contact participants and gather data. |
| [Study Purpose](study_purpose.json) | The study's main goals and associated research questions. |
| [Summary](summary.json) | A description of the data collection that helps users understand its purpose, substance, and key topics. |
| [Time Methods](time_methods.json) | The methods used to collect data over time, like snapshots at one point (cross-sectional) or repeatedly (longitudinal) to study changes or trends |
| [Time Periods](time_periods.json) | The time period(s) to which the data refer, regardless of when the data were collected. |
| [Title](title.json) | The official title that describes what the data collection is about, its geographic scope, and the time period it covered. |
| [Units of Analysis](units_of_analysis.json) | The object(s) of analysis for the data collection, such as an organization, individual, or household. |
| [Universe](universe.json) | The total group of persons or other entities (e.g., households or organizations) that were the object of research and to which analytic results refer. |
| [Variable Description](variable_description.json) | Significant variables (particularly demographic variables) in the data files. |
| [Version History](version_history.json) | A record of how the data collection has changed over time. |
| [Weights](weight.json) | The weight variables and the criteria for using them in data analysis or other information about how the data are weighted if no weight variables are present. |


## Under Review Metadata Elements
These metadata elements are still under review by the Metadata & Preservation team and as a result are not ready for use.
| Property Title | Description |
| ----- | ----------- |
| [Extent of Processing](extent_of_processing.json) | Processing activities and checks performed on the data collection by ICPSR curation staff. |
