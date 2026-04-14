# Operator Quickstart v1.5

## Purpose

Describe the first operator path that proves OESIS can measure household
response rather than only render parcel condition.

## What this guide should prove

This quickstart should prove the first serious bridge from parcel evidence to
household response measurement:

1. ingest outdoor or parcel hazard evidence
2. ingest house-state support evidence
3. capture observed equipment posture
4. record a bounded household action
5. measure the outcome over a bounded response window

## Minimum bridge surfaces

- indoor PM2.5 plus indoor temperature and RH
- mains and backup-power posture
- HVAC fan and recirculation state where available
- purifier state where available
- action-log entries
- verification-outcome records

## First serious proof path

Smoke protection remains the first serious closed-loop proof:

1. ingest outdoor evidence
2. ingest indoor response evidence
3. capture observed equipment state
4. record bounded household action
5. measure outcome over a bounded response window such as 30 to 90 minutes

## What this guide should not imply

- that the product mainly advances by adding richer weather hardware everywhere
- that controls compatibility is already a full product promise
- that bounded controls are already the center of gravity

## Stage note

- `current v1`: parcel sensing and inference baseline
- `v1.5`: response bridge surfaces become first-class
- `v2.5`: compatibility inventory and bounded controls mature later

## Related

- `README.md`
- `inference-engine/architecture.md`
- `inference-engine/interfaces.md`
- `parcel-platform/interfaces.md`
