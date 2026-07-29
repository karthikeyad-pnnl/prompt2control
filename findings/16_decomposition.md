## Step 16.a Findings
- File(s) inspected:
  - c:/buildings_library/modelica-buildings/Buildings/Templates/Plants/HeatPumps/Validation/AirToWater.mo
  - c:/buildings_library/modelica-buildings/Buildings/Templates/Plants/HeatPumps/Validation/AirToWaterShc2.mo (temporary, deleted at end of step)
  - c:/buildings_library/modelica-buildings/Buildings/Templates/Plants/HeatPumps/Validation/AirToWaterShc3.mo (temporary, deleted at end of step)
  - c:/buildings_library/modelica-buildings/Buildings/Templates/Plants/HeatPumps/Validation/package.order (temporarily edited, restored)
  - c:/git_repos/prompt2control/logs/16a_shc2_run/dymola_model_check.log
  - c:/git_repos/prompt2control/logs/16a_shc3_run/dymola_model_check.log
  - c:/git_repos/prompt2control/logs/16a_shc2.log
  - c:/git_repos/prompt2control/logs/16a_shc3.log
- Key observations:
  - Implemented temporary SHC probes exactly on the requested axis:
    - AirToWaterShc2: `cfg(nHpShc=2)` with `staEqu*` resized to 3x5.
    - AirToWaterShc3: `cfg(nHpShc=3)` with `staEqu*` resized to 3x6.
  - Initial attempt to override `pla.ctl.staEqu*` directly failed because those are final/not visible through the wrapper (`HybridAirToWater`), so the probe was switched to legal overrides via `datAll(pla(ctl(...)))`.
  - Both legal SHC2 and SHC3 runs abort during model instantiation before unknown/equation counting:
    - Dymola reports translator limitation on conditional components with fixed conditions.
    - Repeated `Internal failure to expand NotImplemented` appears in `pla.ctl.ctl.chaStaHea.*` and `pla.ctl.ctl.chaStaCoo.*` (`Greater.mo` / `Less.mo`).
  - Because checkModel aborts prior to balance counting, no reduced-difference value is emitted for SHC2/SHC3.
- Hypotheses generated/refuted:
  - Generated: SHC2/SHC3 paths trigger a translator/expansion limitation in Dymola 2025x that blocks Step 16.a quantitative decomposition.
  - Refuted: a simple syntax/modifier error in the final probe models (final legal variants compile far enough to invoke the translator limitation).
  - Carried forward: SHC axis remains significant from Step 15 (`-30` to `-12` at nHpShc=1), but Step 16.a cannot complete with current translator behavior.
- Artifacts produced:
  - c:/git_repos/prompt2control/logs/16a_shc2_run/model_check.mos
  - c:/git_repos/prompt2control/logs/16a_shc2_run/dymola_model_check.log
  - c:/git_repos/prompt2control/logs/16a_shc3_run/model_check.mos
  - c:/git_repos/prompt2control/logs/16a_shc3_run/dymola_model_check.log
  - c:/git_repos/prompt2control/logs/16a_shc2.log
  - c:/git_repos/prompt2control/logs/16a_shc3.log

### Step 16.a Table

| nHp | nHpShc | non-SHC count | Reduced diff | Notes |
|---|---|---|---|---|
| 3 | 0 | 3 | -30 | Baseline (previous steps) |
| 3 | 1 | 2 | -12 | Step 15.a result |
| 3 | 2 | 1 | N/A (aborted) | Translator `NotImplemented` before balance counting |
| 3 | 3 | 0 | N/A (aborted) | Translator `NotImplemented` before balance counting |

## Step 16.b Findings
- File(s) inspected:
  - c:/buildings_library/modelica-buildings/Buildings/Templates/Plants/Controls/HeatPumps/AirToWater.mo
- Key observations:
  - SHC branch (`have_HpShc=true`) declaration set:
    - `ctlPlaHyb` at line ~1715 (hybrid controller block).
    - `or6`/`or7` at lines ~1708/~1712 (primary pump signal combines).
    - SHC-only I/O and slices (`u1HpShc_actual`, `y1HpShc`, `y1Pum*Shc`, `yMod`, SHC temp outputs) around lines ~1748-1801.
  - Non-SHC branch (`not have_HpShc`) declaration set:
    - `staMat[nSta,nHpTot]` at ~1725.
    - `con(k=false)` at ~1728.
    - `booScaRep(nout=nHpTot)` at ~1731.
    - `pasPumHeaWatPri` at ~1793.
  - Branch wiring pairs for key downstream consumers exist and are symmetric in intent:
    - Availability to `or1.u2`/`or2.u1`: `ctlPlaHyb.yAvaHpShc*` vs `booScaRep.y`.
    - Stage matrix to `avaStaHea.staEqu`/`avaStaCoo.staEqu`: `ctlPlaHyb.yStaEqu` vs `staMat.y`.
    - HW primary pump enable to `ctlPumPri.u1PumHeaWatPri`: `or3.y` vs `pasPumHeaWatPri.y`.
  - No additional obvious unpaired `if have_HpShc`/`if not have_HpShc` branch was found in this section.
- Hypotheses generated/refuted:
  - Refuted: a trivial missing fallback branch in non-SHC path.
  - Generated: residual contribution likely comes from deeper branch behavior inside SHC-related block internals (or translator behavior) rather than top-level connect omission.
- Artifacts produced:
  - This report section and extracted line anchors from `AirToWater.mo`.

### Step 16.b Branch Contribution Snapshot

| Block | Branch active when | Equations contributed (qualitative) | Counterpart in other branch | Counterpart contributions |
|---|---|---|---|---|
| `ctlPlaHyb` | `have_HpShc` | HybridOperation internal equations over `nHpTot` | `staMat` + `con` + `booScaRep` | Constant/mapping equations over `nSta*nHpTot` and `nHpTot` |
| `or3` | `have_HpShc` | Combines CHW+HW primary pump enables | `pasPumHeaWatPri` | Pass-through enable path when no SHC |
| `or6`/`or7` | `have_HpShc` | Additional SHC pump combining logic | none (not needed) | SHC-only logic by design |
| SHC I/O slices | `have_HpShc` | Extra SHC-only command/status equations | none (not needed) | SHC-only interface by design |

## Step 16.c Findings
- File(s) inspected:
  - c:/buildings_library/modelica-buildings/Buildings/Templates/Plants/Controls/StagingRotation/HybridOperation.mo
  - c:/buildings_library/modelica-buildings/Buildings/Templates/Plants/Controls/StagingRotation/StageAvailability.mo
  - c:/buildings_library/modelica-buildings/Buildings/Templates/Plants/Controls/HeatPumps/AirToWater.mo
- Key observations:
  - In `HybridOperation.mo`, `yStaEqu` is declared as `yStaEqu[nSta,nHp]` (line ~123).
  - In controller instantiation, `ctlPlaHyb` is passed `final nHp=nHpTot` (line ~1719 in `AirToWater.mo`).
  - Therefore, in this controller context, `ctlPlaHyb.yStaEqu` resolves to `[nSta,nHpTot]`.
  - `StageAvailability.staEqu` expects `[nSta,nEqu]` with `nEqu` bound to `nHpTot` in both `avaStaHea` and `avaStaCoo` declarations.
  - Both connects are dimension-consistent:
    - `connect(ctlPlaHyb.yStaEqu, avaStaHea.staEqu)`
    - `connect(ctlPlaHyb.yStaEqu, avaStaCoo.staEqu)`
    - `connect(staMat.y, avaStaHea.staEqu)`
    - `connect(staMat.y, avaStaCoo.staEqu)`
- Hypotheses generated/refuted:
  - Refuted: a direct `yStaEqu` size mismatch (`nHp` vs `nHpTot`) at the connect boundary.
  - Generated: if equation imbalance persists, cause is not this interface size contract.
- Artifacts produced:
  - This report section.

## Step 16.d Findings
- File(s) inspected:
  - c:/git_repos/prompt2control/logs/16a_shc2.log
  - c:/git_repos/prompt2control/logs/16a_shc3.log
  - c:/git_repos/prompt2control/findings/14_diff_vs_hybrid.md
  - c:/git_repos/prompt2control/findings/15_nhpshc_axis.md
- Key observations:
  - Step 16.d depends on obtaining residual at `nHpShc=3` to determine whether Component B exists.
  - `nHpShc=3` run did not produce reduced difference due translator abort (`NotImplemented`).
  - Therefore Component B cannot be isolated by the planned decision tree in this run.
- Hypotheses generated/refuted:
  - Generated: Step 16.d is blocked by toolchain behavior rather than missing probe setup.
  - Not refuted/confirmed: existence and magnitude of Component B.
- Artifacts produced:
  - None beyond Step 16.a logs.

## Step 16.e Findings
- File(s) inspected:
  - c:/buildings_library/modelica-buildings/Buildings/Templates/Plants/HeatPumps/Validation/package.order
- Key observations:
  - Temporary files removed:
    - `AirToWaterShc2.mo`
    - `AirToWaterShc3.mo`
  - `package.order` restored to:
    - `AirToWater`
    - `HybridAirToWater`
    - `UserProject`
- Hypotheses generated/refuted:
  - N/A.
- Artifacts produced:
  - Clean repository state for validation package definitions.

## Step 16 Outcome Summary
- Step 16.a quantitative decomposition is blocked: SHC2/SHC3 checks abort before unknown/equation and reduced-difference reporting.
- Step 16.b/c static audits completed:
  - No missing SHC/non-SHC top-level fallback was found.
  - `ctlPlaHyb.yStaEqu` vs `staMat` dimension contract into `StageAvailability` is consistent.
- `Internal failure to expand NotImplemented` has been captured and preserved as requested.
