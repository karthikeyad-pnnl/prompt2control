# ASHRAE Guideline 36-2024 Addendum n Report

## Inventory
- **Description:** Addition to allow fans to cycle off during occupied-standby mode for fan-powered terminal units and single zone VAV air handling units.
- **ASHRAE approval date:** August 30, 2024
- **Affected sections:** 5.7.5.5; 5.8.5.1; 5.8.5.2; 5.9.5.5; 5.10.5.5; 5.18.4.1
- **Appendix C PDF page(s):** 307

## Methodology and limitations
The supplied `addendum_a_analysis.py` extraction workflow was run in `--all` mode against the supplied 2021 and 2024 PDFs. It extracted Appendix C inventory rows and section-level evidence. The comparisons below use that evidence and normalized word-level alignment; they are not a substitute for the controlled standalone addendum redline. Because the 2024 PDF is consolidated, unrelated cumulative edits in an affected section are not independently attributed to this addendum.

## Impact classification
- **Systems impacted:** Single-zone VAV air handling units; Air handling units; VAV terminal units; Fan-powered terminal units
- **Primary functional category:** Mode or state logic
- **Secondary functional categories:** Equipment enable/disable, Process control
- **Comparison status:** Complete
- **Quality level:** Partially verified

## Section-level comparison
### Section 5.7.5.5
- **2021 reference:** PDF page(s) 81
- **2024 reference:** PDF page(s) 92
- **2021 excerpt:** 5.7.5.5. Fan Control a. Fan shall run whenever Zone State is heating. b. If ventilation is according to ASHRAE Standard 62.1-2016, the fan shall run in Deadband and Cooling when the primary air volume is less than Voz for 1 minute and shall shut off when primary air volume is above Voz by 10% for 3 minutes. c. If ventilation is according to California Title 24, the fan shall run in Deadband and Cooling when the primary air volume is less than Zone-Abs-OA-min for 1 minute, and shall shut off when primary air volume is above Zone-Abs-OA-min by 10% for 3 minutes. The designer must ensure that the sum of the indirect ventilation provided by the …
- **2024 excerpt:** 5.7.5.5. Fan Control a. Fan shall run whenever Zone State is heating. b. If ventilation is according to ASHRAE Standard 62.1, in Occupied Mode only, the fan shall run in Deadband and Cooling when both of the following conditions are true for 1 minute: Voz is greater than zero and the primary airflow is less than Voz. The fan shall be disabled when either of the following conditions are true for 3 minutes: Voz is equal to zero or primary airflow is above Voz by 10%. c. If ventilation is according to California Title 24, in Occupied Mode only, the fan shall run in Deadband and Cooling when both of the following conditions are true for 1 …
- **Textual difference:** replace: 2021 [Control a. Fan shall run whenever Zone State is heating. b. If ventilation is according to ASHRAE Standard 62.1-2016, the fan shall run in Deadband and Cooling when the primary air volume is less than Voz for] -> 2024 [Control a. Fan shall run whenever Zone State is heating. b. If ventilation is according to ASHRAE Standard 62.1, in Occupied Mode only, the fan shall run in Deadband and Cooling when both of the following conditions are true for 1] | insert: 2021 [b. If ventilation is according to ASHRAE Standard 62.1-2016, the fan shall run in Deadband and Cooling when the primary air volume is less than Voz for 1 minute and shall shut off when primary air] -> 2024 [according to ASHRAE Standard 62.1, in Occupied Mode only, the fan shall run in Deadband and Cooling when both of the following conditions are true for 1 minute: …
- **Operational interpretation:** Addition to allow fans to cycle off during occupied-standby mode for fan-powered terminal units and single zone VAV air handling units.. The affected behavior should be confirmed against the full section and controlled addendum source before implementation.

### Section 5.8.5.1
- **2021 reference:** PDF page(s) 84, 85
- **2024 reference:** PDF page(s) 96, 97
- **2021 excerpt:** 5.8.5.1. When the Zone State Is Cooling a. The cooling-loop output shall be mapped to the active airflow setpoint from the minimum endpoint to the cooling maximum endpoint. Discharge Air Temperature Setpoint Heating Loop Signal Cooling Loop Signal Active Primary Airflow Setpoint, Vspt Minimum Cooling Maximum Pfan-htgmax Total CFM (not directly controlled) Pfan-z OA-min Parallel Fan Airflow Setpoint Deadband © ASHRAE. Per international copyright law, additional reproduction, distribution, or transmission in either print or digital form is not permitted without ASHRAE's prior written permission. Copyright American Society of Heating, …
- **2024 excerpt:** 5.8.5.1. When the Zone State Is Cooling a. The cooling-loop output shall be mapped to the active airflow setpoint from the minimum endpoint to the cooling maximum endpoint. 1. If supply air temperature from the air handler is greater than room temperature, the active primary airflow setpoint shall be no higher than the minimum endpoint. b. Heating coil is OFF. c. If ventilation is according to ASHRAE Standard 62.1, in Occupied Mode only, the fan shall run when both of the following conditions are true for 1 minute: Voz is greater than zero and the active primary airflow setpoint drops below Voz minus one half of Pfan-z. The fan shall be …
- **Textual difference:** delete: 2021 [output shall be mapped to the active airflow setpoint from the minimum endpoint to the cooling maximum endpoint. Discharge Air Temperature Setpoint Heating Loop Signal Cooling Loop Signal Active Primary Airflow Setpoint, Vspt Minimum Cooling Maximum Pfan-htgmax Total CFM (not directly controlled) Pfan-z OA-min Parallel Fan Airflow Setpoint Deadband © ASHRAE. Per international copyright law, additional reproduction, distribution, or transmission in either print or digital form is not permitted without ASHRAE's prior written permission. Copyright American Society of Heating, Refrigerating and Air-Conditioning Engine Provided by IHS Markit under license with ASHRAE - Uncontrolled Copy Licensee=BATTELLE PACIFIC NW DIVISION/5940137102, User=Devaprasad, Karthikeya Not for Resale, 01/27/2022 04:30:51 MST No reproduction or …
- **Operational interpretation:** Addition to allow fans to cycle off during occupied-standby mode for fan-powered terminal units and single zone VAV air handling units.. The affected behavior should be confirmed against the full section and controlled addendum source before implementation.

### Section 5.8.5.2
- **2021 reference:** PDF page(s) 85
- **2024 reference:** PDF page(s) 97
- **2021 excerpt:** 5.8.5.2. When the Zone State Is Deadband a. The active primary airflow setpoint shall be the minimum endpoint. b. Heating coil is OFF. c. If ventilation is according to ASHRAE Standard 62.1-2016, parallel fan runs if the active primary airflow setpoint is below Voz. Fan airflow rate setpoint is equal to Voz minus the active primary airflow setpoint. d. If ventilation is according to California Title 24, in Occupied Mode only, parallel fan runs if the active primary airflow setpoint is below Zone-Abs-OA-min. Fan airflow rate setpoint is equal to Zone-Abs-OA-min minus the active primary airflow setpoint. The designer must ensure that the sum …
- **2024 excerpt:** 5.8.5.2. When the Zone State Is Deadband a. The active primary airflow setpoint shall be the minimum endpoint. b. Heating coil is OFF. c. If ventilation is according to ASHRAE Standard 62.1, in Occupied Mode only, the fan shall run when both of the following conditions are true for 1 minute: Voz is greater than zero and the active primary airflow setpoint is below Voz. The fan shall be disabled when either of the following conditions are true for 3 minutes: Voz is equal to zero or the primary air setpoint is above Voz by 10%. The fan airflow rate setpoint shall be equal to Voz minus the active primary airflow setpoint. d. If ventilation is …
- **Textual difference:** replace: 2021 [shall be the minimum endpoint. b. Heating coil is OFF. c. If ventilation is according to ASHRAE Standard 62.1-2016, parallel fan runs if the active primary airflow setpoint is below Voz. Fan airflow rate setpoint is equal to] -> 2024 [shall be the minimum endpoint. b. Heating coil is OFF. c. If ventilation is according to ASHRAE Standard 62.1, in Occupied Mode only, the fan shall run when both of the following conditions are true for 1 minute: Voz is greater than] | replace: 2021 [minimum endpoint. b. Heating coil is OFF. c. If ventilation is according to ASHRAE Standard 62.1-2016, parallel fan runs if the active primary airflow setpoint is below Voz. Fan airflow rate setpoint is equal to Voz minus the] -> 2024 [coil is OFF. c. If ventilation is according to ASHRAE Standard 62.1, in Occupied Mode only, the fan shall run …
- **Operational interpretation:** Addition to allow fans to cycle off during occupied-standby mode for fan-powered terminal units and single zone VAV air handling units.. The affected behavior should be confirmed against the full section and controlled addendum source before implementation.

### Section 5.9.5.5
- **2021 reference:** PDF page(s) 89
- **2024 reference:** PDF page(s) 102
- **2021 excerpt:** 5.9.5.5. Fan Control. Fan shall run whenever zone is in heating or cooling Zone State, or if the associated Zone Group is in Occupied Mode. Prior to starting the fan, the damper is first driven fully closed to ensure that the fan is not rotating backward. Once the fan is proven ON for a fixed time delay (15 seconds), the damper override is released.
- **2024 excerpt:** 5.9.5.5. Fan Control. Fan shall run whenever zone is in heating or cooling Zone State, or if the associated Zone Group is in Occupied Mode and the active primary airflow setpoint, Vspt, is greater than zero. Prior to starting the fan, the damper is first driven fully closed to ensure that the fan is not rotating backward. Once the fan is proven ON for a fixed time delay (15 seconds), the damper override is released.
- **Textual difference:** replace: 2021 [whenever zone is in heating or cooling Zone State, or if the associated Zone Group is in Occupied Mode. Prior to starting the fan, the damper is first driven fully closed to ensure that the fan is] -> 2024 [whenever zone is in heating or cooling Zone State, or if the associated Zone Group is in Occupied Mode and the active primary airflow setpoint, Vspt, is greater than zero. Prior to starting the fan, the damper is first driven fully closed to ensure that the fan
- **Operational interpretation:** Addition to allow fans to cycle off during occupied-standby mode for fan-powered terminal units and single zone VAV air handling units.. The affected behavior should be confirmed against the full section and controlled addendum source before implementation.

### Section 5.10.5.5
- **2021 reference:** PDF page(s) 93
- **2024 reference:** PDF page(s) 106
- **2021 excerpt:** 5.10.5.5. Fan Control. Fan shall run whenever zone is in heating or cooling Zone State, or if the associated Zone Group is in Occupied Mode. Prior to starting the fan, the damper is first driven fully closed to ensure that the fan is not rotating backward. Once the fan is proven ON for a fixed time delay (15 seconds), the damper override is released.
- **2024 excerpt:** 5.10.5.5. Fan Control. Fan shall run whenever zone is in heating or cooling Zone State, or if the associated Zone Group is in Occupied Mode and the active primary airflow setpoint, Vspt, is greater than zero. Prior to starting the fan, the damper is first driven fully closed to ensure that the fan is not rotating backward. Once the fan is proven ON for a fixed time delay (15 seconds), the damper override is released.
- **Textual difference:** replace: 2021 [whenever zone is in heating or cooling Zone State, or if the associated Zone Group is in Occupied Mode. Prior to starting the fan, the damper is first driven fully closed to ensure that the fan is] -> 2024 [whenever zone is in heating or cooling Zone State, or if the associated Zone Group is in Occupied Mode and the active primary airflow setpoint, Vspt, is greater than zero. Prior to starting the fan, the damper is first driven fully closed to ensure that the fan
- **Operational interpretation:** Addition to allow fans to cycle off during occupied-standby mode for fan-powered terminal units and single zone VAV air handling units.. The affected behavior should be confirmed against the full section and controlled addendum source before implementation.

### Section 5.18.4.1
- **2021 reference:** PDF page(s) 153
- **2024 reference:** PDF page(s) 171
- **2021 excerpt:** 5.18.4.1. The supply fan shall run whenever the unit is in any mode other than Unoccupied Mode.
- **2024 excerpt:** 5.18.4.1. The supply fan shall run whenever the zone is in heating or cooling Zone State, or if the unit is in Occupied Mode and the minimum outdoor airflow setpoint, MinOAsp, is greater than zero.
- **Textual difference:** insert: 2021 [5.18.4.1. The supply fan shall run whenever the unit is in any mode other than Unoccupied Mode.] -> 2024 [5.18.4.1. The supply fan shall run whenever the zone is in heating or cooling Zone State, or if the unit is in Occupied Mode and the minimum outdoor airflow setpoint, MinOAsp, is greater than zero.] | replace: 2021 [5.18.4.1. The supply fan shall run whenever the unit is in any mode other than Unoccupied Mode.] -> 2024 [shall run whenever the zone is in heating or cooling Zone State, or if the unit is in Occupied Mode and the minimum outdoor airflow setpoint, MinOAsp, is greater than zero.] | replace: 2021 [5.18.4.1. The supply fan shall run whenever the unit is in any mode other than Unoccupied Mode.] -> 2024 [or if the unit is in Occupied Mode and the minimum outdoor airflow setpoint, MinOAsp, is greater than
- **Operational interpretation:** Addition to allow fans to cycle off during occupied-standby mode for fan-powered terminal units and single zone VAV air handling units.. The affected behavior should be confirmed against the full section and controlled addendum source before implementation.

## Reviewer notes
- The 2024 source is a consolidated edition; section differences cannot be attributed exclusively to this addendum without the controlled standalone addendum redline.
- System categories are engineering mappings from affected sections and descriptions; confirm against the official 2024 index.

## Validation
- Appendix C inventory row represented: **Pass**.
- All 6 listed section references represented: **Pass**.
- Systems and functional categories populated: **Pass with mapping limitation**.
- 2021-to-2024 evidence status: **Complete**.
- CDL implementation status: **Not assessed by this PDF-based workflow**.
