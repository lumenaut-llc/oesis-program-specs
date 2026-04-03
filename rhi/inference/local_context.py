def get_location_mode(payload: dict) -> str:
    raw_packet = payload.get("raw_packet", {})
    return raw_packet.get("location_mode", "indoor")


def find_node_installation(parcel_context: dict | None, node_id: str) -> dict | None:
    if not parcel_context:
        return None
    for installation in parcel_context.get("node_installations", []):
        if installation.get("node_id") == node_id:
            return installation
    return None


def classify_local_context(payload: dict, parcel_context: dict | None = None) -> dict:
    installation = find_node_installation(parcel_context, payload["node_id"])
    location_mode = installation.get("location_mode", get_location_mode(payload)) if installation else get_location_mode(payload)
    is_indoor = location_mode == "indoor"
    is_sheltered = location_mode == "sheltered"
    is_outdoor = location_mode == "outdoor"
    local_observability = "low"
    if is_outdoor:
        local_observability = "moderate"
    elif is_sheltered:
        local_observability = "limited"

    return {
        "location_mode": location_mode,
        "is_indoor": is_indoor,
        "is_sheltered": is_sheltered,
        "is_outdoor": is_outdoor,
        "local_observability": local_observability,
        "install_role": installation.get("install_role", "unknown") if installation else "unknown",
        "exposure_bias_flags": installation.get("exposure_bias_flags", []) if installation else [],
        "has_parcel_context": parcel_context is not None,
    }


def prior_adjustment(prior_value: str | None, *, low: float = -0.02, moderate: float = 0.0, high: float = 0.04) -> float:
    mapping = {
        "low": low,
        "moderate": moderate,
        "high": high,
        "unknown": 0.0,
        None: 0.0,
    }
    return mapping.get(prior_value, 0.0)
