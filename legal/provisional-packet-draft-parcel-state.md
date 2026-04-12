# Provisional Packet Draft: Parcel-State Generation

## Status

Internal drafting document for a possible narrow U.S. provisional filing.

Do not publish this file or derivative diagrams before the filing decision.

This is planning support, not legal advice.

## Working assumptions

- filing path: narrow U.S. provisional first, then enabling open release
- candidate invention type: parcel-level status generation using parcel priors plus local and public evidence with explicit evidence mode and confidence handling
- project objective after filing: release the broader system under commons-protective open licenses

## Packet metadata

- working title: Parcel-level environmental condition generation with source-aware evidence modes
- inventors: `[confirm]`
- owner/applicant: `[confirm with counsel]`
- drafting owner: Liam / project lead `[confirm]`
- target filing date: `[fill]`
- related materials to hold until filing:
  - parcel-inference flowchart
  - detailed evidence weighting notes
  - neighborhood contribution transform details, which are outside this narrow filing
  - detailed calibration and threshold rules

## Section 1. Problem Statement

Conventional environmental information systems often operate at coarse regional scales, depend on centralized sensing, or present generalized alerts that do not resolve conditions at the level of an individual parcel. A parcel operator deciding whether shelter conditions, reentry conditions, egress conditions, or asset-risk conditions are degraded often has a mix of incomplete sources: one or more private nodes on the parcel, parcel-specific context such as node placement or structure characteristics, and delayed or low-resolution public context such as weather, smoke, or flood feeds. Existing tools tend either to expose raw readings without parcel-specific interpretation or to present simplified guidance without making the provenance and uncertainty of the result explicit.

The technical gap addressed here is not merely collecting more observations. The gap is generating a parcel-level condition state from heterogeneous evidence sources while preserving source boundaries, degrading gracefully under sparse evidence, and explicitly indicating the mode of evidence used to produce the result. In practical terms, the system should remain useful for a single-home deployment and still distinguish between a result based on direct local observations and a result based partly or entirely on public context.

This problem matters because a parcel can differ materially from surrounding conditions due to structure type, orientation, topography, drainage behavior, microclimate, or node placement. A dwelling-facing system therefore benefits from a parcel-specific state-generation method that can combine locally observed evidence, parcel metadata, and public context, while preserving confidence and explanation outputs rather than collapsing all conditions into a single unsupported label.

## Section 2. Narrow Invention Summary

The candidate invention is a computer-implemented method for generating parcel-level environmental condition states by assembling an evidence set for a target parcel from local observations, parcel-specific context, and optional public context, applying parcel-specific context and hazard-specific evaluation logic, and producing a parcel-state snapshot that includes one or more parcel operator-readable status outputs, at least one confidence value, and at least one explicit evidence-mode indicator describing whether the result was derived from local observations, local observations plus public context, public context only, or insufficient evidence.

In one implementation, the method accepts normalized observations from one or more operator-controlled nodes associated with a parcel, parcel context describing the parcel or node placement, and optional public hazard context. The method groups evidence by hazard domain, evaluates freshness and source quality, computes hazard-supporting scores or probabilities, maps those results into parcel-level status fields, and emits explanation content that identifies why the status was assigned and what evidence classes contributed. The method further downgrades confidence or returns an `unknown`-type output when evidence is stale, sparse, conflicting, or absent.

This candidate differs from ordinary sensor dashboards and regional alert overlays because it does not merely display raw node values or public feed values. It generates a parcel-state object with explicit provenance-aware outputs, source-mode labeling, and graceful degradation logic so the same system can operate under direct-local or public-context-supported conditions without representing all results as equally certain.

## Section 3. System Context

The candidate invention sits inside the broader Open Environmental Sensing and
Inference System, which includes hardware sensor nodes, an ingest service, an
inference engine, a parcel platform, and shared neighborhood views. For
purposes of this draft, the focus is the parcel-state generation method
performed after ingest normalization and before parcel operator presentation.

Relevant system modules are:

- hardware nodes that collect raw environmental observations
- an ingest service that validates packets, normalizes observations, and preserves raw-packet provenance
- an inference engine that assembles parcel evidence and generates parcel-state snapshots
- a parcel platform that presents the resulting parcel-state view
- optional shared-map or neighborhood layers, which are outside this narrow filing

The candidate begins when normalized observations and parcel context are available for a target parcel. The candidate ends when a parcel-state snapshot is produced for storage, API use, or parcel operator display.

For this candidate, likely conventional background elements include:

- generic sensor hardware
- timestamped packet ingestion
- ordinary schema validation
- storage of normalized observations
- display of previously computed statuses in a user interface

Candidate material for the narrow filing is more likely to include:

- assembly of parcel evidence from distinct source classes
- use of parcel priors or parcel context in hazard evaluation
- explicit evidence-mode classification tied to the available source classes
- confidence degradation and `unknown` behavior based on freshness, sparsity, or conflict
- generation of a parcel-state object that carries both parcel operator-readable statuses and provenance-aware explanation outputs

For this draft, neighborhood-sharing transforms and shared-evidence aggregation are intentionally excluded from the narrow filing candidate.

## Section 4. Definitions

### Parcel

A specific home site, lot, structure location, or similarly bounded property unit for which a condition state is generated.

### Parcel prior

Pre-existing context about the parcel used in interpretation, including by example structure type, topography, drainage characteristics, node placement context, or previously known parcel attributes relevant to one or more hazards.

### Local evidence

Observations originating from one or more operator-controlled devices, sensors, or other direct parcel-linked sources associated with the target parcel.

### Shared evidence

Evidence derived from other participating parcels or neighborhood contributors under an opt-in sharing mode that is more limited than direct access to another parcel's raw data. Shared evidence is outside the scope of this narrow filing draft.

### Public context

Third-party or public-source information such as weather, flood, smoke, terrain, or alert layers used to interpret parcel conditions.

### Hazard evidence set

A set of evidence items associated with a given parcel and hazard domain, assembled from one or more of local evidence, public context, and parcel prior information.

### Evidence mode

A categorical indicator representing which source classes materially contributed to a parcel-state result. Example modes may include local-only, local-plus-public, public-only, or insufficient.

### Confidence

A numeric or categorical representation of support for a parcel-state result based on evidence quality, freshness, consistency, and completeness, distinct from any claim of certainty.

### Freshness

A representation of the recency of one or more inputs used in a parcel-state result, including whether a relevant input is stale under hazard-specific rules.

### Parcel-state snapshot

A structured output describing one or more current parcel-level condition estimates, together with supporting metadata such as confidence, evidence mode, reasons, freshness, and provenance summary.

### Explanation payload

Human-readable or machine-readable content identifying at least part of the basis for a parcel-state result.

## Section 5. Detailed Method Description

### Overview

The method generates a parcel-state snapshot for a target parcel by gathering available evidence, separating that evidence by source class and hazard domain, evaluating the evidence in light of parcel context, producing hazard-supporting outputs, and then mapping those outputs into parcel operator-readable parcel condition states with confidence, freshness, and evidence-mode metadata.

### Step 1. Receive or retrieve parcel inputs

The system receives or retrieves, for a target parcel:

- normalized local observations associated with one or more parcel-linked nodes
- parcel metadata and parcel prior information
- optional public context relevant to one or more hazards
- hazard-specific evaluation parameters, rules, thresholds, or model settings

Inputs may arrive event-driven after a new observation, on a scheduled recomputation cycle, or in response to a parcel operator request for the latest parcel state.

### Step 2. Assemble hazard-specific evidence sets

The system groups available inputs into one or more hazard evidence sets. For example, one set may be assembled for smoke, another for flooding or runoff, and another for heat.

For each hazard evidence set, the system may:

- identify which local observations are relevant to the hazard
- identify which parcel priors affect interpretation
- identify which public context sources are relevant and fresh enough to use
- retain references to underlying observations for later provenance reporting

The assembly step keeps source classes distinct rather than flattening all inputs into an undifferentiated pool.

### Step 3. Evaluate freshness, completeness, and conflict

For each hazard evidence set, the system evaluates whether the available inputs are sufficiently recent, sufficiently complete, and mutually consistent enough to support a parcel-state output stronger than `unknown`.

This step may include:

- measuring time since latest local observation
- checking whether the parcel has direct observations for the hazard or only indirect context
- identifying conflicts between local evidence and public context
- downgrading support where evidence is sparse or stale

### Step 4. Apply parcel-specific hazard evaluation

For each hazard domain, the system applies hazard-specific logic that uses at least some combination of:

- local evidence
- parcel priors
- public context

The exact hazard logic may vary by hazard type, but the method maintains a common source-aware structure. In one example, local evidence may dominate when recent and relevant, while public context may expand or constrain interpretation where local coverage is partial. In another example, the absence of direct local evidence may limit the system to a lower-confidence public-context result rather than a parcel-specific affirmative condition.

This step produces one or more supporting values such as:

- hazard score
- hazard probability
- rule outcome
- supporting reason codes

### Step 5. Determine evidence mode

The system assigns an evidence mode for the parcel-state result based on which source classes materially contributed to the determination. The evidence mode is not merely a hidden internal flag; it is carried into the output so downstream systems and parcel operators can distinguish a locally grounded result from a shared or public-context result.

Example evidence-mode logic may include:

- local-only when the output is supported only by parcel-linked direct observations
- local-plus-public when local evidence exists and public context materially supplements interpretation
- public-only when the result relies only on external context
- insufficient when evidence is too weak for a meaningful condition estimate

### Step 6. Determine confidence and degrade when needed

The system determines confidence for the parcel-state result using evidence quality factors such as recency, amount of direct local evidence, consistency across sources, and relevance of parcel priors.

Confidence is reduced when:

- evidence is stale
- evidence is sparse
- source classes conflict materially
- only public context is available
- parcel priors are insufficient to support stronger interpretation

Where degradation crosses a threshold, the output may remain or become `unknown` rather than overstating parcel certainty.

### Step 7. Map supporting outputs into parcel-state fields

The system maps the hazard-supporting outputs into one or more parcel operator-readable status fields. In current project language, these may include:

- shelter conditions estimate
- reentry conditions estimate
- egress conditions estimate
- asset risk estimate

The mapping may produce parallel hazard-specific values and general parcel-state values in the same snapshot.

### Step 8. Generate reasons and provenance summary

The system generates explanation content identifying the main basis for the parcel-state output. This may include:

- human-readable reason fragments
- source-mode summary
- freshness indicators
- observation references or source references

This step helps distinguish observed conditions from inferred conditions and supports auditability.

### Step 9. Persist and serve the parcel-state snapshot

The system stores or transmits a parcel-state snapshot that may include:

- parcel identifier
- computed time
- one or more status outputs
- confidence
- evidence mode
- reasons
- hazard-supporting values
- freshness block
- provenance summary

The parcel platform can then present this snapshot without recomputing hazard logic in the user interface layer.

### Example implementation pattern

One example uses:

- normalized node observations from an indoor air node on a parcel
- parcel metadata indicating deployment location and structure context
- a smoke-related public context layer

The system assembles a smoke evidence set, determines whether recent local observations exist, checks whether public smoke context is present, evaluates freshness and conflict, computes a smoke-support value, assigns an evidence mode, degrades confidence if only indirect evidence exists, and produces a parcel-state snapshot including a shelter condition estimate, confidence, evidence mode, reasons, and provenance references.

### Variants to preserve

The filing packet should preserve at least these variants:

- operation with direct local evidence only
- operation with local evidence plus public context
- operation with no direct local evidence but with public context
- operation across multiple hazards with common output structure but hazard-specific evaluation logic
- operation where the system intentionally returns `unknown` because evidence quality is insufficient

## Draft figure list

- Figure 1. System block diagram from node observations to parcel-state snapshot
- Figure 2. Parcel evidence assembly by source class and hazard domain
- Figure 3. Evidence-mode assignment flow
- Figure 4. Confidence degradation and unknown-state transition
- Figure 5. Example parcel-state snapshot with provenance fields

## Immediate fill-ins needed

- named inventors
- exact target filing date
- preferred evidence-mode vocabulary
- confirm that shared evidence is carved into a separate filing candidate
- any implementation details important enough to preserve now rather than later
