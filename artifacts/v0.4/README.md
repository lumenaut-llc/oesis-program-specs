# Artifacts v0.4

`v0.4` is a promotion lane marker for multi-node registry and evidence composition.

## What v0.4 means for artifacts

- Validation artifacts cover registry lifecycle and evidence composition
- Build evidence includes deployment maturity verification checks

## Acceptance-to-artifact mapping

| Acceptance test | Artifact class |
|----------------|---------------|
| AC-1: Node lifecycle (register/bind/disable/replace/retire) | Registry lifecycle log |
| AC-2: Installation metadata capture | Deployment-metadata validation log |
| AC-3: Evidence composition with quality weighting | Inference weighting snapshot |
| AC-4: Deployment-quality flags visible | View rendering evidence |
| AC-5: Node replacement continuity | Inference continuity log |
| AC-6: v0.3 regression | `make oesis-v03-accept` + baseline logs |

## Acceptance command (proposed)

```
make oesis-v04-accept
```

## How to use this lane

- Inherit baseline artifact definitions from `../v0.1/`.
- Add files here only if a `v0.4`-specific artifact delta is explicitly accepted.

## Related

- `../v0.3/README.md`
- `../../release/v0.4/README.md`
- `../../release/v0.4/v0.4-acceptance-criteria.md`
