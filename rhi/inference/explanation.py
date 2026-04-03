from datetime import datetime

from .local_context import classify_local_context, find_node_installation


def derive_reasons(
    payload: dict,
    confidence: float,
    evidence_contributions: list[dict],
    *,
    parcel_context: dict | None = None,
    public_context: dict | None = None,
) -> list[str]:
    reasons = []
    context = classify_local_context(payload, parcel_context=parcel_context)
    parcel_priors = parcel_context.get("parcel_priors", {}) if parcel_context else {}

    for contribution in evidence_contributions[:6]:
        reasons.append(contribution["summary"])

    if parcel_priors.get("heat_retention_class") == "high":
        reasons.append("Parcel prior suggests elevated heat retention, which modestly raises heat support.")
    elif parcel_priors.get("heat_retention_class") == "low":
        reasons.append("Parcel prior suggests lower heat retention, which modestly reduces heat support.")

    if context["is_indoor"]:
        reasons.append("Current local evidence comes from an indoor node and does not directly represent parcel-wide outdoor conditions.")
    elif context["is_sheltered"]:
        reasons.append("Current local evidence comes from a sheltered node and only partially represents wider parcel conditions.")
    else:
        reasons.append("Current local evidence comes from one outdoor-capable node and still reflects only part of the parcel.")

    if confidence >= 0.5 and public_context:
        reasons.append("Confidence improves because public context supports the local evidence, but parcel certainty is still limited.")
    elif confidence >= 0.5:
        reasons.append("The current decision is based on a single homeowner-owned node without confirming public context.")

    deduped = []
    seen = set()
    for reason in reasons:
        if reason not in seen:
            deduped.append(reason)
            seen.add(reason)

    if not deduped:
        deduped.append("Available evidence is limited, so the parcel state remains mostly unknown.")

    return deduped


def make_evidence_contribution(
    *,
    contribution_id: str,
    source_class: str,
    source_name: str,
    role: str,
    summary: str,
    hazards: list[str],
    weight: float,
    visibility: str = "homeowner_safe",
    freshness_band: str | None = None,
) -> dict:
    contribution = {
        "contribution_id": contribution_id,
        "source_class": source_class,
        "source_name": source_name,
        "role": role,
        "summary": summary,
        "hazards": hazards,
        "weight": round(weight, 2),
        "visibility": visibility,
    }
    if freshness_band is not None:
        contribution["freshness_band"] = freshness_band
    return contribution


def build_evidence_contributions(
    *,
    payload: dict,
    parcel_context: dict | None,
    shared_context: dict | None,
    public_context: dict | None,
    hazards: dict,
    confidence: float,
    stale: bool,
    now: datetime,
    public_context_freshness_band_fn,
    trust_gates: dict,
) -> list[dict]:
    contributions = []
    context = classify_local_context(payload, parcel_context=parcel_context)

    gas_resistance = payload["values"].get("gas_resistance_ohm")
    if gas_resistance is not None:
        if gas_resistance < 100000:
            summary = "Local gas-resistance trend suggests an indoor or sheltered air anomaly worth checking."
            weight = 0.48
        elif gas_resistance < 180000:
            summary = "Local gas-resistance trend shows a moderate change, but it is not a direct smoke concentration measurement."
            weight = 0.32
        else:
            summary = "Local gas-resistance trend appears comparatively steady."
            weight = 0.12
        contributions.append(
            make_evidence_contribution(
                contribution_id="local_gas_trend",
                source_class="local",
                source_name=payload["node_id"],
                role="driver",
                summary=summary,
                hazards=["smoke"],
                weight=weight,
            )
        )

    temperature_c = payload["values"].get("temperature_c_primary")
    if temperature_c is not None:
        if temperature_c >= 34:
            summary = (
                "Indoor temperature is elevated at the node location, which may indicate local heat burden."
                if context["is_indoor"]
                else "Measured temperature is elevated at the node location and may contribute to heat concern."
            )
            weight = 0.52
        elif temperature_c >= 24:
            summary = (
                "Indoor temperature is somewhat elevated at the node location."
                if context["is_indoor"]
                else "Measured temperature is modestly elevated at the node location."
            )
            weight = 0.28
        else:
            summary = "Local temperature does not currently suggest elevated heat concern."
            weight = 0.1
        contributions.append(
            make_evidence_contribution(
                contribution_id="local_temperature",
                source_class="local",
                source_name=payload["node_id"],
                role="driver",
                summary=summary,
                hazards=["heat"],
                weight=weight,
            )
        )

    siting_summary = "Current local evidence comes from one outdoor-capable node and still reflects only part of the parcel."
    siting_weight = 0.28
    if context["is_indoor"]:
        siting_summary = "Current local evidence comes from an indoor node and does not directly represent parcel-wide outdoor conditions."
        siting_weight = 0.72
    elif context["is_sheltered"]:
        siting_summary = "Current local evidence comes from a sheltered node and only partially represents wider parcel conditions."
        siting_weight = 0.56
    contributions.append(
        make_evidence_contribution(
            contribution_id="local_siting_limit",
            source_class="local",
            source_name=payload["node_id"],
            role="limitation",
            summary=siting_summary,
            hazards=["smoke", "heat", "flood"],
            weight=siting_weight,
        )
    )

    if parcel_context:
        installation = find_node_installation(parcel_context, payload["node_id"])
        if installation:
            contributions.append(
                make_evidence_contribution(
                    contribution_id="parcel_install_role",
                    source_class="parcel_context",
                    source_name=installation.get("install_role", "unknown"),
                    role="limitation",
                    summary=(
                        f"Install role {installation.get('install_role', 'unknown')} constrains how strongly this node "
                        "represents wider parcel conditions."
                    ),
                    hazards=["smoke", "heat", "flood"],
                    weight=0.44,
                )
            )
        else:
            contributions.append(
                make_evidence_contribution(
                    contribution_id="parcel_missing_installation",
                    source_class="parcel_context",
                    source_name=parcel_context["parcel_id"],
                    role="limitation",
                    summary="Parcel context is present, but this node lacks a matching installation record.",
                    hazards=["smoke", "heat", "flood"],
                    weight=0.46,
                )
            )
    else:
        contributions.append(
            make_evidence_contribution(
                contribution_id="missing_parcel_context",
                source_class="system",
                source_name=payload["parcel_id"],
                role="limitation",
                summary="Parcel installation context is missing, so siting relevance and parcel priors cannot improve interpretation.",
                hazards=["smoke", "heat", "flood"],
                weight=0.64,
            )
        )

    if public_context:
        for member in public_context.get("members", [public_context]):
            member_hazards = []
            if member["hazards"]["smoke_probability"] >= 0.1:
                member_hazards.append("smoke")
            if member["hazards"]["heat_probability"] >= 0.1:
                member_hazards.append("heat")
            if member["hazards"]["flood_probability"] >= 0.03:
                member_hazards.append("flood")
            if member_hazards:
                freshness_band = public_context_freshness_band_fn(member, now=now)
                contributions.append(
                    make_evidence_contribution(
                        contribution_id=f"public_{member['source_name']}",
                        source_class="public",
                        source_name=member["source_name"],
                        role="driver",
                        summary=member.get("summary", ["Public context contributed to the estimate."])[0],
                        hazards=member_hazards,
                        weight={
                            "fresh": 0.48,
                            "aging": 0.32,
                            "stale": 0.18,
                            "expired": 0.0,
                        }[freshness_band],
                        freshness_band=freshness_band,
                    )
                )
                if freshness_band in {"aging", "stale", "expired"}:
                    contributions.append(
                        make_evidence_contribution(
                            contribution_id=f"public_{member['source_name']}_freshness_limit",
                            source_class="public",
                            source_name=member["source_name"],
                            role="limitation",
                            summary={
                                "aging": "Some regional public context is aging, so it provides limited support.",
                                "stale": "Some regional public context is stale and contributes little weight to the current parcel estimate.",
                                "expired": "Some available public context was too old to materially affect the current parcel estimate.",
                            }[freshness_band],
                            hazards=member_hazards,
                            weight={
                                "aging": 0.28,
                                "stale": 0.46,
                                "expired": 0.7,
                            }[freshness_band],
                            freshness_band=freshness_band,
                        )
                    )

    if shared_context:
        shared_hazards = []
        if shared_context["hazards"]["smoke_probability"] >= 0.2:
            shared_hazards.append("smoke")
        if shared_context["hazards"]["heat_probability"] >= 0.2:
            shared_hazards.append("heat")
        if shared_context["hazards"]["flood_probability"] >= 0.05:
            shared_hazards.append("flood")
        contributions.append(
            make_evidence_contribution(
                contribution_id="shared_cell_signal",
                source_class="shared",
                source_name=shared_context["cell_id"],
                role="driver",
                summary=shared_context["summary"][0],
                hazards=shared_hazards or ["smoke"],
                weight=0.34,
            )
        )
        contributions.append(
            make_evidence_contribution(
                contribution_id="shared_scope_limit",
                source_class="shared",
                source_name=shared_context["cell_id"],
                role="limitation",
                summary="Shared neighborhood signals are nearby supporting context, not direct confirmation of this parcel's conditions.",
                hazards=["smoke", "heat", "flood"],
                weight=0.42,
            )
        )

    if hazards["flood_probability"] == 0:
        contributions.append(
            make_evidence_contribution(
                contribution_id="missing_flood_evidence",
                source_class="parcel_context" if parcel_context else "local",
                source_name=payload["node_id"] if not parcel_context else parcel_context["parcel_id"],
                role="limitation",
                summary="No flood-capable local sensor or public flood context is present.",
                hazards=["flood"],
                weight=0.58,
            )
        )

    if stale:
        contributions.append(
            make_evidence_contribution(
                contribution_id="stale_local_observation",
                source_class="system",
                source_name="freshness_gate",
                role="limitation",
                summary="The latest local observation is aging out and may no longer reflect current parcel conditions.",
                hazards=["smoke", "heat", "flood"],
                weight=trust_gates["freshness_gate"]["stale_weight"],
            )
        )

    if confidence < trust_gates["confidence_gate"]["low_confidence_threshold"]:
        contributions.append(
            make_evidence_contribution(
                contribution_id="low_confidence_gate",
                source_class="system",
                source_name="confidence_gate",
                role="limitation",
                summary="Confidence is limited because the current estimate relies on sparse or weakly representative evidence.",
                hazards=["smoke", "heat", "flood"],
                weight=trust_gates["confidence_gate"]["weight"],
            )
        )

    public_members = public_context.get("members", [public_context]) if public_context else []
    strongest_public_smoke = max((member["hazards"]["smoke_probability"] for member in public_members), default=0.0)
    strongest_public_heat = max((member["hazards"]["heat_probability"] for member in public_members), default=0.0)
    strongest_shared_smoke = shared_context["hazards"]["smoke_probability"] if shared_context else 0.0
    strongest_shared_heat = shared_context["hazards"]["heat_probability"] if shared_context else 0.0

    disagreement = trust_gates["cross_source_disagreement"]

    if (
        gas_resistance is not None
        and gas_resistance >= disagreement["smoke_local_steady_min_gas_resistance_ohm"]
        and max(strongest_public_smoke, strongest_shared_smoke) >= disagreement["smoke_external_support_threshold"]
    ):
        contributions.append(
            make_evidence_contribution(
                contribution_id="smoke_disagreement_gate",
                source_class="system",
                source_name="cross_source_agreement",
                role="limitation",
                summary="Regional or neighborhood smoke context is stronger than the local node trend, so the estimate remains conservative.",
                hazards=["smoke"],
                weight=disagreement["weight"],
            )
        )

    if (
        temperature_c is not None
        and temperature_c < disagreement["heat_local_cool_max_temp_c"]
        and max(strongest_public_heat, strongest_shared_heat) >= disagreement["heat_external_support_threshold"]
    ):
        contributions.append(
            make_evidence_contribution(
                contribution_id="heat_disagreement_gate",
                source_class="system",
                source_name="cross_source_agreement",
                role="limitation",
                summary="Regional or neighborhood heat context is stronger than the local node reading, so parcel heat interpretation remains cautious.",
                hazards=["heat"],
                weight=disagreement["weight"],
            )
        )

    return contributions


def confidence_band(confidence: float) -> str:
    if confidence >= 0.75:
        return "high"
    if confidence >= 0.45:
        return "medium"
    return "low"


def build_explanation_payload(
    *,
    confidence: float,
    evidence_mode: str,
    inference_basis: str,
    evidence_contributions: list[dict],
    parcel_context: dict | None,
    shared_context: dict | None,
    public_context: dict | None,
) -> dict:
    sorted_drivers = sorted(
        (item for item in evidence_contributions if item["role"] == "driver"),
        key=lambda item: item["weight"],
        reverse=True,
    )
    sorted_limitations = sorted(
        (item for item in evidence_contributions if item["role"] == "limitation"),
        key=lambda item: item["weight"],
        reverse=True,
    )
    drivers = [item["summary"] for item in sorted_drivers[:3]]
    limitations = [item["summary"] for item in sorted_limitations[:3]]
    if not limitations:
        limitations = ["Evidence limits are currently low enough that few explicit caveats were generated."]

    headline = (
        f"Estimate uses {inference_basis.replace('_', ' ')} evidence with "
        f"{confidence_band(confidence)} confidence."
    )

    return {
        "headline": headline,
        "basis": {
            "evidence_mode": evidence_mode,
            "inference_basis": inference_basis,
            "confidence_band": confidence_band(confidence),
        },
        "drivers": drivers,
        "limitations": limitations,
        "evidence_contributions": evidence_contributions,
        "source_breakdown": {
            "local": True,
            "shared": shared_context is not None,
            "public": public_context is not None,
            "parcel_context": parcel_context is not None,
            "system": any(item["source_class"] == "system" for item in evidence_contributions),
        },
    }
