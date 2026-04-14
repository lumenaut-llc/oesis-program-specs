# Outside Concepts and Technology Pull-Forward

**Canonical incorporation:** Synthesis → [`architecture/v1.0/proposed-architecture.md`](../../architecture/v1.0/proposed-architecture.md). This file keeps the outside-concept catalog and pull-forward timing.

## Why import ideas from outside the field

The project is strongest as a systems synthesis, not as a novel sensor invention.

That means the best way to make it more distinctive is to borrow powerful patterns from other fields that improve:
- coordination
- trust
- interoperability
- learning
- explanation

## Highest-value outside concepts

### 1. Internet routing and peering

Use network-of-networks logic instead of assuming one pooled network.

Applied idea:
- adjacent local clusters peer instead of merging raw data
- clusters exchange derived, trust-weighted boundary signals
- overlap zones raise confidence where independent nearby networks agree
- disagreement becomes a visible uncertainty signal

This supports a parcel-first but not parcel-bounded future.

### 2. Zero trust from cybersecurity

Treat every cross-parcel or cross-network signal as explicitly authorized and trust-scored.

Applied idea:
- no implicit trust because a node is “inside the neighborhood”
- no implicit trust because a signal comes from a participant
- freshness, calibration state, sharing scope, and evidence quality all gate use

This strengthens governance as technical behavior rather than policy copy.

### 3. Public-health surveillance design

Think in terms of sentinel placement, event definitions, escalation detection, and intervention monitoring.

Applied idea:
- sentinel nodes in especially informative places
- event definitions for smoke, runoff, and heat escalation
- open-source/event-based signals alongside direct measurements
- explicit tracking of intervention impact over time

This moves the system from “sensor dashboard” toward “resilience intelligence network.”

### 4. Federated computation

Aim long term for private-by-computation, not only private-by-policy.

Applied idea:
- parcels or local clusters compute summaries locally
- shared layers exchange aggregated updates rather than raw parcel truth
- useful shared computation happens without centralizing all raw data

### 5. Bounded digital twins

Use operational twins rather than flashy full-scene twins.

Applied idea:
- parcel twin
- route-segment twin
- drainage-path twin
- shared-asset twin

Each twin should hold:
- current state
- uncertainty
- dependencies
- likely failure modes
- interventions
- outcome history

### 6. Observability and event architecture

Borrow strong trace and event-lineage ideas from software infrastructure.

Applied idea:
- treat observation, normalization, inference, confidence downgrade, and sharing decisions as linked events
- build explanation graphs instead of static reasons-only surfaces
- make replay, audit, and post-event learning easier

## Technologies worth pulling forward earlier

### Pull forward now

#### OpenTelemetry
Use tracing early for packet ingest → normalization → inference → parcel view.

Why now:
- strengthens provenance
- improves debugging
- makes the current narrow slice easier to trust

#### CloudEvents
Use a standard event envelope for observation/state changes.

Why now:
- makes append-only event history cleaner
- improves replay and export structure
- helps future interoperability without forcing a full model rewrite

#### DuckDB + Parquet
Use this for cheap analytics, replay, exports, and later public-safe research bundles.

Why now:
- strong for observation/state history
- good for local and cloud analysis
- helps long-term learning without heavy infrastructure

### Pull forward soon after

#### Home Assistant / Matter compatibility inventory
Do this as a compatibility layer, not as a control commitment.

Why soon:
- supports the later bounded-control path
- lets the system understand what could be influenced later

#### MQTT 5 as optional transport
Add as a transport option after the basic HTTP path is clean.

Why soon:
- useful for intermittent connectivity and buffered delivery
- not necessary as the initial central architecture

#### OGC SensorThings compatibility at the edges
Use as an adapter layer, not as the internal core model.

Why soon:
- helps future exchange with cities, researchers, and adjacent systems
- preserves internal parcel-first modeling while improving interoperability

### Pull forward later

#### PMTiles
Good for neighborhood/shared/public map surfaces later.

#### Federated learning
Useful only after the data-quality and governance model are stronger.

#### Fully decentralized mesh as primary transport
Interesting for degraded-mode operation, but too heavy as an early central design.

## Most promising original direction

If one outside pattern should become native to the project, it is this:

**Build OESIS as a zero-trust, parcel-first network-of-networks with client-vantage inference.**

That means:
- owner-controlled local clusters
- derived-signal peering between adjacent clusters
- trust-scored overlap zones
- parcel / route / block outputs chosen from the standpoint of the place being served rather than from the standpoint of a central aggregator

This is more distinctive than “community sensors plus a dashboard,” and it fits the project’s governance model unusually well.

## Caution

Do not chase originality by stacking too many imported ideas at once.

The project gets stronger when outside concepts:
- sharpen the design
- simplify choices
- strengthen trust or learning

The project gets weaker when they become novelty theater.
