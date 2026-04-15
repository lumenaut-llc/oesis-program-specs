# Legal v0.5

`v0.5` is a promotion lane marker for operational governance enforcement.

## What v0.5 means for legal

- Consent and sharing enforcement becomes operational — legal posture must
  support query-time consent checks and mark-not-delete revocation semantics
- Retention compliance requires defined schedules and named owners
- Export audit requirements formalized — export bundles must be complete and
  machine-readable
- Revocation behavior must meet legal expectations for data handling
- Custody tier enforcement (internal_only vs operator_visible) must be
  legally defensible

## Legal review items

- Consent record schema and lifecycle compliance
  (see `../../contracts/v1.0/governance-operational-model.md`)
- Mark-not-delete revocation semantics: legal adequacy for data subject requests
- Retention schedule: legal minimum/maximum retention periods
- Export bundle: completeness requirements for data subject access requests
- Custody tier: legal basis for differential access levels
- Operator access logging: adequacy for accountability requirements

## Key acceptance criteria with legal implications

- **AC-1/AC-2**: Consent gates sharing; missing consent blocks it
- **AC-3**: Revocation stops future sharing (mark-not-delete)
- **AC-4**: Retention cleanup executes with auditable report
- **AC-5**: Export bundle validates and includes all parcel-linked data classes
- **AC-8**: Custody tier enforcement at query time

## How to use this lane

- Inherit baseline legal docs from `../v0.1/`.
- Add files here only if a `v0.5`-specific legal delta is explicitly accepted.

## Related

- `../v0.4/README.md`
- `../../release/v0.5/README.md`
- `../../release/v0.5/v0.5-scope-matrix.md` (governance scope section)
- `../../release/v0.5/v0.5-acceptance-criteria.md`
- `../../contracts/v1.0/governance-operational-model.md`
- `../../legal/privacy/data-ownership.md`
