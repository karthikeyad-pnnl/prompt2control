## Step 13.5 Findings
- File(s) inspected:
  - c:/buildings_library/modelica-buildings/Buildings/Templates/Plants/Controls/HeatPumps/AirToWater.mo
  - c:/buildings_library/modelica-buildings/Buildings/Templates/Plants/Controls/StagingRotation/EquipmentAvailability.mo
  - c:/buildings_library/modelica-buildings/Buildings/Templates/Plants/HeatPumps/Validation/AirToWater.mo
  - c:/buildings_library/modelica-buildings/Buildings/Templates/Plants/HeatPumps/Components/Controls/HybridAirToWater.mo
- Key observations:
  - In the failing validation model, `nHp=3` and `cfg(nHpShc=0)` are set in `Validation/AirToWater.mo`, which yields `nHpTot=nHp+nHpShc=3` and `have_HpShc=false` in controller `Controls/HeatPumps/AirToWater.mo`.
  - `ctlPlaHyb` is conditionally declared `if have_HpShc` while `booScaRep` is conditionally declared `if not have_HpShc`, making them declaration-level mutually exclusive.
  - `y1HeaPre` is declared `if have_heaWat and have_chiWat`; therefore in the heating-only probe (`have_chiWat=false`) this source is absent and both connects from `y1HeaPre.y` are dropped.
  - `avaEquHeaCoo` itself is always declared, but its source pin `y1Coo` is conditional inside `StagingRotation/EquipmentAvailability.mo` (`if have_chiWat`), so `connect(avaEquHeaCoo.y1Coo, or1.u1)` drops in heating-only.
  - All six target connects in Step 13.5.b are in the main `equation` section (not inside an enclosing `if` block or loop). The only nearby `if have_HpShc then ... end if;` block is empty.
  - `HybridAirToWater` wrapper instantiates the same controller class: `Buildings.Templates.Plants.Controls.HeatPumps.AirToWater ctl(...)`.
- Hypotheses generated/refuted:
  - Refuted: simultaneous active over-connection on `or1.u2` from both `ctlPlaHyb` and `booScaRep` in the failing config.
  - Confirmed: heating-only disconnects are explained by conditional source disappearance (`y1HeaPre` and `avaEquHeaCoo.y1Coo`) and Modelica conditional-connect dropping.
  - Generated: the remaining full-model deficit likely requires additional contributors beyond this `or1/andHeaEna/notCooMod` cluster (because this cluster behavior is now structurally explained).
- Artifacts produced:
  - This report: `findings/13_5_source_block_audit.md`
  - Extracted declaration/connect evidence with line references captured below.

### Step 13.5.a - Source Block Declaration Audit

| Block | Type | Conditional guard on declaration | Active in failing config? | Active in heating-only probe? |
|---|---|---|---|---|
| avaEquHeaCoo | `StagingRotation.EquipmentAvailability avaEquHeaCoo[nHpTot]` | none on declaration (`AirToWater.mo`:1433) | Yes | Yes (component exists), but `y1Coo` pin is conditional inside block |
| ctlPlaHyb | `StagingRotation.HybridOperation ctlPlaHyb(...)` | `if have_HpShc` (`AirToWater.mo`:1715) | No (`nHpShc=0 => have_HpShc=false`) | No |
| booScaRep | `Buildings.Controls.OBC.CDL.Routing.BooleanScalarReplicator booScaRep(nout=nHpTot)` | `if not have_HpShc` (`AirToWater.mo`:1731) | Yes | Yes |
| y1HeaPre | `Buildings.Controls.OBC.CDL.Logical.Pre y1HeaPre[nHpTot]` | `if have_heaWat and have_chiWat` (`AirToWater.mo`:1439-1440) | Yes (`have_heaWat=true`, `have_chiWat=true`) | No (`have_chiWat=false`) |
| y1HpPre | `Buildings.Controls.OBC.CDL.Logical.Pre y1HpPre[nHpTot]` | none (`AirToWater.mo`:1546) | Yes | Yes |

Resolution basis for failing config:
- `Validation/AirToWater.mo`: `have_chiWat=true` (parameter default at line 8), `have_hrc_select=true` (line 42), `cfg(nHpShc=0)` (line 43), `nHp=3` (line 50).
- `Controls/HeatPumps/AirToWater.mo`: `have_hrc=if have_heaWat and have_chiWat then have_hrc_select else false` (line 26), `nHpTot=nHp+nHpShc` (line 182), `have_HpShc=nHpShc>0` (line 186).

Acceptance test result:
- Not confirmed for over-connection hypothesis. `ctlPlaHyb` and `booScaRep` are mutually exclusive by declaration guard; both are not active simultaneously in the failing config.

### Step 13.5.b - Connect Guard Re-Inspection

| Connect statement | Line | Enclosing block classification |
|---|---:|---|
| `connect(avaEquHeaCoo.y1Coo, or1.u1)` | `AirToWater.mo`:2203 | Main `equation` section; unguarded connect |
| `connect(ctlPlaHyb.yAvaHpShcCoo, or1.u2)` | `AirToWater.mo`:2232 | Main `equation` section; unguarded connect |
| `connect(booScaRep.y, or1.u2)` | `AirToWater.mo`:2271 | Main `equation` section; unguarded connect |
| `connect(y1HpPre.y, andHeaEna.u1)` | `AirToWater.mo`:2273 | Main `equation` section; unguarded connect |
| `connect(y1HeaPre.y, andHeaEna.u2)` | `AirToWater.mo`:2277 | Main `equation` section; unguarded connect |
| `connect(y1HeaPre.y, notCooMod.u)` | `AirToWater.mo`:2281 | Main `equation` section; unguarded connect |

Notes:
- No enclosing `if` equation block around these connects.
- Nearby `if have_HpShc then ... end if;` is empty (`AirToWater.mo`:2252-2253).

### Step 13.5.c - Conditional-Connect Dropping Semantics Cross-Check

| Pair | Source A guard | Source B guard | Mutually exclusive? | Both active in failing config? |
|---|---|---|---|---|
| (`ctlPlaHyb`, `booScaRep`) into `or1.u2` | `ctlPlaHyb if have_HpShc` | `booScaRep if not have_HpShc` | Yes | No |

Conclusion:
- The `or1.u2` dual-connect pattern is structurally safe under Modelica conditional component semantics in this configuration.

### Step 13.5.d - Track the Heating-Only Disconnect

1. `or1.u1 <- avaEquHeaCoo.y1Coo`
   - `avaEquHeaCoo` declaration: unconditional (`AirToWater.mo`:1433).
   - Inside `EquipmentAvailability`, `y1Coo` is conditional `if have_chiWat` (`EquipmentAvailability.mo`:27-28).
   - In heating-only (`have_chiWat=false`), source pin `y1Coo` is absent, so `connect(avaEquHeaCoo.y1Coo, or1.u1)` drops.

2. `andHeaEna.u2 <- y1HeaPre.y`
   - `y1HeaPre` declaration is conditional `if have_heaWat and have_chiWat` (`AirToWater.mo`:1439-1440).
   - In heating-only (`have_chiWat=false`), `y1HeaPre` absent, so `connect(y1HeaPre.y, andHeaEna.u2)` drops.

3. `notCooMod.u <- y1HeaPre.y`
   - Same source and same conditional absence as above.
   - In heating-only, `connect(y1HeaPre.y, notCooMod.u)` drops.

This exactly explains the reported heating-only unconnected pins localized by Dymola.

### Step 13.5.e - Per-HP Arithmetic Reconciliation

- Controller parameter resolution in failing config:
  - `nHp=3`, `nHpShc=0` (`Validation/AirToWater.mo`:43,50)
  - `nHpTot=nHp+nHpShc=3` (`Controls/HeatPumps/AirToWater.mo`:182)
- Because the `or1.u2` over-connection hypothesis is refuted, no equation surplus from simultaneous `ctlPlaHyb` and `booScaRep` applies in this config.
- Heating-only disconnect mechanism remains valid and accounts for the heating-only localization, but this alone is insufficient to explain full-model `-30`.
- Ranked remaining contributors (highest first):
  1. Additional conditional source/target pin disappearance in other controller branches not yet partitioned.
  2. Plant-template/wrapper-level connections becoming inactive under specific `cfg` paths while downstream pins remain active.
  3. Potential duplicated equations in other arrays not in the `or1/andHeaEna/notCooMod` cluster.

### Step 13.5.f - Compare Same Code Block in HybridAirToWater Validation Path

- Verified: `Buildings/Templates/Plants/HeatPumps/Components/Controls/HybridAirToWater.mo` instantiates
  `Buildings.Templates.Plants.Controls.HeatPumps.AirToWater ctl(...)` at line 30.
- Therefore, the same controller class is used in the hybrid wrapper path.

## Updated Root Cause Report

1. The suspected primary defect from Step 13.5 kickoff (simultaneous dual connect to `or1.u2`) is not present in the failing validation configuration.
2. `ctlPlaHyb` vs `booScaRep` are declaration-level mutually exclusive via `have_HpShc` and `not have_HpShc`; with `nHpShc=0`, only `booScaRep` is active.
3. The heating-only localized disconnects are real and explained by conditional source absence:
   - `y1HeaPre` absent when `have_chiWat=false`.
   - `avaEquHeaCoo.y1Coo` absent when `have_chiWat=false` due to conditional output declaration in `EquipmentAvailability`.
4. This explains heating-only localization behavior but does not fully account for full-model `-30`; additional contributors remain to be found.

## Proposed Fix

1. Do not patch `or1.u2` dual-connect logic at this stage; current evidence indicates it is correct under conditional-component semantics.
2. Proceed to Step 14 diff and/or Step 16 re-audit to locate remaining contributors, prioritizing:
   - conditional output pins feeding always-active logic arrays,
   - wrapper/plant-level connect differences between failing `AirToWater` and passing `HybridAirToWater` paths,
   - any arrayed connections where one side can be conditionally absent without a paired fallback.