#!/usr/bin/env python3
"""
Concatenate frozen v0.1 technical markdown into one printable bundle.

Reads only; writes to build/print/ under the program-specs repo (gitignored).
Does not modify source documents.
"""

from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

# Paths relative to oesis-program-specs repository root
CORE_SOURCES = [
    "architecture/current/technical-philosophy.md",
    "architecture/current/reference-stack.md",
    "architecture/current/minimum-functioning-v0.1.md",
    "architecture/current/v0.1-runtime-modules.md",
    "architecture/current/v0.1-acceptance-criteria.md",
    "architecture/current/architecture-object-map.md",
    "architecture/current/implementation-posture.md",
    "architecture/current/component-boundaries.md",
    "architecture/current/milestone-roadmap.md",
    "architecture/current/pre-1.0-version-progression.md",
]

EXTRA_SOURCES_SPECS = [
    "architecture/system/technical-philosophy-and-architecture.md",
    "architecture/system/integrated-parcel-system-spec.md",
    "software/v0.1/README.md",
    "release/v.0.1/implementation-status-matrix.md",
    "software/operator-quickstart.md",
]

BENCH_AIR_SOURCES = [
    "hardware/bench-air-node/README.md",
    "hardware/bench-air-node/build-guide.md",
    "hardware/bench-air-node/operator-runbook.md",
]


def repo_root() -> Path:
    return Path(__file__).resolve().parent.parent.parent


def default_runtime_readme(specs_root: Path) -> Path | None:
    p = specs_root.parent / "oesis-runtime" / "README.md"
    return p if p.is_file() else None


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def build_bundle(
    *,
    specs_root: Path,
    include_extras: bool,
    include_bench_air: bool,
    runtime_readme: Path | None,
) -> str:
    lines: list[str] = []
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    lines.append("# OESIS technical v0.1 — printable bundle\n\n")
    lines.append(
        "Generated read-only concatenation of canonical specs. "
        "Source files are unchanged.\n\n"
    )
    lines.append(f"_Bundle assembled: {now}_\n\n")
    lines.append("---\n\n")

    def append_file(rel_or_abs: str | Path, label: str | None = None) -> None:
        path = Path(rel_or_abs) if Path(rel_or_abs).is_absolute() else specs_root / rel_or_abs
        if not path.is_file():
            try:
                missing_label = path.resolve().relative_to(specs_root.resolve())
            except ValueError:
                missing_label = path
            lines.append(f"## Missing: `{missing_label}`\n\n")
            lines.append("_File not found; skipped._\n\n---\n\n")
            return
        try:
            rel = path.resolve().relative_to(specs_root.resolve())
        except ValueError:
            rel = path
        title = label or str(rel).replace("\\", "/")
        lines.append(f"## Source: `{title}`\n\n")
        lines.append(read_text(path).rstrip() + "\n\n---\n\n")

    for rel in CORE_SOURCES:
        append_file(rel)

    if runtime_readme and runtime_readme.is_file():
        try:
            rt_label = runtime_readme.resolve().relative_to(specs_root.parent.resolve())
        except ValueError:
            rt_label = runtime_readme.name
        append_file(runtime_readme, label=str(rt_label).replace("\\", "/"))

    if include_extras:
        for rel in EXTRA_SOURCES_SPECS:
            append_file(rel)

    if include_bench_air:
        for rel in BENCH_AIR_SOURCES:
            append_file(rel)

    return "".join(lines).rstrip() + "\n"


def run_pandoc(md_path: Path, pdf_path: Path | None) -> None:
    if not shutil.which("pandoc"):
        print("error: pandoc not found on PATH; install pandoc or omit --pdf", file=sys.stderr)
        raise SystemExit(1)
    out = pdf_path or md_path.with_suffix(".pdf")
    out.parent.mkdir(parents=True, exist_ok=True)
    cmd = ["pandoc", str(md_path), "-o", str(out)]
    subprocess.run(cmd, check=True)
    print(f"Wrote {out}")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "-o",
        "--output",
        type=Path,
        help="Output markdown path (default: <repo>/build/print/v0.1-technical-bundle.md)",
    )
    parser.add_argument(
        "--extras",
        action="store_true",
        help="Append alignment docs, implementation matrix, operator quickstart",
    )
    parser.add_argument(
        "--bench-air",
        action="store_true",
        help="Append bench-air-node README, build-guide, operator-runbook",
    )
    parser.add_argument(
        "--no-runtime-readme",
        action="store_true",
        help="Do not include sibling oesis-runtime/README.md even if present",
    )
    parser.add_argument(
        "--pdf",
        action="store_true",
        help="After writing markdown, run pandoc to produce a .pdf beside the .md",
    )
    parser.add_argument(
        "--pdf-output",
        type=Path,
        default=None,
        help="PDF path when using --pdf (default: same basename as markdown output)",
    )
    args = parser.parse_args()

    specs_root = repo_root()
    out = args.output or (specs_root / "build" / "print" / "v0.1-technical-bundle.md")
    out.parent.mkdir(parents=True, exist_ok=True)

    runtime = None if args.no_runtime_readme else default_runtime_readme(specs_root)

    body = build_bundle(
        specs_root=specs_root,
        include_extras=args.extras,
        include_bench_air=args.bench_air,
        runtime_readme=runtime,
    )
    out.write_text(body, encoding="utf-8")
    print(f"Wrote {out} ({len(body):,} bytes)")
    if args.pdf:
        run_pandoc(out, args.pdf_output)


if __name__ == "__main__":
    main()
