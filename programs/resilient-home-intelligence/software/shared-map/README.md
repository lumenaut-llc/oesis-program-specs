# Shared Map

## Purpose

The neighborhood condition layer and parcel/cell visualization surface.

## Current responsibilities

- define inputs
- define outputs
- define interfaces to adjacent services
- track unresolved architectural questions
- provide a coarse aggregation path that suppresses under-threshold shared signals
- provide an operator-facing inspection path for reviewing suppression and sharing-store effects

## Needs from other workstreams

- glossary alignment
- governance rules
- procurement assumptions for node capabilities
- hazard model inputs

## Reference tools

- `scripts/aggregate_shared_map.py`
- `scripts/serve_shared_map_api.py`

## Implementation scaffold

The `scripts/*.py` entrypoints are now thin compatibility wrappers around the canonical repo-root `rhi.shared_map` package. From `repo/`, prefer `python3 -m rhi.shared_map.aggregate_shared_map` or `python3 -m rhi.shared_map.serve_shared_map_api` for new runbooks.

`scripts/serve_shared_map_api.py` exposes both the homeowner-safe map tile surface and an operator-facing inspection surface for validating threshold suppression against the configured sharing store.
