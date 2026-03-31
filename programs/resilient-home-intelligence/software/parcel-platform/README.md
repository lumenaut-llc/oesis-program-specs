# Parcel Platform

## Purpose

The homeowner-facing parcel application and API surface. It turns parcel-state outputs, evidence summaries, and freshness data into a usable view of conditions at one parcel without hiding uncertainty.

## Current responsibilities

- present the latest parcel-state snapshot
- explain why the current status was produced
- expose freshness, confidence, and evidence mode clearly
- let a homeowner inspect recent parcel-state history
- act as the boundary for future notifications and user controls

## Needs from other workstreams

- glossary alignment
- governance rules
- procurement assumptions for node capabilities
- hazard model inputs

## MVP focus

The first version should do a small number of things well:
- show the current parcel-state output
- show the reasons and provenance summary behind it
- show whether the assessment is based on local evidence, public evidence, or both
- avoid pretending confidence is higher than it is
- keep sharing, rights requests, reference audit state, and retention actions inspectable for pilot operations

## Adjacent systems

- inference engine produces parcel-state snapshots
- ingest service and node schemas shape the evidence references exposed here
- privacy and governance rules constrain what neighborhood or external context can be shown
- shared-map may later consume summarized parcel outputs, but the parcel platform stays parcel-first

## Reference tools

- `scripts/format_parcel_view.py`
- `scripts/serve_parcel_api.py`
- `scripts/summarize_reference_state.py`
- `scripts/admin_reference_state.py`
- `scripts/process_rights_requests.py`
- `scripts/export_parcel_bundle.py`
- `scripts/run_retention_cleanup.py`

## Implementation scaffold

The first executable parcel-platform reference lives in `scripts/format_parcel_view.py`. It reads a parcel-state snapshot and emits the homeowner-facing response shape described in `interfaces.md`.

`scripts/serve_parcel_api.py` now exposes the same reference governance loop through local API endpoints, including summary readout, rights-request processing, and retention cleanup.

For a full demo across the current reference stack, use `scripts/reference_pipeline.py`. It runs the raw packet through normalization, inference, and parcel formatting in one command.
