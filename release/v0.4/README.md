# Release v0.4 — Multi-Node Registry and Evidence Composition

## Purpose

Track release readiness for the v0.4 accepted runnable slice: the first
runtime with a mature node registry lifecycle and principled multi-source
evidence composition.

## Sign-off sentence

**v0.4** means: the system manages node lifecycle (register, bind, disable,
replace) across multiple node classes, composes evidence from heterogeneous
sources with appropriate weighting, and captures installation metadata that
feeds measurement trust — without claiming full trust scoring, governance
enforcement, or intervention logic.

## What v0.4 adds over v0.3

- Node registry lifecycle management (register, bind, disable, replace, retire)
- Installation metadata capture as structured input
- Evidence composition weighting across heterogeneous observation families
- Deployment-quality flags distinguishing bench-grade from field-ready

## Release artifacts

- `v0.4-scope-matrix.md`
- `v0.4-gap-register.md`
- `v0.4-acceptance-criteria.md`
- `v0.4-implementation-status.md`

## Related

- `../v0.3/` — v0.3 baseline (flood-capable)
- `../../contracts/v1.0/deployment-metadata-schema.md` — installation metadata
- `../../architecture/current/milestone-roadmap.md` — milestone 4 maps to v0.4
