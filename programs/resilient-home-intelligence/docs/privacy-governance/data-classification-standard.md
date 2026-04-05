# Data Classification Standard

## Purpose

Define the operational data classes for the MVP so architecture, UI, API design, and policy all use the same boundaries.

## Governing rule

The platform must keep private parcel data, shared data, public context, derived parcel states, and administrative records distinct in storage, access control, API presentation, and user-facing language.

## Data classes

### 1. Private parcel data

Definition:
Data linked to one parcel, household, or device deployment that is not shared by default beyond the homeowner account and necessary service operations.

Examples:
- raw sensor observations
- exact parcel identifier and geometry
- exact node location
- device serials, network identifiers, and health details
- fine-grained timestamps tied to one parcel
- structure-specific notes
- route-specific or ingress/egress-specific annotations
- exact parcel-level event history
- occupancy-adjacent inferences, whether explicit or implicit
- house-state telemetry such as indoor PM, indoor temperature/RH, HVAC mode, recirculation state, purifier state, backup-power state, and window/shade state
- house capability and compatibility records such as filter-path limits, higher-MERV support, local-controller availability, and control-locality notes
- intervention and verification histories tied to one parcel

Handling rules:
- private by default
- highest sensitivity class in the product
- must not be exposed in public APIs or public map layers
- must not be used for advertising, lead scoring, insurance profiling, or unrelated analytics
- access limited to the homeowner, authorized household roles, and narrowly approved service operations

### 2. Shared data

Definition:
Data a homeowner affirmatively elects to contribute beyond private parcel use under a documented sharing mode.

Examples:
- delayed hazard indicators
- coarse spatial bins or neighborhood-cell signals
- thresholded trend summaries
- aggregated contributions to neighborhood inference
- event-based contribution during a declared or user-selected hazard window

Handling rules:
- opt-in only
- separately governed from private parcel data
- should default to derived or coarsened signals rather than raw streams
- must be revocable for future sharing
- must not be represented as anonymous unless a documented de-identification standard is actually met

### 3. Public context

Definition:
Third-party or public-source information used to interpret parcel conditions.

Examples:
- weather feeds
- flood and hydrology context
- smoke and air-quality context
- terrain, elevation, and land-cover context
- parcel basemap and public records context
- public alert feeds

Handling rules:
- store source, timestamp, freshness, and license metadata
- clearly distinguish from homeowner-contributed data
- do not imply local verification when the source is regional or delayed

### 4. Derived parcel states

Definition:
System-generated interpretations about parcel conditions produced from one or more evidence sources.

Examples:
- stay, enter, escape, and asset condition outputs
- confidence values
- evidence mode
- reasons and explanation payloads
- hazard-specific probability or risk estimates

Handling rules:
- must be labeled as inferences, not facts
- must include provenance and freshness support
- must show uncertainty honestly
- should degrade to `unknown` when evidence quality is weak
- must not be marketed as emergency instructions or guarantees

### 5. Administrative and governance records

Definition:
Records required to operate the system responsibly and demonstrate accountability.

Examples:
- consent records
- sharing setting history
- admin access logs
- export and deletion requests
- incident records
- model or rule version history
- notice and policy acceptance records

Handling rules:
- retained as evidence of governance actions
- access restricted to personnel with operational need
- kept separate from product telemetry where possible

## Data ownership model

For MVP, the platform should use the following model:

- homeowners own and control the raw sensor data they contribute from their parcel deployments
- the platform receives a limited operating license to process that data for the service the homeowner enabled
- shared contributions are governed by the specific sharing mode selected by the homeowner
- public context remains subject to the underlying source license and attribution rules
- derived parcel states are platform-generated outputs about the homeowner's parcel, but they do not erase the homeowner's rights in the underlying raw data

## Data-class handling requirements

- Every schema and API must identify the data class it carries.
- Every user-facing view must distinguish private, shared, public, and derived content.
- Every new feature must declare whether it creates a new data class or new use of an existing class.
- No feature may silently repurpose private parcel data into shared or public outputs.
- Control configuration or automation eligibility must not be treated as an implied sharing permission.

## Prohibited shortcuts

- treating exact parcel-linked data as ordinary analytics telemetry
- mixing public context and local evidence without source labeling
- calling shared parcel-linked data anonymous by default
- exposing exact parcel contributions through neighborhood tools
- using one blanket consent for all sharing purposes
