# Architecture

## Summary

The inference engine consumes normalized observations and produces parcel-state snapshots. It should remain separate from ingest so raw evidence handling, schema validation, and transport concerns do not get mixed with hazard reasoning. The engine evaluates each parcel using available evidence, computes hazard-specific probabilities or scores, and then maps those into homeowner-readable statuses with confidence and explanation payloads.

The engine should produce condition estimates rather than implied safety authorizations, and it should preserve enough provenance for audit without leaking private parcel detail into downstream shared surfaces.

## Core objects

- normalized observation
- parcel context
- hazard evidence set
- hazard score or probability
- parcel-state snapshot
- explanation payload
- provenance summary

## Inputs

- normalized observations from the ingest service
- parcel metadata such as structure type or node placement context
- parcel-context records describing installation role and parcel priors
- optional shared neighborhood signals when the parcel's sharing mode and policy allow them
- optional public context such as weather or smoke layers
- hazard-specific thresholds or model parameters
- policy constraints on whether shared neighborhood evidence is allowed for the parcel's active sharing mode

## Outputs

- parcel-state snapshots
- hazard-specific supporting scores
- explanation payloads for UI and auditability
- confidence and freshness values
- source-mode metadata suitable for provenance summaries

## Internal modules

- parcel evidence assembler
- hazard scoring module
- uncertainty and freshness evaluator
- status mapper
- explanation generator
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
- allowing public feeds to overwhelm homeowner-owned local evidence without explanation
- letting shared-neighborhood evidence affect parcel outputs without preserving source distinctions
- letting stale public context continue to influence parcel outputs as if it were current
