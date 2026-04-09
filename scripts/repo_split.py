#!/usr/bin/env python3

from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import shutil
import subprocess
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
PROGRAM_ROOT = REPO_ROOT
CONTRACTS_ROOT = PROGRAM_ROOT / "contracts"
CONTRACT_EXAMPLES_ROOT = CONTRACTS_ROOT / "examples"
CONTRACT_SCHEMAS_ROOT = CONTRACTS_ROOT / "schemas"
CONTRACT_V10_ROOT = CONTRACTS_ROOT / "v1.0"
CONTRACT_V10_EXAMPLES_ROOT = CONTRACT_V10_ROOT / "examples"
CONTRACT_V10_SCHEMAS_ROOT = CONTRACT_V10_ROOT / "schemas"
INFERENCE_CONFIG_ROOT = PROGRAM_ROOT / "software" / "inference-engine" / "config"
INFERENCE_CONFIG_V10_ROOT = INFERENCE_CONFIG_ROOT / "v1.0"
RUNTIME_REPO_ROOT = Path(os.environ.get("OESIS_RUNTIME_REPO_DIR", str(REPO_ROOT.parent / "oesis-runtime"))).expanduser().resolve()
PUBLIC_SITE_REPO_ROOT = Path(os.environ.get("OESIS_PUBLIC_SITE_REPO_DIR", str(REPO_ROOT.parent / "oesis-public-site"))).expanduser().resolve()
ARTIFACTS_ROOT = REPO_ROOT / "artifacts"
RUNTIME_REPO_ASSETS_ROOT = RUNTIME_REPO_ROOT / "oesis" / "assets"
RUNTIME_REPO_EXAMPLES_ROOT = RUNTIME_REPO_ASSETS_ROOT / "examples"
RUNTIME_REPO_INFERENCE_CONFIG_ROOT = RUNTIME_REPO_ASSETS_ROOT / "config" / "inference"
RUNTIME_REPO_V10_ROOT = RUNTIME_REPO_ASSETS_ROOT / "v1.0"
RUNTIME_REPO_V10_EXAMPLES_ROOT = RUNTIME_REPO_V10_ROOT / "examples"
RUNTIME_REPO_V10_INFERENCE_CONFIG_ROOT = RUNTIME_REPO_V10_ROOT / "config" / "inference"
PUBLIC_SITE_GENERATED_ROOT = PUBLIC_SITE_REPO_ROOT / "src" / "generated"

DEFAULT_PUBLIC_RELEASE_TAG = "v1.0"
PROGRAM_ROOT_REL = ""
PRIVACY_ROOT_REL = f"{PROGRAM_ROOT_REL}legal/privacy/"
LEGAL_ROOT_REL = f"{PROGRAM_ROOT_REL}legal/"
REPO_BLOB_BASE = "https://github.com/lumenaut-llc/oesis-program-specs/blob/main/"


def release_root_rel(tag: str) -> str:
    return f"{PROGRAM_ROOT_REL}release/{tag}/"


def default_public_release_title(tag: str) -> str:
    if tag == "v1.0":
        return "OESIS public preview v1.0 packet"
    if tag == "2026-04-14":
        return "April 14, 2026 public preview"
    return f"OESIS public preview ({tag})"


def default_public_release_summary(tag: str) -> str:
    if tag == "v1.0":
        return (
            "Release-scoped public packet and publication boundary for the Astro preview site; "
            "canonical markdown roots under release/v1.0/."
        )
    return "Current release-scoped public packet and publication boundary for the Astro preview site."


def now_iso() -> str:
    return dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def ensure_clean_dir(path: Path) -> None:
    if path.exists():
        shutil.rmtree(path)
    path.mkdir(parents=True, exist_ok=True)


def copy_tree(src: Path, dst: Path) -> None:
    if dst.exists():
        shutil.rmtree(dst)
    shutil.copytree(src, dst, dirs_exist_ok=False)


def overlay_tree(src: Path, dst: Path) -> None:
    if not src.exists():
        return
    dst.mkdir(parents=True, exist_ok=True)
    shutil.copytree(src, dst, dirs_exist_ok=True)


def copy_files(src_paths: list[Path], dst_dir: Path) -> None:
    dst_dir.mkdir(parents=True, exist_ok=True)
    for src in src_paths:
        shutil.copy2(src, dst_dir / src.name)


def copy_root_files(src_dir: Path, dst_dir: Path) -> None:
    dst_dir.mkdir(parents=True, exist_ok=True)
    for src in sorted(src_dir.iterdir()):
        if src.is_file():
            shutil.copy2(src, dst_dir / src.name)


def should_skip_path(path: Path) -> bool:
    skip_names = {
        "node_modules",
        "dist",
        "build",
        ".astro",
        "__pycache__",
    }
    return path.name in skip_names


def git_head() -> str | None:
    result = subprocess.run(
        ["git", "rev-parse", "HEAD"],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
        check=False,
    )
    if result.returncode != 0:
        return None
    return result.stdout.strip() or None


def repo_blob_base() -> str:
    configured = os.environ.get("OESIS_REPO_BLOB_BASE")
    if configured:
        return configured

    result = subprocess.run(
        ["git", "remote", "get-url", "origin"],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
        check=False,
    )
    if result.returncode == 0:
        remote = result.stdout.strip()
        if remote.startswith("https://github.com/") and remote.endswith(".git"):
            return remote.removesuffix(".git") + "/blob/main/"
        if remote.startswith("git@github.com:") and remote.endswith(".git"):
            slug = remote.removeprefix("git@github.com:").removesuffix(".git")
            return f"https://github.com/{slug}/blob/main/"

    return REPO_BLOB_BASE


def repo_relative(path: Path) -> str:
    return path.relative_to(REPO_ROOT).as_posix()


def write_json(path: Path, payload: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def normalize_lane(lane: str) -> str:
    # Keep the split tooling aligned with the current runtime policy:
    # one frozen `v0.1` baseline plus one additive future lane until a second
    # accepted pre-1.0 slice is real enough to justify broader lane support.
    if lane not in {"v0.1", "v1.0"}:
        raise SystemExit(f"unsupported lane: {lane}")
    return lane


def sync_runtime_assets(*, lane: str = "v0.1") -> None:
    lane = normalize_lane(lane)
    if not RUNTIME_REPO_ROOT.exists():
        raise SystemExit(f"runtime repo not found: {RUNTIME_REPO_ROOT}")
    if lane == "v0.1":
        copy_tree(CONTRACT_EXAMPLES_ROOT, RUNTIME_REPO_EXAMPLES_ROOT)
        ensure_clean_dir(RUNTIME_REPO_INFERENCE_CONFIG_ROOT)
        copy_root_files(INFERENCE_CONFIG_ROOT, RUNTIME_REPO_INFERENCE_CONFIG_ROOT)
        return

    ensure_clean_dir(RUNTIME_REPO_V10_EXAMPLES_ROOT)
    overlay_tree(CONTRACT_V10_EXAMPLES_ROOT, RUNTIME_REPO_V10_EXAMPLES_ROOT)
    ensure_clean_dir(RUNTIME_REPO_V10_INFERENCE_CONFIG_ROOT)
    overlay_tree(INFERENCE_CONFIG_V10_ROOT, RUNTIME_REPO_V10_INFERENCE_CONFIG_ROOT)


def build_contracts_bundle(destination: Path, *, lane: str = "v0.1") -> Path:
    lane = normalize_lane(lane)
    ensure_clean_dir(destination)
    schemas_dst = destination / "schemas"
    examples_dst = destination / "examples"
    copy_tree(CONTRACT_SCHEMAS_ROOT, schemas_dst)
    copy_tree(CONTRACT_EXAMPLES_ROOT, examples_dst)
    if lane == "v1.0":
        overlay_tree(CONTRACT_V10_SCHEMAS_ROOT, schemas_dst)
        overlay_tree(CONTRACT_V10_EXAMPLES_ROOT, examples_dst)

    example_names = sorted(path.name for path in examples_dst.glob("*.json"))
    schema_names = sorted(path.name for path in schemas_dst.glob("*.json"))
    manifest = {
        "bundle_version": DEFAULT_PUBLIC_RELEASE_TAG,
        "generated_at": now_iso(),
        "source_repo": "oesis-program-specs",
        "source_commit": git_head(),
        "lane": lane,
        "examples": {name.removesuffix(".example.json"): f"examples/{name}" for name in example_names},
        "schemas": {name.removesuffix(".schema.json"): f"schemas/{name}" for name in schema_names},
        "schema_version_set": ["oesis.bench-air.v1"],
        "compatibility": {
            "runtime_min_version": "0.1.0",
            "runtime_max_version": None,
        },
        "source_roots": {
            "examples": [
                repo_relative(CONTRACT_EXAMPLES_ROOT),
                repo_relative(CONTRACT_V10_EXAMPLES_ROOT),
            ] if lane == "v1.0" else [repo_relative(CONTRACT_EXAMPLES_ROOT)],
            "schemas": [
                repo_relative(CONTRACT_SCHEMAS_ROOT),
                repo_relative(CONTRACT_V10_SCHEMAS_ROOT),
            ] if lane == "v1.0" else [repo_relative(CONTRACT_SCHEMAS_ROOT)],
        },
    }
    write_json(destination / "manifest.json", manifest)
    return destination


def build_public_content_bundle(
    destination: Path,
    *,
    release_tag: str = DEFAULT_PUBLIC_RELEASE_TAG,
    release_title: str | None = None,
    release_summary: str | None = None,
) -> Path:
    ensure_clean_dir(destination)

    rr = release_root_rel(release_tag)
    title = release_title if release_title is not None else default_public_release_title(release_tag)
    summary = release_summary if release_summary is not None else default_public_release_summary(release_tag)

    bundle = {
        "bundle_version": release_tag,
        "generated_at": now_iso(),
        "source_repo": "oesis-program-specs",
        "source_commit": git_head(),
        "repoBlobBase": repo_blob_base(),
        "programRoot": PROGRAM_ROOT_REL,
        "releaseRoot": rr,
        "privacyGovernanceRoot": PRIVACY_ROOT_REL,
        "legalRoot": LEGAL_ROOT_REL,
        "approvedAnchors": [
            "/#snapshot",
            "/#roadmap",
            "/#how-it-works",
            "/#hardware-specs",
            "/#software-specs",
            "/#governance",
            "/#diagrams",
        ],
        "approvedSourceRoots": [
            rr,
            PRIVACY_ROOT_REL,
            f"{PROGRAM_ROOT_REL}architecture/",
            LEGAL_ROOT_REL,
        ],
        "excludedFromPublicNavigation": [
            f"{rr}reviewer-packet-index.md",
            f"{rr}publish-internal-map.md",
            f"{rr}preview-execution-plan.md",
            f"{rr}launch-readiness-checklist.md",
            f"{LEGAL_ROOT_REL}counsel-questions/",
            f"{LEGAL_ROOT_REL}provisional-*",
        ],
        "activePublicRelease": {
            "id": release_tag,
            "title": title,
            "summary": summary,
        },
    }
    write_json(destination / "public-content-bundle.json", bundle)

    generated_ts = """export const publicContentBundle = %s as const;\n""" % json.dumps(bundle, indent=2)
    if not PUBLIC_SITE_REPO_ROOT.exists():
        raise SystemExit(f"public site repo not found: {PUBLIC_SITE_REPO_ROOT}")
    write_text(PUBLIC_SITE_GENERATED_ROOT / "publicContentBundle.ts", generated_ts)
    return destination


def run_command(command: list[str], *, cwd: Path) -> dict[str, object]:
    result = subprocess.run(command, cwd=cwd, capture_output=True, text=True, check=False)
    return {
        "command": command,
        "cwd": str(cwd),
        "exit_code": result.returncode,
        "stdout": result.stdout,
        "stderr": result.stderr,
        "ok": result.returncode == 0,
    }


def build_runtime_evidence_bundle(destination: Path) -> Path:
    ensure_clean_dir(destination)

    runtime_cwd = RUNTIME_REPO_ROOT if RUNTIME_REPO_ROOT.exists() else REPO_ROOT
    commands = [
        ["make", "oesis-validate"],
        ["make", "oesis-check"],
        ["make", "oesis-http-check"],
    ]
    results = [run_command(command, cwd=runtime_cwd) for command in commands]

    for result in results:
        command_name = "_".join(result["command"])
        write_text(destination / f"{command_name}.stdout.log", result["stdout"])
        write_text(destination / f"{command_name}.stderr.log", result["stderr"])

    manifest = {
        "bundle_version": DEFAULT_PUBLIC_RELEASE_TAG,
        "generated_at": now_iso(),
        "source_repo": "oesis-runtime",
        "source_commit": git_head(),
        "checks": [
            {
                "command": " ".join(result["command"]),
                "exit_code": result["exit_code"],
                "ok": result["ok"],
                "stdout_log": f"{'_'.join(result['command'])}.stdout.log",
                "stderr_log": f"{'_'.join(result['command'])}.stderr.log",
                "cwd": result["cwd"],
            }
            for result in results
        ],
        "supported_surfaces": [
            "example payload validation",
            "reference packet-to-parcel pipeline",
            "local ingest API",
            "local inference API",
            "local parcel-platform API",
        ],
    }
    write_json(destination / "manifest.json", manifest)

    if not all(result["ok"] for result in results):
        raise SystemExit("runtime evidence bundle failed because one or more runtime checks did not pass")
    return destination


def init_git_repo(path: Path) -> None:
    if (path / ".git").exists():
        return
    subprocess.run(["git", "init"], cwd=path, capture_output=True, text=True, check=False)


def write_runtime_repo_files(destination: Path) -> None:
    write_text(
        destination / "README.md",
        "# OESIS Runtime\n\n"
        "Standalone runtime repository for the Open Environmental Sensing and Inference System reference services.\n",
    )
    write_text(
        destination / ".gitignore",
        "__pycache__/\n*.pyc\n.env\n.env.local\n",
    )
    write_text(
        destination / "pyproject.toml",
        "[build-system]\n"
        'requires = ["setuptools>=68"]\n'
        'build-backend = "setuptools.build_meta"\n\n'
        "[project]\n"
        'name = "oesis-runtime"\n'
        'version = "0.1.0"\n'
        'description = "Reference runtime services for Open Environmental Sensing and Inference System."\n'
        'requires-python = ">=3.11"\n\n'
        "[tool.setuptools.packages.find]\n"
        'include = ["oesis*"]\n\n'
        "[tool.setuptools.package-data]\n"
        'oesis = ["assets/examples/*.json", "assets/config/inference/*.json"]\n',
    )
    write_text(
        destination / "Makefile",
        ".PHONY: oesis-demo oesis-validate oesis-check oesis-http-check\n\n"
        "oesis-demo:\n\tpython3 -m oesis.parcel_platform.reference_pipeline\n\n"
        "oesis-validate:\n\tpython3 -m oesis.ingest.validate_examples\n\n"
        "oesis-check:\n\t./scripts/oesis_smoke_check.sh\n\n"
        "oesis-http-check:\n\t./scripts/oesis_http_smoke_check.sh\n",
    )


def write_site_repo_files(destination: Path) -> None:
    write_text(
        destination / "README.md",
        "# OESIS Public Site\n\n"
        "Standalone public preview site for the Open Environmental Sensing and Inference System release surface.\n",
    )
    write_text(
        destination / ".gitignore",
        "node_modules/\ndist/\nbuild/\n.astro/\n.env\n.env.local\n",
    )


def extract_runtime_repo(destination: Path) -> Path:
    raise SystemExit(
        "runtime extraction has already completed; use the canonical sibling repo "
        f"at {RUNTIME_REPO_ROOT} and refresh it through the bundle/sync commands."
    )


def extract_site_repo(destination: Path) -> Path:
    raise SystemExit(
        "site extraction has already completed; use the canonical sibling repo "
        f"at {PUBLIC_SITE_REPO_ROOT} and refresh it through the public-content bundle."
    )


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Utility commands for the OESIS repo split.")
    subparsers = parser.add_subparsers(dest="command", required=True)

    sync_runtime = subparsers.add_parser(
        "sync-runtime-assets",
        help="Copy runtime examples and config into oesis-owned assets.",
    )
    sync_runtime.add_argument(
        "--lane",
        default="v0.1",
        choices=("v0.1", "v1.0"),
        help="Version lane to sync. Defaults to the frozen v0.1 lane.",
    )

    contracts = subparsers.add_parser("build-contracts-bundle", help="Build the contracts bundle artifact.")
    contracts.add_argument(
        "--destination",
        default=str(ARTIFACTS_ROOT / "contracts-bundle"),
        help="Output directory for the contracts bundle.",
    )
    contracts.add_argument(
        "--lane",
        default="v0.1",
        choices=("v0.1", "v1.0"),
        help="Version lane to bundle. Defaults to the frozen v0.1 lane.",
    )

    runtime = subparsers.add_parser("build-runtime-evidence-bundle", help="Build the runtime evidence bundle artifact.")
    runtime.add_argument(
        "--destination",
        default=str(ARTIFACTS_ROOT / "runtime-evidence-bundle"),
        help="Output directory for the runtime evidence bundle.",
    )

    public = subparsers.add_parser("build-public-content-bundle", help="Build the public content bundle artifact.")
    public.add_argument(
        "--destination",
        default=str(ARTIFACTS_ROOT / "public-content-bundle"),
        help="Output directory for the public content bundle.",
    )
    public.add_argument(
        "--release-tag",
        default=DEFAULT_PUBLIC_RELEASE_TAG,
        help="Release folder name under release/ (default: v1.0).",
    )
    public.add_argument(
        "--release-title",
        default=None,
        help="activePublicRelease.title override (default: derived from tag).",
    )
    public.add_argument(
        "--release-summary",
        default=None,
        help="activePublicRelease.summary override (default: derived from tag).",
    )

    extract_site = subparsers.add_parser("extract-site-repo", help="Create the extracted public-site repository.")
    extract_site.add_argument(
        "--destination",
        default=str(REPO_ROOT.parent / "oesis-public-site"),
        help="Destination directory for the extracted site repository.",
    )

    extract_runtime = subparsers.add_parser("extract-runtime-repo", help="Create the extracted runtime repository.")
    extract_runtime.add_argument(
        "--destination",
        default=str(REPO_ROOT.parent / "oesis-runtime"),
        help="Destination directory for the extracted runtime repository.",
    )

    return parser.parse_args()


def main() -> int:
    args = parse_args()

    if args.command == "sync-runtime-assets":
        sync_runtime_assets(lane=args.lane)
        print(RUNTIME_REPO_ASSETS_ROOT if args.lane == "v0.1" else RUNTIME_REPO_V10_ROOT)
        return 0
    if args.command == "build-contracts-bundle":
        destination = build_contracts_bundle(Path(args.destination).resolve(), lane=args.lane)
        print(destination)
        return 0
    if args.command == "build-runtime-evidence-bundle":
        destination = build_runtime_evidence_bundle(Path(args.destination).resolve())
        print(destination)
        return 0
    if args.command == "build-public-content-bundle":
        destination = build_public_content_bundle(
            Path(args.destination).resolve(),
            release_tag=args.release_tag,
            release_title=args.release_title,
            release_summary=args.release_summary,
        )
        print(destination)
        return 0
    if args.command == "extract-site-repo":
        destination = extract_site_repo(Path(args.destination).resolve())
        print(destination)
        return 0
    if args.command == "extract-runtime-repo":
        destination = extract_runtime_repo(Path(args.destination).resolve())
        print(destination)
        return 0

    raise SystemExit(f"unsupported command: {args.command}")


if __name__ == "__main__":
    sys.exit(main())
