# Public Context Freshness Policy

## Purpose

Define when public context is fresh enough to materially support parcel inference and when it should be downgraded or ignored.

## Status

Draft

## Owner

Resilient Home Intelligence

## Related files

- `interfaces.md`
- `architecture.md`
- `hazard-logic-v0.md`
- `config/public_context_policy.json`
- `scripts/infer_parcel_state.py`
- `../ingest-service/public-source-metadata-standard.md`

## Content

## Why this policy exists

Public context helps the system operate under partial adoption, but it creates a trust problem if stale regional data is allowed to move parcel-state outputs as if it were current evidence.

This policy keeps the first inference scaffold conservative.

## Freshness bands

Suggested initial freshness bands for public context:

- `fresh`
  age less than or equal to 30 minutes
- `aging`
  age greater than 30 minutes and less than or equal to 2 hours
- `stale`
  age greater than 2 hours and less than or equal to 6 hours
- `expired`
  age greater than 6 hours

## MVP engine behavior

`fresh`

- public context may materially support parcel inference
- confidence may increase modestly
- `local_plus_public` may be used if local evidence also exists

`aging`

- public context may still support parcel inference
- confidence gain should be reduced
- reasons should acknowledge that public context is aging

`stale`

- public context may appear in provenance and reasons
- confidence gain should be minimal or zero
- public context should not be the sole basis for stronger parcel-state transitions

`expired`

- public context should be ignored for hazard support
- the engine may mention that it was discarded for staleness
- it should not affect `evidence_mode`

## Hazard-specific notes

- smoke context may need stricter freshness than weather context
- flood context may also need stricter freshness when tied to active runoff conditions
- source-specific freshness thresholds should live in machine-readable policy rather than being hardcoded in inference
- the reference policy file for the MVP scaffold lives in `config/public_context_policy.json`

## Explanation guidance

When public context is not fresh, reasons should say so plainly rather than silently lowering confidence.

Example:

- "Regional smoke context is present but aging, so it provides limited support."
- "Public weather context was too old to materially affect the current parcel estimate."
