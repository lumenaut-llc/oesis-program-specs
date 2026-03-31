# Public Preview Scope

## Purpose

Define what may be published on or before the April 14, 2026 public preview while the project preserves the option to file a narrow U.S. provisional first.

This is a release-planning control document, not legal advice.

## Current release path

- Path B: limited public preview first, enabling technical release after filing decision
- U.S.-first sequencing assumption: preserving optional narrow filing matters more than preserving foreign rights
- Default publication rule until filing decision: non-enabling only

## April 14 preview goals

- make the openness and governance posture public
- state homeowner data ownership and sharing boundaries
- show the project mission and hazard scope
- show high-level modular architecture without teaching reproduction of potentially novel implementation details
- keep the later full open-source release straightforward after filing

## Approved public materials before filing

The following are generally in scope for the public preview:

- mission, principles, and problem statement
- high-level architecture overview without implementation-enabling detail
- preview README and program overview pages
- governance, privacy, and data-ownership summaries
- claims, limitations, and safety-position language
- prototype photos that do not reveal reproducible internals
- non-enabling diagrams showing major modules and data classes
- release roadmap and open-license intent by asset class
- contributor and stewardship posture

## Out of scope before filing

Do not publish these items before the filing decision unless attorney review says otherwise or the team deliberately switches to open defensive publication instead:

- schematics
- PCB layouts or fabrication files
- detailed CAD source files
- detailed bills of materials tied to the inventive concept
- serial or network packet contracts that expose novel implementation structure
- calibration methods that materially enable reproduction
- threshold logic or scoring rules tied to parcel inference
- detailed evidence-weighting methods
- privacy-preserving neighborhood-sharing implementation details
- detailed flowcharts that would let a skilled person reproduce the narrow filing candidate
- source code or configuration that teaches a potentially patentable method not yet filed

## Green / yellow / red gate

### Green

Publish without additional escalation if the material:

- explains why the project exists
- explains who controls data
- explains the difference between private, shared, and public data
- names system modules at a high level
- does not reveal a reproducible method

### Yellow

Route for release-owner review before publication if the material:

- describes a method with ordered technical steps
- includes diagrams with message flow, thresholds, or decision points
- includes close-up imagery of boards, wiring, or enclosure internals
- describes how neighborhood contributions are transformed before sharing
- explains how parcel status is calculated beyond broad concept level

### Red

Do not publish before filing or express counsel sign-off if the material:

- would let a skilled person reproduce the narrow invention candidate
- discloses a new variation not captured in the provisional packet
- includes source files, formulas, thresholds, or implementation values tied to the candidate invention
- exposes real homeowner data or parcel-linked records

## Canonical preview package

The April 14 preview should point readers to these materials:

- program README
- governance and privacy overview
- data ownership statement
- claims and limitations page
- contribution and stewardship policy
- release roadmap

## Release-owner checklist

Before a preview asset is published, confirm:

- it is classified as green or approved yellow
- it does not contain real homeowner-contributed data
- it does not contradict the private-by-default rule
- it does not overclaim accuracy or safety
- it does not expose withheld technical details

## Trigger to move from preview to full open release

Move from preview to the technical open release when one of these occurs:

- the narrow provisional is filed and the released materials stay within that support
- the team decides not to file and instead chooses open defensive publication
- attorney review confirms the withheld materials no longer need to be held back
