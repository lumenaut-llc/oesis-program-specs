# Release v0.5 — Operational Governance Enforcement

## Purpose

Track release readiness for the v0.5 accepted runnable slice: the first
runtime with real consent enforcement, revocation behavior, retention cleanup,
and export controls as product behavior — not just policy documentation.

## Sign-off sentence

**v0.5** means: sharing requires verified consent, revocation reliably stops
future sharing, retention cleanup runs on schedule with named owners, and
export bundles produce auditable machine-readable output — making governance
an enforced runtime boundary rather than architectural convention.

## What v0.5 adds over v0.4

- Consent enforcement as a runtime gate on sharing paths
- Revocation that reliably stops future sharing
- Retention cleanup with operational owners and schedule
- Export bundle as a complete, auditable product surface
- Operator access logging as operational discipline
- Sharing settings as a user-facing (or operator-facing) surface

## Release artifacts

- `v0.5-scope-matrix.md`
- `v0.5-gap-register.md`
- `v0.5-acceptance-criteria.md`
- `v0.5-implementation-status.md`

## Why governance gets its own slice

The `pre-1.0-version-progression.md` places governance in v0.5 because:

1. Earlier slices (v0.2–v0.4) can operate safely under architectural
   convention (no sharing API exposed)
2. Before any external pilot with real participant data (Tier B), governance
   must be enforced — not just documented
3. Governance enforcement is a cross-cutting concern that touches consent,
   sharing, export, retention, and access logging simultaneously
4. Proving governance works is a prerequisite for v1.0

## Related

- `../v0.4/` — v0.4 baseline (registry and evidence composition)
- `../v1.0/` — v1.0 target (requires governance from v0.5)
- [`v1.0/governance-operational-model.md`](https://github.com/lumenaut-llc/oesis-contracts/blob/main/v1.0/governance-operational-model.md)
- `../../legal/privacy/permissions-matrix.md`
