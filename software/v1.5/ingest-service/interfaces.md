# Ingest Service Interfaces v1.5

## Purpose

Describe the bridge-stage ingest posture once support surfaces become
first-class inputs.

## Core ingest rule

Not every important bridge input is a hardware-native node packet.

The ingest boundary should be able to accept:

- node packets
- adapter-derived snapshots
- support-object records

without forcing every new capability to become a new physical node class.

## Bridge-stage input families

- outdoor and indoor node packets
- indoor-response observations
- power-state observations
- equipment-state snapshots
- action-log entries
- verification-outcome records

## Why this matters

The next critical product move is not simply more weather hardware support.
It is support for the records that connect parcel evidence to house state,
action, and measured outcome.

## Record classes

### Physical-node packets

- `bench-air-node`
- `mast-lite`
- planned indoor-response and power/outage nodes
- optional geography-gated modules later

### Adapter and support records

- equipment-state adapter snapshots
- house-state support objects
- action-log entries
- verification-outcome records

## Guardrail

The ingest layer should preserve clear distinctions between:

- direct observations
- adapter-derived state
- household or operator action records
- later compatibility records

## Stage note

- `v1.5`: indoor response, outage, equipment-state, action, and verification are
  first-class ingest concerns
- `v2.5`: compatibility inventory may expand the support-object lane later
