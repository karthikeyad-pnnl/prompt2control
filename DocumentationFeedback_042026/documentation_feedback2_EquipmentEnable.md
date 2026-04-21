# Documentation Review Feedback

## Mandatory Edit Suggestions

These suggestions address direct violations of the Buildings Library documentation rules. The primary issues are in the revisions formatting (missing italics) and potential line length exceedances in the <ul> list items, which affect source code readability.

1. **Revisions missing italics for date and author**: Rule 9 requires reverse chronological `<ul><li>` entries with `<i>` tags around the date and author (e.g., `<i>January 15, 2024</i> by Jane Doe`). The current single entry lacks `<i>` tags, violating this.  
   **Suggested change**: Update the revisions section to:  
   ```  
   <ul>  
   <li><i>March 29, 2024</i> by Antoine Gautier:<br/>  
   First implementation.  
   </li>  
   </ul>  
   ```  
   This matches the exact format in rule 9.

2. **Line lengths exceeding ~80 characters in <ul> items**: Rule 3 specifies a soft limit of ~80 characters per line for HTML source readability. Several <li> items in the staging matrix explanation are long, e.g., the item describing coefficients strictly lower than 1 and greater than 0 (exceeds ~100 characters including spaces).  
   **Suggested change**: Break long <li> content across lines and use <br/> for readability. For the affected item:  
   ```  
   <li>  
   A coefficient <code>staEqu[i, j]</code> strictly lower than <i>1</i><br/>  
   and strictly greater than <i>0</i> means that equipment <code>j</code><br/>  
   may be enabled at stage <code>i</code> as a lead/lag alternate equipment.<br/>  
   If equipment <code>j</code> is unavailable but another lead/lag alternate<br/>  
   equipment is available, then the latter equipment is enabled.<br/>  
   Stage <code>i</code> is only deemed unavailable if all<br/>  
   lead/lag alternate equipment specified for stage <code>i</code><br/>  
   are unavailable.  
   </li>  
   ```  
   Apply similarly to the penultimate <li> on the sum of coefficients and the condition <code>∑_j staEqu[i+1, j] &ge; ∑_j staEqu[i, j]</code> – split after "gives the number of" and before the inequality, ensuring each line ≤80 chars.

3. **Inconsistent inline math/symbol formatting**: Rule 5 requires <i> for inline variables (e.g., <i>a<sub>1</sub></i>) and proper escaping for symbols like ∑ (using &sum; or Unicode). The current uses raw ∑_j, which may not render consistently in all viewers, and lacks <sub> for indices in some places.  
   **Suggested change**: Update math expressions for consistency. For the sum in the <li>:  
   ```  
   The sum of the coefficients in a given row <i>&sum;<sub>j</sub> staEqu[i, j]</sub><br/>  
   gives the number of equipment required at stage <code>i</code>.  
   ```  
   Similarly for the inequality:  
   ```  
   The condition <code>&sum;<sub>j</sub> staEqu[i+1, j] &ge; &sum;<sub>j</sub> staEqu[i, j]</code><br/>  
   is required for all <code>i &lt; size(staEqu, 1)</code>.  
   ```  
   Use &ge; and &lt; for inequalities to comply with HTML standards.

4. **Missing <p> closure before final paragraph**: Rule 3 requires wrapping text in <p>...</p>. The structure has two opening <p> but the final descriptive paragraph (about updating enable signals) lacks explicit closure, potentially causing rendering issues in some tools.  
   **Suggested change**: Ensure the last paragraph is wrapped:  
   ```  
   </p>  
   <p>  
   The state of the enable signals is only updated at stage change, or<br/>  
   if the number of previously enabled equipment that is available is<br/>  
   strictly less than the number of equipment required to run.<br/>  
   This avoids hot swapping equipment, e.g., an equipment would not be started<br/>  
   and another stopped during operation just to fulfill the priority order.<br/>  
   However, when a lead/lag alternate equipment becomes unavailable and another<br/>  
   lead/lag alternate equipment can be enabled to meet the number of required<br/>  
   equipment, then the state of the enable signals is updated.  
   </p>  
   ```  
   Also break the long sentence on "hot swapping" to ≤80 chars.

## Suggested Edits

These address gaps where information is missing or could be enhanced for completeness, per the optional sections in rule 4 (Info Section Template). The documentation explains matrices well but omits assumptions about hybrid plants, typical parameters, and validation, which are relevant given variables like `have_HpShc` and connections involving mode switching.

1. **Add "Assumptions and limitations" section**: Rule 4 lists this as optional; it's missing but needed to clarify constraints like matrix requirements (e.g., non-decreasing sums) and hybrid mode handling. The final paragraph hints at logic but doesn't formalize limitations.  
   **Suggested addition**: Insert after the <ul> and before the final <p>:  
   ```  
   <h4>Assumptions and limitations</h4>  
   <p>  
   Staging matrices must satisfy non-decreasing equipment requirements per stage<br/>  
   (i.e., <code>&sum;<sub>j</sub> staEqu[i+1, j] &ge; &sum;<sub>j</sub> staEqu[i, j]</code>).<br/>  
   For hybrid plants (<code>have_HpShc=true</code>), use <code>staEquDouMod</code> for<br/>  
   heating-cooling modes and <code>staEquSinMod</code> otherwise.<br/>  
   Equipment availability (<code>u1Ava</code>) is assumed constant between stage changes.<br/>  
   No support for dynamic runtime sorting beyond input <code>uIdxAltSor</code>.  
   </p>  
   ```  
   This draws from variables (e.g., transposed matrices) and connections (e.g., swiMod for mode switching).

2. **Add "Typical use and important parameters" section**: Missing per rule 4; the intro mentions parameters but doesn't guide usage. Highlight key ones like `nEquAlt`, `staEqu`, and inputs like `uSta` based on variables.  
   **Suggested addition**: Insert after "Assumptions and limitations":  
   ```  
   <h4>Typical use and important parameters</h4>  
   <p>  
   Use this block in plant staging to enable equipment (e.g., heat pumps, chillers)<br/>  
   based on load stages. Connect <code>uSta</code> from upstream stage index logic,<br/>  
   <code>u1Ava</code> from equipment status, and <code>uIdxAltSor</code> from runtime sorter.<br/>  
   Key parameters: <code>staEqu</code> (matrix for non-hybrid plants, size nSta x nEqu),<br/>  
   <code>nEquAlt</code> (number of alternates for rotation), <code>have_HpShc</code><br/>  
   (enable hybrid mode matrices). Set <code>is_pumApp</code> for pump-specific logic if needed.  
   </p>  
   ```  
   This aids integration, referencing defaultComponentName "enaEqu" for drag-and-drop (rule 10).

3. **Add "Implementation" or "References" section**: Rule 4 includes these as optional; the doc lacks details on how matrices are processed (e.g., via reqEquSta extractor in connections). A brief implementation note or self-reference would help.  
   **Suggested addition**: At the end of info:  
   ```  
   <h4>Implementation</h4>  
   <p>  
   Equipment enable is computed by extracting stage row from transposed matrix,<br/>  
   counting required/available units, and using lead/lag alternates via<br/>  
   <code>uIdxAltSor</code>. Updates occur on stage change (<code>cha</code>) or availability loss.  
   For hybrid modes, <code>swiMod</code> selects appropriate matrix.  
   </p>  
   ```  
   Alternatively, if external refs exist, add a "References" <ul> linking to related blocks like runtime sorters.

4. **Enhance parameter descriptions for clarity**: Rule 1 requires short noun-phrases; most are good (e.g., "Staging matrix for non-hybrid plant – Equipment required for each stage"), but transposed matrices (e.g., `traStaEqu`) could specify "Transpose of staEqu for row extraction".  
   **Suggested change**: For `traStaEqu`: Update to "Transpose of staging matrix for non-hybrid plant – Enables row extraction by stage".

## General Comments and Recommendations

The documentation is clear, technical, and well-focused on the core functionality of generating enable commands from staging matrices, making it suitable for advanced users in plant control modeling. It adheres to most rules: lower-case HTML, <p> wrapping for paragraphs, <code> for parameters/references (e.g., <code>uSta</code>), and <i> for inline values like <i>0</i> and <i>1</i> (rule 5). The <ul> structure effectively breaks down matrix semantics, and the single revision is concise. defaultComponentName="enaEqu" is appropriately set in lowerCamelCase (rule 10), and no figures/tables are needed for this algorithmic block.

**Strengths**:
- Conciseness: The explanation of matrix coefficients is precise and avoids fluff, with good use of <code> for code-like elements.
- Clarity: Terms like "lead/lag alternate equipment" are explained in context, and the final paragraph on update logic ties into practical concerns like avoiding "hot swapping."
- Compliance: No upper-case headings beyond <h4> (none used), spell-checked (no errors), and logical flow from intro to details.

**Areas for improvement**:
- **Conciseness**: Some sentences in the final <p> are wordy (e.g., "the number of previously enabled equipment that is available is strictly less than the number of equipment required to run" could be "available previously enabled equipment < required"). Trim by 10-15% for tighter prose without losing detail.
- **Clarity**: Math symbols (∑, ≥) should use HTML entities (&sum;, &ge;) for universal rendering. Define acronyms on first use if not in parent docs (e.g., none here, but "lead/lag" assumes familiarity). The hybrid plant mention in variables isn't expanded – the suggested section would help.
- **Completeness**: Optional sections (rule 4) would elevate the doc; currently, it's intro-heavy but lacks guidance on setup/validation. No "Validation" section, but if tests exist (e.g., for matrix edge cases like unavailable alternates), add a brief <h4>Validation</h4> with references. For complex packages like staging, link to a User's Guide (rule 10) in the intro.
- **Consistency and Polish**: Ensure all <i> tags are closed (they are). Test line breaks in a Modelica IDE to confirm ~80-char limit. The block handles hybrid modes via connections (e.g., u1HeaCoo), so emphasizing this in edits would align doc with implementation.
- **Overall recommendation**: Solid foundation; mandatory fixes ensure compliance, while suggested sections add value for usability. Post-edits, the doc would be more comprehensive (aim for 20% length increase) and self-explanatory, ideal for the Buildings library's emphasis on reusable controls. Validate in Dymola for rendering, especially math and lists.