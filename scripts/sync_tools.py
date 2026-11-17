#!/usr/bin/env python3
"""Regenerate tools.json from the WizzHire server's tool registry.

Usage: python3 scripts/sync_tools.py <path to dropcv_core/agent_tools/registry.py> <commit>

Staff-only tools never go into the public list: the Wizz Talent Pool tools (WizzHire's own
sourcing pool) and everything imported from agent_tools/platform_admin.py (superadmin only).
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
STAFF_FEATURES = ("WIZZ_POOL_CAPABILITY",)


def staff_only(source: str) -> set[str]:
    block = re.search(r"from dropcv_core\.agent_tools\.platform_admin import \((.*?)\)", source, re.S)
    admin = set(re.findall(r"([a-z_]+)", block.group(1))) if block else set()
    return admin


def main() -> int:
    registry, commit = Path(sys.argv[1]), sys.argv[2]
    source = registry.read_text()
    body = source.split("TOOLS: dict[str, ToolSpec] = {", 1)[1]
    specs = re.findall(r'^    "([a-z_]+)": ToolSpec\((.*?)\n    \),', body, re.M | re.S)
    hidden = staff_only(source)
    tools = []
    for name, spec in specs:
        if name in hidden or any(f"feature={f}" in spec for f in STAFF_FEATURES):
            continue
        tools.append({"name": name, "read_only": "read_only=True" in spec})
    out = {"source": "dropcv_core/agent_tools/registry.py", "commit": commit, "tools": tools}
    (ROOT / "tools.json").write_text(json.dumps(out, indent=1) + "\n")
    print(f"{len(specs)} tools in the registry, {len(tools)} public, {len(specs) - len(tools)} staff-only")
    return 0


if __name__ == "__main__":
    sys.exit(main())
