# Buildings Library — Modelica Documentation Rules

> **Audience:** Human contributors and LLM-based code generators.
> These rules govern the `documentation` annotation (the `info` and `revisions`
> sections) as well as description strings and related annotations in every
> Modelica class within the **Buildings** library.

---

## Table of Contents

1. [Description Strings](#1-description-strings)
2. [Parameter and Variable Grouping](#2-parameter-and-variable-grouping)
3. [HTML Documentation — General](#3-html-documentation--general)
4. [HTML Documentation — Structure and Template](#4-html-documentation--structure-and-template)
5. [HTML Documentation — Equations](#5-html-documentation--equations)
6. [HTML Documentation — Parameter References and Code](#6-html-documentation--parameter-references-and-code)
7. [HTML Documentation — Tables](#7-html-documentation--tables)
8. [HTML Documentation — Figures](#8-html-documentation--figures)
9. [HTML Documentation — Hyperlinks to Other Models](#9-html-documentation--hyperlinks-to-other-models)
10. [Headings](#10-headings)
11. [Revisions Section](#11-revisions-section)
12. [Default Component Names](#12-default-component-names)
13. [Line Length](#13-line-length)
14. [HTML Tag Casing](#14-html-tag-casing)
15. [Spell Check](#15-spell-check)
16. [User's Guide for Packages](#16-users-guide-for-packages)
17. [Use of fixme](#17-use-of-fixme)

---

## 1. Description Strings

**Every** parameter, variable, and connector — including `protected`
members — **must** have a description string.

### Style

| Aspect | Convention |
|--------|-----------|
| Capitalisation | Start with an upper-case letter |
| Punctuation | No trailing period |
| Form | Short noun-phrase or sentence fragment that fits on one line |

### Example

```modelica
parameter Modelica.Units.SI.MassFlowRate m_flow_nominal
  \"Nominal mass flow rate\";

protected
  Real k \"Gain coefficient\";
```

---

## 2. Parameter and Variable Grouping

Group related parameters using the `group` and/or `tab` keys in the
`Dialog` annotation.

### Example — Group Only

```modelica
parameter Modelica.Units.SI.Time tau = 60
  \"Time constant at nominal flow\"
  annotation (Dialog(group=\"Nominal condition\"));
```

### Example — Tab and Group

```modelica
parameter Types.Dynamics substanceDynamics = energyDynamics
  \"Formulation of substance balance\"
  annotation (
    Evaluate=true,
    Dialog(tab=\"Assumptions\", group=\"Dynamics\"));
```

---

## 3. HTML Documentation — General

All class documentation is placed inside the `info` section of the
`Documentation` annotation and is written in **HTML**.

### Mandatory Rules

| ID | Rule |
|----|------|
| H-1 | Use **lower-case** HTML tags everywhere (`<p>`, not `<P>`). |
| H-2 | Keep source lines to roughly **80 characters** (soft limit). Break long HTML across lines for readability. |
| H-3 | Wrap running text in `<p>…</p>` tags. |
| H-4 | Do **not** use `<h1>`, `<h2>`, or `<h3>`. Start at **`<h4>`**. Use `<h5>` sparingly for sub-sections. |

---

## 4. HTML Documentation — Structure and Template

Every class — including validation and example models — **must** contain
an `info` section with at least a short introductory paragraph.

The following template lists the **recommended** sections. Only the short
introduction is **required**; the remaining sections are **optional** and
should be included when relevant.

```html
<html>
<body>
<p>
A short introduction describing the purpose of the model.
</p>

<h4>Main equations</h4>
<p>
Describe the governing equations (see Section 5 for formatting).
</p>

<h4>Assumptions and limitations</h4>
<p>
State key simplifications, validity ranges, or known limitations.
</p>

<h4>Typical use and important parameters</h4>
<p>
Explain how the model is meant to be used and which parameters
the user should set first.
</p>

<h4>Options</h4>
<p>
Document optional features and their controlling parameters.
</p>

<h4>Dynamics</h4>
<p>
Describe which states and dynamics are present and which parameters
influence them. This section need not appear in partial classes.
</p>

<h4>Validation</h4>
<p>
State whether validation was analytical, comparative, or empirical,
and reference the validation model.
</p>

<h4>Implementation</h4>
<p>
Note any non-obvious implementation details.
</p>

<h4>References</h4>
<p>
List references, if applicable.
</p>
</body>
</html>
```

### Ordering

If present, sections **should** appear in the order shown above.

---

## 5. HTML Documentation — Equations

### Inline Mathematics

Use `<i>…</i>` for variable names in running text:

```html
<p>
where <i>a<sub>1</sub></i> is the first coefficient.
</p>
```

### Display (Centred) Equations

Use a dedicated `<p>` block with centre alignment and italic style:

```html
<p>
The polynomial has the form
</p>
<p align=\"center\" style=\"font-style:italic;\">
y = a<sub>1</sub> + a<sub>2</sub> x
    + a<sub>3</sub> x<sup>2</sup> + &hellip;,
</p>
<p>
where <i>a<sub>1</sub></i> is &hellip;
</p>
```

### Subscripts and Superscripts

| Construct | HTML |
|-----------|------|
| Subscript | `x<sub>i</sub>` |
| Superscript / exponent | `x<sup>2</sup>` |

### Time Derivatives (Dot Notation)

Use the Unicode combining dot above character (`&#775;`) inside a
`<code>` tag:

```html
<code>m&#775;</code>   <!-- renders as ṁ  (mass flow rate) -->
```

---

## 6. HTML Documentation — Parameter References and Code

When referring to parameter names, variable names, enumeration values, or
short code fragments, wrap them in `<code>…</code>`:

```html
<p>
To linearize the equation, set <code>linearize=true</code>.
</p>
```

**Do not** use `<code>` for mathematical variable names that appear in
equations; use `<i>` there instead (see Section 5).

---

## 7. HTML Documentation — Tables

Use the following template for HTML tables:

```html
<p>
<table summary=\"Brief summary of the table content\"
       border=\"1\" cellspacing=\"0\" cellpadding=\"2\"
       style=\"border-collapse:collapse;\">
  <tr>
    <th>Header 1</th>
    <th>Header 2</th>
  </tr>
  <tr>
    <td>Data 1</td>
    <td>Data 2</td>
  </tr>
</table>
</p>
```

### Rules

| ID | Rule |
|----|------|
| T-1 | Always include a `summary` attribute (accessibility). |
| T-2 | Use `<th>` for header cells, `<td>` for data cells. |
| T-3 | Apply `border=\"1\"`, `cellspacing=\"0\"`, `cellpadding=\"2\"`, and `style=\"border-collapse:collapse;\"`. |

---

## 8. HTML Documentation — Figures

### File Locations

| Item | Path convention |
|------|----------------|
| Rendered image (PNG) | `Buildings/Resources/Images/<package-path>/<FileName>.png` |
| Source file (SVG preferred) | Same directory as the PNG |

The directory under `Resources/Images/` **must** mirror the full Modelica
package path. For example, a figure for
`Buildings.Fluid.FixedResistances.PressureDrop` is stored at:

```
Buildings/Resources/Images/Fluid/FixedResistances/PressureDrop.png
```

### Embedding

Close the preceding paragraph, centre the image in its own `<p>` block,
then open a new paragraph:

```html
</p>
<p align=\"center\">
<img alt=\"Descriptive alt text\"
     src=\"modelica://Buildings/Resources/Images/Fluid/FixedResistances/PressureDrop.png\"/>
</p>
<p>
```

### Rules

| ID | Rule |
|----|------|
| F-1 | Always include a meaningful `alt` attribute. |
| F-2 | Use the `modelica://` URI scheme for the `src` attribute. |
| F-3 | Prefer SVG as the **source** format. Use [Inkscape](https://inkscape.org/) or similar to create and export to PNG. |
| F-4 | Store both the SVG source and the PNG rendering in the same directory. |

---

## 9. HTML Documentation — Hyperlinks to Other Models

Reference other Modelica classes by their **fully qualified name** using
the `modelica://` URI:

```html
<p>
See
<a href=\"modelica://Buildings.Fluid.Sensors.Density\">
Buildings.Fluid.Sensors.Density</a>.
</p>
```

### Rules

| ID | Rule |
|----|------|
| L-1 | The `href` uses the `modelica://` protocol followed by the full class path. |
| L-2 | The visible link text **must** also be the full class path (e.g., `Buildings.Fluid.Sensors.Density`). |

---

## 10. Headings

| ID | Rule |
|----|------|
| HD-1 | The **minimum** heading level inside `info` is `<h4>`. Never use `<h1>`, `<h2>`, or `<h3>`. |
| HD-2 | Use `<h5>` only when a sub-section within an `<h4>` section is needed. |
| HD-3 | Follow the standard section order from Section 4 when applicable. |

---

## 11. Revisions Section

Add authorship and change information to the `revisions` section of the
`Documentation` annotation.

### Recommended Format

```html
<html>
<body>
<ul>
<li>
<i>Month Day, Year</i> by Author Name:<br/>
Description of the change.
</li>
</ul>
</body>
</html>
```

### Example

```html
<html>
<body>
<ul>
<li>
<i>January 15, 2024</i> by Jane Doe:<br/>
First implementation.
</li>
</ul>
</body>
</html>
```

### Rules

| ID | Rule |
|----|------|
| R-1 | List entries in **reverse chronological** order (newest first). |
| R-2 | Each entry must include a date and the author's name. |
| R-3 | Briefly describe what was changed. |

---

## 12. Default Component Names

Classes intended for **drag-and-drop** use (models, blocks, etc.) **must**
declare a `defaultComponentName` annotation:

```modelica
annotation (defaultComponentName=\"senDen\", ...);
```

### Naming Convention

| Aspect | Convention |
|--------|-----------|
| Casing | lowerCamelCase |
| Style | Short, readable abbreviation of the class purpose |

---

## 13. Line Length

Keep lines to approximately **80 characters**. This is a **soft** guideline:
occasional overruns (e.g., a long URI in an `href`) are acceptable, but
running text and code should be wrapped to stay near 80 characters for
readability and diff-friendliness.

---

## 14. HTML Tag Casing

All HTML tags and attribute names **must** be lower case.

```html
<!-- Correct -->
<p align=\"center\">

<!-- Wrong -->
<P ALIGN=\"center\">
```

---

## 15. Spell Check

Run a spell check on all documentation text before committing. Pay
particular attention to:

- The `info` section (description and technical prose).
- Description strings on parameters and variables.

---

## 16. User's Guide for Packages

Packages that are large or contain many interrelated classes **should**
provide a dedicated `UsersGuide` package. When such a guide exists, it
**must** be referenced from `Buildings.UsersGuide`.

---

## 17. Use of `fixme`

| Context | Rule |
|---------|------|
| Development / feature branches | Use the marker `fixme` (case-insensitive in intent, but write it lower-case) to flag passages that need revision. |
| Before merging to `master` | **All** `fixme` markers must be resolved and removed. |
| `master` branch | No `fixme` markers are permitted at any time. |

---

## Quick-Reference Checklist

Use this checklist before submitting a model:

- [ ] Every parameter and variable (including `protected`) has a description string.
- [ ] Parameters are grouped with `Dialog(group=…)` / `Dialog(tab=…, group=…)` where appropriate.
- [ ] The `info` section exists and begins with a short introductory paragraph.
- [ ] Applicable template sections (Main equations, Assumptions, Validation, etc.) are present.
- [ ] Equations use centred `<p>` blocks with italic styling; variables use `<i>`.
- [ ] Parameter/code references use `<code>`.
- [ ] Time derivatives use `&#775;` inside `<code>`.
- [ ] Tables follow the prescribed format with `summary`, borders, and `<th>` headers.
- [ ] Figures are in `Resources/Images/<package-path>/`, with SVG sources alongside PNGs.
- [ ] Images use `modelica://` URIs and have `alt` text.
- [ ] Cross-references use fully qualified names with `modelica://` links.
- [ ] Headings start at `<h4>` (no `<h1>`–`<h3>`).
- [ ] All HTML tags are lower case.
- [ ] Lines are ≤ ~80 characters.
- [ ] A `defaultComponentName` annotation is present for drag-and-drop classes.
- [ ] The `revisions` section records author and date.
- [ ] Spell check has been run.
- [ ] No `fixme` markers remain (if targeting `master`).
