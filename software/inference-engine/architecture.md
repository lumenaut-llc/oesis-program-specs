# Architecture

## Summary

The inference engine consumes normalized observations and produces parcel-state snapshots. It should remain separate from ingest so raw evidence handling, schema validation, and transport concerns do not get mixed with hazard reasoning. The engine evaluates each parcel using available evidence, computes hazard-specific probabilities or scores, and then maps those into parcel operator-readable statuses with confidence and explanation payloads.

The engine should produce condition estimates rather than implied safety authorizations, and it should preserve enough provenance for audit without leaking private parcel detail into downstream shared surfaces.

The current parcel-first direction also requires the engine to preserve three
distinct reasoning surfaces inside the parcel-state output:

- parcel metadata priors that shape baseline expectations
- local-versus-public divergence records that expose hyperlocal mismatch
- contrastive fact-versus-foil explanations showing what local evidence changed

The current-truth reference path is still the narrow parcel-sensing baseline.
Support for `mast-lite` as a meaningful second local evidence source belongs to
the widened two-node kit and should be described as **program-phase `v0.2`**
when promoted, not as though the accepted baseline already expanded. Later
**`v1.5`** bridge objects such as house state, action logs, and verification
remain separate support surfaces rather than additions to the current
parcel-state contract.

The next serious product step after that widened kit is the **measurement-to-
intervention bridge**. For inference, that means learning to reason over:

- outdoor hazard evidence
- indoor response evidence
- household operating state
- action records
- measured outcome windows

without collapsing those later surfaces back into the current parcel-state
baseline.

The first serious closed-loop target should be smoke protection:

- outdoor evidence
- indoor PM / temperature / RH response
- bounded household action such as recirculation + fan + purifier
- measured improvement over a bounded response window such as 30–90 minutes

## Core objects

- normalized observation
- parcel context
- hazard evidence set
- hazard score or probability
- parcel-state snapshot
- explanation payload
- divergence record
- public-only counterfactual
- contrastive explanation
- provenance summary

## Currently consumed observation types

The inference engine currently accepts these observation types for parcel-state
computation:

- `air.node.snapshot` — from bench-air-node and mast-lite
- `equipment.circuit.snapshot` — from circuit-monitor (auto-derived into
  `equipment_state_observation` for house-state bridge)
- `air.pm.snapshot` — from weather-pm-mast; outdoor PM2.5 feeds smoke
  probability via `outdoor_pm25_bands`, temperature and gas resistance feed
  existing heat and smoke paths
- `flood.low_point.snapshot` — from flood-node; water depth and rise rate
  feed flood probability via config-driven bands, with a provisional
  calibration penalty

## Inputs

- normalized observations from the ingest service
- parcel metadata such as structure type or node placement context
- parcel-context records describing installation role and parcel priors
- optional shared neighborhood signals when the parcel's sharing mode and policy allow them
- optional public context such as weather or smoke layers
- hazard-specific thresholds or model parameters
- versioned parcel-prior rule configuration
- versioned divergence-threshold configuration
- policy constraints on whether shared neighborhood evidence is allowed for the parcel's active sharing mode

### Planned: admissibility filter on normalized observations

Per ADR [0009](../../meta/adr/0009-admissibility-schema-split-facts-vs-decision.md) and [`../../architecture/system/calibration-program.md`](../../architecture/system/calibration-program.md) §C, the inference engine consumes the `admissible_to_calibration_dataset: bool` + `admissibility_reasons: [string]` fields that ingest attaches to each normalized observation.

- **Coefficient fitting** (when the v1 hazard formula's shadow path is active per [`hazard-formula-v1.md`](hazard-formula-v1.md)): admits **only** observations where `admissible_to_calibration_dataset: true`. Non-admissible observations remain in audit logs but do not train coefficients.
- **Parcel-state computation**: may consume non-admissible observations but with reduced confidence and with `admissibility_reasons` surfaced in the explanation payload.
- **Branch by tier**: observations with `adapter_tier: tier_1_passive` or `tier_2_adapter` are evaluated under [`../../architecture/system/adapter-trust-program.md`](../../architecture/system/adapter-trust-program.md) §C rather than calibration-program §C. The same `admissible_to_calibration_dataset` output is produced; only the rule set differs.

Status: **planned**. Schema extensions tracked as G17; runtime wiring tracked as G15.

## Outputs

- parcel-state snapshots
- hazard-specific supporting scores
- explanation payloads for UI and auditability
- parcel-prior application summaries
- divergence records with persistence and confidence
- public-only foil outputs for audit and verification
- contrastive explanations with verification placeholders
- confidence and freshness values
- source-mode metadata suitable for provenance summaries

Later bridge and response outputs should remain separate first-class records,
for example:

- response-window comparisons
- intervention recommendations
- verification results

Those should sit beside parcel-state rather than being hidden inside it.

## Internal modules

- parcel evidence assembler
- hazard scoring module
- parcel-prior resolver
- divergence classifier
- uncertainty and freshness evaluator
- status mapper
- contrastive explanation generator
- parcel-state persistence writer
- provenance sanitizer for downstream presentation layers

## External dependencies

- observation store
- parcel metadata store
- optional public hazard feeds
- policy rules from privacy and governance docs
- threshold or model configuration source
- machine-readable public-context freshness policy
- machine-readable hazard-threshold configuration

## Realtime needs

- The engine should update a parcel quickly after new evidence arrives, but correctness and traceability matter more than sub-second latency.
- It should tolerate partial evidence and recompute when new observations fill gaps.
- It should support both event-driven updates and scheduled recomputation.

## Risks

- pretending sparse indoor observations are enough to make strong parcel safety claims
- hiding uncertainty behind a single status label
- mixing hazard scoring rules with presentation logic
- failing to represent stale evidence clearly
- allowing public feeds to overwhelm dwelling-scale local evidence without explanation
- hiding hyperlocal divergence inside a fused score instead of preserving it as evidence
- letting parcel metadata influence outcomes without exposing which factors changed the baseline
- letting shared-neighborhood evidence affect parcel outputs without preserving source distinctions
- letting stale public context continue to influence parcel outputs as if it were current
- adding action or control logic before the system can verify whether conditions
  actually improved
