# Ingest Service

## Purpose

The service layer that accepts node packets and external data feeds, validates them, normalizes them into canonical observations, and makes them available to downstream parcel inference and homeowner-facing tools.

## Current responsibilities

- accept device-originated evidence packets
- validate schema version, node identity, and field presence
- normalize accepted packets into canonical observation records
- preserve provenance, freshness, and ingest status
- route clean observations to storage and downstream consumers
- quarantine malformed or suspicious payloads for review

## Needs from other workstreams

- glossary alignment
- governance rules
- procurement assumptions for node capabilities
- hazard model inputs

## MVP focus

The first concrete ingest contract is `rhi.bench-air.v1`, produced by the bench-air-node hardware subsystem. The ingest service should treat that packet as evidence input only. It should not attempt to compute parcel safety statuses directly.

## Adjacent systems

- hardware nodes publish packets to the ingest boundary
- the inference engine consumes normalized observations
- the parcel platform consumes parcel-state outputs produced later by inference
- governance and privacy docs define what data may be retained, shared, or redacted
