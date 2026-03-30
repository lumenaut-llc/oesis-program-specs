# Architecture

## Summary

The inference engine consumes normalized observations and produces parcel-state snapshots. It should remain separate from ingest so raw evidence handling, schema validation, and transport concerns do not get mixed with hazard reasoning. The engine evaluates each parcel using available evidence, computes hazard-specific probabilities or scores, and then maps those into homeowner-readable statuses with confidence and explanation payloads.

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
- optional public context such as weather or smoke layers
- hazard-specific thresholds or model parameters

## Outputs

- parcel-state snapshots
- hazard-specific supporting scores
- explanation payloads for UI and auditability
- confidence and freshness values

## Internal modules

- parcel evidence assembler
- hazard scoring module
- uncertainty and freshness evaluator
- status mapper
- explanation generator
- parcel-state persistence writer

## External dependencies

- observation store
- parcel metadata store
- optional public hazard feeds
- policy rules from privacy and governance docs
- threshold or model configuration source

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
