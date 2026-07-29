## Step 14 Findings
- File(s) inspected:
  - c:/buildings_library/modelica-buildings/Buildings/Templates/Plants/HeatPumps/AirToWater.mo
  - c:/buildings_library/modelica-buildings/Buildings/Templates/Plants/HeatPumps/Validation/AirToWater.mo
  - c:/buildings_library/modelica-buildings/Buildings/Templates/Plants/HeatPumps/Validation/HybridAirToWater.mo
  - c:/buildings_library/modelica-buildings/Buildings/Templates/Plants/HeatPumps/Components/Controls/HybridAirToWater.mo
  - c:/buildings_library/modelica-buildings/Buildings/Templates/Plants/Controls/HeatPumps/AirToWater.mo
- Key observations:
  - The failing validation and the working hybrid validation both instantiate the same plant template class: `Buildings.Templates.Plants.HeatPumps.AirToWater`.
  - The plant template `AirToWater.mo` redeclares the same wrapper controller in both cases: `Buildings.Templates.Plants.HeatPumps.Components.Controls.HybridAirToWater`.
  - The wrapper controller instantiates the same core controller class used in prior steps: `Buildings.Templates.Plants.Controls.HeatPumps.AirToWater`.
  - No alternate top-level `Buildings/Templates/Plants/HeatPumps/HybridAirToWater.mo` template exists in this workspace; the hybrid path differs by configuration and data, not by a separate plant-template implementation.
  - The cross-mode wiring block (`or1`, `andHeaEna`, `notCooMod`) is in the shared controller class and is therefore structurally identical between failing and passing validation paths.
- Hypotheses generated/refuted:
  - Refuted: a code-diff in plant-template equation sections between two different top-level templates (`AirToWater` vs `HybridAirToWater`) explains the deficit.
  - Refuted: the working hybrid path uses a different core controller class than the failing path.
  - Generated: remaining root cause is likely configuration-dependent conditional activation and/or other plant-template-side bus wiring behavior under failing `cfg` values.
- Artifacts produced:
  - This report: `findings/14_diff_vs_hybrid.md`

### 14.1 Controller Class Used by Hybrid Validation

- `Validation/HybridAirToWater.mo` instantiates `Buildings.Templates.Plants.HeatPumps.AirToWater pla(...)`.
- `HeatPumps/AirToWater.mo` redeclares controller wrapper `Components.Controls.HybridAirToWater ctl(...)`.
- `Components/Controls/HybridAirToWater.mo` instantiates core controller `Buildings.Templates.Plants.Controls.HeatPumps.AirToWater ctl(...)`.

Conclusion: both failing and passing validation paths route through the same controller implementation.

### 14.2 Equation-Section Diff Scope and Result

Requested pair in checklist:
- `Buildings/Templates/Plants/HeatPumps/AirToWater.mo` (present)
- `Buildings/Templates/Plants/HeatPumps/HybridAirToWater.mo` (not present)

Canonical fallback used:
- Compare failing and passing *instantiation/configuration* paths that both target `HeatPumps/AirToWater.mo` and shared wrapper/controller.

Result:
- No structural code split at template/controller source level for cross-mode signal wiring; both validations use identical source files.

### 14.3 cfg/have_* Propagation Differences (Failing vs Working Validation)

`Validation/AirToWater.mo` (failing path):
- `cfg(nHpShc=0)`
- `have_hrc_select=true`
- `nHp=3`

`Validation/HybridAirToWater.mo` (working path):
- `cfg(nHpShc=1)`
- `have_hrc_select=false`
- `nHp=2`
- different staging matrices (`staEquDouMod`, `staEquSinMod`) and additional overrides.

Assessment:
- Dominant differences are `cfg`/parameterization, not source wiring code.

### 14.4 Wrapper-Level Wiring Differences Potentially Relevant to or1/andHeaEna/notCooMod

- No direct wrapper connections to internal `or1`, `andHeaEna`, `notCooMod` pins (these are internal to core controller).
- Wrapper uses conditional bus connects for SHC-specific cases (e.g., `if cfg.have_HpShc then ...`).
- Since failing path has `cfg.nHpShc=0`, those SHC branches are inactive there.

Assessment:
- No wrapper-side block found that directly rewires the three localized internal pins.

### Stop Condition Assessment

Step 14 stop condition is met via the second branch:
- The compared paths are structurally identical with respect to cross-mode wiring in the shared controller source.
- Suspicion therefore shifts to configuration-driven activation patterns and plant-template-side behavior under failing `cfg`.