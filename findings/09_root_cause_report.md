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