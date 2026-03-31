# Provisional Figure Captions: Parcel-State Generation

## Status

Internal drafting document for a possible narrow U.S. provisional filing.

Do not publish before the filing decision.

## Purpose

Provide a first-pass figure plan and caption text for the parcel-state generation candidate so diagrams can be produced quickly without re-deciding the story each time.

## Figure 1. System block diagram from node observations to parcel-state snapshot

### Figure intent

Show the end-to-end location of the candidate invention inside the broader system while keeping the claimed focus on parcel-state generation rather than the full platform.

### Suggested visual elements

- homeowner-controlled node or nodes
- ingest service
- normalized observation store
- parcel metadata / parcel prior store
- optional public-context input
- inference engine
- parcel-state snapshot output
- parcel platform / homeowner-facing view

### Draft caption

Figure 1 illustrates an example system in which one or more homeowner-controlled nodes provide environmental observations that are normalized by an ingest service and combined with parcel context and optional public context to produce a parcel-state snapshot for a target parcel. The parcel-state snapshot may include one or more homeowner-readable condition outputs, confidence, evidence mode, reasons, freshness, and provenance summary. The parcel platform may present the parcel-state snapshot without recomputing the hazard logic in the presentation layer.

### Draft annotation notes

- mark local evidence, shared evidence, and public context as separate source classes
- visually isolate the inference engine as the site of the candidate method
- label parcel-state snapshot fields at a high level

## Figure 2. Parcel evidence assembly by source class and hazard domain

### Figure intent

Show that the method assembles evidence sets for a target parcel while preserving distinctions among local and public source classes and grouping by hazard domain.

### Suggested visual elements

- target parcel identifier
- local evidence lane
- public context lane
- parcel prior/context input
- smoke evidence set
- flood/runoff evidence set
- heat evidence set

### Draft caption

Figure 2 illustrates an example evidence-assembly process in which inputs associated with a target parcel are grouped into hazard-specific evidence sets while maintaining distinctions among local parcel-linked observations, public context, and parcel prior information. The assembled evidence sets may be separately evaluated for smoke, flooding or runoff, heat, or other supported hazards.

### Draft annotation notes

- show that not every hazard set needs every source class
- show observation references or provenance hooks surviving assembly

## Figure 3. Evidence-mode assignment flow

### Figure intent

Show how the system classifies the parcel-state result according to the source classes that materially contributed to the output.

### Suggested visual elements

- decision inputs for presence of recent local evidence
- decision inputs for presence of relevant public context
- output modes such as local-only, local-plus-public, public-only, and insufficient

### Draft caption

Figure 3 illustrates an example process for assigning an evidence mode to a parcel-state result based on which evidence source classes materially contribute to the result. In some embodiments, the system distinguishes among results supported by direct parcel-linked observations, results supplemented by public context, results based only on public context, and results classified as insufficient where available evidence is too weak to support a meaningful parcel-level condition estimate.

### Draft annotation notes

- keep it as source-mode logic, not detailed scoring logic
- if desired, note that exact criteria may vary by hazard

## Figure 4. Confidence degradation and unknown-state transition

### Figure intent

Show that the system can reduce confidence and intentionally return an `unknown`-type output when evidence quality is weak instead of overstating certainty.

### Suggested visual elements

- evidence quality inputs: freshness, completeness, conflict, source directness
- confidence computation block
- threshold or decision boundary for unknown-state downgrade
- output path for lower-confidence but still reportable result
- output path for unknown / insufficient result

### Draft caption

Figure 4 illustrates an example confidence-handling process in which the system evaluates evidence quality factors including recency, completeness, consistency across source classes, and availability of direct parcel-linked observations. Confidence may be reduced when evidence is stale, sparse, conflicting, or indirect. Where support falls below a defined sufficiency condition, the system may output an unknown or insufficient parcel-state result instead of presenting a stronger status unsupported by the available evidence.

### Draft annotation notes

- do not lock in numeric thresholds in the figure unless you want those preserved
- this figure helps separate the invention from systems that always emit a definitive state

## Figure 5. Example parcel-state snapshot with provenance fields

### Figure intent

Show the output object structure at a level sufficient to support the filing without forcing the packet to depend on final implementation syntax.

### Suggested visual elements

- parcel identifier
- computed time
- one or more condition-status fields
- confidence
- evidence mode
- reasons
- hazard-supporting values
- freshness block
- provenance summary

### Draft caption

Figure 5 illustrates an example parcel-state snapshot generated for a target parcel. The parcel-state snapshot may include homeowner-readable condition outputs, a confidence value, an evidence-mode value, reasons, hazard-supporting values, freshness information, and a provenance summary identifying at least part of the evidence basis for the result. The parcel-state snapshot may be stored, served by an API, or rendered in a homeowner-facing parcel view.

### Draft annotation notes

- use field labels consistent with the current parcel-state schema where helpful
- keep the figure generic enough that implementation naming can evolve

## Optional Figure 6. Example smoke-domain execution

### Figure intent

Provide one concrete worked example without forcing the entire filing to depend on a single hazard type.

### Suggested visual elements

- indoor node observations
- smoke-related public context
- smoke evidence set
- smoke-support output
- shelter condition estimate / evidence mode / confidence result

### Draft caption

Figure 6 illustrates an example smoke-domain execution in which indoor parcel observations and smoke-related public context are assembled into a smoke evidence set for a target parcel and used to generate a parcel-state result that includes at least a shelter condition estimate, confidence, evidence mode, and one or more reasons.

## Fast diagramming notes

- avoid exact formulas unless you want them preserved in the packet
- keep source classes visually distinct throughout
- emphasize that the UI consumes a produced parcel-state snapshot rather than performing the inference
- use synthetic examples only
