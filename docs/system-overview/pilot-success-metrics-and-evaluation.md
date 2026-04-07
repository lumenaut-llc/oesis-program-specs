# Pilot Success Metrics and Evaluation

## Purpose

Define how to evaluate early pilots of Open Environmental Sensing and Inference
System so the team can distinguish:

- technical capability
- user trust
- product usefulness
- network-effect lift
- governance and privacy fit

## Why this matters

A resilience product can fail even if sensors work.

Early pilots need to answer:

- Did the system help people make better sense of conditions?
- Did users trust the output enough to act on it?
- Did neighbor participation measurably improve usefulness?
- Did the privacy posture feel acceptable?

## Pilot layers

### Layer 1: Home-only evaluation

Tests whether one home gets meaningful value without neighborhood participation.

### Layer 2: Block-effect evaluation

Tests whether nearby participation creates measurable improvement over home-plus-public-only interpretation.

### Layer 3: Governance evaluation

Tests whether sharing controls, consent, and visibility boundaries remain understandable and acceptable.

## Primary pilot questions

1. Is the product useful on ordinary days, not only during major disasters?
2. Does the system become noticeably better with nearby participation?
3. Are recommendations understandable and appropriately cautious?
4. Are uncertainty and limitations visible enough?
5. Do users feel helped rather than surveilled?

## Core metric categories

### A. Technical validity

Measure:

- sensor uptime
- freshness
- read failure rates
- packet completeness
- alert delivery timeliness
- consistency between observed conditions and produced state changes

Example metrics:

- percentage of valid observations per device-day
- median latency from observation to user-visible state update
- percentage of state outputs with usable freshness and confidence data

### B. Home-level usefulness

Measure:

- how often users open the product during meaningful conditions
- whether users understand the current state
- whether recommendations are considered useful
- whether alerts feel timely and relevant

Example metrics:

- recommendation-card open rate during elevated events
- percent of users who can correctly explain why a state was shown
- user-reported usefulness during routine and elevated conditions

### C. Recommendation quality

Measure:

- actionability
- perceived helpfulness
- perceived overreach
- contradiction or confusion rate

Example metrics:

- percent of recommendations rated understandable
- percent of recommendations rated too vague
- percent of recommendations rated too authoritative

### D. Trust and explainability

Measure:

- whether users trust the output
- whether users understand uncertainty and evidence mode
- whether users can distinguish official alerts from system suggestions

Example metrics:

- confidence comprehension score from pilot interviews
- percent of users who can identify what was directly observed versus inferred

### E. Network-effect lift

Measure:

- whether nearby participation improves accuracy, timeliness, or perceived usefulness
- whether users find the shared layer meaningfully better than public-only context

Example metrics:

- time-to-local-awareness improvement over public-only context
- percent of users reporting that block participation provided earlier warning
- number of useful block-level differences detected that were not visible in regional feeds

### F. Privacy and governance fit

Measure:

- whether users understand what is shared
- whether sharing controls feel reversible and bounded
- whether participants feel socially pressured or surveilled

Example metrics:

- percent of participants who can correctly describe their sharing mode
- privacy-comfort rating
- number of revocation or sharing-adjustment actions taken

## Suggested pilot scenarios

### Scenario 1: Everyday value

Goal:

- test whether users get value outside acute disasters

Focus:

- indoor air
- daily ventilation guidance
- heat comfort
- outage readiness checks

### Scenario 2: Elevated smoke event

Goal:

- test smoke burden, recommendations, and block-level trend value

Focus:

- indoor versus outdoor divergence
- public-context corroboration
- neighbor-amplified local awareness

### Scenario 3: Heavy rain or runoff event

Goal:

- test low-point detection and route readiness interpretation

Focus:

- parcel-level runoff
- block trouble spots
- difference between uphill and downhill parcels

### Scenario 4: Heat event

Goal:

- test indoor heat burden and overnight recovery signals

Focus:

- room or parcel shelter stress
- block-level nighttime heat persistence

### Scenario 5: Outage event

Goal:

- test utility readiness and local outage clustering

Focus:

- household readiness
- distinction between isolated home issues and neighborhood outage

## Recommended evaluation methods

### Quantitative

- observation and uptime logs
- state-transition logs
- alert-trigger logs
- response-latency logs
- participation density and coverage metrics

### Qualitative

- post-event interviews
- structured pilot diaries
- recommendation reviews
- privacy and trust surveys
- scenario debriefs

### Comparative

Compare:

- home-only versus home-plus-public
- home-plus-public versus home-plus-block
- private view versus shared block view

## Suggested success thresholds

These are starting points, not final commitments.

### Home-only success

- most pilot homes report value during both routine and elevated conditions
- users can explain current state and next-step suggestions in plain language
- alert fatigue remains acceptable

### Block-effect success

- participants can name at least one way nearby participation improved understanding
- block layer surfaces meaningful local variation not obvious in public feeds alone
- users continue participating after seeing what the shared layer reveals

### Governance success

- most participants understand what is being shared
- revocation and consent changes are understandable
- participants do not report generalized neighborhood-surveillance discomfort

## Failure signals

- users only find value during rare major events
- recommendations are perceived as obvious or untrustworthy
- shared intelligence adds little beyond public context
- participants misunderstand sharing scope
- sensor issues silently degrade trust
- low-confidence outputs appear too authoritative

## Open questions

- Which metrics should be considered launch-gating versus exploratory?
- What is the right balance between user interviews and observational product analytics?
- How should block-level value be measured in low-frequency hazard seasons?
