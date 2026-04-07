# Home and Parcel Context Capture Standard

## Purpose

Define the minimum contextual information the system should capture about a home, parcel, and installation so sensor readings can be interpreted more honestly.

## Why context matters

The same sensor reading can mean very different things depending on:

- whether the sensor is indoors or outdoors
- whether the parcel is uphill or at a drainage low point
- whether the home is shaded or highly exposed
- whether the sensor sits in a representative location

Without context capture, the product risks turning local micro-readings into misleading parcel conclusions.

## Design principles

- capture the smallest set of context that materially improves interpretation
- prefer structured fields over free text where practical
- make sensitive fields optional unless truly necessary
- distinguish parcel context from sensor-installation context
- allow later refinement instead of forcing perfect setup on day one

## Context categories

### 1. Installation context

These fields describe where and how a sensor is placed.

Minimum fields:

- installation mode: indoor, sheltered, outdoor
- approximate placement type: living space, garage, attic, exterior wall, porch, yard, roofline, low point
- height class: floor level, table level, wall level, elevated outdoor, ground-near low point
- representativeness self-assessment: typical, somewhat localized, highly localized

Why it matters:

- determines what hazards the sensor can credibly inform
- improves confidence and recommendation quality

### 2. Structure context

These fields describe relevant home characteristics.

Minimum fields:

- structure type: detached, attached, multi-unit, mobile, other
- primary occupancy type: owner occupied, renter occupied, mixed, other
- conditioned or unconditioned relevant spaces if known
- backup power available: yes, no, unknown
- HVAC or filtration available: yes, no, unknown

Useful later fields:

- cooling type
- heating type
- window AC presence
- whole-home filtration capability
- known vulnerable rooms or zones

Why it matters:

- affects how recommendations should be phrased
- affects what protective actions are realistic

### 3. Parcel context

These fields describe the parcel and its immediate site conditions.

Minimum fields:

- parcel identifier
- basic slope posture: uphill, mid-slope, flat, low point, unknown
- drainage tendency: well-drained, mixed, poor-drainage, unknown
- sun exposure posture: shaded, mixed, exposed, unknown
- route/access posture: multiple exits, limited exits, constrained access, unknown

Useful later fields:

- parcel geometry cues
- surface cover cues
- defensible-space or vegetation cues
- adjacency to drainage channels or culverts

Why it matters:

- improves flood, heat, route, and wildfire-readiness interpretation

### 4. Hazard-specific site notes

Optional structured notes that materially affect risk interpretation.

Examples:

- known basement or crawlspace flooding history
- chronic smoke intrusion through a known side of the home
- recurring wind exposure from a corridor
- frequent power instability
- known icy driveway or access conditions

Why it matters:

- allows the product to tailor recommendations and expectations

### 5. Household sensitivity and priority context

Optional fields that personalize guidance without being required for baseline operation.

Examples:

- medically sensitive occupant present
- elder-care context
- young children present
- limited mobility considerations
- high outage sensitivity

Why it matters:

- helps prioritize recommendation types and alert severity

## Minimum day-one setup set

The first setup flow should probably require only:

- installation mode
- placement type
- parcel identifier or address linkage
- basic slope or drainage posture
- sun exposure posture
- backup power available
- HVAC or filtration available

Anything more demanding should be optional or progressive.

## Capture posture

### Structured first

Use bounded choices where possible so the inference layer can reason on them.

### Progressive disclosure

Ask only what is necessary at initial setup.
Collect additional context later when:

- the user wants better recommendations
- a hazard event reveals missing information
- a more advanced feature is enabled

### Revise over time

Users should be able to update context as:

- sensors move
- seasons change
- hardware changes
- the home is retrofitted

## Relationship to confidence

Missing context should not silently be treated as neutral truth.

Instead:

- confidence should degrade where missing context matters
- recommendations should become more generic where context is incomplete
- unsupported parcel claims should remain weaker

## Example context-driven differences

### Example 1: Heat

Same indoor temperature, different context:

- shaded, insulated home with working cooling
- exposed upper-floor room with weak cooling

These should not receive identical recommendations or confidence.

### Example 2: Flood

Same rainfall, different parcel context:

- uphill parcel with good drainage
- low-point parcel near a known runoff path

These should not receive identical flood-readiness outputs.

### Example 3: Smoke

Same particulate reading, different installation:

- indoor bedroom sensor
- outdoor sheltered porch sensor

These should not be treated as equally representative of parcel-wide outdoor smoke burden.

## Data handling notes

- sensitive context should remain private by default
- only the minimum derived context needed for shared intelligence should leave the household context boundary
- users should be able to review and correct stored context

## Open questions

- Which context fields deliver the highest improvement per setup minute?
- Which parcel fields should be user-entered versus inferred from public datasets later?
- How should the product distinguish confident inferred context from user-confirmed context?
