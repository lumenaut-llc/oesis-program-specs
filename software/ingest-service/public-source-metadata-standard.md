# Public Source Metadata Standard

## Purpose

Define the minimum metadata every external public source must carry before it is allowed to influence parcel inference.

## Status

Draft

## Owner

Open Environmental Sensing and Inference System

## Related files

- `public-weather-adapter.md`
- `public-smoke-adapter.md`
- `public-context-freshness-policy.md`
- `../../legal/third-party-data-source-notice-template.md`

## Content

## Governing rule

No external public source should influence parcel-state logic unless the repo has enough metadata to explain:

- what the source is
- how fresh it is expected to be
- what limits apply to its interpretation
- what provenance label should be shown to users

## Minimum source metadata

Each source used by an adapter should have a completed notice or equivalent record containing:

- source name
- source operator
- source URL
- data category
- geographic scope
- update cadence
- access method
- license or terms
- attribution requirement
- redistribution rule
- known latency or freshness limits
- known quality limitations
- intended use in product
- provenance label shown to users

## Operational requirements

- adapter docs must name the source metadata record they depend on
- source metadata must be reviewed before a feed is used in product logic
- source freshness and source quality limits must be translated into adapter or inference policy
- the parcel view must distinguish public context from homeowner-contributed evidence

## MVP rule

For the reference scaffold, hand-authored demo sources are acceptable, but they should still carry notice records so the repo teaches the right integration discipline from the beginning.
