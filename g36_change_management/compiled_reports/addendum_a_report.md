# ASHRAE Guideline 36-2024 Addendum a Report

## Inventory
- **Description:** Adds Outdoor Air Pollution Mode
- **ASHRAE approval date:** August 30, 2024
- **Affected sections:** 3.1.10; 4.13; 5.1.21; 5.16.4.4; 5.16.5.4; 5.16.6.3; 5.18.7
- **Appendix C PDF page(s):** 306

## Methodology and limitations
The supplied `addendum_a_analysis.py` extraction workflow was run in `--all` mode against the supplied 2021 and 2024 PDFs. It extracted Appendix C inventory rows and section-level evidence. The comparisons below use that evidence and normalized word-level alignment; they are not a substitute for the controlled standalone addendum redline. Because the 2024 PDF is consolidated, unrelated cumulative edits in an affected section are not independently attributed to this addendum.

## Impact classification
- **Systems impacted:** Ventilation systems; Air handling units; Multiple-zone VAV air handling units; Single-zone VAV air handling units; Generic sequences or cross-system functions
- **Primary functional category:** Ventilation control
- **Secondary functional categories:** Outdoor-air control, Mode or state logic
- **Comparison status:** Complete
- **Quality level:** Partially verified

## Section-level comparison
### Section 3.1.10
- **2021 reference:** PDF page(s) not located
- **2024 reference:** PDF page(s) 23, 24
- **2021 excerpt:** Not located in the supplied edition.
- **2024 excerpt:** 3.1.10. Outdoor Air Pollution Mode Setpoints Air quality sensors may be provided to disable economizers when outdoor air quality is poor to reduce the indoor concentration of outdoor air pollutants and to reduce filter loading. The maximum setpoints below are the threshold above which Outdoor Air Pollution Mode will be enabled. Limits are defined for three common air pollutants, but the designer can add other sensors and control thresholds if desired. 3.1.10.1. Outdoor Air PM2.5 Concentration Limit (OA-PM2.5-Max) Outdoor air PM.2.5 concentration limit can be set based on filter rating of AHUs with outdoor air economizers per Informative …
- **Textual difference:** New section/content in 2024; no corresponding 2021 section was extracted.
- **Operational interpretation:** Adds Outdoor Air Pollution Mode. The affected behavior should be confirmed against the full section and controlled addendum source before implementation.

### Section 4.13
- **2021 reference:** PDF page(s) not located
- **2024 reference:** PDF page(s) 48
- **2021 excerpt:** Not located in the supplied edition.
- **2024 excerpt:** 4.13 Air Quality Sensors Although air particulate matter and ozone sensors are generally inexpensive, they tend to require regular maintenance, calibration, and/or replacement. To reduce these costs, outdoor air PM2.5 and Ozone concentrations can be obtained via an internet connection to a weather station, where sensors are professionally maintained. Air Quality Index sensors that measure all six of the contaminants included in the US EPA AQI are generally not currently commercially available, or prohibitively expensive, so an internet connection to a weather station or EPA site is likely the only option. Note that some internet weather and …
- **Textual difference:** New section/content in 2024; no corresponding 2021 section was extracted.
- **Operational interpretation:** Adds Outdoor Air Pollution Mode. The affected behavior should be confirmed against the full section and controlled addendum source before implementation.

### Section 5.1.21
- **2021 reference:** PDF page(s) not located
- **2024 reference:** PDF page(s) 65, 66
- **2021 excerpt:** Not located in the supplied edition.
- **2024 excerpt:** 5.1.21. Outdoor Air Pollution Mode 5.1.21.1. Provide a 3-position software switch for Outdoor Air Pollution Mode: It is recommended to add the user-adjustable 3-position switch to the graphics in a centralized location for easy operator access to initiate Outdoor Air Pollution Mode. a. Off. Locks Outdoor Air Pollution Mode off. b. On. Outdoor Air Pollution Mode is enabled for a preset period of time, after which Outdoor Air Pollution Mode shall be disabled. The preset time shall be operator adjustable for up to 1 week. c. Auto. Outdoor Air Pollution Mode is enabled when any of the following are true. Include only those sensors provided. 1. …
- **Textual difference:** New section/content in 2024; no corresponding 2021 section was extracted.
- **Operational interpretation:** Adds Outdoor Air Pollution Mode. The affected behavior should be confirmed against the full section and controlled addendum source before implementation.

### Section 5.16.4.4
- **2021 reference:** PDF page(s) 120, 121, 122
- **2024 reference:** PDF page(s) 137, 138, 139
- **2021 excerpt:** 5.16.4.4. Outdoor Air and Return Air Dampers The engineer must specify whether the unit has a return fan, relief damper or relief fans. If there is a return fan, keep subsection (a) and delete subsection (b). If there are relief damper or relief fans, keep subsection (b) and delete subsection (a). Delete this flag note after selections have been made. a. For units with return fans Minimum outdoor air control is enabled when return damper position exceeds MRA-P because it cannot be assumed that the combination of the minimum and the economizer outdoor air dampers are providing sufficient outdoor air under these conditions. The 20% threshold …
- **2024 excerpt:** 5.16.4.4. Outdoor Air and Return Air Dampers The engineer must specify whether the unit has a return fan, relief damper or relief fans. If there is a return fan, keep subsection (a) and delete subsection (b). If there are relief damper or relief fans, keep subsection (b) and delete subsection (a). Delete this flag note after selections have been made. a. For units with return fans Minimum outdoor air control is enabled when return damper position exceeds MRA-P because it cannot be assumed that the combination of the minimum and the economizer outdoor air dampers are providing sufficient outdoor airflow under these conditions. The 20% …
- **Textual difference:** replace: 2021 [be assumed that the combination of the minimum and the economizer outdoor air dampers are providing sufficient outdoor air under these conditions. The 20% threshold can be increased to ensure minimum outdoor airflow will be maintained but] -> 2024 [be assumed that the combination of the minimum and the economizer outdoor air dampers are providing sufficient outdoor airflow under these conditions. The 20% threshold can be increased to ensure minimum outdoor airflow will be maintained but] | replace: 2021 [When MRA-P is not being calculated for any reason, it shall be set to 100%. 2. Minimum outdoor air control shall be enabled when the unit is in Occupied Mode and either of the following conditions are] -> 2024 [When MRA-P is not being calculated for any reason, it shall be set to 100%. 2. Minimum outdoor airflow control …
- **Operational interpretation:** Adds Outdoor Air Pollution Mode. The affected behavior should be confirmed against the full section and controlled addendum source before implementation.

### Section 5.16.5.4
- **2021 reference:** PDF page(s) 123, 124, 125
- **2024 reference:** PDF page(s) 140, 141, 142, 143
- **2021 excerpt:** 5.16.5.4. Outdoor Air and Return Air Dampers The engineer must specify whether the unit has a return fan, relief damper or relief fans. If there is a return fan, keep subsection (a) and delete subsection (b). If there are relief dampers or relief fans, keep subsection (b) and delete subsection (a). Delete this flag note after selections have been made. a. For units with return fans Minimum outdoor air control is enabled when return damper position exceeds MRA-P because it cannot be assumed that the combination of the minimum and the economizer outdoor air dampers are providing sufficient outdoor air under these conditions. The 20% threshold …
- **2024 excerpt:** 5.16.5.4. Outdoor Air and Return Air Dampers The engineer must specify whether the unit has a return fan, relief damper or relief fans. If there is a return fan, keep subsection (a) and delete subsection (b). If there are relief dampers or relief fans, keep subsection (b) and delete subsection (a). Delete this flag note after selections have been made. a. For units with return fans Minimum outdoor airflow control is enabled when return damper position exceeds MRA-P because it cannot be assumed that the combination of the minimum and the economizer outdoor air dampers are providing sufficient outdoor airflow under these conditions. The 20% …
- **Textual difference:** replace: 2021 [(a). Delete this flag note after selections have been made. a. For units with return fans Minimum outdoor air control is enabled when return damper position exceeds MRA-P because it cannot be assumed that the combination of] -> 2024 [(a). Delete this flag note after selections have been made. a. For units with return fans Minimum outdoor airflow control is enabled when return damper position exceeds MRA-P because it cannot be assumed that the combination of] | replace: 2021 [be assumed that the combination of the minimum and the economizer outdoor air dampers are providing sufficient outdoor air under these conditions. The 20% threshold can be increased to ensure minimum outdoor airflow will be maintained but] -> 2024 [be assumed that the combination of the minimum and the economizer outdoor air dampers are providing …
- **Operational interpretation:** Adds Outdoor Air Pollution Mode. The affected behavior should be confirmed against the full section and controlled addendum source before implementation.

### Section 5.16.6.3
- **2021 reference:** PDF page(s) 126
- **2024 reference:** PDF page(s) 143, 144, 145, 146, 147
- **2021 excerpt:** 5.16.6.3. Minimum Outdoor Air Control Loop a. Minimum outdoor air control loop is enabled when the supply fan is proven ON and the AHU is in Occupied Mode, and disabled and output set to zero otherwise. The engineer must specify whether the unit has a return fan, relief damper or relief fans. If there is a return fan, keep subsection (b) and delete subsection (c). If there are relief damper or relief fans, keep subsection (c) and delete subsection (b). Delete this flag note after selections have been made. b. For units with return fans: The following logic limits the return damper position to ensure that minimum outdoor air is maintained at …
- **2024 excerpt:** 5.16.6.3. Minimum Outdoor Airflow Control Loop Include the following section if the air handling unit is very large and thus requires staged outdoor air damper/AFMS assemblies so that airflow measurement can be accurate when the AHU is serving small Zone Groups and/or due to many zones with CO2 DCV or occupancy sensors which can result in very low minimum outdoor air rate setpoints. a. Staged Outdoor Air Dampers/AFMS Assemblies 1. Stage each outdoor air economizer damper/AFMS assembly as follows: Design drawings must clearly indicate which outdoor air damper/AFMS assembly corresponds to each stage. Fundamentally, the first stage must be the …
- **Textual difference:** replace: 2021 [5.16.6.3. Minimum Outdoor Air Control Loop a. Minimum outdoor air control loop is enabled when the supply fan is proven ON and] -> 2024 [5.16.6.3. Minimum Outdoor Airflow Control Loop Include the following section if the air handling unit is very large and thus requires staged] | insert: 2021 [5.16.6.3. Minimum Outdoor Air Control Loop a. Minimum outdoor air control loop is enabled when the supply fan is proven ON and the AHU] -> 2024 [5.16.6.3. Minimum Outdoor Airflow Control Loop Include the following section if the air handling unit is very large and thus requires staged outdoor air damper/AFMS assemblies so that airflow measurement can be accurate when the AHU is serving small Zone Groups and/or due to many zones with CO2 DCV or occupancy sensors which can result in very low minimum outdoor air rate setpoints. a. …
- **Operational interpretation:** Adds Outdoor Air Pollution Mode. The affected behavior should be confirmed against the full section and controlled addendum source before implementation.

### Section 5.18.7
- **2021 reference:** PDF page(s) 158
- **2024 reference:** PDF page(s) 177
- **2021 excerpt:** 5.18.7. Economizer Lockout This section describes economizer lockout logic for a unit with a common minimum OA and economizer damper (i.e., no separate minimum OA damper). Other configurations are possible, and would require modifications to the points list (above) and the control logic below. 5.18.7.1. The normal sequencing of the economizer dampers shall be disabled in accordance with Section
- **2024 excerpt:** 5.18.7. Economizer Lockout This section describes economizer lockout logic for a unit with a common minimum OA and economizer damper (i.e., no separate minimum OA damper). Other configurations are possible, and would require modifications to the points list (above) and the control logic below. 5.18.7.1. The normal sequencing of the economizer dampers shall be disabled if the economizer high limit conditions in Section 5.1.17 are exceeded for 10 minutes or Outdoor Air Pollution Mode is enabled per Section 5.1.16. 5.18.7.2. Once the economizer is disabled, it shall not be reenabled within 10 minutes and vice versa. 5.18.7.3. When economizer is …
- **Textual difference:** insert: 2021 [list (above) and the control logic below. 5.18.7.1. The normal sequencing of the economizer dampers shall be disabled in accordance with Section] -> 2024 [list (above) and the control logic below. 5.18.7.1. The normal sequencing of the economizer dampers shall be disabled if the economizer high limit conditions in Section 5.1.17 are exceeded for 10 minutes or Outdoor Air Pollution Mode is enabled per Section 5.1.16.] | delete: 2021 [(above) and the control logic below. 5.18.7.1. The normal sequencing of the economizer dampers shall be disabled in accordance with Section] -> 2024 [5.18.7.1. The normal sequencing of the economizer dampers shall be disabled if the economizer high limit conditions in Section 5.1.17 are exceeded for 10 minutes or Outdoor Air Pollution Mode is enabled per Section 5.1.16. 5.18.7.2.] | insert: 2021 …
- **Operational interpretation:** Adds Outdoor Air Pollution Mode. The affected behavior should be confirmed against the full section and controlled addendum source before implementation.

## Reviewer notes
- The 2024 source is a consolidated edition; section differences cannot be attributed exclusively to this addendum without the controlled standalone addendum redline.
- System categories are engineering mappings from affected sections and descriptions; confirm against the official 2024 index.

## Validation
- Appendix C inventory row represented: **Pass**.
- All 7 listed section references represented: **Pass**.
- Systems and functional categories populated: **Pass with mapping limitation**.
- 2021-to-2024 evidence status: **Complete**.
- CDL implementation status: **Not assessed by this PDF-based workflow**.
