# Operations

Operational playbooks for pilots, rollout execution, and field behavior.

## Lane contract

- **Baseline lane**: `v0.1/` operation docs describe the currently accepted
  operating posture.
- **Additive lanes**: add `v1.0/`, `v1.5/`, etc. under `operations/` only when
  runbooks materially diverge by version lane.
- **Compatibility policy**: if operation docs are moved into versioned lanes,
  keep redirect stubs for high-traffic old paths.
- **Canonical scope mapping**: operational labels must follow
  `../../architecture/system/version-and-promotion-matrix.md` and avoid conflating
  program phase, capability stage, and deployment maturity.

## Mutation rule

Do not silently rewrite baseline playbooks with future-lane behavior assumptions.
Create additive lane docs when operational requirements diverge materially.

## Current contents

- `../pilots/` — first-block pilot framing and operator materials.

## Related

- `../../architecture/system/phase-roadmap.md`
- `../../architecture/system/deployment-maturity-ladder.md`
- `../../release/v0.1/README.md`
