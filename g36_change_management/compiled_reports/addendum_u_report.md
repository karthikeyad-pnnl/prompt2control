# ASHRAE Guideline 36-2024 Addendum u Report

## Inventory
- **Description:** Updates all fan and pump alarms to be consistent throughout.
- **ASHRAE approval date:** March 14, 2024
- **Affected sections:** 5.7.6.3; 5.8.6.3; 5.9.6.3; 5.10.6; 5.16.13.2; 5.17.3.2; 5.18.12.2; 5.19.2.2; 5.22.5.2
- **Appendix C PDF page(s):** 307

## Methodology and limitations
The supplied `addendum_a_analysis.py` extraction workflow was run in `--all` mode against the supplied 2021 and 2024 PDFs. It extracted Appendix C inventory rows and section-level evidence. The comparisons below use that evidence and normalized word-level alignment; they are not a substitute for the controlled standalone addendum redline. Because the 2024 PDF is consolidated, unrelated cumulative edits in an affected section are not independently attributed to this addendum.

## Impact classification
- **Systems impacted:** Multiple-zone VAV air handling units; Air handling units; Single-zone VAV air handling units; VAV terminal units; Dual-duct systems; Chilled-water plants; Central plants
- **Primary functional category:** Alarm
- **Secondary functional categories:** Equipment enable/disable, Process control
- **Comparison status:** Complete
- **Quality level:** Partially verified

## Section-level comparison
### Section 5.7.6.3
- **2021 reference:** PDF page(s) 82
- **2024 reference:** PDF page(s) 93
- **2021 excerpt:** 5.7.6.3. Fan alarm is indicated by the status input being different from the output command after a period of 15 seconds after a change in output status. a. Commanded on, status off: Level 2 b. Commanded off, status on: Level 4
- **2024 excerpt:** 5.7.6.3. Fan alarm is indicated by the status input being different from the output command for 15 seconds. a. Commanded on, status off: Level 2. Do not evaluate the alarm until the equipment has been commanded on for 15 seconds. b. Commanded off, status on: Level 4. Do not evaluate the alarm until the equipment has been commanded off for 60 seconds.
- **Textual difference:** replace: 2021 [5.7.6.3. Fan alarm is indicated by the status input being different from the output command after a period of 15 seconds after a change in output status. a. Commanded on, status off: Level 2 b. Commanded off,] -> 2024 [5.7.6.3. Fan alarm is indicated by the status input being different from the output command for 15 seconds. a. Commanded on, status off: Level 2. Do not evaluate the alarm until the equipment has] | replace: 2021 [alarm is indicated by the status input being different from the output command after a period of 15 seconds after a change in output status. a. Commanded on, status off: Level 2 b. Commanded off, status on: Level 4] -> 2024 [5.7.6.3. Fan alarm is indicated by the status input being different from the output command for 15 seconds. a. Commanded on, status off: Level 2. Do not evaluate the alarm …
- **Operational interpretation:** Updates all fan and pump alarms to be consistent throughout.. The affected behavior should be confirmed against the full section and controlled addendum source before implementation.

### Section 5.8.6.3
- **2021 reference:** PDF page(s) 86
- **2024 reference:** PDF page(s) 98
- **2021 excerpt:** 5.8.6.3. Fan alarm is indicated by the status input being different from the output command after a period of 15 seconds after a change in output status. a. Commanded ON, status OFF Level 2 b. Commanded OFF, status ON: Level 4
- **2024 excerpt:** 5.8.6.3. Fan alarm is indicated by the status input being different from the output command for 15 seconds. a. Commanded on, status off: Level 2. Do not evaluate the alarm until the equipment has been commanded on for 15 seconds. b. Commanded off, status on: Level 4. Do not evaluate the alarm until the equipment has been commanded off for 60 seconds.
- **Textual difference:** replace: 2021 [5.8.6.3. Fan alarm is indicated by the status input being different from the output command after a period of 15 seconds after a change in output status. a. Commanded ON, status OFF Level 2 b. Commanded OFF,] -> 2024 [5.8.6.3. Fan alarm is indicated by the status input being different from the output command for 15 seconds. a. Commanded on, status off: Level 2. Do not evaluate the alarm until the equipment has] | replace: 2021 [alarm is indicated by the status input being different from the output command after a period of 15 seconds after a change in output status. a. Commanded ON, status OFF Level 2 b. Commanded OFF, status ON: Level 4] -> 2024 [5.8.6.3. Fan alarm is indicated by the status input being different from the output command for 15 seconds. a. Commanded on, status off: Level 2. Do not evaluate the alarm until …
- **Operational interpretation:** Updates all fan and pump alarms to be consistent throughout.. The affected behavior should be confirmed against the full section and controlled addendum source before implementation.

### Section 5.9.6.3
- **2021 reference:** PDF page(s) 89, 90
- **2024 reference:** PDF page(s) 102
- **2021 excerpt:** 5.9.6.3. Fan alarm is indicated by the status input being different from the output command after a period of 15 seconds after a change in output status. a. Commanded ON, status OFF: Level 2 b. Commanded OFF, status ON: Level 4 © ASHRAE. Per international copyright law, additional reproduction, distribution, or transmission in either print or digital form is not permitted without ASHRAE's prior written permission. Copyright American Society of Heating, Refrigerating and Air-Conditioning Engine Provided by IHS Markit under license with ASHRAE - Uncontrolled Copy Licensee=BATTELLE PACIFIC NW DIVISION/5940137102, User=Devaprasad, Karthikeya Not …
- **2024 excerpt:** 5.9.6.3. Fan alarm is indicated by the status input being different from the output command for 15 seconds. a. Commanded on, status off: Level 2. Do not evaluate the alarm until the equipment has been commanded on for 15 seconds. b. Commanded off, status on: Level 4. Do not evaluate the alarm until the equipment has been commanded off for 60 seconds.
- **Textual difference:** replace: 2021 [5.9.6.3. Fan alarm is indicated by the status input being different from the output command after a period of 15 seconds after a change in output status. a. Commanded ON, status OFF: Level 2 b. Commanded OFF,] -> 2024 [5.9.6.3. Fan alarm is indicated by the status input being different from the output command for 15 seconds. a. Commanded on, status off: Level 2. Do not evaluate the alarm until the equipment has] | replace: 2021 [alarm is indicated by the status input being different from the output command after a period of 15 seconds after a change in output status. a. Commanded ON, status OFF: Level 2 b. Commanded OFF, status ON: Level 4 © ASHRAE. Per international] -> 2024 [5.9.6.3. Fan alarm is indicated by the status input being different from the output command for 15 seconds. a. Commanded on, status off: Level 2. Do …
- **Operational interpretation:** Updates all fan and pump alarms to be consistent throughout.. The affected behavior should be confirmed against the full section and controlled addendum source before implementation.

### Section 5.10.6
- **2021 reference:** PDF page(s) 93, 94
- **2024 reference:** PDF page(s) 106, 107
- **2021 excerpt:** 5.10.6. Alarms 5.10.6.1. Low Primary Airflow a. If the measured airflow is less than 70% of setpoint for 10 minutes while setpoint is greater than zero, generate a Level 4 alarm. b. If the measured airflow is less than 50% of setpoint for 10 minutes while setpoint is greater than zero, generate a Level 3 alarm. c. If a zone has an Importance-Multiplier of 0 (see Section 5.1.14.2.a.1 for its static pressure reset T&R control loop, low airflow alarms shall be suppressed for that zone. 5.10.6.2. Low-Discharge Air Temperature a. If heating hot-water plant is proven ON, and the DAT is 8.3°C (15°F) less than setpoint for 10 minutes, generate a …
- **2024 excerpt:** 5.10.6. Alarms 5.10.6.1. Low Primary Airflow a. If the measured airflow is less than 70% of setpoint for 10 minutes while setpoint is greater than zero, generate a Level 4 alarm. b. If the measured airflow is less than 50% of setpoint for 10 minutes while setpoint is greater than zero, generate a Level 3 alarm. c. If a zone has an Importance-Multiplier of 0 (see Section 5.1.16) for its static pressure reset T&R control loop, low airflow alarms shall be suppressed for that zone. 5.10.6.2. Low-Discharge Air Temperature a. If heating hot-water plant is proven ON, and the DAT is 8.3°C (15°F) less than setpoint for 10 minutes, generate a Level 4 …
- **Textual difference:** replace: 2021 [than zero, generate a Level 3 alarm. c. If a zone has an Importance-Multiplier of 0 (see Section 5.1.14.2.a.1 for its static pressure reset T&R control loop, low airflow alarms shall be suppressed for that zone. 5.10.6.2.] -> 2024 [than zero, generate a Level 3 alarm. c. If a zone has an Importance-Multiplier of 0 (see Section 5.1.16) for its static pressure reset T&R control loop, low airflow alarms shall be suppressed for that zone. 5.10.6.2.] | insert: 2021 [ON, and the DAT is 17°C (30°F) less than setpoint for 10 minutes, generate a Level 3 alarm. c. If a zone has an Importance-Multiplier of 0 (see Section 5.1.14.2.a.1) for its hot-water reset T&R control] -> 2024 [ON, and the DAT is 17°C (30°F) less than setpoint for 10 minutes, generate a Level 3 alarm. …
- **Operational interpretation:** Updates all fan and pump alarms to be consistent throughout.. The affected behavior should be confirmed against the full section and controlled addendum source before implementation.

### Section 5.16.13.2
- **2021 reference:** PDF page(s) 134
- **2024 reference:** PDF page(s) 154
- **2021 excerpt:** 5.16.13.2. Fan alarm is indicated by the status being different from the command for a period of 15 seconds. a. Commanded on, status off: Level 2 b. Commanded off, status on: Level 4
- **2024 excerpt:** 5.16.13.2. Fan alarm is indicated by the status input being different from the output command for 15 seconds. a. Commanded on, status off: Level 2. Do not evaluate the alarm until the equipment has been commanded on for 15 seconds. b. Commanded off, status on: Level 4. Do not evaluate the alarm until the equipment has been commanded off for 60 seconds.
- **Textual difference:** insert: 2021 [5.16.13.2. Fan alarm is indicated by the status being different from the command for a period of 15 seconds. a. Commanded on, status off: Level 2] -> 2024 [5.16.13.2. Fan alarm is indicated by the status input being different from the output command for 15 seconds. a. Commanded on, status off: Level 2. Do not] | insert: 2021 [5.16.13.2. Fan alarm is indicated by the status being different from the command for a period of 15 seconds. a. Commanded on, status off: Level 2 b. Commanded off, status] -> 2024 [5.16.13.2. Fan alarm is indicated by the status input being different from the output command for 15 seconds. a. Commanded on, status off: Level 2. Do not evaluate the alarm until the] | delete: 2021 [5.16.13.2. Fan alarm is indicated by the status being different from the command for a period of 15 seconds. a. Commanded on, …
- **Operational interpretation:** Updates all fan and pump alarms to be consistent throughout.. The affected behavior should be confirmed against the full section and controlled addendum source before implementation.

### Section 5.17.3.2
- **2021 reference:** PDF page(s) 148
- **2024 reference:** PDF page(s) 167
- **2021 excerpt:** 5.17.3.2. Fan alarm is indicated by the status being different from the command for a period of 15 seconds. a. Commanded ON, status OFF: Level 2 b. Commanded OFF, status ON: Level 4
- **2024 excerpt:** 5.17.3.2. Fan alarm is indicated by the status input being different from the output command for 15 seconds. a. Commanded on, status off: Level 2. Do not evaluate the alarm until the equipment has been commanded on for 15 seconds. b. Commanded off, status on: Level 4. Do not evaluate the alarm until the equipment has been commanded off for 60 seconds.
- **Textual difference:** insert: 2021 [5.17.3.2. Fan alarm is indicated by the status being different from the command for a period of 15 seconds. a. Commanded ON, status OFF: Level 2] -> 2024 [5.17.3.2. Fan alarm is indicated by the status input being different from the output command for 15 seconds. a. Commanded on, status off: Level 2. Do not] | insert: 2021 [5.17.3.2. Fan alarm is indicated by the status being different from the command for a period of 15 seconds. a. Commanded ON, status OFF: Level 2 b. Commanded OFF, status] -> 2024 [5.17.3.2. Fan alarm is indicated by the status input being different from the output command for 15 seconds. a. Commanded on, status off: Level 2. Do not evaluate the alarm until the] | delete: 2021 [5.17.3.2. Fan alarm is indicated by the status being different from the command for a period of 15 seconds. a. Commanded ON, …
- **Operational interpretation:** Updates all fan and pump alarms to be consistent throughout.. The affected behavior should be confirmed against the full section and controlled addendum source before implementation.

### Section 5.18.12.2
- **2021 reference:** PDF page(s) 161
- **2024 reference:** PDF page(s) 180
- **2021 excerpt:** 5.18.12.2. Fan alarm is indicated by the status being different from the command for a period of 15 seconds. a. Commanded ON, status OFF: Level 2 b. Commanded OFF, status ON: Level 4
- **2024 excerpt:** 5.18.12.2. Fan alarm is indicated by the status input being different from the output command for 15 seconds. a. Commanded on, status off: Level 2. Do not evaluate the alarm until the equipment has been commanded on for 15 seconds. b. Commanded off, status on: Level 4. Do not evaluate the alarm until the equipment has been commanded off for 60 seconds.
- **Textual difference:** insert: 2021 [5.18.12.2. Fan alarm is indicated by the status being different from the command for a period of 15 seconds. a. Commanded ON, status OFF: Level 2] -> 2024 [5.18.12.2. Fan alarm is indicated by the status input being different from the output command for 15 seconds. a. Commanded on, status off: Level 2. Do not] | insert: 2021 [5.18.12.2. Fan alarm is indicated by the status being different from the command for a period of 15 seconds. a. Commanded ON, status OFF: Level 2 b. Commanded OFF, status] -> 2024 [5.18.12.2. Fan alarm is indicated by the status input being different from the output command for 15 seconds. a. Commanded on, status off: Level 2. Do not evaluate the alarm until the] | delete: 2021 [5.18.12.2. Fan alarm is indicated by the status being different from the command for a period of 15 seconds. a. Commanded ON, …
- **Operational interpretation:** Updates all fan and pump alarms to be consistent throughout.. The affected behavior should be confirmed against the full section and controlled addendum source before implementation.

### Section 5.19.2.2
- **2021 reference:** PDF page(s) 171, 172
- **2024 reference:** PDF page(s) 190
- **2021 excerpt:** 5.19.2.2. Fan alarm is indicated by the status being different from the command for a period of 15 seconds. a. Commanded on, status off: Level 2 b. Commanded off, status off: Level 4 © ASHRAE. Per international copyright law, additional reproduction, distribution, or transmission in either print or digital form is not permitted without ASHRAE's prior written permission. Copyright American Society of Heating, Refrigerating and Air-Conditioning Engine Provided by IHS Markit under license with ASHRAE - Uncontrolled Copy Licensee=BATTELLE PACIFIC NW DIVISION/5940137102, User=Devaprasad, Karthikeya Not for Resale, 01/27/2022 04:30:51 MST No …
- **2024 excerpt:** 5.19.2.2. Fan alarm is indicated by the status input being different from the output command for 15 seconds. a. Commanded on, status off: Level 2. Do not evaluate the alarm until the equipment has been commanded on for 15 seconds. b. Commanded off, status on: Level 4. Do not evaluate the alarm until the equipment has been commanded off for 60 seconds. Retain the following paragraph if the exhaust fan is to be cycled to maintain room temperature. Delete otherwise.
- **Textual difference:** insert: 2021 [5.19.2.2. Fan alarm is indicated by the status being different from the command for a period of 15 seconds. a. Commanded on, status off: Level 2] -> 2024 [5.19.2.2. Fan alarm is indicated by the status input being different from the output command for 15 seconds. a. Commanded on, status off: Level 2. Do not] | insert: 2021 [5.19.2.2. Fan alarm is indicated by the status being different from the command for a period of 15 seconds. a. Commanded on, status off: Level 2 b. Commanded off, status] -> 2024 [5.19.2.2. Fan alarm is indicated by the status input being different from the output command for 15 seconds. a. Commanded on, status off: Level 2. Do not evaluate the alarm until the] | delete: 2021 [5.19.2.2. Fan alarm is indicated by the status being different from the command for a period of 15 seconds. a. Commanded on, …
- **Operational interpretation:** Updates all fan and pump alarms to be consistent throughout.. The affected behavior should be confirmed against the full section and controlled addendum source before implementation.

### Section 5.22.5.2
- **2021 reference:** PDF page(s) 264
- **2024 reference:** PDF page(s) 284
- **2021 excerpt:** 5.22.5.2. Fan alarm is indicated by the status being different from the command for a period of 15 seconds. a. Commanded on, status off: Level 2 b. Commanded off, status on: Level 4
- **2024 excerpt:** 5.22.5.2. Fan alarm is indicated by the status input being different from the output command for 15 seconds. a. Commanded on, status off: Level 2. Do not evaluate the alarm until the equipment has been commanded on for 15 seconds. b. Commanded off, status on: Level 4. Do not evaluate the alarm until the equipment has been commanded off for 60 seconds.
- **Textual difference:** insert: 2021 [5.22.5.2. Fan alarm is indicated by the status being different from the command for a period of 15 seconds. a. Commanded on, status off: Level 2] -> 2024 [5.22.5.2. Fan alarm is indicated by the status input being different from the output command for 15 seconds. a. Commanded on, status off: Level 2. Do not] | insert: 2021 [5.22.5.2. Fan alarm is indicated by the status being different from the command for a period of 15 seconds. a. Commanded on, status off: Level 2 b. Commanded off, status] -> 2024 [5.22.5.2. Fan alarm is indicated by the status input being different from the output command for 15 seconds. a. Commanded on, status off: Level 2. Do not evaluate the alarm until the] | delete: 2021 [5.22.5.2. Fan alarm is indicated by the status being different from the command for a period of 15 seconds. a. Commanded on, …
- **Operational interpretation:** Updates all fan and pump alarms to be consistent throughout.. The affected behavior should be confirmed against the full section and controlled addendum source before implementation.

## Reviewer notes
- The 2024 source is a consolidated edition; section differences cannot be attributed exclusively to this addendum without the controlled standalone addendum redline.
- System categories are engineering mappings from affected sections and descriptions; confirm against the official 2024 index.

## Validation
- Appendix C inventory row represented: **Pass**.
- All 9 listed section references represented: **Pass**.
- Systems and functional categories populated: **Pass with mapping limitation**.
- 2021-to-2024 evidence status: **Complete**.
- CDL implementation status: **Not assessed by this PDF-based workflow**.
