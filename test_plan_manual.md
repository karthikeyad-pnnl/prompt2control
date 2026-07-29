# Systematic Investigation Plan: `Buildings.Templates.Plants.HeatPumps.Validation.AirToWater` Check Failure

## Overview

This document outlines a systematic investigation to determine the exact root cause of the \"model is not well-posed\" error (equation count exceeds unknown count by 30) in the `AirToWater` validation model, and to identify the required fix.

---

## Step 1: Obtain the Validation Model Source

**File:** `Buildings/Templates/Plants/HeatPumps/Validation/AirToWater.mo`

### Information to Extract

- [ ] The `pla` instantiation: redeclarations and parameter overrides
- [ ] The `datAll` record: which fields are explicitly set vs. defaulted
- [ ] Wiring of `loaHea`, `loaCoo`, `ratLoa` (these contribute to the equation count via `ratLoa.table` and `ratLoa.offset`)
- [ ] Key parameter settings:
  - `nHp`
  - `typDis`
  - `typArrPumPri`, `typArrPumSec`
  - `have_pumChiWatPriDed`, `have_pumHeaWatPriDed`

### Purpose

Determine whether the mismatch originates in the validation scenario itself or is propagated from the template.

---

## Step 2: Inspect the Plant Template and Controller Wrapper

### Files to Examine

- `Buildings/Templates/Plants/HeatPumps/AirToWater.mo` (the `pla` class)
- `Buildings/Templates/Plants/HeatPumps/Components/Controls/*.mo`
  - The outer wrapper: `pla.ctl`
  - The inner G36 block: `pla.ctl.ctl`

### Information to Extract

- [ ] How `pla.ctl.ctl` is instantiated — which `have_*` booleans are set and their sources
- [ ] Which conditional connectors of `ctl` are connected in the `equation` section
- [ ] The `if` guards protecting each `connect()` statement
- [ ] How `staEqu` is propagated from `dat` into `ctl`

### Purpose

Identify inconsistencies where a `have_*` flag inside the controller is `true` while the template's `connect()` is guarded by a different (inconsistent) condition — the classic source of unknowns/equations mismatches.

---

## Step 3: Examine the G36 Plant Controller Interface

**File:** Likely under `Buildings/Controls/OBC/ASHRAE/PrimarySystem/BoilerPlant/...` or an equivalent path for the heat-pump G36 sequence.

### Information to Extract

#### Conditional Input Declarations

Every conditional input appearing as `u_internal` in warnings:

- [ ] `TChiWatRet`, `THeaWatRet`
- [ ] `VChiWatLoa_flow`, `VChiWatSta_flow`
- [ ] `VHeaWatLoa_flow`, `VHeaWatSta_flow`
- [ ] `idxStaCoo.pas[1..3]`, `idxStaHea.pas[1..3]`
- [ ] `staPumChiWatSec.nPumHdrDp.pas[1..3]`
- [ ] `staPumHeaWatSec.nPumHdrDp.pas[1..3]`

#### Associated `enable` Conditions

- [ ] The `enable=` expression on each conditional input
- [ ] Declaration of `staEquSinMod` / `staEquDouMod` parameters (defaulted to `[0,0,0; 0,0,0; 0,0,0]`)
- [ ] `have_valInlIso` / `have_valOutIso` defaults and `enable` logic

### Purpose

Confirm whether the controller's internal `enable` guards match what the template provides.

---

## Step 4: Review the Heat Pump Data Record

**File:** `Buildings/Templates/Plants/HeatPumps/Components/Data/HeatPumpGroup.mo` (or wherever `datAll.pla.hp` is typed).

### Information to Extract

- [ ] The `enable` expression on:
  - `dpSouWwHeaHp_nominal`
  - `mSouWwCooHp_flow_nominal`
  - `mSouWwHeaHp_flow_nominal`
- [ ] The `typ` / `is_airToWater` / equivalent discriminator used in the `enable` predicate

### Purpose

Water-source parameters appearing in an air-to-water scenario strongly suggests the `enable` predicate is wrong, or that the template reads them despite `enable=false`.

---

## Step 5: Capture Version and Provenance Information

### Required Data

- [ ] **Buildings library version or Git commit SHA** (`Buildings.version`)
- [ ] **Modelica tool** and version (Dymola, OpenModelica, etc.)
- [ ] **Modelica Standard Library (MSL)** version

### Notes

- The log phrasing suggests **Dymola** (OpenModelica reports differently).
- Recent releases have substantially changed:
  - `Templates.Plants.HeatPumps`
  - The G36 heat-pump sequence
  - Secondary-pump staging logic

---

## Step 6: Dump Resolved Parameter Values at Check Time

### How to Generate

Run the validation model with one of:

```
Advanced.PrintFailureToDifferentiate = true
Evaluate = true
```

Or extract the translation log / parameter-values section.

### Values to Capture

#### Top-Level Plant Parameters

- [ ] `pla.nHp`
- [ ] `pla.typDis`
- [ ] `pla.typArrPumChiWatPri`, `pla.typArrPumHeaWatPri`
- [ ] `pla.typArrPumChiWatSec`, `pla.typArrPumHeaWatSec`

#### Pump Configuration Flags

- [ ] `pla.have_pumChiWatPriDed`, `pla.have_pumHeaWatPriDed`
- [ ] `pla.have_pumChiWatSec`, `pla.have_pumHeaWatSec`

#### Sensor / Valve Flags

- [ ] `pla.have_senDpChiWatRemWir`, `pla.have_senDpHeaWatRemWir`
- [ ] `pla.have_senVChiWatSec_flow`, `pla.have_senVHeaWatSec_flow`
- [ ] `pla.have_valChiWatMinByp`
- [ ] `pla.have_hrc`

#### Controller Sizing

- [ ] `pla.ctl.ctl.nPumChiWatSec`, `pla.ctl.ctl.nPumHeaWatSec`
- [ ] `pla.ctl.ctl.nSenDpChiWatRem`, `pla.ctl.ctl.nSenDpHeaWatRem`
- [ ] `pla.ctl.ctl.staPumChiWatSec.have_valInlIso`, `have_valOutIso`
- [ ] `pla.ctl.ctl.staPumChiWatSec.nEquAlt`, `nSta`

#### Staging Matrix

- [ ] `pla.ctl.staEqu` as a fully-resolved numeric matrix

### Purpose

With these numbers, the symbolic equation-count expression becomes simple arithmetic — enabling precise identification of which `nin` or `have_*` contributes the surplus 30 equations.

---

## Step 7: Determine Whether This is a Regression

### Questions to Answer

- [ ] Did this model check cleanly in a previous Buildings library version?
- [ ] If so, what's the most recent known-good commit?
- [ ] Was `typDis = Constant1Variable2` added or changed recently?
- [ ] Is `typDis_select2` a new dropdown pattern requiring explicit user choice?

### Purpose

The `typDis_select2` warning with a `start` value suggests a replaceable dropdown that prior versions may have silently defaulted. Confirm whether a recent change now requires an explicit selection.

---

## Step 8: Build a Minimal Reproducer (Optional but Ideal)

### Objective

Create a stripped-down version of the validation model that still fails, using:

- Same plant instantiation
- Simplest possible load side

### Purpose

Isolate whether `loaHea` / `loaCoo` / `ratLoa` contribute to the imbalance (they appear in the equation-count expression via `ratLoa.table` size), or whether the fault is entirely inside `pla`.

---

## Priority Matrix

If providing complete information is not feasible, gather these three items in priority order:

| Priority | Item | Step |
|:--------:|------|:----:|
| 1 | Validation model source (`AirToWater.mo` in `Validation`) | Step 1 |
| 2 | Resolved parameter dump — especially `nHp`, `typDis`, all `have_*` flags inside `pla.ctl.ctl`, and `staEqu` | Step 6 |
| 3 | Buildings library version / Git commit + Modelica tool name and version | Step 5 |

These three are usually sufficient to localize the −30 imbalance to a specific `connect()` / `enable=` mismatch and propose the fix.

---

## Expected Outcome

Once the data above is collected, the investigation should yield:

1. **Identification** of the specific conditional connector(s) causing the equation surplus
2. **Localization** of the inconsistent `have_*` flag or `enable=` predicate
3. **A targeted fix**, typically:
   - A corrected `enable` expression in a data record, or
   - A corrected `connect()` guard in the template, or
   - An explicit parameter setting in the validation model