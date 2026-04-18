# Hazard Logic v0

## Purpose

Set the first honest inference posture for MVP parcel-state generation so the reference engine stays useful without overclaiming what current hardware can support.

## Status

Draft

## Owner

Open Environmental Sensing and Inference System

## Related files

- `README.md`
- `architecture.md`
- `interfaces.md`
- `config/hazard_thresholds_v0.json`
- `config/trust_gates_v0.json`
- `python3 -m oesis.inference.infer_parcel_state` (in `oesis-runtime`)
- [`parcel-context-schema.md`](https://github.com/lumenaut-llc/oesis-contracts/blob/main/v0.1/parcel-context-schema.md)
- [`evidence-mode-and-observability.md`](https://github.com/lumenaut-llc/oesis-contracts/blob/main/v0.1/evidence-mode-and-observability.md)

## Content

## Scope

This document defines the first rules posture for three hazards:

- smoke
- heat
- pluvial flooding and runoff

It does not define a production model. It defines what the MVP reference logic may and may not do.

The reference thresholds for this ruleset should live in `config/hazard_thresholds_v0.json` rather than remaining hardcoded in the inference script.
Trust-gating thresholds for stale data, low-confidence suppression, and cross-source disagreement should live in `config/trust_gates_v0.json`.

## Governing principles

- prefer transparent rules over complex models
- separate point observations from parcel estimates
- prefer `unknown` when evidence is weak
- keep reasons and provenance attached to every output
- do not let the reference pipeline imply stronger claims than the hardware supports
- treat shared neighborhood evidence as supporting context, not parcel-local confirmation

## Hazard observability by node class

`bench-air-node`

- good for: indoor or sheltered microclimate evidence, packet/schema bring-up, device health, trend detection
- weak for: parcel-wide outdoor heat inference
- not sufficient for: direct smoke concentration or flood condition

`mast-lite`

- intended for: more credible outdoor heat and weather context
- still not sufficient for: direct smoke concentration without PM sensing

`weather-pm-mast`

- intended for: outdoor weather plus PM-based smoke evidence

`flood-node`

- intended for: low-point runoff and accumulation evidence at a documented install point

## Smoke logic v0

Allowed inputs now:

- bench-air gas-trend anomaly as weak indoor or sheltered evidence only
- optional public smoke or air-quality context
- explicit parcel context

Rules:

- bench-air gas resistance must not be mapped as direct smoke concentration
- gas-trend anomalies may support a reason such as "indoor air anomaly detected" but should not independently drive strong parcel smoke status
- if only bench-air evidence is present, `smoke_probability` should remain low or uncertain and should usually preserve `unknown`-leaning parcel outputs
- stronger smoke-related parcel outputs require public corroboration or a future PM-capable outdoor node
- regional smoke public context may raise smoke support conservatively, but it must still be explained as public-context support rather than local parcel confirmation
- shared neighborhood smoke signals may raise smoke support conservatively when contribution thresholds are met, but they must still be explained as neighboring shared context rather than local parcel observation

## Heat logic v0

Allowed inputs now:

- bench-air temperature and humidity
- optional public weather context
- parcel context and priors when available

Rules:

- indoor bench-air readings may indicate indoor heat burden concerns, but not parcel-wide outdoor heat truth
- sheltered readings may contribute limited local context with reduced confidence
- parcel heat-retention priors may adjust heat support modestly, not dominate it
- meaningful outdoor heat estimates should prefer `mast-lite` or another outdoor-qualified installation
- if the only local evidence is indoor bench-air, parcel-state outputs should use cautious reasoning and favor `unknown` or low-confidence non-unsafe statuses unless corroborated by public context
- shared neighborhood heat signals may add supporting context, but should not override parcel siting limits or weak local observability

## Flood logic v0

Allowed inputs now:

- public rainfall or flood context only

Rules:

- bench-air observations must not drive flood probability
- parcel runoff priors may shape interpretation only when flood-capable evidence exists
- flood-related parcel outputs should remain `unknown` or public-context-limited until a dedicated flood-node exists
- future flood-node logic must be tied to documented low-point installation context
- shared neighborhood flood signals may support awareness of nearby runoff conditions, but they do not confirm flood conditions on the target parcel

## Status mapping rules

The current parcel-state schema includes:

- `shelter_status`
- `reentry_status`
- `egress_status`
- `asset_risk_status`

For MVP reference logic:

- these fields are parcel condition estimates, not directives
- `unknown` should be the default when evidence is sparse, weakly representative, stale, or single-source
- `unsafe` should require stronger and more hazard-relevant evidence than the current bench-air-only scaffold
- `reentry` and `egress` should be especially conservative because they can sound action-like even when the product avoids command language

## Trust gates v0

The reference engine may emit `system` limitations when the estimate is being held back by inference discipline rather than by a direct evidence source.

Initial trust gates:

- stale local observation gate
- low-confidence gate
- cross-source disagreement gate when regional or shared context materially outweighs the local reading

These gates should be configured in `config/trust_gates_v0.json` rather than embedded as magic numbers in the inference script.

## Minimum reasons guidance

Reasons should mention:

- what was directly observed
- what was inferred
- what evidence is missing
- why confidence is limited

Example reasoning posture:

- "Indoor temperature is elevated at the local node location."
- "No outdoor parcel-confirming sensor is available."
- "Public context does not currently confirm severe smoke conditions."
- "Confidence is limited because the current estimate relies on one indoor node."

## Required changes to the reference scaffold

The initial scaffold in `python3 -m oesis.inference.infer_parcel_state` is useful for demonstrating data flow, but it should be revised so that:

- bench-air gas resistance does not behave like smoke concentration
- flood probability is not inferred from a generic `outdoor` location mode alone
- `unknown` is used more often when only single-node bench-air evidence exists
- `evidence_mode` reflects whether public context is absent, present, or insufficient

## Out of scope for v0

- neighborhood inference
- model training
- H3 aggregation
- advanced parcel priors
- action recommendation language
