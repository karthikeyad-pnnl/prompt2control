## Step 5 Findings
- File(s) inspected: c:/buildings_library/modelica-buildings/Buildings/Templates/Plants/Controls/HeatPumps/AirToWater.mo; c:/buildings_library/modelica-buildings/Buildings/Templates/Plants/Controls/Utilities/PlaceholderReal.mo; c:/buildings_library/modelica-buildings/Buildings/Templates/Plants/Controls/Utilities/StageIndex.mo; c:/buildings_library/modelica-buildings/Buildings/Templates/Plants/Controls/Pumps/Generic/StagingHeadered.mo; c:/buildings_library/modelica-buildings/Buildings/Templates/Plants/HeatPumps/Components/Interfaces/PartialController.mo; c:/buildings_library/modelica-buildings/Buildings/Templates/Plants/HeatPumps/Interfaces/PartialHeatPumpPlant.mo; c:/buildings_library/modelica-buildings/Buildings/Templates/Plants/HeatPumps/Validation/AirToWater.mo
- Key observations:
  - No row with controller-enabled input and missing connect() was found for the flagged list.
  - Most flagged items are placeholder internal parameters (`u_internal`) in paths where input connectors are conditionally absent by design.

| Input | Controller-side enable | Template connect() guard | Match? | Evaluates to (true/false) |
|---|---|---|---|---|
| TChiWatRet | have_senTChiWatPriRet | connect(TChiWatPriRet, TChiWatRet.u), unguarded | Yes | true |
| THeaWatRet | have_senTHeaWatPriRet | connect(THeaWatPriRet, THeaWatRet.u), unguarded | Yes | true |
| VChiWatSta_flow | have_senVChiWatPri | connect(VChiWatPri_flow, VChiWatSta_flow.u), unguarded | Yes | true |
| VHeaWatSta_flow | have_senVHeaWatPri | connect(VHeaWatPri_flow, VHeaWatSta_flow.u), unguarded | Yes | true |
| VChiWatLoa_flow | is_priOnl (for `u`; fallback `uPh` otherwise) | connect(VChiWatPri_flow, VChiWatLoa_flow.u) and connect(VChiWatSec_flow, VChiWatLoa_flow.uPh), unguarded | Yes | false (u), true (uPh path) |
| VHeaWatLoa_flow | is_priOnl (for `u`; fallback `uPh` otherwise) | connect(VHeaWatPri_flow, VHeaWatLoa_flow.u) and connect(VHeaWatSec_flow, VHeaWatLoa_flow.uPh), unguarded | Yes | false (u), true (uPh path) |
| idxStaCoo.pas[1..3] | dtRunSta>0 inside StageIndex | internal connect(tim.passed, pas.u) and connect(sta.active, pas.uPh) | Yes | true |
| idxStaHea.pas[1..3] | dtRunSta>0 inside StageIndex | internal connect(tim.passed, pas.u) and connect(sta.active, pas.uPh) | Yes | true |
| staPumChiWatSec.nPumHdrDp.pas[1..3] | dtRun>0 inside nPumHdrDp StageIndex | internal StageIndex connections in StagingHeadered | Yes | false |
| staPumHeaWatSec.nPumHdrDp.pas[1..3] | dtRun>0 inside nPumHdrDp StageIndex | internal StageIndex connections in StagingHeadered | Yes | false |

- Hypotheses generated/refuted:
  - Generated: Guard inconsistency is not the primary failure mechanism for this model.
  - Generated: The warnings and imbalance are likely tied to default/placeholder parameterization in disabled branches rather than missing connections.
  - Refuted: No direct connect()/enable mismatch in the flagged signals.
- Artifacts produced: findings/05_guard_consistency.md