#!/usr/bin/env python3
"""
Cross-repo sync engine for the OESIS multi-repo architecture.

Propagates changes from oesis-contracts (source of truth) into the four
downstream repos: oesis-runtime, oesis-public-site, oesis-hardware, and
oesis-program-specs (self).

Designed to be called both from developer machines (side-by-side sibling
checkouts) and from CI (arbitrary paths). Every subcommand accepts explicit
--contracts-root and per-target --*-root flags so it is safe to run in a
GitHub Actions workspace where repos may be checked out to non-standard
locations.

Subcommands:
    sync-runtime-assets          Mirror contracts/v{0.1,1.0,1.5}/examples/*.json
                                 into runtime/oesis/assets/v*/examples/.
    build-public-content-bundle  Stamp contracts commit into the site's
                                 generated bundle; verify URL references.
    sync-hardware-refs           Verify that contract citations in hardware docs
                                 still resolve in contracts at the given ref.
    sync-specs-refs              Update version-manifest.json's
                                 oesis-contracts.last_verified_commit.

Flags:
    --contracts-ref SHA          Record this commit in generated metadata.
                                 Defaults to current HEAD of --contracts-root.
    --dry-run                    Describe changes but do not write.
    --json                       Emit a machine-readable summary on stdout
                                 (used by CI to populate PR bodies).

Exit codes:
    0  Clean (no changes needed) or changes applied successfully.
    1  Errors encountered (missing inputs, unresolvable refs, write failures).
    2  Drift detected in --dry-run mode (changes would be made but weren't).

Run from oesis-program-specs repo root (default paths):
    python3 scripts/repo_split.py sync-runtime-assets
    python3 scripts/repo_split.py build-public-content-bundle
    python3 scripts/repo_split.py sync-hardware-refs
    python3 scripts/repo_split.py sync-specs-refs
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

SPECS_ROOT_DEFAULT = Path(__file__).resolve().parent.parent
SIBLINGS_ROOT = SPECS_ROOT_DEFAULT.parent

CANONICAL_EXAMPLE_LANES = ["v0.1", "v1.0", "v1.5"]
ALL_LANES = ["v0.1", "v0.2", "v0.3", "v0.4", "v0.5", "v1.0", "v1.5"]

PASS = "\033[32mPASS\033[0m"
FAIL = "\033[31mFAIL\033[0m"
WARN = "\033[33mWARN\033[0m"
INFO = "\033[36mINFO\033[0m"


def file_hash(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()[:16]


def resolve_head(repo_root: Path) -> str | None:
    """Return the commit SHA at HEAD of a repo, or None if unresolvable."""
    try:
        out = subprocess.check_output(
            ["git", "-C", str(repo_root), "rev-parse", "HEAD"],
            stderr=subprocess.DEVNULL,
        )
        return out.decode().strip()
    except (subprocess.CalledProcessError, FileNotFoundError):
        # Fallback: read .git/HEAD directly (handles CI shallow clones).
        head = repo_root / ".git" / "HEAD"
        if not head.is_file():
            return None
        ref = head.read_text().strip()
        if ref.startswith("ref: "):
            ref_path = repo_root / ".git" / ref.split("ref: ")[1]
            if ref_path.is_file():
                return ref_path.read_text().strip()
            # Packed-refs lookup
            packed = repo_root / ".git" / "packed-refs"
            if packed.is_file():
                ref_name = ref.split("ref: ")[1]
                for line in packed.read_text().splitlines():
                    if line.endswith(" " + ref_name):
                        return line.split()[0]
        else:
            return ref  # detached HEAD: the ref IS the sha
        return None


def utc_now() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


# --------------------------------------------------------------------------
# sync-runtime-assets
# --------------------------------------------------------------------------

def cmd_sync_runtime_assets(
    contracts_root: Path,
    runtime_root: Path,
    contracts_ref: str,
    dry_run: bool,
) -> tuple[int, dict]:
    summary = {
        "command": "sync-runtime-assets",
        "contracts_ref": contracts_ref,
        "lanes": {},
        "files_copied": 0,
        "files_removed": 0,
        "files_unchanged": 0,
        "dry_run": dry_run,
    }
    errors: list[str] = []

    if not contracts_root.is_dir():
        errors.append(f"contracts root not found: {contracts_root}")
    if not runtime_root.is_dir():
        errors.append(f"runtime root not found: {runtime_root}")
    if errors:
        summary["errors"] = errors
        return 1, summary

    had_diff = False

    for lane in CANONICAL_EXAMPLE_LANES:
        lane_summary = {"copied": [], "removed": [], "unchanged": 0}

        src_dir = contracts_root / lane / "examples"
        dst_dir = runtime_root / "oesis" / "assets" / lane / "examples"

        if not src_dir.is_dir():
            print(f"  {WARN} {lane}: contracts examples dir missing at {src_dir}")
            summary["lanes"][lane] = lane_summary
            continue

        src_files = {f.name: f for f in src_dir.glob("*.json")}
        dst_files = {f.name: f for f in dst_dir.glob("*.json")} if dst_dir.is_dir() else {}

        # Copy / overwrite
        for name, src in sorted(src_files.items()):
            dst = dst_dir / name
            needs_copy = not dst.is_file() or file_hash(src) != file_hash(dst)
            if needs_copy:
                had_diff = True
                lane_summary["copied"].append(name)
                summary["files_copied"] += 1
                if not dry_run:
                    dst_dir.mkdir(parents=True, exist_ok=True)
                    dst.write_bytes(src.read_bytes())
            else:
                lane_summary["unchanged"] += 1
                summary["files_unchanged"] += 1

        # Remove runtime-only JSON examples that contracts no longer owns
        # (protects against stale files being kept around forever).
        for name in sorted(set(dst_files) - set(src_files)):
            had_diff = True
            lane_summary["removed"].append(name)
            summary["files_removed"] += 1
            if not dry_run:
                (dst_dir / name).unlink()

        summary["lanes"][lane] = lane_summary
        status = PASS if not (lane_summary["copied"] or lane_summary["removed"]) else INFO
        print(
            f"  {status} {lane}: "
            f"copied={len(lane_summary['copied'])} "
            f"removed={len(lane_summary['removed'])} "
            f"unchanged={lane_summary['unchanged']}"
        )

    if dry_run and had_diff:
        return 2, summary
    return 0, summary


# --------------------------------------------------------------------------
# build-public-content-bundle
# --------------------------------------------------------------------------

# Regex targets the generated bundle object. Only the outermost literal is
# rewritten; we never touch the `as const` suffix or the preamble comment.
_BUNDLE_OBJECT_RE = re.compile(
    r"^(export const publicContentBundle\s*=\s*)(\{.*?\})(\s*as const;)",
    re.DOTALL | re.MULTILINE,
)


def cmd_build_public_content_bundle(
    contracts_root: Path,
    public_site_root: Path,
    specs_root: Path,
    contracts_ref: str,
    dry_run: bool,
) -> tuple[int, dict]:
    summary = {
        "command": "build-public-content-bundle",
        "contracts_ref": contracts_ref,
        "bundle_path": None,
        "updated_fields": [],
        "dry_run": dry_run,
    }
    errors: list[str] = []

    bundle_path = public_site_root / "src" / "generated" / "publicContentBundle.ts"
    if not bundle_path.is_file():
        errors.append(f"publicContentBundle.ts not found at {bundle_path}")
        summary["errors"] = errors
        return 1, summary

    summary["bundle_path"] = str(bundle_path)

    text = bundle_path.read_text(encoding="utf-8")
    match = _BUNDLE_OBJECT_RE.search(text)
    if not match:
        errors.append(
            "could not locate the publicContentBundle object literal — "
            "file layout may have changed"
        )
        summary["errors"] = errors
        return 1, summary

    try:
        bundle = json.loads(match.group(2))
    except json.JSONDecodeError as e:
        errors.append(f"bundle object is not JSON-parseable: {e}")
        summary["errors"] = errors
        return 1, summary

    specs_commit = resolve_head(specs_root) or bundle.get("source_commit")
    new_fields = {
        "generated_at": utc_now(),
        "source_commit": specs_commit,
        "contracts_verified_commit": contracts_ref,
    }

    updated = {}
    for k, v in new_fields.items():
        if bundle.get(k) != v:
            updated[k] = {"old": bundle.get(k), "new": v}
            bundle[k] = v

    summary["updated_fields"] = sorted(updated.keys())

    if not updated:
        print(f"  {PASS} bundle already up to date at {contracts_ref[:12]}")
        return 0, summary

    # Re-emit the object. Preserve the existing key order where possible by
    # round-tripping through json with sort_keys=False; Python dicts keep
    # insertion order, and we only mutated existing values plus appended one
    # new key (contracts_verified_commit) if it did not exist.
    new_obj = json.dumps(bundle, indent=2)
    new_text = text[: match.start(2)] + new_obj + text[match.end(2):]

    if dry_run:
        print(f"  {INFO} would update fields: {', '.join(summary['updated_fields'])}")
        return 2, summary

    bundle_path.write_text(new_text, encoding="utf-8")
    print(f"  {PASS} updated fields: {', '.join(summary['updated_fields'])}")
    return 0, summary


# --------------------------------------------------------------------------
# sync-hardware-refs
# --------------------------------------------------------------------------

# Hardware does not embed contract files; it cites contract URLs/lane tokens
# in prose. We verify those references still resolve at the given contracts
# ref, but do not rewrite anything without explicit maintainer intent.

_CONTRACTS_URL_RE = re.compile(
    r"https://github\.com/lumenaut-llc/oesis-contracts/blob/main/([^\s\)\"`]+)"
)


def cmd_sync_hardware_refs(
    contracts_root: Path,
    hardware_root: Path,
    contracts_ref: str,
    dry_run: bool,
) -> tuple[int, dict]:
    summary = {
        "command": "sync-hardware-refs",
        "contracts_ref": contracts_ref,
        "broken_urls": [],
        "files_scanned": 0,
        "urls_checked": 0,
        "dry_run": dry_run,
    }
    errors: list[str] = []

    if not contracts_root.is_dir():
        errors.append(f"contracts root not found: {contracts_root}")
    if not hardware_root.is_dir():
        errors.append(f"hardware root not found: {hardware_root}")
    if errors:
        summary["errors"] = errors
        return 1, summary

    for md_file in hardware_root.rglob("*.md"):
        if ".git" in md_file.parts or "node_modules" in md_file.parts:
            continue
        try:
            content = md_file.read_text(encoding="utf-8")
        except (UnicodeDecodeError, PermissionError):
            continue

        summary["files_scanned"] += 1
        for m in _CONTRACTS_URL_RE.finditer(content):
            summary["urls_checked"] += 1
            rel = m.group(1).rstrip("/").rstrip("`").rstrip(".").rstrip(",")
            if not rel:
                continue
            target = contracts_root / rel
            if not target.exists():
                try:
                    rel_md = md_file.relative_to(hardware_root)
                except ValueError:
                    rel_md = md_file
                summary["broken_urls"].append(
                    {"file": str(rel_md), "url_path": rel}
                )

    if summary["broken_urls"]:
        for b in summary["broken_urls"]:
            print(f"  {FAIL} {b['file']}: contracts path '{b['url_path']}' missing")
        return 1, summary

    print(
        f"  {PASS} {summary['urls_checked']} contract URL(s) across "
        f"{summary['files_scanned']} hardware file(s) resolve at {contracts_ref[:12]}"
    )
    return 0, summary


# --------------------------------------------------------------------------
# sync-specs-refs
# --------------------------------------------------------------------------

def cmd_sync_specs_refs(
    specs_root: Path,
    contracts_ref: str,
    dry_run: bool,
) -> tuple[int, dict]:
    summary = {
        "command": "sync-specs-refs",
        "contracts_ref": contracts_ref,
        "updated": False,
        "old_commit": None,
        "dry_run": dry_run,
    }
    errors: list[str] = []

    manifest_path = specs_root / "version-manifest.json"
    if not manifest_path.is_file():
        errors.append(f"version-manifest.json not found at {manifest_path}")
        summary["errors"] = errors
        return 1, summary

    try:
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        errors.append(f"version-manifest.json is not valid JSON: {e}")
        summary["errors"] = errors
        return 1, summary

    repos = manifest.get("repos", {})
    contracts_entry = repos.get("oesis-contracts")
    if contracts_entry is None:
        errors.append("version-manifest.json has no repos.oesis-contracts entry")
        summary["errors"] = errors
        return 1, summary

    old = contracts_entry.get("last_verified_commit")
    summary["old_commit"] = old

    if old == contracts_ref:
        print(f"  {PASS} version-manifest already at {contracts_ref[:12]}")
        return 0, summary

    contracts_entry["last_verified_commit"] = contracts_ref
    manifest["generated_at"] = utc_now()
    summary["updated"] = True

    if dry_run:
        print(
            f"  {INFO} would update oesis-contracts.last_verified_commit "
            f"{(old or 'none')[:12]} -> {contracts_ref[:12]}"
        )
        return 2, summary

    # Preserve trailing newline if original had one
    original = manifest_path.read_text(encoding="utf-8")
    trailing = "\n" if original.endswith("\n") else ""
    manifest_path.write_text(
        json.dumps(manifest, indent=2) + trailing, encoding="utf-8"
    )
    print(
        f"  {PASS} updated oesis-contracts.last_verified_commit "
        f"{(old or 'none')[:12]} -> {contracts_ref[:12]}"
    )
    return 0, summary


# --------------------------------------------------------------------------
# CLI
# --------------------------------------------------------------------------

def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        description="OESIS cross-repo sync engine",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    p.add_argument(
        "--specs-root",
        type=Path,
        default=SPECS_ROOT_DEFAULT,
        help="Path to oesis-program-specs checkout (default: script's parent).",
    )
    p.add_argument(
        "--contracts-root",
        type=Path,
        default=SIBLINGS_ROOT / "oesis-contracts",
        help="Path to oesis-contracts checkout.",
    )
    p.add_argument(
        "--runtime-root",
        type=Path,
        default=SIBLINGS_ROOT / "oesis-runtime",
        help="Path to oesis-runtime checkout.",
    )
    p.add_argument(
        "--public-site-root",
        type=Path,
        default=SIBLINGS_ROOT / "oesis-public-site",
        help="Path to oesis-public-site checkout.",
    )
    p.add_argument(
        "--hardware-root",
        type=Path,
        default=SIBLINGS_ROOT / "oesis-hardware",
        help="Path to oesis-hardware checkout.",
    )
    p.add_argument(
        "--contracts-ref",
        default=None,
        help="Commit SHA to record in generated metadata. "
             "Defaults to current HEAD of --contracts-root.",
    )
    p.add_argument(
        "--dry-run",
        action="store_true",
        help="Describe changes but do not write. Exits 2 if changes would be made.",
    )
    p.add_argument(
        "--json",
        action="store_true",
        help="Emit a machine-readable summary on stdout.",
    )
    p.add_argument(
        "subcommand",
        choices=[
            "sync-runtime-assets",
            "build-public-content-bundle",
            "sync-hardware-refs",
            "sync-specs-refs",
            "all",
        ],
        help="Which sync step to run. 'all' runs every step in sequence.",
    )
    return p


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)

    contracts_ref = args.contracts_ref or resolve_head(args.contracts_root)
    if not contracts_ref:
        print(
            f"  {FAIL} could not determine contracts commit ref "
            f"(pass --contracts-ref or ensure .git/ exists at {args.contracts_root})",
            file=sys.stderr,
        )
        return 1

    steps = (
        [args.subcommand]
        if args.subcommand != "all"
        else [
            "sync-runtime-assets",
            "build-public-content-bundle",
            "sync-hardware-refs",
            "sync-specs-refs",
        ]
    )

    overall_rc = 0
    summaries = []

    for step in steps:
        print(f"\n[{step}] contracts @ {contracts_ref[:12]}")
        if step == "sync-runtime-assets":
            rc, s = cmd_sync_runtime_assets(
                args.contracts_root, args.runtime_root, contracts_ref, args.dry_run
            )
        elif step == "build-public-content-bundle":
            rc, s = cmd_build_public_content_bundle(
                args.contracts_root,
                args.public_site_root,
                args.specs_root,
                contracts_ref,
                args.dry_run,
            )
        elif step == "sync-hardware-refs":
            rc, s = cmd_sync_hardware_refs(
                args.contracts_root, args.hardware_root, contracts_ref, args.dry_run
            )
        elif step == "sync-specs-refs":
            rc, s = cmd_sync_specs_refs(
                args.specs_root, contracts_ref, args.dry_run
            )
        else:  # pragma: no cover
            print(f"unknown step: {step}", file=sys.stderr)
            return 1

        summaries.append(s)
        # 2 means "dry-run would diverge" — propagate but keep running so CI
        # can see the full picture before exiting non-zero.
        if rc == 1:
            overall_rc = 1
        elif rc == 2 and overall_rc == 0:
            overall_rc = 2

    if args.json:
        print(json.dumps({"steps": summaries, "exit_code": overall_rc}, indent=2))

    return overall_rc


if __name__ == "__main__":
    sys.exit(main())
