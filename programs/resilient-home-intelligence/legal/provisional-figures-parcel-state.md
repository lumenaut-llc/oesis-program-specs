# Provisional Figures: Parcel-State Generation

## Status

Internal drafting document for a possible narrow U.S. provisional filing.

Do not publish before the filing decision.

## Purpose

Provide fast visual drafts for the parcel-state generation candidate so the team can review the filing story, refine scope, and turn the figures into formal drawings if needed.

## Figure 1. System block diagram from node observations to parcel-state snapshot

```mermaid
flowchart LR
    A["Homeowner-controlled node(s)"] --> B["Ingest service"]
    B --> C["Normalized observation store"]
    C --> F["Inference engine"]
    D["Parcel metadata / parcel priors"] --> F
    G["Optional public context"] --> F
    F --> H["Parcel-state snapshot"]
    H --> I["Parcel platform / homeowner view"]
```

Notes:

- Keep local and public inputs visually distinct.
- The inference engine is the center of the candidate method.
- The parcel platform consumes the output rather than recomputing it.

## Figure 2. Parcel evidence assembly by source class and hazard domain

```mermaid
flowchart TB
    A["Target parcel"] --> B["Local evidence lane"]
    A --> D["Public context lane"]
    A --> E["Parcel priors / parcel context"]

    B --> F["Smoke evidence set"]
    D --> F
    E --> F

    B --> G["Flood / runoff evidence set"]
    D --> G
    E --> G

    B --> H["Heat evidence set"]
    D --> H
    E --> H
```

Notes:

- Not every hazard set needs every source class in practice.
- Observation references and provenance links should survive assembly.

## Figure 3. Evidence-mode assignment flow

```mermaid
flowchart TD
    A["Hazard evidence set for target parcel"] --> B{"Recent local evidence?"}
    B -- Yes --> C{"Relevant public context also used?"}
    C -- Yes --> E["Evidence mode:\nlocal-plus-public"]
    C -- No --> F["Evidence mode:\nlocal-only"]
    B -- No --> H{"Relevant public context only?"}
    H -- Yes --> K["Evidence mode:\npublic-only"]
    H -- No --> L["Evidence mode:\ninsufficient"]
```

Notes:

- This is source-mode logic, not detailed hazard scoring logic.
- This lean version intentionally excludes shared-neighborhood modes from the filing candidate.

## Figure 4. Confidence degradation and unknown-state transition

```mermaid
flowchart TD
    A["Assembled hazard evidence"] --> B["Evaluate evidence quality"]
    B --> C["Freshness / staleness"]
    B --> D["Completeness / sparsity"]
    B --> E["Conflict across sources"]
    B --> F["Directness of evidence"]
    C --> G["Confidence determination"]
    D --> G
    E --> G
    F --> G
    G --> H{"Support sufficient for reportable state?"}
    H -- Yes --> I["Lower or higher confidence parcel-state output"]
    H -- No --> J["Unknown / insufficient parcel-state output"]
```

Notes:

- Keep numeric thresholds out of the figure unless you want to preserve them explicitly.
- This figure is useful because it shows the system does not force a definitive output when support is weak.

## Figure 5. Example parcel-state snapshot with provenance fields

```mermaid
flowchart TB
    A["Parcel-state snapshot"] --> B["parcel_id"]
    A --> C["computed_at"]
    A --> D["status outputs"]
    A --> E["confidence"]
    A --> F["evidence_mode"]
    A --> G["reasons"]
    A --> H["hazard-supporting values"]
    A --> I["freshness"]
    A --> J["provenance_summary"]
```

Notes:

- Keep the figure generic enough that field names can evolve.
- If useful, match labels to the current schema in a later draft.

## Optional Figure 6. Example smoke-domain execution

```mermaid
flowchart LR
    A["Indoor node observations"] --> D["Smoke evidence set"]
    C["Smoke-related public context"] --> D
    E["Parcel priors / deployment context"] --> D
    D --> F["Smoke-support output"]
    F --> G["Shelter conditions estimate"]
    F --> H["Confidence"]
    F --> I["Evidence mode"]
    F --> J["Reasons / provenance"]
```

Notes:

- Use synthetic examples only.
- This is optional if you want the packet to stay hazard-agnostic.

## Review questions

- Are you comfortable keeping shared neighborhood evidence out of this filing candidate entirely?
- Do you want to preserve any exact evidence-mode vocabulary now?
- Do any of these figures reveal more than you want to hold back before filing?
