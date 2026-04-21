# Consolidated Naming Convention Rules

Below is the unified rule set, followed by a dedicated section on contradictions and ambiguities.

---

## 1. Class Names (Models, Blocks, Packages)

**1.1** Class names shall start with an **uppercase letter** and be a noun, or a combination of adjectives and nouns.

**1.2** Use **camelCase** to combine multiple words (e.g., `HeatTransfer`).

**1.3** Do not repeat higher-level package names. Use `Chillers.Carnot`, not `Chillers.CarnotChiller`. Similarly, avoid descriptors in names that are already obvious from the enclosing package (e.g., avoid `boi` for boiler if the block is already in a `BoilerPlant` package).

> *Sources: Set 1 Rule 1, Set 3 Rule 24*

---

## 2. Instance and Variable Names

### 2.1 General Structure

**2.1.1** Instance names (variables, block instances, parameters) shall generally start with a **lowercase letter**, unless they represent a physical quantity conventionally capitalized (e.g., `T` for temperature, `P` for power, `X` for mass fraction).

**2.1.2** Names are composed following this pattern:

| Position | Element | Examples |
|---|---|---|
| 1. Prefix *(optional)* | `u` for input, `y` for output — include only if needed for context | `uOpeMod`, `yHeaCoi` |
| 2. Quantity *(required)* | The physical quantity or descriptor | `TOut`, `TZonHea`, `dpBui` |
| 3. Postfix/Qualifier *(optional)* | Modifiers such as setpoint, min, max, cooling, heating, etc., appended **after** the quantity | `TZonHeaSet`, `TSupSetMin` |

**2.1.3** Strive for **short names**. Omit prefix or postfix when the meaning is clear from context. For example, a room thermostat may simply use `T` as its input.

> *Sources: Set 1 Rules 2 & 5, Set 2 general conventions, Set 3 Rule 6*

### 2.2 Abbreviation Conventions

**2.2.1** Use abbreviations composed of approximately the **first three characters** of each word, combined in camelCase (e.g., `preDro` for pressure drop, `worTim` for working timer, `zonDisEffHea` for zone distribution effectiveness heating).

**2.2.2** Single characters may be used where generally understood (e.g., `T`, `p`, `k`, `n`, `u`, `y`). These may be augmented with descriptors as needed (e.g., `yVal` for valve signal, `yDam` for damper signal, `kCoo` for cooling gain).

> *Sources: Set 1 Rule 2, Set 2 examples*

### 2.3 Cross-Package Consistency

**2.3.1** If an analogous sequence exists for another system (e.g., heating vs. cooling, chiller plant vs. boiler plant), use **consistent, parallel names** across both to facilitate commonization.

**2.3.2** For feedback delay `pre` block instances, use **numbered names** (`pre1`, `pre2`, etc.) rather than bare `pre`.

> *Sources: Set 3 Rules 25 & 26*

---

## 3. Standard Physical Quantity Variables

**3.1** The following single-character or short variables are standard:

| Variable | Meaning |
|---|---|
| `T` | Temperature |
| `p` | Pressure |
| `dp` | Pressure difference |
| `P` | Power |
| `E` (or `Q`) | Energy (or thermal energy) |
| `X` | Mass fraction per total mass |
| `x` | Mass fraction per mass of dry air |
| `Q_flow` | Heat flow rate |
| `m_flow` | Mass flow rate |
| `H_flow` | Enthalpy flow rate |
| `V_flow` | Volume flow rate |
| `k` | Gain (e.g., `kCoo`) |
| `Ti` | Integrator time constant (e.g., `TiCoo`) |
| `Td` | Derivative time constant (e.g., `TdCoo`) |
| `n` | Count / number (e.g., `nChi` for number of chillers) |
| `A` | Area (e.g., `AFlo` for floor area) |
| `h` | Specific enthalpy (e.g., `hOut` for outdoor air enthalpy) |

> *Sources: Set 1 Rules 3–4, Set 2 tables*

---

## 4. Control Signal Naming

**4.1** Control **input** signals start with `u`; control **output** signals start with `y`.

**4.2** The `u`/`y` prefix may be **omitted** when the physical quantity already makes the direction clear.

**4.3** When a controller has multiple outputs or inputs, augment with a descriptor (e.g., `yVal` and `yDam` for valve and damper output signals; `uHea` and `uCoo` for heating and cooling input signals).

> *Sources: Set 1 Rules 2 & 5, Set 2 conventions*

---

## 5. Prefix Conventions

**5.1** The following prefixes are standard:

| Prefix | Meaning | Examples |
|---|---|---|
| `u` | Control input signal | `uOpeMod`, `uDam`, `uHea`, `uCoo` |
| `y` | Control output signal | `yHeaCoi`, `yCooCoi`, `yPosMin`, `yChiPumSpe` |
| `use_` | Conditionally enabled input or feature (boolean parameter) | `use_T_in`, `use_TMix`, `use_enthalpy` |
| `have_` | Indicates the system/zone has a particular component, sensor, or configuration (boolean parameter) | `have_CO2Sen`, `have_occSen`, `have_winSen`, `have_parChi` |
| `need_` | Indicates a required capability or constraint (boolean parameter) | `need_reduceChillerDemand` |

> *Sources: Set 1 Rule 6, Set 2 tables*

---

## 6. Suffix / Postfix Conventions

**6.1** The following suffixes are standard:

| Suffix | Meaning | Examples |
|---|---|---|
| `_flow` | Flow variable | `Q_flow`, `m_flow`, `V_flow`, `VDis_flow` |
| `_nominal` | Design / nominal capacity | `Q_flow_nominal`, `m_flow_nominal`, `V_flow_nominal` |
| `_small` | Small value used for regularization | — |
| `Set` | Setpoint | `TZonHeaSet`, `TZonCooSet` |
| `Min` / `Max` | Minimum / Maximum | `TSupSetMin`, `TZonCooMax`, `VDisHeaSetMax_flow` |
| `_remote` | From a remote sensor | `dpChiWat_remote` |
| `Hea` / `Coo` | Heating / Cooling qualifier | `TZonHeaSet`, `yCooCoi`, `zonDisEffCoo` |

**6.2** When multiple suffixes are needed, follow this general order: *Quantity → Context/Qualifier → Setpoint → Min/Max → `_flow`/`_nominal`*. For example: `VDisHeaSetMax_flow`.

> *Sources: Set 1 Rule 6, Set 2 tables and examples*

---

## 7. Connector Naming

**7.1** Paired connectors of the same domain (identical declarations, different icons) are distinguished by:

| Convention | Usage | Example |
|---|---|---|
| `_a` / `_b` | Fluid ports | `port_a`, `port_b` |
| `_p` / `_n` | Electrical terminals | `terminal_p`, `terminal_n` |

> *Source: Set 1 Rule 7*

---

## 8. Psychrometrics Package Naming (`Buildings.Utilities.Psychrometrics`)

**8.1** Uppercase `X` = mass fraction per total mass; lowercase `x` = mass fraction per mass of dry air.

**8.2** The notation `z_xy` denotes a function or block with output `z` and inputs `x` and `y`.

**8.3** Standard symbols:

| Symbol | Meaning |
|---|---|
| `pW` | Water vapor pressure |
| `TDewPoi` | Dew point temperature |
| `TWetBul` | Wet bulb temperature |
| `TDryBul` (or `T`) | Dry bulb temperature |

> *Source: Set 1 Rule 4*

---

---

# Contradictions and Ambiguities

### Contradiction 1: `_min`/`_max` vs. `Min`/`Max`

| Set 1 (explicit rule) | Set 2 (examples) |
|---|---|
| Suffix `_min` / `_max` (underscore + lowercase), e.g., `TSupCoo_min` | Suffix `Min` / `Max` (camelCase, no underscore), e.g., `TSupSetMin`, `TZonCooMax`, `dpChiWatPumMin` |

Set 2 states that it follows the conventions of Set 1, yet its examples overwhelmingly use `Min`/`Max` in camelCase without an underscore. Confusingly, Set 2 also contains `lift_min`, which follows the Set 1 convention.

**Recommendation:** Adopt **one** format and apply it consistently. The `Min`/`Max` camelCase style is more consistent with other postfix qualifiers (`Set`, `Hea`, `Coo`) that also have no underscore. If that is chosen, the Set 1 rule and the `lift_min` example in Set 2 should be updated.

---

### Contradiction 2: `min` used as a prefix vs. postfix

Set 2 contains the parameter `minChiLif` (minimum chiller lift), where `min` appears as a **prefix**. This directly contradicts:

- Set 1 Rule 6 (suffixes `_min`/`_max`)
- Set 2's own stated convention ("as a postfix a qualifier may be added, such as… `Min` for minimum")
- Set 3 Rule 6 ("modifiers like… minimum, maximum… should be appended **after** the variable name")

**Recommendation:** Rename `minChiLif` to something like `chiLifMin` or `lift_min` to follow the postfix convention.

---

### Ambiguity 1: `need_` prefix not formally defined

The prefix `need_` appears in Set 2's examples (`need_reduceChillerDemand`) but is never explicitly defined as a convention in either Set 1 or Set 2's descriptive text (unlike `use_` and `have_`, which are). Its intended semantic distinction from `have_` is unclear.

**Recommendation:** Formally define `need_` and clarify how it differs from `have_`. A possible distinction: `have_` = "the physical system includes this" vs. `need_` = "the control logic requires this behavior."

---

### Ambiguity 2: When to use underscores vs. camelCase in suffixes

Some suffixes use an underscore (`_flow`, `_nominal`, `_small`, `_remote`) while others use camelCase with no underscore (`Set`, `Min`, `Max`, `Hea`, `Coo`). No explicit rule governs which style to use.

**Possible implicit pattern:** Underscored suffixes (`_flow`, `_nominal`, `_small`) tend to be **category markers** that describe the *type* of quantity, while camelCase suffixes (`Set`, `Min`, `Hea`) tend to be **qualifiers** of the specific value. However, `_remote` doesn't fit this pattern neatly.

**Recommendation:** Explicitly state the rule. For example: *"Use underscore suffixes for quantity-type markers (`_flow`, `_nominal`, `_small`). Use camelCase postfixes for value qualifiers (`Set`, `Min`, `Max`, `Hea`, `Coo`)."*

---

### Ambiguity 3: When to abbreviate vs. use full words

Set 1 Rule 2 says to use "the first three characters of a word," and most examples follow this (`Hea`, `Coo`, `Dis`, `Sup`). However, Set 2 contains full-word names like `samplePeriod`, `lift_min`, and `retDamPhyPosMax`. No rule clarifies when full words are acceptable or preferred.

**Recommendation:** Add guidance such as: *"Use three-character abbreviations for domain-specific or frequently used terms. Full words may be used for general programming terms or when abbreviation would be ambiguous."*

---

### Ambiguity 4: Ordering of multiple postfix qualifiers

When a name requires multiple qualifiers, the ordering is inconsistent across Set 2's examples:

| Name | Apparent order |
|---|---|
| `TSupSetMin` | Quantity → Set → Min |
| `pMinSet` | Quantity → Min → Set |
| `VDisHeaSetMax_flow` | Quantity → Context → Set → Max → \_flow |

`TSupSetMin` puts `Set` before `Min`, while `pMinSet` puts `Min` before `Set`.

**Recommendation:** Standardize the order explicitly. A suggested canonical order: **Quantity → Context (`Hea`/`Coo`/`Dis`/…) → `Set` → `Min`/`Max` → `_flow`/`_nominal`**.

---

### Ambiguity 5: Set 3 Rule 6 — "block names" interpretation

Set 3 Rule 6 states *"block names and variables usually start with a lowercase letter."* If "block names" refers to **class names**, this contradicts Set 1 Rule 1 (class names start uppercase). If it refers to **instance names** of blocks, it is consistent. Per the user's instructions, if it is a contradiction with Set 1, it is ignored. The consolidated rules above interpret it as referring to instance names.