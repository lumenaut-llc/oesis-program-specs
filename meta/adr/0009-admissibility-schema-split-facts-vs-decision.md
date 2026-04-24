# ADR 0009: Admissibility — Schema Carries Facts, Runtime Computes Decision

- Status: Accepted
- Date: 2026-04-19
- Owners: Open Environmental Sensing and Inference System (technical, cross-repo)
- Related workstreams:
  - architecture/system/calibration-program (§C)
  - architecture/system/adapter-trust-program (§C)
  - oesis-contracts (observation schema — planned extensions)
  - oesis-runtime (ingest — admissibility wiring, planned)
  - release/v.0.1 (gap-register G15, G17)

## Context

The calibration program's admissibility rule (calibration-program §C; parallel adapter-trust-program §C) requires 8 runtime checks per normalized observation. Where should those checks live across the cross-repo boundary?

Three options:

- **A1.** Pure runtime. Admissibility decision computed in ingest; schema never represents it. Different consumers may compute differently; audit trail weakens.
- **A2.** Schema carries the decision. Canonical observation contains `admissible: bool` + reason codes. Uniform across consumers, but locks one view and churns the schema when policy evolves.
- **A3.** Hybrid. Schema carries the **facts** (burn-in state, reference-cal session pointer, deployment class, etc.); runtime computes the **decision** on normalized observations.

This affects `oesis-contracts` (canonical observation schema), `oesis-runtime` (ingest and inference), and every consumer that reads normalized observations.

## Decision

**Adopt A3: schema carries facts, runtime computes decision.**

Schema extensions (planned in `oesis-contracts` v1.0 lane; tracked as G17):

Physical-sensor facts per [`../../architecture/system/calibration-program.md`](../../architecture/system/calibration-program.md) §C:

- `burn_in_complete: bool`
- `node_calibration_session_ref: string`
- `node_deployment_maturity: enum` (`v0.1` | `v1.0` | `v1.5` | `v2.0`)
- `node_deployment_class: enum` (`indoor` | `sheltered` | `outdoor`)
- `protective_fixture_verified_at: timestamp | null`
- `placement_representativeness_class: enum | null` (A / B / C / D)

Adapter-derived facts per [`../../architecture/system/adapter-trust-program.md`](../../architecture/system/adapter-trust-program.md) §C:

- `adapter_source_ref: string`
- `adapter_contract_version: string`
- `adapter_onboarding_ref: string`
- `adapter_credential_last_verified_at: timestamp`
- `adapter_tier: enum` (`tier_1_passive` | `tier_2_adapter` | `tier_3_direct`)

Runtime outputs on normalized observations (never back-propagated to schema):

- `admissible_to_calibration_dataset: bool`
- `admissibility_reasons: [string]` (reason codes: `burn_in_incomplete`, `reference_calibration_stale`, `fixture_unverified`, `contract_version_drift`, `credentials_expired`, etc.)

Runtime branches on `adapter_tier`: absent or `tier_3_direct` → calibration-program §C rules; `tier_1_passive` or `tier_2_adapter` → adapter-trust-program §C rules.

## Consequences

Positive:

- **Schema stays stable** as admissibility policy evolves. Policy lives in code, not in contract.
- **Every consumer sees the same facts** — no consumer re-probes the node registry or reference-calibration log.
- **Audit trail preserved** on normalized records. Coefficient-fitting filters on the boolean; audit tooling reads reasons.
- **Historical records remain interpretable** under old rules and re-evaluable under new rules.
- Works across the two-programs architecture (calibration + adapter-trust) via the `adapter_tier` branch.

Negative:

- Observation schema grows by ~11 fields. For a schema already tracking node identity, timing, and sensor values, this is non-trivial size increase.
- Cross-repo schema change required in `oesis-contracts` before `oesis-runtime` can produce or consume the decision fields. Coordination overhead.
- Runtime consumers that cached observation structure need to accept the schema additions (additive, but still a contract change).

## Alternatives considered

**A1: pure runtime.** Rejected because different consumers (coefficient fitting, inference, audit tooling) would each recompute admissibility from primary sources, risking inconsistent decisions. The decision needs to live once.

**A2: schema carries the decision.** Rejected because any change to the 8-point check (adding a 9th, changing a threshold) would require schema migration. Historical records encoded under old rules become ambiguous. Policy is expected to evolve; schema should not.

## Follow-up work

- Cross-repo schema change in `oesis-contracts` v1.0 lane: extend observation schema with the 11 fact fields above. Tracked as G17.
- Runtime implementation in `oesis-runtime` ingest: read facts, apply §C check per tier, emit decision. Tracked as G15.
- Update `architecture/system/calibration-program.md` §C "Schema vs runtime split" subsection (already done 2026-04-19).
- Coordinate schema migration with existing consumers; all changes are additive so forward-compat is preserved.
