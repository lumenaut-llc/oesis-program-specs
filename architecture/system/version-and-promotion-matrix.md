# Version and Promotion Matrix

## Purpose

Hold a single **non-ambiguous** map between:

- **Public / accepted runnable slices** (`v0.1`, next `v0.2`, …)
- **Capability stages** (`current v1`, `v1.5`, `v2`, `v2.5`, `v3`, `v4`)
- **Deployment maturity** (per node family: `deployment maturity v0.1` … `v2.0`)
- **Implementation status** (`implemented`, `partial`, `docs-only`, `planned`)

Use this document when writing roadmaps, kit language, or marketing so **taxonomy** and **implementation truth** do not collapse into one version number.

## The four axes

| Axis | Question it answers | Examples |
| --- | --- | --- |
| **Accepted runnable slice** | What end-to-end story is **promoted** as the current honest baseline? | `v0.1` today; `v0.2` when bench-air + mast-lite + contracts/runtime meet the promotion bar |
| **Capability stage** | What **class of product behavior** is in scope for architecture and contracts? | `current v1` sensing/inference; `v1.5` intervention bridge objects |
| **Deployment maturity** | Is this **node family** bench-grade or field-hardened? | Per family in `deployment-maturity-ladder.md`; calibration posture required at each tier is in `calibration-program.md` |
| **Implementation status** | For each surface, what is actually shipped vs drafted? | Runtime observation table in `integrated-parcel-system-spec.md` |

**Folder note:** `architecture/current/` is the frozen **architecture lane** aligned with program-phase `v0.1`. That is **not** the same label as capability stage `current v1` (see `architecture-gaps-by-stage.md`).

## Product anchor: current truth, next promotion, later staged additions

| | **Current truth** | **Next promotion** | **Later staged additions** |
| --- | --- | --- | --- |
| **Product bar** | One parcel, one bench-air lineage, ingest → inference → parcel view. Frozen working reference slice (`v0.1`). | **Program-phase `v0.2`:** real indoor + sheltered-outdoor parcel kit (`bench-air-node` + `mast-lite`) with explicit architecture scope, contract/runtime boundary updates, acceptance checks, and implementation-status evidence (`../current/pre-1.0-version-progression.md`). Do **not** treat mast-lite as fully proven until that promotion bar is met. | Capability `v1.5` through `v4`: intervention bridge, bounded guidance, controls compatibility, adaptation memory, route/block resilience (`phase-roadmap.md`). |
| **Core purpose** | Prove parcel-first sensing and inference under partial adoption. | Prove the first coherent **field-credible** two-node parcel kit with stronger parcel binding and ops evidence. | Evolve toward bounded adaptation: connect hazard, house state, action, and verified outcome without overclaiming automation. |
| **Hardware in scope** | Bench-air as the proven reference lineage. | Mast-lite as coordinated kit member; optional flood only where parcel-relevant. | `v1.5` bridge families (indoor-response, power-outage, adapters); geography modules (`flood-node`, `weather-pm-mast`, `freeze-node`); `thermal-pod` remains research-gated (`node-taxonomy.md`). |
| **Software / data in scope** | Ingest, normalization, parcel inference, parcel view, confidence, evidence mode, provenance, private/shared/public distinction. | Stronger ingest authorization, parcel binding, field-hardening alignment, clearer evidence summaries in the parcel view. | `v1.5` support objects; `v2` guidance layer; `v2.5` compatibility inventory and bounded controls; `v3` adaptation memory; `v4` route/community layers. |
| **House-state / intervention** | Not part of the current proven reference slice beyond parcel-context optional fields in drafts. | Design and document bridge surfaces; do not describe them as fully implemented in runtime unless status says so. | `v1.5`: indoor response, outage, equipment-state signals, building/site metadata, action log, outcome verification (`architecture-gaps-by-stage.md`). |
| **Controls compatibility** | Not an executed product guarantee in the narrow slice. | Draft or partial docs may exist; keep language honest. | **Primary home for full compatibility inventory and bounded-control execution: `v2.5`**, not `v1.5`. |
| **Governance** | Private-by-default and provenance discipline are part of product framing; several flows remain **partial** or **docs-only**. | Same honesty constraint while kit scope widens. | Stronger export/retention execution, verified revocation, and operational governance UX land in later promotions (see `../current/pre-1.0-version-progression.md` for example `v0.5` governance slice). |

## Pre-1.0 progression (accepted slice ladder)

Canonical detail: `../current/pre-1.0-version-progression.md`.

| Slice | Intent |
| --- | --- |
| `v0.1` | One parcel, one bench-air path, ingest → parcel view |
| `v0.2` | First widened kit: stable indoor + sheltered outdoor |
| `v0.3` | First flood-capable runtime slice with dedicated flood observation family |
| `v0.4` | Stronger multi-node registry and evidence composition |
| `v0.5` | Operational sharing/governance slice with real revocation, retention, export evidence |
| `v1.0` (program sense) | Materially broader system than the first narrow slice — distinct from website marketing labels |

New `v0.x` slices should **only** ship when the runnable system boundary **materially** expands, not when a single schema draft appears.

## Capability stages (summary)

| Stage | Role |
| --- | --- |
| `current v1` | Parcel sensing and inference baseline |
| `v1.5` | Minimum bridge: house-state and intervention **support objects**, equipment-state **read-side** evidence, action/outcome logs, trust/device-operation objects |
| `v2` | Bounded adaptation **guidance** (policy separate from hazard) |
| `v2.5` | **Compatibility inventory**, bounded controls, control verification |
| `v3` | Adaptation memory / learning |
| `v4` | Parcel + route + block resilience |

## Governance honesty

Revocation, sharing/consent execution, and some governance paths may remain **docs-only** or **partial** while the reference slice is narrow. Product copy and architecture claims should say **implemented** only when the runtime and acceptance evidence match.

## Related docs

- `../current/pre-1.0-version-progression.md`
- `node-taxonomy.md`
- `architecture-gaps-by-stage.md`
- `architectural-choices-by-stage.md`
- `deployment-maturity-ladder.md`
- `calibration-program.md`
- `adapter-trust-program.md`
- `sensor-placement-and-representativeness-guide.md`
- `integrated-parcel-system-spec.md`
- `phase-roadmap.md`
- [`v0.1/README.md`](https://github.com/lumenaut-llc/oesis-contracts/blob/main/v0.1/README.md)
