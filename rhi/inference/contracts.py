class InferenceError(Exception):
    pass


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


def validate_public_context(payload: dict):
    required = [
        "context_id",
        "source_kind",
        "source_name",
        "observed_at",
        "coverage_mode",
        "parcel_id",
        "hazards",
        "summary",
    ]
    for field in required:
        if field not in payload:
            raise InferenceError(f"public context missing required field: {field}")

    if payload["source_kind"] != "public_context":
        raise InferenceError("public context source_kind must be public_context")


def validate_parcel_context(payload: dict):
    required = ["parcel_id", "site_profile", "node_installations", "parcel_priors"]
    for field in required:
        if field not in payload:
            raise InferenceError(f"parcel context missing required field: {field}")


def validate_shared_neighborhood_signal(payload: dict):
    required = ["generated_at", "min_participants", "sharing_settings", "contributions"]
    for field in required:
        if field not in payload:
            raise InferenceError(f"shared neighborhood signal missing required field: {field}")
