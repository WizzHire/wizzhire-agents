#!/usr/bin/env python3
"""Fail when a skill or agent names a WizzHire tool that tools.json does not list.

Tool names in skills are a public contract: a rename on the server breaks every
installed copy. Every `backticked_snake_case` word that looks like a tool name is
checked against tools.json, which is regenerated from the server's registry.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TOOL_WORD = re.compile(r"`([a-z]+(?:_[a-z]+)+)`")
# Snake-case words that appear in backticks but are argument names or values, not tools.
NOT_TOOLS = {
    "copy_stages_from_job_id", "on_behalf", "dated_from", "dry_run", "create_anyway", "stage_id",
    "closed_on", "won_on", "earn_from", "running_contract", "source_days", "show_salary", "show_if",
    "link_to", "cycle_id", "fixed_term", "my_team", "favorites_only", "only_sitting_too_long",
    "is_template", "skip_if_already_asked",
}


def main() -> int:
    data = json.loads((ROOT / "tools.json").read_text())
    known = {t["name"] for t in data["tools"]}
    pending = {t["name"] for t in data.get("pending", [])}
    files = sorted([*ROOT.glob("skills/*/SKILL.md"), *ROOT.glob("agents/*.md")])
    problems: list[str] = []
    used: set[str] = set()
    for path in files:
        for word in TOOL_WORD.findall(path.read_text()):
            if word in NOT_TOOLS:
                continue
            if word in known:
                used.add(word)
            elif word in pending:
                print(f"{path.relative_to(ROOT)}: `{word}` is pending on the server, the skill must work without it")
            else:
                problems.append(f"{path.relative_to(ROOT)}: `{word}` is not a WizzHire tool")
    for p in problems:
        print(p)
    print(f"{len(files)} files, {len(used)} of {len(known)} tools used, {len(problems)} unknown names")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
