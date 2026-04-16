# Cross-Repository System Architecture

## Purpose

Describe how the four OESIS repositories work together as one system. This is
the document to read when you need to understand the end-to-end data flow,
ownership boundaries, and version alignment across repos.

## The four repositories

| Repository | Identity | Owns | Consumes |
|-----------|----------|------|----------|
| [oesis-program-specs](https://github.com/lumenaut-llc/oesis-program-specs) | Architecture, contracts, governance, release | Schemas, examples, architecture canon, publication policy | Runtime evidence bundles |
| [oesis-runtime](https://github.com/lumenaut-llc/oesis-runtime) | Python reference implementation | Executable services, acceptance tests, reference outputs | Contracts bundles from specs |
| [oesis-hardware](https://github.com/lumenaut-llc/oesis-hardware) | Sensor node specs, firmware, BOMs | Hardware designs, build guides, serial-JSON contracts | Architecture and promotion rules from specs |
| [oesis-public-site](https://github.com/lumenaut-llc/oesis-public-site) | Public preview website | Frontend application, site build/deploy | Public-content bundles from specs |

## End-to-end data flow

```
  oesis-hardware                oesis-runtime                    oesis-program-specs
  ─────────────                ──────────────                   ───────────────────
  Sensor node                  Ingest service                   Contracts & schemas
  (bench-air, mast-lite,       (normalize_packet,               (node-observation,
   flood, weather-pm,           normalize_flood_packet,          parcel-state,
   circuit-monitor)             normalize_weather_pm_packet)     parcel-context, ...)
       │                              │
       │  serial JSON packet          │  normalized observation
       │  (oesis.bench-air.v1,        │
       │   flood.low_point.snapshot,  │
       │   air.pm_weather.snapshot)   │
       ▼                              ▼
  ┌─────────────┐            ┌─────────────────┐
  │ Node emits  │───────────▶│ Ingest service  │
  │ JSON packet │  serial/   │ validates and   │
  │ over serial │  HTTP      │ normalizes      │
  └─────────────┘            └────────┬────────┘
                                      │
                                      ▼
                             ┌─────────────────┐
                             │ Inference engine │
                             │ combines node +  │
                             │ public context + │
                             │ support objects  │
                             │ → parcel state   │
                             └────────┬────────┘
                                      │
                                      ▼
                             ┌─────────────────┐          ┌─────────────────┐
                             │ Parcel platform  │─────────▶│ oesis-public-   │
                             │ builds views,    │  public  │ site renders    │
                             │ evidence,        │  content │ approved content│
                             │ shared map       │  bundle  │ for preview     │
                             └─────────────────┘          └─────────────────┘
```

## Ownership boundaries

### Specs defines, runtime implements

The program-specs repo is the **source of truth** for:

- What schemas exist and what fields they contain
- What examples are canonical for each contract
- What each version lane means and what it includes
- What acceptance criteria must be met for promotion
- What governance, privacy, and publication rules apply

The runtime repo **implements** those specifications:

- Normalizers that produce outputs matching specs schemas
- Inference logic that follows specs-defined hazard rules
- Acceptance tests that verify the specs contract is honored
- Lane overlay system that materializes specs-defined asset sets

**The rule:** change the spec first, then update the implementation. Never let
runtime create contract shapes that specs does not own.

### Hardware defines physical contracts

The hardware repo owns:

- What JSON packets each node family emits (serial-JSON contracts)
- What sensors are used and how they are calibrated
- What physical installation requirements exist
- What firmware behavior produces the packet

These serial-JSON contracts are the **interface agreement** between hardware and
the runtime ingest layer. When a hardware node emits a packet matching
`oesis.bench-air.v1`, the runtime ingest normalizer must accept it.

### Public site presents approved content

The public site consumes a **generated content bundle** from specs. It does not
read raw specs files. The bundle includes:

- Approved source roots (which docs are public-safe)
- Excluded paths (what must not appear in public navigation)
- Release metadata (active release ID, title, summary)
- Repository blob base URL for source links

## Version alignment model

### Three independent version identifiers

| Identifier | Where it lives | What it means |
|-----------|----------------|---------------|
| **Program phase** (v0.1, v1.0, v1.5) | specs: `release/<version>/` | What the accepted product slice includes |
| **Runtime lane** (v0.1 through v1.5) | runtime: `oesis/assets/<lane>/` | Which capability set the runtime activates |
| **Deployment maturity** (v0.1, v1.0, v1.5, v2.0) | specs: `architecture/system/deployment-maturity-ladder.md` | How field-hardened the hardware is |

These are **not the same version**. A runtime lane of v1.0 does not imply
deployment maturity v1.0. See
[`version-and-promotion-matrix.md`](version-and-promotion-matrix.md) for the
full four-axis model.

### How lanes stay synchronized

1. **Specs** defines lane scope in `contracts/<lane>/` (schemas + examples)
2. **Runtime** materializes lane assets from `oesis/assets/<lane>/` overlaid on
   the v0.1 baseline
3. **Canonical example lanes** (v0.1, v1.0, v1.5) must have identical examples
   in both repos — enforced by `make cross-repo-sync` and CI
4. **Overlay lanes** (v0.2–v0.5) may have runtime-only test fixtures that specs
   does not track — these are testing overlays, not canonical contracts

### Consistency enforcement

| Mechanism | Where | What it checks |
|-----------|-------|----------------|
| `make cross-repo-sync` | specs | Example sync, schema coverage, lane alignment, manifest freshness, hardware URL validation |
| `cross-repo-sync` CI job | specs GitHub Actions | Same checks on every push/PR |
| `cross-repo-example-sync` CI job | runtime GitHub Actions | Byte-compares canonical lane examples against specs |
| `version-manifest.json` | specs repo root | Machine-readable snapshot of all 4 repos' alignment state |

## Cross-repo artifact bundles

### Contracts bundle (specs → runtime)

Published by specs. Contains schemas, checked example payloads, version
metadata. The runtime materializes this bundle when activating a non-default
lane.

- Manifest: `artifacts/contracts-bundle/manifest.json`
- Consumer: `oesis-runtime` via `materialize_contracts_bundle()`

### Runtime evidence bundle (runtime → specs)

Published by runtime. Contains acceptance test results, supported-surface
metadata, and optionally generated reference outputs. Specs uses this to make
honest implementation-status claims.

- Manifest: `artifacts/runtime-evidence-bundle/manifest.json`

### Public content bundle (specs → public site)

Published by specs. Contains public-safe content, approved media, release
metadata. The public site renders this without reading raw specs files.

- Source: `artifacts/public-content-bundle/public-content-bundle.json`
- Consumer: `oesis-public-site` via `src/generated/publicContentBundle.ts`

## Adding a new capability

When extending the system (new node family, new observation type, new
governance surface), the work spans repos in this order:

1. **Specs first:** Define the schema, create a canonical example, update the
   relevant contract README, and place it in the correct lane
2. **Runtime second:** Implement the normalizer/inference/platform code, add
   the example to the correct asset lane, write acceptance tests
3. **Hardware if applicable:** Design the node, write the serial-JSON contract,
   create the build guide
4. **Run `make cross-repo-sync`** from specs to verify alignment
5. **Update `version-manifest.json`** if lane counts changed

## Related documents

- [`version-and-promotion-matrix.md`](version-and-promotion-matrix.md) — four-axis versioning
- [`deployment-maturity-ladder.md`](deployment-maturity-ladder.md) — hardware maturity overlay
- [`../../program/execution-plan.md`](../../program/execution-plan.md) — current build sequence
- [`../../meta/repo-split-plan.md`](../../meta/repo-split-plan.md) — split history and ownership rules
- [`node-taxonomy.md`](node-taxonomy.md) — all node families and their staging
