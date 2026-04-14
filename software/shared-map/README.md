# Shared Map

## Purpose

The neighborhood condition layer and parcel/cell visualization surface.

## Stage placement

This subsystem is intentionally **later** than the narrow parcel-sensing
baseline. It should be treated as a staged shared-resilience surface that grows
after the parcel-first evidence path is honest. It is not the center of the
`v0.1` or `v0.2` product slice.

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

- `python3 -m oesis.shared_map.aggregate_shared_map`
- `python3 -m oesis.shared_map.serve_shared_map_api`

## Implementation scaffold

Executable shared-map entrypoints live in the sibling `oesis-runtime`
repository. From that repo root, prefer
`python3 -m oesis.shared_map.aggregate_shared_map` or
`python3 -m oesis.shared_map.serve_shared_map_api` for new runbooks.

`python3 -m oesis.shared_map.serve_shared_map_api` exposes both the parcel
operator-safe map tile surface and an operator-facing inspection surface for
validating threshold suppression against the configured sharing store.
