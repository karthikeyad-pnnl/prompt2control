# ASHRAE Guideline 36-2024 Addendum c Report

## Inventory
- **Description:** Addresses an issue with the minimum outdoor airflow setpoint logic for ASHRAE Standard 62.1 ventilation. Relocates the Zpz calculation from the Multiple Zone VAV Air Handling Unit section to the Generic Ventilation Zones section.
- **ASHRAE approval date:** March 14, 2024
- **Affected sections:** 5.2.1.3; 5.16.3.1
- **Appendix C PDF page(s):** 306

## Methodology and limitations
The supplied `addendum_a_analysis.py` extraction workflow was run in `--all` mode against the supplied 2021 and 2024 PDFs. It extracted Appendix C inventory rows and section-level evidence. The comparisons below use that evidence and normalized word-level alignment; they are not a substitute for the controlled standalone addendum redline. Because the 2024 PDF is consolidated, unrelated cumulative edits in an affected section are not independently attributed to this addendum.

## Impact classification
- **Systems impacted:** Ventilation systems; Air handling units; Multiple-zone VAV air handling units
- **Primary functional category:** Ventilation control
- **Secondary functional categories:** Outdoor-air control, Setpoint generation, Documentation or editorial correction
- **Comparison status:** Complete
- **Quality level:** Partially verified

## Section-level comparison
### Section 5.2.1.3
- **2021 reference:** PDF page(s) 59
- **2024 reference:** PDF page(s) 66, 67, 68, 69, 70, 71
- **2021 excerpt:** 5.2.1.3. For compliance with the Ventilation Rate Procedure of ASHRAE Standard 62.1-2016, outdoor air and zone minimum setpoints shall be calculated as follows: a. See Section 3.1.1.2 for zone ventilation setpoints. b. Determine zone air distribution effectiveness Ez. 1. If the DAT at the terminal unit is less than or equal to zone space temperature, Ez shall be equal to EzC (default to 1.0 if no value is scheduled). 2. If the DAT at the terminal unit is greater than zone space temperature, Ez shall be equal to EzH (default to 0.8 if no value is scheduled). c. Vbz-P* is the population component of the required breathing zone outdoor airflow. …
- **2024 excerpt:** 5.2.1.3. For compliance with the Ventilation Rate Procedure of ASHRAE Standard 62.1, outdoor air and zone minimum setpoints shall be calculated as follows: a. See Section 3.1.1.2 for zone ventilation setpoints. b. VAV Terminal Units 1. Determine zone air distribution effectiveness Ez. i. If the DAT at the terminal unit is less than or equal to zone space temperature, Ez shall be equal to EzC (default to 1.0 if no value is scheduled). ii. If the DAT at the terminal unit is greater than zone space temperature, Ez shall be equal to EzH (default to 0.8 if no value is scheduled). 2. Vbz-P* is the population component of the required breathing …
- **Textual difference:** replace: 2021 [5.2.1.3. For compliance with the Ventilation Rate Procedure of ASHRAE Standard 62.1-2016, outdoor air and zone minimum setpoints shall be calculated as follows: a. See Section 3.1.1.2 for zone ventilation] -> 2024 [5.2.1.3. For compliance with the Ventilation Rate Procedure of ASHRAE Standard 62.1, outdoor air and zone minimum setpoints shall be calculated as follows: a. See Section 3.1.1.2 for zone ventilation] | insert: 2021 [and zone minimum setpoints shall be calculated as follows: a. See Section 3.1.1.2 for zone ventilation setpoints. b. Determine zone air distribution effectiveness Ez. 1. If the DAT at the terminal unit is less than or] -> 2024 [and zone minimum setpoints shall be calculated as follows: a. See Section 3.1.1.2 for zone ventilation setpoints. b. VAV Terminal Units 1. Determine zone air distribution …
- **Operational interpretation:** Addresses an issue with the minimum outdoor airflow setpoint logic for ASHRAE Standard 62.1 ventilation. Relocates the Zpz calculation from the Multiple Zone VAV Air Handling Unit section to the Generic Ventilation Zones section.. The affected behavior should be confirmed against the full section and controlled addendum source before implementation.

### Section 5.16.3.1
- **2021 reference:** PDF page(s) 117, 118
- **2024 reference:** PDF page(s) 134, 135
- **2021 excerpt:** 5.16.3.1. Outdoor Airflow Setpoint for ASHRAE Standard 62.1-2016 Ventilation The CO2 DCV strategy for Standard 62.1 currently increases both the zone primary airflow and the population component of the breathing zone outdoor airflow in response to increasing CO2 concentrations. Through the dynamic implementation of the Standard 62.1 Multiple Spaces Equation (see Vou and Ev calculations in this section), the minimum outdoor airflow setpoint is adjusted accordingly in tandem with the zone DCV response. Though this combined response increases ventilation with rising CO2 concentrations, it is not strictly adherent with Standard 62.1. ASHRAE …
- **2024 excerpt:** 5.16.3.1. Outdoor Airflow Setpoint for ASHRAE Standard 62.1 Ventilation The CO2 DCV strategy for Standard 62.1 currently increases both the zone primary airflow and the population component of the breathing zone outdoor airflow in response to increasing CO2 concentrations. Through the dynamic implementation of the Standard 62.1 Multiple Spaces Equation (see Vou and Ev calculations in this section), the minimum outdoor airflow setpoint is adjusted accordingly in tandem with the zone DCV response. Though this combined response increases ventilation with rising CO2 concentrations, it is not strictly adherent with Standard 62.1. ASHRAE research …
- **Textual difference:** replace: 2021 [5.16.3.1. Outdoor Airflow Setpoint for ASHRAE Standard 62.1-2016 Ventilation The CO2 DCV strategy for Standard 62.1 currently increases both the zone primary airflow and the population] -> 2024 [5.16.3.1. Outdoor Airflow Setpoint for ASHRAE Standard 62.1 Ventilation The CO2 DCV strategy for Standard 62.1 currently increases both the zone primary airflow and the population] | replace: 2021 [the guideline pending further confirmation of its stability in real-world applications. a. See Section 5.2.1.3 for zone outdoor air requirement Voz. b. See Section 3.1.4.2.a for setpoints DesVou and DesVot. The following logic solves the Standard 62.1 multiple-spaces] -> 2024 [the guideline pending further confirmation of its stability in real-world applications. a. See Section 5.2.1.3 for zone outdoor airflow requirement, Voz. b. See …
- **Operational interpretation:** Addresses an issue with the minimum outdoor airflow setpoint logic for ASHRAE Standard 62.1 ventilation. Relocates the Zpz calculation from the Multiple Zone VAV Air Handling Unit section to the Generic Ventilation Zones section.. The affected behavior should be confirmed against the full section and controlled addendum source before implementation.

## Reviewer notes
- The 2024 source is a consolidated edition; section differences cannot be attributed exclusively to this addendum without the controlled standalone addendum redline.
- System categories are engineering mappings from affected sections and descriptions; confirm against the official 2024 index.

## Validation
- Appendix C inventory row represented: **Pass**.
- All 2 listed section references represented: **Pass**.
- Systems and functional categories populated: **Pass with mapping limitation**.
- 2021-to-2024 evidence status: **Complete**.
- CDL implementation status: **Not assessed by this PDF-based workflow**.
