# Implementation Posture v0.1

## Purpose

Tie the current architecture to the current executable and documented reference
state.

## Status

Current reference implementation posture.

## Canonical homes

- sibling repo `../../../oesis-runtime` (program-specs checkout and runtime
  checkout are siblings under the same parent directory)
  Canonical implementation tree for the current reference services.
- `../../../../oesis_build/`
  Canonical build-foundation implementation tree.
- `../../software/*/architecture.md`
  Subsystem-local architecture explanation.
- `../../contracts/`
  Formal contracts, schemas, and examples.
- `../../legal/privacy/` and `../../legal/`
  Policy constraints that shape implementation behavior.

## Current execution evidence

The current local reference posture is anchored by:

- `make oesis-validate`
- `make oesis-check`
- `make oesis-http-check`

These checks are the minimum evidence for calling a surface implemented in the
current reference path.

**Field or pilot “deployed” is not the same thing.** Install and operations
credibility come from pilot playbooks, operator checklists, and rows in the
implementation status matrix—not from Makefile targets alone. Keep deployment
claims aligned with what is repeatable and evidenced outside the dev reference
path.

## Version versus status

Keep these concepts separate:

- `v0.x` version labels describe accepted product slices
- `implemented`, `partial`, `docs-only`, and `planned` describe maturity within
  or around those slices
- **Program phase**, **reference-runtime asset lane**, and **public or marketing**
  release naming are also distinct; see `../../program/v0.1/README.md` and
  `../../program/operating-packet/00-version-labels-and-lanes.md`

A new `partial` node lane or documented boundary does not automatically justify
promoting a new `v0.x`.

## Near-term blueprint posture

Sensing and hardware expansion order (aligned with
`../../program/operating-packet/05-revised-architecture-blueprint.md`):

- bench-air first
- mast-lite second
- flood optional
- thermal deferred
- weather + PM later

Classifications below should stay consistent with that ordering and with
`../../release/v.0.1/implementation-status-matrix.md` (release label `v0.1`,
filesystem path `v.0.1/`).

**Ingest and temporal integrity** (normalization, receipt timing, buffering,
replay, dedupe, staleness) are part of the **truth model** for the reference
path—not optional polish beneath **`implemented`** claims.

For **program-phase `v0.1`**, the narrow-slice object set in `05` (parcel, packet,
normalized observation, parcel context, parcel state, parcel view, evidence
summary) is satisfied when the reference pipeline and contracts honor those
boundaries; see `architecture-object-map.md` for the enumerated model.

## Current coverage

The lists below summarize posture; the **matrix** remains authoritative for
status.

### Implemented

- example payload validation
- reference packet-to-parcel pipeline
- local ingest API
- local inference API
- local parcel-platform API
- bench-air packet normalization

Parcel-facing condition estimates (for example shelter, reentry, egress, and
asset risk) are **functional interpretation** of fused evidence. **`implemented`**
here means the reference inference and parcel-platform path produces them with
confidence, evidence mode, and reasons—not that every governance or presentation
surface is complete.

### Partial

- mast-lite through the current shared packet lineage
- rights request, export, retention, and operator-access utilities
- shared-map aggregate API
- several hardware build/install lanes beyond the smallest indoor slice

### Docs-only or planned

- richer sharing-settings and consent surfaces
- revocation as a product guarantee
- flood-specific observation family
- weather-pm outdoor observation family
- thermal scene observation family
- public parcel-resolution map support

### Governance execution status

The technical philosophy treats governance as an architecture input, and contract
schemas exist for consent, sharing, rights, and revocation. In the current `v0.1`
reference path, governance surfaces have the following enforcement reality:

- **Sharing settings and consent records**: schema defined, `docs-only` in runtime — no runtime enforcement gate prevents data flow without consent
- **Rights requests and revocation**: schema and utility defined, `partial` — request logging works but revocation does not block downstream surfaces
- **Provenance summary in parcel-state**: `implemented` structurally — source-type labels (local, public, shared) appear in output but are not filtered by sharing policy
- **Private-by-default posture**: enforced by architecture convention (no sharing API exposed in v0.1 pilot), not by runtime governance check

Until governance surfaces reach `implemented` status in the matrix, do not
describe data access as "gated by consent" or sharing as "policy-enforced."

## Posture discipline

- Do not promote **shared neighborhood** surfaces to **`implemented`** until
  **collection, ingest, and parcel-private** reasoning are credible on the
  reference path (`technical-philosophy.md`, `milestone-roadmap.md`).
- Do not claim **governance** execution beyond what the runtime and product
  **enforce**; keep documentation aligned with `partial` and `docs-only` rows in
  the matrix.

## Alignment rule

`v0.1` architecture claims should not outrun the implementation-status
classification used in:

- `../../release/v.0.1/implementation-status-matrix.md` (release label `v0.1`, filesystem path `v.0.1/`)

If a surface is only `partial`, `docs-only`, or `planned`, the architecture
should say so.

If a broader accepted runnable slice is promoted later, update the versioned
architecture documents and the evidence set together rather than treating status
changes alone as a version bump.

## Related docs

- `../../program/v0.1/README.md`
- `../../program/operating-packet/00-version-labels-and-lanes.md`
- `../../program/operating-packet/05-revised-architecture-blueprint.md`
- `../../program/operating-packet/09-phasing-v0.1-v1.0-v1.5.md`
- `technical-philosophy.md`
- `milestone-roadmap.md`
- `architecture-object-map.md`
- `measurement-and-kpis-v0.1.md`
