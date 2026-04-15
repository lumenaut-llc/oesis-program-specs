# Artifacts v0.5

`v0.5` is a promotion lane marker for operational governance enforcement.

## What v0.5 means for artifacts

- Validation artifacts cover governance enforcement paths
- Build evidence includes consent, revocation, retention, and export checks

## Acceptance-to-artifact mapping

| Acceptance test | Artifact class |
|----------------|---------------|
| AC-1: Consent gates sharing | Consent enforcement log |
| AC-2: Missing consent blocks sharing | Consent enforcement log |
| AC-3: Revocation stops future sharing | Revocation verification log |
| AC-4: Retention cleanup executes | Retention cleanup report |
| AC-5: Export bundle validates | Export bundle validation log |
| AC-6: Operator access logging complete | Access log audit evidence |
| AC-7: Sharing settings configurable | Settings configuration log |
| AC-8: Custody tier enforcement | Custody tier verification log |
| AC-9: End-to-end governance lifecycle | Full lifecycle trace |
| AC-10: v0.4 regression | `make oesis-v04-accept` + baseline logs |

## Acceptance command (proposed)

```
make oesis-v05-accept
```

## How to use this lane

- Inherit baseline artifact definitions from `../v0.1/`.
- Add files here only if a `v0.5`-specific artifact delta is explicitly accepted.

## Related

- `../v0.4/README.md`
- `../../release/v0.5/README.md`
- `../../release/v0.5/v0.5-acceptance-criteria.md`
