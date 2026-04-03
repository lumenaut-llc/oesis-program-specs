#!/usr/bin/env python3

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

from rhi.common.repo_paths import DOCS_EXAMPLES_DIR, INFERENCE_CONFIG_DIR

from .context_fusion import build_shared_neighborhood_context as _build_shared_neighborhood_context_impl
from .context_fusion import combine_public_contexts as _combine_public_contexts_impl
from .explanation import build_evidence_contributions
from .explanation import build_explanation_payload
from .explanation import confidence_band
from .explanation import derive_reasons
from .explanation import make_evidence_contribution
from .hazard_logic import derive_confidence as _derive_confidence_impl
from .hazard_logic import derive_hazards as _derive_hazards_impl
from .local_context import classify_local_context
from .local_context import find_node_installation
from .local_context import get_location_mode
from .local_context import prior_adjustment

EXAMPLES_DIR = DOCS_EXAMPLES_DIR
CONFIG_DIR = INFERENCE_CONFIG_DIR
PUBLIC_CONTEXT_POLICY_PATH = CONFIG_DIR / "public_context_policy.json"
HAZARD_THRESHOLDS_PATH = CONFIG_DIR / "hazard_thresholds_v0.json"
TRUST_GATES_PATH = CONFIG_DIR / "trust_gates_v0.json"

__all__ = [
    "EXAMPLES_DIR",
    "CONFIG_DIR",
    "PUBLIC_CONTEXT_POLICY_PATH",
    "HAZARD_THRESHOLDS_PATH",
    "TRUST_GATES_PATH",
    "InferenceError",
    "load_json",
    "now_iso",
    "clamp_probability",
    "status_from_probability",
    "parse_time",
    "validate_normalized_observation",
    "validate_public_context",
    "validate_parcel_context",
    "validate_shared_neighborhood_signal",
    "load_public_context_policy",
    "PUBLIC_CONTEXT_POLICY",
    "load_hazard_thresholds",
    "HAZARD_THRESHOLDS",
    "load_trust_gates",
    "TRUST_GATES",
    "get_policy_for_source",
    "probability_from_lt_bands",
    "probability_from_gte_bands",
    "public_context_age_seconds",
    "public_context_freshness_band",
    "combine_public_contexts",
    "build_shared_neighborhood_context",
    "get_location_mode",
    "find_node_installation",
    "classify_local_context",
    "prior_adjustment",
    "derive_hazards",
    "derive_confidence",
    "derive_reasons",
    "make_evidence_contribution",
    "build_evidence_contributions",
    "confidence_band",
    "build_explanation_payload",
    "infer_parcel_state",
    "parse_args",
    "main",
]


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


def load_public_context_policy() -> dict:
    return load_json(PUBLIC_CONTEXT_POLICY_PATH)


PUBLIC_CONTEXT_POLICY = load_public_context_policy()


def load_hazard_thresholds() -> dict:
    return load_json(HAZARD_THRESHOLDS_PATH)


HAZARD_THRESHOLDS = load_hazard_thresholds()


def load_trust_gates() -> dict:
    return load_json(TRUST_GATES_PATH)


TRUST_GATES = load_trust_gates()


def get_policy_for_source(source_name: str) -> dict:
    default_policy = PUBLIC_CONTEXT_POLICY["default_policy"]
    override = PUBLIC_CONTEXT_POLICY.get("source_overrides", {}).get(source_name, {})
    return {
        "fresh_max_age_seconds": override.get("fresh_max_age_seconds", default_policy["fresh_max_age_seconds"]),
        "aging_max_age_seconds": override.get("aging_max_age_seconds", default_policy["aging_max_age_seconds"]),
        "stale_max_age_seconds": override.get("stale_max_age_seconds", default_policy["stale_max_age_seconds"]),
        "hazard_multiplier": default_policy["hazard_multiplier"],
        "confidence_adjustment": default_policy["confidence_adjustment"],
    }


def probability_from_lt_bands(value: float | None, bands: list[dict], default_probability: float) -> float:
    if value is None:
        return default_probability
    for band in bands:
        if value < band["lt"]:
            return band["probability"]
    return default_probability


def probability_from_gte_bands(value: float | None, bands: list[dict], default_probability: float) -> float:
    if value is None:
        return default_probability
    for band in bands:
        if value >= band["gte"]:
            return band["probability"]
    return default_probability


def public_context_age_seconds(public_context: dict, *, now: datetime) -> int:
    return max(0, int((now - parse_time(public_context["observed_at"])).total_seconds()))


def public_context_freshness_band(public_context: dict, *, now: datetime) -> str:
    policy = get_policy_for_source(public_context["source_name"])
    age_seconds = public_context_age_seconds(public_context, now=now)
    if age_seconds <= policy["fresh_max_age_seconds"]:
        return "fresh"
    if age_seconds <= policy["aging_max_age_seconds"]:
        return "aging"
    if age_seconds <= policy["stale_max_age_seconds"]:
        return "stale"
    return "expired"


def combine_public_contexts(public_contexts: list[dict]) -> dict | None:
    return _combine_public_contexts_impl(
        public_contexts,
        validate_public_context_fn=validate_public_context,
        parse_time_fn=parse_time,
        error_type=InferenceError,
    )


def build_shared_neighborhood_context(shared_signal: dict) -> dict | None:
    return _build_shared_neighborhood_context_impl(
        shared_signal,
        validate_shared_neighborhood_signal_fn=validate_shared_neighborhood_signal,
    )


def derive_hazards(
    payload: dict,
    parcel_context: dict | None = None,
    shared_neighborhood_context: dict | None = None,
    public_context: dict | None = None,
    *,
    now: datetime,
) -> dict:
    return _derive_hazards_impl(
        payload,
        now=now,
        classify_local_context_fn=classify_local_context,
        probability_from_lt_bands_fn=probability_from_lt_bands,
        probability_from_gte_bands_fn=probability_from_gte_bands,
        prior_adjustment_fn=prior_adjustment,
        public_context_freshness_band_fn=public_context_freshness_band,
        get_policy_for_source_fn=get_policy_for_source,
        clamp_probability_fn=clamp_probability,
        hazard_thresholds=HAZARD_THRESHOLDS,
        parcel_context=parcel_context,
        shared_neighborhood_context=shared_neighborhood_context,
        public_context=public_context,
    )


def derive_confidence(
    payload: dict,
    hazards: dict,
    *,
    now: datetime,
    parcel_context: dict | None = None,
    shared_neighborhood_context: dict | None = None,
    public_context: dict | None = None,
) -> float:
    return _derive_confidence_impl(
        payload,
        hazards,
        now=now,
        parse_time_fn=parse_time,
        classify_local_context_fn=classify_local_context,
        public_context_freshness_band_fn=public_context_freshness_band,
        get_policy_for_source_fn=get_policy_for_source,
        clamp_probability_fn=clamp_probability,
        parcel_context=parcel_context,
        shared_neighborhood_context=shared_neighborhood_context,
        public_context=public_context,
    )


def infer_parcel_state(
    payload: dict,
    *,
    computed_at: str | None = None,
    parcel_context: dict | None = None,
    shared_neighborhood_context: dict | None = None,
    public_context: dict | None = None,
) -> dict:
    validate_normalized_observation(payload)
    if parcel_context is not None:
        validate_parcel_context(parcel_context)
    if shared_neighborhood_context is not None:
        validate_shared_neighborhood_signal(shared_neighborhood_context)
    if public_context is not None:
        validate_public_context(public_context)

    now = parse_time(computed_at) if computed_at else datetime.now(timezone.utc)
    computed_at = (computed_at or now_iso())
    observed_at = parse_time(payload["observed_at"])
    age_seconds = max(0, int((now - observed_at).total_seconds()))
    stale = age_seconds > 900
    context = classify_local_context(payload, parcel_context=parcel_context)

    shared_context = build_shared_neighborhood_context(shared_neighborhood_context) if shared_neighborhood_context else None

    hazards = derive_hazards(
        payload,
        parcel_context=parcel_context,
        shared_neighborhood_context=shared_context,
        public_context=public_context,
        now=now,
    )
    confidence = derive_confidence(
        payload,
        hazards,
        now=now,
        parcel_context=parcel_context,
        shared_neighborhood_context=shared_context,
        public_context=public_context,
    )
    status_config = HAZARD_THRESHOLDS["status_mapping"]
    state_rules = HAZARD_THRESHOLDS["state_rules"]

    smoke_status = status_from_probability(
        hazards["smoke_probability"],
        unknown_floor=status_config["default_unknown_floor"],
    )
    heat_status = status_from_probability(
        hazards["heat_probability"],
        unknown_floor=status_config["heat_unknown_floor"],
    )
    flood_status = status_from_probability(
        hazards["flood_probability"],
        unknown_floor=status_config["flood_unknown_floor"],
    )

    shelter_status = "unknown"
    if max(hazards["smoke_probability"], hazards["heat_probability"]) >= state_rules["shelter_hazard_floor"] and confidence >= state_rules["shelter_confidence_floor"]:
        shelter_status = smoke_status if hazards["smoke_probability"] >= hazards["heat_probability"] else heat_status
    elif heat_status == "caution" and not context["is_indoor"] and confidence >= state_rules["heat_caution_confidence_floor"]:
        shelter_status = "caution"

    reentry_status = "unknown"
    egress_status = "unknown"
    asset_risk_status = "unknown"

    if not context["is_indoor"] and max(hazards.values()) >= state_rules["asset_risk_hazard_floor"] and confidence >= state_rules["asset_risk_confidence_floor"]:
        asset_risk_status = "caution"

    if not context["is_indoor"] and max(hazards.values()) >= state_rules["egress_hazard_floor"] and confidence >= state_rules["egress_confidence_floor"]:
        egress_status = "caution"

    if flood_status == "caution" and confidence >= 0.5:
        asset_risk_status = "caution"

    if stale and confidence < 0.6:
        shelter_status = "unknown"
        reentry_status = "unknown"
        egress_status = "unknown"
        asset_risk_status = "unknown"

    evidence_mode = "local_only"
    has_nonexpired_public_context = False
    if public_context:
        member_contexts = public_context.get("members", [public_context])
        has_nonexpired_public_context = any(
            public_context_freshness_band(member, now=now) != "expired" for member in member_contexts
        )

    if public_context and has_nonexpired_public_context and not stale and confidence >= state_rules["insufficient_confidence_floor"]:
        evidence_mode = "local_plus_public"
    if stale or confidence < state_rules["insufficient_confidence_floor"]:
        evidence_mode = "insufficient"

    inference_basis = "local_only"
    if stale or confidence < state_rules["insufficient_confidence_floor"]:
        inference_basis = "insufficient"
    elif shared_context and has_nonexpired_public_context:
        inference_basis = "local_plus_shared_plus_public"
    elif shared_context:
        inference_basis = "local_plus_shared"
    elif has_nonexpired_public_context:
        inference_basis = "local_plus_public"

    evidence_contributions = build_evidence_contributions(
        payload=payload,
        parcel_context=parcel_context,
        shared_context=shared_context,
        public_context=public_context,
        hazards=hazards,
        confidence=confidence,
        stale=stale,
        now=now,
        public_context_freshness_band_fn=public_context_freshness_band,
        trust_gates=TRUST_GATES,
    )
    reasons = derive_reasons(
        payload,
        confidence,
        evidence_contributions,
        parcel_context=parcel_context,
        public_context=public_context,
    )
    explanation_payload = build_explanation_payload(
        confidence=confidence,
        evidence_mode=evidence_mode,
        inference_basis=inference_basis,
        evidence_contributions=evidence_contributions,
        parcel_context=parcel_context,
        shared_context=shared_context,
        public_context=public_context,
    )

    source_modes = [payload["provenance"]["source_kind"]]
    if shared_context:
        source_modes.append(shared_context["source_kind"])
    if public_context:
        source_modes.append(public_context["source_kind"])

    return {
        "parcel_id": payload["parcel_id"],
        "computed_at": computed_at,
        "shelter_status": shelter_status,
        "reentry_status": reentry_status,
        "egress_status": egress_status,
        "asset_risk_status": asset_risk_status,
        "confidence": confidence,
        "evidence_mode": evidence_mode,
        "inference_basis": inference_basis,
        "explanation_payload": explanation_payload,
        "reasons": reasons,
        "hazards": hazards,
        "freshness": {
            "latest_observation_at": payload["observed_at"],
            "seconds_since_latest": age_seconds,
            "stale": stale,
        },
        "provenance_summary": {
            "observation_count": 1,
            "source_modes": source_modes,
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
    parser.add_argument(
        "--parcel-context",
        default=None,
        help="Optional path to a parcel context JSON file to combine with local evidence.",
    )
    parser.add_argument(
        "--shared-neighborhood-signal",
        default=None,
        help="Optional path to a shared neighborhood signal JSON file to combine with local evidence.",
    )
    parser.add_argument(
        "--public-context",
        action="append",
        default=[],
        help="Optional path to a public context JSON file to combine with local evidence. May be passed more than once.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    input_path = Path(args.input).resolve()

    try:
        payload = load_json(input_path)
        parcel_context = load_json(Path(args.parcel_context).resolve()) if args.parcel_context else None
        shared_neighborhood_signal = (
            load_json(Path(args.shared_neighborhood_signal).resolve())
            if args.shared_neighborhood_signal
            else None
        )
        public_contexts = [load_json(Path(path).resolve()) for path in args.public_context]
        public_context = combine_public_contexts(public_contexts)
        result = infer_parcel_state(
            payload,
            computed_at=args.computed_at,
            parcel_context=parcel_context,
            shared_neighborhood_context=shared_neighborhood_signal,
            public_context=public_context,
        )
    except (InferenceError, FileNotFoundError, json.JSONDecodeError, KeyError) as exc:
        print(f"ERROR {input_path}: {exc}", file=sys.stderr)
        return 1

    print(json.dumps(result, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    sys.exit(main())
