# ADR 0002: Private-by-Default Parcel Data Model

- Status: Accepted
- Date: 2026-03-30
- Owners: program maintainers
- Related workstreams: privacy governance, parcel platform, shared-map, legal

## Context

The project is building a parcel-first environmental sensing and parcel-awareness platform that combines private homeowner data, shared neighborhood signals, public context, and derived parcel-level estimates.

Without a hard architectural decision, future product work could blur these categories, weaken trust, and create avoidable privacy and consumer-protection risk. The repo now has governance docs that define these classes, but the decision should also be recorded as a durable architecture choice.

## Decision

The platform adopts a private-by-default parcel data model.

This means:
- private parcel data, shared data, public context, derived parcel states, and administrative records are distinct classes
- raw homeowner-contributed parcel-linked data is private by default
- non-private sharing requires an explicit sharing mode and consent record
- product and API design must preserve class distinctions rather than hiding them behind one blended output
- new features may not silently repurpose private parcel data into shared or public outputs

## Consequences

Positive:
- aligns architecture with trust claims
- reduces risk of accidental public exposure of parcel-linked data
- gives product, API, and policy work a stable common model

Costs:
- more metadata and policy plumbing is required
- some features will ship more slowly because they need class-aware access control and consent handling
- shared-map and analytics features must accept coarser and more limited inputs

## Alternatives considered

- simpler blended telemetry model
  Rejected because it would undermine private-by-default commitments and make provenance harder to explain.
- open-by-default neighborhood sensing model
  Rejected because it increases privacy, singling-out, and vulnerability-targeting risk too early.

## Follow-up work

- implement data-class annotations in APIs and storage design
- enforce sharing-mode checks in shared-map and inference integrations
- keep consent, revocation, and audit records as first-class system objects
