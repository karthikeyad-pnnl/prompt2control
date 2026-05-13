# AI Agent Investigation Checklist: `Buildings.Templates.Plants.HeatPumps.Validation.AirToWater`

## Mission

Diagnose the root cause of a \"model is not well-posed\" error (equation count exceeds unknown count by 30) in the `Buildings.Templates.Plants.HeatPumps.Validation.AirToWater` model, and propose a minimal, targeted fix.

## Available Capabilities

- You will only use the skills defined within this workspace, and no other terminal commands.

## Known Facts from Initial Error Log

- Tool reports: `The model has the same number of unknowns and equations: 18551` but `the difference could be reduced to -30` (30 more equations than unknowns).
- Numerous warnings about parameters with `enable=false` that only have `start` values.
- Suspicious parameters flagged:
  - Water-source HP parameters appearing in an air-to-water validation: `datAll.pla.hp.dpSouWwHeaHp_nominal`, `mSouWwCooHp_flow_nominal`, `mSouWwHeaHp_flow_nominal`.
  - Controller conditional inputs with `u_internal` start values: `TChiWatRet`, `THeaWatRet`, `V*Loa_flow`, `V*Sta_flow`, `idxStaCoo/Hea.pas[1..3]`, `staPum*WatSec.nPumHdrDp.pas[1..3]`.
  - Secondary-pump staging parameters defaulted: `staEquSinMod`, `staEquDouMod`, `have_valInlIso`, `have_valOutIso`.
  - Distribution type flagged: `pla.typDis_select2(start = Constant1Variable2)`.

## Output Format Requirement

For every step below, record findings in the form:

```
## Step N Findings
- File(s) inspected: <paths>
- Key observations: <bullet list>
- Hypotheses generated/refuted: <bullet list>
- Artifacts produced: <log files, extracted snippets>
```

At the end, produce a **Root Cause Report** and a **Proposed Fix** section (templates provided below).

---

## Step 0 — Environment Capture

- [ ] Record the Buildings library version: read `Buildings/package.mo` for `version` annotation and, if available, the Git commit SHA.
- [ ] Record the Modelica Standard Library version in use.
- [ ] Record which tool will be used for translation (Dymola and/or OpenModelica) and their versions.
- [ ] Save this information to `findings/00_environment.md`.

**Stop condition:** Environment info recorded. Proceed regardless of outcome.

---

## Step 1 — Baseline Reproduction

- [ ] Translate `Buildings.Templates.Plants.HeatPumps.Validation.AirToWater` in Dymola using `checkModel`.
- [ ] Save the full translation log to `logs/01_dymola_check.log`.
- [ ] Extract and save to `findings/01_baseline.md`:
  - The exact \"unknowns\" and \"equations\" counts.
  - The final \"difference could be reduced to\" value.
  - The complete list of parameters flagged with `enable=false` and only start values.
  - Any error or warning referencing `connect`, `conditional`, `enable`, or `size mismatch`.
- [ ] If OpenModelica is available, also run `checkModel` there and save to `logs/01_om_check.log`. Note any differences in diagnostic messages.

**Stop condition:** Baseline reproduced and the −30 imbalance confirmed. If the model now checks cleanly, stop and report.

---

## Step 2 — Inspect the Validation Model

- [ ] Open `Buildings/Templates/Plants/HeatPumps/Validation/AirToWater.mo`.
- [ ] Extract and record in `findings/02_validation_model.md`:
  - The full `pla` instantiation including every redeclaration and parameter override.
  - The full `datAll` record contents.
  - Wiring of `loaHea`, `loaCoo`, `ratLoa` (note array sizes of `ratLoa.table` and `ratLoa.offset`).
  - Explicit values (or absence thereof) for:
    - `nHp`
    - `typDis` (including whether it is set explicitly or via `_select2` dropdown)
    - `typArrPumChiWatPri`, `typArrPumHeaWatPri`
    - `typArrPumChiWatSec`, `typArrPumHeaWatSec`
    - `have_pumChiWatPriDed`, `have_pumHeaWatPriDed`
    - `have_pumChiWatSec`, `have_pumHeaWatSec`
- [ ] Flag any parameter in the flagged-warnings list from Step 1 that the validation model does **not** explicitly set.

**Stop condition:** Full parameter override list for `pla` captured.

---

## Step 3 — Inspect the Plant Template

- [ ] Open the class referenced by the `pla` instantiation (typically `Buildings/Templates/Plants/HeatPumps/AirToWater.mo`).
- [ ] Locate the controller subcomponent (`pla.ctl`) and its inner G36 block (`pla.ctl.ctl`). Record their full type paths.
- [ ] Extract and record in `findings/03_plant_template.md`:
  - How `pla.ctl.ctl` is instantiated: every `have_*` boolean passed in and its source expression.
  - For each conditional input flagged in Step 1 (e.g. `TChiWatRet`, `V*Loa_flow`, `idxSta*.pas`, `nPumHdrDp.pas`):
    - Is there a `connect()` statement for it? Yes/No.
    - If yes, what is the `if` guard (if any) on that `connect()`?
    - Is that guard the **same** expression as the `enable` on the input in the controller? (See Step 4 for the `enable` side.)
- [ ] Record how `staEqu`, `staEquSinMod`, `staEquDouMod` are propagated from `dat` into `ctl`.

**Stop condition:** Every flagged `u_internal` input has been traced to a `connect()` statement or confirmed to have none.

---

## Step 4 — Inspect the G36 Controller Interface

- [ ] From the type path recorded in Step 3, open the G36 plant controller class.
- [ ] For each conditional input listed below, record:
  - Its declaration (`parameter`/`input`, type, dimensions).
  - Its `enable=` expression (or the `if ... then ... else` guard on its declaration).
- [ ] Required input list:
  - `TChiWatRet`, `THeaWatRet`
  - `VChiWatLoa_flow`, `VChiWatSta_flow`
  - `VHeaWatLoa_flow`, `VHeaWatSta_flow`
  - `idxStaCoo.pas[1..3]`, `idxStaHea.pas[1..3]`
  - `staPumChiWatSec.nPumHdrDp.pas[1..3]`
  - `staPumHeaWatSec.nPumHdrDp.pas[1..3]`
- [ ] Also record the `enable`/default of:
  - `staEquSinMod`, `staEquDouMod` (note that defaults are zero matrices).
  - `have_valInlIso`, `have_valOutIso` in both `staPumChiWatSec` and `staPumHeaWatSec`.
- [ ] Save to `findings/04_controller_interface.md`.

**Stop condition:** All conditional input `enable` expressions captured.

---

## Step 5 — Cross-Check Guards (Critical Step)

- [ ] Build a table in `findings/05_guard_consistency.md` with columns:

  | Input | Controller-side `enable` | Template `connect()` guard | Match? | Evaluates to (true/false) |
  |-------|--------------------------|----------------------------|--------|---------------------------|

- [ ] Fill one row per flagged input using data from Steps 3 and 4.
- [ ] For the \"Evaluates to\" column, substitute the resolved values from Step 2 (and Step 6 once available).
- [ ] **Flag any row where `Match? = No`**, or where the controller enables an input but the template provides no connection. These are prime root-cause candidates.

**Stop condition:** Table complete. Candidate mismatches flagged.

---

## Step 6 — Resolved Parameter Dump

- [ ] Translate the model in Dymola with parameter evaluation enabled (e.g. `Advanced.PrintFailureToDifferentiate = true` and check the parameter log, or use the `dsin.txt` dump).
- [ ] Alternatively, instantiate a dummy test model in OpenModelica and use `getParameterValue` / translation log.
- [ ] Extract and record in `findings/06_resolved_params.md`:
  - `pla.nHp`
  - `pla.typDis` (as enum value)
  - `pla.typArrPumChiWatPri`, `pla.typArrPumHeaWatPri`, `pla.typArrPumChiWatSec`, `pla.typArrPumHeaWatSec`
  - All `pla.have_*` flags: `have_pumChiWatPriDed`, `have_pumHeaWatPriDed`, `have_pumChiWatSec`, `have_pumHeaWatSec`, `have_senDpChiWatRemWir`, `have_senDpHeaWatRemWir`, `have_senVChiWatSec_flow`, `have_senVHeaWatSec_flow`, `have_valChiWatMinByp`, `have_hrc`
  - `pla.ctl.ctl.nPumChiWatSec`, `nPumHeaWatSec`, `nSenDpChiWatRem`, `nSenDpHeaWatRem`
  - `pla.ctl.ctl.staPumChiWatSec.have_valInlIso`, `have_valOutIso`, `nEquAlt`, `nSta`
  - `pla.ctl.ctl.staPumHeaWatSec.have_valInlIso`, `have_valOutIso`, `nEquAlt`, `nSta`
  - `pla.ctl.staEqu` (full numeric matrix)
  - Every `*.nin` / `*.nout` referenced in the error log's equation-count expression

**Stop condition:** All values resolved to concrete numbers/booleans/enums.

---

## Step 7 — Inspect the Heat Pump Data Record

- [ ] Locate the record type of `datAll.pla.hp` (typically `Buildings/Templates/Plants/HeatPumps/Components/Data/HeatPumpGroup.mo` or similar).
- [ ] Record in `findings/07_data_record.md`:
  - The declaration and `enable=` expression for `dpSouWwHeaHp_nominal`, `mSouWwCooHp_flow_nominal`, `mSouWwHeaHp_flow_nominal`.
  - The discriminator used (likely `typ == Buildings.Templates.Components.Types.HeatPump.WaterToWater` or similar).
  - Evaluate whether the discriminator correctly excludes these fields when `typ` indicates an air-to-water unit.
- [ ] Flag whether this is a **warning-only issue** (record bug but non-fatal) or potentially contributes to the equation imbalance.

**Stop condition:** Record behavior characterized.

---

## Step 8 — Arithmetic Reconciliation

- [ ] Using resolved values from Step 6, evaluate both sides of the symbolic cardinality expression reported by Dymola:
  - **Unknowns formula:** `18470 + 16 * countTrue(...) + <nin/nout/size terms>`
  - **Equations formula:** `18278 + <s