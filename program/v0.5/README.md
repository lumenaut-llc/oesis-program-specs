# Program v0.5

`v0.5` is a promotion lane marker for operational governance enforcement.

## Sign-off sentence

**v0.5** means: governance enforced as runtime behavior — consent gates sharing,
revocation stops it, retention has owners, export produces auditable output —
making governance an enforced runtime boundary rather than architectural convention.

## What v0.5 means for the program

- Governance becomes an enforced product behavior, not just policy documentation
- Consent, revocation, retention, and export are operational requirements
- Program readiness for real participant data (Tier B) requires this slice
- All v0.4 pipeline and registry surfaces carry forward

## Why governance gets its own slice

Per `pre-1.0-version-progression.md`:

1. Earlier slices (v0.2–v0.4) operate safely under architectural convention
   (no sharing API exposed)
2. Before any external pilot with real participant data (Tier B), governance
   must be enforced — not just documented
3. Governance enforcement is cross-cutting: consent, sharing, export, retention,
   and access logging simultaneously
4. Proving governance works is a prerequisite for v1.0

## Scope boundaries

- **In scope**: Consent enforcement, revocation, retention cleanup, export bundle,
  operator access logging, sharing settings, custody tiers
- **Not in scope**: Full consumer governance UX, trust scoring (v1.0),
  shared-map governance (v1.0), house-state governance (v1.5)

## Acceptance command (proposed)

```
make oesis-v05-accept
```

Runs AC-1 through AC-10 from `release/v0.5/v0.5-acceptance-criteria.md`.

## How to use this lane

- Inherit baseline program docs from `../v0.1/`.
- Add files here only if a `v0.5`-specific program delta is explicitly accepted.

## Related

- `../v0.4/README.md`
- `../../release/v0.5/README.md`
- `../../release/v0.5/v0.5-scope-matrix.md`
- `../../release/v0.5/v0.5-acceptance-criteria.md`
- `../../contracts/v1.0/governance-operational-model.md`
