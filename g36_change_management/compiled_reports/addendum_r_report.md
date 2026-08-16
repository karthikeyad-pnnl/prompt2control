# ASHRAE Guideline 36-2024 Addendum r Report

## Inventory
- **Description:** Addresses a potential issue where condenser water supply temperature setpoint could get “stuck” if load were to suddenly increase, making it impossible for CWST to achieve setpoint + 0.5°F for hours on end.
- **ASHRAE approval date:** March 14, 2024
- **Affected sections:** 5.20.12.2
- **Appendix C PDF page(s):** 307

## Methodology and limitations
The supplied `addendum_a_analysis.py` extraction workflow was run in `--all` mode against the supplied 2021 and 2024 PDFs. It extracted Appendix C inventory rows and section-level evidence. The comparisons below use that evidence and normalized word-level alignment; they are not a substitute for the controlled standalone addendum redline. Because the 2024 PDF is consolidated, unrelated cumulative edits in an affected section are not independently attributed to this addendum.

## Impact classification
- **Systems impacted:** Condenser-water systems; Central plants
- **Primary functional category:** Setpoint generation
- **Secondary functional categories:** Hydronic control, Plant optimization
- **Comparison status:** Complete
- **Quality level:** Partially verified

## Section-level comparison
### Section 5.20.12.2
- **2021 reference:** PDF page(s) 213, 214, 215, 216, 217, 218
- **2024 reference:** PDF page(s) 232, 233, 234, 235, 236, 237
- **2021 excerpt:** 5.20.12.2. Fan Control Use the following CWRT Control Sequence for plants with dynamic load profiles, i.e., those for which PLR may change by more than approximately 25% in any hour. Examples include plants primarily serving a few large air handlers with similar schedules and plants serving intermittent process loads. Delete otherwise. © ASHRAE. Per international copyright law, additional reproduction, distribution, or transmission in either print or digital form is not permitted without ASHRAE's prior written permission. Copyright American Society of Heating, Refrigerating and Air-Conditioning Engine Provided by IHS Markit under license …
- **2024 excerpt:** 5.20.12.2. Fan Control Use the following CWRT Control Sequence for plants with dynamic load profiles, i.e., those for which PLR may change by more than approximately 25% in any hour. Examples include plants primarily serving a few large air handlers with similar schedules and plants serving intermittent process loads. Delete otherwise. ThisfileislicensedtoKarthikeyaDevaprasad(karthikeya.devaprasad@pnnl.gov).DownloadDate:1/28/2025 === PDF page 233 === ASHRAE Guideline 36-2024 231 a. Condenser Water Return Temperature (CWRT) Control 1. Tower fan control is in part dictated by plant part load ratio, PLRplant, which is the ratio of current plant …
- **Textual difference:** replace: 2021 [primarily serving a few large air handlers with similar schedules and plants serving intermittent process loads. Delete otherwise. © ASHRAE. Per international copyright law, additional reproduction, distribution, or transmission in either print or digital form is not permitted without ASHRAE's prior written permission. Copyright American Society of Heating, Refrigerating and Air-Conditioning Engine Provided by IHS Markit under license with ASHRAE - Uncontrolled Copy Licensee=BATTELLE PACIFIC NW DIVISION/5940137102, User=Devaprasad, Karthikeya Not for Resale, 01/27/2022 04:30:51 MST No reproduction or networking permitted without license from IHS Markit --`,,,,```,,,`,`,`,`````,,,``,`-`-`,,`,,`,`,,`--- === PDF page 214 === 212 ASHRAE Guideline 36-2021 a. Condenser Water Return Temperature (CWRT) Control 1. Tower] -> 2024 …
- **Operational interpretation:** Addresses a potential issue where condenser water supply temperature setpoint could get “stuck” if load were to suddenly increase, making it impossible for CWST to achieve setpoint + 0.5°F for hours on end.. The affected behavior should be confirmed against the full section and controlled addendum source before implementation.

## Reviewer notes
- The 2024 source is a consolidated edition; section differences cannot be attributed exclusively to this addendum without the controlled standalone addendum redline.
- System categories are engineering mappings from affected sections and descriptions; confirm against the official 2024 index.

## Validation
- Appendix C inventory row represented: **Pass**.
- All 1 listed section references represented: **Pass**.
- Systems and functional categories populated: **Pass with mapping limitation**.
- 2021-to-2024 evidence status: **Complete**.
- CDL implementation status: **Not assessed by this PDF-based workflow**.
