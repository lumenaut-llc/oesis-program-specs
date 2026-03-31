#!/usr/bin/env python3

import argparse
import json
import subprocess
import sys
import tempfile
from pathlib import Path


PROGRAM_ROOT = Path(__file__).resolve().parents[2]
DOC_EXAMPLES = PROGRAM_ROOT.parent / "docs" / "data-model" / "examples"
INGEST_DIR = PROGRAM_ROOT / "ingest-service" / "scripts"
INFERENCE_DIR = PROGRAM_ROOT / "inference-engine" / "scripts"
PARCEL_DIR = PROGRAM_ROOT / "parcel-platform" / "scripts"


def run_script(script: Path, *args: str) -> dict:
    result = subprocess.run(
        [sys.executable, str(script), *args],
        capture_output=True,
        text=True,
        check=False,
    )
    if result.returncode != 0:
        raise RuntimeError(f"{script.name} failed:\n{result.stderr.strip()}")
    return json.loads(result.stdout)


def build_pipeline(*, computed_at: str | None) -> dict:
    node_packet_path = DOC_EXAMPLES / "node-observation.example.json"
    node_packet = json.loads(node_packet_path.read_text(encoding="utf-8"))

    normalized = run_script(
        INGEST_DIR / "normalize_packet.py",
        str(node_packet_path),
        "--parcel-id",
        "parcel_demo_001",
    )

    with tempfile.TemporaryDirectory() as tmpdir:
        normalized_path = Path(tmpdir) / "normalized-observation.json"
        normalized_path.write_text(json.dumps(normalized), encoding="utf-8")

        infer_args = [str(normalized_path)]
        if computed_at:
            infer_args.extend(["--computed-at", computed_at])
        parcel_state = run_script(INFERENCE_DIR / "infer_parcel_state.py", *infer_args)

        parcel_state_path = Path(tmpdir) / "parcel-state.json"
        parcel_state_path.write_text(json.dumps(parcel_state), encoding="utf-8")
        parcel_view = run_script(PARCEL_DIR / "format_parcel_view.py", str(parcel_state_path))

    return {
        "node_packet": node_packet,
        "normalized_observation": normalized,
        "parcel_state": parcel_state,
        "parcel_view": parcel_view,
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run the reference RHI pipeline from packet to parcel view.")
    parser.add_argument(
        "--computed-at",
        default="2026-03-30T19:46:00Z",
        help="Optional RFC 3339 timestamp passed to the inference stage.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    try:
        output = build_pipeline(computed_at=args.computed_at)
    except Exception as exc:
        print(f"ERROR reference pipeline: {exc}", file=sys.stderr)
        return 1

    print(json.dumps(output, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    sys.exit(main())
