# Architecture Decision Records

One ADR per significant decision. ADRs are immutable records — superseded ADRs stay in place with a status change, not a delete.

## Format

See [`0001-template.md`](0001-template.md). Minimum sections: Status, Date, Owners, Related workstreams, Context, Decision, Consequences, Alternatives considered, Follow-up work.

## When to write an ADR

Per [`../doc-discipline.md`](../doc-discipline.md) rule 1, an ADR is justified when the decision:

- **Changes how the system thinks about a concept** (e.g., ADR 0009: admissibility as schema-facts + runtime-decision rather than single-location)
- **Rejects a reasonable alternative that future readers might otherwise assume was chosen** (e.g., ADR 0008: option A over option B)
- **Sets a house rule or policy that shapes future work** (e.g., ADR 0011: doc-discipline)
- **Commits to a non-obvious architectural split** (e.g., ADR 0010: parallel adapter-trust-program rather than extending calibration-program)

If a decision is inline in prose ("decision 2026-04-19: ...") and the decision meets one of the above criteria, promote it to an ADR. Inline prose is not durable; ADRs are.

## Index by number

| ADR | Title | Date | Status |
|---|---|---|---|
| [0001](0001-bench-air-claim-boundary.md) | Bench-Air Claim Boundary | 2026-03-30 | Proposed |
| [0002](0002-private-by-default-parcel-data.md) | Private-by-Default Parcel Data | 2026-03-30 | Proposed |
| [0003](0003-no-public-parcel-hazard-map-in-mvp.md) | No Public Parcel Hazard Map in MVP | 2026-03-30 | Proposed |
| [0004](0004-condition-estimate-terminology.md) | Condition Estimate Terminology | 2026-03-30 | Proposed |
| [0005](0005-open-code-open-hardware-not-open-real-parcel-data.md) | Open Code / Open Hardware (Not Open Real Parcel Data) | 2026-03-30 | Proposed |
| [0006](0006-project-controlled-v1-dataset-public-release.md) | Project-Controlled v1 Dataset Public Release | 2026-03-30 | Proposed |
| [0007](0007-hazard-formula-v1-sensor-primary-log-odds.md) | Hazard Formula v1 — Sensor-Primary Log-Odds Form | 2026-04-19 | Accepted |
| [0008](0008-mast-lite-build-spec-as-milestone-2-gate.md) | Mast-Lite Build Spec as Milestone 2 Gate (Option A) | 2026-04-19 | Accepted |
| [0009](0009-admissibility-schema-split-facts-vs-decision.md) | Admissibility — Schema Carries Facts, Runtime Computes Decision | 2026-04-19 | Accepted |
| [0010](0010-adapter-trust-program-parallel-to-calibration.md) | Adapter-Trust Program Parallel to Calibration Program | 2026-04-19 | Accepted |
| [0011](0011-doc-discipline-extend-before-creating.md) | Doc Discipline — Extend Before Creating | 2026-04-19 | Accepted |

## Index by domain

Grouping by what the ADR decided about.

### Claims and scope

- [0001](0001-bench-air-claim-boundary.md) — what bench-air can and cannot claim
- [0003](0003-no-public-parcel-hazard-map-in-mvp.md) — no public parcel-resolution map in MVP
- [0004](0004-condition-estimate-terminology.md) — language posture (condition estimates, not directives)

### Privacy and data governance

- [0002](0002-private-by-default-parcel-data.md) — parcel data is private by default
- [0005](0005-open-code-open-hardware-not-open-real-parcel-data.md) — open stack ≠ open real parcel data
- [0006](0006-project-controlled-v1-dataset-public-release.md) — v1 dataset release posture

### Inference engine

- [0007](0007-hazard-formula-v1-sensor-primary-log-odds.md) — v1 hazard formula; sensor-primary log-odds
- [0009](0009-admissibility-schema-split-facts-vs-decision.md) — where admissibility lives (schema vs runtime)

### Hardware and deployment

- [0008](0008-mast-lite-build-spec-as-milestone-2-gate.md) — mast-lite spec as v0.2 promotion gate

### Platform programs

- [0010](0010-adapter-trust-program-parallel-to-calibration.md) — adapter-trust parallel to calibration-program

### Meta / house rules

- [0011](0011-doc-discipline-extend-before-creating.md) — doc discipline rules

## Superseded / deprecated

None yet. When an ADR is superseded, change its Status to `Superseded by ADR XXXX` (do not delete) and add a new ADR that supersedes it.
