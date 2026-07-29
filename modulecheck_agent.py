"""CLI wrapper for ModuleCheck so Copilot agents can run repeatable tasks.

This script exposes ModuleCheck capabilities as explicit subcommands.
"""

from __future__ import annotations

import argparse
import os
from pathlib import Path

from module_check import ModuleCheck


def _default_lib_root() -> str:
    """Resolve a reasonable default path to the modelica-buildings root."""
    repo_root = Path(__file__).resolve().parent
    candidate = (repo_root.parent / "buildings_library" / "modelica-buildings").resolve()
    return str(candidate)


def _default_output_dir() -> str:
    return str((Path(__file__).resolve().parent / "agent_outputs").resolve())


def _get_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Run ModuleCheck skills from the command line.",
    )
    parser.add_argument(
        "--model",
        default=os.getenv("PROMPT2CONTROL_MODEL", "claude-sonnet-4-6-birthright"),
        help="LLM model name.",
    )
    parser.add_argument(
        "--base-url",
        default=os.getenv("PROMPT2CONTROL_BASE_URL", "https://ai-incubator-api.pnnl.gov"),
        help="Base URL for the chat completion API.",
    )
    parser.add_argument(
        "--api-key",
        default=os.getenv("PROMPT2CONTROL_API_KEY", ""),
        help="API key for the LLM endpoint.",
    )
    parser.add_argument(
        "--lib-root",
        default=os.getenv("PROMPT2CONTROL_LIB_ROOT", _default_lib_root()),
        help="Path to the Modelica library root that contains the Buildings package.",
    )
    parser.add_argument(
        "--output-dir",
        default=os.getenv("PROMPT2CONTROL_OUTPUT_DIR", _default_output_dir()),
        help="Directory where generated outputs are written.",
    )

    subparsers = parser.add_subparsers(dest="command", required=True)

    shared = argparse.ArgumentParser(add_help=False)
    shared.add_argument(
        "--class-path",
        required=True,
        help="Modelica package path, e.g. Buildings.Templates.Plants.Controls.StagingRotation.EquipmentEnable",
    )
    shared.add_argument(
        "--output-file",
        default="",
        help="Optional output file path. If omitted, a default file is generated in output-dir.",
    )

    subparsers.add_parser(
        "generate-docs",
        parents=[shared],
        help="Generate English HTML documentation from the model.",
    )
    subparsers.add_parser(
        "review-docs",
        parents=[shared],
        help="Review the model documentation and generate markdown feedback.",
    )
    subparsers.add_parser(
        "pseudo-code",
        parents=[shared],
        help="Generate markdown pseudo code from the model.",
    )
    subparsers.add_parser(
        "extract-extends",
        parents=[shared],
        help="Extract extend statements from the model and generate a markdown summary.",
    )

    rename_parser = subparsers.add_parser(
        "rename-component",
        parents=[shared],
        help="Rename a component in a Modelica class using OpenModelica renameComponent.",
    )
    rename_parser.add_argument(
        "--old-name",
        required=True,
        help="Existing component name to rename.",
    )
    rename_parser.add_argument(
        "--new-name",
        required=True,
        help="New component name.",
    )
    rename_parser.add_argument(
        "--no-save",
        action="store_true",
        help="Do not save the class after renameComponent succeeds.",
    )
    rename_parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Validate rename preconditions only; do not rename or save.",
    )

    analyze_parser = subparsers.add_parser(
        "analyze-names",
        parents=[shared],
        help="Analyze variable naming quality against CDL naming rules.",
    )
    analyze_parser.add_argument(
        "--complete-set",
        action="store_true",
        help="Include internal variables along with parameters and interface variables.",
    )

    return parser


def _default_filename(command: str, class_path: str) -> str:
    class_name = class_path.split(".")[-1]
    if command == "generate-docs":
        return f"{class_name}_documentation.html"
    if command == "review-docs":
        return f"{class_name}_documentation_feedback.md"
    if command == "pseudo-code":
        return f"{class_name}_pseudocode.md"
    if command == "analyze-names":
        return f"{class_name}_naming_analysis.md"
    if command == "extract-extends":
        return f"{class_name}_extends.md"
    if command == "rename-component":
        return f"{class_name}_rename_component.txt"
    return f"{class_name}_{command}.txt"


def _resolve_output_path(output_dir: str, output_file: str, command: str, class_path: str) -> Path:
    if output_file:
        out = Path(output_file)
    else:
        out = Path(output_dir) / _default_filename(command, class_path)
    out.parent.mkdir(parents=True, exist_ok=True)
    return out


def _require_api_key_if_needed(command: str, api_key: str) -> None:
    needs_llm = command in {"generate-docs", "review-docs", "pseudo-code", "analyze-names"}
    if needs_llm and not api_key:
        raise ValueError(
            "Missing API key. Set PROMPT2CONTROL_API_KEY or pass --api-key when running this command."
        )


def main() -> None:
    parser = _get_parser()
    args = parser.parse_args()

    _require_api_key_if_needed(args.command, args.api_key)

    os.environ.setdefault("MODELICAPATH", str(Path(args.lib_root).resolve().parent))

    checker = ModuleCheck(
        model=args.model,
        base_url=args.base_url,
        api_key=args.api_key,
        lib_root=args.lib_root,
        run_api_calls=True,
    )

    output_path = _resolve_output_path(args.output_dir, args.output_file, args.command, args.class_path)

    if args.command == "generate-docs":
        result = checker.generate_english_documentation(args.class_path)
    elif args.command == "review-docs":
        result = checker.check_english_documentation(args.class_path)
    elif args.command == "pseudo-code":
        result = checker.get_pseudo_code(args.class_path)
    elif args.command == "extract-extends":
        result = checker.get_extend_statements(args.class_path)
    elif args.command == "rename-component":
        rename_result = checker.rename_component(
            args.class_path,
            args.old_name,
            args.new_name,
            save_class=not args.no_save,
            dry_run=args.dry_run,
        )
        result = (
            f"class_path: {rename_result['class_path']}\n"
            f"old_name: {rename_result['old_name']}\n"
            f"new_name: {rename_result['new_name']}\n"
            f"dry_run: {rename_result['dry_run']}\n"
            f"precheck_success: {rename_result['precheck_success']}\n"
            f"component_exists: {rename_result['component_exists']}\n"
            f"new_name_conflict: {rename_result['new_name_conflict']}\n"
            f"precheck_message: {rename_result['precheck_message']}\n"
            f"rename_success: {rename_result['rename_success']}\n"
            f"rename_result: {rename_result['rename_result']}\n"
            f"save_attempted: {rename_result['save_attempted']}\n"
            f"save_success: {rename_result['save_success']}\n"
            f"save_result: {rename_result['save_result']}\n"
        )
    elif args.command == "analyze-names":
        variables_df = checker.parse_model_variables(args.class_path, complete_set=args.complete_set)
        result = checker.analyze_variable_names(variables_df)
    else:
        raise ValueError(f"Unsupported command: {args.command}")

    output_path.write_text(result, encoding="utf-8")
    print(f"Wrote {args.command} output to: {output_path}")


if __name__ == "__main__":
    main()
