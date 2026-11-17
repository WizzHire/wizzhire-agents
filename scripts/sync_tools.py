#!/usr/bin/env python3
"""Regenerate tools.json from the WizzHire server's tool registry.

Usage: python3 scripts/sync_tools.py <path to dropcv_core/agent_tools/registry.py> <commit>

Each tool also gets its argument names and, where an argument is a Literal, its allowed
values, read from the tool functions beside the registry. check_tools.py uses them to
check every `argument="value"` a skill tells Claude to pass.

Staff-only tools never go into the public list: the Wizz Talent Pool tools (WizzHire's own
sourcing pool) and everything imported from agent_tools/platform_admin.py (superadmin only).
"""

from __future__ import annotations

import ast
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


def literal_values(node: ast.AST) -> list[str]:
    values: list[str] = []
    for sub in ast.walk(node):
        if isinstance(sub, ast.Subscript) and isinstance(sub.value, ast.Name) and sub.value.id == "Literal":
            elts = sub.slice.elts if isinstance(sub.slice, ast.Tuple) else [sub.slice]
            values += [e.value for e in elts if isinstance(e, ast.Constant) and isinstance(e.value, str)]
    return values


def signatures(tool_dir: Path, names: set[str]) -> dict[str, dict[str, list[str]]]:
    """Argument names (and Literal values) of every tool function, by tool name.

    Type aliases are resolved in the module that uses them, then through its imports from
    other agent_tools modules, because the same alias name means different things in
    different modules.
    """
    modules = {f.stem: ast.parse(f.read_text()) for f in sorted(tool_dir.glob("*.py"))}
    local: dict[str, dict[str, ast.AST]] = {}
    imported: dict[str, dict[str, str]] = {}
    for mod, tree in modules.items():
        local[mod] = {
            n.targets[0].id: n.value
            for n in tree.body
            if isinstance(n, ast.Assign) and len(n.targets) == 1 and isinstance(n.targets[0], ast.Name)
        }
        local[mod].update(
            {n.target.id: n.value for n in tree.body if isinstance(n, ast.AnnAssign) and isinstance(n.target, ast.Name) and n.value is not None}
        )
        imported[mod] = {
            alias.asname or alias.name: n.module.rsplit(".", 1)[1]
            for n in tree.body
            if isinstance(n, ast.ImportFrom) and n.module and n.module.startswith("dropcv_core.agent_tools.")
            for alias in n.names
        }

    def resolve(mod: str, name: str) -> ast.AST | None:
        if name in local[mod]:
            return local[mod][name]
        source = imported[mod].get(name)
        return local.get(source, {}).get(name) if source else None

    found: dict[str, dict[str, list[str]]] = {}
    for mod, tree in modules.items():
        for node in tree.body:
            if isinstance(node, ast.AsyncFunctionDef | ast.FunctionDef) and node.name in names:
                args: dict[str, list[str]] = {}
                for arg in [*node.args.args, *node.args.kwonlyargs]:
                    if arg.arg in ("ctx", "context", "self") or arg.annotation is None:
                        continue
                    vals = literal_values(arg.annotation)
                    for sub in ast.walk(arg.annotation):
                        if isinstance(sub, ast.Name) and (target := resolve(mod, sub.id)) is not None:
                            vals += literal_values(target)
                    args[arg.arg] = sorted(set(vals))
                found[node.name] = args
    return found


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
    sigs = signatures(registry.parent, {t["name"] for t in tools})
    for t in tools:
        t["args"] = sigs.get(t["name"], {})
    missing = [t["name"] for t in tools if t["name"] not in sigs]
    if missing:
        print("no signature found for:", ", ".join(missing))
    out = {"source": "dropcv_core/agent_tools/registry.py", "commit": commit, "tools": tools}
    (ROOT / "tools.json").write_text(json.dumps(out, indent=1) + "\n")
    print(f"{len(specs)} tools in the registry, {len(tools)} public, {len(specs) - len(tools)} staff-only")
    return 0


if __name__ == "__main__":
    sys.exit(main())
