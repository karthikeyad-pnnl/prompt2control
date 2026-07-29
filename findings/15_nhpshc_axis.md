## Step 15.a Findings
- File(s) inspected: 
  - c:/buildings_library/modelica-buildings/Buildings/Templates/Plants/HeatPumps/Validation/AirToWater.mo
  - c:/buildings_library/modelica-buildings/Buildings/Templates/Plants/HeatPumps/Validation/AirToWaterShc.mo (temporary)
  - c:/buildings_library/modelica-buildings/Buildings/Templates/Plants/HeatPumps/Validation/package.order
  - c:/git_repos/prompt2control/logs/15a_shc_axis.log
- Key observations:
  - Temporary model `Buildings.Templates.Plants.HeatPumps.Validation.AirToWaterShc` was created as `extends AirToWater(...)` with:
    - `pla(cfg(nHpShc=1))`
    - `staEqu`, `staEquSinMod`, `staEquDouMod` overridden to 3x4 matrices (`nHp=3`, `nHpTot=4`).
  - `checkModel` result for the temporary SHC variant:
    - The model has the same number of unknowns and equations: `20163`.
    - Dymola reports: `Error: The model is not well-posed.`
    - Reduced difference: `-12` (`Using the given settings of the parameters, the difference could be reduced to -12`).
  - Compared to baseline full model (`-30`), toggling `nHpShc` from `0` to `1` improves by `+18` but does not close to zero.
  - Dymola also reports repeated `Error: Internal failure to expand  NotImplemented` in this run.
- Hypotheses generated/refuted:
  - Confirmed (partial): the `nHpShc` / `have_HpShc` axis is materially involved in the equation imbalance.
  - Refuted (strict Step 15.a expectation): this axis alone does not fully resolve the defect in one toggle (residual is still `-12`).
  - Generated: at least one additional contributor remains outside the single `nHpShc` toggle path.
- Artifacts produced:
  - c:/git_repos/prompt2control/logs/15a_shc_axis.log
  - c:/git_repos/prompt2control/findings/15_codegen_AirToWater.md
  - c:/git_repos/prompt2control/findings/15_codegen_HybridOperation.md
  - c:/git_repos/prompt2control/findings/15_codegen_BooleanScalarReplicator.md
  - c:/git_repos/prompt2control/findings/15_extends_AirToWater.md
  - c:/git_repos/prompt2control/findings/15_extends_HybridOperation.md
  - c:/git_repos/prompt2control/findings/15_extends_BooleanScalarReplicator.md

## Step 15.b Findings
- File(s) inspected:
  - c:/buildings_library/modelica-buildings/Buildings/Templates/Plants/Controls/HeatPumps/AirToWater.mo
  - c:/git_repos/prompt2control/findings/15_codegen_AirToWater.md
  - c:/git_repos/prompt2control/findings/15_extends_AirToWater.md
- Key observations:
  - Core axis definitions:
    - `nHpShc` at line 177
    - `nHpTot=nHp+nHpShc` at line 182
    - `have_HpShc=nHpShc>0` at line 186
  - Major `have_HpShc` gated declarations:
    - `ctlPlaHyb` (HybridOperation) at lines 1715-1723: active when `have_HpShc=true`
    - `staMat`, `con`, `booScaRep` at lines 1726-1732: active when `not have_HpShc`
    - `or6`, `or7`, `or3` and SHC I/O (`u1HpShc_actual`, `y1HpShc`, `yMod`, SHC pump status/commands, SHC temperature outputs): active when `have_HpShc=true`
    - `pasPumHeaWatPri` pass-through: active when `not have_HpShc`
    - `ctlFloMin` is explicitly disabled when SHC exists (`if is_priOnl and not have_HpShc`, line 1687)
  - Major `have_HpShc`/`not have_HpShc` connect branches and branch roles:
    - Hybrid source branch (`have_HpShc=true`) routes `ctlPlaHyb` outputs into:
      - `or1.u2` via `ctlPlaHyb.yAvaHpShcCoo` (line 2232)
      - `or2.u1` via `ctlPlaHyb.yAvaHpShcHea` (line 2234)
      - staging/order/mode downstream (`yStaEqu`, `yIdxSta`, `yHeaCoo`, `yMod`, SHC slices)
    - Non-SHC fallback (`have_HpShc=false`) routes:
      - `booScaRep.y -> or2.u1` (line 2269)
      - `booScaRep.y -> or1.u2` (line 2271)
      - `staMat.y` drives staging matrices for both heating and cooling (`avaStaHea.staEqu`, `avaStaCoo.staEqu`)
  - Pairing check (`if have_HpShc` vs `if not have_HpShc`):
    - Well-paired for availability injection into `or1/or2` (`ctlPlaHyb` vs `booScaRep`).
    - Well-paired for staging matrix source (`ctlPlaHyb.yStaEqu` vs `staMat.y`).
    - Well-paired for HW primary pump enable path (`or3` branch vs `pasPumHeaWatPri` branch).
    - Not strictly symmetric but intentional: SHC-only external ports and SHC-only primary-pump combine blocks (`or6/or7`) have no non-SHC counterpart because these signals/components do not exist without SHC units.
- Hypotheses generated/refuted:
  - Refuted: a simple missing non-SHC fallback for `or1.u2`/`or2.u1` (fallback exists and is explicitly wired).
  - Refuted: obvious missing counterpart for key SHC/non-SHC availability/staging branches.
  - Generated: residual `-12` likely comes from deeper cardinality or downstream composition interactions, not from absent top-level branch pairing.
- Artifacts produced:
  - c:/git_repos/prompt2control/findings/15_codegen_AirToWater.md
  - c:/git_repos/prompt2control/findings/15_extends_AirToWater.md

### Step 15.b Master Table (selected high-impact rows)

| Line | Construct | Activates when | What it adds (equations / connects) |
|---|---|---|---|
| 177 | parameter `nHpShc` | both | SHC axis cardinality input |
| 182 | `nHpTot=nHp+nHpShc` | both | Drives array sizes for many equations |
| 186 | `have_HpShc=nHpShc>0` | both | Branch selector for SHC logic |
| 1687 | `ctlFloMin ... if is_priOnl and not have_HpShc` | `not have_HpShc` | Primary-only minimum-flow controller equations |
| 1708 | `or6[nPumHeaWatPriTot] if have_HpShc` | `have_HpShc` | Additional OR equations for SHC HW primary pump combines |
| 1712 | `or7[nPumChiWatPriTot] if have_HpShc` | `have_HpShc` | Additional OR equations for SHC CHW primary pump combines |
| 1715-1723 | declaration `ctlPlaHyb` | `have_HpShc` | HybridOperation block equations |
| 1726 | declaration `staMat[nSta,nHpTot]` | `not have_HpShc` | Constant staging matrix equations |
| 1729 | declaration `con(k=false)` | `not have_HpShc` | Scalar constant equation |
| 1731-1732 | declaration `booScaRep(nout=nHpTot)` | `not have_HpShc` | Replicated Boolean fallback equations |
| 2232 | `connect(ctlPlaHyb.yAvaHpShcCoo, or1.u2)` | `have_HpShc` | SHC availability source to cooling availability OR |
| 2234 | `connect(ctlPlaHyb.yAvaHpShcHea, or2.u1)` | `have_HpShc` | SHC availability source to heating availability OR |
| 2269 | `connect(booScaRep.y, or2.u1)` | `not have_HpShc` | Non-SHC fallback to heating availability OR |
| 2271 | `connect(booScaRep.y, or1.u2)` | `not have_HpShc` | Non-SHC fallback to cooling availability OR |
| 2349 | `connect(ctlPlaHyb.yMod[(nHp+1):(nHp+nHpShc)], yMod)` | `have_HpShc` | SHC mode vector export |
| 2351-2353 | `connect(or6[...]`, `connect(or7[...])` | `have_HpShc` | SHC pump command slices |

## Step 15.c Findings
- File(s) inspected:
  - c:/buildings_library/modelica-buildings/Buildings/Templates/Plants/Controls/StagingRotation/HybridOperation.mo
  - c:/buildings_library/modelica-buildings/Buildings/Controls/OBC/CDL/Routing/BooleanScalarReplicator.mo
  - c:/buildings_library/modelica-buildings/Buildings/Templates/Plants/Controls/HeatPumps/AirToWater.mo
  - c:/git_repos/prompt2control/findings/15_codegen_HybridOperation.md
  - c:/git_repos/prompt2control/findings/15_codegen_BooleanScalarReplicator.md
  - c:/git_repos/prompt2control/findings/15_extends_HybridOperation.md
  - c:/git_repos/prompt2control/findings/15_extends_BooleanScalarReplicator.md
- Key observations:
  - `HybridOperation` relevant outputs (type and cardinality):
    - `yAvaHpShcHea[nHp]` (Boolean vector)
    - `yAvaHpShcCoo[nHp]` (Boolean vector)
    - `y1PumPri[nHp]` (Boolean vector)
    - `yHeaCoo` (Boolean scalar)
    - `yMod[nHp]` (Integer vector)
    - `yStaEqu[nSta,nHp]` (Real matrix)
    - `yIdxSta[nEquAlt]` (Integer vector, conditional on `not have_sorRunTim`)
  - `BooleanScalarReplicator` outputs:
    - `y[nout]`, where `nout` is parameterized (here `nout=nHpTot`).
  - In controller wiring, fallback pairs for availability signals are cardinality-aligned:
    - `or1.u2` receives `ctlPlaHyb.yAvaHpShcCoo` in SHC branch and `booScaRep.y` in non-SHC branch.
    - `or2.u1` receives `ctlPlaHyb.yAvaHpShcHea` in SHC branch and `booScaRep.y` in non-SHC branch.
    - Both branch sources are vectors of size `nHpTot` in this controller instantiation.
- Hypotheses generated/refuted:
  - Refuted: direct output-size mismatch between `HybridOperation` and `BooleanScalarReplicator` for `or1.u2`/`or2.u1` fallback pair.
  - Generated: if a mismatch persists, it is more likely due to downstream branch composition (e.g., extra gated blocks and pump/staging logic interactions) than these two source block interfaces.
- Artifacts produced:
  - c:/git_repos/prompt2control/findings/15_codegen_HybridOperation.md
  - c:/git_repos/prompt2control/findings/15_codegen_BooleanScalarReplicator.md
  - c:/git_repos/prompt2control/findings/15_extends_HybridOperation.md
  - c:/git_repos/prompt2control/findings/15_extends_BooleanScalarReplicator.md

### Step 15.c Source-Comparison Table

| Downstream pin | Source when have_HpShc=true | Source when have_HpShc=false | Equation count match? |
|---|---|---|---|
| `or1.u2` | `ctlPlaHyb.yAvaHpShcCoo` (`HybridOperation`, vector `[nHpTot]`) | `booScaRep.y` (`BooleanScalarReplicator`, vector `[nHpTot]`) | Yes |
| `or2.u1` | `ctlPlaHyb.yAvaHpShcHea` (`HybridOperation`, vector `[nHpTot]`) | `booScaRep.y` (`BooleanScalarReplicator`, vector `[nHpTot]`) | Yes |

## Step 15 Summary
- One-toggle SHC probe reduced the residual from `-30` to `-12`, so the SHC axis is a significant contributor.
- The result did not reach `0`; Step 15.a strict success criterion is not met.
- Branch enumeration and source-cardinality audit did not reveal a simple missing fallback or direct `HybridOperation` vs `BooleanScalarReplicator` output-size mismatch on the `or1/or2` availability paths.
- Next investigation should target the remaining `-12` contributor in SHC-related downstream composition (pump/staging combination paths and associated conditionals).