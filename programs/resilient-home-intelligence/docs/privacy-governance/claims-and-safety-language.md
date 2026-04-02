# Claims and Safety-Language Standard

## Purpose

Set the minimum product-language rules for parcel-level outputs so the MVP does not overclaim safety, certainty, or coverage.

## Governing rule

The platform may provide transparent parcel-level condition estimates and evidence summaries. It must not present itself as an emergency authority, a safety certifier, or a guarantee of property protection.

## Allowed claim posture

Prefer language such as:
- parcel-level condition estimate
- environmental indicator
- decision-support signal
- based on available local, shared, and public inputs
- confidence reduced when evidence is sparse, stale, or conflicting

## Restricted claim areas

The following topics require caution, review, and clear limitation language:
- evacuation or escape guidance
- reentry guidance
- shelter-in-place guidance
- health-effect guidance
- property damage prevention or assurance
- neighborhood coverage claims

## Red-line statements

Do not say:
- safe to evacuate
- safe to re-enter
- your property is safe
- verified safe
- emergency-grade guidance
- real-time certainty
- anonymous by design
- full neighborhood visibility

## Output-label guidance

Current labels should avoid sounding like a direct instruction to stay, enter, or escape.

Preferred direction for user-facing wording:
- `shelter_status` -> shelter conditions estimate
- `reentry_status` -> reentry conditions estimate
- `egress_status` -> egress conditions estimate
- `asset_risk_status` -> asset risk estimate

If the existing labels remain in technical schemas during MVP prototyping, product copy and UI should still avoid presenting them as commands or guarantees.

## Required limitation themes

Whenever the product surfaces parcel-state outputs, it should communicate that:
- outputs are generated from available evidence, not direct certainty
- conditions may change faster than the system updates
- missing or stale inputs reduce confidence
- official alerts, on-scene conditions, and personal judgment still matter

## Review triggers

The following require product-counsel or governance review before release:
- any new public marketing page describing parcel statuses
- any notification text that implies action timing
- any public map language tied to specific parcels
- any statement comparing the product to official emergency systems
