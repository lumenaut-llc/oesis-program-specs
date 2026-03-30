# Inference Engine

## Purpose

The logic layer that turns normalized observations, public context, and explicit uncertainty handling into parcel-level statuses.

## Current responsibilities

- consume normalized observations from the ingest service
- combine parcel evidence with hazard-specific heuristics or models
- produce parcel-state outputs with confidence, freshness, and reasons
- keep provenance attached to every parcel decision
- avoid overclaiming when evidence is sparse, stale, or conflicting

## Needs from other workstreams

- glossary alignment
- governance rules
- procurement assumptions for node capabilities
- hazard model inputs

## MVP focus

The first MVP should support parcel inference from a small evidence set:
- bench-air-node observations
- optional public weather context
- parcel metadata required for basic interpretation

The goal is not perfect classification. The goal is a transparent first-pass parcel state with explicit uncertainty and reasons.

## Adjacent systems

- ingest service delivers normalized observations
- parcel platform reads parcel-state outputs
- shared-map may later consume parcel-level summaries
- privacy and governance define which evidence can be shared across parcel boundaries
