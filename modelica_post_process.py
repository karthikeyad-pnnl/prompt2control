import re

def clean_modelica_code(lines: list[str], title: str, default_within: str = "within Buildings.Controls.OBC.CDL.Examples;") -> list[str]:
    """
    Clean and standardize generated Modelica code lines.

    This function:
    - Removes ```modelica from the first line
    - Removes trailing ``` if present
    - Rewrites 'block' name to match the file name (safe_title)
    - Rewrites 'end' block name to match the file name and ensures semicolon
    - Adds or adjusts 'within' clause
    - Adds default 'within' if none found

    Args:
        lines (list[str]): List of Modelica code lines.
        title (str): Title to use as sanitized block name.
        default_within (str): Default 'within' clause if none exists.

    Returns:
        list[str]: Cleaned list of Modelica code lines.
    """
    # Remove ```modelica at top
    if lines and lines[0].strip().lower() == "```modelica":
        lines = lines[1:]

    # Remove trailing ```
    if lines and lines[-1].strip() == "```":
        lines = lines[:-1]

    safe_title = title.replace(" ", "_").replace("/", "_")

    # Handle 'within' logic
    if lines:
        first_line = lines[0].strip()
        if first_line.startswith("within"):
            lines[0] = default_within
        elif first_line.startswith("block"):
            lines.insert(0, default_within)

    # Rename block name if found in first 3 lines
    for i in range(min(3, len(lines))):
        match = re.match(r"block\s+(\w+)", lines[i])
        if match:
            block_name = match.group(1)
            lines[i] = lines[i].replace(block_name, safe_title)
            break

    # Rename `end` block name in last few lines
    for j in reversed(range(len(lines))):
        match = re.match(r"end\s+(\w+)\s*;?", lines[j])
        if match:
            lines[j] = f"end {safe_title};"
            break

    return lines
