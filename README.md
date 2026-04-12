# Open Environmental Sensing and Inference System (program-specs)

This repository is the program-definition and release home for the Open
Environmental Sensing and Inference System (`OESIS`) program.

Open Environmental Sensing and Inference System (`OESIS`) is the canonical
system name. `Resilient Home Intelligence` (`RHI`) remains a legacy
compatibility name during the transition.

The Git repository is **`oesis-program-specs`** on GitHub (`lumenaut-llc/oesis-program-specs`), alongside the sibling **`oesis-runtime`** checkout.

**Finishing the remote rename:** If GitHub still lists the old repository name, open **Settings → General → Repository name** on that repo and set it to **`oesis-program-specs`**. GitHub keeps redirects from the old URL for a while. This checkout should use `origin` → `https://github.com/lumenaut-llc/oesis-program-specs.git`; if not, run `git remote set-url origin https://github.com/lumenaut-llc/oesis-program-specs.git`. After the rename, confirm with `git fetch origin` and push (`git push -u origin main` if needed). Update **GitHub Pages** or any external links that still use the old path or `github.io/.../resilient-home-intelligence/...` URLs.

## Purpose

Open Environmental Sensing and Inference System is a modular, dwelling-scale
environmental sensing and parcel-awareness initiative. It combines:

- physical sensor builds
- parcel-level software
- neighborhood inference
- privacy/governance rules
- documentation and pilot playbooks

The system is designed so each parcel can receive parcel-level condition estimates even with partial sensor adoption. More participating nodes can improve precision and confidence, but they do not unlock basic functionality.

This repository now serves as the canonical home for:

- architecture and system definitions
- schemas, examples, and release packet materials
- governance, privacy, and publication controls
- build and publication support for split-repo workflows

The runnable Python reference services and the public preview site now live as
standalone sibling repositories:

- `../oesis-runtime`
- `../oesis-public-site`

Operational commands in this repository now proxy to those sibling repos by
default. The old in-repo runtime and site trees have been retired and replaced
with migration pointers only.

## Core principles

- Parcel first
- Private by default
- Shared by choice
- Useful as a standalone build
- More powerful as a network
- Explicit uncertainty
- Open and well documented

## Repository map

- `program/` — program overview, notice, and index
- `architecture/` — canonical architecture home, including frozen `current/` (`v0.1`), debated `future/` (`v1.0`), and system narratives
- `contracts/` — frozen `v0.1` contract docs plus additive `v1.0/` schema/example deltas
- `release/` — release packet materials, publication controls, and launch collateral
- `hardware/` — physical sensor nodes and installation systems
- `software/` — subsystem docs, wrappers, and operator guides
- `legal/` — licensing, defensive publication, governance, contribution policy, and privacy policy
- `operations/` — pilot playbooks and operational rollout materials
- `media/` — diagrams, renders, and images
- `oesis_build/` — build and publication support for contracts, release, and split-repo workflows
- `shared/` — shared standards, templates, and glossary
- `meta/` — planning, milestones, operating notes, repo-split execution docs, and contribution guidance
- `artifacts/` — generated split artifacts such as contracts, public content, and runtime evidence bundles
- `scripts/repo_split.py` — split automation for syncing runtime assets, building bundles, and producing evidence artifacts for sibling repos
- `oesis/` — migration pointer to the standalone `../oesis-runtime` repository
- `sites/public-preview/` — migration pointer to the standalone `../oesis-public-site` repository

## Split workflow

Use these commands while the split is in progress:

- `make oesis-validate`
- `make oesis-check`
- `make oesis-http-check`
- `make public-site-build`
- `make repo-split-sync-runtime-assets`
- `make repo-split-build-contracts-bundle`
- `make repo-split-build-public-content-bundle`
- `make repo-split-build-runtime-evidence-bundle`

The canonical execution plan lives in `meta/repo-split-plan.md`.

## Version lanes

Use these repo surfaces as the default architecture-and-contract entrypoints:

- `architecture/current/` — frozen `v0.1` current truth
- `architecture/future/` — debated `v1.0` target lane
- `contracts/examples/` and `contracts/schemas/` — frozen `v0.1` default contract surface
- `contracts/v1.0/` — additive `v1.0` contract deltas and future-lane notes

The older `technical-architecture/` tree remains as a transitional pointer, but
contributors should treat `architecture/current/` and `architecture/future/` as
the canonical current-vs-future split.

## Start here

1. Read `NOTICE.md`
2. Read `program/README.md`
3. Read `release/v1.0/open-source-v1-summary.md`
4. Read `architecture/README.md`
5. Read `architecture/current/README.md` for the frozen `v0.1` lane or `architecture/future/README.md` for the debated `v1.0` lane
6. Read `meta/repo-split-plan.md` if you are working on runtime/site extraction or bundle boundaries
7. Use `shared/templates/` when starting a new subsystem or document
