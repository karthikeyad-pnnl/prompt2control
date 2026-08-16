# ASHRAE Guideline 36-2024 Addendum o Report

## Inventory
- **Description:** Addresses a typo, which incorrectly disabled minimum outdoor airflow control when the economizer high limit conditions were exceeded.
- **ASHRAE approval date:** March 14, 2024
- **Affected sections:** 5.16.5.4
- **Appendix C PDF page(s):** 307

## Methodology and limitations
The supplied `addendum_a_analysis.py` extraction workflow was run in `--all` mode against the supplied 2021 and 2024 PDFs. It extracted Appendix C inventory rows and section-level evidence. The comparisons below use that evidence and normalized word-level alignment; they are not a substitute for the controlled standalone addendum redline. Because the 2024 PDF is consolidated, unrelated cumulative edits in an affected section are not independently attributed to this addendum.

## Impact classification
- **Systems impacted:** Ventilation systems; Air handling units; Multiple-zone VAV air handling units; Economizer systems
- **Primary functional category:** Ventilation control
- **Secondary functional categories:** Outdoor-air control, Economizer control, Airflow control, Documentation or editorial correction
- **Comparison status:** Complete
- **Quality level:** Partially verified

## Section-level comparison
### Section 5.16.5.4
- **2021 reference:** PDF page(s) 123, 124, 125
- **2024 reference:** PDF page(s) 140, 141, 142, 143
- **2021 excerpt:** 5.16.5.4. Outdoor Air and Return Air Dampers The engineer must specify whether the unit has a return fan, relief damper or relief fans. If there is a return fan, keep subsection (a) and delete subsection (b). If there are relief dampers or relief fans, keep subsection (b) and delete subsection (a). Delete this flag note after selections have been made. a. For units with return fans Minimum outdoor air control is enabled when return damper position exceeds MRA-P because it cannot be assumed that the combination of the minimum and the economizer outdoor air dampers are providing sufficient outdoor air under these conditions. The 20% threshold …
- **2024 excerpt:** 5.16.5.4. Outdoor Air and Return Air Dampers The engineer must specify whether the unit has a return fan, relief damper or relief fans. If there is a return fan, keep subsection (a) and delete subsection (b). If there are relief dampers or relief fans, keep subsection (b) and delete subsection (a). Delete this flag note after selections have been made. a. For units with return fans Minimum outdoor airflow control is enabled when return damper position exceeds MRA-P because it cannot be assumed that the combination of the minimum and the economizer outdoor air dampers are providing sufficient outdoor airflow under these conditions. The 20% …
- **Textual difference:** replace: 2021 [(a). Delete this flag note after selections have been made. a. For units with return fans Minimum outdoor air control is enabled when return damper position exceeds MRA-P because it cannot be assumed that the combination of] -> 2024 [(a). Delete this flag note after selections have been made. a. For units with return fans Minimum outdoor airflow control is enabled when return damper position exceeds MRA-P because it cannot be assumed that the combination of] | replace: 2021 [be assumed that the combination of the minimum and the economizer outdoor air dampers are providing sufficient outdoor air under these conditions. The 20% threshold can be increased to ensure minimum outdoor airflow will be maintained but] -> 2024 [be assumed that the combination of the minimum and the economizer outdoor air dampers are providing …
- **Operational interpretation:** Addresses a typo, which incorrectly disabled minimum outdoor airflow control when the economizer high limit conditions were exceeded.. The affected behavior should be confirmed against the full section and controlled addendum source before implementation.

## Reviewer notes
- The 2024 source is a consolidated edition; section differences cannot be attributed exclusively to this addendum without the controlled standalone addendum redline.
- System categories are engineering mappings from affected sections and descriptions; confirm against the official 2024 index.

## Validation
- Appendix C inventory row represented: **Pass**.
- All 1 listed section references represented: **Pass**.
- Systems and functional categories populated: **Pass with mapping limitation**.
- 2021-to-2024 evidence status: **Complete**.
- CDL implementation status: **Not assessed by this PDF-based workflow**.
