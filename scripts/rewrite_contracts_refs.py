#!/usr/bin/env python3
"""
One-shot link rewriter for the oesis-contracts repo split.

Rewrites relative references to `contracts/...` paths into absolute GitHub URLs
pointing at the new oesis-contracts repository. Mirrors the approach used for
the oesis-hardware split.

Run from oesis-program-specs repo root:
    python3 scripts/rewrite_contracts_refs.py           # dry-run; prints diff summary
    python3 scripts/rewrite_contracts_refs.py --write   # apply in-place

What it rewrites:
    - Markdown links:           [label](contracts/v1.0/foo.md)
    -                           [label](../contracts/v1.0/foo.md)
    -                           [label](../../contracts/v1.0/foo.md)
    - Backtick code refs:       `contracts/v1.0/foo.md`
    -                           `contracts/v1.0/schemas/foo.schema.json`

What it skips:
    - The new stub READMEs (contracts/README.md, artifacts/contracts-bundle/README.md)
    - Anything under .git/, build/, oesis_build/build/

The new target URL:
    https://github.com/lumenaut-llc/oesis-contracts/blob/main/<path-without-contracts-prefix>

For `contracts/schemas/...` (bundle-root sibling) and `contracts/examples/...`,
the prefix is stripped:
    contracts/v1.0/schemas/foo.schema.json
        -> https://github.com/lumenaut-llc/oesis-contracts/blob/main/v1.0/schemas/foo.schema.json
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
GITHUB_BASE = "https://github.com/lumenaut-llc/oesis-contracts/blob/main"

# Skip these files/dirs entirely (stubs we just wrote, build outputs, VCS)
SKIP_PATHS = {
    REPO_ROOT / "contracts" / "README.md",
    REPO_ROOT / "artifacts" / "contracts-bundle" / "README.md",
    REPO_ROOT / "scripts" / "rewrite_contracts_refs.py",  # don't rewrite ourselves
}
SKIP_DIR_PARTS = {".git", "build", "node_modules", ".next"}

# Patterns (applied in order, first match wins per substring)
# Captures the path fragment after the `contracts/` prefix.
PATTERNS = [
    # Markdown link: ](../../contracts/...), ](../contracts/...), ](contracts/...)
    (re.compile(r"\]\((?:\.\./){0,3}contracts/([^\)]+)\)"),
     lambda m: f"]({GITHUB_BASE}/{m.group(1)})"),
    # Backtick path ref with any ../ prefix: `../../contracts/...`, `../contracts/...`, `contracts/...`
    (re.compile(r"`(?:\.\./){0,3}contracts/([^`]+)`"),
     lambda m: f"[`{m.group(1)}`]({GITHUB_BASE}/{m.group(1)})"),
]


def should_skip(path: Path) -> bool:
    if path in SKIP_PATHS:
        return True
    if any(part in SKIP_DIR_PARTS for part in path.parts):
        return True
    return False


def rewrite_content(text: str) -> tuple[str, int]:
    """Returns (new_text, num_replacements)."""
    count = 0
    new_text = text
    for pattern, replacer in PATTERNS:
        def sub(m: re.Match) -> str:
            nonlocal count
            count += 1
            return replacer(m)
        new_text = pattern.sub(sub, new_text)
    return new_text, count


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write", action="store_true", help="Apply changes in place")
    args = parser.parse_args()

    total_replacements = 0
    files_changed = 0

    for md_file in REPO_ROOT.rglob("*.md"):
        if should_skip(md_file):
            continue
        try:
            original = md_file.read_text(encoding="utf-8")
        except (UnicodeDecodeError, PermissionError):
            continue

        rewritten, count = rewrite_content(original)
        if count == 0:
            continue

        total_replacements += count
        files_changed += 1
        rel = md_file.relative_to(REPO_ROOT)
        action = "WRITE" if args.write else "WOULD WRITE"
        print(f"  {action} {rel}: {count} replacement(s)")

        if args.write:
            md_file.write_text(rewritten, encoding="utf-8")

    print(f"\n{'APPLIED' if args.write else 'DRY-RUN'}: "
          f"{total_replacements} replacements across {files_changed} files")
    if not args.write and total_replacements > 0:
        print("Re-run with --write to apply.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
