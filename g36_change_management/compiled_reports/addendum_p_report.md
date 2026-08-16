# ASHRAE Guideline 36-2024 Addendum p Report

## Inventory
- **Description:** Addresses errors in the AFDD fault condition equations. Adds option to use airflow monitoring stations for fault conditions that calculate %OA.
- **ASHRAE approval date:** March 14, 2024
- **Affected sections:** 5.16.13.5; 5.16.14
- **Appendix C PDF page(s):** 307

## Methodology and limitations
The supplied `addendum_a_analysis.py` extraction workflow was run in `--all` mode against the supplied 2021 and 2024 PDFs. It extracted Appendix C inventory rows and section-level evidence. The comparisons below use that evidence and normalized word-level alignment; they are not a substitute for the controlled standalone addendum redline. Because the 2024 PDF is consolidated, unrelated cumulative edits in an affected section are not independently attributed to this addendum.

## Impact classification
- **Systems impacted:** Multiple-zone VAV air handling units; Air handling units
- **Primary functional category:** Fault detection and diagnostics
- **Secondary functional categories:** Sensor validation or calibration
- **Comparison status:** Complete
- **Quality level:** Partially verified

## Section-level comparison
### Section 5.16.13.5
- **2021 reference:** PDF page(s) 134
- **2024 reference:** PDF page(s) 155
- **2021 excerpt:** 5.16.13.5. Low building pressure (less than 0 Pa [0.0 in. of water], i.e., negative) for 5 minutes: Level 4. Automatic fault detection and diagnostics (AFDD) is a sophisticated system for detecting and diagnosing air- handler faults. To function correctly, AFDD requires specific sensors and data be available, as detailed in the sequences below. If this information is not available, AFDD tests that do not apply should be deleted.
- **2024 excerpt:** 5.16.13.5. Low building pressure (less than 0 Pa [0.0 in. of water], i.e., negative) for 5 minutes: Level 4.
- **Textual difference:** delete: 2021 [Low building pressure (less than 0 Pa [0.0 in. of water], i.e., negative) for 5 minutes: Level 4. Automatic fault detection and diagnostics (AFDD) is a sophisticated system for detecting and diagnosing air- handler faults. To function correctly, AFDD requires specific sensors and data be available, as detailed in the sequences below. If this information is not available, AFDD tests that do not apply should be deleted.] -> 2024 [Low building pressure (less than 0 Pa [0.0 in. of water], i.e., negative) for 5 minutes: Level
- **Operational interpretation:** Addresses errors in the AFDD fault condition equations. Adds option to use airflow monitoring stations for fault conditions that calculate %OA.. The affected behavior should be confirmed against the full section and controlled addendum source before implementation.

### Section 5.16.14
- **2021 reference:** PDF page(s) 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145
- **2024 reference:** PDF page(s) 155, 156, 157, 158, 159, 160, 161, 162, 163, 164
- **2021 excerpt:** 5.16.14. Automatic Fault Detection and Diagnostics The AFDD routines for AHUs continually assess AHU performance by comparing the values of BAS inputs and outputs to a subset of potential fault conditions. The subset of potential fault conditions that is assessed at any point depends on the operating state (OS) of the AHU, as determined by the position of the cooling and heating valves and the economizer damper. Time delays are applied to the evaluation and reporting of fault conditions to suppress false alarms. Fault conditions that pass these filters are reported to the building operator along with a series of possible causes. These …
- **2024 excerpt:** 5.16.14. Automatic Fault Detection and Diagnostics Automatic fault detection and diagnostics (AFDD) is a sophisticated system for detecting and diagnosing air- handler faults. To function correctly, AFDD requires specific sensors and data be available, as detailed in the sequences below. If this information is not available, AFDD tests that do not apply should be deleted. The AFDD routines for AHUs continually assess AHU performance by comparing the values of BAS inputs and outputs to a subset of potential fault conditions. The subset of potential fault conditions that is assessed at any point depends on the operating state (OS) of the AHU, …
- **Textual difference:** insert: 2021 [5.16.14. Automatic Fault Detection and Diagnostics The AFDD routines for AHUs continually assess AHU performance by comparing the values of BAS inputs and outputs] -> 2024 [5.16.14. Automatic Fault Detection and Diagnostics Automatic fault detection and diagnostics (AFDD) is a sophisticated system for detecting and diagnosing air- handler faults. To function correctly, AFDD requires specific sensors and data be available, as detailed in the sequences below. If this information is not available, AFDD tests that do not apply should be deleted. The AFDD routines for AHUs continually assess AHU performance by comparing the values of BAS inputs and outputs] | replace: 2021 [any of these components are not present, the associated tests and variables should be omitted from the programming. Note that these alarms rely on reasonably …
- **Operational interpretation:** Addresses errors in the AFDD fault condition equations. Adds option to use airflow monitoring stations for fault conditions that calculate %OA.. The affected behavior should be confirmed against the full section and controlled addendum source before implementation.

## Reviewer notes
- The 2024 source is a consolidated edition; section differences cannot be attributed exclusively to this addendum without the controlled standalone addendum redline.
- System categories are engineering mappings from affected sections and descriptions; confirm against the official 2024 index.

## Validation
- Appendix C inventory row represented: **Pass**.
- All 2 listed section references represented: **Pass**.
- Systems and functional categories populated: **Pass with mapping limitation**.
- 2021-to-2024 evidence status: **Complete**.
- CDL implementation status: **Not assessed by this PDF-based workflow**.
