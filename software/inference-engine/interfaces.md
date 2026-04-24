# Interfaces

## Public API surfaces

### Stateless inference (reference implementation)

The reference runtime uses a stateless POST pattern where the caller supplies
all inputs (normalized observation, parcel context, public context, optional
support objects) and receives a computed parcel-state in response. This avoids
requiring persistent state in the inference service.

- `POST /v1/inference/parcel-state`
  Compute a parcel-state snapshot from a normalized observation and optional
  context inputs. Accepts JSON body with normalized observation plus optional
  `parcel_context`, `public_context`, `shared_neighborhood_signal`,
  `house_state`, `house_capability`, `equipment_state_observation`,
  `source_provenance_record`, `intervention_event`, and
  `verification_outcome` fields.
- `GET /v1/inference/health`
  Report service health, active model versions, and current runtime lane.
- `GET /v1/inference/models`
  Return active hazard model versions or threshold sets, including
  public-context policy versions when applicable.

### Stateful inference (future production target)

When the system has persistent observation storage and a parcel registry, the
following RESTful endpoints should wrap the stateless inference with caching
and history:

- `GET /v1/parcels/{parcel_id}/state`
  Return the latest parcel-state snapshot for the parcel.
- `GET /v1/parcels/{parcel_id}/state/history`
  Return prior parcel-state snapshots and freshness metadata.
- `POST /v1/inference/recompute/{parcel_id}`
  Trigger an explicit recompute for one parcel.

These endpoints are not yet implemented in the reference runtime. They require
observation persistence, node registry binding, and parcel-context lookup —
all of which are v0.4+ scope.

## Internal events / jobs

- `observation.normalized`
  Triggers parcel evidence refresh for affected parcels.
- `parcel.state.updated`
  Emitted when a new parcel-state snapshot is produced.
- `parcel.state.stale`
  Emitted when freshness falls below configured expectations.
- `inference.recompute.requested`
  Used for scheduled backfills or manual reruns.

## Data contracts

Primary input contract:

- normalized observation records from [`node-observation-schema.md`](https://github.com/lumenaut-llc/oesis-contracts/blob/main/v0.1/node-observation-schema.md)
- optional parcel context records from [`parcel-context-schema.md`](https://github.com/lumenaut-llc/oesis-contracts/blob/main/v0.1/parcel-context-schema.md)
- optional shared neighborhood signal records from [`v0.1/schemas/shared-neighborhood-signal.schema.json`](https://github.com/lumenaut-llc/oesis-contracts/blob/main/v0.1/schemas/shared-neighborhood-signal.schema.json)
- optional public context records from [`public-context-schema.md`](https://github.com/lumenaut-llc/oesis-contracts/blob/main/v0.1/public-context-schema.md)

Current-truth input posture remains centered on the narrow baseline. Shared-lineage
`mast-lite` observations may feed the engine, but treating them as a promoted
second local evidence lane belongs to **program-phase `v0.2`** in
`../../architecture/system/version-and-promotion-matrix.md`.

Primary output contract:

- parcel-state snapshot defined in [`parcel-state-schema.md`](https://github.com/lumenaut-llc/oesis-contracts/blob/main/v0.1/parcel-state-schema.md)

Minimum parcel-state output fields:

- `parcel_id`
- `computed_at`
- `shelter_status`
- `reentry_status`
- `egress_status`
- `asset_risk_status`
- `confidence`
- `evidence_mode`
- `inference_basis`
- `explanation_payload`
  Includes weighted `evidence_contributions` that the engine uses to derive UI-facing drivers and limitations.
- `reasons`
- `hazards`
- `hazard_statuses`
- `parcel_priors_applied`
- `divergence_records`
- `public_only_counterfactual`
- `contrastive_explanations`
- `freshness`
- `provenance_summary`

Expected engine behavior:

- accept sparse evidence and lower confidence instead of fabricating certainty
- score hazards independently before mapping to parcel-state outputs
- treat local-vs-public divergence as a first-class signal rather than an error to smooth away
- apply parcel metadata as auditable priors before local/public evidence fusion
- represent stale or missing evidence explicitly in `freshness` and `reasons`
- preserve traceable links back to the source observations used for a decision
- preserve traceable links to public context when external evidence contributes to a decision
- preserve distinctions between local private evidence, shared neighborhood evidence, and public context
- emit a public-only foil path so the system can explain what local evidence changed
- preserve verification hooks so later scoring can compare fused predictions against public-only predictions
- avoid emitting language that implies emergency authorization or guaranteed safety
- downgrade or ignore stale public context according to a defined freshness policy
- read hazard thresholds from versioned configuration where practical
- read trust gates for stale-data suppression, low-confidence limits, and disagreement handling from versioned configuration where practical

Required parcel-first explanation posture:

- `divergence_records` should capture direction, magnitude, and persistence of local-versus-public mismatches
- `parcel_priors_applied` should enumerate which parcel fields affected baseline probabilities
- `public_only_counterfactual` should be stable enough for audit and later verification
- `contrastive_explanations` should answer "why this parcel result instead of the public-only result?"

Later **`v1.5`** bridge objects such as house-state and verification records
should influence future recommendation or response surfaces without silently
changing the current parcel-state contract.

Minimum next bridge support inputs should include:

- indoor-response observations with indoor PM2.5, temperature, and RH
- power-state observations with mains and backup-power posture
- equipment-state snapshots for HVAC mode, fan state, recirculation vs
  fresh-air state, purifier state, and related bounded-response signals
- action-log entries describing what the house or household did
- outcome / verification records describing whether measured conditions improved

Priority next closed loop:

- smoke protection should be the first serious end-to-end response proof:
  outdoor evidence, indoor-response evidence, bounded action, then measured
  verification over a defined response window.
- the first useful smoke-response window should support bounded comparisons such
  as outdoor state at trigger time, indoor PM change over roughly 30–90 minutes,
  and whether recirculation / fan / purifier actions corresponded to improvement
- until those bridge objects exist as real support inputs, inference should stay
  honest about being primarily a parcel-state engine rather than a response
  engine.

## Open questions

- Should the first inference logic be rules-based only, or allow lightweight probabilistic models from the start?

  > **Recommended direction:** Hand-tuned rules first for all three hazards. No learned models until at least 6 months of multi-parcel pilot data exists. Rules are auditable and explainable; models can be layered later.

- How should parcel context be represented when exact building features are unknown?

  > **Recommended direction:** Treat missing features as unknown, not as defaults. Use conservative fallbacks (e.g., assume no basement if unknown) and disclose the assumption in reasons. Do not impute features.

- What minimum evidence should be required before any non-`unknown` status is allowed?

  > **Recommended direction:** At least 1 local node with health OK and freshness < 15 minutes. Public context alone moves evidence_mode to public_only but should not produce non-unknown status without local confirmation.

- Should public context be treated as supporting evidence only unless local nodes confirm it?

  > **Recommended direction:** NWS weather alerts and AirNow PM2.5 are strong enough for local_plus_public when paired with local evidence. Generic forecast APIs are supporting context only, not strong enough to shift evidence mode. Public context alone should not produce non-unknown status.
