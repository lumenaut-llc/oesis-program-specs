# Architecture review: keep, dangerous, change now

**Canonical incorporation:** Judgments are embedded in [`architecture/current/technical-philosophy.md`](architecture/current/technical-philosophy.md), [`architecture/current/milestone-roadmap.md`](architecture/current/milestone-roadmap.md), and [`architecture/current/implementation-posture.md`](architecture/current/implementation-posture.md). This file keeps the scored review.

## Overall verdict

This is a good architecture for building the system you actually want.

It is not automatically a good architecture for building the first thing you should ship unless you defend the phase boundaries aggressively.

## Keep

### 10 out of 10
- parcel-first decision anchor
- evidence modes

### 9 out of 10
- four-layer core separation
- governance as architecture

### 8 out of 10
- modular hardware families
- rules-first baseline posture

## Dangerous

### 10 out of 10
- version-language confusion

### 9 out of 10
- future gravity leaking into the current slice
- shared intelligence being prioritized before collection maturity

### 8 out of 10
- governance doctrine outrunning governance behavior
- hardware family sprawl

### 7 out of 10
- parcel-first reasoning becoming parcel-bounded reasoning

## Change now

### 10 out of 10
- freeze the real near-term architecture in one sentence and repeat it everywhere

Recommended line:

`v0.1` = one parcel, one bench-air lineage, one parcel context, one ingest path, one inference path, one parcel view

Next broader slice (program phase `v1.0`, field-hardened parcel kit with mast-lite and related trust surfaces) stages in this repo via the optional **`v1.0` asset lane** (`oesis/assets/v1.0/`, `make oesis-v10-*`). See [`00-version-labels-and-lanes.md`](00-version-labels-and-lanes.md).

Everything else is downstream.

### 9 out of 10
- move deployment truth ahead of feature truth
- treat flood as opt-in and thermal as non-core until air plus context is stable

### 8 out of 10
- turn governance from mostly policy shape into a minimum executable loop sooner
- keep route and block intelligence downstream of proven parcel outputs for now

### 7 out of 10
- standardize language around parcel-first, multi-scale

## Clean summary

The architecture is not too ambitious because of its ideas.
It is too ambitious only when people speak as though the ideas are already executable product reality.
