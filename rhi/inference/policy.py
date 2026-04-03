import json
from datetime import datetime
from pathlib import Path

from rhi.common.repo_paths import INFERENCE_CONFIG_DIR

CONFIG_DIR = INFERENCE_CONFIG_DIR
PUBLIC_CONTEXT_POLICY_PATH = CONFIG_DIR / "public_context_policy.json"
HAZARD_THRESHOLDS_PATH = CONFIG_DIR / "hazard_thresholds_v0.json"
TRUST_GATES_PATH = CONFIG_DIR / "trust_gates_v0.json"


def load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def parse_time(ts: str) -> datetime:
    return datetime.fromisoformat(ts.replace("Z", "+00:00"))


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
