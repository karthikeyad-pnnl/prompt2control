## Step 15 Findings
- File(s) inspected:
  - c:/buildings_library/modelica-buildings/Buildings/Templates/Plants/Controls/HeatPumps/AirToWater.mo
  - c:/buildings_library/modelica-buildings/Buildings/Templates/Plants/HeatPumps/Components/Controls/HybridAirToWater.mo
  - c:/git_repos/prompt2control/agent_outputs/dymola_model_check/dymola_model_check.log
  - c:/git_repos/prompt2control/logs/15_baseline.log
  - c:/git_repos/prompt2control/logs/15_patch1_y1HeaPre_guard.log
  - c:/git_repos/prompt2control/logs/15_patch2_explicit_or_guard.log
  - c:/git_repos/prompt2control/logs/15_patch3_wrapper_pri_pump_guard.log
- Key observations:
  - Baseline re-run confirms unchanged failure signature:
    - Unknowns/equations: 18551 / 18551
    - Reduced difference: -30
  - Trial patch 1 (broaden `y1HeaPre` declaration guard from `have_heaWat and have_chiWat` to `have_heaWat`) produced no change in reduced difference.
  - Trial patch 2 (explicit `if/else` mutual-exclusion wiring for `or1.u2` and `or2.u1`) produced no change in reduced difference.
  - Trial patch 3 (explicit cfg-guarded primary pump speed bus connects in wrapper `HybridAirToWater.mo`) produced no change in reduced difference.
  - Both trial patches were reverted after evaluation.
- Hypotheses generated/refuted:
  - Refuted: `y1HeaPre` declaration guard is a material contributor to the full-model -30 deficit.
  - Refuted: relying on conditional component dropping (vs explicit `if/else` connect blocks) for `or1/or2` SHC fallback creates the full-model -30 deficit.
  - Refuted: wrapper primary pump speed dual-connect style (`...PriHdr` and `...PriDed`) is causing the full-model -30 deficit.
  - Generated: remaining deficit source lies outside these two candidate sites, likely in other configuration-dependent connect structures.
- Artifacts produced:
  - `logs/15_baseline.log`
  - `logs/15_patch1_y1HeaPre_guard.log`
  - `logs/15_patch2_explicit_or_guard.log`
  - `logs/15_patch3_wrapper_pri_pump_guard.log`
  - `findings/15_patch_trials.md`

| Trial | Change | Pre reduced difference | Post reduced difference | Unknown/Equation count post |
|---|---|---:|---:|---:|
| Baseline | No code change | -30 | -30 | 18551 / 18551 |
| Patch 1 | `y1HeaPre`: `if have_heaWat and have_chiWat` -> `if have_heaWat` | -30 | -30 | 18551 / 18551 |
| Patch 2 | Explicit `if/else` for SHC vs scalar-replicator connects into `or1.u2` and `or2.u1` | -30 | -30 | 18551 / 18551 |
| Patch 3 | Wrapper `HybridAirToWater`: explicit cfg-guarded connects for primary pump speed (`...PriHdr`/`...PriDed`) | -30 | -30 | 18551 / 18551 |

Acceptance criteria check:
- Reduced difference did not improve for any candidate trial.
- Stop condition reached by the second branch: candidate patches from Steps 13-14 (plus one additional wrapper cfg candidate) exhausted without success.