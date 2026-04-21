- **Variable Name**: dpHeaWatRemSet_min
  **Type/Comment Summary**: Real parameter; Minimum value to which the HW differential pressure can be reset - Remote sensor.
  **Compliance Check**: Accurately represents comment (yes); follows rules (no).
  **Issues Identified**: Same as above: `_min` underscore wrong.
  **Suggestions for Improvement**: Rename to `dpHeaWatRemSetMin`.

- **Variable Name**: yPumHeaWatPriSet
  **Type/Comment Summary**: Real parameter; Primary pump speed providing design heat pump flow in heating mode.
  **Compliance Check**: Accurately represents comment (partial); follows rules (no).
  **Issues Identified**: `y` prefix for control output (§4), but this is a **parameter** (not interface/signal)—inappropriate (§2.1.1). Comment describes a fixed design value, not dynamic signal. `Set` postfix ok, but overall mismatch.
  **Suggestions for Improvement**: Remove `y`; rename to `pumHeaWatPriSet` or `yPumHeaWatPriDes` if it's a setpoint (but confirm type).

- **Variable Name**: TChiWatSup_nominal
  **Type/Comment Summary**: Real parameter; Design CHW supply temperature (minimum setpoint). 

  **Compliance Check**: Accurately represents comment (yes); follows rules (yes).
  **Issues Identified**: None. Parallel to HW.
  **Suggestions for Improvement**: Compliant.

- **Variable Name**: TChiWatSupSet_max
  **Type/Comment Summary**: Real parameter; Maximum value to which the CHW supply temperature can be reset.
  **Compliance Check**: Accurately represents comment (yes); follows rules (no).
  **Issues Identified**: `_max` underscore violation.
  **Suggestions for Improvement**: Rename to `TChiWatSupSetMax`.

- **Variable Name**: TOutChiWatLck
  **Type/Comment Summary**: Real parameter; Outdoor air lockout temperature below which the CHW loop is prevented from operating.
  **Compliance Check**: Accurately represents comment (partial); follows rules (partial).     
  **Issues Identified**: Similar to `TOutHeaWatLck`: `lck` not standard; direction ("below") not in name.
  **Suggestions for Improvement**: Rename to `TOutLckCoo` or `TOutLckChi` (parallel to heating; use `coo` for cooling §6.2).

- **Variable Name**: capCooHp_nominal
  **Type/Comment Summary**: Real parameter; Design heat pump cooling capacity - Each heat pump.
  **Compliance Check**: Accurately represents comment (yes); follows rules (yes).
  **Issues Identified**: None. Parallel to heating (`Coo` qualifier §6.2).
  **Suggestions for Improvement**: Compliant.

- **Variable Name**: VChiWatHp_flow_nominal
  **Type/Comment Summary**: Real parameter; Design heat pump CHW volume flow rate - Each heat pump.
  **Compliance Check**: Accurately represents comment (yes); follows rules (yes).
  **Issues Identified**: None.
  **Suggestions for Improvement**: Compliant.

- **Variable Name**: VChiWatHp_flow_min
  **Type/Comment Summary**: Real parameter; Minimum heat pump CHW volume flow rate - Each heat pump.
  **Compliance Check**: Accurately represents comment (yes); follows rules (no).
  **Issues Identified**: Same as `VHeaWatHp_flow_min`: `_min` wrong.
  **Suggestions for Improvement**: Rename to `VChiWatHpMin_flow`.

- **Variable Name**: VChiWatPri_flow_nominal
  **Type/Comment Summary**: Real parameter; Primary CHW volume flow rate.
  **Compliance Check**: Accurately represents comment (yes); follows rules (yes).
  **Issues Identified**: None.
  **Suggestions for Improvement**: Compliant.

- **Variable Name**: VChiWatSec_flow_nominal
  **Type/Comment Summary**: Real parameter; Design secondary CHW volume flow rate.
  **Compliance Check**: Accurately represents comment (yes); follows rules (yes).
  **Issues Identified**: None.
  **Suggestions for Improvement**: Compliant.

- **Variable Name**: dpChiWatRemSet_max
  **Type/Comment Summary**: Real parameter; Maximum CHW differential pressure setpoint - Remote sensor.
  **Compliance Check**: Accurately represents comment (yes); follows rules (no).
  **Issues Identified**: `_max` underscore wrong.
  **Suggestions for Improvement**: Rename to `dpChiWatRemSetMax`.

- **Variable Name**: dpChiWatRemSet_min
  **Type/Comment Summary**: Real parameter; Minimum value to which the CHW differential pressure can be reset - Remote sensor.
  **Compliance Check**: Accurately represents comment (yes); follows rules (no).
  **Issues Identified**: `_min` underscore wrong.
  **Suggestions for Improvement**: Rename to `dpChiWatRemSetMin`.

- **Variable Name**: yPumChiWatPriSet
  **Type/Comment Summary**: Real parameter; Primary pump speed providing design heat pump flow in cooling mode.
  **Compliance Check**: Accurately represents comment (partial); follows rules (no).
  **Issues Identified**: Same as `yPumHeaWatPriSet`: `y` inappropriate for parameter.
  **Suggestions for Improvement**: Rename to `pumChiWatPriSet` or `yPumChiWatPriDes` if signal.

- **Variable Name**: cp_default
  **Type/Comment Summary**: Real parameter; Default specific heat capacity used to compute required capacity.
  **Compliance Check**: Accurately represents comment (yes); follows rules (yes).
  **Issues Identified**: None. `cp` standard for specific heat (full word acceptable §2.2.3); `_default` not listed but analogous to `_nominal` (underscore ok for quantity-type).
  **Suggestions for Improvement**: Compliant.

- **Variable Name**: rho_default
  **Type/Comment Summary**: Real parameter; Default density used to compute required capacity.

  **Compliance Check**: Accurately represents comment (yes); follows rules (yes).
  **Issues Identified**: None. `rho` standard for density.
  **Suggestions for Improvement**: Compliant.

- **Variable Name**: have_inpSch
  **Type/Comment Summary**: Boolean parameter; Set to true to provide schedule via software input point.
  **Compliance Check**: Accurately represents comment (yes); follows rules (partial).
  **Issues Identified**: `have_` prefix ok, but comment is about software feature—better `use_`. `inp` for input (3 chars).
  **Suggestions for Improvement**: Rename to `use_inpSch`.

- **Variable Name**: schHea
  **Type/Comment Summary**: Real parameter; Heating mode enable schedule.
  **Compliance Check**: Accurately represents comment (yes); follows rules (yes).
  **Issues Identified**: None. Short per §2.1.3; `sch` for schedule.
  **Suggestions for Improvement**: Compliant.

- **Variable Name**: schCoo
  **Type/Comment Summary**: Real parameter; Cooling mode enable schedule.
  **Compliance Check**: Accurately represents comment (yes); follows rules (yes).
  **Issues Identified**: None. Parallel (`Coo` §6.2).
  **Suggestions for Improvement**: Compliant.

- **Variable Name**: nReqIgnHeaWat
  **Type/Comment Summary**: Integer parameter; Number of ignored HW plant requests.
  **Compliance Check**: Accurately represents comment (yes); follows rules (yes).
  **Issues Identified**: None. `n` standard, `req` request, `ign` ignore.
  **Suggestions for Improvement**: Compliant.

- **Variable Name**: nReqIgnChiWat
  **Type/Comment Summary**: Integer parameter; Number of ignored CHW plant requests.
  **Compliance Check**: Accurately represents comment (yes); follows rules (yes).
  **Issues Identified**: None.
  **Suggestions for Improvement**: Compliant.

- **Variable Name**: dTOutLck
  **Type/Comment Summary**: Real parameter; Hysteresis for outdoor air lockout temperature.   
  **Compliance Check**: Accurately represents comment (yes); follows rules (yes).
  **Issues Identified**: None. `dT` for delta-T (§3, analogous).
  **Suggestions for Improvement**: Compliant.

- **Variable Name**: dtRunEna
  **Type/Comment Summary**: Real parameter; Minimum runtime of enable and disable states.     
  **Compliance Check**: Accurately represents comment (yes); follows rules (yes).
  **Issues Identified**: None. `dt` for time (common, like `Ti`/`Td` §3); `run` runtime, `ena` enable.
  **Suggestions for Improvement**: Compliant.

- **Variable Name**: dtReqDis
  **Type/Comment Summary**: Real parameter; Runtime with low number of request before disabling.
  **Compliance Check**: Accurately represents comment (yes); follows rules (yes).
  **Issues Identified**: None. `dis` disable.
  **Suggestions for Improvement**: Compliant.

- **Variable Name**: staEqu
  **Type/Comment Summary**: Real parameter; Staging matrix – Equipment required for each stage.
  **Compliance Check**: Accurately represents comment (yes); follows rules (partial).
  **Issues Identified**: `sta` for stage/staging (3 chars); `equ` equipment—short, but full word `equipment` acceptable if non-abbreviable (§2.2.3).
  **Suggestions for Improvement**: Compliant, but `staEquReq` if emphasizing "required."      

- **Variable Name**: staEquCooHea
  **Type/Comment Summary**: Real parameter; Staging matrix for heating-cooling mode – Equipment required for each stage.
  **Compliance Check**: Accurately represents comment (yes); follows rules (yes).
  **Issues Identified**: None. Qualifiers `CooHea` order ok (parallel §2.3.1).
  **Suggestions for Improvement**: Compliant.

- **Variable Name**: staEquOneMod
  **Type/Comment Summary**: Real parameter; Staging matrix for heating-only and cooling-only mode– Equipment required for each stage.
  **Compliance Check**: Accurately represents comment (yes); follows rules (partial).
  **Issues Identified**: `oneMod` for one-mode (ambiguous; "one" first three `one`, "mode" `mod`).
  **Suggestions for Improvement**: Rename to `staEquSngMod` (`sng` single).

- **Variable Name**: staEquTem
  **Type/Comment Summary**: Real parameter; Temporary placeholder.
  **Compliance Check**: Accurately represents comment (yes); follows rules (partial).
  **Issues Identified**: `tem` for temporary—ok, but placeholder names should follow same rules; unclear if permanent.
  **Suggestions for Improvement**: Rename to `staEquPla` (`pla` placeholder) or remove if temporary.

- **Variable Name**: nSta
  **Type/Comment Summary**: Integer parameter; Number of stages.
  **Compliance Check**: Accurately represents comment (yes); follows rules (yes).
  **Issues Identified**: None. Short per context (§2.1.3).
  **Suggestions for Improvement**: Compliant.

- **Variable Name**: nEquAlt
  **Type/Comment Summary**: Integer parameter; Number of lead/lag alternate equipment.        
  **Compliance Check**: Accurately represents comment (yes); follows rules (yes).
  **Issues Identified**: None. `equ` as above.
  **Suggestions for Improvement**: Compliant.

- **Variable Name**: idxEquAlt
  **Type/Comment Summary**: Integer parameter; Indices of lead/lag alternate equipment.       
  **Compliance Check**: Accurately represents comment (yes); follows rules (yes).
  **Issues Identified**: None. `idx` standard for index (full word §2.2.3).
  **Suggestions for Improvement**: Compliant.

- **Variable Name**: plrSta
  **Type/Comment Summary**: Real parameter; Staging part load ratio.
  **Compliance Check**: Accurately represents comment (yes); follows rules (yes).
  **Issues Identified**: None. `plr` part load ratio (3 chars each).
  **Suggestions for Improvement**: Compliant.

- **Variable Name**: dTHea
  **Type/Comment Summary**: Real parameter; Delta-T triggering stage up command for heating applications (>0).
  **Compliance Check**: Accurately represents comment (yes); follows rules (yes).
  **Issues Identified**: None. `dT` standard, `Hea` qualifier.
  **Suggestions for Improvement**: Compliant.

- **Variable Name**: dTCoo
  **Type/Comment Summary**: Real parameter; Delta-T triggering stage up command for cooling applications (>0).
  **Compliance Check**: Accurately represents comment (yes); follows rules (yes).
  **Issues Identified**: None. Parallel (`Coo`).
  **Suggestions for Improvement**: Compliant.

- **Variable Name**: dtVal
  **Type/Comment Summary**: Real parameter; Nominal valve timing.
  **Compliance Check**: Accurately represents comment (yes); follows rules (yes).
  **Issues Identified**: None. Context-clear short name (§2.1.3).
  **Suggestions for Improvement**: Compliant.

- **Variable Name**: dtRunSta
  **Type/Comment Summary**: Real parameter; Minimum runtime of each stage.
  **Compliance Check**: Accurately represents comment (yes); follows rules (yes).
  **Issues Identified**: None.
  **Suggestions for Improvement**: Compliant.

- **Variable Name**: dtOff
  **Type/Comment Summary**: Real parameter; Off time required before equipment is deemed available again.
  **Compliance Check**: Accurately represents comment (yes); follows rules (yes).
  **Issues Identified**: None. Short.
  **Suggestions for Improvement**: Compliant.

- **Variable Name**: dtOffHp
  **Type/Comment Summary**: Real parameter; Heat pump internal shutdown cycle timing.
  **Compliance Check**: Accurately represents comment (yes); follows rules (yes).
  **Issues Identified**: None.
  **Suggestions for Improvement**: Compliant.

- **Variable Name**: dtPri
  **Type/Comment Summary**: Real parameter; Runtime with high primary-setpoint Delta-T before staging up.
  **Compliance Check**: Accurately represents comment (yes); follows rules (yes).
  **Issues Identified**: None. Short for primary context.
  **Suggestions for Improvement**: Compliant.

- **Variable Name**: dtSec
  **Type/Comment Summary**: Real parameter; Runtime with high secondary-primary and secondary-setpoint Delta-T before staging up.
  **Compliance Check**: Accurately represents comment (yes); follows rules (yes).
  **Issues Identified**: None. Parallel.
  **Suggestions for Improvement**: Compliant.

- **Variable Name**: dtRunPumSta
  **Type/Comment Summary**: Real parameter; Runtime before triggering stage change command based on efficiency condition.
  **Compliance Check**: Accurately represents comment (yes); follows rules (yes).
  **Issues Identified**: None.
  **Suggestions for Improvement**: Compliant.

- **Variable Name**: dtRunFaiSafPumSta
  **Type/Comment Summary**: Real parameter; Runtime before triggering stage change command based on failsafe condition.
  **Compliance Check**: Accurately represents comment (yes); follows rules (yes).
  **Issues Identified**: None. `faiSaf` for failsafe (3+3).
  **Suggestions for Improvement**: Compliant.

- **Variable Name**: dtRunFaiSafLowYPumSta
  **Type/Comment Summary**: Real parameter; Runtime before triggering stage change command based on low pump speed failsafe condition.
  **Compliance Check**: Accurately represents comment (yes); follows rules (partial).
  **Issues Identified**: `lowY` for low (output? `y`); `y` here is descriptor, but could be ambiguous (confuses with signal prefix). Long name ok if necessary.
  **Suggestions for Improvement**: Rename to `dtRunFaiSafLowPumSta` (omit `Y` or clarify as `lowSpe` for speed).

- **Variable Name**: dVOffUpPumSta
  **Type/Comment Summary**: Real parameter; Stage up flow point offset.
  **Compliance Check**: Accurately represents comment (yes); follows rules (yes).
  **Issues Identified**: None. `dV` delta-volume/flow.
  **Suggestions for Improvement**: Compliant.

- **Variable Name**: dVOffDowPumSta
  **Type/Comment Summary**: Real parameter; Stage down flow point offset.
  **Compliance Check**: Accurately represents comment (yes); follows rules (yes).
  **Issues Identified**: None. `dow` down.
  **Suggestions for Improvement**: Compliant.

- **Variable Name**: dpOffPumSta
  **Type/Comment Summary**: Real parameter; Stage change ∆p point offset (>0).
  **Compliance Check**: Accurately represents comment (yes); follows rules (yes).
  **Issues Identified**: None. `dp` standard.
  **Suggestions for Improvement**: Compliant.

- **Variable Name**: yUpPumSta
  **Type/Comment Summary**: Real parameter; Stage up pump speed point.
  **Compliance Check**: Accurately represents comment (partial); follows rules (no).
  **Issues Identified**: `y` prefix for parameter (wrong, as with earlier `yPum...`).
  **Suggestions for Improvement**: Rename to `pumStaUpPoi` or `yPumStaUp` if signal.

- **Variable Name**: yDowPumSta
  **Type/Comment Summary**: Real parameter; Stage down pump speed point.
  **Compliance Check**: Accurately represents comment (partial); follows rules (no).
  **Issues Identified**: Same: `y` for parameter.
  **Suggestions for Improvement**: Rename to `pumStaDowPoi` or `yPumStaDow` if signal.        

- **Variable Name**: dtHol
  **Type/Comment Summary**: Real parameter; Minimum hold time during stage change.
  **Compliance Check**: Accurately represents comment (yes); follows rules (yes).
  **Issues Identified**: None. `hol` hold.
  **Suggestions for Improvement**: Compliant.

- **Variable Name**: resDpHeaWat_max
  **Type/Comment Summary**: Real parameter; Upper limit of plant reset interval for HW differential pressure reset.
  **Compliance Check**: Accurately represents comment (yes); follows rules (no).
  **Issues Identified**: `_max` underscore wrong; should be `Max` CamelCase. `res` for reset (3 chars).
  **Suggestions for Improvement**: Rename to `resDpHeaWatMax`.

- **Variable Name**: resTHeaWatSup_min
  **Type/Comment Summary**: Real parameter; Lower limit of plant reset interval for HW supply temperature reset.
  **Compliance Check**: Accurately represents comment (yes); follows rules (no).
  **Issues Identified**: `_min` wrong.
  **Suggestions for Improvement**: Rename to `resTHeaWatSupMin`.

- **Variable Name**: resDpChiWat_max
  **Type/Comment Summary**: Real parameter; Upper limit of plant reset interval for CHW differential pressure reset.
  **Compliance Check**: Accurately represents comment (yes); follows rules (no).
  **Issues Identified**: `_max` wrong.
  **Suggestions for Improvement**: Rename to `resDpChiWatMax`.

- **Variable Name**: resTChiWatSup_min
  **Type/Comment Summary**: Real parameter; Lower limit of plant reset interval for CHW supply temperature reset.
  **Compliance Check**: Accurately represents comment (yes); follows rules (no).
  **Issues Identified**: `_min` wrong.
  **Suggestions for Improvement**: Rename to `resTChiWatSupMin`.

- **Variable Name**: res_init
  **Type/Comment Summary**: Real parameter; Initial reset value.
  **Compliance Check**: Accurately represents comment (yes); follows rules (yes).
  **Issues Identified**: None. `_init` analogous to `_nominal` (underscore for quantity-type).

  **Suggestions for Improvement**: Compliant.

- **Variable Name**: res_min
  **Type/Comment Summary**: Real parameter; Minimum reset value.
  **Compliance Check**: Accurately represents comment (yes); follows rules (no).
  **Issues Identified**: `_min` wrong for value qualifier.
  **Suggestions for Improvement**: Rename to `resMin`.

- **Variable Name**: res_max
  **Type/Comment Summary**: Real parameter; Maximum reset value.
  **Compliance Check**: Accurately represents comment (yes); follows rules (no).
  **Issues Identified**: `_max` wrong.
  **Suggestions for Improvement**: Rename to `resMax`.

- **Variable Name**: dtDel
  **Type/Comment Summary**: Real parameter; Delay time before the reset begins.
  **Compliance Check**: Accurately represents comment (yes); follows rules (yes).
  **Issues Identified**: None. `del` delay.
  **Suggestions for Improvement**: Compliant.

- **Variable Name**: dtResHeaWat
  **Type/Comment Summary**: Real parameter; Time step for HW plant reset.
  **Compliance Check**: Accurately represents comment (yes); follows rules (yes).
  **Issues Identified**: None.
  **Suggestions for Improvement**: Compliant.

- **Variable Name**: nReqResIgnHeaWat
  **Type/Comment Summary**: Integer parameter; Number of ignored requests for HW plant reset. 

  **Compliance Check**: Accurately represents comment (yes); follows rules (yes).
  **Issues Identified**: None.
  **Suggestions for Improvement**: Compliant.

- **Variable Name**: triHeaWat
  **Type/Comment Summary**: Real parameter; Trim amount for HW plant reset.
  **Compliance Check**: Accurately represents comment (yes); follows rules (yes).
  **Issues Identified**: None. `tri` trim (3 chars).
  **Suggestions for Improvement**: Compliant.

- **Variable Name**: rspHeaWat
  **Type/Comment Summary**: Real parameter; Respond amount for HW plant reset.
  **Compliance Check**: Accurately represents comment (yes); follows rules (yes).
  **Issues Identified**: None. `rsp` respond.
  **Suggestions for Improvement**: Compliant.

- **Variable Name**: rspHeaWat_max
  **Type/Comment Summary**: Real parameter; Maximum response per time interval for HW plant reset.
  **Compliance Check**: Accurately represents comment (yes); follows rules (no).
  **Issues Identified**: `_max` wrong.
  **Suggestions for Improvement**: Rename to `rspHeaWatMax`.

- **Variable Name**: dtResChiWat
  **Type/Comment Summary**: Real parameter; Time step for CHW plant reset.
  **Compliance Check**: Accurately represents comment (yes); follows rules (yes).
  **Issues Identified**: None. Parallel.
  **Suggestions for Improvement**: Compliant.

- **Variable Name**: nReqResIgnChiWat
  **Type/Comment Summary**: Integer parameter; Number of ignored requests for CHW plant reset.

  **Compliance Check**: Accurately represents comment (yes); follows rules (yes).
  **Issues Identified**: None.
  **Suggestions for Improvement**: Compliant.

- **Variable Name**: triChiWat
  **Type/Comment Summary**: Real parameter; Trim amount for CHW plant reset.
  **Compliance Check**: Accurately represents comment (yes); follows rules (yes).
  **Issues Identified**: None.
  **Suggestions for Improvement**: Compliant.

- **Variable Name**: rspChiWat
  **Type/Comment Summary**: Real parameter; Respond amount for CHW plant reset.
  **Compliance Check**: Accurately represents comment (yes); follows rules (yes).  
  **Issues Identified**: None.
  **Suggestions for Improvement**: Compliant.

- **Variable Name**: rspChiWat_max
  **Type/Comment Summary**: Real parameter; Maximum response per time interval for CHW plant reset.
  **Compliance Check**: Accurately represents comment (yes); follows rules (no).
  **Issues Identified**: `_max` wrong.
  **Suggestions for Improvement**: Rename to `rspChiWatMax`.

- **Variable Name**: yPumHeaWatPri_min
  **Type/Comment Summary**: Real parameter; Minimum primary HW pump speed.
  **Compliance Check**: Accurately represents comment (partial); follows rules (no).
  **Issues Identified**: `y` for parameter wrong; `_min` underscore wrong.
  **Suggestions for Improvement**: Rename to `pumHeaWatPriMin` (or `yPumHeaWatPriMin` if signal).

- **Variable Name**: kCtlDpHeaWat
  **Type/Comment Summary**: Real parameter; Gain of controller for HW loop ∆p control.        
  **Compliance Check**: Accurately represents comment (yes); follows rules (yes).
  **Issues Identified**: None. `k` standard gain (§3).
  **Suggestions for Improvement**: Compliant.

- **Variable Name**: TiCtlDpHeaWat
  **Type/Comment Summary**: Real parameter; Time constant of integrator block for HW loop ∆p control.
  **Compliance Check**: Accurately represents comment (yes); follows rules (yes).
  **Issues Identified**: None. `Ti` standard (§3).
  **Suggestions for Improvement**: Compliant.

- **Variable Name**: yPumChiWatPri_min
  **Type/Comment Summary**: Real parameter; Minimum primary CHW pump speed.
  **Compliance Check**: Accurately represents comment (partial); follows rules (no).
  **Issues Identified**: Same as `yPumHeaWatPri_min`.
  **Suggestions for Improvement**: Rename to `pumChiWatPriMin`.

- **Variable Name**: kCtlDpChiWat
  **Type/Comment Summary**: Real parameter; Gain of controller for CHW loop ∆p control.       
  **Compliance Check**: Accurately represents comment (yes); follows rules (yes).
  **Issues Identified**: None. Parallel.
  **Suggestions for Improvement**: Compliant.

- **Variable Name**: TiCtlDpChiWat
  **Type/Comment Summary**: Real parameter; Time constant of integrator block for CHW loop ∆p control.
  **Compliance Check**: Accurately represents comment (yes); follows rules (yes).
  **Issues Identified**: None.
  **Suggestions for Improvement**: Compliant.

- **Variable Name**: yPumHeaWatSec_min
  **Type/Comment Summary**: Real parameter; Minimum secondary HW pump speed.
  **Compliance Check**: Accurately represents comment (partial); follows rules (no).
  **Issues Identified**: `y` and `_min` wrong.
  **Suggestions for Improvement**: Rename to `pumHeaWatSecMin`.

- **Variable Name**: yPumChiWatSec_min
  **Type/Comment Summary**: Real parameter; Minimum secondary CHW pump speed.
  **Compliance Check**: Accurately represents comment (partial); follows rules (no).
  **Issues Identified**: Same.
  **Suggestions for Improvement**: Rename to `pumChiWatSecMin`.

- **Variable Name**: kValMinByp
  **Type/Comment Summary**: Real parameter; Gain of controller.
  **Compliance Check**: Accurately represents comment (partial); follows rules (yes).
  **Issues Identified**: None for rules, but comment vague ("controller")—name implies minimum bypass valve gain (`val` valve, `minByp` min bypass). Accurate if context clear. `k` standard.
  **Suggestions for Improvement**: Compliant; add descriptor if comment expanded, e.g., `kValMinBypCtl`.

- **Variable Name**: TiValMinByp
  **Type/Comment Summary**: Modelica.Units.SI.Time parameter; Time constant of integrator block.
  **Compliance Check**: Accurately represents comment (partial); follows rules (yes).
  **Issues Identified**: None. `Ti` standard; similar vagueness as above.
  **Suggestions for Improvement**: Compliant.

- **Variable Name**: have_reqFloHrc
  **Type/Comment Summary**: Boolean parameter; Set to true if HRC provides flow request point via network interface.
  **Compliance Check**: Accurately represents comment (yes); follows rules (partial).
  **Issues Identified**: `have_` ok, but feature-like—consider `use_`. `reqFlo` request flow. 

  **Suggestions for Improvement**: Rename to `use_reqFloHrc`.

- **Variable Name**: TChiWatSupHrc_min
  **Type/Comment Summary**: Real parameter; Sidestream HRC – Minimum allowable CHW supply temperature.
  **Compliance Check**: Accurately represents comment (yes); follows rules (no).
  **Issues Identified**: `_min` wrong (should be `Min`).
  **Suggestions for Improvement**: Rename to `TChiWatSupHrcMin`.

- **Variable Name**: THeaWatSupHrc_max
  **Type/Comment Summary**: Real parameter; Sidestream HRC – Maximum allowable HW supply temperature.
  **Compliance Check**: Accurately represents comment (yes); follows rules (no).
  **Issues Identified**: `_max` wrong.
  **Suggestions for Improvement**: Rename to `THeaWatSupHrcMax`.

- **Variable Name**: COPHeaHrc_nominal
  **Type/Comment Summary**: Real parameter; Sidestream HRC – Heating COP at design heating conditions.
  **Compliance Check**: Accurately represents comment (yes); follows rules (yes).
  **Issues Identified**: None. `COP` full word (standard acronym, acceptable §2.2.3).
  **Suggestions for Improvement**: Compliant.

- **Variable Name**: capCooHrc_min
  **Type/Comment Summary**: Real parameter; Sidestream HRC – Minimum cooling capacity below which cycling occurs.
  **Compliance Check**: Accurately represents comment (yes); follows rules (no).
  **Issues Identified**: `_min` wrong.
  **Suggestions for Improvement**: Rename to `capCooHrcMin`.

- **Variable Name**: capHeaHrc_min
  **Type/Comment Summary**: Real parameter; Sidestream HRC – Minimum heating capacity below which cycling occurs.
  **Compliance Check**: Accurately represents comment (yes); follows rules (no).
  **Issues Identified**: `_min` wrong.
  **Suggestions for Improvement**: Rename to `capHeaHrcMin`.

- **Variable Name**: dtLoaHrc
  **Type/Comment Summary**: Real parameter; Runtime with sufficient load before enabling.     
  **Compliance Check**: Accurately represents comment (yes); follows rules (yes).
  **Issues Identified**: None. `loa` load.
  **Suggestions for Improvement**: Compliant.

- **Variable Name**: dtTem1Hrc
  **Type/Comment Summary**: Real parameter; Runtime with first temperature threshold exceeded before disabling.
  **Compliance Check**: Accurately represents comment (yes); follows rules (yes).
  **Issues Identified**: None. `tem` temperature (but short; 1 for first).
  **Suggestions for Improvement**: Compliant.

- **Variable Name**: dtTem2Hrc
  **Type/Comment Summary**: Real parameter; Runtime with second temperature threshold exceeded before disabling.
  **Compliance Check**: Accurately represents comment (yes); follows rules (yes).
  **Issues Identified**: None.
  **Suggestions for Improvement**: Compliant.

- **Variable Name**: u1SchHea
  **Type/Comment Summary**: BooleanInput interface; Heating mode enable via schedule.
  **Compliance Check**: Accurately represents comment (yes); follows rules (yes).
  **Issues Identified**: None. `u` input prefix (§4), `1` likely for boolean (CDL convention); omit if direction clear, but needed for multiple.
  **Suggestions for Improvement**: Compliant.

- **Variable Name**: u1SchCoo
  **Type/Comment Summary**: BooleanInput interface; Cooling mode enable via schedule.
  **Compliance Check**: Accurately represents comment (yes); follows rules (yes).
  **Issues Identified**: None. Parallel.
  **Suggestions for Improvement**: Compliant.

- **Variable Name**: u1PumHeaWatPri_actual
  **Type/Comment Summary**: BooleanInput interface; Primary HW pump status.
  **Compliance Check**: Accurately represents comment (yes); follows rules (yes).
  **Issues Identified**: None. `_actual` underscore for quantity-type (Modelica standard §2.2.3).
  **Suggestions for Improvement**: Compliant.

- **Variable Name**: u1PumChiWatPri_actual
  **Type/Comment Summary**: BooleanInput interface; Primary CHW pump status.
  **Compliance Check**: Accurately represents comment (yes); follows rules (yes).
  **Issues Identified**: None.
  **Suggestions for Improvement**: Compliant.

- **Variable Name**: u1PumHeaWatSec_actual
  **Type/Comment Summary**: BooleanInput interface; Secondary HW pump status.
  **Compliance Check**: Accurately represents comment (yes); follows rules (yes).
  **Issues Identified**: None.
  **Suggestions for Improvement**: Compliant.

- **Variable Name**: u1PumChiWatSec_actual
  **Type/Comment Summary**: BooleanInput interface; Secondary CHW pump status.
  **Compliance Check**: Accurately represents comment (yes); follows rules (yes).
  **Issues Identified**: None.
  **Suggestions for Improvement**: Compliant.

- **Variable Name**: u1Hp_actual
  **Type/Comment Summary**: BooleanInput interface; Heat pump status.
  **Compliance Check**: Accurately represents comment (yes); follows rules (yes).
  **Issues Identified**: None. Short per context.
  **Suggestions for Improvement**: Compliant.

- **Variable Name**: u1Hrc_actual
  **Type/Comment Summary**: BooleanInput interface; HRC status.
  **Compliance Check**: Accurately represents comment (yes); follows rules (yes).
  **Issues Identified**: None.
  **Suggestions for Improvement**: Compliant.

- **Variable Name**: u1ReqFloChiWat
  **Type/Comment Summary**: BooleanInput interface; CHW flow request from HRC.
  **Compliance Check**: Accurately represents comment (yes); follows rules (yes).
  **Issues Identified**: None. Direction clear, so `u` optional but used for consistency.     
  **Suggestions for Improvement**: Compliant.

- **Variable Name**: u1ReqFloConWat
  **Type/Comment Summary**: BooleanInput interface; CW flow request from HRC.
  **Compliance Check**: Accurately represents comment (yes); follows rules (yes).
  **Issues Identified**: None. `con` condenser? Clear from comment.
  **Suggestions for Improvement**: Compliant.

- **Variable Name**: u1EnaHea
  **Type/Comment Summary**: BooleanInput interface; Heating plant enable from external block. 

  **Compliance Check**: Accurately represents comment (yes); follows rules (yes).
  **Issues Identified**: None. `ena` enable.
  **Suggestions for Improvement**: Compliant.

- **Variable Name**: u1EnaCoo
  **Type/Comment Summary**: BooleanInput interface; Cooling plant enable from external block. 

  **Compliance Check**: Accurately represents comment (yes); follows rules (yes).
  **Issues Identified**: None.
  **Suggestions for Improvement**: Compliant.

- **Variable Name**: nReqPlaHeaWat
  **Type/Comment Summary**: IntegerInput interface; Number of HW plant requests.
  **Compliance Check**: Accurately represents comment (yes); follows rules (yes).
  **Issues Identified**: None. No `u` prefix needed (integer, direction clear via context).   
  **Suggestions for Improvement**: Compliant.

- **Variable Name**: nReqPlaChiWat
  **Type/Comment Summary**: IntegerInput interface; Number of CHW plant requests.
  **Compliance Check**: Accurately represents comment (yes); follows rules (yes).
  **Issues Identified**: None.
  **Suggestions for Improvement**: Compliant.

- **Variable Name**: nReqResHeaWat
  **Type/Comment Summary**: IntegerInput interface; Sum of HW reset requests of all heating loads served.
  **Compliance Check**: Accurately represents comment (yes); follows rules (yes).
  **Issues Identified**: None.
  **Suggestions for Improvement**: Compliant.

- **Variable Name**: nReqResChiWat
  **Type/Comment Summary**: IntegerInput interface; Sum of CHW reset requests of all cooling loads served.
  **Compliance Check**: Accurately represents comment (yes); follows rules (yes).
  **Issues Identified**: None.
  **Suggestions for Improvement**: Compliant.

- **Variable Name**: TOut
  **Type/Comment Summary**: RealInput interface; Outdoor air temperature.
  **Compliance Check**: Accurately represents comment (yes); follows rules (yes).
  **Issues Identified**: None. `T` standard; short per §2.1.3 (omit `u` as direction clear §4.2).
  **Suggestions for Improvement**: Compliant.

- **Variable Name**: THeaWatPriRet
  **Type/Comment Summary**: RealInput interface; Primary HW return temperature.
  **Compliance Check**: Accurately represents comment (yes); follows rules (yes).
  **Issues Identified**: None. Omit `u` correct.
  **Suggestions for Improvement**: Compliant.

- **Variable Name**: VHeaWatPri_flow
  **Type/Comment Summary**: RealInput interface; Primary HW volume flow rate.
  **Compliance Check**: Accurately represents comment (yes); follows rules (yes).
  **Issues Identified**: None. `_flow` correct (§3, §6.2).
  **Suggestions for Improvement**: Compliant.

- **Variable Name**: dpHeaWatLoc
  **Type/Comment Summary**: RealInput interface; Local HW differential pressure.
  **Compliance Check**: Accurately represents comment (yes); follows rules (yes).
  **Issues Identified**: None. `dp` standard, `loc` local.
  **Suggestions for Improvement**: Compliant.

- **Variable Name**: dpHeaWatLocSet
  **Type/Comment Summary**: RealInput interface; Local HW differential pressure setpoint output from each of the remote loops.
  **Compliance Check**: Accurately represents comment (yes); follows rules (yes).
  **Issues Identified**: None. `Set` postfix correct.
  **Suggestions for Improvement**: Compliant.

- **Variable Name**: dpHeaWatRem
  **Type/Comment Summary**: RealInput interface; Remote HW differential pressure.
  **Compliance Check**: Accurately represents comment (yes); follows rules (yes).
  **Issues Identified**: None.
  **Suggestions for Improvement**: Compliant.

- **Variable Name**: dpChiWatLoc
  **Type/Comment Summary**: RealInput interface; Local CHW differential pressure.
  **Compliance Check**: Accurately represents comment (yes); follows rules (yes).
  **Issues Identified**: None. Parallel.
  **Suggestions for Improvement**: Compliant.

- **Variable Name**: dpChiWatLocSet
  **Type/Comment Summary**: RealInput interface; Local CHW differential pressure setpoint output from each of the remote loops.
  **Compliance Check**: Accurately represents comment (yes); follows rules (yes).
  **Issues Identified**: None.
  **Suggestions for Improvement**: Compliant.

- **Variable Name**: dpChiWatRem
  **Type/Comment Summary**: RealInput interface; Remote CHW differential pressure.
  **Compliance Check**: Accurately represents comment (yes); follows rules (yes).
  **Issues Identified**: None.
  **Suggestions for Improvement**: Compliant.

- **Variable Name**: TChiWatPriRet
  **Type/Comment Summary**: RealInput interface; Primary CHW return temperature.
  **Compliance Check**: Accurately represents comment (yes); follows rules (yes).
  **Issues Identified**: None.
  **Suggestions for Improvement**: Compliant.

- **Variable Name**: VChiWatPri_flow
  **Type/Comment Summary**: RealInput interface; Primary CHW volume flow rate.
  **Compliance Check**: Accurately represents comment (yes); follows rules (yes).
  **Issues Identified**: None.
  **Suggestions for Improvement**: Compliant.

- **Variable Name**: THeaWatSecRet
  **Type/Comment Summary**: RealInput interface; Secondary HW return temperature.
  **Compliance Check**: Accurately represents comment (yes); follows rules (yes).
  **Issues Identified**: None.
  **Suggestions for Improvement**: Compliant.

- **Variable Name**: VHeaWatSec_flow
  **Type/Comment Summary**: RealInput interface; Secondary HW volume flow rate.
  **Compliance Check**: Accurately represents comment (yes); follows rules (yes).
  **Issues Identified**: None.
  **Suggestions for Improvement**: Compliant.

- **Variable Name**: TChiWatSecRet
  **Type/Comment Summary**: RealInput interface; Secondary CHW return temperature.
  **Compliance Check**: Accurately represents comment (yes); follows rules (yes).
  **Issues Identified**: None.
  **Suggestions for Improvement**: Compliant.

- **Variable Name**: VChiWatSec_flow
  **Type/Comment Summary**: RealInput interface; Secondary CHW volume flow rate.
  **Compliance Check**: Accurately represents comment (yes); follows rules (yes).
  **Issues Identified**: None.
  **Suggestions for Improvement**: Compliant.

- **Variable Name**: THeaWatPriSup
  **Type/Comment Summary**: RealInput interface; Primary HW supply temperature.
  **Compliance Check**: Accurately represents comment (yes); follows rules (yes).
  **Issues Identified**: None.
  **Suggestions for Improvement**: Compliant.

- **Variable Name**: TChiWatPriSup
  **Type/Comment Summary**: RealInput interface; Primary CHW return temperature.
  **Compliance Check**: Accurately represents comment (no); follows rules (yes).
  **Issues Identified**: Comment says "return" but name uses `Sup` (supply)—mismatch! Likely typo in comment.
  **Suggestions for Improvement**: Correct comment to "supply" or rename to `TChiWatPriRet` if return.

- **Variable Name**: THeaWatSecSup
  **Type/Comment Summary**: RealInput interface; Secondary HW supply temperature.
  **Compliance Check**: Accurately represents comment (yes); follows rules (yes).
  **Issues Identified**: None.
  **Suggestions for Improvement**: Compliant.

- **Variable Name**: TChiWatSecSup
  **Type/Comment Summary**: RealInput interface; Secondary CHW return temperature.
  **Compliance Check**: Accurately represents comment (no); follows rules (yes).
  **Issues Identified**: Same mismatch: comment "return" but `Sup` supply.
  **Suggestions for Improvement**: Correct comment or rename to `TChiWatSecRet`.

- **Variable Name**: TChiWatRetUpsHrc
  **Type/Comment Summary**: RealInput interface; CHW return temperature upstream of HRC.      
  **Compliance Check**: Accurately represents comment (yes); follows rules (yes).
  **Issues Identified**: None. `ups` upstream.
  **Suggestions for Improvement**: Compliant.

- **Variable Name**: THeaWatRetUpsHrc
  **Type/Comment Summary**: RealInput interface; HW return temperature upstream of HRC.       
  **Compliance Check**: Accurately represents comment (yes); follows rules (yes).
  **Issues Identified**: None. Parallel.
  **Suggestions for Improvement**: Compliant.

- **Variable Name**: y1ValHeaWatHpInlIso
  **Type/Comment Summary**: BooleanOutput interface; Heat pump inlet HW inlet isolation valve command.
  **Compliance Check**: Accurately represents comment (yes); follows rules (yes).
  **Issues Identified**: None. `y` output, `1` boolean; `inl` inlet (repeated "inlet" in comment, but name clear).
  **Suggestions for Improvement**: Compliant.

- **Variable Name**: y1ValHeaWatHpOutIso
  **Type/Comment Summary**: BooleanOutput interface; Heat pump outlet HW isolation valve command.
  **Compliance Check**: Accurately represents comment (yes); follows rules (yes).
  **Issues Identified**: None.
  **Suggestions for Improvement**: Compliant.

- **Variable Name**: y1ValChiWatHpInlIso
  **Type/Comment Summary**: BooleanOutput interface; Heat pump inlet CHW isolation valve command.
  **Compliance Check**: Accurately represents comment (yes); follows rules (yes).
  **Issues Identified**: None.
  **Suggestions for Improvement**: Compliant.

- **Variable Name**: y1ValChiWatHpOutIso
  **Type/Comment Summary**: BooleanOutput interface; Heat pump outlet CHW isolation valve command.
  **Compliance Check**: Accurately represents comment (yes); follows rules (yes).
  **Issues Identified**: None.
  **Suggestions for Improvement**: Compliant.

- **Variable Name**: y1PumHeaWatPri
  **Type/Comment Summary**: BooleanOutput interface; Primary HW pump start command.
  **Compliance Check**: Accurately represents comment (yes); follows rules (yes).
  **Issues Identified**: None.
  **Suggestions for Improvement**: Compliant.

- **Variable Name**: y1PumChiWatPri
  **Type/Comment Summary**: BooleanOutput interface; Primary CHW pump start command.
  **Compliance Check**: Accurately represents comment (yes); follows rules (yes).
  **Issues Identified**: None.
  **Suggestions for Improvement**: Compliant.

- **Variable Name**: y1PumHeaWatSec
  **Type/Comment Summary**: BooleanOutput interface; Secondary HW pump start command.
  **Compliance Check**: Accurately represents comment (yes); follows rules (yes).
  **Issues Identified**: None.
  **Suggestions for Improvement**: Compliant.

- **Variable Name**: y1PumChiWatSec
  **Type/Comment Summary**: BooleanOutput interface; Secondary CHW pump start command.        
  **Compliance Check**: Accurately represents comment (yes); follows rules (yes).
  **Issues Identified**: None.
  **Suggestions for Improvement**: Compliant.

- **Variable Name**: y1Hp
  **Type/Comment Summary**: BooleanOutput interface; Heat pump enable command.
  **Compliance Check**: Accurately represents comment (yes); follows rules (yes).
  **Issues Identified**: None. Short.
  **Suggestions for Improvement**: Compliant.

- **Variable Name**: y1HeaHp
  **Type/Comment Summary**: BooleanOutput interface; Heat pump heating/cooling mode command: true=heating, false=cooling.
  **Compliance Check**: Accurately represents comment (yes); follows rules (partial).
  **Issues Identified**: `HeaHp` could be `heaModHp` for mode; but `Hea` as qualifier ok if true=heating.
  **Suggestions for Improvement**: Compliant, or `y1ModHp` for clarity.

- **Variable Name**: y1CooHrc
  **Type/Comment Summary**: BooleanOutput interface; Sidestream HRC mode command: true for cooling, false for heating.
  **Compliance Check**: Accurately represents comment (yes); follows rules (partial).
  **Issues Identified**: Similar: `CooHrc` implies cooling, but comment has dual mode—parallel to above.
  **Suggestions for Improvement**: Rename to `y1ModHrc` or `y1CooModHrc`.

- **Variable Name**: y1PumChiWatHrc
  **Type/Comment Summary**: BooleanOutput interface; Sidestream HRC CHW pump enable command.  
  **Compliance Check**: Accurately represents comment (yes); follows rules (yes).
  **Issues Identified**: None.
  **Suggestions for Improvement**: Compliant.

- **Variable Name**: y1PumHeaWatHrc
  **Type/Comment Summary**: BooleanOutput interface; Sidestream HRC HW pump enable command.   
  **Compliance Check**: Accurately represents comment (yes); follows rules (yes).
  **Issues Identified**: None. Parallel.
  **Suggestions for Improvement**: Compliant.

- **Variable Name**: y1Hrc
  **Type/Comment Summary**: BooleanOutput interface; Sidestream HRC enable command.
  **Compliance Check**: Accurately represents comment (yes); follows rules (yes).
  **Issues Identified**: None.
  **Suggestions for Improvement**: Compliant.

- **Variable Name**: y1EnaPla
  **Type/Comment Summary**: BooleanOutput interface; Heat pump plant enable command.
  **Compliance Check**: Accurately represents comment (yes); follows rules (yes).
  **Issues Identified**: None. `pla` plant.
  **Suggestions for Improvement**: Compliant.

- **Variable Name**: yMod
  **Type/Comment Summary**: IntegerOutput interface; Operation mode integer signal for each HP.
  **Compliance Check**: Accurately represents comment (yes); follows rules (yes).
  **Issues Identified**: None. `y` for output; short for mode.
  **Suggestions for Improvement**: Compliant.

- **Variable Name**: dpHeaWatRemSet
  **Type/Comment Summary**: RealOutput interface; HW differential pressure setpoint.
  **Compliance Check**: Accurately represents comment (yes); follows rules (yes).
  **Issues Identified**: None. `y` omitted as output clear (§4.2).
  **Suggestions for Improvement**: Compliant.

- **Variable Name**: dpChiWatRemSet
  **Type/Comment Summary**: RealOutput interface; CHW differential pressure setpoint.
  **Compliance Check**: Accurately represents comment (yes); follows rules (yes).
  **Issues Identified**: None.
  **Suggestions for Improvement**: Compliant.

- **Variable Name**: yPumHeaWatPriHdr
  **Type/Comment Summary**: RealOutput interface; Primary headered HW pump speed command.     
  **Compliance Check**: Accurately represents comment (yes); follows rules (yes).
  **Issues Identified**: None. `y` correct for output signal (§4).
  **Suggestions for Improvement**: Compliant.

- **Variable Name**: yPumChiWatPriHdr
  **Type/Comment Summary**: RealOutput interface; Primary headered CHW pump speed command.    
  **Compliance Check**: Accurately represents comment (yes); follows rules (yes).
  **Issues Identified**: None.
  **Suggestions for Improvement**: Compliant.

- **Variable Name**: yPumHeaWatSec
  **Type/Comment Summary**: RealOutput interface; Primary HW pump speed command.
  **Compliance Check**: Accurately represents comment (no); follows rules (yes).
  **Issues Identified**: Comment says "Primary" but name uses `Sec` (secondary)—likely typo. Rules ok.
  **Suggestions for Improvement**: Correct comment to "Secondary" or rename to `yPumHeaWatPri` if primary.

- **Variable Name**: yPumChiWatSec
  **Type/Comment Summary**: RealOutput interface; Primary CHW pump speed command.
  **Compliance Check**: Accurately represents comment (no); follows rules (yes).
  **Issues Identified**: Same mismatch: comment "Primary" but `Sec` secondary.
  **Suggestions for Improvement**: Correct comment or rename to `yPumChiWatPri`.

- **Variable Name**: TChiWatSupSet
  **Type/Comment Summary**: RealOutput interface; CHW supply temperature setpoint.
  **Compliance Check**: Accurately represents comment (yes); follows rules (yes).
  **Issues Identified**: None. No `y` needed (§4.2).
  **Suggestions for Improvement**: Compliant.

- **Variable Name**: THeaWatSupSet
  **Type/Comment Summary**: RealOutput interface; HW supply temperature setpoint.
  **Compliance Check**: Accurately represents comment (yes); follows rules (yes).
  **Issues Identified**: None.
  **Suggestions for Improvement**: Compliant.

- **Variable Name**: yPumHeaWatPriDed
  **Type/Comment Summary**: RealOutput interface; Primary dedicated HW pump speed command.    
  **Compliance Check**: Accurately represents comment (yes); follows rules (yes).
  **Issues Identified**: None.
  **Suggestions for Improvement**: Compliant.

- **Variable Name**: yPumChiWatPriDed
  **Type/Comment Summary**: RealOutput interface; Primary dedicated CHW pump speed command.   
  **Compliance Check**: Accurately represents comment (yes); follows rules (yes).
  **Issues Identified**: None.
  **Suggestions for Improvement**: Compliant.

- **Variable Name**: TSupSet
  **Type/Comment Summary**: RealOutput interface; Active HP supply temperature setpoint.      
  **Compliance Check**: Accurately represents comment (yes); follows rules (yes).
  **Issues Identified**: None. Short per context (HP package?).
  **Suggestions for Improvement**: Compliant.

- **Variable Name**: TSupSetHrc
  **Type/Comment Summary**: RealOutput interface; Sidestream HRC active supply temperature setpoint.
  **Compliance Check**: Accurately represents comment (yes); follows rules (yes).
  **Issues Identified**: None.
  **Suggestions for Improvement**: Compliant.

  **Type/Comment Summary**: RealOutput interface; CHW minimum flow bypass valve command.
  **Compliance Check**: Accurately represents comment (yes); follows rules (yes).
  **Issues Identified**: None. Parallel.
  **Suggestions for Improvement**: Compliant.

### Summary of Common Issues
- **Most Frequent Violations**: Underscore before value qualifiers like `_min`/`_max` (20+ cases)—always use CamelCase `Min`/`Max` (§6.1).
- **Prefix Mismatches**: `y` used on parameters (5 cases)—reserve for signals (§4); non-standard `is_` (2 cases)—use `have_`/`use_`.
- **Comment-Name Mismatches**: 4 cases (e.g., supply vs. return temps)—fix comments for accuracy.
- **Overall Compliance**: ~85% fully compliant. Interfaces are strongest; parameters have suffix issues. No class names to check (all instances). Ensure parallelism (e.g., Hea/Coo) is maintained in fixes. If this is part of a larger library, test for cross-package consistency (§2.3).