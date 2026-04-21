# Buildings Library — Modelica Documentation Rules (Compact)

> For LLM use. Governs `Documentation` annotation (`info`, `revisions`),
> description strings, and related annotations in the Buildings library.

---

## 1. Description Strings

- **Every** parameter, variable, connector — including `protected` — must have a description string.
- Start with upper-case, no trailing period, short noun-phrase.

```modelica
parameter Modelica.Units.SI.MassFlowRate m_flow_nominal
  \"Nominal mass flow rate\";
```

---

## 2. Parameter Grouping

Use `Dialog(group=…)` and optionally `Dialog(tab=…, group=…)`:

```modelica
parameter Modelica.Units.SI.Time tau = 60
  \"Time constant at nominal flow\"
  annotation (Dialog(group=\"Nominal condition\"));
```

---

## 3. HTML General Rules

- All HTML tags **lower-case**.
- Lines ≤ ~80 characters (soft limit).
- Wrap text in `<p>…</p>`.
- Headings start at `<h4>`. Never use `<h1>`–`<h3>`. Use `<h5>` sparingly.

---

## 4. Info Section Template

Every class must have an `info` section. Short intro is **required**; other sections **optional**, in this order:

```
<p>Short introduction.</p>
<h4>Main equations</h4>
<h4>Assumptions and limitations</h4>
<h4>Typical use and important parameters</h4>
<h4>Options</h4>
<h4>Dynamics</h4>           (not needed in partial classes)
<h4>Validation</h4>
<h4>Implementation</h4>
<h4>References</h4>
```

---

## 5. Equations

**Display equation** — centred italic `<p>`:

```html
<p align=\"center\" style=\"font-style:italic;\">
y = a<sub>1</sub> + a<sub>2</sub> x + a<sub>3</sub> x<sup>2</sup>
</p>
```

**Inline variables** — use `<i>`: `<i>a<sub>1</sub></i>`

**Time derivatives** — use `<code>m&#775;</code>` for m_dot.

**Parameter/code references** — use `<code>`: `<code>linearize=true</code>`

---

## 6. Tables

```html
<table summary=\"…\" border=\"1\" cellspacing=\"0\" cellpadding=\"2\"
       style=\"border-collapse:collapse;\">
  <tr><th>Header</th></tr>
  <tr><td>Data</td></tr>
</table>
```

Always include `summary`, use `<th>` for headers.

---

## 7. Figures

- Store PNGs at `Buildings/Resources/Images/<package-path>/`, SVG sources alongside.
- Use `modelica://` URI. Always include `alt` text.

```html
<p align=\"center\">
<img alt=\"Description\"
     src=\"modelica://Buildings/Resources/Images/Fluid/Example/Fig.png\"/>
</p>
```

---

## 8. Hyperlinks

Use fully qualified names with `modelica://`:

```html
<a href=\"modelica://Buildings.Fluid.Sensors.Density\">
Buildings.Fluid.Sensors.Density</a>
```

---

## 9. Revisions

Reverse chronological `<ul><li>` entries with date and author:

```html
<ul>
<li><i>January 15, 2024</i> by Jane Doe:<br/>
First implementation.</li>
</ul>
```

---

## 10. Other Rules

- **defaultComponentName**: Required for drag-and-drop classes. Use lowerCamelCase: `annotation(defaultComponentName=\"senDen\")`.
- **Spell check**: Run before committing.
- **fixme**: Allowed in dev branches only. Must be removed before merging to `master`.
- **User's Guide**: Provide for complex packages; reference from `Buildings.UsersGuide`.
```

---

### Token comparison

| Version | Est. tokens | Reduction |
|---------|-------------|-----------|
| Full `rules.md` | ~4,000 | — |
| **Compact `rules.md`** | **~1,800** | **~55%** |

The compact version preserves every rule and at least one example per topic, but strips redundant prose, the table of contents, the checklist, and multi-example sections. It should be sufficient as a system prompt while leaving maximum context for the actual generation task.