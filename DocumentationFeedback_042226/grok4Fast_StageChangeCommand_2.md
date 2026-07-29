# Documentation Feedback for Buildings.Templates.Plants.Controls.StagingRotation

## Mandatory Edit Suggestions
These address direct violations of the rules, such as description strings not being short noun-phrases starting with upper-case and lacking a trailing period (Rule 1), or improper HTML formatting.

| Original Text with Issue | Suggested Edit | Rationale |
|--------------------------|----------------|-----------|
| have_HpShc Boolean "True: The logic block is used in a hybrid heat pump plant" | have_HpShc Boolean "Flag for hybrid heat pump plant" | Violates Rule 1: Description is a full sentence with colon and period-like structure; must be a short noun-phrase starting with upper-case, no trailing period. |
| have_pumSec Boolean "Set to true for primary-secondary distribution, false for primary-only" | have_pumSec Boolean "Flag for primary-secondary distribution" | Violates Rule 1: Instructional sentence; convert to short noun-phrase for conciseness and compliance. |
| have_inpPlrSta Boolean "Set to true to use an input signal for SPLR, false to use a parameter" | have_inpPlrSta Boolean "Flag for input signal of staging part load ratio" | Violates Rule 1: Instructional full sentence; must be noun-phrase without imperative language. |
| `<p>\n<i>OPLR = Qrequired / Qstage</i>\n</p>` (equation in info section) | `<p align=\"center\" style=\"font-style:italic;\">\nOPLR = Q<sub>required</sub> / Q<sub>stage</sub>\n</p>` | Violates Rule 5: Display equations must be centered italic in `<p>` with `align="center"` and `style="font-style:italic;"`; current is plain `<i>` inline without subscripts or centering. Use subscripts for variables. |
| `<h4>\nDetails\n</h4>` (heading in info section) | `<h4>Implementation</h4>` (or align to template like `<h4>Typical use and important parameters</h4>`) | Violates Rule 4: Headings should follow the optional template order (e.g., Implementation, Typical use); "Details" is non-standard and unclear—map to closest template section for structure. |

## Suggested Edits
These address potential missing information, such as incomplete coverage of optional info sections (Rule 4), lack of parameter grouping annotations (Rule 2), or absent references to validation/examples.

| Original Text with Issue | Suggested Edit | Rationale |
|--------------------------|----------------|-----------|
| No `Dialog(group=...)` annotations visible for parameters like `plrSta`, `dtRun`, `dtMea` in variables list | Add: `annotation (Dialog(group="Staging thresholds"));` to parameters like `plrSta`, `dtRun`, `dtMea` | Rule 2 suggests using `Dialog(group=...)` for logical grouping (e.g., nominal conditions, timers); missing grouping reduces usability in the GUI—group related parameters for clarity. |
| Info section lacks optional sections like `<h4>Assumptions and limitations</h4>` or `<h4>Typical use and important parameters</h4>` after intro | Insert after existing `<p>` blocks: `<h4>Assumptions and limitations</h4>\n<p>Assumes steady-state capacity calculations; limited to primary-secondary loops without bypass.</p>\n<h4>Typical use and important parameters</h4>\n<p>Use for heat pump staging. Key: <code>plrSta</code> (threshold), <code>dtRun</code> (minimum runtime).</p>` | Rule 4 requires short intro (present) but optional sections enhance completeness; missing details on assumptions (e.g., sensor availability) and parameters could confuse users—add for better guidance. |
| No `<h4>References</h4>` or external links in info | Add at end of info: `<h4>References</h4>\n<p>See Buildings Users Guide for staging examples.</p>` | Rule 4 lists References as optional but recommended for complex controls; missing ties to broader library (e.g., UsersGuide) reduces context—suggest for completeness. |
| Revisions lack entry for initial model creation if March 2024 is not first | No change needed, but add if applicable: `<li>January 2024, by Initial Author:<br/>Initial concept.</li>` before existing entries | Rule 9 requires reverse chronological; current is fine, but if model predates March 2024, missing early revision—suggest for full history if known. |

## General Comments and Recommendations
- **Clarity**: The info section is mostly clear with good use of `<i>` for variables and `<code>` for parameters, but long paragraphs (e.g., staging conditions) could be split into more `<p>` blocks for readability. Hyperlinks are correctly formatted with `modelica://` (Rule 8), aiding navigation.
- **Conciseness**: Some `<p>` blocks exceed ~80 characters (e.g., the availability condition paragraph); break into shorter lines or bullet points. Avoid repetition, like multiple mentions of `dtRun`—cross-reference once.
- **Compliance**: Overall strong adherence to HTML rules (lower-case tags, `<p>` wrapping, no `<h1>`-`<h3>`). Revisions follow Rule 9 perfectly. Ensure spell-check (e.g., "tranverse" in connections should be "transpose" if in docs). No figures/tables, which is fine if not needed (Rules 6-7).
- **Improvements**: Add `defaultComponentName` usage example in info if drag-and-drop is key (Rule 10). For internals like `faiSaf`, briefly mention in "Implementation" if expanding section. Test HTML rendering in Modelica tools for line wraps. Consider adding a simple table for staging matrix `staEqu` example (Rule 6) to visualize equipment enablement.