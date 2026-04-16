# Open Questions

> **Status (2026-04-15):** All questions below now have recommended directions.
> These directions are reflected in the v1.0 parcel-platform implementation
> (`oesis-runtime/oesis/parcel_platform/v1_0/`). Treat them as decided unless
> a future architecture review reopens them.

- Should the dwelling-facing UI show raw probabilities, or should it emphasize statuses plus short explanations?

  > **Recommended direction:** Statuses plus short explanations. Show confidence bands (low/medium/high) rather than numeric probabilities. Raw probabilities available in evidence-summary for advanced users.

- How should the platform distinguish `unknown` due to missing local evidence from `unknown` due to conflicting evidence?

  > **Recommended direction:** Distinguish in the explanation_payload. Use 'insufficient evidence' for missing data and 'inconclusive evidence' for conflicting data. Both map to unknown status but the explanation differs.

- What history depth is useful in the MVP: hours, days, or event-based transitions only?

  > **Recommended direction:** Event-based transitions for MVP (status changes, evidence mode changes, freshness failures). Continuous timeseries deferred to v1.0+ when storage and UI patterns are proven.

- What user controls belong in the first version: acknowledge alerts, add parcel notes, or manage sharing preferences?

  > **Recommended direction:** Acknowledge alerts and add parcel notes only. Sharing preferences deferred to v1.0 when consent enforcement is real.

- How should the UI phrase low-confidence outputs so they remain useful without sounding falsely authoritative?

  > **Recommended direction:** Use 'estimate' language consistently. Example: 'This is a low-confidence estimate based on limited local evidence.' Never use 'safe' or 'clear' at low confidence.

- Which `v1.5` bridge objects should appear early in the parcel UI: house-state only, or also intervention and verification timelines?

  > **Recommended direction:** House-state first (it has the clearest standalone value). Intervention and verification timelines only after house-state proves useful in at least one pilot.

- When should draft `control_compatibility` records become visible in the parcel UI, given that full compatibility inventory is primarily a `v2.5` concern?

  > **Recommended direction:** Keep invisible in the parcel UI until v2.5. Draft capture is an API-level concern for pilot operators, not a user-facing feature.
