# Consolidated Naming Convention Rules (Revised)

Below is the unified rule set. All previously identified contradictions and
ambiguities have been resolved; a change log appears at the end.

---

## 1. Class Names (Models, Blocks, Packages)

**1.1** Class names shall start with an **uppercase letter** and be a noun,
or a combination of adjectives and nouns.

**1.2** Use **UpperCamelCase (PascalCase)** to combine multiple words
(e.g., `HeatTransfer`, `BoilerPolynomial`).

**1.3** Do not repeat higher-level package names. Use `Chillers.Carnot`,
not `Chillers.CarnotChiller`. Similarly, avoid descriptors in names that are
already obvious from the enclosing package (e.g., avoid `boi` for boiler if
the block is already in a `BoilerPlant` package).

---

## 2. Instance and Variable Names

### 2.1 General Structure

**2.1.1** Instance names — including variables, **block instances** (i.e.,
instances of block classes, not the class definitions themselves, which are
governed by §1), and parameters — shall start with a **lowercase letter**,
unless they represent a physical quantity conventionally capitalised
(e.g., `T` for temperature, `P` for power, `X` for mass fraction).

**2.1.2** Names are composed following this pattern:

| Position | Element | Examples |
|---|---|---|
| 1. Prefix *(optional)* | `u` for input, `y` for output — include only if needed for context | `uOpeMod`, `yHeaCoi` |
| 2. Quantity *(required)* | The physical quantity or descriptor | `TOut`, `TZonHea`, `dpBui` |
| 3. Postfix / Qualifier *(optional)* | Modifiers such as setpoint, min, max, cooling, heating, etc., appended **after** the quantity | `TZonHeaSet`, `TSupSetMin` |

**2.1.3** Strive for **short names**. Omit prefix or postfix when the
meaning is clear from context. For example, a room thermostat may simply
use `T` as its input.

### 2.2 Abbreviation Conventions

**2.2.1** Use abbreviations composed of **the first three characters** of
each word, combined in lowerCamelCase (e.g., `preDro` for pressure drop,
`worTim` for working timer, `zonDisEffHea` for zone distribution
effectiveness heating). Two or four characters may be used when three
characters would be ambiguous or when a natural breakpoint in the word
makes a different length clearer.

**2.2.2** Single characters may be used where generally understood
(e.g., `T`, `p`, `k`, `n`, `u`, `y`). These may be augmented with
descriptors as needed (e.g., `yVal` for valve signal, `yDam` for damper
signal, `kCoo` for cooling gain).

**2.2.3** **Full (unabbreviated) words** may be used for:

- General programming terms not specific to the HVAC/building domain
  (e.g., `samplePeriod`).
- Standard Modelica / library underscore suffixes (e.g., `_nominal`,
  `_flow`; see §6).
- Cases where the three-character abbreviation would be ambiguous or
  unrecognisable to a domain practitioner.

In all other cases — particularly for HVAC/building-domain terms that
appear frequently — the three-character abbreviation rule applies.

### 2.3 Cross-Package Consistency

**2.3.1** If an analogous sequence exists for another system (e.g., heating
vs. cooling, chiller plant vs. boiler plant), use **consistent, parallel
names** across both to facilitate commonisation.

**2.3.2** For feedback delay `pre` block instances, use **numbered names**
(`pre1`, `pre2`, etc.) rather than bare `pre`.

---

## 3. Standard Physical Quantity Variables

**3.1** The following single-character or short variables are standard:

| Variable | Meaning |
|---|---|
| `T` | Temperature |
| `p` | Pressure |
| `dp` | Pressure difference |
| `P` | Power |
| `E` | Energy (general) |
| `Q` | Thermal energy |
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

---

## 4. Control Signal Naming

**4.1** Control **input** signals start with `u`; control **output** signals
start with `y`.

**4.2** The `u`/`y` prefix may be **omitted** when the physical quantity
already makes the direction clear (e.g., a temperature sensor output may
simply be `T` or `TOut` rather than `yT`).

**4.3** When a controller has multiple outputs or inputs, augment with a
descriptor (e.g., `yVal` and `yDam` for valve and damper output signals;
`uHea` and `uCoo` for heating and cooling input signals).

---

## 5. Prefix Conventions

**5.1** The following prefixes are standard:

| Prefix | Meaning | Examples |
|---|---|---|
| `u` | Control input signal | `uOpeMod`, `uDam`, `uHea`, `uCoo` |
| `y` | Control output signal | `yHeaCoi`, `yCooCoi`, `yPosMin`, `yChiPumSpe` |
| `use_` | Conditionally enabled input or feature (boolean parameter). *"Should the model use this optional input/feature?"* | `use_TMix`, `use_enthalpy` |
| `have_` | The system/zone **has** a particular component, sensor, or physical configuration (boolean parameter). *"Does this system physically include this?"* | `have_CO2Sen`, `have_occSen`, `have_winSen`, `have_parChi` |
| `need_` | A required **control capability or operational constraint** (boolean parameter). *"Does the control logic need to enforce this behaviour?"* | `need_redChiDem` |

**5.2** Names following `use_`, `have_`, and `need_` prefixes shall apply
the same abbreviation conventions as other variables (see §2.2). Full words
are acceptable only under the exceptions listed in §2.2.3.

---

## 6. Suffix / Postfix Conventions

### 6.1 Two Suffix Types

Suffixes fall into two categories, each with a distinct formatting rule:

| Category | Formatting rule | Purpose | Standard set |
|---|---|---|---|
| **Quantity-type markers** | Underscore + **full (unabbreviated) word** | Classify the variable's fundamental nature or modelling role. Library-wide or Modelica-wide conventions. | `_flow`, `_nominal`, `_small`, `_remote` |
| **Value qualifiers** | **CamelCase, no underscore**, following the three-character abbreviation convention (§2.2) | Narrow the engineering meaning of the specific variable. | `Set`, `Min`, `Max`, `Hea`, `Coo` |

> **Rationale:** If the suffix is an unabbreviated word that classifies the
> variable's role, it takes an underscore. If it is an abbreviated qualifier
> that specifies the engineering context or constrains the value, it is
> written in CamelCase with no underscore. New underscore suffixes should
> be introduced sparingly and only for broadly applicable concepts used
> consistently across the library.

### 6.2 Standard Suffixes

| Suffix | Type | Meaning | Examples |
|---|---|---|---|
| `_flow` | Quantity-type | Flow variable | `Q_flow`, `m_flow`, `V_flow`, `VDis_flow` |
| `_nominal` | Quantity-type | Design / nominal capacity | `Q_flow_nominal`, `m_flow_nominal` |
| `_small` | Quantity-type | Small value for regularisation | — |
| `_remote` | Quantity-type | From a remote sensor | `dpChiWat_remote` |
| `_select` | Quantity-type | Dummy variable used to enforce configuration options. This has no bearing on almost identical parameters without `_select` | `have_hrc_select` |
| `Set` | Value qualifier | Setpoint | `TZonHeaSet`, `TZonCooSet` |
| `Min` | Value qualifier | Minimum | `TSupSetMin`, `lifMin` |
| `Max` | Value qualifier | Maximum | `TZonCooMax`, `VDisHeaSetMax_flow` |
| `Hea` | Value qualifier | Heating qualifier | `TZonHeaSet`, `zonDisEffHea` |
| `Coo` | Value qualifier | Cooling qualifier | `yCooCoi`, `zonDisEffCoo` |

### 6.3 Ordering of Multiple Suffixes

When a name requires multiple suffixes, follow this canonical order:

> **Quantity → Context / Domain (`Sup`, `Zon`, `Dis`, …) → Domain Qualifier
> (`Hea`, `Coo`, …) → `Set` → `Min` / `Max` → `_flow` → `_nominal`**

| Example | Decomposition |
|---|---|
| `TSupSetMin` | `T` (quantity) → `Sup` (context) → `Set` → `Min` |
| `TZonHeaSet` | `T` (quantity) → `Zon` (context) → `Hea` (qualifier) → `Set` |
| `VDisHeaSetMax_flow` | `V` (quantity) → `Dis` (context) → `Hea` (qualifier) → `Set` → `Max` → `_flow` |
| `m_flow_nominal` | `m` (quantity) → `_flow` → `_nominal` |

> **Important:** Value qualifiers such as `Min`, `Max`, `Set`, `Hea`, `Coo`
> must always appear as **postfixes**, never as prefixes.
> For example, use `chiLifMin`, **not** `minChiLif`.

---

## 7. Connector Naming

**7.1** Paired connectors of the same domain (identical declarations,
different icons) are distinguished by:

| Convention | Usage | Example |
|---|---|---|
| `_a` / `_b` | Fluid ports | `port_a`, `port_b` |
| `_p` / `_n` | Electrical terminals | `terminal_p`, `terminal_n` |

---

## 8. Psychrometrics Package Naming (`Buildings.Utilities.Psychrometrics`)

**8.1** Uppercase `X` = mass fraction per total mass; lowercase `x` = mass
fraction per mass of dry air.

**8.2** The notation `z_xy` denotes a function or block with output `z` and
inputs `x` and `y`.

**8.3** Standard symbols:

| Symbol | Meaning |
|---|---|
| `pW` | Water vapour pressure |
| `TDewPoi` | Dew point temperature |
| `TWetBul` | Wet bulb temperature |
| `TDryBul` (or `T`) | Dry bulb temperature |
