# Proposed Architecture v1.0

## Purpose

Capture the target architecture shape once the project is ready to debate it in
more concrete terms.

## Status

Debate draft.

## Lane context

This file debates **program-phase `v1.0`**-style target architecture (and adjacent
future), not the frozen **`v0.1`** reference slice in `../current/`. Executable
phase and lane vocabulary: `../../program/v0.1/README.md`,
`../../program/operating-packet/00-version-labels-and-lanes.md`, `../../program/operating-packet/09-phasing-v0.1-v1.0-v1.5.md`.
Staged delivery toward this target: `../current/milestone-roadmap.md`. Long-term
product vision: `../system/vision-and-use-cases.md`.

## Initial framing

`v1.0` should answer questions such as:

- what changes materially from the `v0.1` reference stack
- which architectural boundaries remain fixed
- which new subsystem responsibilities or contracts are required
- what operational, governance, and product surfaces must become first-class

## Proposed doctrine

The target architecture should remain parcel-first without becoming
parcel-bounded.

The parcel should stay the primary:

- decision object
- ownership and permission surface
- dwelling-facing explanation surface

But the system should reason across multiple scales underneath parcel
conclusions.

The target rule is:

- parcel-first for decisions
- sensor-first for direct observation
- field-aware for hazard reasoning
- route-aware for movement and access
- provenance-first for trust

## Multi-scale architecture stance

### Parcel

The parcel remains the main decision and ownership object.

### Sensor node

The sensor node remains the direct observation object, not the parcel truth
object.

### Shared neighborhood signal

Neighborhood-scale signals become a more explicit inference object rather than a
downstream extra.

### Route and infrastructure segment

Route and infrastructure context should become first-class operational objects
for escape, access, drainage, and utility-aware reasoning.

### Hazard field

Smoke, runoff, and heat should increasingly be modeled at their natural
operational scale before being reduced into parcel consequences.

### Derived parcel state

The parcel state remains the final product-facing answer, but should more
explicitly show how parcel, neighborhood, route, and public context contributed.

## Federation and network-of-networks

Long-term federation may follow **network-of-networks** patterns rather than one
pooled mesh:

- **Owner-controlled clusters** peer with **adjacent** clusters using **derived**
  boundary signals, not unrestricted raw parcel pooling by default.
- **Overlap zones** raise confidence when independent networks agree within
  tolerance; **disagreement** remains a visible uncertainty signal.
- **Event-mode** sharing can **time-bound** broader derived exchange during smoke,
  flood, heat, or similar stress.
- **Corridor and topology** (drainage path, utility corridor, wind channel, choke
  point) matter alongside geographic distance.
- In **outages or disasters**, clusters may exchange **minimal** derived signals
  **locally**, then reconcile when backhaul returns.

Detail: `../../program/operating-packet/06-network-of-networks-concepts.md`. Internet-style **routing and
peering** framing: `../../program/operating-packet/10-outside-concepts-and-technology-pull-forward.md` §1.

## Information-layer and functional-recovery target

Target the best **evidence-to-impact** system: optimize **accuracy**, **local
recency**, **spatial relevance**, and **decision usefulness** together
(`../../program/operating-packet/07-information-layer-and-functional-recovery.md`).

- **Continuous state estimates** at parcel, segment, and shared-cell granularity:
  value, **uncertainty**, **freshness**, **evidence mix**, likely direction, not
  only feeds plus rules.
- **Functional and lifeline** reasoning: impaired functions, **dependencies**
  (transport, energy, communications, drainage, water, cooling/refuge),
  degradation trajectory, and plausible **recovery paths**, not only hazard
  labels reduced to parcels.
- **Observed conditions** vs **validated impacts** stay separable at scale.
- **Social vulnerability** informs **community** prioritization layers, not
  private parcel inference directly.

Object split (hazard / functional / response): `../../program/operating-packet/functional-state-and-response-model.md`,
`../../program/operating-packet/05-revised-architecture-blueprint.md`.

## Outside concepts (synthesis)

Patterns worth **native** debate vocabulary (full detail in `../../program/operating-packet/10-outside-concepts-and-technology-pull-forward.md`):

- **Zero trust:** every cross-parcel or cross-network use is **explicitly
  authorized** and **trust-scored** (freshness, calibration, sharing scope,
  evidence quality), governance as technical behavior, not policy-only copy.
- **Public-health style surveillance:** **sentinel** placement, **event
  definitions**, escalation detection, **intervention impact** tracking over
  time, moving beyond "sensor dashboard."
- **Federated computation:** local or cluster-local summaries; shared layers
  exchange **aggregated** updates where policy allows, **private-by-computation**
  where feasible, not only private-by-policy.
- **Bounded operational twins:** parcel, route-segment, drainage-path, or
  shared-asset twins holding state, uncertainty, dependencies, failure modes,
  interventions, and outcome history, **operational**, not full-scene novelty.
- **Observability / event architecture:** linked events across normalize -> infer
  -> confidence change -> sharing decision; **explanation graphs** and **replay**
  that strengthen provenance-first outputs.

**Caution:** outside ideas should **sharpen** design and trust, not stack into
novelty theater; adopt incrementally with phase discipline.

## Technology pull-forward (non-commitments)

Timing and rationale: `../../program/operating-packet/10-outside-concepts-and-technology-pull-forward.md`.
Nothing here changes frozen **`v0.1`** claims without `../current/implementation-posture.md`
and the implementation status matrix.

- **Pull forward early:** OpenTelemetry-style tracing along ingest -> normalize ->
  inference -> parcel view; **CloudEvents**-style envelopes for observation/state
  changes; **DuckDB + Parquet** for replay, export, and research-safe bundles.
- **Pull forward soon after:** **Home Assistant / Matter** compatibility **inventory**
  (compatibility layer, not a control commitment); **MQTT 5** as optional
  transport after HTTP paths are clean; **OGC SensorThings** at **adapter**
  edges for interoperability without capturing the internal core model.
- **Pull forward later:** PMTiles for shared/public map surfaces where policy
  allows; **federated learning** only after data-quality and governance mature;
  **decentralized mesh as primary transport** only if justified, degraded-mode
  exchange can stay narrower first.

## Non-negotiable target rules

- do not treat parcel boundaries as physical hazard boundaries
- do not make inferred parcel outputs look identical to directly observed local
  results
- keep privacy parcel-first even when inference becomes more multi-scale
- preserve confidence, evidence mode, freshness, and explanation as required
  product outputs

## Implementation implications

Relative to `v0.1`, the target architecture implies:

- richer first-class context objects beyond the parcel itself
- stronger distinction between observation objects and decision objects
- more explicit neighborhood and route-aware reasoning surfaces
- stronger product treatment of inferred-neighbor and inferred-regional support
- clearer contracts for how shared and public evidence affect parcel outputs
- **trust-scored** cross-cluster and cross-parcel signal paths aligned with
  federation and zero-trust posture
- **event lineage** and observability hooks that support explanation, replay, and
  audit without weakening privacy defaults
- **adapter-first** interoperability (MQTT, SensorThings, civic exchange) that
  does not replace the parcel-first internal model
