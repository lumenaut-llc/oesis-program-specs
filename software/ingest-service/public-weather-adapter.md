# Public Weather Adapter v0

## Purpose

Define the first source-specific adapter contract for external public weather context so the repo has one concrete path from raw external data into the canonical public-context object used by inference.

## Status

Draft

## Owner

Open Environmental Sensing and Inference System

## Related files

- `README.md`
- `architecture.md`
- `interfaces.md`
- `python3 -m oesis.ingest.normalize_public_weather_context` (in `oesis-runtime`)
- `public-source-metadata-standard.md`
- `../../contracts/public-context-schema.md`
- `../../contracts/v0.1/examples/raw-public-weather.example.json`
- `../../contracts/v0.1/examples/public-context.example.json`
- `../../legal/licenses/demo-regional-weather-v1-notice.md`

## Content

## Why weather first

Weather and heat context are the simplest external source family to integrate first because:

- they are broadly available from public feeds
- they support heat inference without pretending local parcel truth
- they do not require the same source-specific caveats as smoke composition or flood-depth products

This adapter remains a reference scaffold. It is not yet a production source integration.

## Raw input shape

The first adapter target is a simple source-shaped JSON object containing:

- source name
- observed timestamp
- parcel identifier
- regional air temperature
- regional relative humidity
- optional advisory tags

Example raw payload:

```json
{
  "source_name": "demo_regional_weather_v1",
  "observed_at": "2026-03-30T19:40:00Z",
  "parcel_id": "parcel_demo_001",
  "regional_temperature_c": 31.0,
  "regional_relative_humidity_pct": 34.0,
  "advisories": [
    "warm_afternoon"
  ]
}
```

## Adapter output shape

The adapter emits the canonical public-context object defined in `../../contracts/public-context-schema.md`.

Initial hazard translation rules:

- `heat_probability`
  derived from regional temperature with a modest upward adjustment when humidity is elevated
- `smoke_probability`
  held low by default because weather-only context is not a smoke source
- `flood_probability`
  held low by default because weather-only context without rainfall/runoff logic is not a flood source

## Reference mapping rules

- regional temperature below 24 C -> low heat support
- 24 C to under 29 C -> modest heat support
- 29 C to under 34 C -> moderate heat support
- 34 C and above -> elevated heat support
- humidity above 55 percent may increase heat support slightly
- advisory strings may contribute explanation text but should not directly override numeric hazard bounds

## Design rules

- Keep source-specific quirks inside the adapter, not in parcel inference.
- Preserve the source name and timestamp in the normalized public-context object.
- Prefer conservative hazard support over aggressive source translation.
- Do not use a weather-only adapter to generate strong smoke or flood conclusions.

## Next steps

- add a smoke-context adapter with explicit source notice metadata
- add a rainfall or runoff-supporting adapter for flood context
- decide how multiple public-context records should be merged when they arrive close together
