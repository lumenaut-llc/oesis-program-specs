#!/usr/bin/env python3

import argparse
import json
import sys
from pathlib import Path

from oesis.common.repo_paths import DOCS_EXAMPLES_DIR
from oesis.ingest.normalize_packet import normalize_packet
from oesis.ingest.normalize_public_smoke_context import normalize_public_smoke_context
from oesis.ingest.normalize_public_weather_context import normalize_public_weather_context
from oesis.inference.infer_parcel_state import combine_public_contexts, infer_parcel_state

from .format_evidence_summary import build_evidence_summary
from .format_parcel_view import build_parcel_view


def build_pipeline(*, computed_at: str | None) -> dict:
    node_packet_path = DOCS_EXAMPLES_DIR / "node-observation.example.json"
    parcel_context_path = DOCS_EXAMPLES_DIR / "parcel-context.example.json"
    shared_signal_path = DOCS_EXAMPLES_DIR / "shared-neighborhood-signal.example.json"
    raw_public_weather_path = DOCS_EXAMPLES_DIR / "raw-public-weather.example.json"
    raw_public_smoke_path = DOCS_EXAMPLES_DIR / "raw-public-smoke.example.json"
    node_packet = json.loads(node_packet_path.read_text(encoding="utf-8"))
    parcel_context = json.loads(parcel_context_path.read_text(encoding="utf-8"))
    shared_signal = json.loads(shared_signal_path.read_text(encoding="utf-8"))
    raw_public_weather = json.loads(raw_public_weather_path.read_text(encoding="utf-8"))
    raw_public_smoke = json.loads(raw_public_smoke_path.read_text(encoding="utf-8"))

    normalized = normalize_packet(
        node_packet,
        parcel_id="parcel_demo_001",
    )
    public_context = normalize_public_weather_context(raw_public_weather)
    public_smoke_context = normalize_public_smoke_context(raw_public_smoke)
    combined_public_context = combine_public_contexts([public_context, public_smoke_context])

    parcel_state = infer_parcel_state(
        normalized,
        computed_at=computed_at,
        parcel_context=parcel_context,
        shared_neighborhood_context=shared_signal,
        public_context=combined_public_context,
    )
    parcel_view = build_parcel_view(parcel_state)
    evidence_summary = build_evidence_summary(parcel_state)

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
    parser = argparse.ArgumentParser(
        description="Run the reference OESIS pipeline from packet to parcel view."
    )
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
