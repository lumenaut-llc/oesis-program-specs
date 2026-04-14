# Interfaces

## Public API surfaces

- `GET /v1/shared-map/tiles`
  Return coarse aggregated map tiles or cells suitable for the current authorized audience.
- `GET /v1/shared-map/legend`
  Return map legend, provenance labels, and data-delay explanations.
- `GET /v1/shared-map/coverage`
  Return coverage and participation disclaimers without exposing singling-out details.
- `GET /v1/admin/shared-map/config`
  Return reference shared-map configuration, including whether a file-backed sharing store is in use.
- `POST /v1/admin/shared-map/inspect`
  Aggregate a candidate shared-map payload and return an operator-facing inspection summary with visible/suppressed cell counts.

## Internal events / jobs

- `shared.aggregate.updated`
  Refresh cached neighborhood aggregates after new eligible contributions arrive.
- `shared.aggregate.suppressed`
  Mark outputs hidden because policy thresholds are not met.
- `shared.publication.reviewed`
  Record approval state for a map layer or pilot-specific view.

## Data contracts

- shared-map outputs should carry coarse spatial identifiers rather than exact parcel geometry
- every payload should identify whether a visible layer comes from shared parcel operator contributions, public context, or both
- payloads should include delay/freshness metadata suitable for user-facing disclaimers
- payloads should not include exact contributing parcel identifiers or raw observation refs

## Open questions

- Which coarse spatial unit is safest and still useful for early pilots?

  > **Recommended direction:** Use a grid cell large enough that minimum 3 participating parcels are required before any condition is shown. Census block groups or equivalent-sized hexagonal cells are a reasonable starting point. Exact size should be tuned during pilot to balance utility against singling-out risk.

- How should coverage be communicated without leaking low-participation counts?

  > **Recommended direction:** Display 'insufficient coverage' for cells below the participation threshold rather than showing zero or empty states that imply absence. Never display exact participant counts. Every shared-map view should carry a persistent banner: 'Neighborhood conditions are delayed, approximate, and based on limited participation.'
