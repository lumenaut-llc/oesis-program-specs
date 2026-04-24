# Minimum Functioning v0.1

## Purpose

Define the minimum object and behavior set required for a genuinely functioning
first `v0.1` version.

This file is narrower than the full `v0.1` architecture object map. It focuses
on what the first working product slice must do, not on every object the
architecture already recognizes.

## Status

Current minimum functioning slice.

## Frozen v0.1 product slice (implementation scope)

For build and test planning, treat **`v0.1`** as this narrow executable slice:

- **One parcel** — one `parcel_id` and one parcel-context bundle in the reference path.
- **One bench-air node** — one `oesis.bench-air.v1` observation path (default fixture: `bench-air-01`).
- **One software path** — ingest → normalized observation, combined with parcel and public context → inference → parcel view (evidence summary included on the offline reference pipeline).
- **One parcel view** — one coherent dwelling-facing status surface.

Executable checks for this slice live in the sibling **`oesis-runtime`** checkout
(`../../../oesis-runtime` from this file; `../oesis-runtime` from the program-specs
repo root): `make oesis-check`, `make oesis-http-check`, `make oesis-accept`.

**Explicitly out of scope** for this frozen executable slice (do not block `v0.1` on these): other observation families (`mast-lite`, `flood-node`, `weather-pm-mast`, `thermal-pod`), a mature shared-map product surface, full consent/rights/revocation UX, or required live Wi-Fi transport from the node (serial capture and local processing are enough). See `v0.1-acceptance-criteria.md` for the software acceptance checklist.

## Why this file exists

The full `v0.1` architecture includes objects that are `implemented`,
`partial`, `docs-only`, or `planned`.

That is useful for architectural truthfulness, but it can blur the answer to a
different question:

What is the minimum set of objects and behaviors needed for a functioning first
version?

This file answers that question directly.

## Required objects

### 1. Sensor node

Role:

- produce direct local observations
- expose device health and freshness

Status in current reference path: `implemented`

### 2. Packet / raw evidence

Role:

- carry versioned local evidence into ingest

Status in current reference path: `implemented`

### 3. Collection path / home-platform ingest boundary

Role:

- move node data from the device into the trusted ingest surface
- preserve enough receipt, freshness, and delivery truth to support parcel
  conclusions honestly

Status in current reference path: `implemented`

### 4. Normalized observation

Role:

- create one canonical ingest output for downstream reasoning

Status in current reference path: `implemented`

### 5. Parcel

Role:

- act as the primary decision anchor
- give the system a concrete dwelling-facing scope

Status in current reference path: `implemented`

### 6. Parcel context

Role:

- provide enough site and install context to interpret evidence honestly

Status in current reference path: `implemented`

### 7. Public context source

Role:

- provide weather or smoke context when local evidence is sparse or incomplete

Status in current reference path: `implemented`

### 8. Derived parcel condition

Role:

- express what the system believes is true for the parcel now
- carry confidence, evidence mode, and freshness

Status in current reference path: `implemented`

### 9. Derived operational status

Role:

- turn condition logic into user-facing operational conclusions

Status in current reference path: `implemented`

In `v0.1`, this is still expressed through the parcel-state and parcel-view
status surfaces rather than through a richer independent object family.

### 10. Explanation record

Role:

- explain why the parcel condition and status were assigned
- preserve source mix and trust cues

Status in current reference path: `implemented`

### 11. Parcel view

Role:

- present the current parcel answer, confidence, evidence mode, reasons, and
  freshness in one coherent surface

Status in current reference path: `implemented`

### 12. Minimum sharing policy

Role:

- keep exact parcel data private by default
- support at least a simple technical distinction between private and broader
  sharing

Status in current reference path: `partial`

The architecture depends on this object, but the full product surface is not
yet complete.

## Required behaviors

To count as a functioning first version, the system should be able to:

1. collect at least one valid local node packet into the home/platform ingest
   path
2. ingest that packet through a trusted collection boundary
3. normalize that packet into a canonical observation
4. combine it with parcel context and public context
5. derive parcel-level condition outputs
6. derive operational status outputs from those conditions
7. attach confidence, evidence mode, freshness, and explanation
8. present those results in one coherent parcel-facing view
9. keep exact parcel data private by default

## Explicitly deferred or non-blocking for the first functioning slice

These objects matter architecturally, but they are not required to call the
first `v0.1` version functioning:

- full node-registry-driven lifecycle
- mature shared neighborhood signal product surface
- mature shared-map product surface
- route or infrastructure segment as a first-class runtime object
- hazard field unit as a first-class runtime object
- full rights, export, deletion, revocation, and consent product lifecycle
- broader multi-scale doctrine beyond what current confidence and explanation can
  already support honestly

## Relationship to the object map

- `architecture-object-map.md`
  answers: what objects the architecture recognizes
- `minimum-functioning-v0.1.md`
  answers: what subset must work for a functioning first version

## Current interpretation

The current reference stack is already strong enough to support a functioning
first version if it is framed around:

- one local observation path
- one collection path into the home/platform ingest boundary
- one parcel anchor
- one public-context lane
- one parcel inference layer
- one operational status layer
- one explanation layer
- one parcel-facing view
- one minimum sharing boundary

## Source of truth

Use this file together with:

- `reference-stack.md`
- `implementation-posture.md`
- `../../release/v0.1/implementation-status-matrix.md` (release label `v0.1`, filesystem path `v0.1/`)

If a proposed `v0.1` requirement depends on an object that is still only
`partial`, `docs-only`, or `planned`, it should not be treated as part of the
minimum functioning slice without explicit justification.
