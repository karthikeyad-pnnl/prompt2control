# ASHRAE Guideline 36-2024 Addendum v Report

## Inventory
- **Description:** Adds a way to establish different demand limit adjustments to different space types.
- **ASHRAE approval date:** March 14, 2024
- **Affected sections:** 3.1.1.1; 5.3.2.6; 5.3.2.7
- **Appendix C PDF page(s):** 307

## Methodology and limitations
The supplied `addendum_a_analysis.py` extraction workflow was run in `--all` mode against the supplied 2021 and 2024 PDFs. It extracted Appendix C inventory rows and section-level evidence. The comparisons below use that evidence and normalized word-level alignment; they are not a substitute for the controlled standalone addendum redline. Because the 2024 PDF is consolidated, unrelated cumulative edits in an affected section are not independently attributed to this addendum.

## Impact classification
- **Systems impacted:** Generic sequences or cross-system functions
- **Primary functional category:** Process control
- **Secondary functional categories:** None
- **Comparison status:** Complete
- **Quality level:** Partially verified

## Section-level comparison
### Section 3.1.1.1
- **2021 reference:** PDF page(s) 6
- **2024 reference:** PDF page(s) 6
- **2021 excerpt:** 3.1.1.1. Zone Temperature Setpoints Zone temperature initial setpoints can be specified by the designer in a number of ways. The most flexible way is to include them for each zone in variable-air-volume (VAV) box and single-zone VAV (SZVAV) air-handling unit (AHU) equipment schedules. They can also be generically listed by zone type, such as the example in (a) below. a. Default setpoints shall be based on zone type as shown in Table 3.1.1.1. Table 3.1.1.1 Default Setpoints Zone Type Occupied Unoccupied Heating Cooling Heating Cooling VAV 21°C (70°F) 24°C (75°F) 16°C (60°F) 32°C (90°F) Mechanical/electrical rooms 18°C (65°F) 29°C (85°F) 18°C …
- **2024 excerpt:** 3.1.1.1. Zone Temperature Setpoints Zone temperature initial setpoints can be specified by the designer in a number of ways. The most flexible way is to include them for each zone in variable-air-volume (VAV) box and single-zone VAV (SZVAV) air-handling unit (AHU) equipment schedules. They can also be generically listed by zone type, such as the example in (a) and (b) below. a. Default setpoints shall be based on zone type as shown in Table 3.1.1.1-1. Table 3.1.1.1-1 Default Setpoints Zone Type Occupied Unoccupied Heating Cooling Heating Cooling VAV 21°C (70°F) 24°C (75°F) 16°C (60°F) 32°C (90°F) Mechanical/electrical rooms 18°C (65°F) 29°C …
- **Textual difference:** insert: 2021 [(AHU) equipment schedules. They can also be generically listed by zone type, such as the example in (a) below. a. Default setpoints shall be based on zone type as shown in Table 3.1.1.1. Table 3.1.1.1 Default] -> 2024 [(AHU) equipment schedules. They can also be generically listed by zone type, such as the example in (a) and (b) below. a. Default setpoints shall be based on zone type as shown in Table 3.1.1.1-1. Table 3.1.1.1-1 Default] | replace: 2021 [the example in (a) below. a. Default setpoints shall be based on zone type as shown in Table 3.1.1.1. Table 3.1.1.1 Default Setpoints Zone Type Occupied Unoccupied Heating Cooling Heating Cooling VAV 21°C (70°F) 24°C (75°F) 16°C] -> 2024 [in (a) and (b) below. a. Default setpoints shall be based on zone type as shown in Table 3.1.1.1-1. Table 3.1.1.1-1 Default Setpoints Zone …
- **Operational interpretation:** Adds a way to establish different demand limit adjustments to different space types.. The affected behavior should be confirmed against the full section and controlled addendum source before implementation.

### Section 5.3.2.6
- **2021 reference:** PDF page(s) 68
- **2024 reference:** PDF page(s) 77
- **2021 excerpt:** 5.3.2.6. Cooling Demand Limit Set-Point Adjustment. The active cooling setpoints for all zones shall be increased when a demand limit is imposed on the associated Zone Group. The operator shall have the ability to exempt individual zones from this adjustment through the normal BAS user interface. Changes due to demand limits are not cumulative. a. At demand-limit Level 1, increase setpoint by 0.5°C (1°F). b. At demand-limit Level 2, increase setpoint by 1°C (2°F). c. At demand-limit Level 3, increase setpoint by 2°C (4°F).
- **2024 excerpt:** 5.3.2.6. Cooling Demand Limit Set-Point Adjustment. The active cooling setpoints for all zones shall be increased when a demand limit is imposed on the associated Zone Group. The operator shall have the ability to exempt individual zones from this adjustment through the normal BAS user interface. Changes due to demand limits are not cumulative. a. At demand-limit Level 1, increase setpoint by offset listed in Section 3.1.1.1.b. b. At demand-limit Level 2, increase setpoint by offset listed in Section 3.1.1.1.b. c. At demand-limit Level 3, increase setpoint by offset listed in Section 3.1.1.1.b.
- **Textual difference:** replace: 2021 [user interface. Changes due to demand limits are not cumulative. a. At demand-limit Level 1, increase setpoint by 0.5°C (1°F). b. At demand-limit Level 2, increase setpoint by 1°C (2°F). c. At demand-limit Level 3, increase setpoint by] -> 2024 [user interface. Changes due to demand limits are not cumulative. a. At demand-limit Level 1, increase setpoint by offset listed in Section 3.1.1.1.b. b. At demand-limit Level 2, increase setpoint by offset listed in Section 3.1.1.1.b. c. At demand-limit Level 3,] | replace: 2021 [a. At demand-limit Level 1, increase setpoint by 0.5°C (1°F). b. At demand-limit Level 2, increase setpoint by 1°C (2°F). c. At demand-limit Level 3, increase setpoint by 2°C (4°F).] -> 2024 [Level 1, increase setpoint by offset listed in Section 3.1.1.1.b. b. At demand-limit Level 2, increase setpoint by …
- **Operational interpretation:** Adds a way to establish different demand limit adjustments to different space types.. The affected behavior should be confirmed against the full section and controlled addendum source before implementation.

### Section 5.3.2.7
- **2021 reference:** PDF page(s) 68
- **2024 reference:** PDF page(s) 77, 78
- **2021 excerpt:** 5.3.2.7. Heating Demand-Limit Set-Point Adjustment. The active heating setpoints for all zones shall be decreased when a demand limit is imposed on the associated Zone Group. The operator shall have the ability to exempt individual zones from this adjustment through the normal BAS user interface. Changes due to demand limits are not cumulative. a. At demand-limit Level 1, decrease setpoint by 0.5°C (1°F). b. At demand-limit Level 2, decrease setpoint by 1°C (2°F). c. At demand-limit Level 3, decrease setpoint by 2°C (4°F). Heating demand limits may be desirable in buildings with electric heat or heat pumps or in regions with limited gas …
- **2024 excerpt:** 5.3.2.7. Heating Demand-Limit Set-Point Adjustment. The active heating setpoints for all zones shall be decreased when a demand limit is imposed on the associated Zone Group. The operator shall have the ability to exempt individual zones from this adjustment through the normal BAS user interface. Changes due to demand limits are not cumulative. a. At demand-limit Level 1, decrease setpoint by offset listed in Section 3.1.1.1.b. b. At demand-limit Level 2, decrease setpoint by offset listed in Section 3.1.1.1.b. c. At demand-limit Level 3, decrease setpoint by offset listed in Section 3.1.1.1.b. …
- **Textual difference:** replace: 2021 [user interface. Changes due to demand limits are not cumulative. a. At demand-limit Level 1, decrease setpoint by 0.5°C (1°F). b. At demand-limit Level 2, decrease setpoint by 1°C (2°F). c. At demand-limit Level 3, decrease setpoint by] -> 2024 [user interface. Changes due to demand limits are not cumulative. a. At demand-limit Level 1, decrease setpoint by offset listed in Section 3.1.1.1.b. b. At demand-limit Level 2, decrease setpoint by offset listed in Section 3.1.1.1.b. c. At demand-limit Level 3,] | replace: 2021 [a. At demand-limit Level 1, decrease setpoint by 0.5°C (1°F). b. At demand-limit Level 2, decrease setpoint by 1°C (2°F). c. At demand-limit Level 3, decrease setpoint by 2°C (4°F). Heating demand limits may be desirable in buildings] -> 2024 [Level 1, decrease setpoint by offset listed in Section …
- **Operational interpretation:** Adds a way to establish different demand limit adjustments to different space types.. The affected behavior should be confirmed against the full section and controlled addendum source before implementation.

## Reviewer notes
- The 2024 source is a consolidated edition; section differences cannot be attributed exclusively to this addendum without the controlled standalone addendum redline.
- System categories are engineering mappings from affected sections and descriptions; confirm against the official 2024 index.

## Validation
- Appendix C inventory row represented: **Pass**.
- All 3 listed section references represented: **Pass**.
- Systems and functional categories populated: **Pass with mapping limitation**.
- 2021-to-2024 evidence status: **Complete**.
- CDL implementation status: **Not assessed by this PDF-based workflow**.
