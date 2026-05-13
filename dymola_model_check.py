"""Run Dymola model check for a Modelica class.

This utility generates a temporary .mos script, launches Dymola, and runs
checkModel on a target class from the Buildings library.
"""

from __future__ import annotations

import argparse
import os
import shutil
import subprocess
from pathlib import Path


def _find_dymola_executable(explicit_path: str = "") -> str:
    """Resolve Dymola executable path from argument, env var, or PATH."""
    candidates = []
    if explicit_path:
        candidates.append(explicit_path)
    env_path = os.getenv("DYMOLA_EXE", "")
    if env_path:
        candidates.append(env_path)

    for candidate in candidates:
        if Path(candidate).exists():
            return str(Path(candidate).resolve())

    for binary in ["dymola.exe", "dymola"]:
        found = shutil.which(binary)
        if found:
            return found

    raise FileNotFoundError(
        "Dymola executable not found. Pass --dymola-exe or set DYMOLA_EXE."
    )


def _default_output_dir() -> Path:
    return (Path(__file__).resolve().parent / "agent_outputs" / "dymola_model_check").resolve()


def _build_mos_content(model_class: str, library_root: str, output_dir: str, modelica_path: str = "") -> str:
    """Create the Dymola command script for model check."""
    lib_path = Path(library_root).resolve().as_posix()
    lines = [
        "Advanced.TranslationInCommandLog:=true;",
    ]

    if modelica_path:
        mp = modelica_path.replace("\\", "/")
        lines.append(f'Modelica.Utilities.System.setEnvironmentVariable("MODELICAPATH", "{mp}");')

    lines.extend(
        [
            'openModel("C:/Program Files/Dymola 2025x/Modelica/Library/Modelica 4.1.0/package.mo");',
            f'openModel("{lib_path}/Buildings/package.mo");',
            f'ok := checkModel("{model_class}");',
            "if not ok then",
            '  Modelica.Utilities.Streams.print("Model check failed.");',
            "end if;",
            f'savelog("{output_dir}/dymola_model_check.log");',
            "exit();",
        ]
    )
    return "\n".join(lines) + "\n"


def run_model_check(
    model_class: str,
    library_root: str,
    output_dir: Path,
    dymola_exe: str = "",
    modelica_path: str = "",
) -> int:
    """Execute Dymola checkModel and return process exit code."""
    output_dir.mkdir(parents=True, exist_ok=True)
    mos_path = output_dir / "model_check.mos"
    mos_path.write_text(
        _build_mos_content(model_class, library_root, str(output_dir.resolve().as_posix()), modelica_path=modelica_path),
        encoding="utf-8",
    )

    exe = _find_dymola_executable(dymola_exe)
    cmd = [exe, '/nowindow', str(mos_path)]

    proc = subprocess.run(
        cmd,
        cwd=str(output_dir),
        text=True,
        capture_output=True,
        check=False,
    )

    (output_dir / "dymola_model_check_stdout.log").write_text(proc.stdout or "", encoding="utf-8")
    (output_dir / "dymola_model_check_stderr.log").write_text(proc.stderr or "", encoding="utf-8")

    print(f"Dymola executable: {exe}")
    print(f"MOS script: {mos_path}")
    print(f"Exit code: {proc.returncode}")
    print(f"Stdout log: {output_dir / 'dymola_model_check_stdout.log'}")
    print(f"Stderr log: {output_dir / 'dymola_model_check_stderr.log'}")

    return proc.returncode


def _get_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Run Dymola model check (checkModel) for a Modelica class.",
    )
    parser.add_argument(
        "--class-path",
        required=True,
        help="Fully-qualified Modelica class path.",
    )
    parser.add_argument(
        "--library-root",
        default=os.getenv("PROMPT2CONTROL_LIB_ROOT", str((Path(__file__).resolve().parent.parent / "buildings_library" / "modelica-buildings").resolve())),
        help="Path to modelica-buildings root (contains Buildings/).",
    )
    parser.add_argument(
        "--output-dir",
        default=os.getenv("PROMPT2CONTROL_DYMOLA_MODEL_CHECK_OUTPUT_DIR", str(_default_output_dir())),
        help="Directory to store generated .mos and logs.",
    )
    parser.add_argument(
        "--dymola-exe",
        default=os.getenv("DYMOLA_EXE", ""),
        help="Path to Dymola executable. Optional if on PATH or DYMOLA_EXE is set.",
    )
    parser.add_argument(
        "--modelica-path",
        default=os.getenv("MODELICAPATH", ""),
        help="Optional MODELICAPATH override passed to Dymola.",
    )
    return parser


def main() -> None:
    args = _get_parser().parse_args()
    exit_code = run_model_check(
        model_class=args.class_path,
        library_root=args.library_root,
        output_dir=Path(args.output_dir),
        dymola_exe=args.dymola_exe,
        modelica_path=args.modelica_path,
    )
    raise SystemExit(exit_code)


if __name__ == "__main__":
    main()
