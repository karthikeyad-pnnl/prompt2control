## Step 16 Findings
- File(s) inspected:
  - c:/buildings_library/modelica-buildings/Buildings/Templates/Plants/HeatPumps/AirToWater.mo
  - c:/buildings_library/modelica-buildings/Buildings/Templates/Plants/HeatPumps/Components/Controls/HybridAirToWater.mo
  - c:/buildings_library/modelica-buildings/Buildings/Templates/Plants/Controls/HeatPumps/AirToWater.mo
  - c:/buildings_library/modelica-buildings/Buildings/Templates/Plants/HeatPumps/Validation/AirToWater.mo
- Key observations:
  - Plant template `HeatPumps/AirToWater.mo` uses the `Components.Controls.HybridAirToWater` wrapper in both failing and passing validation paths.
  - Wrapper bus-to-controller connections are predominantly unconditional; SHC-specific connects are conditionally wrapped in `if cfg.have_HpShc then ... end if`.
  - In failing config (`Validation/AirToWater.mo` uses `cfg(nHpShc=0)`), `cfg.have_HpShc=false`, so SHC branches are inactive.
  - No direct plant-template-side connect was found that targets internal `or1`, `andHeaEna`, or `notCooMod` pins (all are internal to core controller).
  - Duplicate-looking wrapper connects for pump speed commands map to conditionally declared outputs (`...PriHdr` vs `...PriDed`) and are intended to be mutually exclusive under the parameter logic.
- Hypotheses generated/refuted:
  - Refuted: obvious plant-template-side controller-bus miswire in `HeatPumps/AirToWater.mo` directly explains the -30 deficit.
  - Refuted: SHC branch activation mismatch is active in failing config (it is inactive for `nHpShc=0`).
  - Generated: next likely contributors are deeper conditional declarations/connects in components reached through wrapper buses, not the already-audited `or1/andHeaEna/notCooMod` cluster.
- Artifacts produced:
  - `findings/16_plant_template_reaudit.md`

## Updated Root Cause Report

1. Step 14 confirmed no source-code split between failing and passing paths for the core controller wiring; both use the same implementation chain.
2. Step 15 trial patches did not change reduced difference (`-30` remained invariant), so the tested hypotheses are not causal for the full failure.
3. Step 16 found no clear plant-template bus miswire that directly explains the deficit under failing `cfg`.
4. Current evidence indicates the remaining deficit is likely in other configuration-gated connect structures/components outside the two tested candidate sites.

## Proposed Fix

1. Keep trial patches reverted (already done).
2. Continue with targeted candidate discovery before further patching, prioritizing:
   - Additional conditionally declared sources feeding always-declared array logic in core controller subcomponents.
   - Wrapper-bus downstream component graphs where endpoint existence differs by `cfg` while consuming logic remains active.
   - A focused cooling-only partition confirmation and per-subgraph equation-balance probes to isolate the remaining -24/-30 contributors.