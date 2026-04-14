# Software v1.5

## Purpose

Hold the bridge-stage software narratives for the measurement-to-intervention
foundation.

## Scope of this lane

Use `software/v1.5/` for software docs that connect:

`hazard -> house state -> action -> measured outcome`

without implying that full automation or `v2.5` compatibility mapping already
exists.

## Expected subareas

- `inference-engine/` for response-model and verification inputs
- `ingest-service/` for bridge-stage event and support-object ingestion
- `parcel-platform/` for action, outcome, and operator-facing verification
  surfaces

## Initial contents

- `operator-quickstart.md`
- `inference-engine/architecture.md`
- `inference-engine/interfaces.md`
- `ingest-service/interfaces.md`
- `parcel-platform/interfaces.md`

## Guardrail

This lane is for the minimum measurement-to-intervention foundation.
Full compatibility inventory and bounded controls posture still belong later in
`v2.5`.
