# Parcel Platform

## Purpose

The dwelling-facing parcel application and API surface. It turns parcel-state outputs, evidence summaries, and freshness data into a usable view of conditions at one parcel without hiding uncertainty.

The current `v1` center of gravity remains parcel-state presentation.

**Capability stage `v1.5`** adds separate support-object surfaces for **house state**, **coarse house-capability** and **read-side equipment signals**, **intervention history**, and **verification / outcome history** without breaking the parcel-state baseline.

**Control-compatibility inventory** (full per-parcel interface-class mapping, integration tiers, and bounded-control policy) is primarily **capability stage `v2.5`**. Draft `control_compatibility` payloads or APIs may appear under `v1.5` for forward compatibility; they must not be described as operationally complete until `v2.5` criteria are met. See `../../architecture/system/architecture-gaps-by-stage.md` and `../../architecture/system/version-and-promotion-matrix.md`.

## Current responsibilities

- present the latest parcel-state snapshot
- explain why the current status was produced
- expose freshness, confidence, and evidence mode clearly
- let a parcel operator inspect recent parcel-state history
- act as the boundary for future notifications and user controls
- expose separate private support objects for house state, coarse capability / equipment-state, optional draft control-compatibility records, intervention history, and verification history as those records appear

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

**`v1.5` bridge** adds data capture and reference APIs for:

- house-state support
- house-capability support (coarse / read-side; not the full integration matrix)
- optional draft storage for control-compatibility payloads where needed for experiments
- intervention logging
- verification logging

**`v2.5`** is the primary stage for treating **control-compatibility inventory** and bounded-control policy as first-class, complete operational requirements.

Those support objects stay separate from the current parcel-state output.

## Adjacent systems

- inference engine produces parcel-state snapshots
- ingest service and node schemas shape the evidence references exposed here
- privacy and governance rules constrain what neighborhood or external context can be shown
- shared-map may later consume summarized parcel outputs, but the parcel platform stays parcel-first

## Reference tools

- `python3 -m oesis.parcel_platform.format_parcel_view`
- `python3 -m oesis.parcel_platform.serve_parcel_api`
- `python3 -m oesis.parcel_platform.summarize_reference_state`
- `python3 -m oesis.parcel_platform.admin_reference_state`
- `python3 -m oesis.parcel_platform.process_rights_requests`
- `python3 -m oesis.parcel_platform.export_parcel_bundle`
- `python3 -m oesis.parcel_platform.run_retention_cleanup`

## Implementation scaffold

Executable parcel-platform entrypoints live in the sibling `oesis-runtime`
repository. From that repo root, prefer
`python3 -m oesis.parcel_platform.reference_pipeline` and the other
`python3 -m oesis.parcel_platform.*` commands for new local operator flows.

The first executable parcel-platform reference is
`python3 -m oesis.parcel_platform.format_parcel_view`. It reads a parcel-state
snapshot and emits the dwelling-facing response shape described in `interfaces.md`.

`python3 -m oesis.parcel_platform.serve_parcel_api` exposes the same reference
governance loop through local API endpoints, including summary readout,
rights-request processing, and retention cleanup.

For a full demo across the current reference stack, use
`python3 -m oesis.parcel_platform.reference_pipeline`. It runs the raw packet
through normalization, inference, and parcel formatting in one command.
