# ASHRAE Guideline 36-2024 Addendum w Report

## Inventory
- **Description:** Removes the need to update list of all parameters and setpoints referenced in each section.
- **ASHRAE approval date:** March 14, 2024
- **Affected sections:** 5.5.3; 5.6.3; 5.7.3; 5.8.3; 5.9.3; 5.10.3; 5.11.3; 5.12.3; 5.13.3; 5.14.3; 5.18.2; 5.18.3; 5.19.2.3; 5.20.1; 5.21.1; 5.22.2; 5.22.3
- **Appendix C PDF page(s):** 307

## Methodology and limitations
The supplied `addendum_a_analysis.py` extraction workflow was run in `--all` mode against the supplied 2021 and 2024 PDFs. It extracted Appendix C inventory rows and section-level evidence. The comparisons below use that evidence and normalized word-level alignment; they are not a substitute for the controlled standalone addendum redline. Because the 2024 PDF is consolidated, unrelated cumulative edits in an affected section are not independently attributed to this addendum.

## Impact classification
- **Systems impacted:** Single-zone VAV air handling units; Air handling units; VAV terminal units; Condenser-water systems; Central plants; Chilled-water plants; Hot-water plants; Hydronic distribution systems
- **Primary functional category:** Setpoint generation
- **Secondary functional categories:** Documentation or editorial correction
- **Comparison status:** Complete
- **Quality level:** Partially verified

## Section-level comparison
### Section 5.5.3
- **2021 reference:** PDF page(s) 73
- **2024 reference:** PDF page(s) 83
- **2021 excerpt:** 5.5.3. See Section 3.1.2.1 for zone minimum airflow setpoint Vmin, zone maximum cooling airflow setpoint Vcool-max, and zone maximum heating airflow setpoint Vheat-max. If the minimum ventilation rate is more than 25% or so of the cooling maximum, or DCV is used, a reheat box is recommended to avoid overcooling. DCV logic is not provided for cooling-only boxes, because doing so results in periods of overcooling, as the CO2 levels due to occupants rises much faster than the cooling load due to occupants because of thermal mass. Cooling-only terminal units can provide heating only when the AHU supply air temperature is more than 3°C (5°F) …
- **2024 excerpt:** 5.5.3. See Sections 3.1.1 and 3.1.2.1 for operating parameters and setpoints. If the minimum ventilation rate is more than 25% or so of the cooling maximum, or DCV is used, a reheat box is recommended to avoid overcooling. DCV logic is not provided for cooling-only boxes, because doing so results in periods of overcooling, as the CO2 levels due to occupants rises much faster than the cooling load due to occupants because of thermal mass. Cooling-only terminal units can provide heating only when the AHU supply air temperature is more than 3°C (5°F) above the room temperature.
- **Textual difference:** replace: 2021 [5.5.3. See Section 3.1.2.1 for zone minimum airflow setpoint Vmin, zone maximum cooling airflow setpoint Vcool-max, and zone maximum heating airflow] -> 2024 [5.5.3. See Sections 3.1.1 and 3.1.2.1 for operating parameters and setpoints. If the minimum ventilation rate is more than 25% or so of] | replace: 2021 [5.5.3. See Section 3.1.2.1 for zone minimum airflow setpoint Vmin, zone maximum cooling airflow setpoint Vcool-max, and zone maximum heating airflow setpoint Vheat-max. If the minimum ventilation rate is more than 25% or so] -> 2024 [5.5.3. See Sections 3.1.1 and 3.1.2.1 for operating parameters and setpoints. If the minimum ventilation rate is more than 25% or so of the cooling maximum, or] | replace: 2021 [5.5.3. See Section 3.1.2.1 for zone minimum airflow setpoint Vmin, zone maximum cooling airflow setpoint …
- **Operational interpretation:** Removes the need to update list of all parameters and setpoints referenced in each section.. The affected behavior should be confirmed against the full section and controlled addendum source before implementation.

### Section 5.6.3
- **2021 reference:** PDF page(s) 75
- **2024 reference:** PDF page(s) 86
- **2021 excerpt:** 5.6.3. See Section 3.1.2.2 for zone minimum airflow setpoints Vmin, zone maximum cooling airflow setpoint Vcool-max, zone maximum heating airflow setpoint Vheat-max, zone minimum heating airflow setpoint Vheat-min, and the maximum DAT rise above heating setpoint MaxT.
- **2024 excerpt:** 5.6.3. See Sections 3.1.1 and 3.1.2.2 for operating parameters and setpoints.
- **Textual difference:** replace: 2021 [5.6.3. See Section 3.1.2.2 for zone minimum airflow setpoints Vmin, zone maximum cooling airflow setpoint Vcool-max, zone maximum heating airflow setpoint] -> 2024 [5.6.3. See Sections 3.1.1 and 3.1.2.2 for operating parameters and setpoints.] | replace: 2021 [5.6.3. See Section 3.1.2.2 for zone minimum airflow setpoints Vmin, zone maximum cooling airflow setpoint Vcool-max, zone maximum heating airflow setpoint Vheat-max, zone minimum heating airflow setpoint Vheat-min, and the maximum DAT rise above heating setpoint MaxT.] -> 2024 [5.6.3. See Sections 3.1.1 and 3.1.2.2 for operating parameters and setpoints.] | replace: 2021 [maximum cooling airflow setpoint Vcool-max, zone maximum heating airflow setpoint Vheat-max, zone minimum heating airflow setpoint Vheat-min, and the maximum DAT rise above heating setpoint MaxT.] …
- **Operational interpretation:** Removes the need to update list of all parameters and setpoints referenced in each section.. The affected behavior should be confirmed against the full section and controlled addendum source before implementation.

### Section 5.7.3
- **2021 reference:** PDF page(s) 79
- **2024 reference:** PDF page(s) 90
- **2021 excerpt:** 5.7.3. See Section 3.1.2.3 for zone minimum airflow setpoint Vmin, zone maximum cooling airflow setpoint Vcool-max, and the maximum DAT rise above heating setpoint MaxT.
- **2024 excerpt:** 5.7.3. See Sections 3.1.1 and 3.1.2.3 for operating parameters and setpoints.
- **Textual difference:** replace: 2021 [5.7.3. See Section 3.1.2.3 for zone minimum airflow setpoint Vmin, zone maximum cooling airflow setpoint Vcool-max, and the maximum DAT rise] -> 2024 [5.7.3. See Sections 3.1.1 and 3.1.2.3 for operating parameters and setpoints.] | replace: 2021 [5.7.3. See Section 3.1.2.3 for zone minimum airflow setpoint Vmin, zone maximum cooling airflow setpoint Vcool-max, and the maximum DAT rise above heating setpoint MaxT.] -> 2024 [5.7.3. See Sections 3.1.1 and 3.1.2.3 for operating parameters and setpoints.] | replace: 2021 [5.7.3. See Section 3.1.2.3 for zone minimum airflow setpoint Vmin, zone maximum cooling airflow setpoint Vcool-max, and the maximum DAT rise above heating setpoint MaxT.] -> 2024 [5.7.3. See Sections 3.1.1 and 3.1.2.3 for operating parameters and
- **Operational interpretation:** Removes the need to update list of all parameters and setpoints referenced in each section.. The affected behavior should be confirmed against the full section and controlled addendum source before implementation.

### Section 5.8.3
- **2021 reference:** PDF page(s) 83
- **2024 reference:** PDF page(s) 95
- **2021 excerpt:** 5.8.3. See Section 3.1.2.4 for zone minimum airflow setpoint Vmin, zone maximum cooling airflow setpoint Vcool-max, the parallel fan maximum heating airflow setpoint Pfan-htgmax, and the maximum DAT rise above heating setpoint MaxT. 5.8.3.1. Pfan-z is the lowest rate at which the fan will operate when it is turned on but has the lowest possible speed signal from the BAS.
- **2024 excerpt:** 5.8.3. See Sections 3.1.1 and 3.1.2.4 for operating parameters and setpoints. 5.8.3.1. Pfan-z is the lowest rate at which the fan will operate when it is turned on but has the lowest possible speed signal from the BAS.
- **Textual difference:** replace: 2021 [5.8.3. See Section 3.1.2.4 for zone minimum airflow setpoint Vmin, zone maximum cooling airflow setpoint Vcool-max, the parallel fan maximum heating] -> 2024 [5.8.3. See Sections 3.1.1 and 3.1.2.4 for operating parameters and setpoints. 5.8.3.1. Pfan-z is the lowest rate at which the fan will operate] | replace: 2021 [5.8.3. See Section 3.1.2.4 for zone minimum airflow setpoint Vmin, zone maximum cooling airflow setpoint Vcool-max, the parallel fan maximum heating airflow setpoint Pfan-htgmax, and the maximum DAT rise above heating setpoint MaxT. 5.8.3.1. Pfan-z is the lowest rate at which the] -> 2024 [5.8.3. See Sections 3.1.1 and 3.1.2.4 for operating parameters and setpoints. 5.8.3.1. Pfan-z is the lowest rate at which the fan will operate when it is turned] | replace: 2021 [airflow setpoint Vmin, zone maximum cooling …
- **Operational interpretation:** Removes the need to update list of all parameters and setpoints referenced in each section.. The affected behavior should be confirmed against the full section and controlled addendum source before implementation.

### Section 5.9.3
- **2021 reference:** PDF page(s) 88
- **2024 reference:** PDF page(s) 100
- **2021 excerpt:** 5.9.3. See Section 3.1.2.5 for zone minimum airflow setpoints Vmin, zone maximum cooling airflow setpoint Vcool-max, and the maximum DAT rise above heating setpoint MaxT.
- **2024 excerpt:** 5.9.3. See Sections 3.1.1 and 3.1.2.5 for operating parameters and setpoints.
- **Textual difference:** replace: 2021 [5.9.3. See Section 3.1.2.5 for zone minimum airflow setpoints Vmin, zone maximum cooling airflow setpoint Vcool-max, and the maximum DAT rise] -> 2024 [5.9.3. See Sections 3.1.1 and 3.1.2.5 for operating parameters and setpoints.] | replace: 2021 [5.9.3. See Section 3.1.2.5 for zone minimum airflow setpoints Vmin, zone maximum cooling airflow setpoint Vcool-max, and the maximum DAT rise above heating setpoint MaxT.] -> 2024 [5.9.3. See Sections 3.1.1 and 3.1.2.5 for operating parameters and setpoints.] | replace: 2021 [5.9.3. See Section 3.1.2.5 for zone minimum airflow setpoints Vmin, zone maximum cooling airflow setpoint Vcool-max, and the maximum DAT rise above heating setpoint MaxT.] -> 2024 [5.9.3. See Sections 3.1.1 and 3.1.2.5 for operating parameters and
- **Operational interpretation:** Removes the need to update list of all parameters and setpoints referenced in each section.. The affected behavior should be confirmed against the full section and controlled addendum source before implementation.

### Section 5.10.3
- **2021 reference:** PDF page(s) 91
- **2024 reference:** PDF page(s) 104
- **2021 excerpt:** 5.10.3. See Section 3.1.2.6 for zone minimum airflow setpoint Vmin, zone maximum cooling airflow setpoint Vcool-max, the series fan maximum heating airflow Sfan-htgmax, and the maximum DAT rise above heating setpoint MaxT.
- **2024 excerpt:** 5.10.3. See Sections 3.1.1 and 3.1.2.6 for operating parameters and setpoints.
- **Textual difference:** replace: 2021 [5.10.3. See Section 3.1.2.6 for zone minimum airflow setpoint Vmin, zone maximum cooling airflow setpoint Vcool-max, the series fan maximum heating] -> 2024 [5.10.3. See Sections 3.1.1 and 3.1.2.6 for operating parameters and setpoints.] | replace: 2021 [5.10.3. See Section 3.1.2.6 for zone minimum airflow setpoint Vmin, zone maximum cooling airflow setpoint Vcool-max, the series fan maximum heating airflow Sfan-htgmax, and the maximum DAT rise above heating setpoint MaxT.] -> 2024 [5.10.3. See Sections 3.1.1 and 3.1.2.6 for operating parameters and setpoints.] | replace: 2021 [minimum airflow setpoint Vmin, zone maximum cooling airflow setpoint Vcool-max, the series fan maximum heating airflow Sfan-htgmax, and the maximum DAT rise above heating setpoint MaxT.] -> 2024 [5.10.3. See Sections 3.1.1 and 3.1.2.6 for …
- **Operational interpretation:** Removes the need to update list of all parameters and setpoints referenced in each section.. The affected behavior should be confirmed against the full section and controlled addendum source before implementation.

### Section 5.11.3
- **2021 reference:** PDF page(s) 95
- **2024 reference:** PDF page(s) 109
- **2021 excerpt:** 5.11.3. See Section 3.1.2.7 for zone minimum airflow setpoint Vmin, maximum cooling airflow setpoint Vcool-max, and the zone maximum heating airflow setpoint Vheat-max.
- **2024 excerpt:** 5.11.3. See Sections 3.1.1 and 3.1.2.7 for operating parameters and setpoints.
- **Textual difference:** replace: 2021 [5.11.3. See Section 3.1.2.7 for zone minimum airflow setpoint Vmin, maximum cooling airflow setpoint Vcool-max, and the zone maximum heating airflow] -> 2024 [5.11.3. See Sections 3.1.1 and 3.1.2.7 for operating parameters and setpoints.] | replace: 2021 [5.11.3. See Section 3.1.2.7 for zone minimum airflow setpoint Vmin, maximum cooling airflow setpoint Vcool-max, and the zone maximum heating airflow setpoint Vheat-max.] -> 2024 [5.11.3. See Sections 3.1.1 and 3.1.2.7 for operating parameters and setpoints.] | replace: 2021 [5.11.3. See Section 3.1.2.7 for zone minimum airflow setpoint Vmin, maximum cooling airflow setpoint Vcool-max, and the zone maximum heating airflow setpoint Vheat-max.] -> 2024 [5.11.3. See Sections 3.1.1 and 3.1.2.7 for operating parameters and
- **Operational interpretation:** Removes the need to update list of all parameters and setpoints referenced in each section.. The affected behavior should be confirmed against the full section and controlled addendum source before implementation.

### Section 5.12.3
- **2021 reference:** PDF page(s) 100
- **2024 reference:** PDF page(s) 114
- **2021 excerpt:** 5.12.3. See Section 3.1.2.7 for zone minimum airflow setpoint Vmin, zone maximum cooling airflow setpoint Vcool-max, and the zone maximum heating airflow setpoint Vheat-max.
- **2024 excerpt:** 5.12.3. See Sections 3.1.1 and 3.1.2.7 for operating parameters and setpoints.
- **Textual difference:** replace: 2021 [5.12.3. See Section 3.1.2.7 for zone minimum airflow setpoint Vmin, zone maximum cooling airflow setpoint Vcool-max, and the zone maximum heating] -> 2024 [5.12.3. See Sections 3.1.1 and 3.1.2.7 for operating parameters and setpoints.] | replace: 2021 [5.12.3. See Section 3.1.2.7 for zone minimum airflow setpoint Vmin, zone maximum cooling airflow setpoint Vcool-max, and the zone maximum heating airflow setpoint Vheat-max.] -> 2024 [5.12.3. See Sections 3.1.1 and 3.1.2.7 for operating parameters and setpoints.] | replace: 2021 [5.12.3. See Section 3.1.2.7 for zone minimum airflow setpoint Vmin, zone maximum cooling airflow setpoint Vcool-max, and the zone maximum heating airflow setpoint Vheat-max.] -> 2024 [5.12.3. See Sections 3.1.1 and 3.1.2.7 for operating parameters and
- **Operational interpretation:** Removes the need to update list of all parameters and setpoints referenced in each section.. The affected behavior should be confirmed against the full section and controlled addendum source before implementation.

### Section 5.13.3
- **2021 reference:** PDF page(s) 104
- **2024 reference:** PDF page(s) 118
- **2021 excerpt:** 5.13.3. See Section 3.1.2.7 for zone minimum airflow setpoint Vmin, zone maximum cooling airflow setpoint Vcool-max, and the zone maximum heating airflow setpoint Vheat-max.
- **2024 excerpt:** 5.13.3. See Sections 3.1.1 and 3.1.2.7 for operating parameters and setpoints.
- **Textual difference:** replace: 2021 [5.13.3. See Section 3.1.2.7 for zone minimum airflow setpoint Vmin, zone maximum cooling airflow setpoint Vcool-max, and the zone maximum heating] -> 2024 [5.13.3. See Sections 3.1.1 and 3.1.2.7 for operating parameters and setpoints.] | replace: 2021 [5.13.3. See Section 3.1.2.7 for zone minimum airflow setpoint Vmin, zone maximum cooling airflow setpoint Vcool-max, and the zone maximum heating airflow setpoint Vheat-max.] -> 2024 [5.13.3. See Sections 3.1.1 and 3.1.2.7 for operating parameters and setpoints.] | replace: 2021 [5.13.3. See Section 3.1.2.7 for zone minimum airflow setpoint Vmin, zone maximum cooling airflow setpoint Vcool-max, and the zone maximum heating airflow setpoint Vheat-max.] -> 2024 [5.13.3. See Sections 3.1.1 and 3.1.2.7 for operating parameters and
- **Operational interpretation:** Removes the need to update list of all parameters and setpoints referenced in each section.. The affected behavior should be confirmed against the full section and controlled addendum source before implementation.

### Section 5.14.3
- **2021 reference:** PDF page(s) 108
- **2024 reference:** PDF page(s) 122
- **2021 excerpt:** 5.14.3. See Section 3.1.2.7 for zone minimum airflow setpoint Vmin, zone maximum cooling airflow setpoint Vcool-max, and the zone maximum heating airflow setpoint Vheat-max.
- **2024 excerpt:** 5.14.3. See Sections 3.1.1 and 3.1.2.7 for operating parameters and setpoints.
- **Textual difference:** replace: 2021 [5.14.3. See Section 3.1.2.7 for zone minimum airflow setpoint Vmin, zone maximum cooling airflow setpoint Vcool-max, and the zone maximum heating] -> 2024 [5.14.3. See Sections 3.1.1 and 3.1.2.7 for operating parameters and setpoints.] | replace: 2021 [5.14.3. See Section 3.1.2.7 for zone minimum airflow setpoint Vmin, zone maximum cooling airflow setpoint Vcool-max, and the zone maximum heating airflow setpoint Vheat-max.] -> 2024 [5.14.3. See Sections 3.1.1 and 3.1.2.7 for operating parameters and setpoints.] | replace: 2021 [5.14.3. See Section 3.1.2.7 for zone minimum airflow setpoint Vmin, zone maximum cooling airflow setpoint Vcool-max, and the zone maximum heating airflow setpoint Vheat-max.] -> 2024 [5.14.3. See Sections 3.1.1 and 3.1.2.7 for operating parameters and
- **Operational interpretation:** Removes the need to update list of all parameters and setpoints referenced in each section.. The affected behavior should be confirmed against the full section and controlled addendum source before implementation.

### Section 5.18.2
- **2021 reference:** PDF page(s) 152
- **2024 reference:** PDF page(s) 171
- **2021 excerpt:** 5.18.2. See Section 3.1.6.1 for Cool_SAT, Heat_SAT, and MaxDPT.
- **2024 excerpt:** 5.18.2. See Sections 3.1.1 and 3.2.2 for operating parameters and setpoints.
- **Textual difference:** replace: 2021 [5.18.2. See Section 3.1.6.1 for Cool_SAT, Heat_SAT, and MaxDPT.] -> 2024 [5.18.2. See Sections 3.1.1 and 3.2.2 for operating parameters and setpoints.] | replace: 2021 [5.18.2. See Section 3.1.6.1 for Cool_SAT, Heat_SAT, and MaxDPT.] -> 2024 [5.18.2. See Sections 3.1.1 and 3.2.2 for operating parameters and setpoints.] | replace: 2021 [5.18.2. See Section 3.1.6.1 for Cool_SAT, Heat_SAT, and MaxDPT.] -> 2024 [5.18.2. See Sections 3.1.1 and 3.2.2 for operating parameters and
- **Operational interpretation:** Removes the need to update list of all parameters and setpoints referenced in each section.. The affected behavior should be confirmed against the full section and controlled addendum source before implementation.

### Section 5.18.3
- **2021 reference:** PDF page(s) 152
- **2024 reference:** PDF page(s) 171
- **2021 excerpt:** 5.18.3. See Section 3.2.2 for MinSpeed, MaxHeatSpeed, MaxCoolSpeed, MinPosMin, MinPosMax, DesPosMin, DesPosMax, MinRelief, MaxRelief, and S-R-DIFF.
- **2024 excerpt:** 5.18.3. Not Used
- **Textual difference:** replace: 2021 [5.18.3. See Section 3.2.2 for MinSpeed, MaxHeatSpeed, MaxCoolSpeed, MinPosMin, MinPosMax, DesPosMin, DesPosMax, MinRelief, MaxRelief, and S-R-DIFF.] -> 2024 [5.18.3. Not
- **Operational interpretation:** Removes the need to update list of all parameters and setpoints referenced in each section.. The affected behavior should be confirmed against the full section and controlled addendum source before implementation.

### Section 5.19.2.3
- **2021 reference:** PDF page(s) not located
- **2024 reference:** PDF page(s) 190
- **2021 excerpt:** Not located in the supplied edition.
- **2024 excerpt:** 5.19.2.3. See Section 5.3.6 for zone temperature alarms.
- **Textual difference:** New section/content in 2024; no corresponding 2021 section was extracted.
- **Operational interpretation:** Removes the need to update list of all parameters and setpoints referenced in each section.. The affected behavior should be confirmed against the full section and controlled addendum source before implementation.

### Section 5.20.1
- **2021 reference:** PDF page(s) 172
- **2024 reference:** PDF page(s) 190
- **2021 excerpt:** 5.20.1. See Section 3.1.7 for CHWSTminX, CWRTdesX, CWSTdesX, CH-LOT, CHW-MinFlowX, CHW- DesFlowX, LIFTminX, LIFTmaxX, QchX, PCHWFdesign, SCHWFdesign, MinUnloadCapX, DAHX, DTWB, DACT, HXFdesign, and HXDP-Design. See Section 3.2.3 for CHW-DPmax, LocalCHW-DPmax, Cw- DesPumpSpdStage, MinCWVlvPos, MinCWPspeed, HxPumpDesSpd, Ch-MaxPriPumpSpdStage, and CH-MinPriPumpSpdStage.
- **2024 excerpt:** 5.20.1. See Sections 3.1.7 and 3.2.3 for operating parameters and setpoints.
- **Textual difference:** replace: 2021 [5.20.1. See Section 3.1.7 for CHWSTminX, CWRTdesX, CWSTdesX, CH-LOT, CHW-MinFlowX, CHW- DesFlowX, LIFTminX, LIFTmaxX, QchX, PCHWFdesign, SCHWFdesign, MinUnloadCapX, DAHX, DTWB, DACT,] -> 2024 [5.20.1. See Sections 3.1.7 and 3.2.3 for operating parameters and setpoints.] | delete: 2021 [5.20.1. See Section 3.1.7 for CHWSTminX, CWRTdesX, CWSTdesX, CH-LOT, CHW-MinFlowX, CHW- DesFlowX, LIFTminX, LIFTmaxX, QchX, PCHWFdesign, SCHWFdesign, MinUnloadCapX, DAHX, DTWB, DACT, HXFdesign, and HXDP-Design. See Section 3.2.3 for CHW-DPmax, LocalCHW-DPmax, Cw- DesPumpSpdStage, MinCWVlvPos, MinCWPspeed, HxPumpDesSpd, Ch-MaxPriPumpSpdStage, and CH-MinPriPumpSpdStage.] -> 2024 [5.20.1. See Sections 3.1.7 and 3.2.3 for operating parameters and setpoints.] | delete: 2021 [CHWSTminX, CWRTdesX, CWSTdesX, CH-LOT, CHW-MinFlowX, CHW- DesFlowX, …
- **Operational interpretation:** Removes the need to update list of all parameters and setpoints referenced in each section.. The affected behavior should be confirmed against the full section and controlled addendum source before implementation.

### Section 5.21.1
- **2021 reference:** PDF page(s) 235
- **2024 reference:** PDF page(s) 255
- **2021 excerpt:** 5.21.1. See Section 3.1.8 for HWSTmax, HW-LOT, HW-MinFlowX, HW-DesFlowX, QbX, B-FiringMinX, PHWFdesign, and SHWFdesign. See Section 3.2.4 for HW-DPmax, LocalHW-DPmax, and B- MinPriPumpSpdStage.
- **2024 excerpt:** 5.21.1. See Sections 3.1.8 and 3.2.4 for operating parameters and setpoints.
- **Textual difference:** replace: 2021 [5.21.1. See Section 3.1.8 for HWSTmax, HW-LOT, HW-MinFlowX, HW-DesFlowX, QbX, B-FiringMinX, PHWFdesign, and SHWFdesign. See Section 3.2.4 for HW-DPmax, LocalHW-DPmax, and] -> 2024 [5.21.1. See Sections 3.1.8 and 3.2.4 for operating parameters and setpoints.] | delete: 2021 [5.21.1. See Section 3.1.8 for HWSTmax, HW-LOT, HW-MinFlowX, HW-DesFlowX, QbX, B-FiringMinX, PHWFdesign, and SHWFdesign. See Section 3.2.4 for HW-DPmax, LocalHW-DPmax, and B- MinPriPumpSpdStage.] -> 2024 [5.21.1. See Sections 3.1.8 and 3.2.4 for operating parameters and setpoints.] | delete: 2021 [5.21.1. See Section 3.1.8 for HWSTmax, HW-LOT, HW-MinFlowX, HW-DesFlowX, QbX, B-FiringMinX, PHWFdesign, and SHWFdesign. See Section 3.2.4 for HW-DPmax, LocalHW-DPmax, and B- MinPriPumpSpdStage.] -> 2024 [5.21.1. See Sections 3.1.8 and 3.2.4 for operating …
- **Operational interpretation:** Removes the need to update list of all parameters and setpoints referenced in each section.. The affected behavior should be confirmed against the full section and controlled addendum source before implementation.

### Section 5.22.2
- **2021 reference:** PDF page(s) 262, 263
- **2024 reference:** PDF page(s) 282
- **2021 excerpt:** 5.22.2. See Section 3.1.7 for Cool_SAT, Heat_SAT, and DP100. © ASHRAE. Per international copyright law, additional reproduction, distribution, or transmission in either print or digital form is not permitted without ASHRAE's prior written permission. Copyright American Society of Heating, Refrigerating and Air-Conditioning Engine Provided by IHS Markit under license with ASHRAE - Uncontrolled Copy Licensee=BATTELLE PACIFIC NW DIVISION/5940137102, User=Devaprasad, Karthikeya Not for Resale, 01/27/2022 04:30:51 MST No reproduction or networking permitted without license from IHS Markit --`,,,,```,,,`,`,`,`````,,,``,`-`-`,,`,,`,`,,`--- === PDF …
- **2024 excerpt:** 5.22.2. See Sections 3.1.7 and 3.2.3 for operating parameters and setpoints.
- **Textual difference:** replace: 2021 [5.22.2. See Section 3.1.7 for Cool_SAT, Heat_SAT, and DP100. © ASHRAE. Per international copyright law, additional reproduction, distribution, or transmission in] -> 2024 [5.22.2. See Sections 3.1.7 and 3.2.3 for operating parameters and setpoints.] | insert: 2021 [5.22.2. See Section 3.1.7 for Cool_SAT, Heat_SAT, and DP100. © ASHRAE. Per international copyright law, additional reproduction, distribution, or transmission in either] -> 2024 [5.22.2. See Sections 3.1.7 and 3.2.3 for operating parameters and setpoints.] | replace: 2021 [5.22.2. See Section 3.1.7 for Cool_SAT, Heat_SAT, and DP100. © ASHRAE. Per international copyright law, additional reproduction, distribution, or transmission in either print or digital] -> 2024 [5.22.2. See Sections 3.1.7 and 3.2.3 for operating parameters and setpoints.] | replace: 2021 …
- **Operational interpretation:** Removes the need to update list of all parameters and setpoints referenced in each section.. The affected behavior should be confirmed against the full section and controlled addendum source before implementation.

### Section 5.22.3
- **2021 reference:** PDF page(s) 263
- **2024 reference:** PDF page(s) 282
- **2021 excerpt:** 5.22.3. See Section 3.2.3 for MinSpeed, DeadbandSpeed, MaxHeatSpeed, and MaxCoolSpeed.
- **2024 excerpt:** 5.22.3. Not Used
- **Textual difference:** replace: 2021 [5.22.3. See Section 3.2.3 for MinSpeed, DeadbandSpeed, MaxHeatSpeed, and MaxCoolSpeed.] -> 2024 [5.22.3. Not
- **Operational interpretation:** Removes the need to update list of all parameters and setpoints referenced in each section.. The affected behavior should be confirmed against the full section and controlled addendum source before implementation.

## Reviewer notes
- The 2024 source is a consolidated edition; section differences cannot be attributed exclusively to this addendum without the controlled standalone addendum redline.
- System categories are engineering mappings from affected sections and descriptions; confirm against the official 2024 index.

## Validation
- Appendix C inventory row represented: **Pass**.
- All 17 listed section references represented: **Pass**.
- Systems and functional categories populated: **Pass with mapping limitation**.
- 2021-to-2024 evidence status: **Complete**.
- CDL implementation status: **Not assessed by this PDF-based workflow**.
