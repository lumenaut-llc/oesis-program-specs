---
title: Evidence Mode and Observability
description: How the platform distinguishes direct observation from inference, and how that distinction appears in parcel-state outputs.
section: data-model
audience: [builder, researcher, homeowner]
order: 11
status: draft
---

## Purpose

Define how the platform distinguishes direct observation from inference, and how that distinction should appear in parcel-state outputs.

## Core distinction

The platform estimates parcel conditions from evidence layers. It does not observe every parcel condition directly.

This means the system must separate:

- what was directly measured by a sensor at a specific install location
- what was inferred from that measurement plus parcel context
- what was inferred from public context without local confirmation

## Directly measurable examples

- air temperature at a node location
- humidity at a node location
- pressure at a node location
- gas-resistance trend at a node location
- later: PM concentration at a node location
- later: water depth at a flood-node low point

## Not directly measurable from one point sensor

- parcel-wide smoke condition
- parcel-wide outdoor heat burden
- parcel-wide runoff extent
- safe-to-shelter, safe-to-reenter, or safe-to-egress determinations

Those outputs are always interpreted estimates, even when local evidence exists.

## Current parcel-state enum

- `local_only`
- `local_plus_public`
- `public_only`
- `insufficient`

These values remain acceptable for MVP use because they are easy to explain in the UI. They should be interpreted as evidence-composition modes, not as direct statements about truth.

## Observability rules

- A local node does not convert a parcel estimate into direct parcel truth.
- Observability depends on hazard, node type, install role, freshness, and sensor quality.
- A bench-air-node in `indoor` or `sheltered` mode is low-observability evidence for parcel-wide smoke and outdoor heat conditions.
- A future outdoor PM mast has higher smoke observability than a bench-air-node.
- A future flood-node installed at a documented runoff low point has higher flood observability than a generic outdoor node.

## Confidence rules tied to observability

Confidence should fall when:

- evidence comes from a location with weak hazard relevance
- local evidence is stale
- only one point observation supports a parcel-wide conclusion
- public context and local context disagree
- install metadata is missing

Confidence may increase when:

- evidence comes from a hazard-relevant node type and install role
- local and public evidence agree
- recent observations are available
- parcel priors are explicit rather than guessed

## UI and API guidance

- `evidence_mode` should be shown next to confidence and freshness, not hidden behind a tooltip.
- Reasons should explicitly mention whether a conclusion is based on local measurements, public context, or both.
- If evidence is weak, the platform should prefer `unknown` over a confident-sounding warning or reassurance.
