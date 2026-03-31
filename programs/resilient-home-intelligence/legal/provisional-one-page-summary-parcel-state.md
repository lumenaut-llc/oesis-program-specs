# One-Page Summary: Parcel-State Generation Candidate

## Status

Internal summary for inventor alignment and counsel review.

Do not publish before the filing decision.

## Candidate title

Parcel-level environmental condition generation with source-aware evidence modes

## Short description

This candidate covers a method for generating parcel-level condition outputs for hazards such as smoke, flooding/runoff, and heat by combining parcel-linked local observations, parcel-specific context, and optional public context into a parcel-state snapshot that explicitly reports confidence, freshness, reasons, and an evidence mode identifying what classes of evidence materially supported the result.

## Problem being solved

Regional feeds and raw sensor dashboards do not reliably answer parcel-level questions such as whether conditions for shelter, reentry, egress, or asset risk appear degraded at a specific home. A single parcel often has incomplete information, and the available evidence may come from mixed sources with different quality and directness. The project needs a way to generate parcel-level outputs that remain useful under partial adoption while still making source provenance and uncertainty explicit.

## Why this candidate may matter

- it aims at the parcel-level interpretation layer rather than just data collection
- it distinguishes between direct local observation and public-context-supported inference
- it degrades confidence and can return `unknown` instead of overstating certainty
- it produces a structured parcel-state output that downstream systems can present without recomputing the reasoning

## Core claimed idea in plain language

For a target parcel, the system assembles evidence from different source classes, applies parcel-specific evaluation for one or more hazards, determines what kinds of sources materially supported the result, and emits a parcel-state object containing homeowner-readable statuses plus confidence, evidence mode, freshness, reasons, and provenance summary.

## Example output fields

- shelter conditions estimate
- reentry conditions estimate
- egress conditions estimate
- asset risk estimate
- confidence
- evidence mode
- reasons
- hazard-supporting values
- freshness
- provenance summary

## Candidate boundaries

More likely in scope for this narrow filing:

- evidence assembly by source class for a target parcel
- parcel-specific hazard evaluation using local evidence, parcel priors, and public context
- explicit evidence-mode output
- confidence degradation and unknown-state behavior
- structured parcel-state snapshot generation

More likely outside this narrow filing:

- generic sensor hardware
- ordinary packet transport and schema validation
- general-purpose data storage
- final UI presentation details
- unrelated open-governance and licensing materials

## Key questions for counsel

- Is this narrow enough to file quickly but still commercially meaningful?
- Is it better to keep shared neighborhood evidence out of this filing entirely?
- What extra implementation details are needed for stronger written-description support?
- Which public preview materials are safe before filing, and which must stay held back?

## Immediate decisions needed from the project

- confirm inventors
- confirm owner/applicant
- choose exact filing target date
- confirm that neighborhood-sharing transforms are excluded from this filing
- decide whether any formulas, thresholds, or specific embodiments need to be preserved now
