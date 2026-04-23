# Node part sheets

## Purpose

One-page-per-node aggregator pages. Each part sheet pulls together what lives in canonical docs scattered across the repo: architecture posture (from `node-taxonomy.md` and `integrated-parcel-system-spec.md`), deployment-class defaults (from `deployment-maturity-ladder.md`), calibration posture (from `calibration-program.md`), adapter-trust posture where applicable (from `adapter-trust-program.md`), cross-repo references (design in oesis-hardware, build in oesis-builds, runtime in oesis-runtime), gap-register entries, and per-phase role evolution.

## What these pages are — and what they aren't

Part sheets **aggregate via links**. They cite canonical sources; they do not restate cell values. Per [`../../../meta/doc-discipline.md`](../../../meta/doc-discipline.md) Rule 2, if a part sheet and its cited source disagree, the source wins — fix the sheet.

Part sheets are **not**:

- Build guides (those live in [oesis-hardware](https://github.com/lumenaut-llc/oesis-hardware))
- Build specs (those live in [oesis-builds/specs/](https://github.com/lumenaut-llc/oesis-builds/tree/main/specs))
- Runtime normalizers (those live in [oesis-runtime](https://github.com/lumenaut-llc/oesis-runtime))
- The taxonomy itself ([`../node-taxonomy.md`](../node-taxonomy.md))

They are the answer to "give me one page that tells me the architectural story of `<node>` across all repos and version stages."

## Pages in this directory

| Node family | Type | Deployment class | Maturity | Stage of introduction |
|---|---|---|---|---|
| [`bench-air-node.md`](bench-air-node.md) | Physical sensor | indoor | `v0.1` → targeting `v1.0` | v0.1 (current truth) |
| [`mast-lite.md`](mast-lite.md) | Physical sensor | sheltered | targeting `v1.0` | v0.2 (next promotion; G12 blocker) |
| [`flood-node.md`](flood-node.md) | Physical sensor | outdoor | targeting `v1.0` | v0.3 |
| [`weather-pm-mast.md`](weather-pm-mast.md) | Physical sensor | outdoor | targeting `v1.5` | v1.0 (second wave) |
| [`thermal-pod.md`](thermal-pod.md) | Physical sensor | outdoor (research-gated) | intentionally < `v1.0` | research lane |
| [`circuit-monitor.md`](circuit-monitor.md) | Tier 3 adapter | mains-adjacent | targeting `v1.5` | capability-stage `v1.5` |

## When to update a part sheet

Update when:

- A new build version of the node lands (add a row to the page's version-evolution table, link the new spec).
- A deployment-class or maturity change is proposed (cite the decision; do not change the values without updating upstream).
- A new gap-register entry involves the node (add to cross-repo link map).
- A per-phase role changes (amend the phase table).

Do **not** update to restate values that live in `deployment-maturity-ladder.md`, `calibration-program.md`, or other canonical sources. Those updates happen upstream; the part sheet inherits them via citation.

## Template

New part sheets follow the same shape:

1. One-line summary
2. Deployment posture (citing ladder + role-map row)
3. Version evolution table
4. Calibration posture (citing calibration-program or adapter-trust-program)
5. Role in each program-phase
6. Cross-repo link map
7. Known gotchas
8. Related docs

When adding a new part sheet, start from the bench-air-node sheet or mast-lite sheet (most complete) and adapt.

## Related

- [`../node-taxonomy.md`](../node-taxonomy.md) — canonical taxonomy and posture tags
- [`../integrated-parcel-system-spec.md`](../integrated-parcel-system-spec.md) "Deployment posture per node" table — source of per-node posture values
- [`../deployment-maturity-ladder.md`](../deployment-maturity-ladder.md) — class / power / IP / transport defaults
- [`../calibration-program.md`](../calibration-program.md) — physical-sensor calibration policy
- [`../adapter-trust-program.md`](../adapter-trust-program.md) — adapter-derived trust policy
- [`../architectural-choices-by-stage.md`](../architectural-choices-by-stage.md) — master cross-phase summary
- [`../../../release/v.0.1/v0.1-gap-register.md`](../../../release/v.0.1/v0.1-gap-register.md) — G1–G24 gap tracking
