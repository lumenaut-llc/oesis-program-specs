# Open Source DIY Tech — Open Environmental Sensing and Inference System

This repository is the program-definition and release home for the Open
Environmental Sensing and Inference System program inside Open Source DIY Tech.

Open Environmental Sensing and Inference System (`OESIS`) is the canonical
system name. `Resilient Home Intelligence` (`RHI`) remains a legacy
compatibility name during the transition.

## Purpose

Open Environmental Sensing and Inference System is a modular, homeowner-owned
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

- `PROGRAM.md` — program overview retained after flattening the old program root
- `PROGRAM-NOTICE.md` — program-specific notice retained after flattening the old program root
- `INDEX.md` — program index retained at the repo root
- `docs/` — system docs, release packet materials, schemas, calibration, and pilot playbooks
- `technical-architecture/` — versioned technical architecture canon
- `architecture/` — transitional architecture pointer materials
- `hardware/` — physical sensor nodes and installation systems
- `software/` — subsystem docs, wrappers, and operator guides
- `legal/` — licensing, defensive publication, governance, and contribution policy
- `media/` — diagrams, renders, and images
- `oesis_build/` — build and publication support for contracts, release, and split-repo workflows
- `shared/` — shared standards, templates, and glossary
- `meta/` — planning, milestones, operating notes, and repo-split execution docs
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

## Start here

1. Read `NOTICE.md`
2. Read `PROGRAM.md`
3. Read `docs/release/2026-04-14/open-source-v1-summary.md`
4. Read `technical-architecture/README.md`
5. Read `meta/repo-split-plan.md` if you are working on runtime/site extraction or bundle boundaries
6. Use `shared/templates/` when starting a new subsystem or document
