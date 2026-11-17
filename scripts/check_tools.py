#!/usr/bin/env python3
"""Fail when a skill or agent tells Claude to call something the WizzHire server does not have.

Tool names and arguments in skills are a public contract: a rename on the server breaks every
installed copy over MCP. For every skill and agent file this checks, against tools.json (which
scripts/sync_tools.py generates from the server's registry):

- every backticked snake_case word is a tool, an argument of some tool, an allowed value, or a
  field inside a structured argument listed in NESTED;
- every backticked `argument=value` names an argument of a tool mentioned on the same line (or
  of any tool when the line mentions none), and a quoted value is one the argument allows.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
WORD = re.compile(r"`([a-z]+(?:_[a-z]+)+)`")
ASSIGN = re.compile(r"`([a-z_]+)=(\"[^\"]*\"|[A-Za-z0-9_]+)`")
# Fields inside structured arguments (a questionnaire's questions, an import row, a deal line).
NESTED = {
    "show_if", "create_anyway", "earn_from", "source_days", "closed_on", "won_on", "running_contract",
    "fixed_term",
}


def main() -> int:
    data = json.loads((ROOT / "tools.json").read_text())
    tools: dict[str, dict[str, list[str]]] = {t["name"]: t.get("args", {}) for t in data["tools"]}
    all_args = {a for args in tools.values() for a in args}
    all_values = {v for args in tools.values() for vals in args.values() for v in vals}
    files = sorted([*ROOT.glob("skills/*/SKILL.md"), *ROOT.glob("agents/*.md")])
    problems: list[str] = []
    used: set[str] = set()
    for path in files:
        where = path.relative_to(ROOT)
        for number, line in enumerate(path.read_text().splitlines(), 1):
            named = [w for w in WORD.findall(line) if w in tools]
            used.update(named)
            for word in WORD.findall(line):
                if word not in tools and word not in all_args and word not in all_values and word not in NESTED:
                    problems.append(f"{where}:{number}: `{word}` is not a WizzHire tool, argument or value")
            scope = named or list(tools)
            for arg, raw in ASSIGN.findall(line):
                owners = [t for t in scope if arg in tools[t]]
                if not owners:
                    problems.append(f"{where}:{number}: `{arg}` is not an argument of {', '.join(named) or 'any tool'}")
                    continue
                value = raw.strip('"')
                if raw.startswith('"'):
                    allowed = {v for t in owners for v in tools[t][arg]}
                    if allowed and value not in allowed:
                        problems.append(f"{where}:{number}: `{arg}=\"{value}\"` is not allowed; use one of {sorted(allowed)}")
    for p in problems:
        print(p)
    print(f"{len(files)} files, {len(used)} of {len(tools)} tools used, {len(problems)} problems")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
