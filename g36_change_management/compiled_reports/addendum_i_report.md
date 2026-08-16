# ASHRAE Guideline 36-2024 Addendum i Report

## Inventory
- **Description:** Rearranges the supply fan speed and supply air temperature setpoint sections for Single Zone VAV Air Handling Units to enhance clarify.
- **ASHRAE approval date:** March 14, 2024
- **Affected sections:** 5.18.4.6
- **Appendix C PDF page(s):** 306

## Methodology and limitations
The supplied `addendum_a_analysis.py` extraction workflow was run in `--all` mode against the supplied 2021 and 2024 PDFs. It extracted Appendix C inventory rows and section-level evidence. The comparisons below use that evidence and normalized word-level alignment; they are not a substitute for the controlled standalone addendum redline. Because the 2024 PDF is consolidated, unrelated cumulative edits in an affected section are not independently attributed to this addendum.

## Impact classification
- **Systems impacted:** Single-zone VAV air handling units; Air handling units
- **Primary functional category:** Setpoint generation
- **Secondary functional categories:** Equipment enable/disable, Process control, Documentation or editorial correction
- **Comparison status:** Complete
- **Quality level:** Partially verified

## Section-level comparison
### Section 5.18.4.6
- **2021 reference:** PDF page(s) 154, 155, 156
- **2024 reference:** PDF page(s) 172, 173, 174, 175
- **2021 excerpt:** 5.18.4.6. Figure 5.18.4.5-2 separates Figure 5.18.4.5-1 in two for clarity and to illustrate the relative setpoints. However, both fan speed and supply air temperature setpoints are reset simultaneously and by the same signal: the value of the Heating Loop or Cooling Loop. a. For a heating-loop signal of 100% to 50%, fan speed is reset from MaxHeatSpeed to MinSpeed. b. For a heating-loop signal of 50% to 0%, fan speed setpoint is MinSpeed. c. In deadband, fan speed setpoint is MinSpeed. d. For a cooling-loop signal of 0% to 25%, fan speed is MinSpeed. e. For a cooling-loop signal of 25% to 50%, fan speed is reset from MinSpeed to MedSpeed. …
- **2024 excerpt:** 5.18.4.6. Figure 5.18.4.5-2 separates Figure 5.18.4.5-1 in two for clarity and to illustrate the relative setpoints. However, both fan speed and supply air temperature setpoints are reset simultaneously and by the same signal: the value of the Heating Loop or Cooling Loop. a. For a heating-loop signal of 100% to 50% 1. Fan speed is reset from MaxHeatSpeed to MinSpeed. 2. SATsp is Heat_SAT. b. For a heating-loop signal of 50% to 0% 1. Fan speed setpoint is MinSpeed. 2. SATsp is reset from Heat_SAT to the deadband value. c. In deadband 1. Fan speed setpoint is MinSpeed. 2. SATsp is the deadband value. d. For a cooling-loop signal of 0% to 25% …
- **Textual difference:** replace: 2021 [signal: the value of the Heating Loop or Cooling Loop. a. For a heating-loop signal of 100% to 50%, fan speed is reset from MaxHeatSpeed to MinSpeed. b. For a heating-loop signal of 50% to 0%, fan speed] -> 2024 [signal: the value of the Heating Loop or Cooling Loop. a. For a heating-loop signal of 100% to 50% 1. Fan speed is reset from MaxHeatSpeed to MinSpeed. 2. SATsp is Heat_SAT. b. For a heating-loop signal of 50%] | insert: 2021 [Loop. a. For a heating-loop signal of 100% to 50%, fan speed is reset from MaxHeatSpeed to MinSpeed. b. For a heating-loop signal of 50% to 0%, fan speed setpoint is MinSpeed. c. In deadband, fan] -> 2024 [a. For a heating-loop signal of 100% to 50% 1. Fan speed is reset from MaxHeatSpeed to MinSpeed. 2. SATsp is Heat_SAT. b. For a heating-loop signal of 50% to 0% 1. Fan speed setpoint is …
- **Operational interpretation:** Rearranges the supply fan speed and supply air temperature setpoint sections for Single Zone VAV Air Handling Units to enhance clarify.. The affected behavior should be confirmed against the full section and controlled addendum source before implementation.

## Reviewer notes
- The 2024 source is a consolidated edition; section differences cannot be attributed exclusively to this addendum without the controlled standalone addendum redline.
- System categories are engineering mappings from affected sections and descriptions; confirm against the official 2024 index.

## Validation
- Appendix C inventory row represented: **Pass**.
- All 1 listed section references represented: **Pass**.
- Systems and functional categories populated: **Pass with mapping limitation**.
- 2021-to-2024 evidence status: **Complete**.
- CDL implementation status: **Not assessed by this PDF-based workflow**.
