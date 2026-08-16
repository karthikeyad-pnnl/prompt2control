# ASHRAE Guideline 36-2024 Addendum q Report

## Inventory
- **Description:** Revises demand controlled ventilation calculations to be consistent with ASHRAE Standard 62.1 and California Title 24.
- **ASHRAE approval date:** August 30, 2024
- **Affected sections:** 3.1.1.3; 5.2.1.3; 5.2.1.4; 5.2.3
- **Appendix C PDF page(s):** 307

## Methodology and limitations
The supplied `addendum_a_analysis.py` extraction workflow was run in `--all` mode against the supplied 2021 and 2024 PDFs. It extracted Appendix C inventory rows and section-level evidence. The comparisons below use that evidence and normalized word-level alignment; they are not a substitute for the controlled standalone addendum redline. Because the 2024 PDF is consolidated, unrelated cumulative edits in an affected section are not independently attributed to this addendum.

## Impact classification
- **Systems impacted:** Ventilation systems; Air handling units; Multiple-zone VAV air handling units; Generic sequences or cross-system functions
- **Primary functional category:** Ventilation control
- **Secondary functional categories:** Outdoor-air control
- **Comparison status:** Complete
- **Quality level:** Partially verified

## Section-level comparison
### Section 3.1.1.3
- **2021 reference:** PDF page(s) 7, 8, 9
- **2024 reference:** PDF page(s) 7, 8
- **2021 excerpt:** 3.1.1.3. CO2 Setpoints Space CO2 setpoints are used for demand-controlled ventilation (DCV) and monitoring/alarming as required by LEED and other green building standards. It is the designer’s responsibility to determine CO2 setpoints. The maximum setpoint varies by ventilation standard. Some guidance is provided below for Standard 62.1 and Title 24. The designer may also decide to set lower, more conservative setpoints for improved indoor air quality but at the expense of higher energy use. Standard 62.1 CO2 Setpoint Guidance Recommended maximum CO2 is 90% of the steady state concentration per Lawrence1: 𝐶𝑂2𝑠𝑒𝑡𝑝𝑜𝑖𝑛𝑡= 0.9(𝐶𝑂𝐴+ 8400𝐸𝑧𝑚 …
- **2024 excerpt:** 3.1.1.3. CO2 Maximum Concentration Space CO2 sensors are used for demand-controlled ventilation (DCV) as required by energy standards such as ASHRAE Standard 90.1 and California Title 24, as well as for indoor air quality monitoring/alarming as required by LEED and other green building standards. It is the designer’s responsibility to determine maximum ΔCO2, the maximum difference between zone and ambient CO2 concentration. The maximum varies depending on the applicable ventilation standard, Standard 62.1 and Title 24. The designer may also decide to set lower, more conservative setpoints for improved indoor air quality but at the expense of …
- **Textual difference:** replace: 2021 [3.1.1.3. CO2 Setpoints Space CO2 setpoints are used for demand-controlled ventilation (DCV) and monitoring/alarming as required by LEED and other green] -> 2024 [3.1.1.3. CO2 Maximum Concentration Space CO2 sensors are used for demand-controlled ventilation (DCV) as required by energy standards such as ASHRAE Standard] | replace: 2021 [3.1.1.3. CO2 Setpoints Space CO2 setpoints are used for demand-controlled ventilation (DCV) and monitoring/alarming as required by LEED and other green building standards. It] -> 2024 [3.1.1.3. CO2 Maximum Concentration Space CO2 sensors are used for demand-controlled ventilation (DCV) as required by energy standards such as ASHRAE Standard 90.1 and California] | insert: 2021 [3.1.1.3. CO2 Setpoints Space CO2 setpoints are used for demand-controlled ventilation (DCV) and monitoring/alarming …
- **Operational interpretation:** Revises demand controlled ventilation calculations to be consistent with ASHRAE Standard 62.1 and California Title 24.. The affected behavior should be confirmed against the full section and controlled addendum source before implementation.

### Section 5.2.1.3
- **2021 reference:** PDF page(s) 59
- **2024 reference:** PDF page(s) 66, 67, 68, 69, 70, 71
- **2021 excerpt:** 5.2.1.3. For compliance with the Ventilation Rate Procedure of ASHRAE Standard 62.1-2016, outdoor air and zone minimum setpoints shall be calculated as follows: a. See Section 3.1.1.2 for zone ventilation setpoints. b. Determine zone air distribution effectiveness Ez. 1. If the DAT at the terminal unit is less than or equal to zone space temperature, Ez shall be equal to EzC (default to 1.0 if no value is scheduled). 2. If the DAT at the terminal unit is greater than zone space temperature, Ez shall be equal to EzH (default to 0.8 if no value is scheduled). c. Vbz-P* is the population component of the required breathing zone outdoor airflow. …
- **2024 excerpt:** 5.2.1.3. For compliance with the Ventilation Rate Procedure of ASHRAE Standard 62.1, outdoor air and zone minimum setpoints shall be calculated as follows: a. See Section 3.1.1.2 for zone ventilation setpoints. b. VAV Terminal Units 1. Determine zone air distribution effectiveness Ez. i. If the DAT at the terminal unit is less than or equal to zone space temperature, Ez shall be equal to EzC (default to 1.0 if no value is scheduled). ii. If the DAT at the terminal unit is greater than zone space temperature, Ez shall be equal to EzH (default to 0.8 if no value is scheduled). 2. Vbz-P* is the population component of the required breathing …
- **Textual difference:** replace: 2021 [5.2.1.3. For compliance with the Ventilation Rate Procedure of ASHRAE Standard 62.1-2016, outdoor air and zone minimum setpoints shall be calculated as follows: a. See Section 3.1.1.2 for zone ventilation] -> 2024 [5.2.1.3. For compliance with the Ventilation Rate Procedure of ASHRAE Standard 62.1, outdoor air and zone minimum setpoints shall be calculated as follows: a. See Section 3.1.1.2 for zone ventilation] | insert: 2021 [and zone minimum setpoints shall be calculated as follows: a. See Section 3.1.1.2 for zone ventilation setpoints. b. Determine zone air distribution effectiveness Ez. 1. If the DAT at the terminal unit is less than or] -> 2024 [and zone minimum setpoints shall be calculated as follows: a. See Section 3.1.1.2 for zone ventilation setpoints. b. VAV Terminal Units 1. Determine zone air distribution …
- **Operational interpretation:** Revises demand controlled ventilation calculations to be consistent with ASHRAE Standard 62.1 and California Title 24.. The affected behavior should be confirmed against the full section and controlled addendum source before implementation.

### Section 5.2.1.4
- **2021 reference:** PDF page(s) 63, 64, 65, 66
- **2024 reference:** PDF page(s) 71, 72, 73, 74
- **2021 excerpt:** 5.2.1.4. For compliance with California Title 24, outdoor air setpoints shall be calculated as follows: a. See Section 3.1.1.2 for zone ventilation setpoints. b. Determine the zone minimum outdoor air setpoints Zone-Abs-OA-min and Zone-Des-OA-min. Zone-Abs-OA-min is used in terminal-unit sequences and air-handler sequences. Zone-Des-OA-min is used in air- handler sequences only. 1. Zone-Abs-OA-min shall be reset based on the following conditions in order from highest to lowest priority: i. Zero if the zone has a window switch and the window is open. ii. Zero if the zone has an occupancy sensor and is unpopulated and is permitted to be in …
- **2024 excerpt:** 5.2.1.4. For compliance with California Title 24, outdoor airflow setpoints shall be calculated as follows: a. See Section 3.1.1.2 for zone ventilation setpoints. b. VAV Terminal Units 1. Determine the zone minimum outdoor airflow setpoints Zone-Abs-OA-min and Zone-Des-OA- min. Zone-Abs-OA-min is used in terminal-unit sequences and air-handler sequences. Zone-Des-OA-min is used in air- handler sequences only. i. Zone-Abs-OA-min shall be reset based on the following conditions in order from highest to lowest priority: (a) Zero if the zone has a window switch and the window is open. (b) Zero if the zone has an occupancy sensor and is …
- **Textual difference:** replace: 2021 [5.2.1.4. For compliance with California Title 24, outdoor air setpoints shall be calculated as follows: a. See Section 3.1.1.2 for zone ventilation setpoints. b. Determine the zone] -> 2024 [5.2.1.4. For compliance with California Title 24, outdoor airflow setpoints shall be calculated as follows: a. See Section 3.1.1.2 for zone ventilation setpoints. b. VAV Terminal Units] | insert: 2021 [24, outdoor air setpoints shall be calculated as follows: a. See Section 3.1.1.2 for zone ventilation setpoints. b. Determine the zone minimum outdoor air setpoints Zone-Abs-OA-min and Zone-Des-OA-min. Zone-Abs-OA-min is used in terminal-unit sequences and air-handler] -> 2024 [24, outdoor airflow setpoints shall be calculated as follows: a. See Section 3.1.1.2 for zone ventilation setpoints. b. VAV Terminal Units 1. Determine the zone …
- **Operational interpretation:** Revises demand controlled ventilation calculations to be consistent with ASHRAE Standard 62.1 and California Title 24.. The affected behavior should be confirmed against the full section and controlled addendum source before implementation.

### Section 5.2.3
- **2021 reference:** PDF page(s) not located
- **2024 reference:** PDF page(s) 75
- **2021 excerpt:** Not located in the supplied edition.
- **2024 excerpt:** 5.2.3. Zone Alarms 5.2.3.1. For zones with CO2 sensors: a. If the CO2 concentration is less than 300 ppm, or the zone is in Unoccupied Mode for more than 2 hours and zone CO2 concentration exceeds 600 ppm, generate a Level 3 alarm. The alarm text shall identify the sensor and indicate that it may be out of calibration. b. If the CO2 concentration exceeds Cmax plus 10% for more than 10 minutes, generate a Level 3 alarm. Note that in some cases, alarms may be generated that do not necessarily indicate an indoor air quality problem or noncompliance with Standard 62.1. Cmax determined in accordance with Standard 62.1, including occupancy density …
- **Textual difference:** New section/content in 2024; no corresponding 2021 section was extracted.
- **Operational interpretation:** Revises demand controlled ventilation calculations to be consistent with ASHRAE Standard 62.1 and California Title 24.. The affected behavior should be confirmed against the full section and controlled addendum source before implementation.

## Reviewer notes
- The 2024 source is a consolidated edition; section differences cannot be attributed exclusively to this addendum without the controlled standalone addendum redline.
- System categories are engineering mappings from affected sections and descriptions; confirm against the official 2024 index.

## Validation
- Appendix C inventory row represented: **Pass**.
- All 4 listed section references represented: **Pass**.
- Systems and functional categories populated: **Pass with mapping limitation**.
- 2021-to-2024 evidence status: **Complete**.
- CDL implementation status: **Not assessed by this PDF-based workflow**.
