import re
from dataclasses import dataclass, field
from typing import List, Optional

@dataclass
class ExtendsClause:
    base_class: str
    modifiers: List[str] = field(default_factory=list)
    raw_modifier_block: Optional[str] = None
    redeclares: List[str] = field(default_factory=list)
    assignments: List[str] = field(default_factory=list)  # final x=..., x=...

def _strip_comments(text: str) -> str:
    text = re.sub(r'/\*.*?\*/', '', text, flags=re.DOTALL)
    text = re.sub(r'//[^\n]*', '', text)
    return text

def _find_matching_paren(text: str, open_idx: int) -> int:
    """Given index of '(', return index of matching ')'. Handles nesting and strings."""
    depth = 0
    i = open_idx
    in_str = False
    while i < len(text):
        c = text[i]
        if in_str:
            if c == '\\' and i + 1 < len(text):
                i += 2
                continue
            if c == '"':
                in_str = False
        else:
            if c == '"':
                in_str = True
            elif c == '(':
                depth += 1
            elif c == ')':
                depth -= 1
                if depth == 0:
                    return i
        i += 1
    raise ValueError("Unmatched parenthesis")

def _split_top_level(text: str, sep: str = ',') -> List[str]:
    """Split on separator, ignoring those inside parentheses or strings."""
    parts, buf, depth, in_str = [], [], 0, False
    i = 0
    while i < len(text):
        c = text[i]
        if in_str:
            buf.append(c)
            if c == '\\' and i + 1 < len(text):
                buf.append(text[i+1]); i += 2; continue
            if c == '"':
                in_str = False
        else:
            if c == '"':
                in_str = True; buf.append(c)
            elif c == '(':
                depth += 1; buf.append(c)
            elif c == ')':
                depth -= 1; buf.append(c)
            elif c == sep and depth == 0:
                parts.append(''.join(buf).strip()); buf = []
            else:
                buf.append(c)
        i += 1
    tail = ''.join(buf).strip()
    if tail:
        parts.append(tail)
    return parts

EXTENDS_RE = re.compile(r'\bextends\s+([A-Za-z_][\w\.]*)\s*')

def extract_extends(source: str) -> List[ExtendsClause]:
    source = _strip_comments(source)
    results = []
    for m in EXTENDS_RE.finditer(source):
        base = m.group(1)
        pos = m.end()
        # Skip whitespace
        while pos < len(source) and source[pos].isspace():
            pos += 1
        clause = ExtendsClause(base_class=base)
        if pos < len(source) and source[pos] == '(':
            close = _find_matching_paren(source, pos)
            inner = source[pos+1:close]
            clause.raw_modifier_block = inner.strip()
            mods = _split_top_level(inner)
            clause.modifiers = mods
            for mod in mods:
                if re.match(r'^\s*redeclare\b', mod):
                    clause.redeclares.append(mod)
                else:
                    clause.assignments.append(mod)
        results.append(clause)
    return results
