# ASHRAE Guideline 36-2024 Addendum z Report

## Inventory
- **Description:** Adds options for humidity limiting logic.
- **ASHRAE approval date:** December 3, 2024
- **Affected sections:** 3.1.1.4; 3.1.4.6; 4.1; 4.2; 4.3; 4.4; 4.5; 4.6; 5.3.6.2; 5.5.8.3; 5.6.8.5; 5.7.8.5; 5.8.8.5; 5.9.8.5; 5.10.8.5; 5.11.8.6; 5.12.8.6; 5.13.8.6; 5.14.8.6; 5.16.2.2; 5.16.2.3
- **Appendix C PDF page(s):** 307, 308

## Methodology and limitations
The supplied `addendum_a_analysis.py` extraction workflow was run in `--all` mode against the supplied 2021 and 2024 PDFs. It extracted Appendix C inventory rows and section-level evidence. The comparisons below use that evidence and normalized word-level alignment; they are not a substitute for the controlled standalone addendum redline. Because the 2024 PDF is consolidated, unrelated cumulative edits in an affected section are not independently attributed to this addendum.

## Impact classification
- **Systems impacted:** Humidity-control systems; Air handling units; Multiple-zone VAV air handling units; VAV terminal units; Generic sequences or cross-system functions
- **Primary functional category:** Humidity control
- **Secondary functional categories:** Setpoint generation
- **Comparison status:** Partial
- **Quality level:** Partially verified

## Section-level comparison
### Section 3.1.1.4
- **2021 reference:** PDF page(s) not located
- **2024 reference:** PDF page(s) 8, 9
- **2021 excerpt:** Not located in the supplied edition.
- **2024 excerpt:** 3.1.1.4. Zone Dew Point Temperature (DPT) High Limits For Climate Zones 0A, 1A, 2A, and 3A, ASHRAE Standard 90.1 requires supply air temperature reset to be unimpeded by dehumidification controls, thus implying the use of separate outdoor air cooling coil, dedicated outdoor air system, etc., all of which are currently outside the scope of ASHRAE Guideline 36. For all other Climate Zones, ASHRAE Standard 90.1 allows humidity controls to adjust the supply air temperature reset in multiple-zone HVAC systems. ASHRAE Guideline 36 provides a means for this adjustment as described below. At the designer’s option, this limit may be imposed based on …
- **Textual difference:** New section/content in 2024; no corresponding 2021 section was extracted.
- **Operational interpretation:** Adds options for humidity limiting logic.. The affected behavior should be confirmed against the full section and controlled addendum source before implementation.

### Section 3.1.4.6
- **2021 reference:** PDF page(s) not located
- **2024 reference:** PDF page(s) 16, 17
- **2021 excerpt:** Not located in the supplied edition.
- **2024 excerpt:** 3.1.4.6. Humidity limits For Climate Zones 0A, 1A, 2A, and 3A, ASHRAE Standard 90.1 requires supply air temperature reset to be unimpeded by dehumidification controls, thus implying the use of separate outdoor air cooling coil, dedicated outdoor air system, etc., all of which are currently outside the scope of ASHRAE Guideline 36. For all other Climate Zones, ASHRAE Standard 90.1 allows humidity controls to adjust the supply air temperature reset in multiple-zone HVAC systems. ASHRAE Guideline 36 provides a means for this adjustment as described below. At the designer’s option, this limit may be imposed based on outdoor air dew point, return …
- **Textual difference:** New section/content in 2024; no corresponding 2021 section was extracted.
- **Operational interpretation:** Adds options for humidity limiting logic.. The affected behavior should be confirmed against the full section and controlled addendum source before implementation.

### Section 4.1
- **2021 reference:** PDF page(s) not located
- **2024 reference:** PDF page(s) 3
- **2021 excerpt:** Not located in the supplied edition.
- **2024 excerpt:** Not located in the supplied edition.
- **Textual difference:** Comparison unavailable from the supplied extraction evidence.
- **Operational interpretation:** Adds options for humidity limiting logic.. The affected behavior should be confirmed against the full section and controlled addendum source before implementation.

### Section 4.2
- **2021 reference:** PDF page(s) not located
- **2024 reference:** PDF page(s) 3
- **2021 excerpt:** Not located in the supplied edition.
- **2024 excerpt:** Not located in the supplied edition.
- **Textual difference:** Comparison unavailable from the supplied extraction evidence.
- **Operational interpretation:** Adds options for humidity limiting logic.. The affected behavior should be confirmed against the full section and controlled addendum source before implementation.

### Section 4.3
- **2021 reference:** PDF page(s) not located
- **2024 reference:** PDF page(s) 3
- **2021 excerpt:** Not located in the supplied edition.
- **2024 excerpt:** Not located in the supplied edition.
- **Textual difference:** Comparison unavailable from the supplied extraction evidence.
- **Operational interpretation:** Adds options for humidity limiting logic.. The affected behavior should be confirmed against the full section and controlled addendum source before implementation.

### Section 4.4
- **2021 reference:** PDF page(s) not located
- **2024 reference:** PDF page(s) 3
- **2021 excerpt:** Not located in the supplied edition.
- **2024 excerpt:** Not located in the supplied edition.
- **Textual difference:** Comparison unavailable from the supplied extraction evidence.
- **Operational interpretation:** Adds options for humidity limiting logic.. The affected behavior should be confirmed against the full section and controlled addendum source before implementation.

### Section 4.5
- **2021 reference:** PDF page(s) not located
- **2024 reference:** PDF page(s) 3
- **2021 excerpt:** Not located in the supplied edition.
- **2024 excerpt:** Not located in the supplied edition.
- **Textual difference:** Comparison unavailable from the supplied extraction evidence.
- **Operational interpretation:** Adds options for humidity limiting logic.. The affected behavior should be confirmed against the full section and controlled addendum source before implementation.

### Section 4.6
- **2021 reference:** PDF page(s) not located
- **2024 reference:** PDF page(s) 3
- **2021 excerpt:** Not located in the supplied edition.
- **2024 excerpt:** Not located in the supplied edition.
- **Textual difference:** Comparison unavailable from the supplied extraction evidence.
- **Operational interpretation:** Adds options for humidity limiting logic.. The affected behavior should be confirmed against the full section and controlled addendum source before implementation.

### Section 5.3.6.2
- **2021 reference:** PDF page(s) not located
- **2024 reference:** PDF page(s) 80
- **2021 excerpt:** Not located in the supplied edition.
- **2024 excerpt:** 5.3.6.2. Zone Dew Point Alarms a. See Section 3.1.1.4 for zone dew point high limits. b. High dew point alarm 1. If the zone is less than or equal to 1°C (2°F) above the dew point limit for 6 hours, generate a Level 4 alarm. 2. If the zone is less than or equal to 1°C (2°F) above the dew point limit for 12 hours, generate a Level 3 alarm. 3. If the zone is less than or equal to 1°C (2°F) above the dew point limit for 24 hours, generate a Level 2 alarm. 4. If the zone is greater than 1°C (2°F) above the dew point limit for 2 hours, generate a Level 3 alarm. 5. If the zone is greater than 2°C (4°F) above the dew point limit for 8 hours, …
- **Textual difference:** New section/content in 2024; no corresponding 2021 section was extracted.
- **Operational interpretation:** Adds options for humidity limiting logic.. The affected behavior should be confirmed against the full section and controlled addendum source before implementation.

### Section 5.5.8.3
- **2021 reference:** PDF page(s) not located
- **2024 reference:** PDF page(s) 86
- **2021 excerpt:** Not located in the supplied edition.
- **2024 excerpt:** 5.5.8.3. For zones with a humidity sensor and a dew point high limit assigned to the zone per Section 3.1.1.4, Humidity SAT Limit Requests. a. If the zone dew point exceeds the limit by 3°C (5°F) for 30 minutes and after suppression period due to setpoint change per Section 5.1.20, send 3 requests. b. Else if the zone dew point exceeds the limit by 2°C (3°F) for 30 minutes and after suppression period due to setpoint change per Section 5.1.20, send 2 requests. c. Else if the zone dew point exceeds the limit for 30 minutes and after suppression period due to setpoint change per Section 5.1.20, send 1 request until the zone dew point is less …
- **Textual difference:** New section/content in 2024; no corresponding 2021 section was extracted.
- **Operational interpretation:** Adds options for humidity limiting logic.. The affected behavior should be confirmed against the full section and controlled addendum source before implementation.

### Section 5.6.8.5
- **2021 reference:** PDF page(s) not located
- **2024 reference:** PDF page(s) 90
- **2021 excerpt:** Not located in the supplied edition.
- **2024 excerpt:** 5.6.8.5. For zones with a humidity sensor and a dew point high limit assigned to the zone per Section 3.1.1.4, Humidity SAT Limit Requests. a. If the zone dew point exceeds the limit by 3°C (5°F) for 30 minutes and after suppression period due to setpoint change per Section 5.1.20, send 3 requests. b. Else if the zone dew point exceeds the limit by 2°C (3°F) for 30 minutes and after suppression period due to setpoint change per Section 5.1.20, send 2 requests. c. Else if the zone dew point exceeds the limit for 30 minutes and after suppression period due to setpoint change per Section 5.1.20, send 1 request until the zone dew point is less …
- **Textual difference:** New section/content in 2024; no corresponding 2021 section was extracted.
- **Operational interpretation:** Adds options for humidity limiting logic.. The affected behavior should be confirmed against the full section and controlled addendum source before implementation.

### Section 5.7.8.5
- **2021 reference:** PDF page(s) not located
- **2024 reference:** PDF page(s) 94, 95
- **2021 excerpt:** Not located in the supplied edition.
- **2024 excerpt:** 5.7.8.5. For zones with a humidity sensor and a dew point high limit assigned to the zone per Section 3.1.1.4, Humidity SAT Limit Requests. ThisfileislicensedtoKarthikeyaDevaprasad(karthikeya.devaprasad@pnnl.gov).DownloadDate:1/28/2025 === PDF page 95 === ASHRAE Guideline 36-2024 93 a. If the zone dew point exceeds the limit by 3°C (5°F) for 30 minutes and after suppression period due to setpoint change per Section 5.1.20, send 3 requests. b. Else if the zone dew point exceeds the limit by 2°C (3°F) for 30 minutes and after suppression period due to setpoint change per Section 5.1.20, send 2 requests. c. Else if the zone dew point exceeds …
- **Textual difference:** New section/content in 2024; no corresponding 2021 section was extracted.
- **Operational interpretation:** Adds options for humidity limiting logic.. The affected behavior should be confirmed against the full section and controlled addendum source before implementation.

### Section 5.8.8.5
- **2021 reference:** PDF page(s) not located
- **2024 reference:** PDF page(s) 100
- **2021 excerpt:** Not located in the supplied edition.
- **2024 excerpt:** 5.8.8.5. For zones with a humidity sensor and a dew point high limit assigned to the zone per Section 3.1.1.4, Humidity SAT Limit Requests. a. If the zone dew point exceeds the limit by 3°C (5°F) for 30 minutes and after suppression period due to setpoint change per Section 5.1.20, send 3 requests. b. Else if the zone dew point exceeds the limit by 2°C (3°F) for 30 minutes and after suppression period due to setpoint change per Section 5.1.20, send 2 requests. c. Else if the zone dew point exceeds the limit for 30 minutes and after suppression period due to setpoint change per Section 5.1.20, send 1 request until the zone dew point is less …
- **Textual difference:** New section/content in 2024; no corresponding 2021 section was extracted.
- **Operational interpretation:** Adds options for humidity limiting logic.. The affected behavior should be confirmed against the full section and controlled addendum source before implementation.

### Section 5.9.8.5
- **2021 reference:** PDF page(s) not located
- **2024 reference:** PDF page(s) 104
- **2021 excerpt:** Not located in the supplied edition.
- **2024 excerpt:** 5.9.8.5. For zones with a humidity sensor and a dew point high limit assigned to the zone per Section 3.1.1.4, Humidity SAT Limit Requests. a. If the zone dew point exceeds the limit by 3°C (5°F) for 30 minutes and after suppression period due to setpoint change per Section 5.1.20, send 3 requests. b. Else if the zone dew point exceeds the limit by 2°C (3°F) for 30 minutes and after suppression period due to setpoint change per Section 5.1.20, send 2 requests. c. Else if the zone dew point exceeds the limit for 30 minutes and after suppression period due to setpoint change per Section 5.1.20, send 1 request until the zone dew point is less …
- **Textual difference:** New section/content in 2024; no corresponding 2021 section was extracted.
- **Operational interpretation:** Adds options for humidity limiting logic.. The affected behavior should be confirmed against the full section and controlled addendum source before implementation.

### Section 5.10.8.5
- **2021 reference:** PDF page(s) not located
- **2024 reference:** PDF page(s) 108, 109
- **2021 excerpt:** Not located in the supplied edition.
- **2024 excerpt:** 5.10.8.5. For zones with a humidity sensor and a dew point high limit assigned to the zone per Section 3.1.1.4, Humidity SAT Limit Requests. a. If the zone dew point exceeds the limit by 3°C (5°F) for 30 minutes and after suppression period due to setpoint change per Section 5.1.20, send 3 requests. b. Else if the zone dew point exceeds the limit by 2°C (3°F) for 30 minutes and after suppression period due to setpoint change per Section 5.1.20, send 2 requests. c. Else if the zone dew point exceeds the limit for 30 minutes and after suppression period due to setpoint change per Section 5.1.20, send 1 request until the zone dew point is less …
- **Textual difference:** New section/content in 2024; no corresponding 2021 section was extracted.
- **Operational interpretation:** Adds options for humidity limiting logic.. The affected behavior should be confirmed against the full section and controlled addendum source before implementation.

### Section 5.11.8.6
- **2021 reference:** PDF page(s) not located
- **2024 reference:** PDF page(s) 114
- **2021 excerpt:** Not located in the supplied edition.
- **2024 excerpt:** 5.11.8.6. For zones with a humidity sensor and a dew point high limit assigned to the zone per Section 3.1.1.4, Humidity SAT Limit Requests. a. If the zone dew point exceeds the limit by 3°C (5°F) for 30 minutes and after suppression period due to setpoint change per Section 5.1.20, send 3 requests. b. Else if the zone dew point exceeds the limit by 2°C (3°F) for 30 minutes and after suppression period due to setpoint change per Section 5.1.20, send 2 requests. c. Else if the zone dew point exceeds the limit for 30 minutes and after suppression period due to setpoint change per Section 5.1.20, send 1 request until the zone dew point is less …
- **Textual difference:** New section/content in 2024; no corresponding 2021 section was extracted.
- **Operational interpretation:** Adds options for humidity limiting logic.. The affected behavior should be confirmed against the full section and controlled addendum source before implementation.

### Section 5.12.8.6
- **2021 reference:** PDF page(s) not located
- **2024 reference:** PDF page(s) 117, 118
- **2021 excerpt:** Not located in the supplied edition.
- **2024 excerpt:** 5.12.8.6. For zones with a humidity sensor and a dew point high limit assigned to the zone per Section 3.1.1.4, Humidity SAT Limit Requests. ThisfileislicensedtoKarthikeyaDevaprasad(karthikeya.devaprasad@pnnl.gov).DownloadDate:1/28/2025 === PDF page 118 === 116 ASHRAE Guideline 36-2024 a. If the zone dew point exceeds the limit by 3°C (5°F) for 30 minutes and after suppression period due to setpoint change per Section 5.1.20, send 3 requests. b. Else if the zone dew point exceeds the limit by 2°C (3°F) for 30 minutes and after suppression period due to setpoint change per Section 5.1.20, send 2 requests. c. Else if the zone dew point exceeds …
- **Textual difference:** New section/content in 2024; no corresponding 2021 section was extracted.
- **Operational interpretation:** Adds options for humidity limiting logic.. The affected behavior should be confirmed against the full section and controlled addendum source before implementation.

### Section 5.13.8.6
- **2021 reference:** PDF page(s) not located
- **2024 reference:** PDF page(s) 121, 122
- **2021 excerpt:** Not located in the supplied edition.
- **2024 excerpt:** 5.13.8.6. For zones with a humidity sensor and a dew point high limit assigned to the zone per Section 3.1.1.4, Humidity SAT Limit Requests. ThisfileislicensedtoKarthikeyaDevaprasad(karthikeya.devaprasad@pnnl.gov).DownloadDate:1/28/2025 === PDF page 122 === 120 ASHRAE Guideline 36-2024 a. If the zone dew point exceeds the limit by 3°C (5°F) for 30 minutes and after suppression period due to setpoint change per Section 5.1.20, send 3 requests. b. Else if the zone dew point exceeds the limit by 2°C (3°F) for 30 minutes and after suppression period due to setpoint change per Section 5.1.20, send 2 requests. c. Else if the zone dew point exceeds …
- **Textual difference:** New section/content in 2024; no corresponding 2021 section was extracted.
- **Operational interpretation:** Adds options for humidity limiting logic.. The affected behavior should be confirmed against the full section and controlled addendum source before implementation.

### Section 5.14.8.6
- **2021 reference:** PDF page(s) not located
- **2024 reference:** PDF page(s) 125, 126
- **2021 excerpt:** Not located in the supplied edition.
- **2024 excerpt:** 5.14.8.6. For zones with a humidity sensor and a dew point high limit assigned to the zone per Section 3.1.1.4, Humidity SAT Limit Requests. a. If the zone dew point exceeds the limit by 3°C (5°F) for 30 minutes and after suppression period due to setpoint change per Section 5.1.20, send 3 requests. ThisfileislicensedtoKarthikeyaDevaprasad(karthikeya.devaprasad@pnnl.gov).DownloadDate:1/28/2025 === PDF page 126 === 124 ASHRAE Guideline 36-2024 b. Else if the zone dew point exceeds the limit by 2°C (3°F) for 30 minutes and after suppression period due to setpoint change per Section 5.1.20, send 2 requests. c. Else if the zone dew point exceeds …
- **Textual difference:** New section/content in 2024; no corresponding 2021 section was extracted.
- **Operational interpretation:** Adds options for humidity limiting logic.. The affected behavior should be confirmed against the full section and controlled addendum source before implementation.

### Section 5.16.2.2
- **2021 reference:** PDF page(s) 112, 113, 114
- **2024 reference:** PDF page(s) 128, 129, 130
- **2021 excerpt:** 5.16.2.2. Supply Air Temperature Setpoint The default range of outdoor air temperatures [21°C (70°F) –16°C (60°F)] used to reset the Occupied Mode SAT setpoint was chosen to maximize economizer hours. It may be preferable to use a lower range of OATs (e.g., 18°C [65°F] – 13°C [55°F]) to minimize fan energy if there is a 24/7 chiller plant that is running anyway; reheat is minimized, as in a VAV dual-fan dual-duct system, or the climate severely limits the number of available economizer hours. If using this logic, the engineer should oversize interior zones and rooms with high cooling loads (design them to be satisfied by the warmest SAT) so …
- **2024 excerpt:** 5.16.2.2. Supply Air Temperature Setpoint The default range of outdoor air temperatures [21°C (70°F) –16°C (60°F)] used to reset the Occupied Mode SAT setpoint was chosen to maximize economizer hours. It may be preferable to use a lower range of OATs (e.g., 18°C [65°F] – 13°C [55°F]) to minimize fan energy if there is a 24/7 chiller plant that is running anyway; reheat is minimized, as in a VAV dual-fan dual-duct system, or the climate severely limits the number of available economizer hours. This lower range also can be used to indirectly limit zone humidity in humid climates, e.g. setting both Max_ClgSAT and OAT_Max to 16°C (60°F) ensures …
- **Textual difference:** insert: 2021 [as in a VAV dual-fan dual-duct system, or the climate severely limits the number of available economizer hours. If using this logic, the engineer should oversize interior zones and rooms with high cooling loads (design them] -> 2024 [as in a VAV dual-fan dual-duct system, or the climate severely limits the number of available economizer hours. This lower range also can be used to indirectly limit zone humidity in humid climates, e.g. setting both Max_ClgSAT and OAT_Max to 16°C (60°F) ensures that supply air dew point temperature is always below 16°C (60°F), effectively maintaining space dew point temperature below that limit in zones with low latent loads such as offices. See Section 5.16.2.3 for other more direct ways to limit zone humidity. If using this logic, the engineer should oversize interior zones and rooms with …
- **Operational interpretation:** Adds options for humidity limiting logic.. The affected behavior should be confirmed against the full section and controlled addendum source before implementation.

### Section 5.16.2.3
- **2021 reference:** PDF page(s) 114, 115, 116, 117
- **2024 reference:** PDF page(s) 130, 131
- **2021 excerpt:** 5.16.2.3. Supply air temperature shall be controlled to setpoint using a control loop whose output is mapped to sequence the heating coil (if applicable), outdoor air damper, return air damper, and cooling coil as shown in Figure 5.16.2.3. The engineer must specify whether the unit has a return fan, relief damper or relief fans. If there is a return fan, keep subsection (a) and delete subsection (b). If there are relief dampers or relief fans, keep subsection (b) and delete subsection (a). Delete this flag note after selections have been made. a. For units with return fans 1. Return air damper maximum position MaxRA-P is modulated to control …
- **2024 excerpt:** 5.16.2.3. Supply Air Temperature Setpoint Limit for Humidity Control a. The Humidity_SAT_Limit shall be the lowest value dictated by the following strategies: Note that control based on outdoor air dew point will prevent the introduction of large volumes of humid ventilation air, but will not respond to elevated indoor humidity conditions. 1. Based on outdoor air dew point temperature i. See Sections 3.1.4.6 for OADPT_Min and OADPT_Max. ii. Humidity_SAT_Limit shall be reset from Min_ClgSAT when the outdoor air dew point is OADPT_Max and above, proportionally up to Max_ClgSAT when the outdoor air dew point is OADPT_Min and below. Note that …
- **Textual difference:** replace: 2021 [5.16.2.3. Supply air temperature shall be controlled to setpoint using a control loop whose output is mapped to sequence the heating coil] -> 2024 [5.16.2.3. Supply Air Temperature Setpoint Limit for Humidity Control a. The Humidity_SAT_Limit shall be the lowest value dictated by the following strategies: Note that control based on outdoor air dew] | replace: 2021 [5.16.2.3. Supply air temperature shall be controlled to setpoint using a control loop whose output is mapped to sequence the heating coil (if applicable), outdoor air damper, return air] -> 2024 [5.16.2.3. Supply Air Temperature Setpoint Limit for Humidity Control a. The Humidity_SAT_Limit shall be the lowest value dictated by the following strategies: Note that control based on outdoor air dew point will prevent the introduction of large volumes of humid …
- **Operational interpretation:** Adds options for humidity limiting logic.. The affected behavior should be confirmed against the full section and controlled addendum source before implementation.

## Reviewer notes
- The 2024 source is a consolidated edition; section differences cannot be attributed exclusively to this addendum without the controlled standalone addendum redline.
- System categories are engineering mappings from affected sections and descriptions; confirm against the official 2024 index.
- At least one affected section was not cleanly isolated by the PDF extractor and requires manual page-level review.
- Appendix C description contains a trailing repeated column label; it was removed during normalization.

## Validation
- Appendix C inventory row represented: **Pass**.
- All 21 listed section references represented: **Pass**.
- Systems and functional categories populated: **Pass with mapping limitation**.
- 2021-to-2024 evidence status: **Partial**.
- CDL implementation status: **Not assessed by this PDF-based workflow**.
