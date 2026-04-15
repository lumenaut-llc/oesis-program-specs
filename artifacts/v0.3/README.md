# Artifacts v0.3

`v0.3` is a promotion lane marker for the first flood-capable runtime.

## What v0.3 means for artifacts

- Validation artifacts include flood observation family checks
- Build evidence covers three observation families in a single parcel

## Acceptance-to-artifact mapping

| Acceptance test | Artifact class |
|----------------|---------------|
| AC-1: Flood packet normalization | Ingest validation log |
| AC-2: Three-node registry binding | Registry validation log |
| AC-3: Flood condition in parcel-state | Inference output snapshot |
| AC-4: Flood attribution in parcel view | View rendering evidence |
| AC-5: Flood-node independent bring-up | Hardware build evidence |
| AC-6: v0.2 regression | `make oesis-v02-accept` + baseline logs |

## Acceptance command (proposed)

```
make oesis-v03-accept
```

## How to use this lane

- Inherit baseline artifact definitions from `../v0.1/`.
- Add files here only if a `v0.3`-specific artifact delta is explicitly accepted.

## Related

- `../v0.2/README.md`
- `../../release/v0.3/README.md`
- `../../release/v0.3/v0.3-acceptance-criteria.md`
