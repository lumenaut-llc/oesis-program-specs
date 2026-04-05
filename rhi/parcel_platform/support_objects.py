from copy import deepcopy
from uuid import uuid4


class SupportObjectError(Exception):
    pass


def _require(condition: bool, message: str):
    if not condition:
        raise SupportObjectError(message)


def _require_type(value, expected_type, field_name: str):
    _require(isinstance(value, expected_type), f"{field_name}: expected {expected_type.__name__}")


def _require_number(value, field_name: str, *, minimum=None, maximum=None):
    _require(isinstance(value, (int, float)) and not isinstance(value, bool), f"{field_name}: expected number")
    if minimum is not None:
        _require(value >= minimum, f"{field_name}: expected >= {minimum}")
    if maximum is not None:
        _require(value <= maximum, f"{field_name}: expected <= {maximum}")


def validate_house_state(payload: dict):
    required = ["parcel_id", "updated_at", "observed_at", "indoor_air", "hvac_state", "device_state"]
    for field in required:
        _require(field in payload, f"house state missing required field: {field}")

    _require_type(payload["parcel_id"], str, "parcel_id")
    _require_type(payload["updated_at"], str, "updated_at")
    _require_type(payload["observed_at"], str, "observed_at")

    indoor_air = payload["indoor_air"]
    _require_type(indoor_air, dict, "indoor_air")
    _require_number(indoor_air["pm25_ugm3"], "indoor_air.pm25_ugm3", minimum=0)
    _require_number(indoor_air["temperature_c"], "indoor_air.temperature_c")
    _require_number(indoor_air["relative_humidity_pct"], "indoor_air.relative_humidity_pct", minimum=0, maximum=100)

    hvac_state = payload["hvac_state"]
    _require_type(hvac_state, dict, "hvac_state")
    _require(hvac_state["mode"] in {"off", "heat", "cool", "auto", "fan_only", "unknown"}, "hvac_state.mode invalid")
    _require(hvac_state["fan_mode"] in {"auto", "on", "circulate", "unknown"}, "hvac_state.fan_mode invalid")
    _require(hvac_state["air_mode"] in {"recirculate", "fresh", "auto", "unknown"}, "hvac_state.air_mode invalid")
    _require_type(hvac_state["filter_condition"], str, "hvac_state.filter_condition")

    device_state = payload["device_state"]
    _require_type(device_state, dict, "device_state")
    _require(device_state["purifier_state"] in {"on", "off", "auto", "unknown"}, "device_state.purifier_state invalid")
    _require(
        device_state["backup_power_state"] in {"unavailable", "standby", "active", "unknown"},
        "device_state.backup_power_state invalid",
    )
    _require(device_state["window_state"] in {"open", "closed", "mixed", "unknown"}, "device_state.window_state invalid")
    _require(device_state["shade_state"] in {"open", "closed", "partial", "unknown"}, "device_state.shade_state invalid")
    _require(device_state["sump_state"] in {"on", "off", "fault", "unknown"}, "device_state.sump_state invalid")


def validate_house_capability(payload: dict):
    required = ["parcel_id", "updated_at", "protective_capacity", "hvac_profile", "site_profile"]
    for field in required:
        _require(field in payload, f"house capability missing required field: {field}")

    _require_type(payload["parcel_id"], str, "parcel_id")
    _require_type(payload["updated_at"], str, "updated_at")

    protective_capacity = payload["protective_capacity"]
    _require_type(protective_capacity, dict, "protective_capacity")
    for field in ("backup_power_available", "portable_purifier_present", "clean_air_room_ready"):
        _require_type(protective_capacity[field], bool, f"protective_capacity.{field}")

    hvac_profile = payload["hvac_profile"]
    _require_type(hvac_profile, dict, "hvac_profile")
    _require_type(hvac_profile["system_type"], str, "hvac_profile.system_type")
    _require_type(hvac_profile["recirculation_available"], bool, "hvac_profile.recirculation_available")
    _require_type(hvac_profile["filter_size"], str, "hvac_profile.filter_size")
    _require_type(hvac_profile["higher_merv_support"], str, "hvac_profile.higher_merv_support")

    site_profile = payload["site_profile"]
    _require_type(site_profile, dict, "site_profile")
    _require_type(site_profile["orientation_class"], str, "site_profile.orientation_class")
    _require_type(site_profile["shading_posture"], str, "site_profile.shading_posture")
    _require_type(site_profile["drainage_posture"], str, "site_profile.drainage_posture")


def validate_control_compatibility(payload: dict):
    required = ["parcel_id", "updated_at", "local_controller", "control_surfaces"]
    for field in required:
        _require(field in payload, f"control compatibility missing required field: {field}")

    _require_type(payload["parcel_id"], str, "parcel_id")
    _require_type(payload["updated_at"], str, "updated_at")

    local_controller = payload["local_controller"]
    _require_type(local_controller, dict, "local_controller")
    _require_type(local_controller["available"], bool, "local_controller.available")
    _require_type(local_controller["controller_type"], str, "local_controller.controller_type")

    control_surfaces = payload["control_surfaces"]
    _require_type(control_surfaces, list, "control_surfaces")
    valid_interface_classes = {"manual", "local_api", "matter", "home_assistant", "cloud_only", "bacnet", "smart_plug", "none"}
    valid_locality = {"local_only", "cloud_required", "hybrid", "unknown"}
    valid_tiers = {"advisory_only", "soft_integration", "hard_integration"}
    for i, surface in enumerate(control_surfaces):
        _require_type(surface, dict, f"control_surfaces[{i}]")
        for field in ("control_id", "system_type", "interface_class", "locality", "integration_tier", "enabled", "override_rule"):
            _require(field in surface, f"control_surfaces[{i}] missing required field: {field}")
        _require_type(surface["control_id"], str, f"control_surfaces[{i}].control_id")
        _require_type(surface["system_type"], str, f"control_surfaces[{i}].system_type")
        _require(surface["interface_class"] in valid_interface_classes, f"control_surfaces[{i}].interface_class invalid")
        _require(surface["locality"] in valid_locality, f"control_surfaces[{i}].locality invalid")
        _require(surface["integration_tier"] in valid_tiers, f"control_surfaces[{i}].integration_tier invalid")
        _require_type(surface["enabled"], bool, f"control_surfaces[{i}].enabled")
        _require_type(surface["override_rule"], str, f"control_surfaces[{i}].override_rule")


def prepare_intervention_event(payload: dict, *, parcel_id: str, now_iso: str) -> dict:
    prepared = deepcopy(payload)
    prepared["parcel_id"] = parcel_id
    prepared.setdefault("intervention_id", f"intv_{uuid4().hex[:12]}")
    prepared.setdefault("recorded_at", now_iso)
    return prepared


def validate_intervention_event(payload: dict):
    required = [
        "intervention_id",
        "parcel_id",
        "recorded_at",
        "hazard_target",
        "action_kind",
        "initiated_by",
        "status",
        "baseline_window_minutes",
        "evaluation_window_minutes",
    ]
    for field in required:
        _require(field in payload, f"intervention event missing required field: {field}")

    _require_type(payload["intervention_id"], str, "intervention_id")
    _require_type(payload["parcel_id"], str, "parcel_id")
    _require_type(payload["recorded_at"], str, "recorded_at")
    _require_type(payload["hazard_target"], str, "hazard_target")
    _require_type(payload["action_kind"], str, "action_kind")
    _require_type(payload["initiated_by"], str, "initiated_by")
    _require(payload["status"] in {"planned", "attempted", "completed", "failed"}, "status invalid")
    _require_number(payload["baseline_window_minutes"], "baseline_window_minutes", minimum=0)
    _require_number(payload["evaluation_window_minutes"], "evaluation_window_minutes", minimum=0)
    if "notes" in payload:
        _require_type(payload["notes"], str, "notes")


def prepare_verification_outcome(payload: dict, *, parcel_id: str, now_iso: str) -> dict:
    prepared = deepcopy(payload)
    prepared["parcel_id"] = parcel_id
    prepared.setdefault("verification_id", f"verify_{uuid4().hex[:12]}")
    prepared.setdefault("evaluated_at", now_iso)
    return prepared


def validate_verification_outcome(payload: dict):
    required = [
        "verification_id",
        "parcel_id",
        "intervention_id",
        "evaluated_at",
        "metric_name",
        "baseline_value",
        "outcome_value",
        "assessment",
        "confidence_band",
    ]
    for field in required:
        _require(field in payload, f"verification outcome missing required field: {field}")

    _require_type(payload["verification_id"], str, "verification_id")
    _require_type(payload["parcel_id"], str, "parcel_id")
    _require_type(payload["intervention_id"], str, "intervention_id")
    _require_type(payload["evaluated_at"], str, "evaluated_at")
    _require_type(payload["metric_name"], str, "metric_name")
    _require_number(payload["baseline_value"], "baseline_value")
    _require_number(payload["outcome_value"], "outcome_value")
    _require(payload["assessment"] in {"improved", "no_change", "worsened", "inconclusive"}, "assessment invalid")
    _require(payload["confidence_band"] in {"low", "medium", "high"}, "confidence_band invalid")
    if "response_window_minutes" in payload:
        _require_number(payload["response_window_minutes"], "response_window_minutes", minimum=0)
    if "summary" in payload:
        _require_type(payload["summary"], str, "summary")


__all__ = [
    "SupportObjectError",
    "prepare_intervention_event",
    "prepare_verification_outcome",
    "validate_control_compatibility",
    "validate_house_capability",
    "validate_house_state",
    "validate_intervention_event",
    "validate_verification_outcome",
]
