---
name: modulecheck
description: "Run ModuleCheck workflows for Modelica classes: generate English documentation, review annotation documentation quality, generate pseudo code, analyze CDL variable naming compliance, rename components with OpenModelica, and extract extends data. Use when users ask to evaluate or document a Buildings model class. For Dymola pedantic translation checks, use dymola-pedantic. For Dymola checkModel validation, use dymola-model-check."
---

# ModuleCheck Skill

Use this skill to run the Python CLI wrapper around `ModuleCheck` in `module_check.py`.

For Dymola pedantic translation checks, route to `dymola-pedantic` and use:

```powershell
python dymola_pedantic_check.py --class-path <ModelicaClassPath>
```

For Dymola model checks (`checkModel`), route to `dymola-model-check` and use:

```powershell
python dymola_model_check.py --class-path <ModelicaClassPath>
```

## Prerequisites

- Python environment with dependencies installed (`pip install -r requirements.txt`).
- OpenModelica available.
- Environment variables configured:

```powershell
$env:PROMPT2CONTROL_API_KEY="<your_key>"
$env:PROMPT2CONTROL_BASE_URL="https://ai-incubator-api.pnnl.gov"
$env:PROMPT2CONTROL_MODEL="claude-sonnet-4-6-birthright"
$env:PROMPT2CONTROL_LIB_ROOT="c:/buildings_library/modelica-buildings"
$env:PROMPT2CONTROL_OUTPUT_DIR="c:/git_repos/prompt2control/agent_outputs"
```

## Commands

Run from repository root.

### 1) Generate English documentation

```powershell
python modulecheck_agent.py generate-docs --class-path <ModelicaClassPath>
```

### 2) Review existing model documentation

```powershell
python modulecheck_agent.py review-docs --class-path <ModelicaClassPath>
```

### 3) Generate pseudo code

```powershell
python modulecheck_agent.py pseudo-code --class-path <ModelicaClassPath>
```

### 4) Analyze variable names against CDL naming rules

```powershell
python modulecheck_agent.py analyze-names --class-path <ModelicaClassPath> --complete-set
```

### 5) Extract Extend Statements

Extract extend statements from a Modelica model to analyze inheritance and redeclarations. This method parses the model file and generates a markdown table summarizing the base classes, redeclared components, and other assignments.

#### Command

Run from repository root:

```powershell
python modulecheck_agent.py extract-extends --class-path <ModelicaClassPath>
```

### 6) Rename a component in a class

Rename a component in a target class using OpenModelica `renameComponent`.

```powershell
python modulecheck_agent.py rename-component --class-path <ModelicaClassPath> --old-name <OldComponentName> --new-name <NewComponentName>
```

To rename without saving to disk immediately:

```powershell
python modulecheck_agent.py rename-component --class-path <ModelicaClassPath> --old-name <OldComponentName> --new-name <NewComponentName> --no-save
```

To run a preflight check only (verify old component exists and new name is available):

```powershell
python modulecheck_agent.py rename-component --class-path <ModelicaClassPath> --old-name <OldComponentName> --new-name <NewComponentName> --dry-run
```

#### Example Output

| Base Class                          | Redeclares       | Other Assignments |
|-------------------------------------|------------------|-------------------|
| Buildings.Controls.OBC.CDL.Interfaces | param1, param2   | assign1=value1    |

## Output

By default, files are written under `agent_outputs/` with task-specific names.

- `*_documentation.html`
- `*_documentation_feedback.md`
- `*_pseudocode.md`
- `*_naming_analysis.md`
- `*_rename_component.txt`

Use `--output-file` to override the destination.
