# Specification: ASHRAE Guideline 36 Addenda Impact Matrix

## 1. Objective

Create a comprehensive table documenting the addenda incorporated into ASHRAE Guideline 36-2024.

The table shall preserve the original columns from Informative Appendix C, Table C-1, and add the following analytical columns:

1. Systems impacted by the addendum
2. Functional category impacted by the addendum
3. Actual textual change from ASHRAE Guideline 36-2021 to Guideline 36-2024

The resulting table shall support engineering review, implementation planning, and traceability from each addendum to the affected HVAC sequence-of-operation content.

## 2. Source documents

### Primary source

- ASHRAE Guideline 36-2024
- Informative Appendix C, “Addenda Description”
- Table C-1, “Addenda Description Table”

The source table provides:

- Addendum
- Section(s) affected
- Description of change
- ASHRAE approval date

Guideline 36-2024 identifies the addenda incorporated into the 2024 edition and provides the approval dates and summary descriptions in Appendix C [1].

### Comparison source

- ASHRAE Guideline 36-2021

The 2021 edition shall be used as the baseline for determining the actual wording and sequence changes introduced by each addendum [2].

### Supporting source

- The index of ASHRAE Guideline 36-2024

The index shall be used to map each affected section to a broad system category.

## 3. Required output columns

| Column | Description |
|---|---|
| Addendum | Addendum identifier, such as `a`, `b`, or `z` |
| Section(s) Affected | Section numbers listed in Table C-1 |
| Description of Change | Original summary from Table C-1 |
| ASHRAE Approval Date | Approval date listed in Table C-1 |
| Systems Impacted | Broad HVAC system category or categories derived from the index and affected sections |
| Functional Category | Primary functional classification of the change |
| Actual Change from 2021 | Detailed comparison of the 2021 and 2024 text |

## 4. Systems impacted

The `Systems Impacted` column shall use broad categories derived from the index rather than overly specific equipment names.

Recommended categories include:

- Air handling units
- Multiple-zone VAV air handling units
- Single-zone VAV air handling units
- Fan-powered terminal units
- VAV terminal units
- Dual-duct systems
- Chilled-water plants
- Hot-water plants
- Condenser-water systems
- Hydronic distribution systems
- Ventilation systems
- Economizer systems
- Indoor-air-quality and outdoor-air-pollution control systems
- Humidity-control systems
- Central plants
- Generic sequences or cross-system functions

### System-category rules

1. Use the most specific broad category supported by the index.
2. Assign multiple categories when an addendum affects multiple system types.
3. Use `Cross-system` when the affected sections apply to multiple equipment classes and no single system category is dominant.
4. Do not infer a system category solely from the wording of the addendum summary when the affected section or index provides more precise information.
5. Preserve the original section number as the traceability anchor.

## 5. Functional categories

Each addendum shall receive one primary functional category and, where necessary, one or more secondary categories.

Recommended functional categories include:

- Alarm
- Setpoint generation
- Process control
- Mode or state logic
- Ventilation control
- Outdoor-air control
- Economizer control
- Humidity control
- Demand-controlled ventilation
- Fault detection and diagnostics
- Equipment enable/disable
- Scheduling and occupancy
- Airflow control
- Temperature control
- Hydronic control
- Plant optimization
- Sensor validation or calibration
- Documentation or editorial correction

### Functional-category rules

1. Classify the addendum based on the operational behavior changed, not merely the equipment affected.
2. Use `Alarm` when the change modifies alarm thresholds, delays, priorities, alarm suppression, or alarm generation.
3. Use `Setpoint generation` when the change modifies how a setpoint is calculated, reset, limited, or selected.
4. Use `Process control` when the change modifies equipment sequencing, control-loop behavior, valve or damper commands, or operating-state logic.
5. Use multiple functional categories when the addendum clearly affects more than one control function.
6. Use `Documentation or editorial correction` only when the change does not alter control behavior.

## 6. Actual textual change from the 2021 version

The `Actual Change from 2021` column shall document the difference between the applicable 2021 text and the corresponding 2024 text.

For every affected section:

1. Extract the relevant 2021 text.
2. Extract the corresponding 2024 text.
3. Align the two versions by section, subsection, paragraph, and item lettering.
4. Identify additions, deletions, substitutions, relocations, and changed numerical values.
5. Summarize the operational effect in engineering terms.
6. Retain enough quoted or near-verbatim text to make the change auditable.
7. Clearly distinguish:
   - New text
   - Deleted text
   - Revised text
   - Relocated text
   - Editorial-only text

### Recommended format

Each cell should use the following structure:

```text
Section 5.x.x:
- 2021: [relevant wording or concise excerpt]
- 2024: [relevant wording or concise excerpt]
- Change: [specific textual difference]
- Operational effect: [effect on sequence or control behavior]
```

For large changes, the table should link to a separate detailed change log rather than placing the entire redline in a single cell.

## 7. Change classification

Each textual difference shall be classified as one or more of:

- Added requirement or sequence logic
- Removed requirement or sequence logic
- Modified calculation
- Modified threshold or limit
- Modified timing or delay
- Modified alarm level
- Modified equipment enable/disable behavior
- Modified operating mode
- Modified sensor or measurement logic
- Modified setpoint reset logic
- Modified fault-detection logic
- Typographical or editorial correction
- Clarification without apparent behavioral change

## 8. Traceability requirements

Every row shall be traceable to:

- The addendum identifier
- The 2024 section number
- The corresponding 2021 section number
- The source-page location in the 2021 document
- The source-page location in the 2024 document
- The index entry used for system categorization
- The comparison status

Recommended traceability fields:

| Field | Purpose |
|---|---|
| 2021 Reference | Section and page in the 2021 document |
| 2024 Reference | Section and page in the 2024 document |
| Index Reference | Index term used to identify the system |
| Comparison Status | Complete, partial, or unavailable |
| Reviewer Notes | Ambiguities, assumptions, or unresolved mappings |

## 9. Processing workflow

### Step 1: Extract the addenda inventory

Extract every row from 2024 Informative Appendix C, Table C-1.

The inventory must include all addenda listed in the appendix, not only those visible in an excerpt.

### Step 2: Normalize section references

Normalize section references by:

- Removing line-break artifacts
- Standardizing punctuation
- Separating multiple section numbers
- Preserving subsection precision
- Detecting continuation rows spanning pages

### Step 3: Map sections to systems

For each affected section:

1. Search the 2024 index.
2. Identify the corresponding broad system category.
3. Resolve multiple matches.
4. Record the index term and confidence level.
5. Assign one or more system categories.

### Step 4: Assign functional categories

Review the addendum description and affected text.

Assign:

- One primary functional category
- Zero or more secondary functional categories
- A confidence level if classification is ambiguous

### Step 5: Compare 2021 and 2024 text

For each affected section:

1. Locate the 2021 baseline text.
2. Locate the 2024 revised text.
3. Perform a textual comparison.
4. Identify the exact modifications.
5. Summarize the control-system impact.
6. Record any sections that cannot be compared directly.

### Step 6: Validate the results

Perform the following checks:

- Every 2024 addendum has a row.
- Every affected section is represented.
- Every row has a system category.
- Every row has a functional category.
- Every row has a comparison result.
- Approval dates match Appendix C.
- No 2021-only addendum is incorrectly represented as a 2024 addendum.
- Page continuation artifacts have not caused duplicated or missing content.
- Numerical values, units, timing values, and alarm levels have been checked manually.

## 10. Handling incomplete or ambiguous evidence

If the 2021 and 2024 text is unavailable, unreadable, or not directly comparable:

- Do not claim that an exact textual redline has been completed.
- Set `Comparison Status` to `Partial` or `Unavailable`.
- Use the Appendix C description as a preliminary summary only.
- Identify the missing section or page.
- Mark the system and functional classification as provisional if it was inferred.
- Require manual review before the row is considered complete.

The currently provided excerpts are sufficient to identify several addenda and their summary descriptions, but they do not include the complete text of every affected 2021 and 2024 section. Therefore, a fully verified “actual change” column cannot be produced from the excerpts alone.

## 11. Quality levels

Each row shall receive one of the following quality levels:

### Verified

- Both 2021 and 2024 text were located.
- The textual change was reviewed.
- System mapping was confirmed against the index.
- Functional category was reviewed.

### Partially verified

- The addendum description and affected sections are available.
- The complete text comparison is incomplete or one source is unclear.

### Provisional

- The classification is based primarily on the addendum summary or inferred section context.
- Manual verification is required.

## 12. Proposed final table structure

| Addendum | Section(s) Affected | Description of Change | ASHRAE Approval Date | Systems Impacted | Functional Category | Actual Change from 2021 | 2021 Reference | 2024 Reference | Comparison Status | Quality Level |
|---|---|---|---|---|---|---|---|---|---|---|

## 13. Example row format

The following is an illustrative format, not a completed redline:

| Addendum | Section(s) Affected | Description of Change | ASHRAE Approval Date | Systems Impacted | Functional Category | Actual Change from 2021 | Comparison Status |
|---|---|---|---|---|---|---|---|
| m | 5.6.6.5, 5.7.6.6, 5.8.6.6, 5.9.6.6, 5.10.6.6 | Revision to the leaking valve alarm for equipment with hot-water valves to reduce nuisance alarms | March 14, 2024 | VAV terminal units; hydronic heating systems | Alarm; sensor validation or calibration | To be completed by comparing the affected 2021 and 2024 subsections, including alarm criteria, timing, thresholds, and alarm level | Pending full-text comparison |

The 2024 appendix identifies addendum m as a revision to leaking-valve alarms for equipment with hot-water valves [1].

## 14. Deliverables

The completed work shall produce:

1. A final CSV or spreadsheet containing the complete impact matrix.
2. A Markdown report with:
   - Methodology
   - Assumptions
   - System-category mapping
   - Functional-category definitions
   - Detailed change summaries
   - Exceptions and unresolved items
3. A YAML representation of the metadata and row-level results.
4. An optional detailed redline appendix containing section-level comparisons.
5. A validation report identifying incomplete or provisional rows.

## 15. Acceptance criteria

The work is complete when:

- All addenda listed in 2024 Appendix C are included.
- Original Appendix C fields are preserved.
- New system and functional fields are populated.
- Every affected section has been reviewed.
- Actual 2021-to-2024 changes are documented where source text is available.
- Incomplete comparisons are explicitly identified.
- System classifications are traceable to the index.
- Functional classifications are consistent across rows.
- Dates and section numbers match the source documents.
- The output is suitable for engineering review and future updates.