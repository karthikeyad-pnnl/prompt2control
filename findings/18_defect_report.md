**Title:** Buildings.Templates.Plants.HeatPumps.Validation.AirToWater not well-posed (-30 equations) on branch issue4304_HybridAirSourceHeatPumpPlantControls_April2026

**Environment**
- Buildings library: 13.0.0, branch issue4304_HybridAirSourceHeatPumpPlantControls_April2026, commit 18d6e62
- MSL: 4.1.0
- Tool: Dymola 2025x

**Reproducer**
- checkModel("Buildings.Templates.Plants.HeatPumps.Validation.AirToWater")

**Symptom**
- Baseline reports not well-posed with reduced difference -30.
- Prior logs recorded 18551 unknowns and 18581 equations before reduction.

**Diagnosis**
Defect scope is localized to branch-dependent behavior in:
- Buildings/Templates/Plants/Controls/HeatPumps/AirToWater.mo

Most likely defective path:
- not have_HpShc branch (cfg.nHpShc=0 in failing validation), interacting with always-active nHpTot-sized logic.

Empirical decomposition points available:

| nHp | nHpShc | Reduced diff |
|---|---|---:|
| 3 | 0 | -30 |
| 2 | 0 | -16 |
| 3 | 1 | -12 |
| 2 | 1 (Hybrid validation) | 0 (passes) |

Interpretation:
- Residual scales strongly with non-SHC cardinality changes, but simple linear decomposition is inconsistent with the Hybrid pass case.
- Static source audit eliminates simple top-level missing fallback or direct dimensional mismatch on the known or1/or2 and stage-matrix paths.
- Remaining candidate is branch-dependent topology/internal equation composition rather than obvious single connect omission.

**Eliminated as causes**
- have_hrc / HRC integration axis (HRC-disable probe did not change -30).
- Simple cross-mode wiring omission on previously flagged pins (or1/andHeaEna/notCooMod): structural fallbacks verified in source audit.
- Direct yStaEqu vs staMat size contract mismatch into StageAvailability: dimensions are consistent in controller context.
- Missing non-SHC fallback for or1.u2/or2.u1: fallback exists via booScaRep.
- Component-level sub-block balance regressions (prior isolated checks reported balanced).

**Companion translator issue**
Independent of the -30 imbalance, SHC2/SHC3 probe runs (nHpShc>=2) abort before balance counting with:
- Internal failure to expand NotImplemented
- References include pla.ctl.ctl.chaStaHea.* and pla.ctl.ctl.chaStaCoo.* (Greater.mo / Less.mo)

This blocks completing the intended Step 16 empirical decomposition and should be tracked as a separate toolchain/model interaction defect.

**Suggested next-step patch strategy**
1. Add a temporary minimal reproducer at controller level only (AirToWater control block harness) with nHp sweep and nHpShc in {0,1}, avoiding full plant wrappers.
2. Instrument branch-equation deltas by selectively toggling the non-SHC declarations:
   - staMat, booScaRep, pasPumHeaWatPri, and related downstream stage/pump links.
3. Apply a minimal guard/connect patch where branch asymmetry is confirmed, then re-run full validation checkModel.
4. Run a separate issue workflow for the NotImplemented translator abort to unblock SHC2/SHC3 measurements.

**Attachments / Evidence**
- findings/15_nhpshc_axis.md
- findings/16_decomposition.md
- findings/17_per_hp_defect_localization.md
- logs/15a_shc_axis.log
- logs/16a_shc2.log
- logs/16a_shc3.log
