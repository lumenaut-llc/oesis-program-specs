# Release v0.2 — First Widened Parcel Kit

## Purpose

Track release readiness for the v0.2 accepted runnable slice: the first
two-node parcel kit with stable indoor + sheltered outdoor operation.

## Sign-off sentence

**v0.2** means: the system operates with bench-air (indoor) and mast-lite
(sheltered outdoor) bound to one parcel, with both observation streams
normalized through ingest, combined in inference, and reflected in a
parcel view that explains the source mix.

## What v0.2 adds over v0.1

- mast-lite as a second node class contributing to parcel-state
- Node registry binding two nodes to one parcel
- Parcel view that distinguishes indoor vs sheltered outdoor evidence
- Field-hardening posture for sheltered outdoor deployment

## Release artifacts

- `v0.2-scope-matrix.md` — what is in and out of v0.2 scope
- `v0.2-gap-register.md` — gaps between current state and v0.2 readiness
- `v0.2-acceptance-criteria.md` — concrete acceptance tests
- `v0.2-implementation-status.md` — per-surface implementation status

## Related

- `../v0.1/` — v0.1 baseline (frozen)
- `../v1.0/` — v1.0 target release
- `../../architecture/current/pre-1.0-version-progression.md` — promotion model
- `../../architecture/current/milestone-roadmap.md` — milestone 2 maps to v0.2
