# Release Lanes

Use additive release lanes from the release directory root:

- [`v.0.1/`](v.0.1/) — frozen v0.1 baseline (one parcel, one bench-air node)
- [`v0.2/`](v0.2/) — first widened parcel kit (bench-air + mast-lite)
- [`v0.3/`](v0.3/) — first flood-capable runtime
- [`v0.4/`](v0.4/) — multi-node registry and evidence composition
- [`v0.5/`](v0.5/) — operational governance enforcement
- [`v1.0/`](v1.0/) — first fielded parcel-intelligence lane
- [`v1.5/`](v1.5/) — measurement-to-intervention bridge

## Progression model

Each pre-1.0 slice represents a materially expanded accepted runnable
reference. See `architecture/current/pre-1.0-version-progression.md` for
promotion criteria.

```
v0.1 → v0.2 → v0.3 → v0.4 → v0.5 → v1.0
 │       │       │       │       │       │
 │       │       │       │       │       └─ fielded parcel kit + trust scoring
 │       │       │       │       └─ governance enforcement (consent, revocation, retention)
 │       │       │       └─ node lifecycle + evidence composition + install metadata
 │       │       └─ flood observation family in canonical ingest
 │       └─ two-node kit (indoor + sheltered outdoor)
 └─ one parcel, one bench-air, one pipeline
```
