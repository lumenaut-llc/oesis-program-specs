# Debate Map

## Purpose

Capture the major design debates shaping Open Environmental Sensing and
Inference System.

The goal is not to force premature certainty.
The goal is to make the important tensions explicit, identify what is at stake
on both sides, and record the project's current provisional stance.

This file should be treated as a living doctrine file.
As the program matures, some debates may be resolved, some may be split into
narrower decisions, and some may be reframed by real pilot experience.

## How to use this file

Use this file when:

- framing architecture decisions
- deciding what belongs in MVP versus later phases
- evaluating tradeoffs across hardware, software, privacy, and product design
- writing ADRs or design notes
- checking whether a proposal is aligned with the project's deeper principles

For each debate below:

- the left and right side are both partially valid
- the real question is where the project should anchor itself now
- the provisional stance is intentionally practical rather than ideological

## Relationship to the canon

This file is a cross-version doctrine layer.

Use it alongside:

- `../current/architecture-object-map.md`
- `../current/minimum-functioning-v0.1.md`
- `../v1.0/proposed-architecture.md`
- `../v1.0/open-questions.md`

Use `current/` files for frozen `v0.1` truth.
Use `v1.0/` files for debated `v1.0` target architecture.
Use this file for the tensions that influence both.

## Debate 1: parcel-first vs field-first

Version pressure: `cross-version`, strongest in `v1.0`

Affected objects:
- parcel
- public context
- shared neighborhood signal
- derived parcel condition
- route and infrastructure segment
- hazard field unit

### Why it matters

The project is framed around parcel-level conditions and statuses, but the
underlying hazards do not naturally stop at parcel lines.

### What the parcel-first side gets right

- matches the parcel operator's decision surface
- gives the product a clear primary object
- provides a clean permissions and ownership boundary
- keeps the system directly useful to a specific household

### What the field-first side gets right

- better matches physical reality for smoke, runoff, and heat
- reduces false precision
- supports neighborhood and route reasoning more naturally
- avoids treating property lines as truth boundaries

### Risk if overdone

If parcel-first is overdone, the product may imply sharper certainty than the
evidence supports.

If field-first is overdone, the product may become too abstract and stop
answering the parcel operator's core question.

### Provisional project stance

Use parcel-first as the decision and presentation frame.
Use field-first reasoning where the hazard demands it.
Treat parcel outputs as derived conclusions, not as the raw scale of physical
reality.

## Debate 2: rules-first vs model-first

Version pressure: `v0.1` now, `v1.0` later

Affected objects:
- normalized observation
- parcel prior
- public context
- shared neighborhood signal
- derived parcel condition
- explanation record

### Why it matters

The platform wants trustworthy and explainable outputs, but it also wants to
improve over time and eventually handle more complex inference.

### What the rules-first side gets right

- easier to explain and debug
- easier to audit against evidence mode and provenance
- easier to ship honestly in MVP
- better aligned with early sparse data

### What the model-first side gets right

- may eventually handle non-linear interactions better
- can improve with more historical data and pilot evidence
- may perform better on difficult interpolation or multi-signal patterns later

### Risk if overdone

If rules-first is overdone, the system may become brittle or hard to evolve.

If model-first is overdone, the system may become opaque before it has enough
data quality to justify opacity.

### Provisional project stance

Start rules-first.
Design interfaces so that statistical or learned components can later replace or
augment specific scoring steps.
Do not make opaque models foundational to MVP trust.

## Debate 3: exactness vs honesty

Version pressure: `v0.1` now

Affected objects:
- derived parcel condition
- derived operational status
- explanation record
- parcel view

### Why it matters

Users often prefer crisp answers, but the project's trust rules require
explicit confidence, evidence mode, and provenance.

### What the exactness side gets right

- simple answers are easier to act on
- product clarity matters during stressful situations
- users do not want to decode technical uncertainty every time

### What the honesty side gets right

- uncertainty is a real property of the system
- sparse adoption and mixed evidence should not be disguised
- overconfidence is more dangerous than careful ambiguity

### Risk if overdone

If exactness is overdone, the system becomes confidence theater.

If honesty is overdone without careful UX, the system becomes noisy, technical,
and frustrating.

### Provisional project stance

Lead with a clear answer.
Immediately pair it with confidence, evidence mode, and reasons.
Offer deeper provenance on demand.
Do not hide uncertainty in order to make the product feel smoother.

## Debate 4: local-first processing vs cloud-first processing

Version pressure: primarily `v1.0`

Affected objects:
- sensor node
- packet / raw evidence
- normalized observation
- parcel view
- sharing policy

### Why it matters

Processing location affects privacy, resilience, cost, latency, reliability
during outages, and maintenance burden.

### What the local-first side gets right

- stronger alignment with parcel stewardship
- better resilience when connectivity is degraded
- lower dependency on a central operator
- potentially stronger privacy posture

### What the cloud-first side gets right

- easier deployment and iteration
- simpler aggregation and shared intelligence
- easier central QA, monitoring, and updates
- lower initial engineering complexity

### Risk if overdone

If local-first is overdone too early, the project may drown in operational
complexity.

If cloud-first is overdone, the project may drift away from its decentralized
and dwelling-scale values.

### Provisional project stance

Use a practical cloud-backed MVP for ingestion, storage, and explanation.
Preserve clean boundaries so more local processing can be added later without
re-architecting the whole system.
Do not hard-code centralization into the trust model.

## Debate 5: collection network vs shared intelligence network

Version pressure: `v0.1` now, `v1.0` later

Affected objects:
- sensor node
- packet / raw evidence
- collection path / home-platform ingest boundary
- normalized observation
- shared neighborhood signal
- shared map aggregate

### Why it matters

In `v0.1`, the most immediate meaning of network is getting node data into the
home/platform ingest path. In later versions, network can also mean
neighborhood-scale shared intelligence. These are related but different
architecture problems.

### What the collection-network side gets right

- grounds the first version in actual evidence availability
- makes delivery, freshness, and receipt truth part of the architecture
- prevents parcel conclusions from sounding magical or detached from collection
- aligns with the current ingest-first reference path

### What the shared-intelligence side gets right

- captures the longer-term distinctiveness of the project
- supports partial-adoption inference and neighborhood value
- justifies shared-map and generalized network intelligence work later

### Risk if overdone

If collection-network thinking dominates forever, the system may remain only a
private sensing stack and underbuild its network value.

If shared-intelligence thinking dominates too early, `v0.1` may overpromise
neighborhood intelligence before reliable collection and ingest are mature.

### Provisional project stance

In `v0.1`, network should primarily be treated as a collection and
evidence-availability layer.
Shared intelligence is architecturally anticipated, but it is not the primary
meaning of network in the first functioning version.

## Debate 6: standalone value vs network value

Version pressure: `cross-version`

Affected objects:
- sensor node
- shared neighborhood signal
- parcel view
- shared map aggregate

### Why it matters

Every build should be useful on its own, but the larger promise of the project
depends on shared intelligence under partial adoption.

### What the standalone side gets right

- easier adoption and learning
- clearer value for a single parcel operator
- less fragile bootstrapping
- stronger educational and open-source utility

### What the network side gets right

- makes partial-adoption inference meaningful
- increases neighborhood relevance
- creates differentiated value beyond ordinary sensor kits
- supports shared maps and confidence improvements

### Risk if overdone

If standalone value is too weak, adoption will depend on network effects that
do not yet exist.

If network value is underbuilt, the project becomes a collection of disconnected
gadgets instead of a real intelligence system.

### Provisional project stance

Every node and subproject should have standalone value.
Network value should be designed in from the start, but not required for the
first successful user experience.

## Debate 7: private exact data vs useful shared abstraction

Version pressure: `cross-version`

Affected objects:
- sharing policy
- parcel
- shared neighborhood signal
- derived shared-facing outputs
- public context

### Why it matters

The platform depends on shared intelligence, but the project is explicitly
private by default and sharing by choice.

### What the private exact side gets right

- aligns with parcel operator control and trust
- reduces surveillance risk
- preserves the legitimacy of participation
- keeps exact parcel conditions appropriately protected

### What the useful shared side gets right

- allows neighborhood intelligence to exist at all
- improves inference under sparse adoption
- helps users benefit from nearby participation
- supports broader public-interest usefulness where appropriate

### Risk if overdone

If private exactness dominates without abstraction design, the network layer
becomes weak or symbolic.

If sharing dominates, the platform stops being dwelling-scale in any
meaningful sense.

### Provisional project stance

Make sharing granular, scoped, and layered.
Prefer derived, generalized, or cell-level contributions over exposing exact raw
parcel truth.
Retain exact raw owner data as private by default.

## Debate 8: parcel operator tool vs civic infrastructure

Version pressure: primarily `v1.0`

Affected objects:
- parcel view
- shared neighborhood signal
- route and infrastructure segment
- shared map aggregate
- sharing policy

### Why it matters

The system can be built as a household product, a neighborhood intelligence
layer, or eventually a form of community infrastructure.

### What the parcel operator tool side gets right

- strong immediate user value
- clearer UX priorities
- simpler permissions and accountability model
- easier MVP framing

### What the civic infrastructure side gets right

- better supports shared resilience goals
- creates commons-oriented value
- supports broader coordination and public usefulness
- may justify stronger governance and interoperability structures

### Risk if overdone

If the project is treated only as a parcel operator tool, it may underbuild the
shared intelligence layer that makes it distinctive.

If it is treated too early as civic infrastructure, it may acquire governance
and reliability expectations it cannot yet meet.

### Provisional project stance

Start as a strong parcel operator tool with community-aware architecture.
Allow the system to grow toward neighborhood infrastructure only as governance,
quality controls, and operational maturity justify it.

## Debate 9: sensor realism vs product ambition

Version pressure: `v0.1` now

Affected objects:
- sensor node
- observation
- derived parcel condition
- explanation record

### Why it matters

The project uses modular, learnable, open-source-friendly hardware, but
inexpensive sensors have drift, installation bias, and maintenance limits.

### What the sensor realism side gets right

- low-cost sensing has real limitations
- installation and maintenance matter as much as sensor choice
- device health is part of epistemology
- QA must precede strong truth claims

### What the ambition side gets right

- useful systems can still be built with imperfect sensors
- open hardware becomes powerful when combined with priors and external context
- modular staged learning is a strength, not a weakness

### Risk if overdone

If realism becomes defeatist, the project never ships meaningful prototypes.

If ambition outruns quality control, the platform becomes scientifically and
operationally fragile.

### Provisional project stance

Use modest hardware honestly.
Limit early claims.
Invest heavily in node health, packet QA, trust scoring, and explanation of
uncertainty.

## Debate 10: hazard-specific engines vs one unified safety engine

Version pressure: `cross-version`

Affected objects:
- derived parcel condition
- derived operational status
- explanation record

### Why it matters

Smoke, flood, and heat do not behave the same way, but users still need a
coherent system experience.

### What the hazard-specific side gets right

- better scientific honesty
- different evidence scales and update rates are respected
- different failure modes can be handled more cleanly
- each hazard can evolve on its own schedule

### What the unified side gets right

- simpler user experience
- easier communication of an overall situation
- fewer disjoint product surfaces

### Risk if overdone

If hazard-specific logic is too fragmented, the product may feel inconsistent or
hard to navigate.

If unified safety is overdone, the system may collapse important distinctions
into a vague generic risk score.

### Provisional project stance

Keep hazard engines distinct.
Allow them to feed a shared parcel state surface and shared action-oriented
outputs.
Do not force one generic number to carry all meanings.

## Debate 11: current conditions vs forward-looking prediction

Version pressure: primarily `v1.0`

Affected objects:
- public context
- derived parcel condition
- derived operational status
- explanation record

### Why it matters

Users care about what is true now, but often also need to know what is likely
soon.

### What the current-conditions side gets right

- easier to validate
- better aligned with early sensing and explanation
- lower speculative risk
- more suitable for MVP trust-building

### What the prediction side gets right

- better supports real decisions and preparation
- can make the system more operationally useful
- is especially relevant for runoff, heat, and route degradation

### Risk if overdone

If the system moves into forecasting too early, it may stack uncertainty on
uncertainty.

If the system stays only present-tense forever, it may underdeliver on the
practical decisions users actually need to make.

### Provisional project stance

Start with current conditions and recent change.
Add near-term outlooks only after the evidence, explanation, and confidence
model are strong enough to support them.

## Debate 12: route safety vs on-parcel safety

Version pressure: strongest in `v1.0`

Affected objects:
- parcel
- route and infrastructure segment
- derived parcel condition
- derived operational status

### Why it matters

A parcel can be locally acceptable while access, escape, or surrounding
infrastructure becomes unsafe.

### What the on-parcel side gets right

- keeps the system anchored to the home
- supports straightforward local sensing and explanation
- fits the parcel operator's immediate mental model

### What the route side gets right

- movement and access often determine real safety
- parcel safety without route awareness can be dangerously incomplete
- utilities, roads, and low points may be the decisive operational factors

### Risk if overdone

If the system remains too on-parcel, it may imply safety where practical
mobility is degrading.

If route logic dominates too early, the MVP may become too complex for the
initial build.

### Provisional project stance

Treat route and access as a core secondary layer, not as an optional
afterthought.
Parcel outputs should eventually distinguish on-parcel condition from movement
and access condition.

## Debate 13: monolith vs modular federation

Version pressure: `cross-version`

Affected objects:
- packet schema
- normalized observation
- parcel
- derived parcel condition
- sharing policy

### Why it matters

The project includes hardware, ingest, inference, dashboards, governance, and
open-source documentation across multiple workstreams.

### What the monolith side gets right

- easier to reason about early integration
- fewer moving parts for MVP
- simpler development setup at the beginning

### What the modular side gets right

- matches the staged hardware and software roadmap
- easier to evolve and reuse subprojects
- better alignment with open-source and educational goals
- prevents early lock-in to one giant system

### Risk if overdone

If everything becomes one tightly coupled application, future reuse and
governance flexibility may suffer.

If modularity is taken too far too early, the project may become over-abstracted
and slow to build.

### Provisional project stance

Build a coherent MVP slice, but preserve modular boundaries between hardware
packets, ingest, inference, governance, and presentation.
Favor modular architecture without premature fragmentation.

## Debate 14: user-facing simplicity vs explanation depth

Version pressure: `v0.1` now

Affected objects:
- explanation record
- parcel view
- evidence summary
- derived operational status

### Why it matters

The project wants explanation and provenance, but users still need fast,
understandable answers.

### What the simplicity side gets right

- people need clarity in stressful moments
- less UI clutter improves usability
- action matters more than technical detail for most users most of the time

### What the explanation side gets right

- trust requires inspectability
- uncertainty and source mix matter
- parcel operators should be able to challenge the system when needed

### Risk if overdone

If simplicity dominates, the product may hide the very details that make it
trustworthy.

If explanation dominates, the product may overwhelm people and undermine
actionability.

### Provisional project stance

Use layered explanation.
Show summary first, reasons second, deeper provenance third.
Keep the trust model visible without making every screen read like a lab
notebook.

## Debate 15: partial adoption truthfulness vs network optimism

Version pressure: `v0.1` now

Affected objects:
- public context
- shared neighborhood signal
- derived parcel condition
- explanation record

### Why it matters

The system is explicitly meant to work under partial adoption, but sparse
participation can limit what shared inference can honestly claim.

### What the truthfulness side gets right

- sparse coverage should lower confidence
- some conditions cannot be estimated precisely with little local evidence
- weak coverage should remain visibly weak

### What the optimism side gets right

- the project should still provide value before full participation exists
- priors plus public context plus small numbers of nodes can still be useful
- if the early experience is too weak, adoption may never grow

### Risk if overdone

If truthfulness is handled poorly, the system may feel empty or defeatist under
sparse adoption.

If optimism is handled poorly, the project may make speculative claims that
damage trust.

### Provisional project stance

Design for useful partial adoption, but make coverage and evidence strength
explicit.
The system should still answer under sparse participation, but with visible
confidence and clear explanation of what is missing.

## Debate 16: open-source commons vs controlled stewardship

Version pressure: `cross-version`

Affected objects:
- sharing policy
- explanation record
- packet schema
- neighborhood shared aggregate

### Why it matters

The project aims to be open-source-ready and commons-protective, but shared
environmental systems also need quality control, contribution rules, and
governance discipline.

### What the open side gets right

- aligns with the project's public-interest goals
- supports reproducibility and adaptation
- avoids unnecessary enclosure of useful civic technology

### What the controlled stewardship side gets right

- protects quality and trust
- prevents low-quality or misleading contributions from polluting shared layers
- supports governance, moderation, and data policy enforcement

### Risk if overdone

If openness is naive, the platform may struggle to defend quality and
legitimacy.

If control is overdone, the project may recreate the centralized structures it
is trying to challenge.

### Provisional project stance

Keep the technical and documentation base open where practical.
Use governance, contribution standards, and clear provenance to protect quality
rather than defaulting to closed control.

## Debate 17: local parcel observation vs multi-scale climate roadmap

Version pressure: `cross-version`, strongest at `v1.0` and beyond

Affected objects:
- public context
- parcel prior
- derived parcel condition
- explanation record
- shared neighborhood signal

### Why it matters

The project's real-time inference uses local sensor readings and near-real-time public context (NWS, AirNow, NOAA HMS). But the program's long-term value depends on connecting those readings to **multi-decadal climate information** — climate normals (NCEI 30-year), regional adaptation plans (state and county), long-horizon scenarios (IPCC RCPs, NOAA climate projections), and vulnerability overlays (CDC Heat Vulnerability Index, FEMA future-flood projections, Cal Fire WUI maps). That comparison is **not** what the v1 hazard formula's divergence channels do today. Divergence channels compare the moment; climate roadmaps describe the trajectory.

Four structural differences that don't yet have architectural homes:

- **Spatial aggregation** — parcel (meters) → tract → county → HUC watershed → climate region. No explicit ladder today.
- **Temporal alignment** — real-time reading vs. 30-year normal vs. decadal trend vs. 2050 projection. Each has different uncertainty shapes.
- **Scenario bearing** — climate projections are conditional on emission scenarios (RCP 4.5 vs 8.5), not "truth."
- **Purpose divergence** — local readiness, regional planning, and adaptation-investment targeting each need the same data treated differently.

### What the local-primary side gets right

- local sensor is what the parcel operator can verify
- matches parcel-first doctrine (debate 1)
- avoids overclaim based on coarse regional projections
- respects the sensor-primary architectural commitment in the v1 hazard formula

### What the roadmap-primary side gets right

- most decisions about adaptation happen at planning horizons, not event horizons
- local trajectory is the information most communities actually lack
- pairing parcel data with climate roadmap is the distinctive long-term value proposition
- without it, OESIS remains "another sensor product"

### Risk if overdone

If local-primary is overdone, OESIS never bridges from real-time readings to the scenario and adaptation layer — it stays a sensing product without the climate-intelligence dimension.

If roadmap-primary is overdone, OESIS starts making 2050-scenario claims based on a single parcel's bench-air readings — confidence theater at geologic timescale.

### Provisional project stance

Preserve the v1 formula's sensor-primary posture for real-time inference. Treat climate-roadmap context as a **separate, explicit output layer** with its own confidence model and its own admissibility rules — not as an additional term in the hazard-probability log-odds. When roadmap context is displayed alongside parcel-state, it should be presented as "trajectory" or "planning context," not as additional evidence for the current-hazard call.

This debate is **open** — it will require a dedicated design document when the architectural work begins. Likely new program-level doc (sibling to `calibration-program.md` / `adapter-trust-program.md`): something like **scenario-context-program.md** covering source authorities (NCEI, FEMA, CDC, IPCC, state plans), temporal alignment rules, spatial aggregation ladder, and the scenario-vs-observation distinction.

Related existing hooks: `architecture/system/architectural-choices-by-stage.md` (per-phase choice table; could eventually add a "scenario context tier" column), `sensor-placement-and-representativeness-guide.md` (placement representativeness already thinks in spatial scale), `adapter-trust-program.md` §A (source authority pattern likely transfers).

## Debate 18: standardized OESIS contract vs ecosystem-native IoT adaptation

Version pressure: `v1.5` and beyond; begins biting as adapter surfaces enter scope

Affected objects:
- normalized observation
- equipment-state observation (v1.5 bridge)
- adapter source authority
- packet schema
- sharing policy
- admissibility decision

### Why it matters

The adapter-trust program handles **single-source** cloud-API adapters cleanly: Ecobee, Nest, Sensibo — one OAuth flow, one pinned API contract, one source authority. It does not yet handle:

- **Local-network ecosystems** — Matter, Thread, Zigbee, Z-Wave, Apple HomeKit, Google Home, SmartThings. Each is a hub-rooted protocol with device discovery, not a cloud API.
- **Building protocols** — BACnet, Modbus TCP, LonWorks for commercial and multi-unit. Controller-rooted, not cloud.
- **Utility AMI** — smart meters over multiple vendor protocols (Itron, Landis+Gyr, etc.), often retrospective-only access.
- **Consumer environmental** — PurpleAir, Davis, Ambient Weather, Tempest. Each with different API, quality, and privacy posture.
- **Personal health / wearables** — Apple HealthKit, Google Fit, Fitbit. Very different consent model.
- **Energy monitors** — Sense, Emporia, Shelly, TP-Link beyond the Tier 3 circuit-monitor path.

Three sub-problems:

- **Protocol adaptation** — how does OESIS speak to each ecosystem?
- **Semantic normalization** — what does "HVAC mode" mean across Ecobee / Nest / BACnet / Matter / generic smart thermostat? A canonical vocabulary is needed.
- **Multi-source trust composition** — if three adapters all report HVAC state, how are they reconciled? Adapter-trust §C handles per-source admissibility; multi-source fusion is distinct.

### What the standardized-contract side gets right

- one canonical data model keeps inference stable as adapters proliferate
- semantic alignment prevents "HVAC mode" drift across sources
- supports multi-source fusion rules in one place
- preserves the "one parcel, one contract" architectural commitment
- simpler governance — fewer variable surfaces to audit

### What the ecosystem-native side gets right

- every ecosystem that loses to OESIS's preferred model is an ecosystem OESIS can't integrate
- users don't replace their Matter hub to accommodate OESIS
- building owners don't rewrite their BACnet stack
- adaptation-layer thinness is what makes open-source projects interoperate in the real world
- matching the Matter data model where it already covers a concept avoids reinventing vocabularies

### Risk if overdone

If standardized-contract is overdone, OESIS becomes an isolated stack that requires users to leave their existing IoT investments behind — the opposite of useful partial adoption (debate 15).

If ecosystem-native is overdone, OESIS loses its coherent inference story; "HVAC mode" means three different things in three different observations depending on which adapter produced them.

### Provisional project stance

Treat the canonical OESIS observation schema as the **target normalization**, and design adapters as **translators** from each ecosystem's native vocabulary into it. Where a canonical OESIS concept has a clear equivalent in a major standard (Matter, BACnet, CTA-2045), align the name and semantics deliberately. Where it doesn't, declare an OESIS-internal name with a mapping table.

Three concrete implications:

- Semantic vocabulary becomes a **separate architectural surface**: a canonical names document mapping internal OESIS concepts to each external ecosystem. Not yet written.
- Adapter-trust §F gains an **ecosystem family** dimension above individual source authority: "this adapter is Matter-compatible" vs. "this adapter is Ecobee-v1-API-specific." Allows whole families to upgrade posture at once.
- Multi-source fusion needs its own rule: preference order (Tier 3 direct > Tier 2 cloud > Tier 1 passive), confidence stacking, and per-measurand reconciliation policy.

This debate is **open** — requires a dedicated design doc when the architectural work begins. Likely candidate: **semantic-vocabulary.md** or **iot-integration-standards.md** at the `system/` layer, coupled with an extension to `adapter-trust-program.md` §F introducing the ecosystem-family concept.

Related existing hooks: `node-taxonomy.md` tiered acquisition model (Tier 1/2/3 is the starting structure; ecosystem family lives above tier), `adapter-trust-program.md` §A source-authority schema (adapts to multi-ecosystem), `architecture/system/architectural-choices-by-stage.md` (could eventually add ecosystem-alignment row).

## Cross-cutting decision rules

When a new design question appears, test it against these checks:

1. Does it make parcel outputs more useful without pretending to know more than
   the system knows?
2. Does it preserve the distinction between private owner data, shared data,
   public data, and derived states?
3. Does it improve standalone value, network value, or both?
4. Does it preserve explanation, confidence, and evidence mode?
5. Does it keep the system modular enough to evolve without becoming
   fragmented?
6. Does it improve parcel operator agency rather than weakening it?

## Current meta-stance

The project should currently bias toward:

- practical MVP truth over conceptual grandiosity
- rules-first explanation over opaque cleverness
- modularity over monolith lock-in
- privacy by default over incidental exposure
- useful partial adoption over all-or-nothing dependency
- parcel operator value first, with neighborhood intelligence growing on top

## Likely next decisions to formalize

The following debates are likely to need companion doctrine or ADR documents
next:

1. local-first vs cloud-first processing boundary
2. exact owner data vs shared derived contribution schema
3. hazard engine interface design
4. route safety model scope for MVP
5. pilot governance and quality thresholds for shared map visibility
6. scenario-context-program for multi-scale climate-roadmap integration (debate 17) — likely sibling to `calibration-program.md` and `adapter-trust-program.md`
7. semantic-vocabulary and ecosystem-family concept for IoT standardization (debate 18) — likely extension of `adapter-trust-program.md` §F plus a new canonical names document

## How to use this file for frontier architectural questions

Debates 17 and 18 are **frontier questions** — architectural design problems large enough to warrant dedicated design work, but not yet being actively designed. The pattern they establish:

- **Frame the tension** with both sides doing justice (the "what each side gets right" sections).
- **Name what structurally differs** from what the current architecture already handles, so a future reader doesn't assume existing programs cover the frontier.
- **Identify likely architectural hooks** — the existing docs that will be extended or the new docs that will likely need creation.
- **Record provisional stance** — what the program will currently act on while the full design is pending.
- **Add a numbered entry to "Likely next decisions to formalize"** so the frontier is visible from a single list.

A frontier question belongs in this file (not in the gap register, not in an ADR) when:

- it will require dedicated design work rather than a single-step remediation (gap register);
- it is not yet decided (ADR);
- it is cross-version in nature (operates across program phases);
- losing track of it would force future contributors to rediscover the same concerns.

When a frontier question is ready to be designed, it either (a) gets a dedicated program doc at the `system/` layer, (b) becomes an ADR if the decision is narrow and crisp, or (c) gets split into concrete gap-register entries with named remediation paths. The debate entry stays in place as the frame for future readers; the design doc, ADR, or gaps are what move the work forward.
