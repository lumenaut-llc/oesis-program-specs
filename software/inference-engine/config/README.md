# Inference Engine Config

Configuration files for the inference engine's hazard estimation and
trust-gating logic.

- `hazard_thresholds_v0.json` — Probability bands for smoke, heat, and flood hazards
- `public_context_policy.json` — Public data source trust and freshness policy
- `trust_gates_v0.json` — Confidence gates, freshness limits, and cross-source agreement rules
- `v1.0/` — Forward-lane config overrides

These files are the program-specs reference copies. The runtime copies live
in `oesis-runtime/oesis/assets/v0.1/config/inference/`.
