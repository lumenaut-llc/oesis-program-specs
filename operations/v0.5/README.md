# Operations v0.5

`v0.5` is a promotion lane marker for operational governance enforcement.

## What v0.5 means for operations

- Consent management operational workflows
- Revocation execution and verification procedures
- Retention cleanup schedules with named operational owners
- Export and audit procedures for governance compliance
- Operator access logging covering all parcel-linked admin actions

## Key operational acceptance criteria

- **AC-4**: Retention cleanup executes on schedule, produces auditable report
- **AC-6**: Operator access logging covers view, settings update, rights request,
  retention cleanup — all with timestamps and operator identity
- **AC-7**: Sharing settings configurable by operator
- **AC-9**: End-to-end lifecycle: configure → consent → share → revoke → export → cleanup

## Operational gaps

| ID | Gap | Status |
|----|-----|--------|
| V05-G3 | Retention cleanup: schedule with named owners | **Blocker** — utility exists; no schedule or owner assigned |
| V05-G5 | Operator access logging: coverage not proven | Partial — reference logging exists in `serve_parcel_api.py`; proving completeness is ongoing (SO-2 gate closed, broader audit pending) |
| V05-G6 | Sharing settings surface for operator | Partial — API-level sharing settings implemented and tested in v0.5 acceptance; product UI not yet built (PU-7) |
| V05-G8 | Rights request processing: operator-mediated flow | Partial — admin utility exists; `process_rights_requests` and export bundle work at API level |

## Non-goals

- Full consumer governance UX with rich settings panels
- Automated retention enforcement (manual-with-tooling acceptable)

## How to use this lane

- Inherit baseline operations docs from `../v0.1/`.
- Add files here only if a `v0.5`-specific operations delta is explicitly accepted.

## Related

- `../v0.4/README.md`
- `../../release/v0.5/README.md`
- `../../release/v0.5/v0.5-acceptance-criteria.md`
- `../../release/v0.5/v0.5-gap-register.md`
- [`v1.0/governance-operational-model.md`](https://github.com/lumenaut-llc/oesis-contracts/blob/main/v1.0/governance-operational-model.md)
