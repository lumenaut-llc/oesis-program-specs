# Recommendation Engine and Safety Language

## Purpose

Define how the product should present recommendations, warnings, and safety-oriented guidance without overstating certainty or drifting into unsupported emergency-command behavior.

## Why this matters

Recommendation language is part of the product, not just a legal afterthought.

The same underlying sensor state can be:

- useful and trustworthy
- confusing and noisy
- or overly authoritative and risky

The system therefore needs explicit rules for how it speaks.

## Core principle

The product should provide:

- readiness guidance
- protective action suggestions
- situational prompts
- preparation steps

It should not casually present itself as:

- an emergency authority
- a medical authority
- a fire behavior authority
- an evacuation command system

## Language goals

Recommendation text should be:

- specific enough to help
- cautious enough to stay truthful
- tied to evidence mode and confidence
- understandable to non-experts
- calm during stressful conditions

## Recommendation tiers

### Tier 1: Informational

Used when the system sees a condition worth noticing but not an urgent change.

Examples:

- indoor air quality is beginning to worsen
- overnight cooling appears weaker than usual
- localized runoff concern is present near the parcel edge

### Tier 2: Protective action suggestion

Used when evidence is strong enough to justify practical next-step guidance.

Examples:

- close windows
- run filtration
- move activity to the coolest room
- inspect drains and low points
- reduce nonessential power loads

### Tier 3: Escalation prompt

Used when conditions appear materially worse and the system should encourage the user to review plans or official information.

Examples:

- review local official alerts now
- prepare your backup cooling or shelter plan
- reconsider using this route if conditions continue to worsen

### Tier 4: Emergency-adjacent caution

Reserved for cases where the system sees severe local degradation or strong corroboration from public context.

This tier should still avoid pretending to issue authoritative orders unless the product is explicitly relaying an official alert.

Examples:

- conditions affecting route safety appear severely degraded
- official alerts are active for your area; review them immediately

## Evidence-aware language rules

### High-confidence observed local

Allowed posture:

- more specific about what was observed
- more direct about household protective steps

Example:

- indoor particulate levels are rising quickly; close windows and run filtration now if available

### Mixed local plus public

Allowed posture:

- specific about the shared direction of concern
- explicit that public context supports the interpretation

Example:

- local conditions and public smoke context both indicate worsening air burden; reduce outdoor exposure and protect indoor air

### Weak or uncertain evidence

Required posture:

- softer language
- more preparation-focused
- visible uncertainty

Example:

- available evidence is limited, but conditions may be worsening; check your supplies and monitor updates closely

### Unsupported hazard observability

Required posture:

- explicitly say what the system cannot determine well

Example:

- this home setup cannot directly confirm parcel-level flood depth; inspect known low points if safe to do so

## Recommended sentence patterns

Good patterns:

- "Conditions suggest..."
- "Local evidence indicates..."
- "Public context supports..."
- "Confidence is limited because..."
- "Consider taking these steps..."
- "Review official alerts if..."

Avoid by default:

- "You must..."
- "Evacuate now"
- "It is safe"
- "The fire will reach your block in..."
- "This confirms..."

unless the product is explicitly quoting or relaying an official source.

## Hazard-specific guidance boundaries

### Smoke and indoor air

Good guidance:

- close windows
- run air filtration
- use recirculation if available
- reduce outdoor activity
- move to the cleanest room

Watchouts:

- do not imply medical diagnosis
- do not imply exact toxic exposure conclusions from limited sensors

### Heat

Good guidance:

- reduce exertion
- move to cooler rooms
- pre-cool where possible
- close shades or blinds
- prepare backup cooling

Watchouts:

- avoid clinical heat-illness diagnosis language

### Flood and runoff

Good guidance:

- inspect low points
- move vulnerable belongings
- review safer local routes
- prepare existing barriers or pumps

Watchouts:

- avoid definitive route-safety claims without strong corroboration
- avoid encouraging hazardous physical inspection in unsafe circumstances

### Freeze

Good guidance:

- protect exposed pipes
- maintain minimum indoor temperature
- prepare freeze mitigation steps appropriate to the home

Watchouts:

- local climate and plumbing practices vary

### Outage and shelter readiness

Good guidance:

- preserve battery and device charge
- reduce nonessential loads
- check backup resources
- prepare food, water, and communications

Watchouts:

- avoid implying utility restoration certainty

## Official-source relay rule

If the product relays an official alert, it should:

- label the alert source clearly
- distinguish the official alert from the product's own inference
- avoid paraphrasing the alert in a way that changes its meaning

## Recommendation rendering requirements

Each recommendation card should show:

- recommendation text
- why it is being shown
- confidence or evidence note
- freshness note
- whether it is based on local observation, public context, or both

## Accessibility requirements

Recommendation language should be:

- short
- plain-language
- readable under stress
- suitable for voice and notification surfaces

The product should later support:

- multilingual presentation
- caregiver and accessibility-friendly modes
- lower-literacy variants

## Evaluation criteria

- users understand what the system is asking them to consider
- users can distinguish suggestion from official instruction
- low-confidence recommendations still feel useful
- stressful events do not produce confusing or contradictory tone shifts

## Examples

### Strong example

"Indoor air burden is rising quickly and outdoor smoke is also worsening. Close windows and run filtration now if available."

Why it works:

- states observed condition
- ties action to evidence
- stays within household guidance

### Weak-evidence example

"Available evidence is limited, but smoke conditions may be worsening nearby. Prepare to protect indoor air and monitor official updates."

Why it works:

- does not overclaim
- still gives useful preparation guidance

### Bad example

"Your block will become unsafe in 12 minutes. Evacuate immediately."

Why it fails:

- false precision
- unsupported predictive authority
- likely beyond current technical capability
