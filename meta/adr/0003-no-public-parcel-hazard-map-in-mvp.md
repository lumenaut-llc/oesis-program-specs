# ADR 0003: No Public Parcel Hazard Map in MVP

- Status: Accepted
- Date: 2026-03-30
- Owners: program maintainers
- Related workstreams: shared-map, privacy governance, pilot playbooks, legal

## Context

The platform concept naturally invites a neighborhood map experience, but parcel-level hazard visualization can reveal which households are participating, distressed, vacant, or vulnerable. Under partial adoption, even coarse displays can become identifying if thresholds and timing are not handled carefully.

The project needs an explicit decision about whether MVP includes a public parcel-by-parcel map.

## Decision

MVP will not include a public parcel-by-parcel hazard map based on real homeowner-contributed data.

Early shared-map behavior is limited to:
- coarse spatial units
- delayed or batched updates
- thresholded aggregate outputs
- clear distinction between shared homeowner contributions and public context

MVP also prohibits:
- exact parcel markers for real contributed hazard data
- public listing of participating households
- parcel-level publication of egress, reentry, occupancy-adjacent, or similar sensitive states

## Consequences

Positive:
- lowers singling-out and re-identification risk
- reduces vulnerability-targeting risk
- keeps early pilots aligned with private-by-default commitments

Costs:
- neighborhood features will feel less vivid or immediate
- some community value is deferred until stronger privacy and coverage controls exist

## Alternatives considered

- public live parcel map
  Rejected because it creates the fastest path to privacy and safety misuse.
- authenticated parcel-visible map among neighbors
  Rejected for MVP because even limited audiences can still infer specific household conditions under low adoption.

## Follow-up work

- implement map suppression thresholds and delay logic
- define a coverage-disclosure pattern that does not leak low-participation counts
- require review before any broader map publication
