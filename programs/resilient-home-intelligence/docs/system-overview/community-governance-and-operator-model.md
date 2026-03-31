# Community Governance and Operator Model

## Purpose

Define how neighborhood-scale participation, stewardship, and limited operator roles should work without undermining homeowner ownership or private-by-default defaults.

## Why governance is a core system component

At home scale, the system is mostly a product.
At block and neighborhood scale, it also becomes a governance system.

Without clear governance, the project risks becoming:

- socially confusing
- privacy-invasive
- over-centralized
- vulnerable to operator overreach

## Governance principles

- households own their raw local data
- participation in shared intelligence is voluntary
- shared outputs should be narrower than private household outputs by default
- operator roles should exist only where they solve a real coordination problem
- operator roles should not imply unrestricted household visibility
- revocation and exit should be possible

## Core governance questions

Every block or neighborhood deployment should be able to answer:

1. Who can participate?
2. What is shared by default?
3. What can other participants see?
4. Is there an operator role, and if so what can it actually do?
5. How can a participant change or revoke sharing?

## Participation model

### Household participant

A household participant:

- receives private home-level outputs
- can choose whether to contribute to shared intelligence
- can review and adjust sharing settings
- can leave the shared layer

### Block or neighborhood participant

A participant in the shared layer:

- receives shared block or neighborhood intelligence
- contributes bounded derived signals according to consent and product rules

### Community operator

A community operator is an optional stewardship role for pilots or mature neighborhood deployments.

This role may include:

- viewing block or neighborhood condition summaries
- monitoring participation and sensor-health coverage at an aggregate level
- coordinating voluntary incident communication or mutual aid
- helping participants understand shared-layer outputs

This role should not include unrestricted access to raw household telemetry by default.

## Operator role boundaries

### Allowed operator capabilities

- see aggregate participation health
- see block-level trend summaries
- see route and hotspot outputs intended for community coordination
- manage community notices and operating rules

### Restricted capabilities

- browsing raw household sensor histories by default
- viewing private household recommendation cards
- inferring sensitive household status from privileged dashboards where avoidable
- exporting participant data outside community rules

## Governance levels

### Level 0: Solo home

- no community operator
- no shared intelligence

### Level 1: Informal block sharing

- light shared intelligence
- little or no formal operator role
- mostly self-serve participation

### Level 2: Managed neighborhood pilot

- explicit participant cohort
- optional operator role
- documented consent and visibility rules
- incident and escalation procedures

### Level 3: Mature community network

- stable governance model
- transparent operating practices
- well-defined participant rights and community expectations

## Default visibility posture

The shared layer should default to:

- block and neighborhood summaries
- trend and confidence indicators
- route and hotspot signals
- participation-health summaries

The system should avoid defaulting to:

- parcel-identified household condition browsing
- detailed participant-to-participant inspection
- social comparison surfaces that encourage oversharing

## Consent model expectations

Participants should be able to understand:

- what private data stays private
- what derived signals may be shared
- who can see shared outputs
- how long shared outputs persist
- how to change or revoke participation

## Revocation and exit

A participant should be able to:

- stop future contributions
- reduce sharing scope
- leave the shared layer
- understand what previously contributed shared outputs may persist temporarily

## Governance for mutual aid features

Mutual aid is powerful but socially sensitive.

If the project supports check-ins, vulnerability flags, or support coordination later, it should:

- require explicit opt-in
- minimize unnecessary exposure
- separate resilience coordination from generalized neighborhood monitoring

## Transparency requirements

Every community deployment should have:

- a plain-language participation notice
- a sharing-summary view
- a statement of operator role boundaries
- an incident and misuse escalation path

## Abuse and drift risks

The governance model should guard against:

- pressure to overshare
- community operator overreach
- repurposing for non-resilience surveillance
- informal social ranking of households
- exporting resident data to institutional actors without clear approval

## Recommended first pilot posture

For early block pilots:

- keep governance simple
- minimize operator privileges
- make shared outputs obviously derived and bounded
- collect trust and privacy feedback continuously

## Open questions

- When does a block actually need an operator role?
- Which community actions require stronger governance than the product currently assumes?
- How should disputes or misuse be handled in a neighborhood-run deployment?
