# Network-of-networks concepts

**Canonical incorporation:** Federation posture → [`architecture/system/vision-and-use-cases.md`](../../architecture/system/vision-and-use-cases.md) and [`architecture/v1.0/proposed-architecture.md`](../../architecture/v1.0/proposed-architecture.md). This file keeps the concept catalog.

## Core idea

The best long-term network design may not be one giant pooled sensor network.

It may be a network-of-networks where:

- local clusters remain owner-controlled
- adjacent clusters exchange derived signals, not raw parcel truth
- overlap zones increase confidence
- disagreement becomes a visible uncertainty signal
- sharing can expand in event mode during smoke, flood, or heat events

## Why this matters

This design better fits:

- private by default
- shared by choice
- partial adoption
- trust-weighted fusion
- neighborhood intelligence without raw-data centralization

## Promising concepts

### Adjacent-cluster peering

Each neighborhood or block cluster publishes derived boundary signals into overlap zones.

### Confidence handshakes

If nearby networks agree within tolerance and are fresh and trustworthy, confidence rises.
If they disagree, confidence stays capped and the disagreement becomes visible.

### Event-mode federation

During smoke, flood, or heat events, clusters can temporarily broaden sharing of derived, cell-level, time-bounded signals.

### Corridor intelligence

Cross-network value should consider topology, not only geographic distance.
Examples:

- same road choke point
- same creek or drainage path
- same canyon wind corridor
- same utility corridor

### Cross-network calibration transfer

A stronger or denser nearby network can help benchmark a weaker one through comparison windows, generalized reference summaries, or bias flags.

### Value-of-information driven node placement

The goal is not simply to add a sensor where there is no sensor.
The goal is to place one more sensor where it most reduces uncertainty across parcels, routes, or lifelines.

### Derived-signal exchange instead of raw-data exchange

Exchange:

- confidence surfaces
- event flags
- anomaly summaries
- cell-level hazard gradients
- route and corridor status signals

Not:

- unrestricted raw parcel-level data pooling

### Local degraded-mode exchange with later cloud reconciliation

In outages or disasters, nearby clusters can exchange minimal derived signals locally, then reconcile later.

## Best summary sentence

The future advantage of OESIS may not come from one giant unified network.
It may come from many small, owner-controlled local networks that become dramatically more useful when adjacent clusters can exchange trust-weighted, derived, time-bounded signals across overlap zones.
