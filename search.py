import os
import logging
import re

# Optional: Setup a default logger for this module if not already set by main
log = logging.getLogger(__name__)
if not log.hasHandlers():
    logging.basicConfig(level=logging.INFO)

def strip_annotations(text: str) -> str:
    """
    Remove all `annotation(...)` blocks from Modelica code.
    """
    return re.sub(r"annotation\s*\(.*?\);", "", text, flags=re.DOTALL)

def gather_cdl_modules(module_list: list[str], cdl_root: str = "CDL") -> list[str]:
    """
    Load and strip annotations from CDL modules.

    Args:
        module_list: List of CDL module names in dot notation (e.g., "CDL.Controls.PID").
        cdl_root: Root directory where CDL modules are located.

    Returns:
        List of CDL module code strings with annotations stripped.
    """
    gathered_modules = []
    for module in module_list:
        module_path = os.path.join(cdl_root, *module.split(".")) + ".mo"
        if os.path.exists(module_path):
            with open(module_path, encoding="utf-8") as f:
                text = f.read()
            stripped = strip_annotations(text)
            gathered_modules.append(stripped)
        else:
            log.warning(f"⚠️ {module_path} not found, skipping.")
    return gathered_modules
