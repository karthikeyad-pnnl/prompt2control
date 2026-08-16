# ASHRAE Guideline 36-2024 Addendum j Report

## Inventory
- **Description:** Separates the ventilation logic for the Single Zone VAV Air Handling Units and VAV terminal units in the generic ventilation zones section.
- **ASHRAE approval date:** February 29, 2024
- **Affected sections:** 5.2.1
- **Appendix C PDF page(s):** 306

## Methodology and limitations
The supplied `addendum_a_analysis.py` extraction workflow was run in `--all` mode against the supplied 2021 and 2024 PDFs. It extracted Appendix C inventory rows and section-level evidence. The comparisons below use that evidence and normalized word-level alignment; they are not a substitute for the controlled standalone addendum redline. Because the 2024 PDF is consolidated, unrelated cumulative edits in an affected section are not independently attributed to this addendum.

## Impact classification
- **Systems impacted:** Ventilation systems; Air handling units; Multiple-zone VAV air handling units
- **Primary functional category:** Ventilation control
- **Secondary functional categories:** Outdoor-air control
- **Comparison status:** Complete
- **Quality level:** Partially verified

## Section-level comparison
### Section 5.2.1
- **2021 reference:** PDF page(s) 59
- **2024 reference:** PDF page(s) 66, 67, 68, 69, 70, 71, 72, 73, 74
- **2021 excerpt:** 5.2.1. Zone Minimum Outdoor Air and Minimum Airflow Setpoints 5.2.1.1. For every zone that requires mechanical ventilation, the zone minimum outdoor airflows and setpoints shall be calculated depending on the governing standard or code for outdoor air requirements. 5.2.1.2. See Section 3.1.2 for zone minimum airflow setpoint Vmin. The engineer must select between ventilation logic options: If the project is to comply with ASHRAE Standard 62.1 ventilation requirements, use Section 5.2.1.3 and delete Section 5.2.1.4. If the project is to comply with California Title 24 ventilation requirements, use Section 5.2.1.4 and delete Section 5.2.1.3. …
- **2024 excerpt:** 5.2.1. Zone Minimum Outdoor Airflow and Minimum Airflow Setpoints 5.2.1.1. For every zone that requires mechanical ventilation, the zone minimum outdoor airflows and setpoints shall be calculated depending on the governing standard or code for outdoor air requirements. 5.2.1.2. For VAV terminal units, see Section 3.1.2 for zone minimum airflow setpoint Vmin. The engineer must select between ventilation logic options: If the project is to comply with ASHRAE Standard 62.1 ventilation requirements, use Section 5.2.1.3 and delete Section 5.2.1.4. If the project is to comply with California Title 24 ventilation requirements, use Section 5.2.1.4 …
- **Textual difference:** replace: 2021 [5.2.1. Zone Minimum Outdoor Air and Minimum Airflow Setpoints 5.2.1.1. For every zone that requires mechanical ventilation, the zone minimum outdoor airflows and] -> 2024 [5.2.1. Zone Minimum Outdoor Airflow and Minimum Airflow Setpoints 5.2.1.1. For every zone that requires mechanical ventilation, the zone minimum outdoor airflows and] | replace: 2021 [airflows and setpoints shall be calculated depending on the governing standard or code for outdoor air requirements. 5.2.1.2. See Section 3.1.2 for zone minimum airflow setpoint Vmin. The engineer must select between ventilation logic options: If the] -> 2024 [airflows and setpoints shall be calculated depending on the governing standard or code for outdoor air requirements. 5.2.1.2. For VAV terminal units, see Section 3.1.2 for zone minimum airflow setpoint Vmin. The …
- **Operational interpretation:** Separates the ventilation logic for the Single Zone VAV Air Handling Units and VAV terminal units in the generic ventilation zones section.. The affected behavior should be confirmed against the full section and controlled addendum source before implementation.

## Reviewer notes
- The 2024 source is a consolidated edition; section differences cannot be attributed exclusively to this addendum without the controlled standalone addendum redline.
- System categories are engineering mappings from affected sections and descriptions; confirm against the official 2024 index.

## Validation
- Appendix C inventory row represented: **Pass**.
- All 1 listed section references represented: **Pass**.
- Systems and functional categories populated: **Pass with mapping limitation**.
- 2021-to-2024 evidence status: **Complete**.
- CDL implementation status: **Not assessed by this PDF-based workflow**.
