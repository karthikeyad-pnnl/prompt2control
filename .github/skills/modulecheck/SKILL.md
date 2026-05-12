---
name: modulecheck
description: "Run ModuleCheck workflows for Modelica classes: generate English documentation, review annotation documentation quality, generate pseudo code, and analyze CDL variable naming compliance. Use when users ask to evaluate or document a Buildings model class."
---

# ModuleCheck Skill

Use this skill to run the Python CLI wrapper around `ModuleCheck` in `module_check.py`.

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

## Output

By default, files are written under `agent_outputs/` with task-specific names.

- `*_documentation.html`
- `*_documentation_feedback.md`
- `*_pseudocode.md`
- `*_naming_analysis.md`

Use `--output-file` to override the destination.
