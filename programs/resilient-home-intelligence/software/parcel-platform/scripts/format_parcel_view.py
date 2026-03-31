#!/usr/bin/env python3

import argparse
import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
EXAMPLES_DIR = ROOT / "docs" / "data-model" / "examples"


class ParcelViewError(Exception):
    pass


def load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def validate_parcel_state(payload: dict):
    required = [
        "parcel_id",
        "computed_at",
        "stay_status",
        "enter_status",
        "escape_status",
        "asset_status",
        "confidence",
        "evidence_mode",
        "reasons",
        "hazards",
        "freshness",
        "provenance_summary",
    ]
    for field in required:
        if field not in payload:
            raise ParcelViewError(f"parcel state missing required field: {field}")


def format_summary(payload: dict) -> str:
    statuses = {
        "stay": payload["stay_status"],
        "enter": payload["enter_status"],
        "escape": payload["escape_status"],
        "asset": payload["asset_status"],
    }
    priority = {
        "unsafe": 3,
        "caution": 2,
        "safe": 1,
        "unknown": 0,
    }
    dominant_status = max(statuses.values(), key=lambda value: priority.get(value, -1))
    return (
        f"Parcel status is {dominant_status} with "
        f"{int(round(payload['confidence'] * 100))}% confidence "
        f"based on {payload['evidence_mode'].replace('_', ' ')} evidence."
    )


def build_parcel_view(payload: dict) -> dict:
    validate_parcel_state(payload)

    return {
        "parcel_id": payload["parcel_id"],
        "computed_at": payload["computed_at"],
        "statuses": {
            "stay": payload["stay_status"],
            "enter": payload["enter_status"],
            "escape": payload["escape_status"],
            "asset": payload["asset_status"],
        },
        "confidence": payload["confidence"],
        "evidence_mode": payload["evidence_mode"],
        "summary": format_summary(payload),
        "reasons": payload["reasons"],
        "hazards": payload["hazards"],
        "freshness": payload["freshness"],
        "provenance_summary": payload["provenance_summary"],
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Format a parcel-state snapshot into a parcel-platform response.")
    parser.add_argument(
        "input",
        nargs="?",
        default=str(EXAMPLES_DIR / "parcel-state.example.json"),
        help="Path to a parcel-state JSON file.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    input_path = Path(args.input).resolve()

    try:
        payload = load_json(input_path)
        formatted = build_parcel_view(payload)
    except (ParcelViewError, FileNotFoundError, json.JSONDecodeError, KeyError) as exc:
        print(f"ERROR {input_path}: {exc}", file=sys.stderr)
        return 1

    print(json.dumps(formatted, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    sys.exit(main())
