#!/usr/bin/env python3
"""Scan a directory tree for lean-structure cleanup candidates."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
from collections import Counter, defaultdict
from pathlib import Path

SILENT_PRUNE_DIR_NAMES = {".git"}
REPORTED_PRUNE_DIR_NAMES = {
    ".cache",
    ".astro",
    ".mypy_cache",
    ".next",
    ".nox",
    ".pio",
    ".pytest_cache",
    ".ruff_cache",
    ".tox",
    ".turbo",
    ".venv",
    "__pycache__",
    "build",
    "coverage",
    "dist",
    "htmlcov",
    "node_modules",
}
OS_NOISE_FILES = {".DS_Store", "Thumbs.db"}
GENERATED_FILE_SUFFIXES = {".a", ".class", ".dll", ".dylib", ".o", ".pyc", ".pyd", ".pyo", ".so"}
TEXT_DUPLICATE_EXTENSIONS = {
    ".cfg",
    ".css",
    ".csv",
    ".html",
    ".ini",
    ".js",
    ".json",
    ".jsx",
    ".md",
    ".mjs",
    ".mts",
    ".py",
    ".sh",
    ".sql",
    ".toml",
    ".ts",
    ".tsx",
    ".txt",
    ".yaml",
    ".yml",
}
ALLOWLISTED_REPEATED_BASENAMES = {
    ".DS_Store",
    ".gitignore",
    "__init__.py",
    "README.md",
    "NOTICE.md",
    "architecture.md",
    "build-guide.md",
    "calibration.md",
    "firmware-notes.md",
    "interfaces.md",
    "launch.json",
    "open-questions.md",
    "operator-runbook.md",
    "platformio.ini",
    "serial-json-contract.md",
    "secrets.example.h",
    "wiring.md",
}
MAX_DUPLICATE_FILE_BYTES = 512 * 1024


def relpath(path: Path, root: Path) -> str:
    try:
        return str(path.relative_to(root))
    except ValueError:
        return str(path)


def should_prune_and_report(dirname: str) -> bool:
    return dirname in REPORTED_PRUNE_DIR_NAMES or dirname.endswith(".egg-info")


def visible_children(path: Path) -> list[Path]:
    children: list[Path] = []
    for child in path.iterdir():
        if child.name in SILENT_PRUNE_DIR_NAMES:
            continue
        if child.is_file() and child.name in OS_NOISE_FILES:
            continue
        children.append(child)
    return children


def should_hash_for_duplicates(path: Path) -> bool:
    return path.suffix.lower() in TEXT_DUPLICATE_EXTENSIONS and path.stat().st_size <= MAX_DUPLICATE_FILE_BYTES


def normalized_text_hash(path: Path) -> str | None:
    try:
        data = path.read_bytes()
    except OSError:
        return None
    normalized = data.replace(b"\r\n", b"\n").replace(b"\r", b"\n").strip()
    return hashlib.sha256(normalized).hexdigest()


def capped_list(items: list[str], limit: int) -> dict[str, object]:
    sorted_items = sorted(items)
    return {
        "count": len(sorted_items),
        "items": sorted_items[:limit],
        "truncated": max(len(sorted_items) - limit, 0),
    }


def scan_tree(root: Path, limit: int) -> dict[str, object]:
    root = root.resolve()

    os_noise_files: list[str] = []
    generated_dirs: list[str] = []
    generated_files: list[str] = []
    symlinks: list[str] = []
    empty_dirs: list[str] = []
    low_signal_dirs: list[dict[str, str]] = []
    basename_paths: dict[str, list[str]] = defaultdict(list)
    duplicate_hashes: dict[tuple[str, str], list[str]] = defaultdict(list)
    top_level_file_counts: Counter[str] = Counter()
    files_scanned = 0
    dirs_scanned = 0

    for current, dirnames, filenames in os.walk(root, topdown=True):
        current_path = Path(current)
        dirs_scanned += 1

        kept_dirnames: list[str] = []
        for dirname in sorted(dirnames):
            child = current_path / dirname
            if dirname in SILENT_PRUNE_DIR_NAMES:
                continue
            if should_prune_and_report(dirname):
                generated_dirs.append(relpath(child, root))
                continue
            kept_dirnames.append(dirname)
        dirnames[:] = kept_dirnames

        if current_path != root:
            children = visible_children(current_path)
            if not children:
                empty_dirs.append(relpath(current_path, root))
            elif len(children) == 1:
                only_child = children[0]
                if only_child.is_file():
                    low_signal_dirs.append(
                        {
                            "path": relpath(current_path, root),
                            "only_child": only_child.name,
                        }
                    )

        for filename in sorted(filenames):
            file_path = current_path / filename
            rel = relpath(file_path, root)

            if file_path.is_symlink():
                symlinks.append(rel)
                continue

            files_scanned += 1
            basename_paths[filename].append(rel)

            if filename in OS_NOISE_FILES:
                os_noise_files.append(rel)
                continue

            if any(suffix in GENERATED_FILE_SUFFIXES for suffix in file_path.suffixes):
                generated_files.append(rel)

            rel_parts = Path(rel).parts
            if rel_parts:
                top_level_file_counts[rel_parts[0]] += 1

            if should_hash_for_duplicates(file_path):
                digest = normalized_text_hash(file_path)
                if digest:
                    duplicate_hashes[(file_path.suffix.lower(), digest)].append(rel)

    duplicate_groups = [
        capped_list(paths, limit)
        for paths in duplicate_hashes.values()
        if len(paths) > 1
    ]
    duplicate_groups.sort(key=lambda item: (-int(item["count"]), tuple(item["items"])))

    repeated_basenames = []
    for basename, paths in basename_paths.items():
        if len(paths) < 2 or basename in ALLOWLISTED_REPEATED_BASENAMES:
            continue
        repeated_basenames.append(
            {
                "name": basename,
                "count": len(paths),
                "paths": sorted(paths)[:limit],
                "truncated": max(len(paths) - limit, 0),
            }
        )
    repeated_basenames.sort(key=lambda item: (-item["count"], item["name"]))

    low_signal_dirs.sort(key=lambda item: item["path"])

    return {
        "root": str(root),
        "summary": {
            "files_scanned": files_scanned,
            "dirs_scanned": dirs_scanned,
            "top_level_file_counts": top_level_file_counts.most_common(limit),
        },
        "high_confidence_cleanup": {
            "os_noise_files": capped_list(os_noise_files, limit),
            "generated_dirs": capped_list(generated_dirs, limit),
            "generated_files": capped_list(generated_files, limit),
        },
        "needs_review": {
            "exact_duplicate_groups": duplicate_groups[:limit],
            "repeated_basenames": repeated_basenames[:limit],
            "low_signal_dirs": low_signal_dirs[:limit],
            "empty_dirs": capped_list(empty_dirs, limit),
            "symlinks": capped_list(symlinks, limit),
        },
    }


def print_capped_block(label: str, payload: dict[str, object]) -> None:
    count = int(payload["count"])
    print(f"- {label}: {count}")
    for item in payload["items"]:
        print(f"  - {item}")
    if payload["truncated"]:
        print(f"  - ... {payload['truncated']} more")


def print_report(report: dict[str, object]) -> None:
    summary = report["summary"]
    cleanup = report["high_confidence_cleanup"]
    review = report["needs_review"]

    print("Summary")
    print(f"- Root: {report['root']}")
    print(f"- Files scanned: {summary['files_scanned']}")
    print(f"- Directories scanned: {summary['dirs_scanned']}")
    print("- Top-level file distribution:")
    for name, count in summary["top_level_file_counts"]:
        print(f"  - {name}: {count}")
    if not summary["top_level_file_counts"]:
        print("  - none")

    print("\nHigh-confidence cleanup")
    print_capped_block("OS noise files", cleanup["os_noise_files"])
    print_capped_block("Generated directories", cleanup["generated_dirs"])
    print_capped_block("Generated files", cleanup["generated_files"])

    print("\nNeeds review")
    duplicate_groups = review["exact_duplicate_groups"]
    print(f"- Exact duplicate groups: {len(duplicate_groups)}")
    for group in duplicate_groups:
        print(f"  - group of {group['count']}")
        for path in group["items"]:
            print(f"    - {path}")
        if group["truncated"]:
            print(f"    - ... {group['truncated']} more")

    repeated_basenames = review["repeated_basenames"]
    print(f"- Repeated non-template basenames: {len(repeated_basenames)}")
    for item in repeated_basenames:
        print(f"  - {item['name']}: {item['count']}")
        for path in item["paths"]:
            print(f"    - {path}")
        if item["truncated"]:
            print(f"    - ... {item['truncated']} more")

    low_signal_dirs = review["low_signal_dirs"]
    print(f"- Low-signal directories: {len(low_signal_dirs)}")
    for item in low_signal_dirs:
        print(f"  - {item['path']} (only child: {item['only_child']})")

    print_capped_block("Empty directories", review["empty_dirs"])
    print_capped_block("Symlinks", review["symlinks"])


def main() -> int:
    parser = argparse.ArgumentParser(description="Scan a directory tree for lean-structure cleanup candidates.")
    parser.add_argument("path", nargs="?", default=".", help="Directory to scan")
    parser.add_argument("--limit", type=int, default=12, help="Maximum items to print per section")
    parser.add_argument("--json", action="store_true", help="Emit JSON instead of a text report")
    args = parser.parse_args()

    root = Path(args.path)
    if not root.exists():
        parser.error(f"path does not exist: {root}")
    if not root.is_dir():
        parser.error(f"path is not a directory: {root}")
    if args.limit < 1:
        parser.error("--limit must be at least 1")

    report = scan_tree(root, args.limit)
    if args.json:
        print(json.dumps(report, indent=2))
    else:
        print_report(report)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
