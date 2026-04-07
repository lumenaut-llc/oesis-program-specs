# Public Smoke Adapter v0

## Purpose

Define the first source-specific adapter contract for public smoke context so the repo can carry regional smoke support into parcel inference without treating it as parcel-local measurement.

## Status

Draft

## Owner

Open Environmental Sensing and Inference System

## Related files

- `README.md`
- `architecture.md`
- `interfaces.md`
- `scripts/normalize_public_smoke_context.py`
- `public-source-metadata-standard.md`
- `../../docs/data-model/public-context-schema.md`
- `../../docs/data-model/examples/raw-public-smoke.example.json`
- `../../legal/licenses/demo-regional-smoke-v1-notice.md`

## Content

## Why smoke needs a separate adapter

Smoke context carries stronger overclaim risk than weather context because:

- regional smoke products are not parcel-local measurements
- smoke severity may change materially over short distance or time
- source products often reflect modeled, interpolated, or delayed conditions

This adapter therefore uses conservative mapping rules and explanation text.

## Raw input shape

The first adapter target is a simple source-shaped JSON object containing:

- source name
- observed timestamp
- parcel identifier
- regional PM2.5 estimate
- optional smoke advisory level

Example raw payload:

```json
{
  "source_name": "demo_regional_smoke_v1",
  "observed_at": "2026-03-30T19:40:00Z",
  "parcel_id": "parcel_demo_001",
  "regional_pm25_ugm3": 38.0,
  "smoke_advisory_level": "moderate"
}
```

## Adapter output shape

The adapter emits the canonical public-context object defined in `../../docs/data-model/public-context-schema.md`.

Initial hazard translation rules:

- `smoke_probability`
  derived conservatively from regional PM2.5 bands and advisory level
- `heat_probability`
  held low by default because a smoke adapter is not a heat source
- `flood_probability`
  held low by default because a smoke adapter is not a flood source

## Design rules

- Regional smoke support must not be described as direct parcel smoke truth.
- The adapter should preserve source freshness and source identity.
- Smoke-only public context should improve explanation quality before it drives strong parcel statuses.
- Strong smoke-related parcel outputs still require corroboration from local PM sensing or multiple supporting sources.

## Next steps

- attach completed third-party source notices for real smoke feeds
- define freshness expiry for smoke products separately from weather products
- decide how public smoke and public weather records should be merged when both are present
