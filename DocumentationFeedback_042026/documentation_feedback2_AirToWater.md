# Documentation Review Feedback

## Mandatory Edit Suggestions

These suggestions address direct violations of the Buildings Library documentation rules. The primary issues are in the HTML table structure (missing required attributes and non-descriptive summary) and minor formatting inconsistencies in HTML tags and line lengths.

1. **Table attributes incomplete**: The table lacks required attributes for compliance with rule 6 (Tables). It must include `summary` (descriptive, not placeholder), `border="1"`, `cellspacing="0"`, `cellpadding="2"`, and `style="border-collapse:collapse;"`.  
   **Suggested change**: Replace the table opening tag with:  
   ```<table summary="Supported plant configurations for air-to-water heat pump plants" border="1" cellspacing="0" cellpadding="2" style="border-collapse:collapse;">``  
   This ensures proper rendering and accessibility.

2. **Non-descriptive table summary**: Rule 6 requires a meaningful `summary` attribute. The current `"summary"` is a placeholder and violates this.  
   **Suggested change**: Use the descriptive summary shown in the table fix above.

3. **Line lengths exceeding ~80 characters**: Several lines in the table cells (e.g., notes on defrosting and variable primary plants) exceed the soft limit in rule 3 (HTML General Rules). This affects readability in source code.  
   **Suggested change**: Break long lines, e.g., in the "Type of distribution" row note:  
   Split into:  
   ```It is assumed that the HW and the CHW loops have the``  
   ```same type of distribution, as specified by this parameter.<br/>``  
   ```Most AWHPs on the market use a reverse cycle for defrosting.``  
   ```This requires maximum primary flow during defrost cycles.``  
   Continue splitting subsequent sentences similarly to keep each line ≤80 characters.

4. **Inconsistent escaping in hyperlinks**: Hyperlinks use escaped quotes (e.g., `"modelica://..."`), which is fine in Modelica strings but should be unescaped in rendered HTML for clarity. Rule 8 (Hyperlinks) specifies fully qualified `modelica://` URIs without unnecessary escapes in documentation.  
   **Suggested change**: In the "Details" section, update to:  
   ```<a href="modelica://Buildings.Templates.Plants.Controls.StagingRotation.EquipmentEnable">``  
   ```Buildings.Templates.Plants.Controls.StagingRotation.EquipmentEnable</a>``  
   Similarly for GitHub links in revisions (e.g., unescape to `https://github.com/lbl-srg/modelica-buildings/issues/4432`).

5. **Revisions list formatting**: Rule 9 requires reverse chronological order with `<i>` for dates/authors, but some `<br/>` tags create overly long lines. Dates like "January 23, 2025" are future-dated, which may be intentional but should be italicized consistently.  
   **Suggested change**: Ensure each `<li>` starts with ```<li><i>January 23, 2025</i> by Antoine Gautier:<br/>`` and break descriptions to ≤80 characters, e.g.:  
   ```Refactored to use "required to run" conditions in the``  
   ```equipment availability logic.<br/>``  
   ```This is for <a href="https://github.com/lbl-srg/modelica-buildings/issues/4432">#4432</a>.``  
   Verify chronological order (current is correct: 2025 > 2024 > 2024).

## Suggested Edits

These address potential gaps where information is missing or could be added for completeness, based on the template in rule 4 (Info Section Template). Optional sections like "Assumptions and limitations" are absent but relevant given the model's complexity (e.g., no fault handling mentioned).

1. **Add "Assumptions and limitations" section**: The documentation mentions "At its current stage of development, this controller contains no logic for handling faulted equipment" in "Details," but this fits better in a dedicated `<h4>Assumptions and limitations</h4>` section per the template order. This would improve structure.  
   **Suggested addition**: After the table, insert:  
   ```<h4>Assumptions and limitations</h4>``  
   ```<p>`  
   ```This controller assumes all equipment is available at all times, with no fault handling logic.`  
   ```It supports only centralized secondary pumps; distributed secondary pumps are not supported.`  
   ```Hybrid plants with 4-pipe heat pumps require specific staging matrices.`  
   ```</p>``  
   Move the fault assumption paragraph here from "Details" to avoid redundancy.

2. **Add "Typical use and important parameters" section**: Rule 4 lists this as optional, but it's missing. The variables table (external context) shows many parameters (e.g., `nHp`, `staEqu`); referencing key ones would help users.  
   **Suggested addition**: After "Assumptions and limitations," insert:  
   ```<h4>Typical use and important parameters</h4>`  
   ```<p>`  
   ```Use this block for air-to-water heat pump plants with primary-only or primary-variable secondary distribution.`  
   ```Key parameters include <code>nHp</code> (number of heat pumps), <code>staEqu</code> (staging matrix),`  
   ```and <code>have_pumPriHdr</code> (headered vs. dedicated pumps).`  
   ```See the table above for configuration options.`  
   ```</p>``  
   This ties into the existing table without adding length.

3. **Expand "References" with inline citation**: The intro references "ASHRAE, 2021" but lacks an inline link to the `<li id="ASHRAE2021">`. Rule 5 (Equations) implies consistent referencing; add for hyperlinks.  
   **Suggested change**: In the intro paragraph, update to:  
   ```Most parts of the sequence of operation are similar to that described in`  
   ```<a href="#ASHRAE2021">ASHRAE, 2021</a> for chiller plants.`  
   ```</p>``  
   This improves navigability.

4. **Missing parameter descriptions in external context**: While the provided documentation is the `info` section, the variables list (e.g., `have_sorRunTim`) lacks descriptions in some cases, violating rule 1 (Description Strings). Ensure all parameters in the full model have short noun-phrase descriptions starting with upper-case, no period.  
   **Suggested addition**: For example, add to `have_sorRunTim`:  
   `"Flag to enable runtime sorting for equipment rotation"`

## General Comments and Recommendations

The documentation is generally clear and well-structured, providing a solid introduction and configuration overview via the table. It complies with most rules (e.g., lower-case tags, `<p>` wrapping, `<h4>` headings, `<code>` for parameters, reverse-chronological revisions). The language is concise and technical, suitable for Modelica users in building simulation.

**Strengths**:
- The short intro is required and effective, setting context quickly.
- The table is a strong visual aid for configurations, with good use of `<th>` and notes.
- Hyperlinks and `<code>` usage enhance usability.
- Revisions are detailed and include issue trackers, aiding development traceability.

**Areas for improvement**:
- **Conciseness**: Some table notes are verbose (e.g., defrosting explanation could be tightened: "Most AWHPs use reverse-cycle defrosting, requiring near-design minimum flow in variable primary plants."). Aim to reduce word count by 10-20% without losing meaning.
- **Clarity**: Acronyms like "AWHP" (air-to-water heat pump) and "CHW" (chilled water) are used without initial expansion; add in intro if not defined elsewhere (e.g., "air-to-water heat pumps (AWHPs)").
- **Completeness**: Consider adding a "Validation" or "Implementation" section (optional per rule 4) if test cases or key equations exist. For example, reference staging logic equations using rule 5's display format:  
  ```<p align="center" style="font-style:italic;">``  
  ```y = a<sub>1</sub> + a<sub>2</sub> x + a<sub>3</sub> x<sup>2</sup>`  
  ```</p>``  
  (Adapt to actual equations like part-load ratio `plrSta`.)
- **Consistency**: Ensure all HTML is validated (e.g., no unclosed tags). Run spell check (rule 10) – minor issues like "appplications" in variables (external) should be fixed to "applications".
- **Overall recommendation**: After fixes, the documentation will be more polished and user-friendly. For complex models like this, linking to a User's Guide (rule 10) could provide broader context on integration with `Buildings.Templates.Plants`. Test rendering in Dymola or similar to confirm ~80-char limits and table display.