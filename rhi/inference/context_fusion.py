def combine_public_contexts(
    public_contexts: list[dict],
    *,
    validate_public_context_fn,
    parse_time_fn,
    error_type,
) -> dict | None:
    if not public_contexts:
        return None

    for context in public_contexts:
        validate_public_context_fn(context)

    first = public_contexts[0]
    combined_summary = []
    combined_source_names = []
    combined_hazards = {
        "smoke_probability": 0.0,
        "heat_probability": 0.0,
        "flood_probability": 0.0,
    }
    combined_observed_at = first["observed_at"]
    members = []

    for context in public_contexts:
        if context["parcel_id"] != first["parcel_id"]:
            raise error_type("public contexts must share the same parcel_id")
        if context["coverage_mode"] != first["coverage_mode"]:
            raise error_type("public contexts must share the same coverage_mode")
        combined_source_names.append(context["source_name"])
        combined_summary.extend(context.get("summary", []))
        for hazard_name in combined_hazards:
            combined_hazards[hazard_name] = max(
                combined_hazards[hazard_name],
                context["hazards"][hazard_name],
            )
        if parse_time_fn(context["observed_at"]) > parse_time_fn(combined_observed_at):
            combined_observed_at = context["observed_at"]
        members.append(
            {
                "source_name": context["source_name"],
                "observed_at": context["observed_at"],
                "hazards": context["hazards"],
                "summary": context.get("summary", []),
            }
        )

    return {
        "context_id": "combined_public_context",
        "source_kind": "public_context",
        "source_name": ",".join(combined_source_names),
        "observed_at": combined_observed_at,
        "coverage_mode": first["coverage_mode"],
        "parcel_id": first["parcel_id"],
        "hazards": combined_hazards,
        "summary": combined_summary,
        "members": members,
    }


def build_shared_neighborhood_context(
    shared_signal: dict,
    *,
    validate_shared_neighborhood_signal_fn,
) -> dict | None:
    validate_shared_neighborhood_signal_fn(shared_signal)

    allowed_parcels = {
        item["parcel_ref"]
        for item in shared_signal.get("sharing_settings", [])
        if item.get("neighborhood_aggregate") and not item.get("revocation_pending")
    }

    eligible = []
    for contribution in shared_signal.get("contributions", []):
        if contribution.get("source_class") != "shared_data":
            continue
        parcel_ref = contribution.get("parcel_ref")
        if parcel_ref not in allowed_parcels:
            continue
        eligible.append(contribution)

    if len(eligible) < shared_signal["min_participants"]:
        return None

    cell_counts = {}
    for contribution in eligible:
        cell_id = contribution["cell_id"]
        cell_counts[cell_id] = cell_counts.get(cell_id, 0) + 1

    best_cell_id = None
    best_count = 0
    for cell_id, count in cell_counts.items():
        if count > best_count:
            best_cell_id = cell_id
            best_count = count

    if best_cell_id is None or best_count < shared_signal["min_participants"]:
        return None

    cell_contributions = [item for item in eligible if item["cell_id"] == best_cell_id]
    hazard_keys = ("smoke_probability", "flood_probability", "heat_probability")
    hazards = {}
    for hazard_key in hazard_keys:
        hazards[hazard_key] = round(
            sum(item["hazards"][hazard_key] for item in cell_contributions) / len(cell_contributions),
            2,
        )

    max_delay = max(item.get("delayed_minutes", 0) for item in cell_contributions)
    summary = [
        f"Shared neighborhood signal from {len(cell_contributions)} contributing parcels in {best_cell_id} suggests nearby conditions worth watching."
    ]
    if hazards["smoke_probability"] >= 0.3:
        summary.append("Nearby shared signals suggest modest smoke concern in the surrounding cell.")
    elif hazards["heat_probability"] >= 0.3:
        summary.append("Nearby shared signals suggest modest heat concern in the surrounding cell.")

    return {
        "context_id": "shared_neighborhood_context",
        "source_kind": "shared_data",
        "source_name": "shared_neighborhood_signal",
        "observed_at": shared_signal["generated_at"],
        "coverage_mode": "cell",
        "parcel_id": None,
        "hazards": hazards,
        "summary": summary,
        "member_count": len(cell_contributions),
        "max_delay_minutes": max_delay,
        "cell_id": best_cell_id,
    }
