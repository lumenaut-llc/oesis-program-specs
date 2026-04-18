#!/usr/bin/env python3
"""
Cross-repo consistency check for OESIS multi-repo architecture.

Compares schemas, examples, and version alignment across:
  - oesis-program-specs (architecture, governance, release)
  - oesis-contracts (canonical schemas and examples)
  - oesis-runtime (reference implementation)
  - oesis-hardware (sensor nodes and firmware)

Run from oesis-program-specs repo root:
    python3 scripts/cross_repo_sync_check.py

Exits 0 if consistent, 1 if drift detected.
"""

from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path

SPECS_ROOT = Path(__file__).resolve().parent.parent
CONTRACTS_ROOT = SPECS_ROOT.parent / "oesis-contracts"
RUNTIME_ROOT = SPECS_ROOT.parent / "oesis-runtime"
HARDWARE_ROOT = SPECS_ROOT.parent / "oesis-hardware"

# Lanes where specs owns canonical examples (baseline + additive lanes).
# Overlay lanes v0.2-v0.5 intentionally have no specs examples — runtime
# owns test-fixture overlays for those.
CANONICAL_EXAMPLE_LANES = ["v0.1", "v1.0", "v1.5"]

# All lanes the runtime supports.
ALL_RUNTIME_LANES = ["v0.1", "v0.2", "v0.3", "v0.4", "v0.5", "v1.0", "v1.5"]

PASS = "\033[32mPASS\033[0m"
FAIL = "\033[31mFAIL\033[0m"
WARN = "\033[33mWARN\033[0m"
INFO = "\033[36mINFO\033[0m"


def file_hash(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()[:16]


def check_repo_exists(path: Path, name: str) -> bool:
    if not path.is_dir():
        print(f"  {WARN} {name} not found at {path}")
        return False
    return True


def check_example_sync() -> list[str]:
    """Compare canonical example files between oesis-contracts and runtime."""
    errors: list[str] = []
    if not check_repo_exists(CONTRACTS_ROOT, "oesis-contracts"):
        errors.append("oesis-contracts not found; cannot check example sync")
        return errors
    if not check_repo_exists(RUNTIME_ROOT, "oesis-runtime"):
        errors.append("oesis-runtime not found; cannot check example sync")
        return errors

    for lane in CANONICAL_EXAMPLE_LANES:
        contracts_dir = CONTRACTS_ROOT / lane / "examples"
        runtime_dir = RUNTIME_ROOT / "oesis" / "assets" / lane / "examples"

        contracts_files = {
            f.name for f in contracts_dir.glob("*.json")
        } if contracts_dir.is_dir() else set()
        runtime_files = {
            f.name for f in runtime_dir.glob("*.json")
        } if runtime_dir.is_dir() else set()

        # Files in runtime but not contracts (drift: runtime created examples contracts doesn't own)
        runtime_only = runtime_files - contracts_files
        if runtime_only:
            for f in sorted(runtime_only):
                errors.append(f"{lane}: example '{f}' exists in runtime but not oesis-contracts")

        # Files in contracts but not runtime (drift: contracts has examples runtime doesn't use)
        contracts_only = contracts_files - runtime_files
        if contracts_only:
            for f in sorted(contracts_only):
                errors.append(f"{lane}: example '{f}' exists in oesis-contracts but not runtime")

        # Content mismatches
        common = contracts_files & runtime_files
        for f in sorted(common):
            contracts_hash = file_hash(contracts_dir / f)
            runtime_hash = file_hash(runtime_dir / f)
            if contracts_hash != runtime_hash:
                errors.append(
                    f"{lane}: example '{f}' content differs "
                    f"(contracts={contracts_hash}, runtime={runtime_hash})"
                )

    return errors


def check_schema_coverage() -> list[str]:
    """Verify every schema has at least one matching example."""
    errors: list[str] = []
    if not check_repo_exists(CONTRACTS_ROOT, "oesis-contracts"):
        errors.append("oesis-contracts not found; cannot check schema coverage")
        return errors

    for lane in CANONICAL_EXAMPLE_LANES:
        schemas_dir = CONTRACTS_ROOT / lane / "schemas"
        examples_dir = CONTRACTS_ROOT / lane / "examples"
        if not schemas_dir.is_dir():
            continue

        schemas = {f.stem.replace(".schema", "") for f in schemas_dir.glob("*.schema.json")}
        examples = {f.stem.replace(".example", "") for f in examples_dir.glob("*.example.json")}

        uncovered = schemas - examples
        for s in sorted(uncovered):
            errors.append(f"{lane}: schema '{s}' has no matching example")

    return errors


def check_runtime_lane_alignment() -> list[str]:
    """Verify runtime lane directories exist for all expected lanes."""
    errors: list[str] = []
    if not check_repo_exists(RUNTIME_ROOT, "oesis-runtime"):
        errors.append("oesis-runtime not found; cannot check lane alignment")
        return errors

    for lane in ALL_RUNTIME_LANES:
        lane_dir = RUNTIME_ROOT / "oesis" / "assets" / lane
        if not lane_dir.is_dir():
            errors.append(f"runtime missing asset directory for lane {lane}")

    return errors


def check_manifest_freshness() -> list[str]:
    """Warn (not fail) if the contracts-bundle manifest lags current oesis-contracts HEAD.

    Bundle regeneration is a deliberate step tied to schema releases, not every
    commit, so a lagging manifest is a WARN rather than a hard drift.
    """
    errors: list[str] = []
    if not check_repo_exists(CONTRACTS_ROOT, "oesis-contracts"):
        return errors

    manifest_path = CONTRACTS_ROOT / "bundles" / "contracts-bundle" / "manifest.json"
    if not manifest_path.is_file():
        errors.append("contracts-bundle manifest.json not found in oesis-contracts")
        return errors

    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    bundle_commit = manifest.get("source_commit", "unknown")

    # Get current oesis-contracts HEAD
    git_head = CONTRACTS_ROOT / ".git" / "HEAD"
    if git_head.is_file():
        ref = git_head.read_text().strip()
        if ref.startswith("ref: "):
            ref_path = CONTRACTS_ROOT / ".git" / ref.split("ref: ")[1]
            if ref_path.is_file():
                current_commit = ref_path.read_text().strip()
                if current_commit != bundle_commit:
                    # Print as warning inline; do not add to errors.
                    print(
                        f"  {WARN} contracts-bundle manifest references commit "
                        f"{bundle_commit[:12]}, but oesis-contracts HEAD is "
                        f"{current_commit[:12]}. Consider regenerating the bundle."
                    )

    return errors


def _check_github_cross_refs(repo_root: Path, repo_slug: str, repo_label: str) -> list[str]:
    """Shared helper: verify that GitHub URLs in specs markdown reference real paths in a sibling repo."""
    errors: list[str] = []
    if not check_repo_exists(repo_root, repo_label):
        errors.append(f"{repo_label} not found; cannot check cross-references")
        return errors

    import re
    url_pattern = re.compile(
        rf"https://github\.com/lumenaut-llc/{re.escape(repo_slug)}/blob/main/([^\s\)\"]+)"
    )

    for md_file in SPECS_ROOT.rglob("*.md"):
        # Skip .git and build directories
        if ".git" in md_file.parts or "build" in md_file.parts:
            continue
        try:
            content = md_file.read_text(encoding="utf-8")
        except (UnicodeDecodeError, PermissionError):
            continue

        for match in url_pattern.finditer(content):
            rel_path = match.group(1).rstrip("/").rstrip("`")
            # Skip inline examples like `/...` in prose
            if rel_path.startswith(".") or rel_path == "":
                continue
            target = repo_root / rel_path
            if not target.exists() and not (repo_root / rel_path.rstrip("/")).is_dir():
                try:
                    rel_md = md_file.relative_to(SPECS_ROOT)
                except ValueError:
                    rel_md = md_file
                errors.append(
                    f"{rel_md}: broken {repo_label} URL — "
                    f"'{rel_path}' not found in {repo_label}"
                )

    return errors


def check_hardware_cross_refs() -> list[str]:
    """Verify specs GitHub URLs to hardware repo reference real paths."""
    return _check_github_cross_refs(HARDWARE_ROOT, "oesis-hardware", "oesis-hardware")


def check_contracts_cross_refs() -> list[str]:
    """Verify specs GitHub URLs to oesis-contracts reference real paths."""
    return _check_github_cross_refs(CONTRACTS_ROOT, "oesis-contracts", "oesis-contracts")


def check_version_manifest() -> list[str]:
    """Verify the cross-repo version manifest exists and is parseable."""
    errors: list[str] = []
    manifest_path = SPECS_ROOT / "version-manifest.json"
    if not manifest_path.is_file():
        errors.append("version-manifest.json not found at specs repo root")
        return errors

    try:
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        errors.append(f"version-manifest.json is not valid JSON: {e}")
        return errors

    required_keys = ["format_version", "repos", "lanes", "generated_at"]
    for key in required_keys:
        if key not in manifest:
            errors.append(f"version-manifest.json missing required key: {key}")

    return errors


def main() -> int:
    print("OESIS cross-repo consistency check")
    print("=" * 50)

    all_errors: list[str] = []

    checks = [
        ("Example sync (oesis-contracts <-> runtime)", check_example_sync),
        ("Schema coverage (every schema has an example)", check_schema_coverage),
        ("Runtime lane alignment", check_runtime_lane_alignment),
        ("Contracts-bundle manifest freshness", check_manifest_freshness),
        ("Hardware cross-reference validation", check_hardware_cross_refs),
        ("Contracts cross-reference validation", check_contracts_cross_refs),
        ("Version manifest", check_version_manifest),
    ]

    for name, check_fn in checks:
        print(f"\n{name}...")
        errors = check_fn()
        if errors:
            for e in errors:
                print(f"  {FAIL} {e}")
            all_errors.extend(errors)
        else:
            print(f"  {PASS}")

    print(f"\n{'=' * 50}")
    if all_errors:
        print(f"{FAIL} {len(all_errors)} issue(s) found")
        return 1
    else:
        print(f"{PASS} All checks passed")
        return 0


if __name__ == "__main__":
    sys.exit(main())
