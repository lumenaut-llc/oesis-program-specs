# Program v0.4

`v0.4` is a promotion lane marker for multi-node registry and evidence composition.

## Sign-off sentence

**v0.4** means: mature node lifecycle, installation metadata, evidence
composition weighting, and deployment-quality flags — without claiming trust
scoring as a product surface, governance enforcement, or intervention logic.

## What v0.4 means for the program

- Full node lifecycle management (register, bind, disable, replace, retire)
  becomes a product surface
- Installation metadata is a first-class program input, not optional context
- Evidence composition weighting distinguishes source class and quality
- Deployment-quality flags distinguish bench-grade from field-ready nodes

## Scope boundaries

- **In scope**: Node lifecycle, installation metadata, evidence weighting,
  deployment-quality flags
- **Not in scope**: Full trust scoring (v1.0), governance enforcement (v0.5),
  house-state/intervention (v1.5), append-only history (v1.0)

## Acceptance command (proposed)

```
make oesis-v04-accept
```

Runs AC-1 through AC-6 from `release/v0.4/v0.4-acceptance-criteria.md`.

## How to use this lane

- Inherit baseline program docs from `../v0.1/`.
- Add files here only if a `v0.4`-specific program delta is explicitly accepted.

## Related

- `../v0.3/README.md`
- `../../release/v0.4/README.md`
- `../../release/v0.4/v0.4-scope-matrix.md`
- `../../release/v0.4/v0.4-acceptance-criteria.md`
