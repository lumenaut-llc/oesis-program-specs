# System Overview

## Lane

This directory is the `system/` lane.

Use it for cross-version narrative, operating-model, roadmap, and doctrine
framing that should not be mistaken for frozen current truth or a debated
target-lane spec.

If you need frozen current-truth architecture, use `../current/`.
If you need debated target-lane architecture, use `../v1.0/`.
If you need narrow bridge-stage architecture notes, use `../v1.5/`.

## Purpose

Program-level system narrative and top-level operating model.

## Minimum contents

- vision and use-case framing
- layered system model
- core product principles
- canonical operating assumptions
- links to adjacent architecture and governance docs

## Current status

- `../../architecture/README.md` is the sibling versioned technical architecture canon.
- `../../architecture/current/README.md` is the current truthful reference-architecture slice.
- `../../architecture/v1.0/README.md` is the explicit versioned debated target-architecture slice.
- `../../architecture/v1.5/README.md` is the explicit bridge-stage architecture slice.
- `../../architecture/future/README.md` remains a redirect-only compatibility lane for older target-architecture links.
- `vision-and-use-cases.md` expands the long-term product direction from smart home to smart block to citizen-owned smart city.
- `phase-roadmap.md` translates the vision into staged execution.
- `architecture-gaps-by-stage.md` maps operational-architecture gaps onto capability stages and the deployment-maturity overlay while keeping public release labels such as `v0.1` separate from that stage map.
- `deployment-maturity-ladder.md` defines the separate deployability overlay used for hardware and operational readiness.
- `feature-matrix-by-use-case.md` compares use cases, sensors, outputs, strengths, and constraints.
- `technical-philosophy-and-architecture.md` defines the top-level technical posture, architectural rules, and current reference implementation shape.
- `product-requirements-phase-1.md` defines the first single-parcel release slice.
- `block-level-operating-model.md` defines how shared block intelligence should work.
- `integrated-parcel-system-spec.md` defines the unified parcel-kit architecture and cross-node integration rules.
- `version-and-promotion-matrix.md` maps program-phase promotions, capability stages, deployment maturity, and implementation status.
- `node-taxonomy.md` lists current, next-promotion, geography-gated, research-gated, and v1.5 bridge evidence surfaces.
- `../../media/diagrams/prototype-integration-diagram-pack.md` provides a shared diagram pack for prototype integration, architecture avenues, and design possibilities.
- `neighborhood-signal-transformation-overview.md` frames the privacy-scoped path from home signals to block intelligence.
- `recommendation-engine-and-safety-language.md` defines guidance posture and language boundaries.
- `pilot-success-metrics-and-evaluation.md` defines how early pilots should be judged.
- `home-and-parcel-context-capture-standard.md` defines the minimum context needed for honest interpretation.
- `route-readiness-model-overview.md` defines the local route and access interpretation layer.
- `community-governance-and-operator-model.md` defines participation and operator boundaries.
- `shared-map-product-posture.md` defines what the shared map should and should not be.
- `neighborhood-pilot-design-package.md` defines a practical early network-effect pilot structure.
- `sensor-placement-and-representativeness-guide.md` defines how siting affects confidence and observability.
- `data-rights-and-participant-controls-ux-outline.md` defines the participant-facing control model.
- `network-effect-measurement-methodology.md` defines how to test whether nearby participation really improves the product.
- `multi-unit-building-operating-model.md` extends the operating model to apartments, condos, and shared buildings.
- `resilience-hub-operating-model.md` defines how community hubs fit into the network.
- `household-recommendation-catalog.md` inventories candidate household action guidance.
- Root-level canonical overview files still contain additional program framing and should be reconciled here over time.

## Files in this lane, grouped by concern

The flat `system/` directory holds ~30 canonical documents plus the `parts/` subdirectory. Grouped for discoverability — each entry links to the file and names its job in one line. Authority between `system/` and other lanes is resolved in [`../../meta/markdown-canonical-topic-matrix.md`](../../meta/markdown-canonical-topic-matrix.md); this section is navigation, not reauthorization.

### Version axes and promotion

- [`version-and-promotion-matrix.md`](version-and-promotion-matrix.md) — four-axis model (accepted slice / capability stage / deployment maturity / impl status).
- [`phase-roadmap.md`](phase-roadmap.md) — Stages A–F with per-stage deployment posture.
- [`architecture-gaps-by-stage.md`](architecture-gaps-by-stage.md) — gaps placed at the stage they must become explicit.
- [`architectural-choices-by-stage.md`](architectural-choices-by-stage.md) — master summary of class / power / IP / transport / calibration per program-phase.

### Integrated parcel system

- [`integrated-parcel-system-spec.md`](integrated-parcel-system-spec.md) — unified parcel-kit architecture; hardware role map + deployment posture per node.
- [`node-taxonomy.md`](node-taxonomy.md) — canonical node-family classification with posture tags; tiered acquisition model.
- [`parts/`](parts/) — per-node aggregator pages (bench-air-node, mast-lite, flood-node, weather-pm-mast, thermal-pod, circuit-monitor).
- [`sensor-placement-and-representativeness-guide.md`](sensor-placement-and-representativeness-guide.md) — placement → deployment class map; sensor variant selection principles.
- [`deployment-maturity-ladder.md`](deployment-maturity-ladder.md) — deployment-class standards (power / IP / transport per class) + field-hardening bundle.

### Platform programs (physical + adapter)

- [`calibration-program.md`](calibration-program.md) — reference instruments, burn-in, admissibility, drift, §F build-spec metadata block, §G promotion-bar compliance. Physical sensors.
- [`adapter-trust-program.md`](adapter-trust-program.md) — parallel program for Tier 1 / Tier 2 adapter-derived data.

### Philosophy + technical posture

- [`technical-philosophy-and-architecture.md`](technical-philosophy-and-architecture.md) — top-level principles and architectural rules.
- [`cross-repo-architecture.md`](cross-repo-architecture.md) — how the four repos work together; calibration/admissibility cross-repo flow.

### Product framing

- [`vision-and-use-cases.md`](vision-and-use-cases.md) — long-term product vision, use-case surface.
- [`product-requirements-phase-1.md`](product-requirements-phase-1.md) — first single-parcel release slice requirements.
- [`feature-matrix-by-use-case.md`](feature-matrix-by-use-case.md) — use cases × sensors × outputs × constraints.

### Operating models

- [`block-level-operating-model.md`](block-level-operating-model.md) — shared block intelligence.
- [`multi-unit-building-operating-model.md`](multi-unit-building-operating-model.md) — apartments, condos, shared buildings.
- [`community-governance-and-operator-model.md`](community-governance-and-operator-model.md) — participation + operator boundaries.
- [`resilience-hub-operating-model.md`](resilience-hub-operating-model.md) — community hubs.
- [`neighborhood-pilot-design-package.md`](neighborhood-pilot-design-package.md) — early network-effect pilot structure.
- [`route-readiness-model-overview.md`](route-readiness-model-overview.md) — route/access interpretation.

### Shared-layer and neighborhood surfaces

- [`shared-map-product-posture.md`](shared-map-product-posture.md) — what shared map is and isn't.
- [`neighborhood-signal-transformation-overview.md`](neighborhood-signal-transformation-overview.md) — privacy-scoped path from home signals to block intelligence.
- [`network-effect-measurement-methodology.md`](network-effect-measurement-methodology.md) — testing whether participation improves product.
- [`household-recommendation-catalog.md`](household-recommendation-catalog.md) — candidate household action guidance.
- [`recommendation-engine-and-safety-language.md`](recommendation-engine-and-safety-language.md) — guidance posture and language boundaries.

### Context, participants, and pilots

- [`home-and-parcel-context-capture-standard.md`](home-and-parcel-context-capture-standard.md) — minimum context for honest interpretation.
- [`data-rights-and-participant-controls-ux-outline.md`](data-rights-and-participant-controls-ux-outline.md) — participant-facing control model.
- [`pilot-success-metrics-and-evaluation.md`](pilot-success-metrics-and-evaluation.md) — how pilots are judged.

### Canonical links

- [`canonical-links.md`](canonical-links.md) — link authority roll-up.

## Related workstreams

- data model
- privacy and governance
- pilot playbooks
- hardware node families
- ingest, inference, parcel platform, and shared-map software

## Next docs to add

- public and partner data export posture
- operator dashboard posture
- community incident workflow model
