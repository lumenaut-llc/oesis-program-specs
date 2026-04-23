# Operations v0.3

`v0.3` is a promotion lane marker for the first flood-capable runtime.

## What v0.3 means for operations

- Flood-node deployment and site selection playbooks
- Flood-node calibration (dry reference, depth derivation) procedures
- Three-node parcel commissioning workflow

## Key operational acceptance criteria

- **AC-5**: Flood-node independent bring-up — second operator follows build guide,
  produces functioning node with distance sensor readings and derived water depth
- **AC-1**: Flood packet normalization verifiable through operator runbook

## Operational gaps

| ID | Gap | Status |
|----|-----|--------|
| V03-G5 | Flood-node independent build reproduction | Partial — build guide exists; not independently confirmed |
| V03-G6 | Flood-node calibration validation | Provisional — documented but not field-validated |
| V03-G7 | Flood-node field deployment context | Defer — not required for bench testing |

## Non-goals

- Sump pump or equipment-state operational procedures (v1.5)
- Governance operational workflows (v0.5)

## How to use this lane

- Inherit baseline operations docs from `../v0.1/`.
- Add files here only if a `v0.3`-specific operations delta is explicitly accepted.

## Related

- `../v0.2/README.md`
- `../../release/v0.3/README.md`
- `../../release/v0.3/v0.3-acceptance-criteria.md`
- [`flood-node/README.md`](https://github.com/lumenaut-llc/oesis-hardware/blob/main/v0.1/flood-node/README.md)
