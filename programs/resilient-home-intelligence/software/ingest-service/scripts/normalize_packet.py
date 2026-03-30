#!/usr/bin/env python3

import argparse
import json
import sys
import uuid
from copy import deepcopy
from datetime import datetime, timezone
from pathlib import Path

from validate_examples import ValidationError, load_json, validate_node_observation


ROOT = Path(__file__).resolve().parents[3]
EXAMPLES_DIR = ROOT / "docs" / "data-model" / "examples"


def now_iso() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def make_ref(prefix: str) -> str:
    return f"{prefix}_{uuid.uuid4().hex[:12]}"


def build_values(payload: dict) -> dict:
    sensors = payload["sensors"]
    derived = deepcopy(payload.get("derived", {}))

    values = {}
    if "temperature_c_primary" in derived:
        values["temperature_c_primary"] = derived["temperature_c_primary"]
    elif sensors.get("sht45", {}).get("present"):
        values["temperature_c_primary"] = sensors["sht45"]["temperature_c"]

    if "relative_humidity_pct_primary" in derived:
        values["relative_humidity_pct_primary"] = derived["relative_humidity_pct_primary"]
    elif sensors.get("sht45", {}).get("present"):
        values["relative_humidity_pct_primary"] = sensors["sht45"]["relative_humidity_pct"]

    if "pressure_hpa" in derived:
        values["pressure_hpa"] = derived["pressure_hpa"]
    elif sensors.get("bme688", {}).get("present"):
        values["pressure_hpa"] = sensors["bme688"]["pressure_hpa"]

    if sensors.get("bme688", {}).get("present"):
        values["gas_resistance_ohm"] = sensors["bme688"]["gas_resistance_ohm"]

    if "voc_trend_source" in derived:
        values["voc_trend_source"] = derived["voc_trend_source"]

    return values


def normalize_packet(payload: dict, *, parcel_id: str | None = None, ingested_at: str | None = None) -> dict:
    validate_node_observation(payload)
    ingested_at = ingested_at or now_iso()

    normalized = {
        "observation_id": make_ref("obs"),
        "node_id": payload["node_id"],
        "parcel_id": parcel_id,
        "observed_at": payload["observed_at"],
        "ingested_at": ingested_at,
        "observation_type": "air.node.snapshot",
        "values": build_values(payload),
        "health": {
            "uptime_s": payload["health"]["uptime_s"],
            "wifi_connected": payload["health"]["wifi_connected"],
            "read_failures_total": payload["health"]["read_failures_total"],
        },
        "provenance": {
            "source_kind": "homeowner_node",
            "schema_version": payload["schema_version"],
            "firmware_version": payload["firmware_version"],
            "raw_packet_ref": make_ref("rawpkt"),
        },
        "raw_packet": payload,
    }
    return normalized


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Normalize a node packet into an MVP observation object.")
    parser.add_argument(
        "input",
        nargs="?",
        default=str(EXAMPLES_DIR / "node-observation.example.json"),
        help="Path to a node packet JSON file.",
    )
    parser.add_argument(
        "--parcel-id",
        default="parcel_demo_001",
        help="Optional parcel identifier to attach to the normalized observation.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    input_path = Path(args.input).resolve()

    try:
        payload = load_json(input_path)
        normalized = normalize_packet(payload, parcel_id=args.parcel_id)
    except (ValidationError, FileNotFoundError, json.JSONDecodeError, KeyError) as exc:
        print(f"ERROR {input_path}: {exc}", file=sys.stderr)
        return 1

    print(json.dumps(normalized, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    sys.exit(main())
