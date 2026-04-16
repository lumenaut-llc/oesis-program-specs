# Open Questions

> **Status (2026-04-15):** All questions below now have recommended directions.
> These directions are reflected in the v1.0 shared-map implementation
> (`oesis-runtime/oesis/shared_map/v1_0/`). Treat them as decided unless a
> future architecture review reopens them.

- What minimum participation threshold should be required before any neighborhood condition is shown?

  > **Recommended direction:** Minimum 3 participating parcels per cell before any neighborhood condition is shown. Below that, display 'insufficient coverage' rather than nothing.

- How should route or block surfaces stay visibly distinct from parcel-state outputs when those later layers arrive?

  > **Recommended direction:** Route and block surfaces should use a visually distinct color palette and labeling scheme. Never display route conditions on the same layer as parcel-state outputs without clear separation.

- Which shared signals belong in the first shared-map implementation versus later `v4` route/community resilience work?

  > **Recommended direction:** Smoke and heat neighborhood trends only. Flood neighborhood signals deferred until flood observation family is implemented. Route/community resilience is v4+.

- How should the map explain that it is delayed, thresholded, and partial rather than a real-time parcel-resolution surveillance layer?

  > **Recommended direction:** Every shared-map view should carry a persistent banner: 'Neighborhood conditions are delayed, approximate, and based on limited participation. They do not represent real-time or complete coverage.'
