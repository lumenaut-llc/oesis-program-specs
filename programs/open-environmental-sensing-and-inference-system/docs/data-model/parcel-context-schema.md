# Parcel Context Schema

## Purpose

Define the minimum parcel and installation context needed for the inference engine to interpret observations without pretending a node reading is equivalent to parcel truth.

## Status

Draft

## Owner

Open Environmental Sensing and Inference System

## Related files

- `node-observation-schema.md`
- `parcel-state-schema.md`
- `../../hardware/bench-air-node/README.md`
- `../../software/inference-engine/interfaces.md`

## Content

## Why this schema exists

The current repo has node-observation and parcel-state contracts, but it does not yet have a canonical parcel-context contract between them.

That gap matters because hazard reasoning depends on context such as:

- whether a node is indoor, sheltered, or outdoor
- whether a node is actually attached to a parcel
- whether a node is installed at a runoff-relevant low point
- whether parcel priors are known or absent

Without parcel context, the system can only see measurements. It cannot responsibly interpret their parcel relevance.

## Minimum parcel-context object

```json
{
  "parcel_id": "parcel_123",
  "site_profile": {
    "structure_type": "single_family",
    "parcel_area_m2": 740,
    "climate_zone": "unknown",
    "notes": null
  },
  "node_installations": [
    {
      "node_id": "bench-air-01",
      "node_type": "bench_air_node",
      "location_mode": "indoor",
      "install_role": "reference_indoor",
      "placement_notes": "office near hallway",
      "height_m": 1.2,
      "exposure_bias_flags": [
        "hvac_possible"
      ],
      "installed_at": "2026-03-30T18:00:00Z"
    }
  ],
  "parcel_priors": {
    "heat_retention_class": "unknown",
    "runoff_tendency_class": "unknown",
    "smoke_exposure_class": "unknown"
  }
}
```

## Required top-level fields

- `parcel_id`
- `site_profile`
- `node_installations`
- `parcel_priors`

## Site profile fields

- `structure_type`
  Suggested initial enum: `single_family`, `duplex`, `multi_unit`, `unknown`
- `parcel_area_m2`
  Optional numeric field for later use in parcel modeling
- `climate_zone`
  Optional string for future external-context interpretation
- `notes`
  Optional free-text for admin use, not inference by default

## Node installation fields

Each node linked to a parcel should carry explicit installation context.

Minimum fields:

- `node_id`
- `node_type`
- `location_mode`
- `install_role`
- `placement_notes`
- `height_m`
- `exposure_bias_flags`
- `installed_at`

Suggested initial `location_mode` enum:

- `indoor`
- `sheltered`
- `outdoor`
- `low_point`

Suggested initial `install_role` enum:

- `reference_indoor`
- `reference_sheltered`
- `primary_outdoor_air`
- `runoff_low_point`
- `thermal_scan`
- `unknown`

Suggested initial `exposure_bias_flags` values:

- `hvac_possible`
- `kitchen_adjacent`
- `garage_adjacent`
- `direct_sun_possible`
- `under_eave`
- `not_runoff_representative`

## Parcel priors fields

The initial parcel-prior model should stay categorical.

Suggested initial fields:

- `heat_retention_class`
- `runoff_tendency_class`
- `smoke_exposure_class`

Suggested initial enum for each:

- `low`
- `moderate`
- `high`
- `unknown`

## Interpretation rules

- A node reading is a point observation, not a parcel-wide condition.
- `location_mode` and `install_role` constrain what hazards the node may influence.
- `indoor` and `sheltered` nodes may contribute evidence, but should not be treated as direct parcel-wide outdoor truth.
- `runoff_low_point` context is required before flood-node observations can support stronger runoff or accumulation claims.
- Missing parcel priors should not be silently replaced with assumed values.

## MVP usage rules

- The first MVP may attach one bench-air-node to one parcel with minimal site profile information.
- If parcel context is missing, the inference engine should lower confidence and favor `unknown` outputs.
- Parcel context should be editable without rewriting raw observations.

## Follow-up additions

- parcel geometry linkage
- building-entry-point metadata
- canopy and shade context
- drainage-path annotations
- install-photo references
