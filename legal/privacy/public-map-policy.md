# Public Map Policy

## Purpose

Define the minimum rules for any public-facing or broadly visible shared map layer.

## Governing rule

Early versions should not publish a map that reveals or strongly suggests which specific parcel is contributing smoke, flood, heat, occupancy-adjacent, evacuation-adjacent, or reentry-adjacent information.

## MVP default

- no public parcel-by-parcel hazard map
- no public list of participating households
- no exact parcel geometry tied to real contributed hazard signals

## Allowed early shared-map posture

If a shared map exists in MVP or pilot form, it should:

- use coarse spatial units
- use delayed or batched updates
- require minimum participation thresholds
- avoid exposing raw observations
- avoid precise timestamps that permit singling out

## Publication review triggers

Any shared map release should be reviewed for:

- singling-out risk
- re-identification risk
- vulnerability targeting risk
- mismatch between map confidence and actual coverage
- stale or delayed-source misinterpretation risk

## Red lines

- do not publish exact parcel markers for real contributed hazard data
- do not publish parcel-level egress, reentry, or occupancy-adjacent states
- do not imply complete neighborhood visibility when participation is partial
- do not expose exact contributing parcel counts where that would reveal a small set of homes

## User-facing disclosure

Any shared map should disclose:

- that participation is partial
- that visible conditions may be delayed or aggregated
- that public context and participant-contributed signals are not the same thing
