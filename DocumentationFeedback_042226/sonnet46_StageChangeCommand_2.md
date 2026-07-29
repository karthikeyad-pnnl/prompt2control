# Documentation Review: `Buildings.Templates.Plants.Controls.StagingRotation.ChillerStaging` (inferred)

---

## Section 1 — Mandatory Edits (Rules Being Broken)

| Original Text / Issue | Suggested Edit | Rationale |
|---|---|---|
| `<i>OPLR = Qrequired / Qstage</i>` (inline italic used for a display equation) | `<p align="center" style="font-style:italic;">OPLR = Q<sub>required</sub> / Q<sub>stage</sub></p>` | Rule 5: Display equations must be centred italic `<p>` blocks. Subscripts must use `<sub>` tags. |
| `<i>Qrequired</i>`, `<i>Qstage</i>`, `<i>OPLR</i>` used as inline variable references throughout the text | Change each to e.g. `<i>Q<sub>required</sub></i>`, `<i>Q<sub>stage</sub></i>`, `<i>OPLR</i>` | Rule 5: Inline variables must use `<i>` with `<sub>`/`<sup>` for subscripts/superscripts where applicable. `Qrequired` and `Qstage` need subscript markup. |
| `<i>OPLR &gt; plrSta</i>` and `<i>OPLR &lt; plrSta</i>` (parameter name `plrSta` inside italic) | `<i>OPLR</i> &gt; <code>plrSta</code>` and `<i>OPLR</i> &lt; <code>plrSta</code>` | Rule 5: Parameter/code references must use `<code>`, not `<i>`. Variable names (`OPLR`) stay in `<i>`. |
| `<h4>\nDetails\n</h4>` — heading uses newlines inside the tag and the label "Details" is not in the standard section order | Change to `<h4>Implementation</h4>` (no surrounding newlines inside the tag) | Rule 4: Permitted `<h4>` headings are the fixed set listed in the template. "Details" is not a recognised heading; the content is implementation-level explanation and should use `<h4>Implementation</h4>`. Newlines inside tags are non-standard HTML. |
| The `revisions` entry `May 31, 2024` is listed before `March 29, 2024`, which is correct (reverse chronological), but the month format is inconsistent with the rule example (`January 15, 2024` — full month name, day, year). Both entries already use this format, so this is fine — **however** neither entry ends with a period after the description sentence. | Add a period: `…and added failsafe condition.</li>` and `First implementation.</li>` | Rule 9: Revision entries should be complete sentences. The examples in the rules end with a period. |

---

## Section 2 — Suggested Edits (Possibly Missing Information)

| Original Text / Issue | Suggested Edit | Rationale |
|---|---|---|
| No `<h4>Typical use and important parameters</h4>` section present | Add a section describing key parameters `dtRun`, `dtMea`, `plrSta`, and `staEqu`, their roles and how a user should set them | Rule 4: This section is optional but strongly appropriate here given the number of non-trivial parameters. Users need guidance on configuring the staging matrix and timing parameters. |
| No mention of parameters `dT`, `dtPri`, `dtSec` anywhere in the documentation | Add explanation of `dT`, `dtPri`, and `dtSec` — e.g., under `<h4>Typical use and important parameters</h4>` or within the failsafe discussion | These parameters are defined in the model (delta-T thresholds and runtimes used by the failsafe condition) but are completely undocumented in the `info` section, leaving users without guidance. |
| No mention of the `typ` parameter (`Type of application`) or `have_HpShc` / `have_pumSec` / `have_inpPlrSta` Boolean parameters | Add a brief description of these flags under `<h4>Typical use and important parameters</h4>`, explaining how they alter the block behaviour (e.g., primary-secondary vs primary-only, hybrid vs non-hybrid) | These parameters control major behavioural branches of the block but are not referenced anywhere in the `info` section. |
| No `<h4>Assumptions and limitations</h4>` section | Consider adding a section noting, e.g., that the block assumes a single staging matrix applies uniformly, and that unavailable stages are skipped but staging conditionals in the current stage are still evaluated normally | Rule 4: This section is optional but the existing text already contains one assumption ("Any unavailable stage is skipped… but staging conditionals in the current stage are evaluated as per usual") that belongs here. |
| The `<h4>Implementation</h4>` section (currently labelled "Details") does not mention the hybrid-plant path (matrices `staEquSinMod`, `staEquDouMod`, the `swiMod` switch, or the `u1HeaCoo` signal) | Add a brief note that for hybrid plants the staging matrix is switched between single-operation and heating-cooling modes via the `u1HeaCoo` signal | The model contains significant logic for hybrid plant handling that is invisible to users reading the documentation. |
| No `<h4>Validation</h4>` section | If validation tests exist, add a reference. If not, omit — but consider adding when tests are written | Rule 4 lists `<h4>Validation</h4>` as an optional standard section. |

---

## Section 3 — General Comments and Recommendations

| Original Text / Issue | Suggested Edit | Rationale |
|---|---|---|
| The short introductory paragraph opens with "The plant equipment is staged in part based on required capacity" — this is accurate but does not state what the block *is* | Rewrite opening sentence to something like: "This block computes stage up and stage down commands for plant equipment based on the operative part load ratio (<i>OPLR</i>), a failsafe condition, and minimum runtime requirements." | Rule 4 requires a short introduction. The current opening dives into a sub-concept rather than stating the overall purpose of the block. |
| The sentence "If both primary and secondary hot water temperatures and flow rates are available, the sensors in the primary loop are used for calculating <i>Qrequired</i>." is ambiguous — it is unclear what "available" means (hardware present? signals connected?) | Clarify: "If both primary-loop and secondary-loop temperature and flow sensors are present, the primary-loop sensors are used to calculate <i>Q<sub>required</sub></i>." | Improves clarity for users who are not already familiar with the implementation. |
| The phrase "rolling average" is used in the text but the hyperlink to `LoadAverage` is not provided here — only `FailsafeCondition` and `StageIndex` and `EquipmentEnable` are linked | Add a hyperlink: `<a href="modelica://Buildings.Templates.Plants.Controls.StagingRotation.LoadAverage">Buildings.Templates.Plants.Controls.StagingRotation.LoadAverage</a>` near the mention of `dtMea` and the rolling average | Rule 8: Use fully qualified `modelica://` hyperlinks for cross-references. The `LoadAverage` block is a key sub-component and is already referenced in the revisions; it should also be linked in the `info` text. |
| `<i>30</i>&nbsp;s` — the number 30 is wrapped in `<i>` tags, implying it is a variable | Change to plain text or `<code>30</code>&nbsp;s, or simply `30&nbsp;s` | The number 30 is a fixed constant, not a variable or parameter. Using `<i>` is misleading. |
| The use of `"if"` and `"when"` (with quotation marks) in the Implementation section is inconsistent with the `<code>` convention | Change to `<code>if</code>` condition and `<code>when</code>` condition | Rule 5/10: Modelica language keywords referenced in documentation should be wrapped in `<code>` tags, not quotation marks. |
| Long prose paragraphs in the Implementation section exceed ~80 characters per line in the raw HTML source | Reformat the raw HTML to wrap lines at ~80 characters | Rule 3: Lines should be kept to a soft limit of ~80 characters for maintainability of the source annotation. |