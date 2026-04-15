# Artifacts v0.2

`v0.2` is a promotion lane marker for the first widened parcel kit.

## What v0.2 means for artifacts

- Validation artifacts cover widened two-node kit (bench-air + mast-lite)
- Build evidence includes multi-source ingest and inference checks

## Acceptance-to-artifact mapping

| Acceptance test | Artifact class |
|----------------|---------------|
| AC-1: Mast-lite packet normalization | Ingest validation log |
| AC-2: Two-node registry binding | Registry validation log |
| AC-3: Two-source inference | Inference output snapshot |
| AC-4: Source-mix parcel view | View rendering evidence |
| AC-5: Mast-lite independent bring-up | Hardware build evidence |
| AC-6: v0.1 regression | `make oesis-validate` / `make oesis-check` logs |

## Acceptance command (proposed)

```
make oesis-v02-accept
```

## How to use this lane

- Inherit baseline artifact definitions from `../v0.1/`.
- Add files here only if a `v0.2`-specific artifact delta is explicitly accepted.

## Related

- `../v0.1/README.md`
- `../../release/v0.2/README.md`
- `../../release/v0.2/v0.2-acceptance-criteria.md`
