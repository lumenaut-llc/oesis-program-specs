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

The first concrete ingest contract is `oesis.bench-air.v1`, produced by the bench-air-node hardware subsystem. The ingest service should treat that packet as evidence input only. It should not attempt to compute parcel safety statuses directly.

## Adjacent systems

- hardware nodes publish packets to the ingest boundary
- the inference engine consumes normalized observations
- the parcel platform consumes parcel-state outputs produced later by inference
- governance and privacy docs define what data may be retained, shared, or redacted

## Implementation scaffold

The `scripts/*.py` entrypoints are now thin compatibility wrappers around the
canonical repo-root `oesis.ingest` package. From `repo/`, prefer
`python3 -m oesis.ingest.validate_examples` and the other
`python3 -m oesis.ingest.*` commands when writing new runbooks or automation.

The first executable contract check lives in `scripts/validate_examples.py`. It validates the current example payloads in `../../contracts/examples/` against the MVP expectations for:
- `oesis.bench-air.v1` node observations
- parcel-state snapshots

The next reference scaffold is `scripts/normalize_packet.py`. It reads a node packet, performs the same lightweight validation assumptions as the validator, and emits a normalized observation object shaped for the inference engine boundary.

`scripts/normalize_public_weather_context.py` is the first source-specific external adapter. It reads a raw weather-shaped JSON payload and emits the canonical public-context object used by the inference engine.

`scripts/normalize_public_smoke_context.py` is the smoke-side companion adapter. It reads a raw smoke-shaped JSON payload and emits the same canonical public-context object with conservative smoke support.

`scripts/ingest_packet.py` is the simplest local end-to-end entrypoint for bench bring-up. It accepts a packet from a file or stdin, validates it, and prints the normalized observation.

`scripts/extract_latest_packet.py` pulls the newest JSON packet out of a mixed serial log so boot comments and other monitor noise do not need to be removed by hand.

`scripts/serve_ingest_api.py` is the first minimal HTTP wrapper. It exposes:
- `GET /v1/ingest/health`
- `GET /v1/ingest/schemas`
- `POST /v1/ingest/node-packets`

The server is intentionally lightweight and uses the same normalization code as the local CLI path.

## Local smoke-test path

From `repo/software/ingest-service/`:

1. Run `python3 scripts/validate_examples.py`
2. Run `python3 scripts/normalize_packet.py`
3. Inspect the emitted normalized observation and confirm the raw packet includes `sht45` and `bme680`

This gives the firmware bring-up work a stable local target before any HTTP service, Wi-Fi transport, or persistent storage is introduced.

## Firmware handoff path

When the ESP32 starts emitting serial JSON:

1. Copy one packet line into `packet.json`
2. Run `python3 scripts/ingest_packet.py packet.json`
3. Confirm the packet validates and normalizes cleanly

If you saved a full serial log instead of a clean packet file:

1. Run `python3 scripts/extract_latest_packet.py serial.log --output packet.json`
2. Run `python3 scripts/ingest_packet.py packet.json`

The expected first-build serial payload shape is documented in `../../hardware/bench-air-node/serial-json-contract.md`.
The full first-build operator path is documented in `../../hardware/bench-air-node/operator-runbook.md`.
