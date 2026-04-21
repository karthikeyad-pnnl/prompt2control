# Documentation Review Feedback

## Mandatory Edit Suggestions

These suggestions address direct violations of the Buildings Library documentation rules. The main issues are in the revisions formatting (missing <i> tags), hyperlink escaping (double-escaping that may hinder rendering), and line lengths exceeding ~80 characters in <ul> items and <p> descriptions, which impacts source code readability.

1. **Revisions missing italics for date and author**: Rule 9 requires reverse chronological `<ul><li>` entries with `<i>` tags around the date and author (e.g., `<i>January 15, 2024</i> by Jane Doe`). The single entry lacks this, and the date "July 29, 2025" is future-dated (possibly a placeholder, but format still needs fixing).  
   **Suggested change**: Update the revisions section to:  
   ```  
   <ul>  
   <li><i>July 29, 2025</i> by Karthik Devaprasad:<br/>  
   First implementation.  
   </li>  
   </ul>  
   ```  
   This aligns precisely with the rule 9 example.

2. **Line lengths exceeding ~80 characters**: Rule 3 specifies a soft limit of ~80 characters per line. Several <li> items in the intro <ul> and <p> in "Details" exceed this, e.g., the sentence "Uses the heating plant enable <code>u1EnaHea</code> and cooling plant enable <code>u1EnaCoo</code> signals to determine operation mode <code>yMod</code> (heating-only, cooling-only, or heating-cooling) for the SHC HP." (over 140 chars). Similarly, the first <li> in intro <ul> is long.  
   **Suggested change**: Break lines with <br/> for readability. For the long <p> sentence:  
   ```  
   <p>  
   Uses the heating plant enable <code>u1EnaHea</code> and cooling plant enable<br/>  
   <code>u1EnaCoo</code> signals to determine operation mode <code>yMod</code><br/>  
   (heating-only, cooling-only, or heating-cooling) for the SHC HP. This also influences<br/>  
   the staging order <code>yStaEqu</code> and the equipment rotation index signal<br/>  
   <code>yIdxSta</code>.  
   </p>  
   ```  
   For the first intro <li>:  
   ```  
   <li>  
   In heating and cooling mode operation of the plant, the modular single-mode heat<br/>  
   pumps shall nelead-lag controlled per the definitions in<br/>  
   <a href="modelica://Buildings.Templates.Plants.Controls.StagingRotation.SortRuntime">  
   Buildings.Templates.Plants.Controls.StagingRotation.SortRuntime</a>.  
   </li>  
   ```  
   (Note: "nelead-lag" appears to be a typo for "be lead-lag"; fix to "be lead-lag" during spell check per rule 10.) Apply to all >80-char lines.

3. **Hyperlink escaping inconsistent**: Rule 8 requires fully qualified `modelica://` with appropriate escaping for Modelica strings (e.g., `href=\"modelica://...\"`), but the current uses double-escaping (`\\"modelica://\\"`), which could break in some parsers. There are two instances (SortRuntime and EquipmentEnable).  
   **Suggested change**: Standardize to single-escaped:  
   ```  
   <a href="modelica://Buildings.Templates.Plants.Controls.StagingRotation.SortRuntime">  
   Buildings.Templates.Plants.Controls.StagingRotation.SortRuntime</a>  
   ```  
   And for the second:  
   ```  
   <a href="modelica://Buildings.Templates.Plants.Controls.StagingRotation.EquipmentEnable">  
   Buildings.Templates.Plants.Controls.StagingRotation.EquipmentEnable</a>  
   ```  
   In the Modelica annotation, ensure outer quotes are escaped as needed.

4. **Inline logic gate not using <code> for reference**: Rule 5 specifies <code> for parameter/code references, but "<i>and</i> gate (<code>and2</code>)" mixes <i> and <code> inconsistently; "and" should be plain or <code> if code-like.  
   **Suggested change**: Update to:  
   ```  
   using an <code>and</code> gate (<code>and2</code>).  
   ```  
   This treats "and" as a logical operator reference, consistent with <code> usage.

## Suggested Edits

These address potential gaps where information is missing or could be added for completeness, following the optional sections in rule 4 (Info Section Template). The documentation explains hybrid logic but omits assumptions (e.g., matrix requirements), typical parameters (e.g., staEquDouMod), and validation, which would benefit users integrating with staging blocks (from variables/connections).

1. **Add "Assumptions and limitations" section**: Rule 4 lists this as optional; it's missing but crucial for clarifying matrix dependencies and hybrid assumptions (e.g., SHC HP in stage 1). Connections show switches (swi) for matrices, implying non-decreasing requirements.  
   **Suggested addition**: Insert after the intro <ul> and before <h4>Details</h4>:  
   ```  
   <h4>Assumptions and limitations</h4>  
   <p>  
   Assumes <code>staEquDouMod</code> and <code>staEquSinMod</code> matrices satisfy non-decreasing<br/>  
   equipment per stage (see EquipmentEnable). SHC HP operates in stage 1 for heating-cooling;<br/>  
   modular HPs follow lead/lag order. Requires <code>is_HpShc</code> vector to identify SHC units.<br/>  
   No fault handling; all HPs assumed available unless <code>u1Hp</code> indicates otherwise.<br/>  
   Runtime sorting (<code>have_sorRunTim</code>) must be handled upstream if enabled.  
   </p>  
   ```  
   This ties to parameters like nSta, nEquAlt and internals like conStaDouMod.

2. **Add "Typical use and important parameters" section**: Missing per rule 4; the "Details" <p> mentions parameters but doesn't guide usage. Highlight keys like staEquDouMod, have_sorRunTim from variables.  
   **Suggested addition**: Insert after "Assumptions and limitations":  
   ```  
   <h4>Typical use and important parameters</h4>  
   <p>  
   Use in hybrid air-to-water heat pump plants combining SHC and modular HPs.<br/>  
   Connect <code>u1EnaHea</code>/<code>u1EnaCoo</code> from plant enables,<br/>  
   <code>u1Hp</code> from HP status, and <code>uMod</code> from 2-pipe mode.<br/>  
   Key parameters: <code>staEquDouMod</code> (matrix for heating-cooling, size nSta x nEqu),<br/>  
   <code>staEquSinMod</code> (for single modes), <code>is_HpShc</code> (vector marking SHC HPs,<br/>  
   e.g., {false, ..., true} for last as SHC), <code>have_sorRunTim</code> (enable rotation).<br/>  
   Outputs like <code>yMod</code> feed to EquipmentEnable for staging.  
   </p>  
   ```  
   References defaultComponentName "ctlPlaHyb" for drag-and-drop (rule 10).

3. **Expand "References" section**: Rule 4 includes this as optional; current hyperlinks are inline, but a dedicated <h4>References</h4> would organize them better, especially since "Details" repeats the EquipmentEnable link.  
   **Suggested addition**: At the end of info, after the last <p>:  
   ```  
   <h4>References</h4>  
   <ul>  
   <li>  
   Lead-lag runtime sorting: <a href="modelica://Buildings.Templates.Plants.Controls.StagingRotation.SortRuntime">  
   Buildings.Templates.Plants.Controls.StagingRotation.SortRuntime</a>.  
   </li>  
   <li>  
   Staging matrix requirements: <a href="modelica://Buildings.Templates.Plants.Controls.StagingRotation.EquipmentEnable">  
   Buildings.Templates.Plants.Controls.StagingRotation.EquipmentEnable</a>.  
   </li>  
   </ul>  
   ```  
   Remove redundant inline links from "Details" to avoid duplication.

4. **Enhance parameter descriptions for consistency**: Rule 1 requires short upper-case noun-phrases without periods; most are good (e.g., "Staging matrix for heating-cooling mode – Equipment required for each stage"), but some like "Vector indicating if each HP is an SHC HP; True=Is SHC HP;False=Not SHC HP" for is_HpShc are too verbose and include lowercase.  
   **Suggested change**: Shorten to: "Vector flagging SHC heat pumps (true for SHC, false otherwise)". Ensure internals like swi have descriptions if exposed, e.g., "Switch for staging matrices based on mode".

## General Comments and Recommendations

The documentation is clear and focused, providing a good overview of hybrid plant integration with practical details on mode detection and staging, suitable for advanced users building modular HVAC systems. It complies well with core rules: lower-case HTML, <p> wrapping, <h4> for "Details", <code> for signals/parameters (e.g., <code>u1EnaHea</code>), and <i> for inline terms like <i>and</i> gate (rule 5). The structure uses <ul> effectively for lists, and defaultComponentName="ctlPlaHyb" is appropriate lowerCamelCase (rule 10). Hyperlinks to related blocks enhance usability, and the single revision is concise (though future-dated – verify for release).

**Strengths**:
- Conciseness: Descriptions are technical and direct, e.g., the <ul> in intro succinctly outlines key behaviors without fluff.
- Clarity: Logical flow from intro to details, with explanations of internals like latches and switches tying to outputs (e.g., yHeaCoo). Acronyms like "SHC HP" are used consistently after definition.
- Compliance: No prohibited elements (e.g., no <h1>-<h3>, no figures needed), spell-checked (except possible "nelead-lag" typo – fix per rule 10), and good use of <br/> in places.

**Areas for improvement**:
- **Conciseness**: Some <p> in "Details" repeat concepts (e.g., mode determination mentioned twice); consolidate for ~10% reduction. The staging matrix note could reference upstream blocks more briefly.
- **Clarity**: Define "lead-lag" on first use if not in parent docs (e.g., "lead-lag (rotation based on runtime)"). Use &ge; for inequalities if math appears (none here, but future-proof). The hybrid assumption (SHC in stage 1) could use a simple equation like <i>stage_SHC = 1</i> in heating-cooling (rule 5).
- **Completeness**: Optional sections (rule 4) like "Assumptions and limitations" or "Typical use" would make it more standalone, especially for parameters like nEquAlt (from variables). Add "Validation" if tests exist, e.g., <h4>Validation</h4><p>Verified for mode transitions in hybrid simulations.</p>. For complex packages, reference Buildings.UsersGuide (rule 10) in intro.
- **Consistency and Polish**: Ensure all <code> are for code (e.g., <code>and2</code> is fine, but avoid over-italicizing). Test rendering for broken links due to escaping. Variables like have_heaWat aren't explained – integrate into suggested sections.
- **Overall recommendation**: Strong for a specialized block; mandatory fixes resolve compliance gaps, while additions improve accessibility (aim for 15% length increase). This would align with Buildings library's emphasis on modular, well-documented controls. Validate in a tool like Dymola, focusing on <ul> rendering and line wraps. Consider examples for staEquDouMod in a User's Guide.