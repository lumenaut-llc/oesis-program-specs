# Software v0.5

`v0.5` is a promotion lane marker for operational governance enforcement.

## Sign-off sentence

**v0.5** means: governance enforced as runtime behavior — consent gates sharing,
revocation stops it, retention has owners, export produces auditable output —
without claiming full consumer governance UX, intervention logic, or trust scoring.

## Software scope

| Surface | Status | Acceptance test |
|---------|--------|----------------|
| Consent enforcement (runtime gate) | Docs-only | AC-1, AC-2 |
| Revocation behavior (stops sharing) | Docs-only | AC-3 |
| Retention cleanup (operational) | Partial | AC-4 |
| Export bundle (validated output) | Partial | AC-5 |
| Operator access logging | Partial | AC-6 |
| Sharing settings (operator surface) | Docs-only | AC-7 |
| Custody tier enforcement | Docs-only | AC-8 |
| End-to-end governance lifecycle | Planned | AC-9 |
| All v0.4 software surfaces | v0.4 target | AC-10 (regression) |

## Blockers (from gap register)

| ID | Gap | Status |
|----|-----|--------|
| V05-G1 | Consent enforcement: query-time check before sharing | Docs-only |
| V05-G2 | Revocation: revoked_at stops future sharing | Docs-only |
| V05-G3 | Retention cleanup: schedule with named owners | Partial — utility exists; no schedule/owner |
| V05-G4 | Export bundle: complete schema-validated output | Partial |
| V05-G5 | Operator access logging: all admin actions tracked | Partial — coverage not proven |
| V05-G6 | Sharing settings: operator-configurable surface | Docs-only |
| V05-G7 | Consent store: append-only lifecycle store | Docs-only |
| V05-G8 | Rights request: user-facing or operator-mediated | Partial — admin utility only |
| V05-G9 | Custody tier: query-time eligibility checks | Docs-only |
| V05-G10 | End-to-end acceptance test | Planned |

## Key acceptance criteria

- **AC-1/AC-2**: Consent gates sharing; missing consent blocks it
- **AC-3**: Revocation stops future sharing (mark-not-delete)
- **AC-4**: Retention cleanup executes and produces auditable report
- **AC-5**: Export bundle validates against `export-bundle.schema.json`
- **AC-7**: Sharing settings configurable by operator
- **AC-9**: End-to-end lifecycle: configure → consent → share → revoke → export → cleanup

## Contract boundary changes (v0.4 → v0.5)

- Consent-store and sharing-store become operational runtime surfaces
- Sharing queries enforce consent, revocation, and custody tier at query time
- Retention cleanup produces auditable reports
- Operator access log covers all parcel-linked admin actions

## Non-goals

- Full consumer governance UX with rich settings panels
- Trust scoring as composed product surface (v1.0)
- House-state or intervention governance (v1.5)
- Automated retention enforcement (manual-with-tooling acceptable)

## How to use this lane

- Inherit baseline software docs from `../v0.1/`.
- Add files here only if a `v0.5`-specific software delta is explicitly accepted.

## Related

- `../v0.4/README.md`
- `../../release/v0.5/README.md`
- `../../release/v0.5/v0.5-implementation-status.md`
- [`v1.0/governance-operational-model.md`](https://github.com/lumenaut-llc/oesis-contracts/blob/main/v1.0/governance-operational-model.md)
