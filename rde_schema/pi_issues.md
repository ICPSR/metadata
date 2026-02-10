### Principal Investigators (level 3 heading)

**Description:** The key people or organizations responsible for the data collection, listed by importance. Each data collection requires at least one PI, either a person or an organization.

**Repeatable**: Yes

**Accepted Values**: Multi-part element; see subfield definitions for more information.

#### Subfields: (level 4 heading)

| Property | Required? | Repeatable? | Accepted Values | Description |
| -------- | --------- | ----------- | --------------- | ----------- |
| Person | No | No | Multi-part element; see subfields | A person associated with an ICPSR data collection or service. |
| Organization | No | No | Multi-part element; see subfields | An organization associated with an ICPSR data collection or service. |
| Order | No | No | Number | The order or rank of importance for the PIs associated with the data collection, typically provided to ICPSR by the lead PI. |

##### Person (level 5 heading)

**Description:** A person associated with an ICPSR data collection or service.

**Repeatable**: No

**Accepted Values**: Multi-part element; see subfield definitions for more information.

###### Sub-Subfields: (level 6 heading)

| Property | Required? | Repeatable? | Accepted Values | Description |
| -------- | --------- | ----------- | --------------- | ----------- |
| Personal Name | Yes | No | Multi-part element; see subfield definitions | The person's name. |
| ORCID | No | No | Text | The person's Open Researcher and Contributor ID (ORCID). |
| Affiliation(s) | No | Yes | Array | The person's affiliated organization(s). |
| Email Address | No | No | Text | The person's email address. |

_Personal Name_ (level 7 heading)

**Description:** The person's name.

**Required**: Yes

**Repeatable**: No

**Accepted Values**: Multi-part element; see subfield definitions

Sub-Sub-Subfields: (level 8 heading)

| Property | Required? | Repeatable? | Accepted Values | Description |
| -------- | --------- | ----------- | --------------- | ----------- |
| Given Name | Yes | No | Text | The person's first (given) name, which may include a middle name or initial. |
| Family Name | Yes | No | Text | The person's last (family) name, which may include a suffix (e.g., Jr., Sr., IV). |


**Given Name (First Name)** (level 9 heading)
- **Description:** The person's first (given) name, which may include a middle name or initial.
- **Required:** Yes
- **Type:** Text
- **Examples:**
  - `Chantel`
  - `Giannis`
  - `Mary Kate`
  - `John Q.`

**Family Name (Last Name)** (level 9 heading)
- **Description:** The person's last (family) name, which may include a suffix (e.g., Jr., Sr., IV).
- **Required:** No
- **Type:** Text
- **Examples:**
  - `Smith`
  - `Jordan Jr.`
  - `Escobar-Vega`

_ORCID Identifier_ (level 7 heading)

**Description:** The person's Open Researcher and Contributor ID (ORCID).

**Required**: No

**Repeatable**: No

**Accepted Values**: Text

**Examples:**

```json
"https://orcid.org/0000-0001-6289-1234"
```

_Affiliation(s)_ (level 7 heading)

**Description:** The person's affiliated organization(s).

**Repeatable**: No

**Accepted Values**: Multi-part element; see subfield definitions for more information.

Sub-Sub-Subfields: (level 8 heading)

| Property | Required? | Repeatable? | Accepted Values | Description |
| -------- | --------- | ----------- | --------------- | ----------- |
| Organization Name | Yes | No | Text | The organization's name. |
| Organization Name Code | No | No | Text | A machine-readable/-actionable form of the organization's name. |
| Organization Name URI | No | No | Text | The URI for the organization's name. |
| ROR Identifier | No | No | Text | The organization's Research Organization Registry (ROR) identifier. |
| Email Address | No | No | Text | The organization's email address. |

_Organization Name_ (level 7 heading)

**Description:** The organization's name.

**Required**: Yes

**Repeatable**: No

**Accepted Values**: Text

**Examples:**

```json
"Federal Reserve Bank of St. Louis. Research Division"
```

```json
"University of Michigan. Institute for Social Research"
```

_Organization Name Code_ (level 7 heading)

**Description:** A machine-readable/-actionable form of the organization's name.

**Required**: No

**Repeatable**: No

**Accepted Values**: Text

**Examples:**

```json
"1234"
```

```json
"2345"
```

```json
"3456"
```

_Organization Name URI_ (level 7 heading)

**Description:** The URI for the organization's name.

**Required**: No

**Repeatable**: No

**Accepted Values**: Text

_ROR Identifier_ (level 7 heading)

**Description:** The organization's Research Organization Registry (ROR) identifier.

**Required**: No

**Repeatable**: No

**Accepted Values**: Text

**Examples:**

```json
"https://ror.org/02q7mkh03"
```

_Email Address_ (level 7 heading)

**Description:** The organization's email address.

**Required**: No

**Repeatable**: No

**Accepted Values**: Text

**Examples:**

```json
"info@example.com"
```


Sub-Sub-Subfields: (level 8 heading)

_Email Address_ (level 7 heading)

**Description:** The person's email address.

**Required**: No

**Repeatable**: No

**Accepted Values**: Text

**Examples:**

```json
"j.doe@example.com"
```

## Complete Examples (with Subfields):

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


##### Organization (level 5 heading)

**Description:** An organization associated with an ICPSR data collection or service.

**Repeatable**: No

**Accepted Values**: Multi-part element; see subfield definitions for more information.

###### Subfields: (level 6 heading)

| Property | Required? | Repeatable? | Accepted Values | Description |
| -------- | --------- | ----------- | --------------- | ----------- |
| Organization Name | Yes | No | Text | The organization's name. |
| Organization Name Code | No | No | Text | A machine-readable/-actionable form of the organization's name. |
| Organization Name URI | No | No | Text | The URI for the organization's name. |
| ROR Identifier | No | No | Text | The organization's Research Organization Registry (ROR) identifier. |
| Email Address | No | No | Text | The organization's email address. |

_Organization Name_ (level 7 heading)

**Description:** The organization's name.

**Required**: Yes

**Repeatable**: No

**Accepted Values**: Text

**Examples:**

```json
"Federal Reserve Bank of St. Louis. Research Division"
```

```json
"University of Michigan. Institute for Social Research"
```

_Organization Name Code_ (level 7 heading)

**Description:** A machine-readable/-actionable form of the organization's name.

**Required**: No

**Repeatable**: No

**Accepted Values**: Text

**Examples:**

```json
"1234"
```

```json
"2345"
```

```json
"3456"
```

_Organization Name URI_ (level 7 heading)

**Description:** The URI for the organization's name.

**Required**: No

**Repeatable**: No

**Accepted Values**: Text

_ROR Identifier_ (level 7 heading)

**Description:** The organization's Research Organization Registry (ROR) identifier.

**Required**: No

**Repeatable**: No

**Accepted Values**: Text

**Examples:**

```json
"https://ror.org/02q7mkh03"
```

_Email Address_ (level 7 heading)

**Description:** The organization's email address.

**Required**: No

**Repeatable**: No

**Accepted Values**: Text

**Examples:**

```json
"info@example.com"
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

