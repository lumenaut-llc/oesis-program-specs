# First Block Pilot

## Goal

Validate parcel-level usefulness under partial adoption.

## Assumptions

- 1 block or small hillside pocket
- partial node participation
- simulated non-participating parcels allowed

## Core metrics

- false positives / false negatives
- confidence quality
- node uptime
- installation effort
- parcel operator comprehension / trust

## Governance minimums for this pilot

- private-only mode should be the default enrollment posture
- any neighborhood or research sharing should require a separate explicit choice
- no public parcel-by-parcel map should be created from pilot data
- pilot notices should explain that outputs are condition estimates, not emergency instructions
- publication of pilot results should avoid exact parcel-linked contributed data

## Before launch

- complete a pilot-specific notice and consent flow
- document operator access expectations
- document what data may be published, aggregated, or exported
- define who handles complaints, revocation requests, and incident escalation

## Calibration-program compliance (gap register G19)

Per [`../../architecture/system/calibration-program.md`](../../architecture/system/calibration-program.md) §G and [`../../architecture/current/pre-1.0-version-progression.md`](../../architecture/current/pre-1.0-version-progression.md) promotion-bar item 5, **external pilots require every deployed node family to meet `deployment maturity v1.0` calibration posture**. This is a hard gate per G19 in [`../../release/v.0.1/v0.1-gap-register.md`](../../release/v.0.1/v0.1-gap-register.md); unmet means no external pilot.

Concrete checks per deployed unit before pilot enrollment:

- Node's build spec at `oesis-builds/specs/<node>/v0-X.md` carries a §F metadata block per calibration-program §F (or adapter-trust-program §F for Tier 2/3 adapters).
- At least one characterized reference instrument is populated per measurand per deployment class under `oesis-builds/procedures/<node>/references/`. Placeholder `references/TBD.md` is not acceptable for external pilot (G13).
- BME680-bearing nodes have completed the 48 h burn-in window; `burn_in_complete: true` either by ingest flag (when G14/G15 ship) or by build-log attestation before the flag is wired.
- For outdoor-class nodes (flood-node, weather-pm-mast), protective-fixture acceptance tests (radiation shield, zero-reference/geometry) have passed per calibration-program §C item 7; pre-verification readings are excluded from pilot data.
- For adapters (circuit-monitor Tier 3 direct, or future Tier 2 cloud adapters), source-authority onboarding per [`../../architecture/system/adapter-trust-program.md`](../../architecture/system/adapter-trust-program.md) §B completed for each participating parcel.

If any condition is not met, the pilot must either wait, exclude the affected node family, or document an explicit stop-ship-override decision approved by the governance owner. Internal reference runs (Tier A per [`../../release/v.0.1/v0.1-pilot-minimum-subset.md`](../../release/v.0.1/v0.1-pilot-minimum-subset.md)) have a weaker bar — calibration-posture attestation is recommended but not gating for Tier A.
