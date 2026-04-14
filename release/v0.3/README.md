# Release v0.3 — First Flood-Capable Runtime

## Purpose

Track release readiness for the v0.3 accepted runnable slice: the first
runtime with a dedicated flood observation family normalized through the
canonical ingest path.

## Sign-off sentence

**v0.3** means: the system can ingest flood-node observations alongside
bench-air and mast-lite, normalize them into the canonical observation model,
and reflect flood-relevant conditions in parcel-state — without claiming full
flood response logic, sump pump monitoring, or intervention verification.

## What v0.3 adds over v0.2

- Flood-node as a third node class
- `flood.low_point.snapshot` observation family in ingest
- Parcel-state includes flood-relevant condition estimates (where flood-node
  is installed)
- Node registry supports three node classes bound to one parcel

## Release artifacts

- `v0.3-scope-matrix.md`
- `v0.3-gap-register.md`
- `v0.3-acceptance-criteria.md`
- `v0.3-implementation-status.md`

## Related

- `../v0.2/` — v0.2 baseline (two-node kit)
- `../../hardware/flood-node/` — flood-node hardware specifications
- `../../architecture/current/milestone-roadmap.md` — milestone 3 maps to v0.3
