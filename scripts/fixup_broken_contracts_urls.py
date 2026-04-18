#!/usr/bin/env python3
"""
Second-pass fixup for the oesis-contracts split.

After rewrite_contracts_refs.py converts relative links to GitHub URLs, some
URLs point at stale bare filenames (e.g. node-registry-schema.md) because the
source prose had stale paths. This script rewrites those bare URLs to point at
the actual lane directory where the file lives in oesis-contracts.

Run from oesis-program-specs repo root:
    python3 scripts/fixup_broken_contracts_urls.py            # dry run
    python3 scripts/fixup_broken_contracts_urls.py --write    # apply
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
CONTRACTS_ROOT = REPO_ROOT.parent / "oesis-contracts"
GITHUB_BASE = "https://github.com/lumenaut-llc/oesis-contracts/blob/main"

# Bare-filename -> lane-qualified path. Generated from `find` against oesis-contracts.
# Where a file exists in multiple lanes, prefer v0.1 (baseline) for bare refs.
BARE_SCHEMA_MAP = {
    "node-registry-schema.md": "v0.1/node-registry-schema.md",
    "node-observation-schema.md": "v0.1/node-observation-schema.md",
    "parcel-context-schema.md": "v0.1/parcel-context-schema.md",
    "parcel-state-schema.md": "v0.1/parcel-state-schema.md",
    "public-context-schema.md": "v0.1/public-context-schema.md",
    "shared-neighborhood-signal-schema.md": "v0.1/shared-neighborhood-signal-schema.md",
    "explanation-payload-schema.md": "v0.1/explanation-payload-schema.md",
    "evidence-summary-schema.md": "v0.1/evidence-summary-schema.md",
    "equipment-state-observation-schema.md": "v0.1/equipment-state-observation-schema.md",
    "verification-outcome-schema.md": "v0.1/verification-outcome-schema.md",
    "source-provenance-record-schema.md": "v0.1/source-provenance-record-schema.md",
    "house-state-schema.md": "v0.1/house-state-schema.md",
    "house-capability-schema.md": "v0.1/house-capability-schema.md",
    "intervention-event-schema.md": "v0.1/intervention-event-schema.md",
    "evidence-mode-and-observability.md": "v0.1/evidence-mode-and-observability.md",
    "explainability-claim-schema.md": "v0.1/explainability-claim-schema.md",
    "export-bundle-schema.md": "v0.1/export-bundle-schema.md",
    "house-capability-profile-schema.md": "v0.1/house-capability-profile-schema.md",
    "response-status-schema.md": "v0.1/response-status-schema.md",
}

# Wrong-lane references in prose (e.g. cited as v1.0 but actually in v0.1 or v1.5).
# Fix to actual location.
WRONG_LANE_MAP = {
    "v1.0/equipment-state-observation-schema.md": "v1.5/equipment-state-observation-schema.md",
    "v1.0/verification-outcome-schema.md": "v1.5/verification-outcome-schema.md",
}

SKIP_DIR_PARTS = {".git", "build", "node_modules", ".next"}
SKIP_FILES = {
    REPO_ROOT / "scripts" / "rewrite_contracts_refs.py",
    REPO_ROOT / "scripts" / "fixup_broken_contracts_urls.py",
}


def should_skip(path: Path) -> bool:
    if path in SKIP_FILES:
        return True
    if any(part in SKIP_DIR_PARTS for part in path.parts):
        return True
    return False


def build_patterns() -> list[tuple[re.Pattern, str]]:
    patterns: list[tuple[re.Pattern, str]] = []
    escaped_base = re.escape(GITHUB_BASE)

    for bare, lane_qualified in BARE_SCHEMA_MAP.items():
        old = f"{GITHUB_BASE}/{bare}"
        new = f"{GITHUB_BASE}/{lane_qualified}"
        patterns.append((re.compile(re.escape(old)), new))

    for wrong, right in WRONG_LANE_MAP.items():
        old = f"{GITHUB_BASE}/{wrong}"
        new = f"{GITHUB_BASE}/{right}"
        patterns.append((re.compile(re.escape(old)), new))

    return patterns


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write", action="store_true", help="Apply changes")
    args = parser.parse_args()

    patterns = build_patterns()
    total_replacements = 0
    files_changed = 0

    for md_file in REPO_ROOT.rglob("*.md"):
        if should_skip(md_file):
            continue
        try:
            original = md_file.read_text(encoding="utf-8")
        except (UnicodeDecodeError, PermissionError):
            continue

        new_text = original
        file_count = 0
        for pattern, replacement in patterns:
            new_text, n = pattern.subn(replacement, new_text)
            file_count += n

        if file_count == 0:
            continue

        total_replacements += file_count
        files_changed += 1
        rel = md_file.relative_to(REPO_ROOT)
        action = "WRITE" if args.write else "WOULD WRITE"
        print(f"  {action} {rel}: {file_count} fix(es)")

        if args.write:
            md_file.write_text(new_text, encoding="utf-8")

    print(f"\n{'APPLIED' if args.write else 'DRY-RUN'}: "
          f"{total_replacements} fixes across {files_changed} files")
    if not args.write and total_replacements > 0:
        print("Re-run with --write to apply.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
