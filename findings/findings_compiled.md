
# File: 00_environment.md
## Step 0 Findings
- File(s) inspected: c:/buildings_library/modelica-buildings/Buildings/package.mo; c:/buildings_library/modelica-buildings/.git/HEAD; c:/buildings_library/modelica-buildings/.git/refs/heads/issue4304_HybridAirSourceHeatPumpPlantControls_April2026; c:/git_repos/prompt2control/agent_outputs/dymola_model_check/model_check.mos; c:/git_repos/prompt2control/agent_outputs/dymola_model_check/dymola_model_check.log
- Key observations:
  - Buildings library version is 13.0.0 (versionDate 2025-05-29).
  - Buildings workspace branch ref is refs/heads/issue4304_HybridAirSourceHeatPumpPlantControls_April2026.
  - Buildings Git commit SHA is 18d6e622d7e9bdbb8137b9c408546bedd10ca9c8.
  - Modelica Standard Library loaded by Dymola is Modelica 4.1.0 (openModel path in model_check.mos/log).
  - Translation tool used is Dymola 2025x (from c:/program files/dymola 2025x/insert/dymola.mos in log).
  - OpenModelica was not executed in this run.
- Hypotheses generated/refuted:
  - Generated: Environment matches the expected modern stack (Buildings 13.0.0 + MSL 4.1.0 + Dymola 2025x), so the failure is likely model/configuration-structure related rather than missing library versions.
  - Refuted: No evidence of version mismatch between Buildings and MSL.
- Artifacts produced: findings/00_environment.md
---


# File: 01_baseline.md
## Step 1 Findings
- File(s) inspected: c:/git_repos/prompt2control/agent_outputs/dymola_model_check/dymola_model_check.log; c:/git_repos/prompt2control/agent_outputs/dymola_model_check/model_check.mos; c:/git_repos/prompt2control/logs/01_dymola_check.log
- Key observations:
  - Baseline Dymola checkModel was executed for Buildings.Templates.Plants.HeatPumps.Validation.AirToWater.
  - Unknown/equation report in log:
    - "The model has the same number of unknowns and equations: 18551"
    - Then: "Error: The model is not well-posed."
    - "Using the given settings of the parameters, the difference could be reduced to -30"
  - Complete "enable=false and only start value" list (as reported):
    - datAll.pla.hp.dpSouWwHeaHp_nominal(start = 40000.0)
    - datAll.pla.hp.mSouWwCooHp_flow_nominal(start = 23.90057361376673)
    - datAll.pla.hp.mSouWwHeaHp_flow_nominal(start = 14.937858508604206)
    - datAll.tit24CliZon(start = ... Zone_1)
    - loaCoo.con.dp1_nominal(start = 0)
    - loaHea.con.dp1_nominal(start = 0)
    - pla.ctl.ctl.idxStaCoo.pas[1..3].u_internal(start = true)
    - pla.ctl.ctl.idxStaHea.pas[1..3].u_internal(start = true)
    - pla.ctl.ctl.staPumChiWatSec.enaHdr.staEquDouMod(start = zero 3x3)
    - pla.ctl.ctl.staPumChiWatSec.enaHdr.staEquSinMod(start = zero 3x3)
    - pla.ctl.ctl.staPumChiWatSec.have_valInlIso(start = false)
    - pla.ctl.ctl.staPumChiWatSec.have_valOutIso(start = false)
    - pla.ctl.ctl.staPumChiWatSec.nPumHdrDp.pas[1..3].u_internal(start = true)
    - pla.ctl.ctl.staPumHeaWatSec.enaHdr.staEquDouMod(start = zero 3x3)
    - pla.ctl.ctl.staPumHeaWatSec.enaHdr.staEquSinMod(start = zero 3x3)
    - pla.ctl.ctl.staPumHeaWatSec.have_valInlIso(start = false)
    - pla.ctl.ctl.staPumHeaWatSec.have_valOutIso(start = false)
    - pla.ctl.ctl.staPumHeaWatSec.nPumHdrDp.pas[1..3].u_internal(start = true)
    - pla.ctl.ctl.TChiWatRet.u_internal(start = 0)
    - pla.ctl.ctl.THeaWatRet.u_internal(start = 0)
    - pla.ctl.ctl.VChiWatLoa_flow.u_internal(start = 0)
    - pla.ctl.ctl.VChiWatSta_flow.u_internal(start = 0)
    - pla.ctl.ctl.VHeaWatLoa_flow.u_internal(start = 0)
    - pla.ctl.ctl.VHeaWatSta_flow.u_internal(start = 0)
    - pla.typDis_select2(start = ... Constant1Variable2)
  - No separate connect/size-mismatch warning block appeared; the principal failure is structural equation/unknown imbalance after parameter reduction.
- Hypotheses generated/refuted:
  - Generated: The baseline failure is reproducible and matches the known -30 imbalance signature.
  - Generated: Warnings are concentrated in conditional/placeholder parameters and disabled options (air-to-water model retaining water-to-water fields and internal fallback placeholders).
  - Refuted: The issue is not a missing-library/openModel failure in this run.
- Artifacts produced: logs/01_dymola_check.log; findings/01_baseline.md
---


# File: 02_validation_model.md
## Step 2 Findings
- File(s) inspected: c:/buildings_library/modelica-buildings/Buildings/Templates/Plants/HeatPumps/Validation/AirToWater.mo; c:/buildings_library/modelica-buildings/Buildings/Templates/Plants/HeatPumps/Validation/UserProject/Data/AllSystems.mo
- Key observations:
  - Full pla instantiation (key overrides) in validation model:
    - redeclare final package MediumHeaWat=Medium
    - have_hrc_select=true
    - cfg(nHpShc=0)
    - ctl(is_typDis_override=false, nAirHan=1, nEquZon=0)
    - final dat=datAll.pla
    - final have_chiWat=have_chiWat
    - nHp=3
    - typPumHeaWatPri_select1=...PumpsPrimary.Constant
    - final allowFlowReversal=allowFlowReversal
    - linearized=true
    - show_T=true
    - is_dpBalYPumSetCal=true
  - Full datAll record contents (AllSystems.pla) include:
    - hp sizing/performance data (AWHP heating/cooling files)
    - pump sizing formulas for primary/secondary HW+CHW pumps
    - hrc sizing/performance data
    - ctl overrides including T setpoints, DP setpoints, VHeaWatSec_flow_nominal, VChiWatSec_flow_nominal, yPum*Set, TChiWatSupHrc_min, THeaWatSupHrc_max, COPHeaHrc_nominal, cap*Hrc_min.
    - local override in AirToWater.mo: datAll(pla(final cfg=pla.cfg, ctl(yPumHeaWatPriSet=1, yPumChiWatPriSet=1, staEquDouMod={{1/3,1/3,1/3},{2/3,2/3,2/3},{1,1,1}}, staEquSinMod={{1/3,1/3,1/3},{2/3,2/3,2/3},{1,1,1}})))
  - Wiring of loaHea/loaCoo/ratLoa:
    - ratLoa.table has 3 columns: time + 2 outputs.
    - ratLoa.y[1] -> loaHea.u.
    - ratLoa.y[2] -> loaCoo.u.
    - ratLoa.offset is not explicitly set; TimeTable default is fill(0, nout), where nout=size(table,2)-1=2.
  - Explicit values/absence for requested parameters:
    - nHp: explicitly set to 3 in pla instance.
    - typDis: not explicitly set in validation model; inherited via typDis_select1 default path for AWHP.
    - typArrPumChiWatPri / typArrPumHeaWatPri: no such explicit parameters in this class interface (single typArrPumPri is used and not overridden).
    - typArrPumChiWatSec / typArrPumHeaWatSec: not explicit in this class interface; secondary pump type is derived via typPum*Sec finals.
    - have_pumChiWatPriDed: not explicitly set (driven by have_pumChiWatPriDed_select default path).
    - have_pumHeaWatPriDed: not an explicit parameter in this interface.
    - have_pumChiWatSec / have_pumHeaWatSec: not explicitly set; derived from typDis/is_priOnl logic.
  - Parameters in Step 1 warning list not explicitly set in validation model:
    - datAll.pla.hp.dpSouWwHeaHp_nominal
    - datAll.pla.hp.mSouWwCooHp_flow_nominal
    - datAll.pla.hp.mSouWwHeaHp_flow_nominal
    - pla.typDis_select2
    - pla.ctl.ctl.TChiWatRet.u_internal / THeaWatRet.u_internal
    - pla.ctl.ctl.VChiWatLoa_flow.u_internal / VChiWatSta_flow.u_internal / VHeaWatLoa_flow.u_internal / VHeaWatSta_flow.u_internal
    - pla.ctl.ctl.idxStaCoo.pas[*].u_internal / idxStaHea.pas[*].u_internal
    - pla.ctl.ctl.staPumChiWatSec.* and pla.ctl.ctl.staPumHeaWatSec.* warning-listed fallback parameters.
- Hypotheses generated/refuted:
  - Generated: Validation model intentionally relies on many derived/default parameters; warning set is dominated by non-overridden internal placeholders.
  - Refuted: No obvious direct mismatch in ratLoa dimensions (table and default offset are consistent: nout=2).
- Artifacts produced: findings/02_validation_model.md
---


# File: 03_plant_template.md
## Step 3 Findings
- File(s) inspected: c:/buildings_library/modelica-buildings/Buildings/Templates/Plants/HeatPumps/AirToWater.mo; c:/buildings_library/modelica-buildings/Buildings/Templates/Plants/HeatPumps/Components/Controls/HybridAirToWater.mo; c:/buildings_library/modelica-buildings/Buildings/Templates/Plants/Controls/HeatPumps/AirToWater.mo
- Key observations:
  - Controller type paths:
    - pla.ctl type path: Buildings.Templates.Plants.HeatPumps.Components.Controls.HybridAirToWater
    - pla.ctl.ctl type path: Buildings.Templates.Plants.Controls.HeatPumps.AirToWater
  - How pla.ctl.ctl is instantiated (selected have_* booleans and sources in HybridAirToWater):
    - have_chiWat <- cfg.have_chiWat
    - have_heaWat <- cfg.have_heaWat
    - have_hrc_select <- cfg.have_hrc
    - have_pumChiWatPriDed_select <- cfg.have_pumChiWatPriDed
    - have_pumPriHdr <- (cfg.typArrPumPri == Headered)
    - have_pumHeaWatPriVar_select <- cfg.have_pumHeaWatPriVar
    - have_pumChiWatPriVar_select <- cfg.have_pumChiWatPriVar
    - have_senDpChiWatRemWir <- cfg.have_senDpChiWatRemWir
    - have_senDpHeaWatRemWir <- cfg.have_senDpHeaWatRemWir
    - have_valHpInlIso <- cfg.have_valHpInlIso
    - have_valHpOutIso <- cfg.have_valHpOutIso
    - nPumChiWatSec <- if have_PumHeaWatSec_override then nPumHeaWatSec_override else cfg.nPumChiWatSec
    - nPumHeaWatSec <- if have_PumHeaWatSec_override then nPumHeaWatSec_override else cfg.nPumHeaWatSec
  - Trace of flagged conditional inputs (connect presence/guards):
    - TChiWatRet and THeaWatRet are internal PlaceholderReal blocks in pla.ctl.ctl; connects are unconditional (no if-guard):
      - connect(TChiWatPriRet, TChiWatRet.u)
      - connect(TChiWatSecRet, TChiWatRet.uPh)
      - connect(THeaWatPriRet, THeaWatRet.u)
      - connect(THeaWatSecRet, THeaWatRet.uPh)
    - V*Sta_flow and V*Loa_flow placeholders are connected unconditionally (u and uPh).
    - idxStaCoo/idxStaHea warnings point to StageIndex.pas[*].u_internal (internal PlaceholderLogical); the block-level connections are internal and unguarded.
    - staPum*WatSec.nPumHdrDp.pas[*].u_internal are inside StagingHeadered -> StageIndex; connections are internal and unguarded.
  - Propagation of staging matrices:
    - In HybridAirToWater, pla.ctl.ctl receives final staEquSinMod=dat.staEquSinMod and final staEquDouMod=dat.staEquDouMod.
    - pla.ctl.staEqu (final parameter of HybridAirToWater) is derived from dat.staEqu (or dat.staEquSinMod if cfg.have_HpShc).
- Hypotheses generated/refuted:
  - Generated: There is no obvious missing top-level connect() for flagged items; warnings are tied to internal placeholder fallbacks and disabled branches.
  - Refuted: A direct external bus wiring omission for T*/V* signals in pla.ctl is not observed.
- Artifacts produced: findings/03_plant_template.md
---


# File: 04_controller_interface.md
## Step 4 Findings
- File(s) inspected: c:/buildings_library/modelica-buildings/Buildings/Templates/Plants/Controls/HeatPumps/AirToWater.mo; c:/buildings_library/modelica-buildings/Buildings/Templates/Plants/Controls/Utilities/PlaceholderReal.mo; c:/buildings_library/modelica-buildings/Buildings/Templates/Plants/Controls/Utilities/StageIndex.mo; c:/buildings_library/modelica-buildings/Buildings/Templates/Plants/Controls/Pumps/Generic/StagingHeadered.mo
- Key observations:
  - Required conditional inputs are implemented through internal placeholder blocks and conditional connectors.
  - Declarations and enable/guard logic:
    - TChiWatRet: Utilities.PlaceholderReal TChiWatRet(final have_inp=have_senTChiWatPriRet, final have_inpPh=true) if have_chiWat.
      - Effective enable for direct input u is have_senTChiWatPriRet.
      - Placeholder path uPh is active when not have_senTChiWatPriRet.
    - THeaWatRet: Utilities.PlaceholderReal THeaWatRet(final have_inp=have_senTHeaWatPriRet, final have_inpPh=true) if have_heaWat.
      - Effective enable for direct input u is have_senTHeaWatPriRet.
    - VChiWatSta_flow: Utilities.PlaceholderReal VChiWatSta_flow(final have_inp=have_senVChiWatPri, final have_inpPh=true) if have_chiWat.
    - VHeaWatSta_flow: Utilities.PlaceholderReal VHeaWatSta_flow(final have_inp=have_senVHeaWatPri, final have_inpPh=true) if have_heaWat.
    - VChiWatLoa_flow: Utilities.PlaceholderReal VChiWatLoa_flow(final have_inp=is_priOnl, final have_inpPh=true) if have_chiWat.
    - VHeaWatLoa_flow: Utilities.PlaceholderReal VHeaWatLoa_flow(final have_inp=is_priOnl, final have_inpPh=true) if have_heaWat.
    - idxStaCoo.pas[1..3] and idxStaHea.pas[1..3]: inside Utilities.StageIndex as PlaceholderLogical pas[nSta](have_inp=dtRun>0, have_inpPh=true).
    - staPumChiWatSec.nPumHdrDp.pas[1..3] and staPumHeaWatSec.nPumHdrDp.pas[1..3]: via Pumps.Generic.StagingHeadered -> StageIndex nPumHdrDp(final have_inpAva=false, final nSta=nPum) and its internal pas[nSta](have_inp=dtRun>0, have_inpPh=true).
  - staEquSinMod / staEquDouMod and defaults:
    - Controller parameters staEquSinMod[:, nHpTot] and staEquDouMod[:, nHpTot] exist in AirToWater controller.
    - Warning-listed secondary pump values refer to staPum*Sec.enaHdr.staEquSinMod/DouMod defaults inside EquipmentEnable in StagingHeadered context.
  - have_valInlIso/have_valOutIso in secondary pump staging:
    - In StagingHeadered, parameters default to false and are Dialog-enabled only for is_pri.
    - Secondary instances (is_pri=false) therefore keep defaults false and appear in warning list.
- Hypotheses generated/refuted:
  - Generated: Most warning-listed values are default/fallback parameters from generic blocks, not necessarily active control paths.
  - Refuted: No evidence that these declarations are missing enable logic; they use explicit conditional interfaces and placeholder selection.
- Artifacts produced: findings/04_controller_interface.md
---


# File: 05_guard_consistency.md
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
---


# File: 06_resolved_params.md
## Step 6 Findings
- File(s) inspected: c:/buildings_library/modelica-buildings/Buildings/Templates/Plants/HeatPumps/Validation/AirToWater.mo; c:/buildings_library/modelica-buildings/Buildings/Templates/Plants/HeatPumps/Validation/UserProject/Data/AllSystems.mo; c:/buildings_library/modelica-buildings/Buildings/Templates/Plants/HeatPumps/Interfaces/PartialHeatPumpPlant.mo; c:/buildings_library/modelica-buildings/Buildings/Templates/Plants/HeatPumps/Components/Interfaces/PartialController.mo; c:/buildings_library/modelica-buildings/Buildings/Templates/Plants/Controls/HeatPumps/AirToWater.mo; c:/git_repos/prompt2control/agent_outputs/dymola_model_check/dymola_model_check.log
- Key observations:
  - Resolved/inferred parameter values for this configuration:
    - pla.nHp = 3 (explicit in validation model).
    - pla.typDis = Constant1Variable2 (AWHP uses typDis_select1 default, typDis_select1 default is Constant1Variable2).
    - pla.typArrPumChiWatPri / pla.typArrPumHeaWatPri: not separate parameters in this template; effective primary arrangement is typArrPumPri=Dedicated (default).
    - pla.typArrPumChiWatSec / pla.typArrPumHeaWatSec: not separate parameters; effective secondary pump types derive to Centralized for typDis=Constant1Variable2.
    - have_pumChiWatPriDed = false (have_pumChiWatPriDed_select default false, typArr dedicated).
    - have_pumHeaWatPriDed: not explicit in this interface.
    - have_pumChiWatSec = true; have_pumHeaWatSec = true (is_priOnl=false -> both secondary loops active).
    - have_senDpChiWatRemWir = false; have_senDpHeaWatRemWir = false (defaults from PartialController).
    - have_senVChiWatSec_flow / have_senVHeaWatSec_flow (controller-level equivalents have_senVChiWatSec/have_senVHeaWatSec) = true.
    - have_valChiWatMinByp = false for typDis=Constant1Variable2.
    - have_hrc = true (validation sets have_hrc_select=true).
    - pla.ctl.ctl.nPumChiWatSec = 3; pla.ctl.ctl.nPumHeaWatSec = 3.
    - pla.ctl.ctl.nSenDpChiWatRem = 1; pla.ctl.ctl.nSenDpHeaWatRem = 1.
    - pla.ctl.ctl.staPumChiWatSec.have_valInlIso = false; have_valOutIso = false; nSta = 3; nEquAlt = 3.
    - pla.ctl.ctl.staPumHeaWatSec.have_valInlIso = false; have_valOutIso = false; nSta = 3; nEquAlt = 3.
    - pla.ctl.staEqu = {{1/3,1/3,1/3},{2/3,2/3,2/3},{1,1,1}}.
  - Referenced nin/nout terms on unknown-side expression:
    - pla.ctl.ctl.staPumHeaWatPri.y1Ded_actual.nin = 3.
    - pla.ctl.ctl.staPumHeaWatPri.y1Ded_actual.nout = 3.
    - pla.ctl.ctl.ctlPumHeaWatSec.maxSet.nin = 1.
    - pla.ctl.ctl.ctlPumChiWatSec.maxSet.nin = 1.
  - Additional directly resolved scalar terms in the unknown-side expression:
    - size(pla.dat.hrc.per.PLRSup,1) = 10.
    - size(ratLoa.table,2) = 3.
    - size(ratLoa.offset,1) = 2 (TimeTable default offset length = nout = size(table,2)-1).
- Hypotheses generated/refuted:
  - Generated: Configuration resolves to a fully defined 3-HP, primary-secondary, HRC-enabled AWHP plant.
  - Generated: Several warning-listed `u_internal` values come from fallback paths whose controlling booleans evaluate false by design.
  - Refuted: No evidence that primary cardinality terms are undefined; they resolve to concrete values listed above.
- Artifacts produced: findings/06_resolved_params.md
---


# File: 07_data_record.md
## Step 7 Findings
- File(s) inspected: c:/buildings_library/modelica-buildings/Buildings/Templates/Plants/HeatPumps/Components/Data/HeatPumpGroup.mo
- Key observations:
  - Declarations and enable expressions in HeatPumpGroup record:
    - mSouWwHeaHp_flow_nominal: Dialog enable = typ==Buildings.Templates.Components.Types.HeatPump.WaterToWater.
    - dpSouWwHeaHp_nominal: Dialog enable = typ==Buildings.Templates.Components.Types.HeatPump.WaterToWater.
    - mSouWwCooHp_flow_nominal: Dialog enable = typ==Buildings.Templates.Components.Types.HeatPump.WaterToWater and is_rev.
  - Discriminator used: typ (HeatPump type enum), specifically equality to WaterToWater.
  - Exclusion behavior for AWHP:
    - For AWHP (typ==AirToWater), these water-source parameters are not used in final source flow/pressure finals:
      - mSouHeaHp_flow_nominal uses else branch ratMFloAirByCapChi * abs(capHeaHp_nominal).
      - dpSouHeaHp_nominal uses else branch dpAirChi.
      - mSouCooHp_flow_nominal similarly uses air-side formula.
    - Therefore, warning appearance is from disabled parameter records retaining start-only placeholders, not from active physics equations for AWHP.
- Hypotheses generated/refuted:
  - Generated: This is primarily a warning-only modeling hygiene issue for AWHP configurations.
  - Refuted: No direct evidence these WaterToWater-only record fields are the dominant contributor to the -30 equation imbalance.
- Artifacts produced: findings/07_data_record.md
---


# File: 08_arithmetic_reconciliation.md
## Step 8 Findings
- File(s) inspected: c:/git_repos/prompt2control/agent_outputs/dymola_model_check/dymola_model_check.log; c:/buildings_library/modelica-buildings/Buildings/Templates/Plants/HeatPumps/Validation/AirToWater.mo; c:/buildings_library/modelica-buildings/Buildings/Templates/Plants/HeatPumps/Validation/UserProject/Data/AllSystems.mo; c:/buildings_library/modelica-buildings/Buildings/Controls/OBC/CDL/Reals/Sources/TimeTable.mo
- Key observations:
  - Unknown-side expression reconciliation (values substituted from Step 6):
    - countTrue(...) over pla.ctl.staEqu columns = 3.
    - 18470 + 16*3 = 18518.
    - + staPumHeaWatPri.y1Ded_actual.nin (3) -> 18521.
    - + staPumHeaWatPri.y1Ded_actual.nout (3) -> 18524.
    - + ctlPumHeaWatSec.maxSet.nin (1) -> 18525.
    - + ctlPumChiWatSec.maxSet.nin (1) -> 18526.
    - + 2*size(pla.dat.hrc.per.PLRSup,1) = 2*10 = 20 -> 18546.
    - + size(ratLoa.table,2) = 3 -> 18549.
    - + max([2; size(ratLoa.offset,1)]) = max([2;2]) = 2 -> 18551.
    - Result matches Dymola unknown count 18551.
  - Equations-side expression:
    - Dymola reports same base count 18551 before reduction and then "difference could be reduced to -30".
    - This implies effective reduced equations exceed unknowns by 30 (equations ≈ 18581 vs unknowns 18551).
  - The largest unresolved symbolic contribution on equation side is a large sum of conditional cardinality terms involving many `*.nin` values and conditional branch counts; Dymola collapses this to the reported net imbalance of 30.
- Hypotheses generated/refuted:
  - Generated: Unknown-side expression is internally consistent and fully reconciled.
  - Generated: The residual -30 comes from equation-side conditional block cardinalities after parameter reduction, not from unknown-side count errors.
  - Refuted: ratLoa dimensionality is not the source of the mismatch.
- Artifacts produced: findings/08_arithmetic_reconciliation.md
---


# File: 09_root_cause_report.md
## Root Cause Report
- Primary finding:
  - The baseline failure is reproducible in Dymola: the model is structurally overdetermined by 30 equations after parameter reduction (`difference could be reduced to -30`).
- Most likely mechanism:
  - The imbalance is associated with conditional cardinality in controller internals (especially staged logic and pump-staging subgraphs) rather than a missing top-level connection.
  - Guard-consistency checks show no direct connect()/enable mismatches for the flagged inputs.
  - Warning set is dominated by start-only fallback parameters in disabled branches (`u_internal`, `staEquSinMod`, `staEquDouMod`, `have_valInlIso`, `have_valOutIso`, and WaterToWater-only HP fields).
- Key evidence:
  - Reproduced log: logs/01_dymola_check.log.
  - Unknown-side symbolic expression exactly reconciles to 18551 with resolved parameter values.
  - Equation-side symbolic expression reduces to unknowns + 30 under this configuration.
  - No direct missing connect found for the listed conditional signals.
- Conclusion:
  - The overdetermination is most consistent with disabled-branch placeholder/cardinality behavior in nested controller blocks under this specific configuration (AWHP + Constant1Variable2 + HRC + dedicated primary arrangement + secondary pump staging active).

## Proposed Fix
- Minimal targeted code fix candidate:
  - In `Buildings/Templates/Plants/Controls/Utilities/PlaceholderReal.mo` and `Buildings/Templates/Plants/Controls/Utilities/PlaceholderLogical.mo`, give `u_internal` an explicit default value assignment (not only `start`), e.g. `u_internal=0` and `u_internal=true` respectively.
  - Rationale: this removes start-only parameter ambiguity in disabled branches that are repeatedly flagged by Dymola in this failing translation.
- Secondary hardening fix candidate:
  - In `Buildings/Templates/Plants/Controls/Pumps/Generic/StagingHeadered.mo`, explicitly bind `nPumHdrDp.dtRun=dtRun` when instantiating `Utilities.StageIndex nPumHdrDp(...)`.
  - Rationale: avoids default `dtRun=0` in nested StageIndex that triggers `pas[*].u_internal` fallback behavior in secondary pump staging.
- Verification plan after patch:
  - Re-run the exact baseline command and confirm:
    - no `difference could be reduced to -30` message,
    - reduced warning set for `u_internal`/start-only parameters,
    - checkModel success.
- Scope control:
  - Keep fixes local to placeholder/staging utility blocks; avoid changing plant-level configuration semantics.
---


# File: 10_patch_verification.md
## Patch Verification Findings
- File(s) inspected: c:/git_repos/prompt2control/agent_outputs/dymola_model_check/dymola_model_check.log; c:/git_repos/prompt2control/logs/01_dymola_check.log
- Key observations:
  - Post patch rerun still fails checkModel for Buildings.Templates.Plants.HeatPumps.Validation.AirToWater.
  - New run reports:
    - The model has the same number of unknowns and equations: 18575.
    - Error: The model is not well posed.
    - Using the given settings of the parameters, the difference could be reduced to -30.
  - Relative to baseline:
    - Baseline unknown and equation count was 18551 with reduced difference -30.
    - Post patch unknown and equation count moved to 18575, but reduced difference remained -30.
  - Warning list changed as expected:
    - Previous warning entries for placeholder u_internal terms at idxStaCoo and idxStaHea, nPumHdrDp placeholder terms, and placeholder real terms TChiWatRet, THeaWatRet, V*Sta_flow, V*Loa_flow are no longer listed.
    - Remaining warnings include disabled branch parameters such as staPumChiWatSec and staPumHeaWatSec staEqu and valve flags, typDis_select2, and WaterToWater-only HP data fields.
- Hypotheses generated/refuted:
  - Refuted: The placeholder default and nPumHdrDp dtRun patch is not sufficient to eliminate the -30 structural imbalance.
  - Generated: Root cause likely sits deeper in equation side cardinality of staging and pump control subgraphs, not in placeholder parameter default semantics.
- Artifacts produced: findings/10_patch_verification.md
---


# File: 11_isolation_checks.md
## Isolation Checks After Patch Verification
- Scope: narrow the remaining reduced difference -30 after the placeholder and dtRun patch.

### 1) Symbolic expression delta baseline vs post-patch AirToWater
- Baseline unknown base term: 18470
- Post-patch unknown base term: 18494
- Baseline equation base term: 18278
- Post-patch equation base term: 18302
- Result: both sides increased by +24, so reduced difference stayed -30.
- Interpretation: patch changed absolute model size but not structural imbalance.

### 2) Subsystem validations in staging/pump controls
All of the following pass checkModel with equal unknown/equation counts:
- Buildings.Templates.Plants.Controls.Pumps.Generic.Validation.StagingHeadered: 3245
- Buildings.Templates.Plants.Controls.Pumps.Generic.Validation.StagingHeaderedDeltaP: 2467
- Buildings.Templates.Plants.Controls.StagingRotation.Validation.EquipmentEnable: 520
- Buildings.Templates.Plants.Controls.StagingRotation.Validation.StageChangeCommand: 1926
- Buildings.Templates.Plants.Controls.StagingRotation.Validation.StageCompletion: 82

Interpretation: no isolated defect in these standalone staging/control validation models.

### 3) HeatPumps component validations
All of the following pass checkModel:
- Buildings.Templates.Plants.HeatPumps.Components.Validation.HeatPumpGroupAirToWater: 5450
- Buildings.Templates.Plants.HeatPumps.Components.Validation.HeatRecoveryChiller: 1072
- Buildings.Templates.Plants.HeatPumps.Components.Validation.PumpsPrimaryDedicated: 3463
- Buildings.Templates.Plants.HeatPumps.Components.Validation.ValvesIsolation: 2420
- Buildings.Templates.Plants.HeatPumps.Validation.HybridAirToWater: 16413

Interpretation: component-level models and HybridAirToWater are structurally balanced.

### 4) Targeted HRC isolation experiment
- Temporary model added: Buildings.Templates.Plants.HeatPumps.Validation.AirToWaterNoHRC
- This model extends AirToWater and sets pla.have_hrc_select=false.
- checkModel result:
  - The model has the same number of unknowns and equations: 17018
  - Error: The model is not well-posed.
  - Using the given settings of the parameters, the difference could be reduced to -30.

Interpretation:
- Disabling HRC does not remove the -30 deficit.
- Therefore the root cause is not specific to HRC integration.

### 5) Heating-only isolation experiment (CHW disabled)
- Temporary model added: Buildings.Templates.Plants.HeatPumps.Validation.AirToWaterHeatingOnly
- This model extends AirToWater with have_chiWat=false.
- checkModel result highlights:
  - It has 10453 scalar unknowns and 10444 scalar equations.
  - Boolean part has 3418 unknowns and 3409 equations.
  - Error: model is not well-posed.
  - Reduced difference could be reduced to -6.
  - Dymola localizes structural singularity in pla.ctl.ctl with unconnected inputs such as:
    - pla.ctl.ctl.or1[1..3].u1
    - pla.ctl.ctl.andHeaEna[1..3].u2
    - pla.ctl.ctl.notCooMod[1..3].u

Interpretation:
- The full AirToWater -30 deficit is not purely heating-side.
- With CHW path removed, the reduced difference drops to -6.
- This indicates most of the deficit is tied to cooling-side or cross-mode logic, while a smaller residual remains on heating-side controller logic/guarding.

### Current best hypothesis
- The remaining -30 appears tied to AirToWater top-level integration with the 3-equipment cardinality path (including staged arrays with index [1..3]) rather than HRC and rather than isolated staging components.
- Next high-value probe is to test a cooling-only diagnostic variant and compare the reduced difference with the heating-only (-6) case to partition the residual by mode.

### 6) Two-HP cardinality probe
- Temporary model added: Buildings.Templates.Plants.HeatPumps.Validation.AirToWaterTwoHp
- This model extends AirToWater with pla.nHp=2.
- checkModel result: failed immediately with dimension mismatch before structural counts:
  - pla.ctl.ctl.staEquDouMod = pla.ctl.dat.staEquDouMod has incompatible dimension-2 sizes 2 and 3.

Interpretation:
- The AirToWater data/control staging tables are hard-coupled to 3 equipment columns.
- A direct nHp reduction test is blocked unless staging data arrays are modified in lockstep.

### 7) Two-HP probe with synchronized 2x2 staging matrices (user-specified)
- Matrix values applied to both staging parameters:
  - staEquDouMod={{0.5,0.5},{1,1}}
  - staEquSinMod={{0.5,0.5},{1,1}}
- Applied in temporary model:
  - Buildings.Templates.Plants.HeatPumps.Validation.AirToWaterTwoHp
  - with pla.nHp=2
- checkModel result:
  - The model has the same number of unknowns and equations: 14403.
  - Error: The model is not well-posed.
  - Reduced difference could be reduced to -16.

Interpretation:
- Synchronizing staging matrix dimensions resolves the prior nHp dimension mismatch.
- The structural deficit improves from -30 to -16, but the model remains not well-posed.

### 8) Temporary-file cleanup status
- Removed previously created temporary diagnostic files:
  - AirToWaterNoHRC.mo
  - AirToWaterHeatingOnly.mo
  - AirToWaterTwoHp.mo
- Restored validation package order to permanent models only.
---

