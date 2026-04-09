# Contracts v1.0

## Purpose

Provide the additive `v1.0` contract lane without mutating the frozen root
`v0.1` contract surface.

## How to use this lane

- Put future-lane schema deltas in `schemas/`
- Put future-lane example deltas in `examples/`
- Keep root `../schemas/` and `../examples/` as the accepted `v0.1` baseline

## Current posture

This directory is ready for explicit `v1.0` additions. If a required schema or
example is not yet overridden here, the current `v0.1` artifact remains the
baseline reference until a real `v1.0` delta is added.
