# Governance And Privacy Summary

## Purpose

Provide one compact summary of the ownership, sharing, visibility, and trust
rules that shape the product.

Use this as a short orientation layer.
Use the other docs in this folder and the legal subtree for the full policy
surface.

## Core rule

Private by default.
Shared by choice.
External public data integrated only inside the platform.

Control permission is separate from data-sharing permission.

## Ownership principles

- parcel operators own their raw node data
- parcel operators should be able to see their private exact parcel situation
- parcel operators should choose what they share into the neighborhood intelligence layer
- sharing should improve collective intelligence without forcing parcel operators to expose everything
- community coordination should not become a pretext for household surveillance or operator overreach

## Data categories

### 1. Private owner data

Examples:

- exact raw sensor readings
- exact node location
- exact parcel-level derived state
- structure-specific and route-specific details
- device health and maintenance history
- house-state telemetry such as indoor PM, HVAC mode, recirculation state, purifier state, and backup-power state
- capability and controllability records such as filter-path limits, device compatibility, and control-locality notes
- intervention history and verification history

### 2. Shared data

Examples:

- selected sensor values or trends
- generalized or cell-level signals
- derived contributions to neighborhood inference
- event-based sharing during hazard periods

### 3. External public data

Examples:

- weather
- flood context
- smoke or air context
- terrain or elevation
- alert feeds

### 4. Derived parcel states

Examples:

- shelter_status / reentry_status / egress_status / asset_risk_status
- confidence
- evidence_mode
- reasons
- explanation payloads

## Sharing dimensions

A parcel operator should be able to scope sharing by:

- what is shared
- where it is shared at what precision
- when it is shared
- who can access it
- why it is being shared

## Suggested sharing modes

### Private

Only the parcel operator sees the data.

### Network assist

The platform can use selected data to improve inference, but other users do not
see parcel-attributed raw values.

### Neighborhood visible

Selected signals contribute to a shared neighborhood view at limited precision.

### Public or open

Selected data or derived outputs can be made visible more broadly.

## Product visibility rules

The platform should clearly distinguish:

- your data
- neighbor or shared data
- public or external data
- derived conclusions

## Provenance requirements

Every important displayed condition or status should be traceable to:

- private local evidence
- shared neighbor evidence
- external public context
- derived logic

## Rights and controls

Parcel operators should eventually have:

- access to their raw data
- visibility into what is being shared
- the ability to change sharing settings
- export capability
- delete or revoke controls where practical
- clear visibility into which control paths exist at the parcel and whether any automation is enabled
- a parcel operator override posture that remains separate from neighborhood data-sharing choices

## System trust rules

- do not hide uncertainty
- do not blur private, shared, and public provenance
- do not claim exact knowledge when only regional context exists
- always show observed versus inferred logic clearly

## Related docs

- `README.md`
- `data-ownership.md`
- `privacy.md`
- `permissions-matrix.md`
- `retention-export-deletion-revocation.md`
- `user-consent-and-sharing-notice.md`
- `../../legal/GOVERNANCE.md`
