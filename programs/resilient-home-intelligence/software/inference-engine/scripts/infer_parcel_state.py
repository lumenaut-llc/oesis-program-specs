#!/usr/bin/env python3

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
EXAMPLES_DIR = ROOT / "docs" / "data-model" / "examples"


class InferenceError(Exception):
    pass


def load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def now_iso() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def clamp_probability(value: float) -> float:
    return max(0.0, min(1.0, round(value, 2)))


def status_from_probability(probability: float, *, unknown_floor: float = 0.2) -> str:
    if probability < unknown_floor:
        return "unknown"
    if probability < 0.4:
        return "safe"
    if probability < 0.7:
        return "caution"
    return "unsafe"


def parse_time(ts: str) -> datetime:
    return datetime.fromisoformat(ts.replace("Z", "+00:00"))


def validate_normalized_observation(payload: dict):
    required = [
        "observation_id",
        "node_id",
        "parcel_id",
        "observed_at",
        "ingested_at",
        "observation_type",
        "values",
        "health",
        "provenance",
    ]
    for field in required:
        if field not in payload:
            raise InferenceError(f"normalized observation missing required field: {field}")

    if payload["observation_type"] != "air.node.snapshot":
        raise InferenceError("observation_type must be air.node.snapshot")


def derive_hazards(payload: dict) -> dict:
    values = payload["values"]
    health = payload["health"]
    raw_packet = payload.get("raw_packet", {})
    location_mode = raw_packet.get("location_mode", "indoor")

    smoke_probability = 0.18
    gas_resistance = values.get("gas_resistance_ohm")
    if gas_resistance is not None:
        if gas_resistance < 50000:
            smoke_probability = 0.82
        elif gas_resistance < 100000:
            smoke_probability = 0.58
        elif gas_resistance < 180000:
            smoke_probability = 0.42
        else:
            smoke_probability = 0.24

    heat_probability = 0.12
    temperature_c = values.get("temperature_c_primary")
    if temperature_c is not None:
        if temperature_c >= 40:
            heat_probability = 0.9
        elif temperature_c >= 34:
            heat_probability = 0.7
        elif temperature_c >= 29:
            heat_probability = 0.46
        elif temperature_c >= 24:
            heat_probability = 0.27

    flood_probability = 0.03
    if location_mode == "outdoor":
        flood_probability = 0.08

    if not health.get("wifi_connected", False):
        smoke_probability += 0.03
        heat_probability += 0.03

    if health.get("read_failures_total", 0) > 0:
        smoke_probability -= 0.05
        heat_probability -= 0.05

    return {
        "smoke_probability": clamp_probability(smoke_probability),
        "flood_probability": clamp_probability(flood_probability),
        "heat_probability": clamp_probability(heat_probability),
    }


def derive_confidence(payload: dict, hazards: dict, *, now: datetime) -> float:
    observed_at = parse_time(payload["observed_at"])
    age_seconds = max(0, int((now - observed_at).total_seconds()))

    confidence = 0.62
    if payload["health"].get("read_failures_total", 0) > 0:
        confidence -= 0.1
    if not payload["health"].get("wifi_connected", False):
        confidence -= 0.04
    if age_seconds > 900:
        confidence -= 0.1
    if age_seconds > 3600:
        confidence -= 0.15

    if max(hazards.values()) < 0.2:
        confidence -= 0.08

    return clamp_probability(confidence)


def derive_reasons(payload: dict, hazards: dict, confidence: float, *, stale: bool) -> list[str]:
    reasons = []
    gas_resistance = payload["values"].get("gas_resistance_ohm")
    temperature_c = payload["values"].get("temperature_c_primary")

    if gas_resistance is not None:
        if gas_resistance < 100000:
            reasons.append("Air observation suggests an elevated smoke or air-quality anomaly signal.")
        elif gas_resistance < 180000:
            reasons.append("Indoor air observations show a moderate gas-trend change worth watching.")

    if temperature_c is not None:
        if temperature_c >= 34:
            reasons.append("Temperature is in a range that may support heat-related caution.")
        elif temperature_c >= 24:
            reasons.append("Temperature is elevated enough to contribute modest heat concern.")

    if stale:
        reasons.append("The latest observation is aging out and may no longer reflect current parcel conditions.")

    if confidence < 0.5:
        reasons.append("Confidence is limited because the current decision uses sparse single-node evidence.")
    else:
        reasons.append("The current decision is based on a single homeowner-owned node without confirming public context.")

    if not reasons:
        reasons.append("Available evidence is limited, so the parcel state remains mostly unknown.")

    return reasons


def infer_parcel_state(payload: dict, *, computed_at: str | None = None) -> dict:
    validate_normalized_observation(payload)

    now = parse_time(computed_at) if computed_at else datetime.now(timezone.utc)
    computed_at = (computed_at or now_iso())
    observed_at = parse_time(payload["observed_at"])
    age_seconds = max(0, int((now - observed_at).total_seconds()))
    stale = age_seconds > 900

    hazards = derive_hazards(payload)
    confidence = derive_confidence(payload, hazards, now=now)
    reasons = derive_reasons(payload, hazards, confidence, stale=stale)

    smoke_status = status_from_probability(hazards["smoke_probability"])
    heat_status = status_from_probability(hazards["heat_probability"])
    flood_status = status_from_probability(hazards["flood_probability"], unknown_floor=0.1)

    stay_status = smoke_status if hazards["smoke_probability"] >= hazards["heat_probability"] else heat_status
    enter_status = "unknown" if confidence < 0.6 else stay_status
    escape_status = "unsafe" if max(hazards.values()) >= 0.8 else "safe"
    asset_status = "caution" if max(hazards.values()) >= 0.4 else "safe"

    if stale and confidence < 0.6:
        stay_status = "unknown"
        enter_status = "unknown"

    return {
        "parcel_id": payload["parcel_id"],
        "computed_at": computed_at,
        "stay_status": stay_status,
        "enter_status": enter_status,
        "escape_status": escape_status,
        "asset_status": asset_status,
        "confidence": confidence,
        "evidence_mode": "local_only",
        "reasons": reasons,
        "hazards": hazards,
        "freshness": {
            "latest_observation_at": payload["observed_at"],
            "seconds_since_latest": age_seconds,
            "stale": stale,
        },
        "provenance_summary": {
            "observation_count": 1,
            "source_modes": [
                payload["provenance"]["source_kind"]
            ],
            "observation_refs": [
                payload["observation_id"]
            ],
        },
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Infer a parcel-state snapshot from a normalized observation.")
    parser.add_argument(
        "input",
        nargs="?",
        default=str(EXAMPLES_DIR / "normalized-observation.example.json"),
        help="Path to a normalized observation JSON file.",
    )
    parser.add_argument(
        "--computed-at",
        default=None,
        help="Optional RFC 3339 timestamp to use as the computation time.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    input_path = Path(args.input).resolve()

    try:
        payload = load_json(input_path)
        result = infer_parcel_state(payload, computed_at=args.computed_at)
    except (InferenceError, FileNotFoundError, json.JSONDecodeError, KeyError) as exc:
        print(f"ERROR {input_path}: {exc}", file=sys.stderr)
        return 1

    print(json.dumps(result, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    sys.exit(main())
