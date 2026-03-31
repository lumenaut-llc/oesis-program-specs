# Holdback List

## Purpose

Track the technical materials that should stay out of the April 14, 2026 public preview unless they are already covered by a filed provisional or the team intentionally switches to full defensive publication.

This list should be reviewed before any social post, repo publication, talk, demo, diagram release, or media interview.

## Current holdback categories

### 1. Narrow filing candidate details

Hold back:

- the exact statement of the narrow inventive concept
- ordered method steps beyond high-level concept language
- novel combinations of parcel priors, local observations, shared neighborhood evidence, and public context
- implementation variants that materially expand the candidate invention

Why:

- these are the materials most likely to determine whether a provisional meaningfully supports later claims

### 2. Parcel-inference internals

Hold back:

- decision trees or state-machine logic
- evidence weighting rules
- confidence scoring logic
- fallback and degradation logic tied to novelty
- threshold values
- conflict-resolution rules between local, shared, and public evidence

Why:

- these can turn a high-level concept into an enabling disclosure

### 3. Privacy-preserving sharing mechanics

Hold back:

- exact transformation methods for neighborhood contribution
- aggregation thresholds if they are part of the novel method
- timing and batching rules if they are central to the invention
- any algorithmic description that explains how parcel-linked data becomes shared intelligence

Why:

- this is a plausible narrow patent target and should not leak accidentally through governance or API docs

### 4. Hardware implementation files

Hold back:

- full schematics
- PCB layouts and fabrication outputs
- detailed enclosure CAD
- manufacturing drawings
- board-level closeups that reveal unreleased layouts
- wiring diagrams that expose withheld architecture

Why:

- they may disclose unreleased implementation details and are easy to over-share through photos or diagrams

### 5. Software and protocol specifics

Hold back:

- source code implementing the narrow filing candidate
- detailed API contracts that expose withheld methods
- packet schemas that reveal novel logic or device interactions
- internal scripts or examples that demonstrate the withheld method end-to-end

Why:

- code and schemas are often more enabling than summary prose

### 6. Calibration and operational methods

Hold back:

- calibration procedures that materially enable reproduction of the candidate invention
- field tuning procedures tied to the novel inference method
- exact alerting or state-transition rules

Why:

- these can disclose key practical details even when the main architecture doc looks high-level

## Allowed substitutes during preview

Use these instead of the holdback items:

- abstract architecture blocks
- principle-level descriptions
- prototype photos without internals
- high-level data-class diagrams
- problem statement and user-value framing
- governance, ownership, and limitation language

## Review workflow

For each item under consideration:

1. Ask whether it would help a skilled person reproduce the narrow filing candidate.
2. Ask whether it adds technical detail not already captured in the provisional packet.
3. Ask whether it contains any real parcel-linked user data.
4. If any answer is yes, hold it back pending filing or attorney review.

## Status table

Use this table as the live release gate.

| Item | Owner | Status | Covered by provisional packet | Safe for April 14 preview | Notes |
| --- | --- | --- | --- | --- | --- |
| Narrow invention summary | Legal/IP owner | pending | no | no | fill after filing decision |
| Parcel-inference flowchart | Engineering owner | pending | no | no | keep internal unless filed |
| Neighborhood-sharing transform | Data/governance owner | pending | no | no | likely narrow filing candidate |
| Hardware design package | Hardware owner | pending | no | no | release after filing or open publication decision |
| Example packet schemas | Software owner | pending | no | no | keep internal until legal gate clears |
| High-level architecture diagram | Docs owner | pending | n/a | yes, if non-enabling | remove thresholds and method detail |
