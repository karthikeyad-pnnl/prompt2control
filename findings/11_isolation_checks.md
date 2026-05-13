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