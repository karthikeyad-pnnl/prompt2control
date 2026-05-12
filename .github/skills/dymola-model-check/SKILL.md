---
name: dymola-model-check
description: "Create a Dymola application instance and run checkModel for a Modelica class. Use when users ask for Dymola model check validation on existing classes."
---

# Dymola Model Check Skill

Use this skill to launch Dymola and run `checkModel` for an existing Modelica class.

If you need strict pedantic translation (instead of `checkModel`), use `dymola-pedantic` with:

```powershell
python dymola_pedantic_check.py --class-path <ModelicaClassPath>
```

## Prerequisites

- Dymola installed and accessible:
  - Either on `PATH` as `dymola.exe`
  - Or set `DYMOLA_EXE` to full executable path
- Buildings library available (default from `PROMPT2CONTROL_LIB_ROOT`)

Optional environment variables:

```powershell
$env:DYMOLA_EXE="C:/Program Files/Dymola 202x/bin64/dymola.exe"
$env:PROMPT2CONTROL_LIB_ROOT="c:/buildings_library/modelica-buildings"
$env:PROMPT2CONTROL_DYMOLA_MODEL_CHECK_OUTPUT_DIR="c:/git_repos/prompt2control/agent_outputs/dymola_model_check"
```

## Command

Run from repository root:

```powershell
python dymola_model_check.py --class-path <ModelicaClassPath>
```

Example:

```powershell
python dymola_model_check.py --class-path Buildings.Templates.Plants.Controls.StagingRotation.EquipmentEnable
```

## Outputs

The command writes artifacts to output directory:

- `model_check.mos`
- `dymola_model_check_stdout.log`
- `dymola_model_check_stderr.log`
- `dymola_model_check.log` (when produced by Dymola)

## Notes

- Non-zero exit code indicates launch/check issues.
- Review stdout/stderr logs for diagnostics.
