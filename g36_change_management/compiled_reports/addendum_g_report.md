# ASHRAE Guideline 36-2024 Addendum g Report

## Inventory
- **Description:** Addresses an issue with the minimum outdoor airflow control logic for Multiple Zone VAV Air Handling Units with a single common damper for minimum outdoor air and economizer functions with airflow measurement. Default minimum outdoor airflow control loop erroneously set the AHU to 100% outdoor air during Setback, Setup, Warm-up and Cool-down modes.
- **ASHRAE approval date:** March 14, 2024
- **Affected sections:** 5.16.6.3
- **Appendix C PDF page(s):** 306

## Methodology and limitations
The supplied `addendum_a_analysis.py` extraction workflow was run in `--all` mode against the supplied 2021 and 2024 PDFs. It extracted Appendix C inventory rows and section-level evidence. The comparisons below use that evidence and normalized word-level alignment; they are not a substitute for the controlled standalone addendum redline. Because the 2024 PDF is consolidated, unrelated cumulative edits in an affected section are not independently attributed to this addendum.

## Impact classification
- **Systems impacted:** Ventilation systems; Air handling units; Multiple-zone VAV air handling units; Economizer systems
- **Primary functional category:** Ventilation control
- **Secondary functional categories:** Outdoor-air control, Economizer control, Airflow control, Mode or state logic
- **Comparison status:** Complete
- **Quality level:** Partially verified

## Section-level comparison
### Section 5.16.6.3
- **2021 reference:** PDF page(s) 126
- **2024 reference:** PDF page(s) 143, 144, 145, 146, 147
- **2021 excerpt:** 5.16.6.3. Minimum Outdoor Air Control Loop a. Minimum outdoor air control loop is enabled when the supply fan is proven ON and the AHU is in Occupied Mode, and disabled and output set to zero otherwise. The engineer must specify whether the unit has a return fan, relief damper or relief fans. If there is a return fan, keep subsection (b) and delete subsection (c). If there are relief damper or relief fans, keep subsection (c) and delete subsection (b). Delete this flag note after selections have been made. b. For units with return fans: The following logic limits the return damper position to ensure that minimum outdoor air is maintained at …
- **2024 excerpt:** 5.16.6.3. Minimum Outdoor Airflow Control Loop Include the following section if the air handling unit is very large and thus requires staged outdoor air damper/AFMS assemblies so that airflow measurement can be accurate when the AHU is serving small Zone Groups and/or due to many zones with CO2 DCV or occupancy sensors which can result in very low minimum outdoor air rate setpoints. a. Staged Outdoor Air Dampers/AFMS Assemblies 1. Stage each outdoor air economizer damper/AFMS assembly as follows: Design drawings must clearly indicate which outdoor air damper/AFMS assembly corresponds to each stage. Fundamentally, the first stage must be the …
- **Textual difference:** replace: 2021 [5.16.6.3. Minimum Outdoor Air Control Loop a. Minimum outdoor air control loop is enabled when the supply fan is proven ON and] -> 2024 [5.16.6.3. Minimum Outdoor Airflow Control Loop Include the following section if the air handling unit is very large and thus requires staged] | insert: 2021 [5.16.6.3. Minimum Outdoor Air Control Loop a. Minimum outdoor air control loop is enabled when the supply fan is proven ON and the AHU] -> 2024 [5.16.6.3. Minimum Outdoor Airflow Control Loop Include the following section if the air handling unit is very large and thus requires staged outdoor air damper/AFMS assemblies so that airflow measurement can be accurate when the AHU is serving small Zone Groups and/or due to many zones with CO2 DCV or occupancy sensors which can result in very low minimum outdoor air rate setpoints. a. …
- **Operational interpretation:** Addresses an issue with the minimum outdoor airflow control logic for Multiple Zone VAV Air Handling Units with a single common damper for minimum outdoor air and economizer functions with airflow measurement. Default minimum outdoor airflow control loop erroneously set the AHU to 100% outdoor air during Setback, Setup, Warm-up and Cool-down modes.. The affected behavior should be confirmed against the full section and controlled addendum source before implementation.

## Reviewer notes
- The 2024 source is a consolidated edition; section differences cannot be attributed exclusively to this addendum without the controlled standalone addendum redline.
- System categories are engineering mappings from affected sections and descriptions; confirm against the official 2024 index.

## Validation
- Appendix C inventory row represented: **Pass**.
- All 1 listed section references represented: **Pass**.
- Systems and functional categories populated: **Pass with mapping limitation**.
- 2021-to-2024 evidence status: **Complete**.
- CDL implementation status: **Not assessed by this PDF-based workflow**.
