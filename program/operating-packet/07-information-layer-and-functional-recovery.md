# Information layer and functional recovery

**Canonical incorporation:** Information-layer and recovery framing → [`architecture/system/vision-and-use-cases.md`](../../architecture/system/vision-and-use-cases.md) and [`architecture/v1.0/proposed-architecture.md`](../../architecture/v1.0/proposed-architecture.md). This file keeps the full formulation.

## Best approach

The best approach is not to build the biggest sensor network.
It is to build the best evidence-to-impact system.

For this project, the best information layer should optimize four things at once:

- measurement accuracy
- local recency
- spatial relevance
- decision usefulness

## Evidence hierarchy

Treat every input as one of these:

- direct local observation
- nearby shared observation
- external public observation
- modeled or inferred state
- verified impact or outcome

## Critical distinction

Explicitly separate observed conditions from validated impacts.

Examples:

- smoke concentration is an observed or inferred condition
- road closure is an impact state
- power loss is an impact state
- shelter degradation is an impact state

## Data assimilation posture

Think in terms of a continuously updated state estimate, not just sensor feeds plus a rules engine.

For each parcel, route segment, or shared cell, the system should maintain:

- current state value
- uncertainty
- freshness
- supporting evidence mix
- likely next-state direction

## Timing integrity

Treat these as first-class quality dimensions:

- when was it measured
- when was it transmitted
- when was it ingested
- when was it fused into the current state
- how long does this observation remain decision-relevant

## Functional state objects

The system should move beyond hazard status into functional state objects such as:

- route passability
- shelter viability
- clean-air refuge viability
- cooling refuge viability
- drainage function
- power continuity
- communications continuity
- potable water continuity

## Lifelines and dependencies

Add lifeline and dependency thinking sooner rather than later.

Examples:

- transportation dependence
- energy dependence
- communications dependence
- drainage dependence
- water dependence
- cooling and refuge dependence

## Social vulnerability in community layers

Social vulnerability should not drive private parcel inference directly, but it should shape neighborhood and infrastructure prioritization.

## Active sensing and value-of-information logic

Do not just ask where a sensor is missing.
Ask where one more sensor most improves the state estimate for parcels, routes, or lifelines.

## Functional recovery intelligence

This is the most important undernamed concept.

Not just:

- what is the hazard?
- what is the parcel status?

But:

- what critical functions are impaired?
- what dependencies matter?
- what is degrading?
- what is the expected path to recovery?

## Best summary sentence

If the goal is the best possible information layer for disaster relief and climate resilience, the right target is the best continuously updated, uncertainty-aware estimate of environmental conditions, functional impacts, and recovery-critical dependencies across parcels, routes, and community lifelines.

## Related

Phase-by-phase object split (**hazard state**, **functional state**, **response state**): [`functional-state-and-response-model.md`](functional-state-and-response-model.md).
