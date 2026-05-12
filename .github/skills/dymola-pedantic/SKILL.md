---
name: dymola-pedantic
description: "Create a Dymola application instance and run pedantic translation checks for a Modelica class. Use when users ask to validate strict Modelica translation in Dymola."
---

# Dymola Pedantic Translation Skill

Use this skill to launch Dymola and perform a pedantic translation of a Modelica class.

If you need `checkModel` validation (instead of pedantic translation), use `dymola-model-check` with:

```powershell
python dymola_model_check.py --class-path <ModelicaClassPath>
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
$env:PROMPT2CONTROL_DYMOLA_OUTPUT_DIR="c:/git_repos/prompt2control/agent_outputs/dymola_pedantic"
```

## Command

Run from repository root:

```powershell
python dymola_pedantic_check.py --class-path <ModelicaClassPath>
```

Example:

```powershell
python dymola_pedantic_check.py --class-path Buildings.Templates.Plants.Controls.StagingRotation.EquipmentEnable
```

## Outputs

The command writes artifacts to output directory:

- `pedantic_translate.mos`
- `dymola_stdout.log`
- `dymola_stderr.log`
- `dymola_translation.log` (when produced by Dymola)

## Notes

- Non-zero exit code indicates launch/translation issues.
- Review `dymola_stdout.log` and `dymola_stderr.log` for diagnostics.
