## Step 17.a Findings
- File(s) inspected:
  - c:/buildings_library/modelica-buildings/Buildings/Templates/Plants/Controls/HeatPumps/AirToWater.mo
  - c:/buildings_library/modelica-buildings/Buildings/Controls/OBC/CDL/Reals/Sources/Constant.mo
  - c:/buildings_library/modelica-buildings/Buildings/Controls/OBC/CDL/Logical/Sources/Constant.mo
  - c:/buildings_library/modelica-buildings/Buildings/Controls/OBC/CDL/Routing/BooleanScalarReplicator.mo
  - c:/buildings_library/modelica-buildings/Buildings/Controls/OBC/CDL/Routing/BooleanExtractSignal.mo
- Key observations:
  - Non-SHC branch declarations in AirToWater controller were confirmed at:
    - staMat[nSta,nHpTot] if not have_HpShc (line 1725-1726)
    - con(k=false) if not have_HpShc (line 1728-1729)
    - booScaRep(nout=nHpTot) if not have_HpShc (line 1731-1732)
    - pasPumHeaWatPri(nin=nPumHeaWatPriTot, nout=nPumHeaWatPriTot) if not have_HpShc (line 1793-1795)
  - Equation forms from block definitions:
    - Reals.Sources.Constant: y=k (1 equation per block instance)
    - Logical.Sources.Constant: y=k (1 equation per block instance)
    - BooleanScalarReplicator: y=fill(u,nout) (vector equation size nout)
    - BooleanExtractSignal: for i in 1:nout loop y[i]=u[extract[i]] end for (nout equations)
  - Under nHpShc=0, nHpTot=nHp and (by default in this model family) nPumHeaWatPriTot tracks nHp.
  - Delta from nHp=3 to nHp=2 on these candidate non-SHC declarations:
    - staMat: 3*nHpTot = 9 -> 6, Delta = -3
    - booScaRep: nHpTot = 3 -> 2, Delta = -1
    - pasPumHeaWatPri: nPumHeaWatPriTot = 3 -> 2, Delta = -1
    - con: 1 -> 1, Delta = 0
    - Total explicit branch-local Delta = -5
  - Observed reduced-difference closure between data points (3,0)->(2,0) is +14 (from -30 to -16), so branch-local declarations explain only part of the closure.
- Hypotheses generated/refuted:
  - Refuted: non-SHC branch-local declarations alone explain the full per-HP change.
  - Generated: at least one additional contributor is in branch-dependent interactions with always-active nHpTot-sized logic (not solely in the four non-SHC declarations).
- Artifacts produced:
  - c:/git_repos/prompt2control/findings/17_per_hp_defect_localization.md (this report)

### Step 17.a Delta Table

| Block | Branch | Equation expression | nHp=3,nHpShc=0 | nHp=2,nHpShc=0 | Delta |
|---|---|---|---:|---:|---:|
| staMat[nSta,nHpTot] | not have_HpShc | nSta*nHpTot | 9 | 6 | -3 |
| booScaRep(nout=nHpTot) | not have_HpShc | nHpTot | 3 | 2 | -1 |
| pasPumHeaWatPri(nout=nPumHeaWatPriTot) | not have_HpShc | nPumHeaWatPriTot | 3 | 2 | -1 |
| con(k=false) | not have_HpShc | 1 | 1 | 1 | 0 |
| Total (listed non-SHC declarations) | - | - | 16 | 11 | -5 |

## Step 17.b Findings
- File(s) inspected:
  - c:/buildings_library/modelica-buildings/Buildings/Templates/Plants/Controls/StagingRotation/HybridOperation.mo
  - c:/buildings_library/modelica-buildings/Buildings/Templates/Plants/Controls/HeatPumps/AirToWater.mo
- Key observations:
  - HybridOperation output declaration is yStaEqu[nSta,nHp] (HybridOperation line 123), and AirToWater instantiates ctlPlaHyb with nHp=nHpTot (AirToWater line 1719). Therefore ctlPlaHyb.yStaEqu resolves to [nSta,nHpTot] in this controller.
  - staMat is declared once as staMat[nSta,nHpTot] and is connected to both avaStaHea.staEqu and avaStaCoo.staEqu.
  - The SHC branch similarly uses one source (ctlPlaHyb.yStaEqu) connected to both avaStaHea.staEqu and avaStaCoo.staEqu.
  - No evidence of duplicate staging-matrix source declarations (e.g., one per mode) was found in the non-SHC branch.
- Hypotheses generated/refuted:
  - Refuted: duplicate non-SHC staging-matrix source instantiation as the per-HP carrier.
  - Refuted: direct yStaEqu dimensional mismatch between SHC and non-SHC branch sources.
  - Generated: per-HP excess likely comes from branch-dependent internal logic topology rather than the top-level stage-matrix source size contract.
- Artifacts produced:
  - c:/git_repos/prompt2control/findings/17_per_hp_defect_localization.md (this report)

## Step 17.c Findings
- File(s) inspected:
  - c:/git_repos/prompt2control/findings/15_nhpshc_axis.md
  - c:/git_repos/prompt2control/findings/16_decomposition.md
- Key observations:
  - Using recorded reduced-difference points:
    - (nHp=3, nHpShc=0): -30
    - (nHp=2, nHpShc=0): -16
    - (nHp=3, nHpShc=1): -12
  - Linear fit D = a*nNonShc + b*nShc + c gives:
    - a = -14
    - b = +4
    - c = +12
  - This linear fit predicts D=+2 for (nHp=2,nHpShc=1), but Hybrid validation passes (D=0). Therefore the linear model is inconsistent with the known pass case.
  - Functional form is not uniquely identifiable from available points because SHC2/SHC3 runs were blocked by translator NotImplemented.
- Hypotheses generated/refuted:
  - Refuted: simple linear-in-count decomposition across non-SHC/SHC counts.
  - Generated: defect has nonlinear or edge-triggered behavior in branch composition (likely activated for nNonShc>=2 and/or nHp>=3).
- Artifacts produced:
  - c:/git_repos/prompt2control/findings/17_per_hp_defect_localization.md (this report)

### Step 17.c Data and Fit

| nHp | nHpShc | nNonShc | nShc | Reduced diff |
|---|---|---|---|---:|
| 3 | 0 | 3 | 0 | -30 |
| 2 | 0 | 2 | 0 | -16 |
| 3 | 1 | 2 | 1 | -12 |
| 2 | 1 | 1 | 1 | 0 (Hybrid passes) |

## Step 17.d Findings
- File(s) inspected:
  - c:/buildings_library/modelica-buildings/Buildings/Templates/Plants/Controls/HeatPumps/AirToWater.mo
  - c:/buildings_library/modelica-buildings/Buildings/Templates/Plants/HeatPumps/Validation/AirToWater.mo
  - c:/git_repos/prompt2control/findings/15_codegen_AirToWater.md
  - c:/git_repos/prompt2control/findings/15_extends_AirToWater.md
- Key observations:
  - Declarations gated by not have_HpShc:
    - staMat[nSta,nHpTot], con, booScaRep(nout=nHpTot), pasPumHeaWatPri(nout=nPumHeaWatPriTot), ctlFloMin(if is_priOnl and not have_HpShc)
  - Declarations gated by have_HpShc:
    - ctlPlaHyb, or6, or7, or3, SHC-only input/output arrays (u1HpShc_actual, y1HpShc, y1PumHeaWatPriShc, y1PumChiWatPriShc, yMod, THeaWatSupSetHpShc, TChiWatSupSetHpShc)
  - Always-active arrays sized by nHpTot and interacting with both branches include or1, or2, andHeaEna, andCooEna, notCooMod, seqEve[nHpTot], avaEquHeaCoo[nHpTot], y1HeaPre[nHpTot], y1HpPre[nHpTot], and multiple staging-related blocks with nEqu=nHpTot.
  - In failing validation AirToWater, key modifiers are nHp=3 and cfg(nHpShc=0), which selects not have_HpShc branch globally.
- Hypotheses generated/refuted:
  - Refuted: missing top-level fallback on the known or1/or2 paths (already paired).
  - Generated: unique candidate is branch interaction where non-SHC source blocks constrain always-active nHpTot arrays differently from SHC branch internals, producing excess equations only in certain cardinalities.
- Artifacts produced:
  - c:/git_repos/prompt2control/findings/17_per_hp_defect_localization.md (this report)

### Step 17.d Branch-Scoped Declaration Table

| Declaration | Guard | Cardinality driver | Eq contribution model (approx.) | (3,0) | (2,0) | (3,1) | (2,1) |
|---|---|---|---|---:|---:|---:|---:|
| ctlPlaHyb | have_HpShc | nHpTot | Internal HybridOperation topology | inactive | inactive | active | active |
| staMat | not have_HpShc | nSta*nHpTot | nSta*nHpTot | 9 | 6 | inactive | inactive |
| con | not have_HpShc | scalar | 1 | 1 | 1 | inactive | inactive |
| booScaRep | not have_HpShc | nHpTot | nHpTot | 3 | 2 | inactive | inactive |
| pasPumHeaWatPri | not have_HpShc | nPumHeaWatPriTot | nPumHeaWatPriTot | 3 | 2 | inactive | inactive |
| or6/or7/or3 and SHC I/O | have_HpShc | nHpTot / nHpShc | SHC-only branch wiring | inactive | inactive | active | active |

## Step 17.e Findings
- File(s) inspected:
  - c:/git_repos/prompt2control/findings/15_nhpshc_axis.md
  - c:/git_repos/prompt2control/findings/16_decomposition.md
  - c:/git_repos/prompt2control/findings/13_5_source_block_audit.md
  - c:/buildings_library/modelica-buildings/Buildings/Templates/Plants/Controls/HeatPumps/AirToWater.mo
- Key observations:
  - Diagnosis remains actionable and narrowed to non-SHC branch behavior in controller AirToWater.mo, with branch interaction effects not fully attributable to top-level missing connects.
  - SHC2/SHC3 empirical closure remains blocked by Dymola translator NotImplemented issue.
  - Defect report has been generated in a dedicated artifact file.
- Hypotheses generated/refuted:
  - Confirmed: report-ready root-cause scope (controller non-SHC branch interactions).
  - Open: exact nonlinear contributor form pending unblocked SHC2/SHC3 checks or symbolic simplification.
- Artifacts produced:
  - c:/git_repos/prompt2control/findings/18_defect_report.md
  - c:/git_repos/prompt2control/findings/17_per_hp_defect_localization.md

## Method Execution Artifacts
- generate_code_analysis_inputs_2 outputs:
  - c:/git_repos/prompt2control/findings/17_codegen_AirToWater_variables.md
  - c:/git_repos/prompt2control/findings/17_codegen_AirToWater_connections.txt
  - c:/git_repos/prompt2control/findings/17_codegen_AirToWater_internal_context.md
  - c:/git_repos/prompt2control/findings/17_codegen_HybridOperation_variables.md
  - c:/git_repos/prompt2control/findings/17_codegen_HybridOperation_connections.txt
  - c:/git_repos/prompt2control/findings/17_codegen_HybridOperation_internal_context.md
- get_extend_statements outputs:
  - c:/git_repos/prompt2control/findings/17_extends_AirToWater.md
  - c:/git_repos/prompt2control/findings/17_extends_HybridOperation.md
