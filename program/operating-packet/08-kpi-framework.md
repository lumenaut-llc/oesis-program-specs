# KPI framework

**Canonical incorporation:** Measurement posture for the frozen slice → [`architecture/current/measurement-and-kpis-v0.1.md`](../../architecture/current/measurement-and-kpis-v0.1.md); pilots → [`operations/pilots/pilot-operator-checklist.md`](../../operations/pilots/pilot-operator-checklist.md). This file keeps the full KPI catalog.

## 1. Technical validity

Measure whether the system is producing trustworthy evidence.

Suggested KPIs:
- node uptime
- packet completeness rate
- median ingest latency
- percentage of observations passing QA checks
- stale data rate
- percentage of parcel outputs with clear provenance and confidence labels

## 2. Decision usefulness

Measure whether the system is more useful than raw feeds or standalone devices.

Suggested KPIs:
- percentage of parcels receiving a current status
- percentage of parcel views rated actionable by users
- median time from hazard onset to parcel status update
- false positive and false negative rate for parcel-level statuses
- percentage of events where the system provided a more locally relevant explanation than public-only context
- repeat user engagement during active hazard periods

## 3. Network value

Measure whether shared participation creates measurable benefit.

Suggested KPIs:
- confidence uplift when nearby shared evidence exists
- reduction in parcels stuck in inferred_regional or stale mode
- increase in coverage quality as node density rises
- marginal benefit per additional node
- number of nearby parcels benefiting from one added sensor location

## 4. Functional and adaptation value

Measure whether the data becomes useful beyond awareness.

Suggested KPIs:
- measured indoor PM improvement after smoke-related actions
- indoor temperature reduction after heat-related actions
- better route or access interpretation during runoff events
- percentage of logged interventions with measurable before and after outcomes
- repeatability of results across multiple events
- growth in parcel-specific response history over time

## 5. Governance value

Measure whether the product model is actually owner-controlled.

Suggested KPIs:
- opt-in sharing rate
- revocation success rate
- export completion rate
- percentage of users who understand what is private, shared, public, and derived
- user trust score around privacy and data control
- percentage of critical outputs with visible evidence mode and reasons

## Multi-scale extensions (later)

The five groups above default to parcel-facing metrics. As route, block, and lifeline reasoning mature (see [`07-information-layer-and-functional-recovery.md`](07-information-layer-and-functional-recovery.md)), extend measurement with examples such as:

- **Route / access** — accuracy and timeliness of route or egress degradation signals; share of events where access risk (not parcel hazard alone) was the limiting factor; time to detect access compromise versus public-only baselines.
- **Neighborhood / block** — coverage of block-level weak-point proxies; quality of neighborhood condition surfaces; confidence uplift from adjacent-cluster or corridor-aware evidence (see [`06-network-of-networks-concepts.md`](06-network-of-networks-concepts.md)).
- **Lifelines and function** — signals aligned with functional recovery (shelter viability, power or communications continuity, drainage function, refuge viability); whether outputs track impairment and recovery paths, not only environmental readings.

## Success by horizon

### Near term
Success means the system can reliably collect and normalize parcel-relevant data, produce useful parcel views, and show that some users find it more actionable than public-only information.

### Mid term
Success means network participation measurably increases coverage and confidence, and parcel context plus shared evidence materially improves local interpretation.

### Long term
Success means the system accumulates enough structured history to support adaptation learning, intervention ranking, and neighborhood resilience planning.
