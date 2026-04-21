# Documentation Review Feedback

## Mandatory Edit Suggestions

These suggestions address direct violations of the Buildings Library documentation rules. Key issues include revisions formatting (missing <i> tags), line length exceedances in paragraphs and lists, and inconsistent hyperlink escaping that may affect rendering.

1. **Revisions missing italics for date and author**: Rule 9 requires `<i>` tags around the date and author in reverse chronological `<ul><li>` entries. Both entries lack this, e.g., "May 31, 2024, by Antoine Gautier" should be italicized for the date and author.  
   **Suggested change**: Update the revisions section to:  
   ```  
   <ul>  
   <li><i>May 31, 2024</i> by Antoine Gautier:<br/>  
   Refactored using <code>LoadAverage</code> block and added failsafe condition.  
   </li>  
   <li><i>March 29, 2024</i> by Antoine Gautier:<br/>  
   First implementation.  
   </li>  
   </ul>  
   ```  
   This ensures exact compliance with the example in rule 9.

2. **Line lengths exceeding ~80 characters**: Rule 3 enforces a soft limit of ~80 characters per line for source readability. Several <p> and <li> items exceed this, e.g., the sentence "When a stage up or stage down transition is initiated, <i>Qrequired</i> is held fixed at its last value until the longer of the successful completion of the stage change and the duration <code>dtRun</code>." (over 120 chars). Similarly, some <li> in the stage up/down conditions.  
   **Suggested change**: Break long lines with <br/> or restructure. For the transition sentence:  
   ```  
   <p>  
   When a stage up or stage down transition is initiated,<br/>  
   <i>Qrequired</i> is held fixed at its last value until the longer of<br/>  
   the successful completion of the stage change<br/>  
   and the duration <code>dtRun</code>.  
   </p>  
   ```  
   For <li> items, e.g., the efficiency condition:  
   ```  
   <li>  
   Efficiency condition: Current stage <i>OPLR &gt; plrSta</i> for a duration of <code>dtRun</code>.  
   </li>  
   ```  
   (Shorten where possible; apply to all >80-char lines, like the details on primary/secondary sensors.)

3. **Hyperlink escaping inconsistent**: Rule 8 specifies fully qualified `modelica://` with escaped quotes for Modelica strings (e.g., `href=\"modelica://...\"`), but the current uses double-escaping like `\\"modelica://\\"`, which may cause parsing issues in some tools.  
   **Suggested change**: Standardize to single-escaped:  
   ```  
   <a href="modelica://Buildings.Templates.Plants.Controls.HeatPumps.AirToWater">  
   Buildings.Templates.Plants.Controls.HeatPumps.AirToWater</a>  
   ```  
   Apply to all three hyperlinks (e.g., StageIndex, EquipmentEnable, FailsafeCondition). In the full Modelica annotation, outer quotes are escaped as needed.

4. **Inline equation not fully formatted as display**: Rule 5 recommends centered italic <p> for display equations. The OPLR equation `<i>OPLR = Qrequired / Qstage</i>` is inline in a <p>, but as a key equation, it should be displayed for emphasis.  
   **Suggested change**: Convert to display format after the first <p>:  
   ```  
   <p align="center" style="font-style:italic;">  
   OPLR = <i>Q<sub>required</sub> / Q<sub>stage</sub></i>  
   </p>  
   ```  
   Use <sub> for subscripts on Q_required and Q_stage to match rule 5's example.

## Suggested Edits

These address gaps where information is missing or could be expanded, aligning with the optional sections in rule 4 (Info Section Template). The doc covers logic well but omits assumptions (e.g., sensor priorities), typical parameters (e.g., dtRun), and validation, which would help given the model's reliance on averages and failsafes from variables/connections.

1. **Add "Assumptions and limitations" section**: Rule 4 lists this as optional; it's absent but relevant for clarifying sensor selection (primary over secondary) and hybrid handling. The "Details" <h4> mentions matrices but not limitations like minimum sampling (30 s).  
   **Suggested addition**: Insert before the final <h4>Details</h4>:  
   ```  
   <h4>Assumptions and limitations</h4>  
   <p>  
   Primary loop sensors are prioritized for <i>Q<sub>required</sub></i> calculation if available.<br/>  
   For hybrid plants (<code>have_HpShc=true</code>), use <code>staEquDouMod</code> in heating-cooling mode.<br/>  
   Assumes constant <code>cp_default</code> and <code>rho_default</code> for capacity; actual fluid properties<br/>  
   may vary. Failsafe conditions (<code>faiSaf</code>) prevent unsafe down-staging but require<br/>  
   accurate <code>TPriSup</code> and <code>TSecSup</code> inputs. No handling for zero flow.  
   </p>  
   ```  
   This incorporates variables like have_pumSec and connections (e.g., LoadAverage for QReq).

2. **Add "Typical use and important parameters" section**: Missing per rule 4; the doc references parameters but doesn't guide setup. Highlight keys like plrSta, dtRun, and staEqu from variables.  
   **Suggested addition**: Insert after the stage down <ul>:  
   ```  
   <h4>Typical use and important parameters</h4>  
   <p>  
   Use in plant controls for heat pumps or chillers to trigger staging based on load.<br/>  
   Connect <code>uSta</code> from stage index block, <code>TRet</code>/<code>V_flow</code> from sensors,<br/>  
   and <code>staEqu</code> matrix defining equipment per stage (size nSta x nEqu).<br/>  
   Key parameters: <code>plrSta</code> (threshold, e.g., 0.8), <code>dtRun</code> (min runtime, e.g., 300 s),<br/>  
   <code>dtMea</code> (average duration, e.g., 600 s), <code>dT</code> (delta-T up trigger).<br/>  
   For primary-secondary (<code>have_pumSec=true</code>), provide <code>TPriSup</code>/<code>TSecSup</code>.  
   </p>  
   ```  
   Ties to defaultComponentName "chaSta" for drag-and-drop (rule 10).

3. **Expand "References" section**: Rule 4 includes this as optional; current hyperlinks are good, but consolidate into a <h4>References</h4> <ul> for better structure, avoiding inline repetition.  
   **Suggested addition**: Replace or append to "Details": Move hyperlinks there:  
   ```  
   <h4>References</h4>  
   <ul>  
   <li>  
   Availability and index logic: <a href="modelica://Buildings.Templates.Plants.Controls.Utilities.StageIndex">  
   Buildings.Templates.Plants.Controls.Utilities.StageIndex</a>.  
   </li>  
   <li>  
   Equipment enable: <a href="modelica://Buildings.Templates.Plants.Controls.StagingRotation.EquipmentEnable">  
   Buildings.Templates.Plants.Controls.StagingRotation.EquipmentEnable</a>.  
   </li>  
   <li>  
   Failsafe: <a href="modelica://Buildings.Templates.Plants.Controls.StagingRotation.FailsafeCondition">  
   Buildings.Templates.Plants.Controls.StagingRotation.FailsafeCondition</a>.  
   </li>  
   </ul>  
   ```  
   Keep the matrix explanation in "Details" but reference here.

4. **Improve parameter descriptions for precision**: Rule 1 requires upper-case starting noun-phrases without periods; most comply (e.g., "Staging part load ratio" for plrSta), but some like "True: The logic block is used in a hybrid heat pump plant" for have_HpShc could be shorter: "Flag for hybrid heat pump plant use".  
   **Suggested change**: For dtPri: Update to "Runtime with high primary-setpoint delta-T before staging up". Ensure all internals (e.g., capReq) have descriptions if exposed.

## General Comments and Recommendations

The documentation is clear and comprehensive, effectively explaining staging logic with equations, conditions, and details on averaging/failsafes, making it accessible for HVAC control modelers. It follows most rules well: lower-case tags, <p> wrapping, <h4> for "Details", <code> for parameters (e.g., <code>dtRun</code>), <i> for variables (rule 5), and reverse-chronological revisions. Hyperlinks enhance cross-referencing, and the structure flows logically from concepts to implementation notes. defaultComponentName="chaSta" is correctly lowerCamelCase (rule 10), and no fixme or tables/figures are present (appropriate for this block).

**Strengths**:
- Conciseness: Descriptions are technical yet succinct, e.g., the OPLR equation and condition lists avoid redundancy.
- Clarity: Italics for math (<i>OPLR</i>), bold-like emphasis via structure, and explicit hyperlinks to related blocks aid understanding.
- Compliance: Good use of <ul><li> for lists, no prohibited headings, and spell-checked (minor: "part based" could be "in part based," but no errors).

**Areas for improvement**:
- **Conciseness**: Some <p> repeat ideas (e.g., sensor priority mentioned twice); merge for ~10% reduction. The "Details" on if/when conditions is verbose – shorten to: "Uses 'if' for persistent commands, unlike 'when' for edges, to handle unavailable stages."
- **Clarity**: Expand acronyms on first use (e.g., "operative part load ratio (OPLR)"). Use &gt; and &lt; for inequalities (e.g., <i>OPLR &gt; plrSta</i>) to ensure HTML rendering. The hybrid mode (u1HeaCoo) is implied but not exemplified.
- **Completeness**: Optional sections (rule 4) like "Validation" could reference tests for OPLR accuracy or failsafe triggers, e.g., <h4>Validation</h4><p>Validated against ASHRAE Guideline 36 sequences for chiller staging.</p>. For complex staging, link to Buildings.UsersGuide (rule 10) in intro.
- **Consistency and Polish**: Ensure all <i> use <sub> for subscripts (e.g., Q<sub>required</sub>). Test rendering for long lines and equations in Dymola. Variables like typ (application type) aren't mentioned – integrate into suggested sections.
- **Overall recommendation**: Already high-quality; fixes ensure full compliance, while additions make it more user-friendly (target 15-20% expansion). This aligns with Buildings library standards for reusable, documented controls. Prioritize for integration in hybrid plant examples.