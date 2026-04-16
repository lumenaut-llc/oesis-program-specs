# Operations v0.4

`v0.4` is a promotion lane marker for multi-node registry and evidence composition.

## What v0.4 means for operations

- Node lifecycle operations (register, bind, disable, replace, retire)
- Installation metadata capture workflows (mount type, height, orientation,
  exposure, power source)
- Deployment maturity verification procedures (bench-grade vs field-ready)

## Key operational acceptance criteria

- **AC-1**: Node lifecycle exercised — register, bind, disable, replace, retire
  for a multi-node parcel; retired nodes excluded from inference
- **AC-2**: Installation metadata — operator submits structured deployment metadata
  linked to node installation records
- **AC-4**: Deployment-quality flags visible to operator in parcel view

## Operational gaps

| ID | Gap | Status |
|----|-----|--------|
| V04-G1 | Node registry lifecycle: full end-to-end flow | Partial — schema and v0.4 acceptance test exist (`make oesis-v04-accept` exercises register, bind, disable, replace, retire); full operator-facing flow not yet built |
| V04-G2 | Installation metadata capture surface (CLI, form, or API) | Docs-only — no capture path |

## Non-goals

- Full trust scoring operations (v1.0)
- Governance enforcement operations (v0.5)

## How to use this lane

- Inherit baseline operations docs from `../v0.1/`.
- Add files here only if a `v0.4`-specific operations delta is explicitly accepted.

## Related

- `../v0.3/README.md`
- `../../release/v0.4/README.md`
- `../../release/v0.4/v0.4-acceptance-criteria.md`
