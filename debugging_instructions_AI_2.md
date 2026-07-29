# AI Agent Investigation Checklist (Continuation): `Buildings.Templates.Plants.HeatPumps.Validation.AirToWater`

## Mission (Phase 2)
The placeholder/start-only patch did not eliminate the structural deficit; the model is still over-determined by 30 equations. Heating-only isolation localized real unconnected inputs (`or1[1..3].u1`, `andHeaEna[1..3].u2`, `notCooMod[1..3].u`) inside `pla.ctl.ctl`. The two-HP probe showed the deficit scales with `nHp`. Phase 2 narrows the hunt to those array signals and the cross-mode wiring around them, and verifies any fix against the working sibling `HybridAirToWater`.

## Available Capabilities
- You will only use the skills defined within this workspace, and no other terminal commands.
- You will utilize the `generate_code_analysis_inputs_2` method to extract information about the connectors and the internal instances in a block.
- You will utilize the `get_extend_statements` method to extract any extends statements within a block.
- To understand the logic of a block and study its connections, you will check for any extends statements and retrieve information about its connectors and other internal instances.
- The library root is `c:\buildings_library\modelica-buildings`.

## Carry-Forward Facts From Phase 1
- Buildings 13.0.0 + MSL 4.1.0 + Dymola 2025x. Branch `issue4304_HybridAirSourceHeatPumpPlantControls_April2026`.
- Baseline: 18551 unknowns, 18551 equations, reduced difference **-30**.
- After Step 10 patch (PlaceholderReal/Logical defaults, StagingHeadered `dtRun` binding): 18575/18575, reduced difference still **-30**.
- All component- and utility-level validations check **balanced** (StagingHeadered, EquipmentEnable, StageChangeCommand, StageCompletion, HeatPumpGroupAirToWater, HeatRecoveryChiller, PumpsPrimaryDedicated, ValvesIsolation, HybridAirToWater).
- Heating-only variant: residual collapses from -30 to **-6**, and Dymola flags:
  - `pla.ctl.ctl.or1[1..3].u1`
  - `pla.ctl.ctl.andHeaEna[1..3].u2`
  - `pla.ctl.ctl.notCooMod[1..3].u`
- Two-HP variant (with synchronized 2x2 staging matrices): residual reduces from -30 to **-16**, confirming per-HP scaling (~7 per equipment).
- HRC-disabled variant: residual remains **-30** → HRC is not the cause.
- No `connect()`/`enable` mismatches found in Step 5 for the originally flagged conditional inputs.

## Output Format Requirement
For every step below, record findings in the form:
```
## Step N Findings
- File(s) inspected: <paths>
- Key observations: <bullet list>
- Hypotheses generated/refuted: <bullet list>
- Artifacts produced: <log files, extracted snippets>
```
At the end, produce an updated **Root Cause Report** and **Proposed Fix** section.

---

## Step 12 — Cooling-Only Complement
Mirror the Step 11.5 heating-only experiment to partition the deficit by mode.

- [ ] Create temporary model `Buildings.Templates.Plants.HeatPumps.Validation.AirToWaterCoolingOnly` that extends the failing validation model and forces `have_heaWat = false` (and any sibling flag required to disable the heating-water side without disabling the cooling-water side).
- [ ] Run `checkModel` and capture the full log to `logs/12_cooling_only.log`.
- [ ] Extract and record in `findings/12_cooling_only.md`:
  - Final unknown/equation counts and the "difference could be reduced to" value.
  - Any unconnected-input localizations Dymola emits (mirror format used in Step 11.5).
  - Compare against heating-only -6 residual; expected complement is roughly -24 if mode-partitioning is linear.
- [ ] Build a partition table:

  | Variant | Reduced difference | Localized unconnected inputs |
  |---|---|---|
  | Full (both modes) | -30 | (not localized) |
  | Heating-only (have_chiWat=false) | -6 | or1[1..3].u1, andHeaEna[1..3].u2, notCooMod[1..3].u |
  | Cooling-only (have_heaWat=false) | ? | ? |

- [ ] Delete the temporary file at end of step (mirror Step 11.8 hygiene).

**Stop condition:** Cooling-only residual recorded. Mode partitioning understood.

---

## Step 13 — Locate `or1`, `andHeaEna`, `notCooMod` in the Controller
This is the single most important step. The goal is to determine whether each of the 9 input pins (`or1[1..3].u1`, `andHeaEna[1..3].u2`, `notCooMod[1..3].u`) has a `connect()` statement reaching it under the failing configuration.

- [ ] Open `Buildings/Templates/Plants/Controls/HeatPumps/AirToWater.mo`.
- [ ] For each of `or1`, `andHeaEna`, `notCooMod`:
  - Record the declaration line: type, array dimension expression (`nHp`, `nHpAwh`, `nHpTot`, `nHpHeaCoo`, …), conditional `if` guard on the declaration (if any), and any `each` modifiers.
  - Record every `connect()` statement that targets the relevant pin (`u1`, `u2`, or `u`) — including connects buried in `for` loops or `if`-equations.
  - For each `connect()`, record:
    - Source side
    - Loop range (e.g. `for i in 1:nHp`, `for i in 1:nHpHeaCoo`, etc.)
    - Guard expression (`if have_chiWat`, `if have_heaWat`, `if have_hrc`, …)
    - Whether the guard is on the `connect()` itself or on a containing block
- [ ] Build the wiring table in `findings/13_cross_mode_wiring.md`:

  | Target pin | Source | Loop / index | Guard | Active when have_chiWat=true | Active when have_chiWat=false | Active when have_heaWat=false |
  |---|---|---|---|---|---|---|
  | or1[i].u1 | … | … | … | … | … | … |
  | andHeaEna[i].u2 | … | … | … | … | … | … |
  | notCooMod[i].u | … | … | … | … | … | … |

- [ ] Specifically check for these defect patterns:
  - A `for` loop iterating only over a subset of the array (e.g. `for i in 1:nHpHeaCoo` while the array has size `nHp`).
  - A `connect()` whose guard references the **wrong** boolean (e.g. `if have_hrc` where it should be `if have_chiWat`).
  - An array indexed inconsistently between source and target (e.g. mapping `[1:nHpHea]` to `[1:nHp]`).
  - A second `connect()` to the same pin that doubles up an equation (over-connection rather than under-connection).
- [ ] Flag every row where the pin is unconnected under the failing configuration **or** doubly connected.

**Stop condition:** Each of the 9 pins is classified as connected, unconnected, or over-connected for the failing configuration.

# AI Agent Investigation Checklist (Phase 2 — Step 13.5 Refinement)

## Status Update
Step 13 has produced the **decisive lead**: `or1.u2` is the target of two separate `connect()` statements:
- `connect(ctlPlaHyb.yAvaHpShcCoo, or1.u2)` (HRC-shc pathway)
- `connect(booScaRep.y, or1.u2)` (scalar-replicate fallback)

If both are simultaneously active under the failing configuration, this is a textbook **over-connection** producing extra equations — exactly what produces a -N-style imbalance.

Symmetrically, the heating-only probe localizes `or1[*].u1`, `andHeaEna[*].u2`, `notCooMod[*].u` as **unconnected**. Their declared sources are:
- `or1.u1` ← `avaEquHeaCoo.y1Coo`
- `andHeaEna.u2` ← `y1HeaPre.y`
- `notCooMod.u` ← `y1HeaPre.y`

So the question becomes: **why do these source signals disappear** when `have_chiWat=false` (heating-only probe), and **why do those two `or1.u2` sources both fire** when `have_chiWat=true` (failing config)?

The most likely mechanism is a **conditional declaration** on the source blocks (`avaEquHeaCoo`, `ctlPlaHyb`, `booScaRep`, `y1HeaPre`, `y1HpPre`) that is wrong or asymmetric. When the source is conditionally absent, the corresponding `connect()` statement automatically drops out under Modelica semantics — but if **both** alternatives' sources are simultaneously present, both connects are active and we get over-determination.

This is also consistent with the per-HP arithmetic: each defective array pin contributes `nHpTot` equations.

## Mission of Step 13.5
Verify or refute the over-connection hypothesis on `or1.u2` and characterize the conditional structure of all five source blocks.

## Output Format Requirement
Same as prior steps. Save to `findings/13_5_source_block_audit.md`.

---

## Step 13.5.a — Source Block Declaration Audit
- [ ] Open `Buildings/Templates/Plants/Controls/HeatPumps/AirToWater.mo` and locate the declaration of each of these blocks:
  - `avaEquHeaCoo`
  - `ctlPlaHyb`
  - `booScaRep`
  - `y1HeaPre`
  - `y1HpPre`
- [ ] For each block, record:
  - Full type path
  - Array dimension expression (if any)
  - Conditional `if` guard on the declaration (e.g. `if have_chiWat`, `if have_hrc`, `if have_heaWat`, `if cfg.have_HpShc`, …)
  - Resolution of that guard under the failing full configuration (have_chiWat=true, have_heaWat=true, have_hrc=true, nHp=3)
  - Resolution under the heating-only probe (have_chiWat=false)

- [ ] Build the table:

  | Block | Type | Conditional guard on declaration | Active in failing config? | Active in heating-only probe? |
  |---|---|---|---|---|
  | avaEquHeaCoo | … | … | … | … |
  | ctlPlaHyb | … | … | … | … |
  | booScaRep | … | … | … | … |
  | y1HeaPre | … | … | … | … |
  | y1HpPre | … | … | … | … |

**Acceptance test:** The hypothesis is confirmed if **both** `ctlPlaHyb` and `booScaRep` are simultaneously active under the failing configuration, **or** if `avaEquHeaCoo` / `y1HeaPre` are conditionally absent under the heating-only probe in a way that strands the downstream `or1.u1`, `andHeaEna.u2`, `notCooMod.u` pins.

---

## Step 13.5.b — Connect Guard Re-Inspection
The Step 13 audit reported "no `if` guards around the connect statements," but Modelica `connect()` calls can be **inside an `if`-equation block** that the textual scan may have missed. Re-verify by reading the surrounding lines.

- [ ] For each of these connect statements, record the **exact enclosing block** (search 30 lines above for any `if … then` opening):
  - `connect(avaEquHeaCoo.y1Coo, or1.u1)`
  - `connect(ctlPlaHyb.yAvaHpShcCoo, or1.u2)`
  - `connect(booScaRep.y, or1.u2)`
  - `connect(y1HpPre.y, andHeaEna.u1)`
  - `connect(y1HeaPre.y, andHeaEna.u2)`
  - `connect(y1HeaPre.y, notCooMod.u)`
- [ ] Confirm whether each is in an unguarded `equation` section, inside an `if … then ... end if;` block, or inside a `for` loop.
- [ ] Record file line numbers.

---

## Step 13.5.c — Conditional-Connect Dropping Semantics Cross-Check
In Modelica, a `connect(A, B)` where `A` is a conditional component currently absent is **silently dropped**. So if `ctlPlaHyb` is conditional on `have_hrc` and `booScaRep` is conditional on `not have_hrc`, the two connects to `or1.u2` are mutually exclusive and the wiring is correct. If they are **not** mutually exclusive, the wiring is broken.

- [ ] Build this mutual-exclusion table:

  | Pair | Source A guard | Source B guard | Mutually exclusive? | Both active in failing config? |
  |---|---|---|---|---|
  | (ctlPlaHyb, booScaRep) into or1.u2 | … | … | … | … |

- [ ] If "Both active in failing config?" = Yes for any row, that row is the over-connection defect.

---

## Step 13.5.d — Track the Heating-Only Disconnect
The heating-only probe localized `or1[*].u1`, `andHeaEna[*].u2`, `notCooMod[*].u` as unconnected when `have_chiWat=false`. Trace why each source signal disappears.

- [ ] For `or1.u1` ← `avaEquHeaCoo.y1Coo`:
  - Is `avaEquHeaCoo` conditional on `have_chiWat`?
  - Is the inner pin `y1Coo` conditional on `have_chiWat`?
  - Either way, when `have_chiWat=false`, does this connect drop out?
- [ ] For `andHeaEna.u2` ← `y1HeaPre.y`:
  - Is `y1HeaPre` conditional on `have_chiWat`? (Plausible: a "previous heating-mode" signal might only be needed when mode switching is possible, i.e. when both modes exist.)
  - If yes, this would be the heating-only -6 defect (3 pins × 2 signals = 6 equations missing).
- [ ] For `notCooMod.u` ← `y1HeaPre.y`:
  - Same source as above. Same disposition.

- [ ] Record findings.

---

## Step 13.5.e — Per-HP Arithmetic Reconciliation
- [ ] If the over-connection on `or1.u2` is confirmed (Step 13.5.c) and `nHpTot` resolves to **8** under the failing config:
  - 8 equations stranded over-connection ≈ ½ of -16 cooling-mode-attributable equations per HP × 3 HPs.
  - Insufficient by itself; expect at least one additional defect.
- [ ] If `nHpTot=3` under failing config:
  - 3 equations from over-connection + heating-only -6 + ??? ≠ -30. Still insufficient; another contributor exists.
- [ ] Record `nHpTot` resolution explicitly (it likely equals `nHp + nHrc + nHpShc` or similar; resolve under failing config).
- [ ] If a single defect cannot account for -30, list **all** candidate contributors and rank by likelihood.

---

## Step 13.5.f — Compare Same Code Block in HybridAirToWater Validation
The Hybrid validation passes. Either the same controller class is used with a different `cfg`, **or** the wrapper differs.

- [ ] Open `Buildings/Templates/Plants/HeatPumps/Components/Controls/HybridAirToWater.mo` and verify it instantiates the same `Buildings.Templates.Plants.Controls.HeatPumps.AirTo
---

## Step 14 — Hybrid vs Failing Diff (Top-Down)

### 14.a — Identify Plant Template Used by Each Validation
- [ ] Open `Buildings/Templates/Plants/HeatPumps/Validation/AirToWater.mo` and record the **type path** of `pla` (e.g. `Buildings.Templates.Plants.HeatPumps.AirToWater`).
- [ ] Open `Buildings/Templates/Plants/HeatPumps/Validation/HybridAirToWater.mo` and record the **type path** of `pla` (likely `Buildings.Templates.Plants.HeatPumps.HybridAirToWater` or similar).
- [ ] Confirm whether the two validations instantiate the **same plant class** parameterized differently, or **different plant classes**.
- [ ] Record both plant template paths in `findings/14_diff_vs_hybrid.md`.

### 14.b — Plant-Class Inheritance Tree
- [ ] For each plant class identified above, walk the inheritance tree and list all `extends` relationships up to `PartialHeatPumpPlant`.
- [ ] Record:
  - File path of each class
  - Direct parent (`extends X`)
  - Any `redeclare` statements applied at this level
- [ ] Build a side-by-side tree:

  | Level | Failing template | Hybrid template |
  |---|---|---|
  | Validation `pla` type | … | … |
  | Parent | … | … |
  | Grandparent | … | … |
  | Common ancestor | PartialHeatPumpPlant | PartialHeatPumpPlant |

### 14.c — Connect-Section Diff
- [ ] Diff the equation/connect sections between the two plant templates (or, if they are the same class, diff the parameter overrides between the two validations).
- [ ] Specifically focus on connects involving:
  - `ctl.bus` or any controller-bus signals
  - Array signals indexed by `nHp` or `nHpTot`
  - `mode`, `enable`, `availability`, or staging signals
  - HRC-related signals (since HRC disable doesn't help, ensure the HRC connect block isn't introducing the deficit even when disabled)
- [ ] For each differing block, record file + line range and side-by-side excerpt.

### 14.d — Parameter / Modifier Diff
- [ ] Diff the parameter overrides applied at the `pla` instantiation between the two validations:
  - Validation/AirToWater.mo `pla(...)` modifiers
  - Validation/HybridAirToWater.mo `pla(...)` modifiers
- [ ] Resolve every `cfg.have_*`, `cfg.typ*`, `cfg.n*` field under both validations and tabulate side-by-side. Flag any field where they differ.

  | cfg field | Failing AirToWater | Hybrid | Differs? |
  |---|---|---|---|
  | have_chiWat | … | … | … |
  | have_heaWat | … | … | … |
  | have_hrc | … | … | … |
  | have_HpShc | … | … | … |
  | nHp | … | … | … |
  | nHpShc | … | … | … |
  | typArrPumPri | … | … | … |
  | typDis | … | … | … |
  | nPumChiWatSec | … | … | … |
  | nPumHeaWatSec | … | … | … |

- [ ] **Crucial:** any `cfg` field that differs between the two validations and that resolves to a value reachable only by the failing path is a prime defect candidate.

**Stop condition:** Concrete differing block or parameter identified, or both confirmed structurally identical with the only difference being HRC/HpShc-related (which the Step 11.4 HRC-disable probe already partially refuted).

---

## Mission of Revised Step 15
Confirm the `nHpShc` axis with a one-toggle probe and then enumerate every component, connect, and equation in the controller that is gated by `have_HpShc` (or `not have_HpShc`). The defect is one of:
- A block conditional on `have_HpShc` that has no fallback when `not have_HpShc` (under-determined),
- A block conditional on `not have_HpShc` that double-binds a signal that is otherwise also driven (over-determined),
- A bus signal whose equation count differs between the two branches.

## Output Format Requirement
Same as prior steps. Save to `findings/15_nhpshc_axis.md`.

---

## Step 15.a — One-Toggle Confirmation
Confirm the axis with a single experiment.

- [ ] Create temporary `Buildings.Templates.Plants.HeatPumps.Validation.AirToWaterShc` extending `AirToWater` with the **single** modification `cfg(nHpShc=1)`.
  - Be careful with staging-matrix dimensions: with `nHpShc=1` and `nHp=3`, `nHpTot=4`, so `staEquSinMod` and `staEquDouMod` must be sized `[nSta, 4]`. Update the matrix overrides to e.g. `staEquSinMod={{1/4,1/4,1/4,1/4},{2/4,2/4,2/4,2/4},{1,1,1,1}}` and similarly for `staEquDouMod`.
  - Any other dimension-coupled record (HRC tables, etc.) may also need adjustment. If so, record what had to change.
- [ ] Run `checkModel`, capture log to `logs/15a_shc_axis.log`.
- [ ] Record reduced difference. Expected: 0 (or sharply reduced from -30).
- [ ] Delete temporary file at end of step.

**Stop condition:** `nHpShc` axis confirmed (reduced difference closes by ~30 or to 0). If it does not, the axis hypothesis is wrong and revert to the broader bisection.

---

## Step 15.b — Enumerate `have_HpShc` Branches in the Controller
- [ ] Open `Buildings/Templates/Plants/Controls/HeatPumps/AirToWater.mo`.
- [ ] Search for every occurrence of `have_HpShc` and `nHpShc` (case-sensitive). Record:
  - Line number
  - Context (declaration guard, equation guard, parameter expression, dimension expression, `connect()` line)
  - Branch sign: does this code activate when `have_HpShc=true`, `have_HpShc=false`, or both?
- [ ] Build a master table:

  | Line | Construct | Activates when | What it adds (equations / connects) |
  |---|---|---|---|
  | … | declaration `ctlPlaHyb` | have_HpShc=true | one HybridOperation block |
  | … | declaration `booScaRep` | have_HpShc=false | one BooleanScalarReplicator |
  | … | connect to or1.u2 | have_HpShc=true | 1 connect |
  | … | connect to or1.u2 | have_HpShc=false | 1 connect |
  | … | … | … | … |

- [ ] **Pair every `if have_HpShc` block with a counterpart `if not have_HpShc` block.** Flag any unpaired branch:
  - A `then` branch with no symmetric `else` — under-determined when not have_HpShc
  - A connect to a signal whose alternative-branch source has different cardinality

---

## Step 15.c — Inspect `HybridOperation` vs `BooleanScalarReplicator` Output Cardinality
The two mutually-exclusive blocks must produce **the same equation count** when consumed downstream.

- [ ] Open `Buildings.Templates.Plants.Controls.StagingRotation.HybridOperation` (the type of `ctlPlaHyb`).
- [ ] List every output pin and its array dimension.
- [ ] Open `Buildings.Controls.OBC.CDL.Routing.BooleanScalarReplicator`.
- [ ] List its output pin and array dimension.
- [ ] In the controller `Controls/HeatPumps/AirToWater.mo`, list every `connect()` involving `ctlPlaHyb.*` outputs (in `if have_HpShc` blocks or unconditionally with conditional source).
- [ ] List every `connect()` involving `booScaRep.y`.
- [ ] Build a side-by-side table:

  | Downstream pin | Source when have_HpShc=true | Source when have_HpShc=false | Equation count match? |
  |---|---|---|---|
  |

---

# AI Agent Investigation Checklist (Phase 2 — Step 16: Decompose Residual −30)

## Status After Step 15
- SHC axis confirmed as primary contributor: nHpShc=0→1 closes 18 of 30 equations.
- Residual −12 persists at nHp=3, nHpShc=1.
- Reference passing config (Hybrid validation) uses nHp=2, nHpShc=1.

## Working Decomposition
- Component A: `not have_HpShc` branch contributes ~6 extra equations per HP that is not classified as SHC. (3 non-SHC HPs at nHpShc=0 → 18; 2 non-SHC HPs at nHpShc=1, nHp=3 → ~12; 1 non-SHC HP at nHpShc=1, nHp=2 → ~6, but Hybrid still passes — see Component B.)
- Component B: A configuration-fixed contributor (~−6 or coupled with nHp) that the Hybrid validation suppresses through some other modifier.

## Mission of Step 16
Add two more data points to fully separate Components A and B, then localize each.

## Output Format Requirement
Same as prior steps. Save to `findings/16_decomposition.md`.

---

## Step 16.a — Two-Point Bisection on (nHp, nHpShc)
Add two more data points to nail down per-HP scaling on each branch.

- [ ] Create temporary `Buildings.Templates.Plants.HeatPumps.Validation.AirToWaterShc2`:
  - Extends `AirToWater` with `cfg(nHpShc=2)`, `nHp=3`, so `nHpTot=5` (3 non-SHC + 2 SHC).
  - Resize `staEqu*` matrices to `[nSta, 5]`. Use uniform fractions (e.g. `{{1/5,1/5,1/5,1/5,1/5},{2/5,...},{1,1,1,1,1}}`).
- [ ] Run `checkModel`, capture log to `logs/16a_shc2.log`. Record reduced difference.
- [ ] Create temporary `Buildings.Templates.Plants.HeatPumps.Validation.AirToWaterShc3`:
  - Extends `AirToWater` with `cfg(nHpShc=3)`, `nHp=3`, so `nHpTot=6` (3 non-SHC + 3 SHC).
  - Resize `staEqu*` matrices to `[nSta, 6]`.
- [ ] Run `checkModel`, capture log to `logs/16a_shc3.log`. Record reduced difference.
- [ ] Tabulate:

  | nHp | nHpShc | non-SHC count | Reduced diff | ΔReducedDiff per non-SHC HP |
  |---|---|---|---|---|
  | 3 | 0 | 3 | −30 | — |
  | 3 | 1 | 2 | −12 | +18 (+6/HP reclassified) |
  | 3 | 2 | 1 | ? | ? |
  | 3 | 3 | 0 | ? | ? |

- [ ] If at nHpShc=3 (zero non-SHC HPs) the residual closes to **0**, then Component B does not exist — Component A alone explains everything, and the per-HP scaling is exactly 6 equations per non-SHC HP.
- [ ] If at nHpShc=3 the residual closes to a **non-zero constant** (e.g. −6, −12), Component B is real and equals that constant.
- [ ] Delete temporary files at end of step.

**Stop condition:** Per-HP scaling on the non-SHC branch quantified, and Component B isolated (zero or nonzero).

---

## Step 16.b — Locate the Per-HP Excess on the Non-SHC Branch

If Step 16.a confirms ~6 equations/HP on the non-SHC branch, locate them.

- [ ] In `Buildings/Templates/Plants/Controls/HeatPumps/AirToWater.mo`, list every block whose declaration or equation guard depends on `have_HpShc` / `not have_HpShc`. (Step 15.b already started this — extend it.)
- [ ] For each non-SHC-only block (i.e. `if not have_HpShc`), evaluate:
  - Equation count it adds (declaration size × equations per element)
  - Whether the same block has a SHC counterpart of identical equation count
  - Specifically check: `staMat[nSta,nHpTot]`, `con`, `booScaRep`, `pasPumHeaWatPri`
- [ ] For each block consumed by both branches (i.e. always-active blocks fed by either `ctlPlaHyb` or `booScaRep`/`staMat`), check whether its equation count depends on whether the source provides per-HP information vs replicated scalar information:
  - `or1`, `or2` (OR gates of size `nHpTot`): both branches feed `[nHpTot]`-sized vectors → equation count should match.
  - `avaStaHea`, `avaStaCoo` (consume `staEqu` matrix): SHC branch feeds `ctlPlaHyb.yStaEqu[nSta,nHp]`; non-SHC branch feeds `staMat.y[nSta,nHpTot]`. **Note size mismatch: nHp vs nHpTot.** Investigate whether this is a defect or whether `ctlPlaHyb.yStaEqu` is actually `[nSta,nHpTot]`.
  - `pasPumHeaWatPri`: pass-through declared only on non-SHC branch — does the SHC branch have a different equation in its place? Or does the SHC branch use `or6/or7` instead?
- [ ] Build:

  | Block | Branch active when | Equations contributed | Counterpart in other branch | Counterpart contributions |
  |---|---|---|---|---|
  | … | … | … | … | … |

- [ ] Flag any row where contributions differ by ~6 per HP.

---

## Step 16.c — `ctlPlaHyb.yStaEqu` Dimension Audit

The `yStaEqu[nSta,nHp]` declaration in `HybridOperation` (per Step 15.c) is suspicious because `staMat` on the non-SHC branch is sized `[nSta, nHpTot]`. If `ctlPlaHyb.yStaEqu` is in fact `[nSta, nHp]` (not `[nSta, nHpTot]`), the two branches feed downstream `avaStaHea.staEqu` / `avaStaCoo.staEqu` with different sizes — yet the controller compiles in the SHC branch, suggesting some implicit size adaption. This may also be where the per-HP excess hides.

- [ ] Open `Buildings/Templates/Plants/Controls/StagingRotation/HybridOperation.mo`.
- [ ] Confirm exact declaration of `yStaEqu`: is it `[nSta, nHp]` or `[nSta, nHpTot]` (where `nHpTot` here might be local to `HybridOperation` and equal `nHp+nHpShc` or just `nHp`)?
- [ ] Check `avaStaHea` and `avaStaCoo` declarations in `Buildings/Templates/Plants/Controls/HeatPumps/AirToWater.mo`. What dimension does their `staEqu` parameter expect?
- [ ] Trace the `connect(ctlPlaHyb.yStaEqu, avaStaHea.staEqu)` and `connect(staMat.y, avaStaHea.staEqu)` to verify both connect targets accept the same dimension.
- [ ] If there's a mismatch, this is likely the per-HP-excess source.

---

## Step 16.d — Locate Component B (if Step 16.a shows nonzero residual at nHpShc=3)

If Step 16.a's nHpShc=3 case shows a nonzero residual, identify the contributor.

- [ ] Compare the nHpShc=3 / nHp=3 configuration with the Hybrid validation (nHpShc=1, nHp=2) on every other axis from Step 14.d:
  - `have_hrc` (failing has true, Hybrid has false — but Step 11.4 ruled this out independently)
  - `typArrPumPri`
  - `typDis`
  - Pump arrangement
  - Sensor configurations
- [ ] Run a one-toggle probe for each remaining differing axis on the nHpShc=3 / nHp=3 model. The first toggle that closes the residual is Component B.

---

## Step 16.e — Bookkeeping
- [ ] Delete all temporary `AirToWaterShc*` validation files.
- [ ] Restore `Buildings/Templates/Plants/HeatPumps/Validation/package.order`.

---

## Decision Tree at End of Step 16

- **If 16.a yields 0 at nHpShc=3:** Component A alone, ~6 eq/HP on non-SHC branch. Step 16.b/c locates it. Proceed to Step 17 (patch).
- **If 16.a yields nonzero at nHpShc=3:** Components A and B both exist. Step 16.b/c locates A; Step 16.d locates B. Proceed to Step 17 (patch each independently).

---

## Note on Step 15.a's `Internal failure to expand NotImplemented` Errors
Dymola emitted these. They are likely orthogonal to the equation imbalance but should be captured in `findings/16_decomposition.md` so they are not lost. If they reappear during Step 16.a's nHpShc=2/3 probes, record their source — they may be a separate, latent issue with the SHC code path that warrants a follow-up ticket.

---

# AI Agent Investigation Checklist (Phase 2 — Step 17: Localize the Per-HP Defect & Report) [COMPLETED]

## Status
The −30 deficit decomposes per the data points collected so far. The defect is on the `not have_HpShc` controller branch in `Buildings/Templates/Plants/Controls/HeatPumps/AirToWater.mo`. SHC2/SHC3 probes are blocked by an unrelated `NotImplemented` translator error, so the per-HP coefficient must be inferred from the three available data points rather than measured directly.

## Mission of Step 17
Pin the per-HP excess to a specific block on the non-SHC branch using a targeted symbolic search (no further full-template `checkModel` runs), then file a defect report regardless of whether localization succeeds.

## Output Format Requirement
Same as prior steps. Save to `findings/17_per_hp_defect_localization.md` and `findings/18_defect_report.md`.

---

## Step 17.a — Enumerate `[nHpTot]`-Sized Blocks on the Non-SHC Branch

The defect adds equations per HP on this branch. Candidate carriers must have an `nHp`-, `nHpTot`-, or `nSta·nHpTot`-sized internal equation count and must be declared inside `if not have_HpShc`.

- [ ] In `Buildings/Templates/Plants/Controls/HeatPumps/AirToWater.mo`, list every `if not have_HpShc` declaration. From Step 15.b/16.b that is at minimum:
  - `staMat[nSta, nHpTot]` — internal equations: `nSta · nHpTot` = 3·nHpTot
  - `con` (scalar) — 1 equation
  - `booScaRep(nout=nHpTot)` — `nHpTot` equations
  - `pasPumHeaWatPri` — record exact size
- [ ] For each, compute Δequations going from `nHp=3,nHpShc=0` (non-SHC count = 3) to `nHp=2,nHpShc=0` (non-SHC count = 2), i.e. change in `nHpTot` from 3 to 2:
  - `staMat`: 3·3 → 3·2 = 9 → 6 (Δ = −3 per HP)
  - `booScaRep`: 3 → 2 (Δ = −1 per HP)
  - `pasPumHeaWatPri`: ?
- [ ] Sum candidate Δs and compare against the observed Δ = (−30) − (−16) = −14 closure between nHp=3 and nHp=2.

---

## Step 17.b — Compare `staMat` Equation Topology to `ctlPlaHyb.yStaEqu`

- [ ] Open `Buildings/Templates/Plants/Controls/StagingRotation/HybridOperation.mo`. Verify how `yStaEqu` is **computed** internally (not just declared). It is declared `[nSta, nHp]` but with `nHp=nHpTot` in this context.
- [ ] Compare to `staMat.y`. If `staMat` is a CDL constant-matrix source, count its internal equations: typically `nSta · nHpTot` constant assignments.
- [ ] Specifically check whether `staMat` is instantiated **once** or **twice** on the non-SHC branch (e.g. one for cooling, one for heating). The wiring evidence in Step 15.b shows a **single** `staMat` driving both `avaStaHea.staEqu` and `avaStaCoo.staEqu` — confirm this.
- [ ] If `staMat` is single, document its equation count vs the `ctlPlaHyb.yStaEqu` equation count. Any imbalance per HP is a candidate contributor.

---

## Step 17.c — Refine Per-HP Estimate Across Three Data Points

Use the three available data points jointly rather than per-pair to derive the coefficient.

- [ ] Reduce difference data:

  | nHp | nHpShc | non-SHC count | SHC count | Reduced diff |
  |---|---|---|---|---|
  | 3 | 0 | 3 | 0 | −30 |
  | 2 | 0 | 2 | 0 | −16 |
  | 3 | 1 | 2 | 1 | −12 |

- [ ] Fit a model `D = a · nNonShc + b · nShc + c`:
  - Equation 1: 3a + 0b + c = −30
  - Equation 2: 2a + 0b + c = −16
  - Equation 3: 2a + 1b + c = −12
- [ ] Solve:
  - From (1)−(2): a = −14 → **per non-SHC HP defect = −14 equations**
  - From (3)−(2): b = +4 → **per SHC HP, branch contributes +4 equations**
  - From (2): c = −16 − 2·(−14) = +12 → **fixed contributor on non-SHC branch (or at least when nNonShc > 0): +12 equations**
- [ ] Sanity-check (1): 3·(−14) + 0 + 12 = −30 ✓
- [ ] Sanity-check Hybrid case (nHp=2, nHpShc=1, nNonShc=1, nShc=1): D = −14 + 4 + 12 = +2 ≠ 0. **Hybrid validation passes**, so model must include another term that activates at nNonShc ≥ 2 or nHp ≥ 3, OR the +12 constant is not strictly fixed but rather active only when nNonShc > 1.
- [ ] Try alternative model `D = a · nNonShc + b · nShc + c · max(0, nNonShc − 1)`:
  - (1): 3a + 0 + 2c = −30
  - (2): 2a + 0 + c = −16
  - (3): 2a + b + c = −12
  - Hybrid: a + b = 0
  - From Hybrid: b = −a. From (3)−(2): b = +4 → a = −4. Then (2): c = −16 − 2·(−4) = −8. Check (1): 3·(−4) + 2·(−8) = −28 ≠ −30. Close but not exact.
- [ ] Try `D = a · nNonShc · nHp + b · nShc + c`:
  - (1): 9a + 0 + c = −30
  - (2): 4a + 0 + c = −16 → a = −14/5, non-integer, reject.
- [ ] Try `D = a · nNonShc² + b · nNonShc + c · nShc + d`:
  - With Hybrid passing (nNonShc=1, nShc=1, D=0): a + b + c + d = 0.
  - (2): 4a + 2b + d = −16
  - (1): 9a + 3b + d = −30
  - (3): 4a + 2b + c + d = −12
  - From (3)−(2): c = +4. Then Hybrid: a + b + d = −4.
  - From (1)−(2): 5a + b = −14. Combine with a + b + d = −4 ⇒ 4a − d = −10. With (2): 4a + 2b + d = −16 ⇒ 4a + 2b = −16 − d.
  - System has multiple solutions. The simplest with integer coefficients: a = −2, b = −4, c = +4, d = −2. Check Hybrid: −2 −4 +4 −2 = −4 ≠ 0. Reject.
- [ ] Without a fourth data point, **the functional form cannot be uniquely identified**. The most parsimonious fits are:
  - **Linear in nNonShc with offset:** −14 per non-SHC HP, +12 fixed (Hybrid would predict +2; but Hybrid actually passes — this fit is inconsistent).
  - **The defect is non-linear** in nNonShc, possibly involving combinations like `nNonShc · (nNonShc − 1)` or specific edge cases at nNonShc = 0.
- [ ] **Conclusion:** the defect functional form is not pinnable with the available data. The localization in Step 17.a/b must proceed by structural inspection rather than by arithmetic fitting.

---

## Step 17.d — Final Source Inspection

- [ ] In `Buildings/Templates/Plants/Controls/HeatPumps/AirToWater.mo`, perform an exhaustive listing:
  - Every declaration with the conditional `if not have_HpShc` (regardless of dimension).
  - Every declaration with the conditional `if have_HpShc`.
  - Every declaration of an array sized by `nHp`, `nHpTot`, or any expression containing those.
- [ ] For each, compute the equation contribution at:
  - (nHp=3, nHpShc=0)
  - (nHp=2, nHpShc=0)
  - (nHp=3, nHpShc=1)
  - (nHp=2, nHpShc=1) (Hybrid)
- [ ] Build a side-by-side equation-count table. The defect candidate is the row whose contributions match the observed deficits.
- [ ] If a unique candidate emerges, propose a one-line patch (typically: tighten or correct an `if not have_HpShc` guard, or add a fallback `connect()`).

---

## Step 17.e — File Defect Report

Stop further probing whether or not Step 17.a–d localizes the exact block. The diagnosis is already actionable enough to file.

### Defect Report Template (write into `findings/18_defect_report.md`)

```
**Title:** Buildings.Templates.Plants.HeatPumps.Validation.AirToWater not well-posed (−30 equations) on branch issue4304_HybridAirSourceHeatPumpPlantControls_April2026

**Environment**
- Buildings library: 13.0.0, branch issue4304_HybridAirSourceHeatPumpPlantControls_April2026, commit 18d6e62
- MSL: 4.1.0
- Tool: Dymola 2025x

**Reproducer**
checkModel("Buildings.Templates.Plants.HeatPumps.Validation.AirToWater")

**Symptom**
- 18551 unknowns vs 18581 equations
- Error: model is not well-posed
- "difference could be reduced to −30"

**Diagnosis**
Defect is in the `not have_HpShc` branch of
Buildings/Templates/Plants/Controls/HeatPumps/AirToWater.mo

Empirical decomposition (3 data points):

| nHp | nHpShc | Reduced diff |
|---|---|---|
| 3 | 0 | −30 |
| 2 | 0 | −16 |
| 3 | 1 | −12 |
| 2 | 1 (Hybrid validation) | 0 (passes) |

The reduced difference scales with the number of non-SHC heat pumps, but
not linearly. The Hybrid validation (nHpShc=1, nHp=2) passes; the
default AirToWater validation (nHpShc=0, nHp=3) fails. The defect is
exposed only by configurations with nHpShc=0 or nHp ≥ 3.

**Eliminated as causes**
- have_hrc / HRC integration (Step 11.4: HRC disable did not change −30)
- or1/andHeaEna/notCooMod cross-mode wiring (Step 13.5: confirmed structurally safe)
- yStaEqu vs staMat dimension contract (Step 16.c: dimension-consistent)
- Top-level fallback omission for or1.u2/or2.u1 (Step 16.b: fallback present)
- All component-level validations (Step 11.3: pass)

**Companion translator issue**
Independent of the −30 imbalance, configurations with nHpShc ≥ 2
trigger Dymola "Internal failure to expand NotImplemented" errors in
pla.ctl.ctl.chaStaHea.* and pla.ctl.ctl.chaStaCoo.* (Greater.mo / Less.mo).
This blocks completing the empirical decomposition. May be a separate
defect in the staging-comparison logic for nHpShc ≥ 2.

**Suggested next-step