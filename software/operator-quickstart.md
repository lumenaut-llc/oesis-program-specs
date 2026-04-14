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
- `mast-lite` while it continues to emit the `oesis.bench-air.v1` packet shape with outdoor or sheltered metadata
- example public weather and smoke context
- parcel-state inference and parcel-view formatting

**Staging note:** this quickstart is intentionally wider than the narrow **program-phase `v0.1`** current-truth slice because it also covers the **next-promotion** two-node kit (`bench-air-node` + `mast-lite`). Treat successful local use of both nodes as evidence toward **program-phase `v0.2`**, not as automatic proof that the slice is already promoted. See `../architecture/system/version-and-promotion-matrix.md`.

The following node families remain planned extensions to the reference services:

- `indoor-response-node`
- `power-outage-node`
- `flood-node`
- `weather-pm-mast`
- `freeze-node`
- `thermal-pod`

The following **non-node support surfaces** are part of the product taxonomy and
the **`v1.5`** bridge, but are not yet the center of the current quickstart:

- equipment-state capture
- action logging
- outcome / response verification
- richer building-and-site metadata for response modeling

That means this guide still takes you through parcel sensing and inference first.
It does **not** yet claim a full smoke closed-loop path of outdoor PM -> indoor
PM -> action -> verified outcome, even though that is the priority next proof
target in the newer staged product direction.

## What this guide proves today vs later

What this guide proves today:

- the parcel-first ingest -> inference -> parcel-view path works
- a single parcel can combine indoor and sheltered-outdoor evidence
- the product can stay honest about evidence mode, confidence, and provenance

What this guide does **not** prove yet:

- indoor PM-based response verification
- outage continuity tracking
- HVAC / purifier / shade / pump state capture
- action logging and measured outcome verification
- bounded controls or compatibility inventory

Those later surfaces belong to the **`v1.5`** bridge and beyond.

Minimum future bridge additions needed before the first serious smoke
closed-loop proof:

- indoor PM2.5 plus indoor temperature / RH
- equipment-state capture for recirculation, fan, and purifier posture
- action logging for what changed
- outcome / verification records over a bounded response window such as 30-90
  minutes

## Run from the runtime repo root

All commands below assume you start in the **`oesis-runtime`** repository root (sibling to this `oesis-program-specs` checkout):

```bash
cd /path/to/oesis-runtime
```

## Step 1: Confirm the reference stack is healthy

Run these in order:

```bash
make oesis-validate
make oesis-check
make oesis-http-check
```

What each one proves:

- `make oesis-validate`
  validates the current schemas and example payloads
- `make oesis-check`
  runs the reference pipeline from packet to parcel view
- `make oesis-http-check`
  starts the local ingest, inference, and parcel APIs and exercises their HTTP path

If any of these fail, stop here before treating the parcel kit or release site as ready.

## Step 2: Validate a real packet from an installed node

Use the node-specific firmware capture flow first:

- `hardware/bench-air-node/operator-runbook.md`
- `hardware/mast-lite/operator-runbook.md`

Once you have a serial log, extract the newest JSON packet:

```bash
python3 -m oesis.ingest.extract_latest_packet /path/to/serial.log --output /tmp/oesis-packet.json
```

Validate and normalize it:

```bash
python3 -m oesis.ingest.ingest_packet /tmp/oesis-packet.json --parcel-id parcel_demo_001
```

Success means the node packet is structurally usable by the current software path.

## Step 3: Run the example end-to-end parcel demo

To render the current reference parcel output from the checked-in example inputs:

```bash
make oesis-demo
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
python3 -m oesis.ingest.serve_ingest_api --host 127.0.0.1 --port 8787
```

Terminal 2:

```bash
python3 -m oesis.inference.serve_inference_api --host 127.0.0.1 --port 8788
```

Terminal 3:

```bash
python3 -m oesis.parcel_platform.serve_parcel_api --host 127.0.0.1 --port 8789
```

Optional health checks:

```bash
curl -s http://127.0.0.1:8787/v1/ingest/health
curl -s http://127.0.0.1:8788/v1/inference/health
curl -s http://127.0.0.1:8789/v1/parcel-platform/health
```

Operator-only: with ingest on port `8787`, open **`http://127.0.0.1:8787/v1/ingest/live`** to see the last accepted normalized observation (polls in-memory state; see `oesis-runtime` README). Use **`GET /v1/ingest/debug/last`** for JSON.

## Step 5: Post a packet into the local APIs

The quickest manual API test uses the checked-in example packet:

```bash
curl -s -X POST http://127.0.0.1:8787/v1/ingest/node-packets \
  -H 'Content-Type: application/json' \
  -H 'X-OESIS-Parcel-Id: parcel_demo_http' \
  --data-binary @oesis/assets/v0.1/examples/node-observation.example.json
```

For the full API chain, the easiest repeatable command remains:

```bash
make oesis-http-check
```

Use that when you want a known-good ingest to inference to parcel-view path without hand-copying intermediate JSON.

## Step 6: View the release site locally

The public preview site now lives in the sibling repository `../oesis-public-site`.

From the parent directory that contains this specs repo, run:

```bash
cd ../oesis-public-site
```

install dependencies once:

```bash
npm install
npm run dev
```

Visit the local URL printed by Next.js in the terminal.

For a production-style build, run:

```bash
npm run build
```

Use this site only as the public-facing release surface.
Keep the deeper implementation and packet docs in the controlled-review lane.

## Recommended first-operator sequence

For the first integrated parcel kit (**the `v0.2` promotion target**), use this order:

1. Finish hardware build and siting using the parcel build guides.
2. Run `make oesis-validate`.
3. Run `make oesis-check`.
4. Validate one real packet from `bench-air-node`.
5. Validate one real packet from `mast-lite`.
6. Run `make oesis-http-check`.
7. Serve the preview site locally and compare its claims against the current working behavior.

## Related docs

- `README.md`
- `../hardware/parcel-kit/parcel-kit-procurement-checklist.md`
- `../hardware/parcel-kit/parcel-installation-checklist.md`
- `../release/v.0.1/reviewer-packet-index.md` (release label `v0.1`, filesystem path `v.0.1/`)
