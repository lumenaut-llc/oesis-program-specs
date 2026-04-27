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
PUBLIC_SITE_ROOT = SPECS_ROOT.parent / "oesis-public-site"
# Non-git satellite working dirs. Soft-skipped when not present (CI does not
# clone these — they live as local working dirs maintained outside the
# release-fanout flow, so coverage here is best-effort local validation).
BUILDS_ROOT = SPECS_ROOT.parent / "oesis-builds"
WIKI_ROOT = SPECS_ROOT.parent / "oesis-wiki"

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


def _resolve_head(repo_root: Path) -> str | None:
    """Read the commit SHA at HEAD without invoking git; returns None on failure."""
    head = repo_root / ".git" / "HEAD"
    if not head.is_file():
        return None
    ref = head.read_text().strip()
    if ref.startswith("ref: "):
        ref_path = repo_root / ".git" / ref.split("ref: ")[1]
        if ref_path.is_file():
            return ref_path.read_text().strip()
        packed = repo_root / ".git" / "packed-refs"
        if packed.is_file():
            ref_name = ref.split("ref: ")[1]
            for line in packed.read_text().splitlines():
                if line.endswith(" " + ref_name):
                    return line.split()[0]
        return None
    return ref  # detached HEAD


def check_public_site_bundle_freshness() -> list[str]:
    """Ensure publicContentBundle.ts records a contracts commit that still exists.

    The site stamps contracts_verified_commit whenever the sync workflow runs.
    Missing or stale SHAs here indicate the site never received a fanout or
    a maintainer edited the bundle out-of-band.
    """
    errors: list[str] = []
    if not check_repo_exists(PUBLIC_SITE_ROOT, "oesis-public-site"):
        return errors  # soft-skip when site is not cloned (e.g., narrow CI jobs)

    bundle_path = (
        PUBLIC_SITE_ROOT / "src" / "generated" / "publicContentBundle.ts"
    )
    if not bundle_path.is_file():
        errors.append(f"publicContentBundle.ts not found at {bundle_path}")
        return errors

    import re
    match = re.search(
        r'"contracts_verified_commit"\s*:\s*"([0-9a-f]{7,40})"',
        bundle_path.read_text(encoding="utf-8"),
    )
    if not match:
        print(
            f"  {WARN} publicContentBundle.ts has no contracts_verified_commit "
            f"field; run repo_split.py build-public-content-bundle to stamp it"
        )
        return errors

    recorded = match.group(1)
    current = _resolve_head(CONTRACTS_ROOT)
    if current and not current.startswith(recorded) and not recorded.startswith(current):
        print(
            f"  {WARN} public-site records contracts {recorded[:12]}, but "
            f"oesis-contracts HEAD is {current[:12]} — fanout may be lagging"
        )

    return errors


def check_hardware_contract_urls() -> list[str]:
    """Re-use the shared GitHub URL validator against oesis-hardware.

    Unlike the specs-side URL check (which scans program-specs for links TO
    hardware and contracts), this walks oesis-hardware's own markdown and
    verifies any contracts URLs resolve in the sibling checkout.
    """
    errors: list[str] = []
    if not check_repo_exists(HARDWARE_ROOT, "oesis-hardware"):
        return errors
    if not check_repo_exists(CONTRACTS_ROOT, "oesis-contracts"):
        return errors

    import re
    url_pattern = re.compile(
        r"https://github\.com/lumenaut-llc/oesis-contracts/blob/main/([^\s\)\"`]+)"
    )

    for md_file in HARDWARE_ROOT.rglob("*.md"):
        if ".git" in md_file.parts or "node_modules" in md_file.parts:
            continue
        try:
            content = md_file.read_text(encoding="utf-8")
        except (UnicodeDecodeError, PermissionError):
            continue
        for m in url_pattern.finditer(content):
            rel = m.group(1).rstrip("/").rstrip("`").rstrip(".").rstrip(",")
            if not rel or rel.startswith("."):
                continue
            if not (CONTRACTS_ROOT / rel).exists():
                try:
                    rel_md = md_file.relative_to(HARDWARE_ROOT)
                except ValueError:
                    rel_md = md_file
                errors.append(
                    f"{rel_md}: broken oesis-contracts URL — '{rel}' not found"
                )
    return errors


def check_builds_cross_refs() -> list[str]:
    """Validate relative ../oesis-<repo>/ paths in oesis-builds markdown resolve.

    oesis-builds is a non-git working dir with markdown links to sibling repos
    via relative paths (e.g., ../../../oesis-hardware/v0.1/bench-air-node/...).
    Without CI for builds itself, these references can break silently when a
    sibling repo restructures. Soft-skips when builds is not present locally.
    """
    errors: list[str] = []
    if not check_repo_exists(BUILDS_ROOT, "oesis-builds"):
        return errors  # soft-skip: builds is not git-cloned in CI today

    import re
    # Stop set excludes whitespace, markdown link/wikilink terminators, common
    # prose punctuation. `|` and `]` are wikilink syntax (`[[path|display]]`).
    pattern = re.compile(r"(?:\.\./)+oesis[_-][a-z_-]+/[^\s)\"'\]`|#?]+")

    for md_file in BUILDS_ROOT.rglob("*.md"):
        if ".git" in md_file.parts or "node_modules" in md_file.parts:
            continue
        # Skip template files — they intentionally contain placeholder paths
        # like `../oesis-hardware/<node>/firmware/` for the reader to fill in.
        if "_template" in md_file.parts or "_templates" in md_file.parts:
            continue
        try:
            content = md_file.read_text(encoding="utf-8")
        except (UnicodeDecodeError, PermissionError):
            continue

        for match in pattern.finditer(content):
            rel = match.group(0).rstrip("/").rstrip(".").rstrip(",")
            if not rel:
                continue
            # Skip template placeholders like <node>, <slug>, or glob patterns
            # like ../oesis-hardware/** (used in vault-scope documentation, not
            # as navigable paths).
            if "<" in rel or ">" in rel or "*" in rel:
                continue

            target = (md_file.parent / rel).resolve()
            # Wikilinks (`[[path]]`) and bare path mentions typically omit
            # the .md extension. If the literal path doesn't resolve, try
            # appending .md as a fallback before declaring drift. (Path.suffix
            # is unreliable when path segments contain dots, e.g. `v.0.1/...`.)
            if not target.exists():
                with_md = target.parent / (target.name + ".md")
                if with_md.exists():
                    continue

            if not target.exists():
                try:
                    rel_md = md_file.relative_to(BUILDS_ROOT)
                except ValueError:
                    rel_md = md_file
                errors.append(
                    f"oesis-builds/{rel_md}: broken relative path — "
                    f"'{match.group(0)}' does not resolve"
                )

    return errors


def check_wiki_cross_refs() -> list[str]:
    """Validate textual oesis-<repo>/<path> references in oesis-wiki markdown.

    oesis-wiki uses prose mentions rather than markdown links (e.g.,
    backtick-wrapped `oesis-hardware/v0.1/<family>/file.md`). These are logical
    pointers; they should reference real files relative to the oesis_master
    parent dir. Restricts matching to references that end in a recognised
    file extension to avoid noisy false positives on dir-name mentions.
    Soft-skips when wiki is not present locally.
    """
    errors: list[str] = []
    if not check_repo_exists(WIKI_ROOT, "oesis-wiki"):
        return errors  # soft-skip

    import re
    # Only validate refs that end in a recognised file extension
    pattern = re.compile(
        r"oesis[_-][a-z_-]+/[a-zA-Z0-9._/-]+\."
        r"(?:md|json|csv|toml|yaml|yml|h|cpp|py|sh|ino|ts|tsx|js)"
    )

    # Phrases on the same line indicating an intentionally-aspirational
    # reference (file expected to exist later, not yet written). These are
    # author signals that the target file is acknowledged as missing — not
    # drift. Wiki vault stewardship (oesis-wiki/CLAUDE.md) means we can't
    # edit these files from this script anyway; better to skip cleanly.
    placeholder_markers = (
        "not yet written",
        "not yet created",
        "not yet added",
        "not yet exists",
        "expected:",
        "expected to be at",
        "pending:",
        "(planned)",
        "(tbd)",
        "to be added",
        "will live",
        "when added",
    )

    for md_file in WIKI_ROOT.rglob("*.md"):
        if ".git" in md_file.parts or "node_modules" in md_file.parts:
            continue
        # Skip template files
        if "_template" in md_file.parts or "_templates" in md_file.parts:
            continue
        try:
            content = md_file.read_text(encoding="utf-8")
        except (UnicodeDecodeError, PermissionError):
            continue

        # Build a list of (ref, line_text) tuples so we can check line context
        for match in pattern.finditer(content):
            rel = match.group(0)
            if not rel:
                continue
            # Skip refs containing template placeholders or globs
            if "<" in rel or ">" in rel or "*" in rel:
                continue
            # Skip wikilink-display segments leaked into the match
            if "|" in rel:
                rel = rel.split("|", 1)[0]
            # Find the line containing this ref; skip if it has a placeholder marker
            line_start = content.rfind("\n", 0, match.start()) + 1
            line_end = content.find("\n", match.end())
            if line_end == -1:
                line_end = len(content)
            line = content[line_start:line_end].lower()
            if any(marker in line for marker in placeholder_markers):
                continue

            target = WIKI_ROOT.parent / rel
            if not target.exists():
                try:
                    rel_md = md_file.relative_to(WIKI_ROOT)
                except ValueError:
                    rel_md = md_file
                errors.append(
                    f"oesis-wiki/{rel_md}: broken sibling-repo path — "
                    f"'{rel}' not found in oesis_master"
                )

    return errors


def check_specs_verified_commit() -> list[str]:
    """Warn if version-manifest's recorded oesis-contracts commit lags HEAD."""
    manifest_path = SPECS_ROOT / "version-manifest.json"
    if not manifest_path.is_file():
        return []
    if not check_repo_exists(CONTRACTS_ROOT, "oesis-contracts"):
        return []

    try:
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return []

    recorded = (
        manifest.get("repos", {})
        .get("oesis-contracts", {})
        .get("last_verified_commit")
    )
    current = _resolve_head(CONTRACTS_ROOT)
    if recorded and current and recorded != current:
        print(
            f"  {WARN} version-manifest records oesis-contracts {recorded[:12]}, "
            f"but HEAD is {current[:12]} — run repo_split.py sync-specs-refs"
        )
    return []


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
        ("Public-site bundle freshness", check_public_site_bundle_freshness),
        ("Hardware contracts URL validity", check_hardware_contract_urls),
        ("Builds cross-reference validation (relative paths)", check_builds_cross_refs),
        ("Wiki cross-reference validation (sibling-repo paths)", check_wiki_cross_refs),
        ("Specs verified-commit freshness", check_specs_verified_commit),
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
