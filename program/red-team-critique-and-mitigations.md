# Red Team Critique and Mitigations

## Purpose

Capture the harshest good-faith critique of the product direction. Map each failure mode to the specific architectural responses that design against it. This document exists so risks are visible, not to weaken the project.

## Core red-team question

"If the words parcel-first, adaptation, neighborhood, open, and homeowner-owned were removed from the pitch, what remains that a household, operator, or city could not already approximate with existing sensors, apps, alerts, and smart-home automations?"

Strong answer: the system can combine hazard conditions, house operating state, available actions, and verified outcomes at parcel level under partial adoption, while preserving homeowner data control and explicit uncertainty.

## Failure modes

### 1. Sensor dashboard risk

The system never moves beyond sensing and interpretation. It gathers environmental data, displays it on a dashboard, and calls it resilience intelligence. Users see numbers but never receive actionable guidance or measurable outcomes.

**Design response:** The v1.5 bridge is mandatory, not aspirational. House-state, intervention, and verification contracts are defined as hard requirements before the system claims to be more than monitoring. The phase model treats observation-only as an intermediate step, not a destination.

**Evidence in specs:**

- `program/operating-packet/09-phasing-v0.1-v1.0-v1.5.md` -- v1.5 defined as measurement-to-intervention bridge
- `architecture/v1.5/house-state-and-verification-model.md` -- verification outcome structure

### 2. Parcel-first reasoning too weak

Parcel-level inference outputs are not materially better than what a user could get from public weather data, AQI feeds, and flood maps. The system adds sensors but not insight.

**Design response:** Divergence signals, contrastive explanations, metadata priors, and public-only counterfactuals are built into the parcel-state contract. The system is required to show where local conditions differ from public data, not just echo them.

**Evidence in specs:**

- [`v0.1/parcel-state-schema.md`](https://github.com/lumenaut-llc/oesis-contracts/blob/main/v0.1/parcel-state-schema.md) -- `divergence_records`, `public_only_counterfactual`, `contrastive_explanations`, `parcel_priors_applied`

### 3. Too broad

The project pursues all layers simultaneously -- hardware families, inference engine, governance framework, shared map, consent system -- and ships none of them to a usable standard.

**Design response:** Hard stage boundaries with explicit non-goals per phase. Each version lane names what does not belong in it. The operating packet scores items as "keep," "dangerous," or "change now" and defends phase boundaries aggressively.

**Evidence in specs:**

- `program/operating-packet/09-phasing-v0.1-v1.0-v1.5.md` -- "what does not belong" sections per phase
- `release/v0.1/v0.1-pilot-minimum-subset.md` -- scope fence for v0.1
- `program/operating-packet/04-architecture-review-keep-dangerous-change-now.md` -- scored review with danger ratings

### 4. No early closed loop

The system describes conditions but does not solve anything. It tells you your air quality is bad but cannot prove that a specific action improved a specific outcome at a specific parcel.

**Design response:** Smoke protection is the first mandatory proof case. The verification model requires before-state, intervention, and after-state at the same parcel, producing a verification outcome that can be evaluated.

**Evidence in specs:**

- `architecture/v1.5/house-state-and-verification-model.md` -- lines 197-209, first-closed-loop structure
- `architecture/system/node-taxonomy.md` -- first-closed-loop-priority designation

### 5. More hardware instead of right surfaces

The project expands sensor families (flood, thermal, mast, weather) while avoiding the harder bridge problem: knowing what the house itself is doing and whether interventions change outcomes.

**Design response:** Tiered acquisition model prioritizes bridge surfaces before environmental expansion. Node taxonomy separates environmental observation nodes from house-state and intervention nodes, and sequences bridge nodes ahead of additional environmental coverage.

**Evidence in specs:**

- `architecture/system/node-taxonomy.md` -- tiered acquisition model, taxonomy prioritization
- `architecture/v1.5/house-state-and-verification-model.md` -- bridge node requirements

### 6. House itself remains opaque

The system monitors environmental conditions around the parcel but cannot observe the operating state of the house -- infiltration rate, thermal dynamics, equipment cycling, power draw. Without house state, intervention verification is impossible.

**Design response:** House-state contract includes `io_ratio`, `thermal_dynamics`, `equipment_state`, and `power_state`. Hardware specs for circuit monitor and equipment-state observation provide the observation path.

**Evidence in specs:**

- [`v1.5/house-state-schema.md`](https://github.com/lumenaut-llc/oesis-contracts/blob/main/v1.5/house-state-schema.md) -- `infiltration`, `thermal_dynamics`, `equipment_state`
- [`v1.0/equipment-state-observation-schema.md`](https://github.com/lumenaut-llc/oesis-contracts/blob/main/v1.5/equipment-state-observation-schema.md) -- equipment observation contract
- `hardware/circuit-monitor/` -- hardware path for house-state observation

### 7. Governance remains philosophical

Consent, data control, and homeowner ownership are mentioned in every document but never operationalized. There is no queryable consent store, no mark-not-delete revocation, no custody tier model -- just policy language.

**Design response:** Consent-store is a versioned contract with custody tiers, query-time eligibility checks, and mark-not-delete revocation semantics. Governance is an operational model, not a statement of values.

**Evidence in specs:**

- [`v1.0/consent-store-schema.md`](https://github.com/lumenaut-llc/oesis-contracts/blob/main/v1.0/consent-store-schema.md) -- custody tiers, query-time eligibility
- [`v1.0/governance-operational-model.md`](https://github.com/lumenaut-llc/oesis-contracts/blob/main/v1.0/governance-operational-model.md) -- operational governance contract
- `legal/privacy/permissions-matrix.md` -- permission enforcement matrix

### 8. Partial adoption does not work

Under sparse adoption -- few parcels, few nodes, incomplete coverage -- the system outputs are too weak to be useful. Network value requires network density that does not exist at launch.

**Design response:** Graceful degradation via evidence modes. Each parcel output carries an evidence mode tag indicating what data contributed. Standalone parcel value is required before network-assist value. The system must be useful at a single parcel before it benefits from neighbors.

**Evidence in specs:**

- `program/operating-packet/01-core-thesis-and-framing.md` -- partial-adoption design requirement
- [`v0.1/parcel-state-schema.md`](https://github.com/lumenaut-llc/oesis-contracts/blob/main/v0.1/parcel-state-schema.md) -- evidence mode tagging
- [`v1.0/network-assist-signal-schema.md`](https://github.com/lumenaut-llc/oesis-contracts/blob/main/v1.0/network-assist-signal-schema.md) -- network-assist as additive, not required

### 9. Maintenance burden

Deployment friction kills adoption. Hardware requires calibration, firmware updates, physical maintenance, and operator intervention. The total cost of ownership exceeds the value delivered, especially for early adopters.

**Design response:** Tiered acquisition model starts with zero-friction inference (public data, no hardware) before requiring hardware deployment. Node taxonomy stages hardware by maintenance burden. Deployment maturity ladder defines readiness criteria before each expansion step.

**Evidence in specs:**

- `architecture/system/node-taxonomy.md` -- Tier 1 (inference-only), Tier 2 (low-maintenance), Tier 3 (full deployment)
- `architecture/system/deployment-maturity-ladder.md` -- readiness gates per deployment stage

### 10. Originality not legible

The user cannot see what this system does that a simpler stack -- a weather station, a smart-home hub, a public alert feed -- cannot do. The value proposition is real but invisible in the product surface.

**Design response:** Contrastive explanations surface local-versus-public divergence directly in the parcel view. Verification outcomes prove closed-loop value by showing measurable differences after interventions. The system is designed to make its own distinctiveness visible, not just claimed.

**Evidence in specs:**

- [`v0.1/parcel-state-schema.md`](https://github.com/lumenaut-llc/oesis-contracts/blob/main/v0.1/parcel-state-schema.md) -- contrastive explanation structure
- [`v1.0/verification-outcome-schema.md`](https://github.com/lumenaut-llc/oesis-contracts/blob/main/v1.5/verification-outcome-schema.md) -- verified outcome with before/after delta

## Pass/fail criteria

The project is strategically weak if most of these are true:

- It mostly gathers and displays environmental data.
- It cannot prove one strong closed loop (condition, intervention, verified outcome).
- It cannot show parcel reasoning materially differs from public data.
- It does not know the operating state of the home.
- Governance is mostly rhetorical -- consent language without operational enforcement.
- Sparse-adoption outputs are too weak to be useful at a single parcel.

The project is strategically strong if most of these are true:

- It proves one meaningful closed loop (smoke protection is the first candidate).
- It connects parcel conditions to house operating state.
- It shows verified outcome differences after interventions.
- It produces useful outputs under sparse adoption.
- It preserves homeowner data control in actual product behavior, not just policy.
- It keeps stage boundaries honest -- each phase ships what it claims and excludes what it defers.

## Red-team recommendation

The project is worth building only if it commits to proving the smallest serious version of itself: prove parcel inference is useful, add the v1.5 bridge early, prove the smoke closed loop, then expand selectively. The architecture is sound. The risk is not in the design -- it is in the temptation to ship breadth instead of depth, to add sensors instead of closing loops, and to describe governance instead of enforcing it.
