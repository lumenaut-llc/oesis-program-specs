#!/usr/bin/env python3

import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
EXAMPLES_DIR = ROOT / "docs" / "data-model" / "examples"


class ValidationError(Exception):
    pass


def load_json(path: Path):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise ValidationError(f"{path.name}: invalid JSON: {exc}") from exc


def require(condition: bool, message: str):
    if not condition:
        raise ValidationError(message)


def require_type(value, expected_type, field_name: str):
    require(isinstance(value, expected_type), f"{field_name}: expected {expected_type.__name__}")


def require_number(value, field_name: str, minimum=None, maximum=None, exclusive_minimum=None):
    require(isinstance(value, (int, float)) and not isinstance(value, bool), f"{field_name}: expected number")
    if minimum is not None:
      require(value >= minimum, f"{field_name}: expected >= {minimum}")
    if maximum is not None:
      require(value <= maximum, f"{field_name}: expected <= {maximum}")
    if exclusive_minimum is not None:
      require(value > exclusive_minimum, f"{field_name}: expected > {exclusive_minimum}")


def validate_node_observation(payload):
    required = [
        "schema_version",
        "node_id",
        "observed_at",
        "firmware_version",
        "location_mode",
        "sensors",
        "health",
    ]
    for field in required:
        require(field in payload, f"node observation missing required field: {field}")

    require(payload["schema_version"] == "rhi.bench-air.v1", "schema_version must be rhi.bench-air.v1")
    require_type(payload["node_id"], str, "node_id")
    require_type(payload["observed_at"], str, "observed_at")
    require(payload["location_mode"] in {"indoor", "sheltered", "outdoor"}, "location_mode invalid")

    sensors = payload["sensors"]
    require_type(sensors, dict, "sensors")
    for sensor_name in ("sht45", "bme688"):
        require(sensor_name in sensors, f"sensors missing {sensor_name}")

    sht45 = sensors["sht45"]
    require_type(sht45, dict, "sensors.sht45")
    require_type(sht45["present"], bool, "sensors.sht45.present")
    require_number(sht45["temperature_c"], "sensors.sht45.temperature_c")
    require_number(sht45["relative_humidity_pct"], "sensors.sht45.relative_humidity_pct", 0, 100)

    bme688 = sensors["bme688"]
    require_type(bme688, dict, "sensors.bme688")
    require_type(bme688["present"], bool, "sensors.bme688.present")
    require_number(bme688["temperature_c"], "sensors.bme688.temperature_c")
    require_number(bme688["relative_humidity_pct"], "sensors.bme688.relative_humidity_pct", 0, 100)
    require_number(bme688["pressure_hpa"], "sensors.bme688.pressure_hpa")
    require_number(bme688["gas_resistance_ohm"], "sensors.bme688.gas_resistance_ohm", exclusive_minimum=0)

    health = payload["health"]
    require_type(health, dict, "health")
    require_number(health["uptime_s"], "health.uptime_s", minimum=0)
    require_type(health["wifi_connected"], bool, "health.wifi_connected")
    require_number(health["free_heap_bytes"], "health.free_heap_bytes", minimum=0)
    require_number(health["read_failures_total"], "health.read_failures_total", minimum=0)
    require(isinstance(health["last_error"], (str, type(None))), "health.last_error: expected string or null")


def validate_parcel_state(payload):
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
        require(field in payload, f"parcel state missing required field: {field}")

    statuses = {"safe", "caution", "unsafe", "unknown"}
    for field in ("stay_status", "enter_status", "escape_status", "asset_status"):
        require(payload[field] in statuses, f"{field}: invalid status")

    require_type(payload["parcel_id"], str, "parcel_id")
    require_type(payload["computed_at"], str, "computed_at")
    require_number(payload["confidence"], "confidence", minimum=0, maximum=1)
    require(
        payload["evidence_mode"] in {"local_only", "local_plus_public", "public_only", "insufficient"},
        "evidence_mode invalid",
    )

    reasons = payload["reasons"]
    require_type(reasons, list, "reasons")
    require(len(reasons) > 0, "reasons must not be empty")
    for i, reason in enumerate(reasons):
        require_type(reason, str, f"reasons[{i}]")
        require(reason.strip() != "", f"reasons[{i}] must not be blank")

    hazards = payload["hazards"]
    require_type(hazards, dict, "hazards")
    for field in ("smoke_probability", "flood_probability", "heat_probability"):
        require_number(hazards[field], f"hazards.{field}", minimum=0, maximum=1)

    freshness = payload["freshness"]
    require_type(freshness, dict, "freshness")
    require_type(freshness["latest_observation_at"], str, "freshness.latest_observation_at")
    require_number(freshness["seconds_since_latest"], "freshness.seconds_since_latest", minimum=0)
    require_type(freshness["stale"], bool, "freshness.stale")

    provenance = payload["provenance_summary"]
    require_type(provenance, dict, "provenance_summary")
    require_number(provenance["observation_count"], "provenance_summary.observation_count", minimum=0)
    require_type(provenance["source_modes"], list, "provenance_summary.source_modes")
    require(len(provenance["source_modes"]) > 0, "provenance_summary.source_modes must not be empty")
    if "observation_refs" in provenance:
        require_type(provenance["observation_refs"], list, "provenance_summary.observation_refs")


def main():
    files = [
        ("node observation", EXAMPLES_DIR / "node-observation.example.json", validate_node_observation),
        ("parcel state", EXAMPLES_DIR / "parcel-state.example.json", validate_parcel_state),
    ]

    failures = []
    for label, path, validator in files:
        try:
            payload = load_json(path)
            validator(payload)
            print(f"PASS {label}: {path}")
        except (ValidationError, KeyError) as exc:
            failures.append(f"FAIL {label}: {path} -> {exc}")

    if failures:
        for failure in failures:
            print(failure, file=sys.stderr)
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
