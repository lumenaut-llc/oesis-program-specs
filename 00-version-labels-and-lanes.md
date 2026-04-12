# Version labels and lanes

This file is the short glossary for version language in this repository and in the numbered operating packet (`01`–`11`). Use it to avoid mixing **program phases**, **runtime asset lanes**, and **public release** naming.

**Canonical incorporation:** The same vocabulary is summarized in [`program/README.md`](program/README.md) (program phase labels) and connected to milestones in [`architecture/current/milestone-roadmap.md`](architecture/current/milestone-roadmap.md).

## How to read the table


| Kind of label                                 | Meaning in this packet                                                                                                                                                                                                                                                              | Meaning in `oesis-runtime`                                                                                                                                                                                                                                       |
| --------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Program phase `v0.1`**                      | Narrow executable reference slice (see `[09-phasing-v0.1-v1.0-v1.5.md](09-phasing-v0.1-v1.0-v1.5.md)`)                                                                                                                                                                              | Frozen default: root `oesis/assets/examples/` and `oesis/assets/config/inference/`, `make oesis-accept`, `make oesis-http-check`, etc. (`[README.md](README.md)`)                                                                                                |
| **Program phase `v1.0`** (fielded parcel kit) | First broader fielded parcel-intelligence architecture target: mast-lite, stronger registry/trust, limited shared signal, etc. (see `[05-revised-architecture-blueprint.md](05-revised-architecture-blueprint.md)`, `[09-phasing-v0.1-v1.0-v1.5.md](09-phasing-v0.1-v1.0-v1.5.md)`) | **Same intent as the optional runtime `v1.0` lane**: additive overrides under `oesis/assets/v1.0/` merged over the `v0.1` baseline; `make oesis-v10-accept`, `make oesis-v10-check`, `make oesis-v10-http-check` (`[README.md](README.md)` “Parallel v1.0 lane”) |
| **Program phase `v1.5`**                      | Measurement-to-intervention bridge (house state, intervention, verification)                                                                                                                                                                                                        | Roadmap only; not a separate runtime overlay in this repo today                                                                                                                                                                                                  |
| **Public / marketing “v1.0”**                 | Website, release packet, or grant language                                                                                                                                                                                                                                          | Must not be assumed identical to program-phase `v1.0` or runtime lane `v1.0` unless you explicitly align them in release materials                                                                                                                               |


## `v0.2` and this repository

Older notes sometimes used `**v0.2`** informally for “the next slice after `v0.1`.” **This runtime does not model a `v0.2` lane** (`[README.md](README.md)` “Pre-1.0 lane policy”). Treat `**v0.2` as deprecated shorthand** here; for execution and repo layout, the **next broader pre-1.0 slice** is described as **program phase `v1.0`** (fielded kit) and **staged in code as the optional `v1.0` asset overlay**, not as `v0.2`.

## Canonical specs vs this packet

Contracts, schemas, and formal architecture docs remain canonical in the sibling repository `**oesis-program-specs`** (see `[README.md](README.md)`). The files `00`–`11` in this repo are a **runtime-adjacent operating brief** for framing, phasing, and vocabulary; keep them consistent with program-specs, but they do not replace it.

## Where to start reading

- Thesis and language: `[01-core-thesis-and-framing.md](01-core-thesis-and-framing.md)`
- Phasing detail: `[09-phasing-v0.1-v1.0-v1.5.md](09-phasing-v0.1-v1.0-v1.5.md)`

