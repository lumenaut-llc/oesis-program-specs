# Sensor Placement and Representativeness Guide

## Purpose

Define how sensor placement affects truthfulness, confidence, and hazard observability so the product does not over-interpret poorly placed devices.

## Why placement matters

Most errors in a home resilience system will not come only from bad models.
They will also come from:

- sensors in the wrong place
- sensors in overly local micro-environments
- users assuming all sensors represent the whole parcel equally

Placement is therefore part of the inference system.

## Core principle

The product should never assume that a sensor is fully representative just because it is functioning.

Every placement should be interpreted along two dimensions:

- what it can observe well
- how representative it is of the home, parcel, or shared neighborhood layer

## Placement categories

### Indoor

Typical examples:

- bedroom
- living room
- office
- hallway

Strengths:

- good for indoor air burden
- good for indoor heat and cold burden
- useful for shelter readiness

Weaknesses:

- weak proxy for parcel-wide outdoor conditions
- weak for flood unless tied to specific intrusion detection
- weak for shared neighborhood intelligence by default

### Sheltered

Typical examples:

- covered porch
- garage-adjacent sheltered space
- breezeway
- eave-protected exterior wall

Strengths:

- can provide some local outdoor-like context
- often useful for transition conditions

Weaknesses:

- may be biased by walls, roofs, radiant surfaces, and enclosure effects
- should not be treated as fully outdoor truth

### Outdoor

Typical examples:

- open yard mount
- mast
- roofline with appropriate exposure
- dedicated low-point installation for flooding

Strengths:

- best candidate for parcel outdoor context
- most useful for shared block intelligence if siting is good

Weaknesses:

- can still be distorted by sun, walls, pavement, or direct runoff peculiarities
- requires better calibration and siting discipline

## Deployment-class mapping

Placement category determines the deployment class a node must be built to, which in turn determines power / IP / transport tier per [`deployment-maturity-ladder.md`](deployment-maturity-ladder.md) "Deployment-class standards". This table is the canonical link between placement language here and deployment-class language there:

| Placement category | Required deployment class | Power tier | IP tier | Transport floor |
| --- | --- | --- | --- | --- |
| Indoor | indoor | USB from protected supply | none / IP20 | serial (v0.1 floor); Wi-Fi / wired LAN permitted |
| Sheltered | sheltered | 12 V-DC from outdoor-rated adapter, or USB if within an enclosed space | IP44 | serial; Wi-Fi where coverage is reliable; LoRa permitted |
| Outdoor | outdoor | Battery + solar with documented runtime floor, or mains with outdoor-rated PSU routed through conduit | IP54 (passive) / IP65+ (exposed mast) | serial during bring-up only; Wi-Fi where coverage is verified; LoRa or cellular for parcels beyond Wi-Fi reach |

A node whose declared deployment class does not match its physical installation class produces readings that are inadmissible to the calibration dataset per [`calibration-program.md`](calibration-program.md) §C item 3. This is the enforcement link between placement discipline and admissibility.

## Representativeness classes

The product should classify placement representativeness explicitly.

### Class A: Broadly representative for intended hazard

Example:

- well-sited outdoor air sensor for local smoke trend

### Class B: Partially representative

Example:

- sheltered porch sensor that gives useful but biased outdoor cues

### Class C: Highly localized

Example:

- indoor bedroom sensor near a window or vent

### Class D: Unsupported or misleading for the target interpretation

Example:

- indoor temperature sensor treated as parcel-wide outdoor heat truth

## Hazard-specific placement guidance

### Smoke and air

Best placements:

- dedicated outdoor air-quality sensing for parcel and shared context
- indoor sensing for shelter and indoor burden

Watchouts:

- indoor PM is not the same as outdoor smoke burden
- sheltered outdoor placement may lag or dampen plume behavior

### Heat

Best placements:

- indoor living-space measurements for shelter burden
- properly exposed outdoor measurements for parcel heat context

Watchouts:

- direct sun, attic heat, garage heat, and wall exposure can create false heat severity

### Flood and runoff

Best placements:

- documented low-point sensors
- known runoff pathways
- sump and intrusion sensors for home-specific conditions

Watchouts:

- one dry point on a parcel does not clear the whole parcel
- one wet point may reflect an intended drainage concentration rather than generalized flooding

### Freeze

Best placements:

- exposed pipe-adjacent or cold-zone sensors for freeze risk
- indoor living-space sensors for cold burden

Watchouts:

- central indoor readings can hide freeze-prone edge conditions

### Wind

Best placements:

- elevated outdoor siting with known exposure

Watchouts:

- yard fences, buildings, and tree cover can distort readings dramatically

## Day-one product posture

The phase-1 product should likely assume:

- indoor sensors are highly valuable for home readiness
- indoor sensors are weak for shared neighborhood hazard truth
- outdoor-capable shared intelligence requires more disciplined siting

## Setup requirements

The setup flow should capture at minimum:

- indoor, sheltered, or outdoor mode
- placement type
- approximate height class
- obvious nearby bias factors if known

Examples of bias factors:

- near window
- near HVAC vent
- near pavement
- under eave
- low-point drain area
- against sun-facing wall

## Product behavior implications

### Confidence

Confidence should degrade when:

- placement is weak for the target hazard
- placement is highly localized
- placement quality is unknown

### Recommendation scope

Recommendations should become more general when representativeness is weak.

### Shared-layer eligibility

Not every sensor should contribute equally to neighborhood intelligence.

Shared-layer participation should depend partly on:

- hazard fit
- placement quality
- freshness
- health

## Pilot guidance

During pilots, the team should document:

- where each sensor was placed
- what it was expected to represent
- what it actually appeared to represent during events

## Failure modes to avoid

- treating all connected sensors as equally trustworthy
- silently upgrading indoor readings into parcel truth
- letting poor siting create false neighborhood gradients

## Sensor variant selection principles

When a sensor family ships in multiple variants (for example filtered vs unfiltered SHT45, or BME680 vs BME688), the choice of variant is not cosmetic. It must follow from the placement category the node will occupy and the measurand's tolerance requirements. The rules below are platform-level; specific variant part numbers live in each node's build spec.

### Variant selection is driven by placement, not the reverse

Placement decides the environmental envelope the sensor must tolerate. The sensor variant must be rated for that envelope before the node is spec'd. Picking the variant first and then discovering it cannot survive the intended placement produces field failures that cannot be corrected in software.

### Required minimum tolerances by placement category

| Placement category | Operating-temperature range | Humidity / condensation | Contamination |
|---|---|---|---|
| Indoor | Typical HVAC envelope, 10–35 °C | Non-condensing; standard variants acceptable | Dust from HVAC circulation; PTFE or membrane filter recommended near returns |
| Sheltered | −10 to 50 °C depending on climate zone | Occasional condensation; PTFE or equivalent membrane filter required | Pollen, spider ingress, insect nest risk; enclosure membrane venting required |
| Outdoor | Full local climate envelope, documented per parcel's climate zone | Condensation routine; sintered cap or equivalent protective fixture required | UV, salt (coastal), pollen, ember exposure (WUI), precipitation |

A variant must be rated for the full envelope at the placement category it serves. Nodes deployed outside a sensor's rated envelope produce readings whose accuracy is unbounded; such readings are inadmissible under [`calibration-program.md`](calibration-program.md) §C.

### Accuracy-tier requirements driven by formula sensitivity

The hazard formula's coefficient sensitivity determines the accuracy floor a sensor variant must satisfy for its measurand to be admissible.

Current requirements inferred from [`../../software/inference-engine/hazard-formula-v1.md`](../../software/inference-engine/hazard-formula-v1.md) and [`hazard-formula-v1-phase1.md`](../../software/inference-engine/hazard-formula-v1-phase1.md):

| Measurand | Accuracy floor for admissibility | Rationale |
|---|---|---|
| Temperature (any placement) | ±0.3 °C or better across the operating range | The heat sensor term z-scores against climate-normal σ, which is typically 1–3 °C; a ±0.3 °C sensor is well inside that noise floor. Larger error would dominate the z-score. |
| Relative humidity | ±3 % RH or better | Required for optional heat index / WBGT correction and for condensation-event detection |
| Gas resistance (VOC trend) | No absolute accuracy floor; per-device rolling baseline is what the formula consumes | Repeatability and noise are what matter, not absolute ohms. Stability is gated by the burn-in policy in `calibration-program.md` §B |
| PM2.5 | Accuracy floor TBD per sensor family when a PM-capable node lands | Not required for current hardware lanes |

### Cost and availability

Cost and availability are documented in the node build spec, not here. The platform policy requires that a chosen variant be: (a) sourceable at pilot scale, (b) replacement-compatible across revisions of the node family, and (c) retained as a line item in the `oesis-builds` BOM until explicitly retired. A variant that is temporarily unavailable is not a reason to drop to a lower-accuracy variant; it is a reason to pause deployment of that node family until the variant or an approved equivalent is back in stock.

### Substitutions and equivalents

Any substitution of a sensor variant (e.g., BME680 → BME688, or SHT45 → SHT45-AD1B to -AD2B) is a build decision that must be recorded in an `oesis-builds/decisions/<node>/` entry, and the substitution is valid only after the replacement's accuracy and envelope are verified against the standards above. A substitution cannot reduce the tolerance envelope or accuracy floor without a new calibration session and an update to the node's deployment-maturity posture.

## Open questions

- Which placement fields most improve interpretive quality?
- When should the product ask a user to move a sensor rather than simply degrade confidence?
