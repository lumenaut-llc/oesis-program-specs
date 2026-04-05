---
title: Data Model Overview
description: Canonical definitions for parcels, nodes, observations, states, permissions, provenance, and support objects.
section: data-model
audience: [builder, researcher, contributor]
order: 0
status: stable
---

## Purpose

Canonical definitions for parcels, nodes, observations, states, permissions, provenance, and later-stage support objects.

## Minimum contents

- packet schemas from hardware and external feeds
- normalized observation objects
- parcel-state outputs
- provenance and freshness fields
- identity and permission linkages

## Current status

The current center of gravity remains the `v1` observation, parcel-context, and parcel-state contracts.

`v1.5` adds separate support objects for:
- house state
- house capability
- control compatibility
- intervention events
- verification outcomes

Those support objects should not be mistaken for a breaking change to the current parcel-state contract.

## Machine-readable artifacts

Schemas and examples are available in the repository under `schemas/` and `examples/` directories within the data-model folder.
