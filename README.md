# Open Environmental Sensing and Inference System (OESIS)

OESIS is an open, modular environmental sensing system for individual
properties. It combines low-cost sensor hardware, a structured inference
pipeline, and privacy-first governance to give each dwelling its own
situational awareness — without requiring neighborhood-wide adoption to
be useful.

**What it measures today (v0.1):** smoke, heat, and pluvial flooding / runoff.

**What it produces:** per-parcel condition estimates (shelter, reentry, egress,
asset risk), confidence scores, evidence mode, and plain-language reasoning —
all as structured JSON.

## Why it matters

Most environmental monitoring assumes centralized infrastructure, municipal
sensors, or blanket coverage. OESIS starts from the opposite end: a single
property with a single sensor node can produce useful condition estimates on
its own. Additional nodes and neighborhood participation improve precision and
confidence, but they are not required for the system to work. Data stays
private by default and is only shared when the owner explicitly chooses to
share it.

This matters because:

- **Disaster preparedness gaps are hyperlocal.** Official alerts cover broad
  areas; conditions at your property may differ meaningfully from conditions a
  block away. A parcel-level system closes that gap.
- **Privacy erosion is the norm.** Most smart-home and environmental platforms
  collect data centrally. OESIS keeps parcel-linked data under owner control
  with explicit consent, revocation, retention, and export governance built
  into the system design — not bolted on later.
- **Open hardware and open software lower the barrier.** The full stack — sensor
  builds, firmware, inference engine, and governance rules — is published under
  permissive open licenses so that anyone can build, audit, and adapt the
  system.

Over time, the program's arc extends from sensing and inference toward
functional interpretation, intervention verification, and community-scale
resilience intelligence. But each stage must prove itself as a working,
standalone system before the next stage begins.

## Repositories

OESIS is split across three repositories:

| Repository | What it contains | License |
|---|---|---|
| **[oesis-program-specs](https://github.com/lumenaut-llc/oesis-program-specs)** (this repo) | Architecture, contracts, schemas, hardware specs, release materials, governance | CC BY-SA 4.0 / AGPL-3.0 / CERN-OHL-S-2.0 ([details](#licensing)) |
| **[oesis-runtime](https://github.com/lumenaut-llc/oesis_runtime)** | Python reference services: ingest, inference, parcel-platform | AGPL-3.0 |
| **[oesis-public-site](https://github.com/lumenaut-llc/oesis_public_site)** | Next.js public preview site | AGPL-3.0 |

## Quick start

### 1. Read the specs (this repo)

```
git clone https://github.com/lumenaut-llc/oesis-program-specs.git
```

Start with [`program/v0.1/README.md`](program/v0.1/README.md) for the program
overview, then [`architecture/current/README.md`](architecture/current/README.md)
for the frozen v0.1 architecture.

### 2. Run the runtime

```bash
git clone https://github.com/lumenaut-llc/oesis_runtime.git
cd oesis_runtime
python3 -m venv .venv && source .venv/bin/activate
pip install -e .
```

Validate the full pipeline:

```bash
make oesis-check        # validate examples + run demo + verify CLI output (v0.1)
make oesis-v10-accept   # offline acceptance for v1.0 (trust scoring, multi-node, governance)
make oesis-http-check   # start local HTTP services, verify ingest -> inference -> parcel view
```

Run the demo pipeline (packet in, parcel view out):

```bash
make oesis-demo
```

Run all lane acceptance tests:

```bash
make oesis-accept && make oesis-v02-accept && make oesis-v03-accept && \
make oesis-v04-accept && make oesis-v05-accept && make oesis-v10-accept
```

### 3. Connect hardware (optional)

With a bench-air node connected via USB:

```bash
pip install -e ".[serial-bridge]"
python3 -m oesis.ingest.serve_ingest_api --host 127.0.0.1 --port 8787
python3 -m oesis.ingest.serial_bridge --serial-port /dev/cu.usbmodem101 --parcel-id parcel_demo_001
```

Open `http://127.0.0.1:8787/v1/ingest/live` for a real-time operator dashboard.

## Hardware

OESIS defines open hardware sensor nodes. The v0.1 baseline uses a single node;
later lanes add multi-node kits:

| Node | What it measures | Lane |
|---|---|---|
| **bench-air** | Indoor air quality and environmental conditions | v0.1+ |
| **mast-lite** | Sheltered outdoor air (enables indoor/outdoor comparison) | v0.2+ |
| **flood-node** | Low-point runoff depth | v0.3+ |
| **weather-PM-mast** | Outdoor particulate matter and weather | future |
| **thermal-pod** | Scene-level thermal imaging (Pi + MLX90640) | future |

Hardware specs, BOMs, and installation guides are in [`hardware/`](hardware/).

## How the pipeline works

```
sensor node  -->  ingest service  -->  inference engine  -->  parcel-platform
 (packet)     (normalize packet)    (apply hazard models)   (build parcel view)
```

1. A sensor node produces a raw packet (JSON over serial or HTTP POST).
2. The **ingest service** normalizes the packet into a standard observation.
3. The **inference engine** combines the observation with parcel context and
   public context (e.g., AQI, NWS alerts) to produce a parcel-state snapshot.
4. The **parcel-platform** formats the parcel-state into a dwelling-facing view.

Each step has a JSON schema contract in [`contracts/`](contracts/). The pipeline
runs as a single-pass demo or as three independent HTTP services.

## Version lanes

OESIS uses additive version lanes. Each lane is a progressively wider
"accepted runnable" that adds capability without breaking earlier lanes:

| Lane | Scope | Status |
|---|---|---|
| **v0.1** | One parcel, one bench-air node, one pipeline | Frozen baseline |
| **v0.2** | Two-node kit (bench-air + mast-lite) | Active |
| **v0.3** | Flood-capable runtime (three-node kit) | Active |
| **v0.4** | Multi-node registry + evidence composition | Active |
| **v0.5** | Governance enforcement (consent, revocation, retention, export) | Implemented |
| **v1.0** | Trust scoring, multi-node evidence, contrastive explanations, divergence analysis | Implemented (Tier A) |
| **v1.5** | Measurement-to-intervention bridge | Future |

The runtime defaults to v0.1. Opt into a different lane with:

```bash
export OESIS_RUNTIME_LANE=v0.3
```

See [`architecture/system/version-and-promotion-matrix.md`](architecture/system/version-and-promotion-matrix.md)
for promotion criteria and the full version model.

## Core principles

- **Parcel first** — the dwelling is the anchor for all decisions
- **Private by default** — parcel-linked data stays under owner control
- **Shared by choice** — sharing requires explicit consent and can be revoked
- **Useful standalone** — one node on one parcel produces real condition estimates
- **More powerful as a network** — additional nodes improve precision, not unlock features
- **Explicit uncertainty** — conclusions state their confidence and evidence basis
- **Open and documented** — full stack is published and auditable

## Repository map

| Directory | Contents |
|---|---|
| `program/` | Program overview and numbered narrative packet |
| `architecture/` | Frozen v0.1 architecture, versioned lanes (v1.0, v1.5), system narratives |
| `contracts/` | JSON schemas, examples, and narrative docs per contract object |
| `release/` | Release packet materials per lane (v0.1 through v1.5) |
| `hardware/` | Sensor node specs, BOMs, installation systems |
| `software/` | Subsystem interface docs and operator guides |
| `legal/` | Licensing, governance, privacy policy, contribution policy |
| `operations/` | Pilot playbooks and operational rollout materials |
| `shared/` | Shared standards, templates, and glossary |
| `meta/` | Planning, milestones, and contribution guidance |

## Licensing

This repository uses **split licenses by asset class**. See
[`NOTICE.md`](NOTICE.md) and [`LICENSES.md`](LICENSES.md) for the full matrix.

| Scope | License |
|---|---|
| Documentation and specifications | [CC BY-SA 4.0](LICENSE) |
| Software in `software/` | [GNU AGPL v3](software/LICENSE) |
| Hardware designs in `hardware/` | [CERN-OHL-S-2.0](hardware/LICENSE) |

## Contributing

See [`CONTRIBUTING.md`](CONTRIBUTING.md). Key points:

- Match your contribution's license to the directory it lands in
- Respect privacy boundaries — no real participant data in commits
- Read [`NOTICE.md`](NOTICE.md) to understand the release posture
- Align with the sibling runtime and public-site repos when changes cross boundaries

## Cross-repo workflows

This repository's Makefile proxies validation and build commands to the
sibling checkouts (expected at `../oesis-runtime` and `../oesis-public-site`):

```bash
make oesis-validate                       # runtime example validation
make oesis-check                          # runtime contract checks
make oesis-http-check                     # runtime HTTP endpoint checks
make public-site-build                    # build the public preview site
make repo-split-sync-runtime-assets       # sync spec assets into the runtime
make repo-split-build-contracts-bundle    # produce the contracts bundle
make repo-split-build-public-content-bundle   # produce the public-content bundle
make repo-split-build-runtime-evidence-bundle # produce the evidence bundle
```
