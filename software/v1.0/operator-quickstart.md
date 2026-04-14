# Operator Quickstart v1.0 Direction

## Purpose

Describe the target-lane operator path once OESIS moves beyond parcel sensing
alone and begins to prove response loops.

## What this guide should prove

The target quickstart should prove more than "the parcel sensing stack runs."
It should prove the first serious bridge from parcel evidence to household
response measurement.

## Foundation surfaces

The starting parcel kit still centers on:

- `bench-air-node`
- `mast-lite`

But the next critical quickstart additions are:

- indoor response evidence
- power and outage evidence
- equipment-state capture
- action logging
- outcome / verification capture

## What this guide should not imply

It should not imply that the product advances mainly by adding richer weather
hardware everywhere.

It should not imply that controls compatibility or bounded controls are already
the center of gravity either.

## First serious proof path

Smoke protection remains the first serious closed-loop proof:

1. ingest outdoor evidence
2. ingest indoor response evidence
3. capture observed equipment state
4. record bounded household action
5. measure outcome over a bounded response window

## Minimum bridge additions

- indoor PM2.5 plus indoor temperature and RH
- mains and backup-power posture
- HVAC fan and recirculation state where available
- purifier state where available
- action-log entries
- verification-outcome records

## Staging note

- `current v1`: parcel sensing and inference baseline
- `v1.5`: response bridge surfaces become first-class
- `v2.5`: compatibility inventory and bounded controls mature later

## Related

- `README.md`
- `inference-engine/architecture.md`
- `inference-engine/interfaces.md`
- `parcel-platform/interfaces.md`
