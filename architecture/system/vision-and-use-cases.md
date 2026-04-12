# Vision and Use Cases

## Purpose

Define the long-term product vision for Open Environmental Sensing and
Inference System and map the broadest credible use-case surface for home,
block, neighborhood, and city-scale deployment.

This document is intentionally expansive. It is meant to stretch the design space beyond the current MVP while preserving the project's core principles:

- dwelling-scale data
- private by default
- shared by choice
- useful for one home
- more accurate with neighborhood participation
- explicit uncertainty
- resilience before convenience

## Problem and opportunity (summary)

Many people can see **regional** hazard information or buy **isolated** sensors,
but still lack a trustworthy, **parcel-grounded** read that answers what is
likely true **here**, how sure the system is, what evidence supports it, and
what that means for staying, leaving, reentering, or protecting assets.

Longer term, the gap is a **durable local adaptation evidence base**: how hazards
show up at the parcel, how routes and structures respond, what interventions
help, and where neighborhood weak points actually are—without forcing parcel
operators to surrender raw parcel-linked data.

The opportunity is a **parcel-first, multi-hazard, private-by-default**
intelligence layer between coarse public systems and consumer devices—**useful
under partial adoption** and aligned with official systems rather than replacing
them. Strong framing: a locally grounded **climate and disaster intelligence
layer**. Full argument: `../../02-problem-opportunity-and-market-gap.md`.

## Version map

The long-term vision should be interpreted through these staged boundaries:

- `current v1`: parcel sensing and inference
- `v1.5`: measurement-to-intervention foundation
- `v2`: bounded adaptation guidance
- `v2.5`: bounded controls and compatibility mapping
- `v3`: parcel adaptation engine
- `v4`: parcel + route + block resilience

The product should not collapse these stages together in user-facing claims.

**These labels are vision staging, not program-phase or runtime labels.** Executable
phasing (`v0.1` narrow slice, `v1.0` fielded target, `v1.5` measurement-to-intervention
bridge, optional runtime asset lanes, and marketing “v1.0”) lives in
`../../program/README.md`, `../../00-version-labels-and-lanes.md`, and
`../../09-phasing-v0.1-v1.0-v1.5.md`. Do not read `current v1` here as identical to
program-phase `v1.0` or a public release name.

Rough intuition only: vision **`current v1`** overlaps the **parcel-first truth**
territory of narrow program-phase **`v0.1`** through early **`v1.0`**-style fielding;
vision **`v1.5`+** tracks **intervention, control, and verification** themes that
program-phase **`v1.5`** and later milestones formalize elsewhere.

## Product thesis

Open Environmental Sensing and Inference System should start as a parcel operator
resilience system, grow into block-level shared intelligence, and eventually
support citizen-built smart cities.

The home is the primary unit of intelligence.
The block is the first shared coordination layer.
The city is a federation of participating homes and blocks, not a top-down surveillance platform.

The system should be able to answer four questions at every scale:

1. What appears to be happening here right now?
2. How sure is the system?
3. Why does the system believe that?
4. What reasonable next steps should the person or group consider?

Over time, it should also answer two harder questions:

5. What can this parcel change?
6. Did that action help?

## Strategic framing

This project should not be framed as:

- just another smart home dashboard
- a pure climate-risk score product
- a government smart-city system
- a generic environmental sensor map

It should be framed as:

- a dwelling-scale resilience system
- a neighborhood intelligence layer built from voluntary participation
- a citizen-controlled civic infrastructure network
- a platform that turns local sensing into readiness guidance
- a staged path from parcel sensing to parcel adaptation rather than a sudden leap into automation

## Interpreting the long-term end state

The "self-protective house" vision should be interpreted as increasing measurability, interpretability, controllability, and verified adaptation over time.

It should not be interpreted as:
- magical architectural movement
- unsupported automation claims
- control without verification
- centralized operator authority over household systems

The disciplined path is:
- sensing
- inference
- intervention ranking
- bounded control
- outcome verification
- gradual adaptation learning

## Layered model

### 1. Smart home

The home layer must deliver immediate value on day one.

Primary goals:

- monitor household conditions and hazards
- combine sensors with parcel and structure context
- produce clear readiness states
- recommend protective actions
- reduce uncertainty during disruptions

Typical outputs:

- shelter readiness
- air quality readiness
- heat readiness
- flood readiness
- freeze readiness
- outage readiness
- route readiness
- confidence
- reasons
- next steps

### 2. Smart block

The block layer is the first network effect.

Primary goals:

- improve local accuracy through nearby participation
- detect gradients, trends, and anomalies that one parcel cannot see alone
- provide shared intelligence without exposing raw household data by default
- support voluntary coordination and mutual aid

Typical outputs:

- shared block condition summary
- trend direction
- hotspot or low-point alerts
- likely spread or worsening direction
- route degradation by street segment
- neighborhood confidence map

### 3. Smart neighborhood and city

The neighborhood and city layers emerge from many participating blocks.

Primary goals:

- create citizen-owned resilience infrastructure
- support planning and coordination without centralizing household control
- expose aggregate public-interest signals where consent and governance allow
- enable federated collaboration across communities

Typical outputs:

- neighborhood resilience snapshots
- local infrastructure stress signals
- block-to-block condition trends
- civic planning data products
- community adaptation evidence

## Network-of-networks posture

The long-term network may be a **network-of-networks**, not one giant pooled mesh:

- **Owner-controlled clusters** exchange **derived** signals (confidence surfaces,
  event flags, anomaly summaries, coarse cell-level gradients, route or corridor
  status)—not unrestricted raw parcel telemetry pooling by default.
- **Adjacent-cluster peering** and **overlap zones** can raise confidence when
  signals agree within tolerance; **disagreement** stays visible as uncertainty.
- **Event-mode federation** can temporarily broaden **time-bounded** sharing during
  smoke, flood, heat, or similar stress.
- **Corridor and topology** (same choke point, drainage path, wind channel, utility
  corridor) matter alongside geographic distance for cross-network value.
- In **outages or disasters**, nearby clusters may exchange **minimal** derived
  signals **locally**, then reconcile when backhaul returns.
- **Value-of-information** placement: add sensing where it most reduces uncertainty
  across **parcels, routes, or lifelines**—not only where no sensor exists.

Expanded concepts: `../../06-network-of-networks-concepts.md`.

## Product principles

### Immediate utility before network dependency

One home should gain value even if no neighbor joins.

### Shared intelligence before raw-data sharing

The system should prefer privacy-scoped derived signals, aggregation, and bounded visibility instead of exposing raw household telemetry by default.

### Actionable guidance before abstract dashboards

The product should help people decide what to do next, not only show measurements.

### Measurement before control, verification before stronger claims

The project should only expand into stronger control or adaptation claims after it can measure house state, log interventions, and verify whether those actions improved outcomes.

### Honest uncertainty before overclaiming

The system must clearly separate:

- observed
- inferred
- predicted
- stale
- unknown

### Resilience before convenience automation

The first priority is helping people adapt to disruption, degradation, and recovery.

## Information-layer and recovery target

North star: build the best **evidence-to-impact** system, not merely the largest
sensor count. Optimize **measurement accuracy**, **local recency**, **spatial
relevance**, and **decision usefulness** together (`../../07-information-layer-and-functional-recovery.md`).

**Evidence hierarchy:** direct local observation → nearby shared observation →
external public context → modeled or inferred state → verified impact or outcome.

**Observed conditions vs impacts:** separate what the environment appears to be
doing (e.g. smoke burden) from **impact** states (e.g. route closure, power loss,
shelter degradation).

**Assimilation posture:** think in terms of a **continuously updated** state estimate
per parcel or shared cell—value, uncertainty, freshness, evidence mix, and likely
direction—not only a feed plus a rules engine. **Timing integrity** (measured,
transmitted, ingested, fused, decision-relevant horizon) is a first-class quality
dimension.

**Functional and recovery intelligence:** beyond “what hazard?” and “what parcel
status?”—what **functions** are impaired, which **dependencies** matter (transport,
energy, communications, drainage, water, cooling/refuge), what is degrading, and
what **recovery path** looks plausible. **Social vulnerability** should inform
**community** prioritization and planning layers, not drive private parcel inference
directly.

Hazard, functional, and response-state separation: `../../functional-state-and-response-model.md`,
`../../05-revised-architecture-blueprint.md`. This section describes **target**
capability; frozen scope and claims remain in `../current/` and release materials.

## Use-case map

The project can support many more use cases than the current MVP hazard list.

### A. Climate and disaster readiness

#### Wildfire smoke

Home value:

- detect rising indoor and outdoor smoke burden
- compare indoor conditions with nearby shared conditions
- recommend filtration, window closure, recirculation, or ventilation timing

Block and neighborhood value:

- observe plume arrival and directional change
- identify safer local microzones
- detect when nearby blocks worsen before a target home does

#### Urban wildfire and ember exposure

Home value:

- estimate readiness degradation from smoke, heat, wind, and public fire context
- warn when shelter or route confidence is falling

Block and neighborhood value:

- identify probable directional worsening
- highlight clusters of degrading conditions
- support voluntary shared situational awareness during fast-moving events

Important note:

- the system should frame this as readiness and local condition intelligence, not exact flame-front truth

#### Flooding and runoff

Home value:

- detect low-point water accumulation
- identify basement or parcel intrusion risk
- recommend drain checks, item relocation, and route review

Block and neighborhood value:

- identify recurring trouble spots
- reveal curb, inlet, and drainage failures
- show route degradation and passability patterns

#### Extreme heat

Home value:

- identify unsafe indoor heat burden
- track overnight cooling failure
- estimate room-level or parcel-level shelter stress

Block and neighborhood value:

- detect street-level heat islands
- compare shaded and exposed microzones
- identify neighborhoods with weak nighttime recovery

#### Freeze, winter storm, and pipe risk

Home value:

- detect pipe-freeze risk and indoor cold burden
- support freeze preparation and damage prevention

Block and neighborhood value:

- identify outage-plus-freeze clusters
- estimate route icing risk
- map localized cold pockets

#### Windstorm and severe storm

Home value:

- detect gust-driven exposure and rapid pressure shifts
- estimate branch-fall and debris risk

Block and neighborhood value:

- identify exposed corridors and tree-fall zones
- detect neighborhood-level obstruction patterns

#### Landslide and debris flow

Home value:

- detect slope instability precursors where terrain supports it
- estimate runoff and ground-failure risk near a parcel

Block and neighborhood value:

- identify unstable corridors
- support route avoidance and early warning

#### Drought and chronic dryness

Home value:

- track household and parcel dryness stress
- support irrigation timing and vegetation protection

Block and neighborhood value:

- reveal neighborhood vegetation stress patterns
- surface shared drought conditions earlier than coarse public summaries

### B. Household safety and operations

#### Indoor air health

- pollen, smoke, dust, cooking, and ventilation burden
- HVAC effectiveness and filtration status
- recommended safe ventilation windows

#### Home thermal comfort and energy resilience

- room-level heat and cold burden
- insulation or envelope weakness clues
- demand-management and backup readiness
- safe occupancy guidance during outages

#### Water safety and intrusion

- leak detection
- burst-pipe early warning
- sump and crawlspace monitoring
- mold-promoting humidity patterns

#### Backup power and utility resilience

- outage detection
- generator or battery readiness
- load-shedding prompts
- communications and connectivity degradation

#### Home maintenance intelligence

- moisture and mold risk patterns
- ventilation failures
- abnormal thermal behavior
- weather-driven wear and degradation clues

### C. Accessibility, health, and vulnerable-population support

#### Elder care and medically sensitive households

- dangerous heat or cold burden warnings
- poor indoor air alerts
- outage risks for powered medical equipment
- simplified readiness guidance for caregivers

#### Child and school-route safety

- route smoke burden
- flood-passability concerns
- heat exposure for walking corridors

#### Disability and mobility support

- route readiness for wheelchair or low-mobility users
- elevator and outage awareness for multi-unit contexts
- home and neighborhood accessibility degradation during events

### D. Mutual aid and neighborhood coordination

#### Block-level preparedness

- voluntary neighborhood readiness snapshots
- shared alerts about worsening conditions
- supply, shelter, and support coordination

#### Mutual aid activation

- identify where conditions are degrading fastest
- prioritize elderly, isolated, or medically sensitive households if they opt in
- coordinate check-ins and local assistance

#### Community resilience drills

- measure participation readiness
- test communications and response workflows
- evaluate neighborhood preparedness over time

### E. Civic and infrastructure intelligence

#### Street and route condition awareness

- route obstruction
- local flooding
- heavy smoke corridors
- wind-fall trouble spots

#### Utility stress and outage clustering

- identify local power instability
- reveal repeated outage corridors
- support evidence for grid resilience investment

#### Drainage and public-works evidence

- surface repeated curb, inlet, and runoff failures
- provide resident-owned evidence for stormwater fixes

#### Environmental justice and burden mapping

- measure chronic block-to-block environmental disparities
- build resident-controlled evidence about pollution, heat, drainage, and service inequality

### F. Insurance, finance, and property decision support

#### Household preparedness and mitigation planning

- identify where a home most needs hardening
- estimate which improvements reduce household risk the most

#### Property stewardship

- document recurring hazard stressors
- track whether local conditions are improving or worsening over time

#### Evidence for claims or disputes

- create time-stamped household condition records
- support parcel operator evidence during insurance or landlord disputes

Important note:

- these functions require careful legal, policy, and product review before any operational claim is made

### G. Community science and citizen evidence

#### Hyperlocal environmental monitoring

- neighborhood air-quality studies
- heat-island mapping
- runoff pattern tracking
- chronic nuisance evidence

#### Citizen-led adaptation planning

- identify where community investment has the biggest payoff
- support neighborhood-level climate adaptation proposals

#### Shared learning and local governance

- let communities decide what to measure
- define block-specific sharing norms
- support resident-led stewardship models

### H. Recovery and post-event use cases

#### Reentry and habitability

- estimate whether a home is trending toward livable conditions after smoke, flood, or outage events
- distinguish private household recovery from neighborhood-wide recovery

#### Damage triage

- identify which homes or blocks show persistent abnormal conditions
- support priority repair and check-in workflows

#### Recovery monitoring

- track whether conditions are normalizing
- detect secondary risks such as mold, residual smoke, or infrastructure instability

### I. Everyday quality-of-life uses beyond disasters

#### Better daily home operation

- optimize ventilation timing
- improve sleep comfort
- reduce indoor air burden
- make energy use more resilient and informed

#### Neighborhood environmental quality

- understand daily traffic, construction, and pollution effects
- identify healthy times and places for walking, exercise, and play

#### Local place intelligence

- show how a block behaves over seasons
- reveal microclimate differences invisible to regional apps

## Opportunity areas not yet central in the current design

These are plausible future branches that extend beyond the present MVP.

### Multi-unit buildings

- apartment and condo resilience intelligence
- shared-system failures
- floor-by-floor heat and outage conditions
- building-managed and tenant-owned hybrid models

### Schools, churches, and community spaces

- resilience hubs
- neighborhood shelter readiness
- cooling or clean-air refuge support

### Small businesses and storefront corridors

- local hazard and readiness insights for commercial strips
- merchant mutual-aid intelligence

### Agriculture and urban growing

- backyard garden stress
- irrigation and frost timing
- small-plot environmental awareness

### Water quality and contamination

- future expansion into water-quality sensing and household treatment readiness

### Noise and livability

- chronic noise mapping
- neighborhood quality-of-life evidence

### Security-adjacent but non-carceral uses

- environmental anomaly detection
- infrastructure disruption awareness
- community-defined safety signals without turning the platform into a surveillance product

### Public health early signals

- neighborhood heat burden
- smoke burden
- indoor air stress
- chronic exposure patterns

## What the product should avoid becoming

To stay coherent, the project should avoid drifting into:

- generic consumer home automation
- indiscriminate neighborhood surveillance
- raw-data extraction for institutional buyers
- overclaiming predictive power
- a system that only works when the entire network exists

## Recommended product narrative

Use this story arc:

1. Start with one home.
2. Make the home safer, calmer, and more resilient.
3. Let neighbors voluntarily create better local intelligence.
4. Turn blocks into shared resilience networks.
5. Federate those blocks into citizen-built smart cities.

Short positioning statement:

Private resilience at home.
Shared intelligence on the block.
Citizen-owned infrastructure across the city.

## Implications for future workstreams

This broader vision implies future work in:

- multi-hazard sensing strategy
- recommendation and action engine design
- neighborhood signal transformation methods
- mutual-aid and community governance tooling
- route and street-segment readiness modeling
- building and parcel context enrichment
- city-scale federation and interoperability
- claims, safety language, and legal boundaries

## Open questions

- Which use cases create the strongest day-one parcel operator pull?
- Which use cases create the clearest network effect at block scale?
- Which use cases require new hardware classes?
- Which use cases should stay out of scope to avoid surveillance drift?
- How should the project define safe boundaries between guidance, estimation, and formal emergency instruction?
