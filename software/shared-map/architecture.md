# Architecture

## Summary

The shared map is the neighborhood condition layer, not a public parcel surveillance tool. It should present coarse, delayed, thresholded shared conditions without revealing which specific parcel contributed a real hazard signal.

This is a later-stage surface relative to the parcel-first baseline. It should
not be described as though route, block, or neighborhood resilience are already
core current-v1 product behavior.

## Core objects

- neighborhood cell summary
- aggregate hazard indicator
- participation threshold state
- public-context overlay
- provenance class summary

## Inputs

- shared-mode contributions permitted by active sharing settings
- public context layers suitable for map display
- map publication policy constraints

### Planned: admissibility gate on shared-layer eligibility

Per gap register G22 and the shared-layer eligibility rule in [`../../architecture/system/sensor-placement-and-representativeness-guide.md`](../../architecture/system/sensor-placement-and-representativeness-guide.md) "Product behavior implications", shared-layer contribution requires the contributing node's most recent observation to be admissible per [`../../architecture/system/calibration-program.md`](../../architecture/system/calibration-program.md) §C (physical sensors) or [`../../architecture/system/adapter-trust-program.md`](../../architecture/system/adapter-trust-program.md) §C (adapter-derived).

Concrete consequence: a well-placed but uncalibrated node (for example, a bench-air node without a populated reference instrument, G13) cannot contribute to shared-map aggregation even if it has an active sharing setting. The gate runs **after** sharing-policy check and **before** the thresholding / coarsening modules.

Status: **planned**. Ships as part of the v0.5 governance slice or later. Until wired, the current aggregation-and-thresholding module treats all opted-in contributions as eligible — which over-counts during the v0.1 / v0.2 period where admissibility tooling itself (G15) is not yet active.

## Outputs

- coarse shared neighborhood condition view
- map-ready aggregate summaries for participating users
- coverage or participation disclaimer metadata

## Internal modules

- aggregation and thresholding module
- spatial coarsening module
- provenance labeler
- publication policy filter

## External dependencies

- shared-data store
- public-context store
- policy rules from privacy governance and legal docs

## Realtime needs

- neighborhood updates should prefer delay and safety over apparent real-time precision
- publication should be suppressible when participation is too low or data is too sparse

## Risks

- revealing the likely identity of a contributing parcel
- implying full neighborhood visibility under partial adoption
- mixing public context and participant-contributed signals without distinction
- exposing map timestamps or counts that enable singling out
