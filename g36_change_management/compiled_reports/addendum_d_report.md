# ASHRAE Guideline 36-2024 Addendum d Report

## Inventory
- **Description:** Addresses an issue with heating control for VAV boxes with hot water reheat coils when Vmin* is zero due to no occupancy indicated by the occupancy sensor in occupied-standby mode.
- **ASHRAE approval date:** March 14, 2024
- **Affected sections:** 5.6.4
- **Appendix C PDF page(s):** 306

## Methodology and limitations
The supplied `addendum_a_analysis.py` extraction workflow was run in `--all` mode against the supplied 2021 and 2024 PDFs. It extracted Appendix C inventory rows and section-level evidence. The comparisons below use that evidence and normalized word-level alignment; they are not a substitute for the controlled standalone addendum redline. Because the 2024 PDF is consolidated, unrelated cumulative edits in an affected section are not independently attributed to this addendum.

## Impact classification
- **Systems impacted:** VAV terminal units; Hot-water plants; Hydronic distribution systems
- **Primary functional category:** Mode or state logic
- **Secondary functional categories:** Sensor validation or calibration
- **Comparison status:** Complete
- **Quality level:** Partially verified

## Section-level comparison
### Section 5.6.4
- **2021 reference:** PDF page(s) 75, 76
- **2024 reference:** PDF page(s) 86, 87
- **2021 excerpt:** 5.6.4. Active endpoints used in the control logic depicted in Figure 5.6.5 shall vary depending on the mode of the Zone Group the zone is a part of (see Table 5.6.4). Table 5.6.4 Endpoints as a Function of Zone Group Mode Endpoint Occupied Cooldown Setup Warmup Setback Unoccupied Cooling maximum Vcool-max Vcool-max Vcool-max 0 0 0 Cooling minimum Vmin* 0 0 0 0 0 Minimum Vmin* 0 0 0 0 0 Heating minimum Max (Vheat-min, min*) Vheat-min 0 Vheat-max Vheat-max 0 Heating maximum Max (Vheat-max, min*) Vheat-max 0 Vcool-max Vcool-max 0 © ASHRAE. Per international copyright law, additional reproduction, distribution, or transmission in either print or …
- **2024 excerpt:** 5.6.4. Active endpoints used in the control logic depicted in Figure 5.6.5 shall vary depending on the mode of the Zone Group the zone is a part of (see Table 5.6.4). Table 5.6.4 Endpoints as a Function of Zone Group Mode Endpoint Occupied Cooldown Setup Warmup Setback Unoccupied Cooling maximum Vcool-max Vcool-max Vcool-max 0 0 0 Cooling minimum Vmin* 0 0 0 0 0 Minimum Vmin* 0 0 0 0 0 Heating minimum Max (Vheat-min, Vmin*, Vm) Vheat-min 0 Vheat-max Vheat-max 0 Heating maximum Max (Vheat-max, Vmin*) Vheat-max 0 Vcool-max Vcool-max 0 These sequences use different maximum airflow setpoints for heating and cooling. This dual-max logic allows …
- **Textual difference:** replace: 2021 [minimum Vmin* 0 0 0 0 0 Minimum Vmin* 0 0 0 0 0 Heating minimum Max (Vheat-min, min*) Vheat-min 0 Vheat-max Vheat-max 0 Heating maximum Max (Vheat-max, min*) Vheat-max 0 Vcool-max Vcool-max 0 © ASHRAE. Per] -> 2024 [minimum Vmin* 0 0 0 0 0 Minimum Vmin* 0 0 0 0 0 Heating minimum Max (Vheat-min, Vmin*, Vm) Vheat-min 0 Vheat-max Vheat-max 0 Heating maximum Max (Vheat-max, Vmin*) Vheat-max 0 Vcool-max Vcool-max 0 These sequences use] | replace: 2021 [0 0 0 0 Heating minimum Max (Vheat-min, min*) Vheat-min 0 Vheat-max Vheat-max 0 Heating maximum Max (Vheat-max, min*) Vheat-max 0 Vcool-max Vcool-max 0 © ASHRAE. Per international copyright law, additional reproduction, distribution, or transmission in either] -> 2024 [0 0 0 Heating minimum Max (Vheat-min, Vmin*, Vm) Vheat-min 0 Vheat-max Vheat-max 0 Heating maximum Max …
- **Operational interpretation:** Addresses an issue with heating control for VAV boxes with hot water reheat coils when Vmin* is zero due to no occupancy indicated by the occupancy sensor in occupied-standby mode.. The affected behavior should be confirmed against the full section and controlled addendum source before implementation.

## Reviewer notes
- The 2024 source is a consolidated edition; section differences cannot be attributed exclusively to this addendum without the controlled standalone addendum redline.
- System categories are engineering mappings from affected sections and descriptions; confirm against the official 2024 index.

## Validation
- Appendix C inventory row represented: **Pass**.
- All 1 listed section references represented: **Pass**.
- Systems and functional categories populated: **Pass with mapping limitation**.
- 2021-to-2024 evidence status: **Complete**.
- CDL implementation status: **Not assessed by this PDF-based workflow**.
