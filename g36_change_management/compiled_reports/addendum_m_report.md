# ASHRAE Guideline 36-2024 Addendum m Report

## Inventory
- **Description:** Revision to the leaking valve alarm for all equipment with hot water valves to reduce nuisance alarms.
- **ASHRAE approval date:** March 14, 2024
- **Affected sections:** 5.6.6.5; 5.7.6.6; 5.8.6.6; 5.9.6.6; 5.10.6.6
- **Appendix C PDF page(s):** 307

## Methodology and limitations
The supplied `addendum_a_analysis.py` extraction workflow was run in `--all` mode against the supplied 2021 and 2024 PDFs. It extracted Appendix C inventory rows and section-level evidence. The comparisons below use that evidence and normalized word-level alignment; they are not a substitute for the controlled standalone addendum redline. Because the 2024 PDF is consolidated, unrelated cumulative edits in an affected section are not independently attributed to this addendum.

## Impact classification
- **Systems impacted:** VAV terminal units; Hot-water plants; Hydronic distribution systems
- **Primary functional category:** Alarm
- **Secondary functional categories:** None
- **Comparison status:** Complete
- **Quality level:** Partially verified

## Section-level comparison
### Section 5.6.6.5
- **2021 reference:** PDF page(s) 78
- **2024 reference:** PDF page(s) 88, 89
- **2021 excerpt:** 5.6.6.5. Leaking Valve. If the valve position is 0% for 15 minutes, DAT is above AHU SAT by 3°C (5°F), and the fan serving the zone is proven ON, generate a Level 4 alarm.
- **2024 excerpt:** 5.6.6.5. Leaking Valve. If all of the following are true for 15 minutes, generate a Level 4 alarm. a. Valve position is 0%; and b. DAT is above AHU SAT by 3°C (5°F); and ThisfileislicensedtoKarthikeyaDevaprasad(karthikeya.devaprasad@pnnl.gov).DownloadDate:1/28/2025 === PDF page 89 === ASHRAE Guideline 36-2024 87 c. Damper position is greater than 0% and the AHU supply fan serving the zone is proven ON.
- **Textual difference:** insert: 2021 [5.6.6.5. Leaking Valve. If the valve position is 0% for 15 minutes, DAT is above AHU SAT by 3°C (5°F), and the] -> 2024 [5.6.6.5. Leaking Valve. If all of the following are true for 15 minutes, generate a Level 4 alarm. a. Valve position is 0%; and] | replace: 2021 [5.6.6.5. Leaking Valve. If the valve position is 0% for 15 minutes, DAT is above AHU SAT by 3°C (5°F), and the fan serving the zone is] -> 2024 [5.6.6.5. Leaking Valve. If all of the following are true for 15 minutes, generate a Level 4 alarm. a. Valve position is 0%; and b. DAT is above] | insert: 2021 [5.6.6.5. Leaking Valve. If the valve position is 0% for 15 minutes, DAT is above AHU SAT by 3°C (5°F), and the fan serving the zone is proven ON, generate] -> 2024 [5.6.6.5. Leaking Valve. If all of the following are true for 15 minutes, generate a Level 4 …
- **Operational interpretation:** Revision to the leaking valve alarm for all equipment with hot water valves to reduce nuisance alarms.. The affected behavior should be confirmed against the full section and controlled addendum source before implementation.

### Section 5.7.6.6
- **2021 reference:** PDF page(s) 82
- **2024 reference:** PDF page(s) 93
- **2021 excerpt:** 5.7.6.6. Leaking Valve. If the valve position is 0% for 15 minutes, DAT is above AHU SAT by 3°C (5°F), and the fan serving the zone is proven ON, generate a Level 4 alarm.
- **2024 excerpt:** 5.7.6.6. Leaking Valve. If all of the following are true for 15 minutes, generate a Level 4 alarm. a. Valve position is 0%; and b. DAT is above AHU SAT by 3°C (5°F); and c. DAT is above room temperature by 3°C (5°F); and d. Damper position is greater than 0% and the AHU supply fan or the parallel fan serving the zone is proven ON.
- **Textual difference:** insert: 2021 [5.7.6.6. Leaking Valve. If the valve position is 0% for 15 minutes, DAT is above AHU SAT by 3°C (5°F), and the] -> 2024 [5.7.6.6. Leaking Valve. If all of the following are true for 15 minutes, generate a Level 4 alarm. a. Valve position is 0%; and] | replace: 2021 [5.7.6.6. Leaking Valve. If the valve position is 0% for 15 minutes, DAT is above AHU SAT by 3°C (5°F), and the fan serving the zone is] -> 2024 [5.7.6.6. Leaking Valve. If all of the following are true for 15 minutes, generate a Level 4 alarm. a. Valve position is 0%; and b. DAT is above] | insert: 2021 [5.7.6.6. Leaking Valve. If the valve position is 0% for 15 minutes, DAT is above AHU SAT by 3°C (5°F), and the fan serving the zone is proven ON, generate] -> 2024 [5.7.6.6. Leaking Valve. If all of the following are true for 15 minutes, generate a Level 4 …
- **Operational interpretation:** Revision to the leaking valve alarm for all equipment with hot water valves to reduce nuisance alarms.. The affected behavior should be confirmed against the full section and controlled addendum source before implementation.

### Section 5.8.6.6
- **2021 reference:** PDF page(s) 86
- **2024 reference:** PDF page(s) 98
- **2021 excerpt:** 5.8.6.6. Leaking Valve. If the valve position is 0% for 15 minutes, and DAT is above AHU SAT by 3°C (5°F), generate a Level 4 alarm.
- **2024 excerpt:** 5.8.6.6. Leaking Valve. If all of the following are true for 15 minutes, generate a Level 4 alarm. a. Valve position is 0%; and b. DAT is above AHU SAT by 3°C (5°F); and c. DAT is above room temperature by 3°C (5°F); and d. Damper position is greater than 0% and the AHU supply fan or the parallel fan serving the zone is proven ON.
- **Textual difference:** insert: 2021 [5.8.6.6. Leaking Valve. If the valve position is 0% for 15 minutes, and DAT is above AHU SAT by 3°C (5°F), generate] -> 2024 [5.8.6.6. Leaking Valve. If all of the following are true for 15 minutes, generate a Level 4 alarm. a. Valve position is 0%; and] | replace: 2021 [5.8.6.6. Leaking Valve. If the valve position is 0% for 15 minutes, and DAT is above AHU SAT by 3°C (5°F), generate a Level 4 alarm.] -> 2024 [5.8.6.6. Leaking Valve. If all of the following are true for 15 minutes, generate a Level 4 alarm. a. Valve position is 0%; and b. DAT is above] | insert: 2021 [5.8.6.6. Leaking Valve. If the valve position is 0% for 15 minutes, and DAT is above AHU SAT by 3°C (5°F), generate a Level 4 alarm.] -> 2024 [5.8.6.6. Leaking Valve. If all of the following are true for 15 minutes, generate a Level 4 alarm. a. Valve position …
- **Operational interpretation:** Revision to the leaking valve alarm for all equipment with hot water valves to reduce nuisance alarms.. The affected behavior should be confirmed against the full section and controlled addendum source before implementation.

### Section 5.9.6.6
- **2021 reference:** PDF page(s) 90
- **2024 reference:** PDF page(s) 103
- **2021 excerpt:** 5.9.6.6. Leaking Valve. If the valve position is 0% for 15 minutes, and DAT is above AHU SAT by 3°C (5°F), generate a Level 4 alarm.
- **2024 excerpt:** 5.9.6.6. Leaking Valve. If all of the following are true for 15 minutes, generate a Level 4 alarm. a. Valve position is 0%; and b. DAT is above AHU SAT by 3°C (5°F); and c. DAT is above room temperature by 3°C (5°F); and d. Series fan serving the zone is proven ON.
- **Textual difference:** insert: 2021 [5.9.6.6. Leaking Valve. If the valve position is 0% for 15 minutes, and DAT is above AHU SAT by 3°C (5°F), generate] -> 2024 [5.9.6.6. Leaking Valve. If all of the following are true for 15 minutes, generate a Level 4 alarm. a. Valve position is 0%; and] | replace: 2021 [5.9.6.6. Leaking Valve. If the valve position is 0% for 15 minutes, and DAT is above AHU SAT by 3°C (5°F), generate a Level 4 alarm.] -> 2024 [5.9.6.6. Leaking Valve. If all of the following are true for 15 minutes, generate a Level 4 alarm. a. Valve position is 0%; and b. DAT is above] | insert: 2021 [5.9.6.6. Leaking Valve. If the valve position is 0% for 15 minutes, and DAT is above AHU SAT by 3°C (5°F), generate a Level 4 alarm.] -> 2024 [5.9.6.6. Leaking Valve. If all of the following are true for 15 minutes, generate a Level 4 alarm. a. Valve position …
- **Operational interpretation:** Revision to the leaking valve alarm for all equipment with hot water valves to reduce nuisance alarms.. The affected behavior should be confirmed against the full section and controlled addendum source before implementation.

### Section 5.10.6.6
- **2021 reference:** PDF page(s) 94
- **2024 reference:** PDF page(s) 107
- **2021 excerpt:** 5.10.6.6. Leaking Valve. If the valve position is 0% for 15 minutes, and DAT is above AHU SAT by 3°C (5°F), generate a Level 4 alarm.
- **2024 excerpt:** 5.10.6.6. Leaking Valve. If all of the following are true for 15 minutes, generate a Level 4 alarm. a. Valve position is 0%; and b. DAT is above AHU SAT by 3°C (5°F); and c. DAT is above room temperature by 3°C (5°F); and d. Series fan serving the zone is proven ON.
- **Textual difference:** insert: 2021 [5.10.6.6. Leaking Valve. If the valve position is 0% for 15 minutes, and DAT is above AHU SAT by 3°C (5°F), generate] -> 2024 [5.10.6.6. Leaking Valve. If all of the following are true for 15 minutes, generate a Level 4 alarm. a. Valve position is 0%; and] | replace: 2021 [5.10.6.6. Leaking Valve. If the valve position is 0% for 15 minutes, and DAT is above AHU SAT by 3°C (5°F), generate a Level 4 alarm.] -> 2024 [5.10.6.6. Leaking Valve. If all of the following are true for 15 minutes, generate a Level 4 alarm. a. Valve position is 0%; and b. DAT is above] | insert: 2021 [5.10.6.6. Leaking Valve. If the valve position is 0% for 15 minutes, and DAT is above AHU SAT by 3°C (5°F), generate a Level 4 alarm.] -> 2024 [5.10.6.6. Leaking Valve. If all of the following are true for 15 minutes, generate a Level 4 alarm. a. Valve …
- **Operational interpretation:** Revision to the leaking valve alarm for all equipment with hot water valves to reduce nuisance alarms.. The affected behavior should be confirmed against the full section and controlled addendum source before implementation.

## Reviewer notes
- The 2024 source is a consolidated edition; section differences cannot be attributed exclusively to this addendum without the controlled standalone addendum redline.
- System categories are engineering mappings from affected sections and descriptions; confirm against the official 2024 index.

## Validation
- Appendix C inventory row represented: **Pass**.
- All 5 listed section references represented: **Pass**.
- Systems and functional categories populated: **Pass with mapping limitation**.
- 2021-to-2024 evidence status: **Complete**.
- CDL implementation status: **Not assessed by this PDF-based workflow**.
