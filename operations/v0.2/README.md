# Operations v0.2

`v0.2` is a promotion lane marker for the first widened parcel kit.

## What v0.2 means for operations

- Field deployment playbooks for two-node kit (indoor + sheltered outdoor)
- Sheltered outdoor installation and maintenance procedures
- Two-node parcel commissioning workflow

## Key operational acceptance criteria

- **AC-5**: Mast-lite independent bring-up — a second operator follows the build
  guide and produces a functioning mast-lite node
- **AC-1**: Mast-lite packet normalization verifiable through operator runbook

## Operational gaps

| ID | Gap | Status |
|----|-----|--------|
| V02-G5 | Mast-lite bench bring-up: repeatable build independently reproduced | Partial |
| V02-G6 | Mast-lite field-hardening bundle | Defer — bench-only acceptable for v0.2 |

## Non-goals

- Field-hardened outdoor deployment operations (bench-only acceptable)
- Governance operational workflows (v0.5)
- Flood-node deployment (v0.3)

## How to use this lane

- Inherit baseline operations docs from `../v0.1/`.
- Add files here only if a `v0.2`-specific operations delta is explicitly accepted.

## Related

- `../v0.1/README.md`
- `../../release/v0.2/README.md`
- `../../release/v0.2/v0.2-acceptance-criteria.md`
