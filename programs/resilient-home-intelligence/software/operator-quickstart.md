# Operator Quickstart

## Purpose

Provide one short repo-level path for running the current reference software after the first parcel kit is built and installed.

Use this guide when you want to go from:

- installed `bench-air-node` and `mast-lite`
- local packet validation
- reference ingest, inference, and parcel APIs
- local preview-site viewing

without guessing which commands to run.

## Current implementation boundary

The current reference software path fully supports:

- `bench-air-node`
- `mast-lite` while it continues to emit the `rhi.bench-air.v1` packet shape with outdoor or sheltered metadata
- example public weather and smoke context
- parcel-state inference and parcel-view formatting

The following node families remain planned extensions to the reference services:

- `flood-node`
- `weather-pm-mast`
- `thermal-pod`

## Run from the repo root

All commands below assume you start in:

```bash
cd repo
```

## Step 1: Confirm the reference stack is healthy

Run these in order:

```bash
make rhi-validate
make rhi-check
make rhi-http-check
```

What each one proves:

- `make rhi-validate`
  validates the current schemas and example payloads
- `make rhi-check`
  runs the reference pipeline from packet to parcel view
- `make rhi-http-check`
  starts the local ingest, inference, and parcel APIs and exercises their HTTP path

If any of these fail, stop here before treating the parcel kit or release site as ready.

## Step 2: Validate a real packet from an installed node

Use the node-specific firmware capture flow first:

- `programs/resilient-home-intelligence/hardware/bench-air-node/operator-runbook.md`
- `programs/resilient-home-intelligence/hardware/mast-lite/operator-runbook.md`

Once you have a serial log, extract the newest JSON packet:

```bash
python3 -m rhi.ingest.extract_latest_packet /path/to/serial.log --output /tmp/rhi-packet.json
```

Validate and normalize it:

```bash
python3 -m rhi.ingest.ingest_packet /tmp/rhi-packet.json --parcel-id parcel_demo_001
```

Success means the node packet is structurally usable by the current software path.

## Step 3: Run the example end-to-end parcel demo

To render the current reference parcel output from the checked-in example inputs:

```bash
make rhi-demo
```

This prints one JSON object that includes:

- `normalized_observation`
- `parcel_state`
- `parcel_view`
- `evidence_summary`

Use this command when you want the fastest software-only confidence check.

## Step 4: Start the local APIs manually

If you want the services running in separate terminals, start:

Terminal 1:

```bash
python3 -m rhi.ingest.serve_ingest_api --host 127.0.0.1 --port 8787
```

Terminal 2:

```bash
python3 -m rhi.inference.serve_inference_api --host 127.0.0.1 --port 8788
```

Terminal 3:

```bash
python3 -m rhi.parcel_platform.serve_parcel_api --host 127.0.0.1 --port 8789
```

Optional health checks:

```bash
curl -s http://127.0.0.1:8787/v1/ingest/health
curl -s http://127.0.0.1:8788/v1/inference/health
curl -s http://127.0.0.1:8789/v1/parcel-platform/health
```

## Step 5: Post a packet into the local APIs

The quickest manual API test uses the checked-in example packet:

```bash
curl -s -X POST http://127.0.0.1:8787/v1/ingest/node-packets \
  -H 'Content-Type: application/json' \
  -H 'X-RHI-Parcel-Id: parcel_demo_http' \
  --data-binary @programs/resilient-home-intelligence/docs/data-model/examples/node-observation.example.json
```

For the full API chain, the easiest repeatable command remains:

```bash
make rhi-http-check
```

Use that when you want a known-good ingest to inference to parcel-view path without hand-copying intermediate JSON.

## Step 6: View the release site locally

The release site now uses Astro instead of plain static HTML.

From:

```bash
cd programs/resilient-home-intelligence/docs/release/2026-04-14/site
```

install dependencies once:

```bash
npm install
```

then run:

```bash
npm run dev
```

Visit the local URL printed by Astro in the terminal.

For a production-style static build, run:

```bash
npm run build
```

Use this site only as the public-facing release surface.
Keep the deeper implementation and packet docs in the controlled-review lane.

## Recommended first-operator sequence

For the first integrated parcel kit, use this order:

1. Finish hardware build and siting using the parcel build guides.
2. Run `make rhi-validate`.
3. Run `make rhi-check`.
4. Validate one real packet from `bench-air-node`.
5. Validate one real packet from `mast-lite`.
6. Run `make rhi-http-check`.
7. Serve the Astro release site locally and compare its claims against the current working behavior.

## Related docs

- `README.md`
- `../docs/build-guides/parcel-kit-procurement-checklist.md`
- `../docs/build-guides/parcel-installation-checklist.md`
- `../docs/release/2026-04-14/reviewer-packet-index.md`
