def derive_hazards(
    payload: dict,
    *,
    now,
    classify_local_context_fn,
    probability_from_lt_bands_fn,
    probability_from_gte_bands_fn,
    prior_adjustment_fn,
    public_context_freshness_band_fn,
    get_policy_for_source_fn,
    clamp_probability_fn,
    hazard_thresholds: dict,
    parcel_context: dict | None = None,
    shared_neighborhood_context: dict | None = None,
    public_context: dict | None = None,
) -> dict:
    values = payload["values"]
    health = payload["health"]
    context = classify_local_context_fn(payload, parcel_context=parcel_context)
    smoke_config = hazard_thresholds["smoke"]
    heat_config = hazard_thresholds["heat"]
    sensor_penalties = hazard_thresholds["sensor_penalties"]
    parcel_priors = parcel_context.get("parcel_priors", {}) if parcel_context else {}

    smoke_probability = smoke_config["base_probability"]
    gas_resistance = values.get("gas_resistance_ohm")
    smoke_probability = probability_from_lt_bands_fn(
        gas_resistance,
        smoke_config["gas_resistance_bands"],
        smoke_config["default_probability"],
    )

    heat_probability = heat_config["base_probability"]
    temperature_c = values.get("temperature_c_primary")
    heat_probability = probability_from_gte_bands_fn(
        temperature_c,
        heat_config["temperature_bands"],
        heat_config["base_probability"],
    )

    if context["is_indoor"]:
        heat_probability -= heat_config["indoor_penalty"]
    elif context["is_sheltered"]:
        heat_probability -= heat_config["sheltered_penalty"]

    heat_probability += prior_adjustment_fn(parcel_priors.get("heat_retention_class"))
    smoke_probability += prior_adjustment_fn(
        parcel_priors.get("smoke_exposure_class"),
        low=-0.01,
        moderate=0.0,
        high=0.03,
    )

    flood_probability = 0.0

    if not health.get("wifi_connected", False):
        smoke_probability -= sensor_penalties["wifi_disconnected"]
        heat_probability -= sensor_penalties["wifi_disconnected"]

    if health.get("read_failures_total", 0) > 0:
        smoke_probability -= sensor_penalties["read_failures"]
        heat_probability -= sensor_penalties["read_failures"]

    if public_context:
        member_contexts = public_context.get("members", [public_context])
        for member in member_contexts:
            freshness_band = public_context_freshness_band_fn(member, now=now)
            policy = get_policy_for_source_fn(member["source_name"])
            public_hazards = member["hazards"]
            multiplier = policy["hazard_multiplier"][freshness_band]
            smoke_probability = max(
                smoke_probability,
                round(public_hazards["smoke_probability"] * multiplier, 2),
            )
            heat_probability = max(
                heat_probability,
                round(public_hazards["heat_probability"] * multiplier, 2),
            )
            flood_probability = max(
                flood_probability,
                round(public_hazards["flood_probability"] * multiplier, 2),
            )

    if shared_neighborhood_context:
        shared_hazards = shared_neighborhood_context["hazards"]
        smoke_probability = max(smoke_probability, round(shared_hazards["smoke_probability"] * 0.55, 2))
        heat_probability = max(heat_probability, round(shared_hazards["heat_probability"] * 0.45, 2))
        flood_probability = max(flood_probability, round(shared_hazards["flood_probability"] * 0.4, 2))

    return {
        "smoke_probability": clamp_probability_fn(smoke_probability),
        "flood_probability": clamp_probability_fn(flood_probability),
        "heat_probability": clamp_probability_fn(heat_probability),
    }


def derive_confidence(
    payload: dict,
    hazards: dict,
    *,
    now,
    parse_time_fn,
    classify_local_context_fn,
    public_context_freshness_band_fn,
    get_policy_for_source_fn,
    clamp_probability_fn,
    parcel_context: dict | None = None,
    shared_neighborhood_context: dict | None = None,
    public_context: dict | None = None,
) -> float:
    observed_at = parse_time_fn(payload["observed_at"])
    age_seconds = max(0, int((now - observed_at).total_seconds()))
    context = classify_local_context_fn(payload, parcel_context=parcel_context)

    confidence = 0.52
    if payload["health"].get("read_failures_total", 0) > 0:
        confidence -= 0.1
    if not payload["health"].get("wifi_connected", False):
        confidence -= 0.04
    if context["is_indoor"]:
        confidence -= 0.14
    elif context["is_sheltered"]:
        confidence -= 0.08
    if not context["has_parcel_context"]:
        confidence -= 0.08
    if "hvac_possible" in context["exposure_bias_flags"]:
        confidence -= 0.04
    if age_seconds > 900:
        confidence -= 0.1
    if age_seconds > 3600:
        confidence -= 0.15

    if max(hazards.values()) < 0.2:
        confidence -= 0.08
    if public_context:
        member_contexts = public_context.get("members", [public_context])
        confidence_adjustment = min(
            0.18,
            sum(
                get_policy_for_source_fn(member["source_name"])["confidence_adjustment"][
                    public_context_freshness_band_fn(member, now=now)
                ]
                for member in member_contexts
            ),
        )
        confidence += confidence_adjustment
    if shared_neighborhood_context:
        confidence += 0.06

    return clamp_probability_fn(confidence)
