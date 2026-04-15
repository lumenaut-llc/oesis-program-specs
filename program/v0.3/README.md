# Program v0.3

`v0.3` is a promotion lane marker for the first flood-capable runtime.

## Sign-off sentence

**v0.3** means: flood-node observations normalized through canonical ingest,
flood conditions reflected in parcel-state where a flood-node is installed —
without claiming response logic, sump monitoring, or intervention surfaces.

## What v0.3 means for the program

- Program scope includes flood-capable parcels as a supported use case
- Flood observation evidence joins the parcel-state computation
- Geography-gated module pattern becomes an accepted program concept
- Three node classes composable in a single parcel (indoor + outdoor + flood)

## Scope boundaries

- **In scope**: Flood-node ingest and inference, three-node registry, flood evidence in parcel view
- **Not in scope**: Sump monitoring, flood intervention/verification, weather-PM/thermal
  families, trust scoring, governance enforcement

## Acceptance command (proposed)

```
make oesis-v03-accept
```

Runs AC-1 through AC-6 from `release/v0.3/v0.3-acceptance-criteria.md`.

## How to use this lane

- Inherit baseline program docs from `../v0.1/`.
- Add files here only if a `v0.3`-specific program delta is explicitly accepted.

## Related

- `../v0.2/README.md`
- `../../release/v0.3/README.md`
- `../../release/v0.3/v0.3-scope-matrix.md`
- `../../release/v0.3/v0.3-acceptance-criteria.md`
