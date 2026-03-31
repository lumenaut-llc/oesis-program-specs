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
    parcel_context_path = DOC_EXAMPLES / "parcel-context.example.json"
    shared_signal_path = DOC_EXAMPLES / "shared-neighborhood-signal.example.json"
    raw_public_weather_path = DOC_EXAMPLES / "raw-public-weather.example.json"
    raw_public_smoke_path = DOC_EXAMPLES / "raw-public-smoke.example.json"
    node_packet = json.loads(node_packet_path.read_text(encoding="utf-8"))
    parcel_context = json.loads(parcel_context_path.read_text(encoding="utf-8"))
    shared_signal = json.loads(shared_signal_path.read_text(encoding="utf-8"))
    raw_public_weather = json.loads(raw_public_weather_path.read_text(encoding="utf-8"))
    raw_public_smoke = json.loads(raw_public_smoke_path.read_text(encoding="utf-8"))

    normalized = run_script(
        INGEST_DIR / "normalize_packet.py",
        str(node_packet_path),
        "--parcel-id",
        "parcel_demo_001",
    )
    public_context = run_script(
        INGEST_DIR / "normalize_public_weather_context.py",
        str(raw_public_weather_path),
    )
    public_smoke_context = run_script(
        INGEST_DIR / "normalize_public_smoke_context.py",
        str(raw_public_smoke_path),
    )

    with tempfile.TemporaryDirectory() as tmpdir:
        normalized_path = Path(tmpdir) / "normalized-observation.json"
        normalized_path.write_text(json.dumps(normalized), encoding="utf-8")

        public_context_path = Path(tmpdir) / "public-context-weather.json"
        public_context_path.write_text(json.dumps(public_context), encoding="utf-8")

        public_smoke_context_path = Path(tmpdir) / "public-context-smoke.json"
        public_smoke_context_path.write_text(json.dumps(public_smoke_context), encoding="utf-8")

        infer_args = [str(normalized_path)]
        if computed_at:
            infer_args.extend(["--computed-at", computed_at])
        infer_args.extend(["--parcel-context", str(parcel_context_path)])
        infer_args.extend(["--shared-neighborhood-signal", str(shared_signal_path)])
        infer_args.extend(["--public-context", str(public_context_path)])
        infer_args.extend(["--public-context", str(public_smoke_context_path)])
        parcel_state = run_script(INFERENCE_DIR / "infer_parcel_state.py", *infer_args)

        parcel_state_path = Path(tmpdir) / "parcel-state.json"
        parcel_state_path.write_text(json.dumps(parcel_state), encoding="utf-8")
        parcel_view = run_script(PARCEL_DIR / "format_parcel_view.py", str(parcel_state_path))
        evidence_summary = run_script(PARCEL_DIR / "format_evidence_summary.py", str(parcel_state_path))

    return {
        "node_packet": node_packet,
        "parcel_context": parcel_context,
        "shared_neighborhood_signal": shared_signal,
        "raw_public_weather": raw_public_weather,
        "raw_public_smoke": raw_public_smoke,
        "public_context": public_context,
        "public_smoke_context": public_smoke_context,
        "normalized_observation": normalized,
        "parcel_state": parcel_state,
        "parcel_view": parcel_view,
        "evidence_summary": evidence_summary,
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
