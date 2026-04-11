# System Overview

## Purpose

Program-level system narrative and top-level operating model.

## Minimum contents

- vision and use-case framing
- layered system model
- core product principles
- canonical operating assumptions
- links to adjacent architecture and governance docs

## Current status

- `vision-and-use-cases.md` expands the long-term product direction from smart home to smart block to citizen-owned smart city.
- `phase-roadmap.md` translates the vision into staged execution.
- `architecture-gaps-by-stage.md` maps operational-architecture gaps onto capability stages and the deployment-maturity overlay while keeping public release labels such as `v0.1` separate from that stage map.
- `deployment-maturity-ladder.md` defines the separate deployability overlay used for hardware and operational readiness.
- `feature-matrix-by-use-case.md` compares use cases, sensors, outputs, strengths, and constraints.
- `product-requirements-phase-1.md` defines the first homeowner-focused product slice.
- `block-level-operating-model.md` defines how shared block intelligence should work.
- `integrated-parcel-system-spec.md` defines the unified parcel-kit architecture and cross-node integration rules.
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
