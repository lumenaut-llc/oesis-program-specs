# Resilient Home Intelligence Glossary

## Parcel
The primary unit of reasoning in the system. Usually a specific house lot or property footprint with associated spatial and contextual features.

## Home
The occupant or structure-specific object associated with a parcel.

## Sensor node
A physical sensing unit deployed at or near a parcel. Examples: bench air node, mast-lite, flood node, thermal pod.

## Parcel prior
The baseline expectation for a parcel before fresh sensor evidence is applied. Built from terrain, drainage, exposure, access, and other slow-changing context.

## Local evidence
Observations from a healthy sensor node directly associated with a parcel.

## Shared evidence
Observations or derived signals that a homeowner has opted to contribute to the neighborhood or shared intelligence layer.

## External public data
Regional or public context sources integrated inside the platform, such as weather, flood, smoke, and terrain data.

## Derived parcel state
The platform's computed view of conditions or statuses for a parcel, based on parcel priors plus evidence layers.

## Confidence
How certain the system is about a computed parcel condition or status.

## Evidence mode
A label describing where the current parcel state comes from.
Possible values:
- observed_local
- inferred_neighbors
- inferred_regional
- stale

## Observed local
The parcel has a healthy local node with fresh data, and direct evidence strongly informs the parcel state.

## Inferred neighbors
The parcel lacks strong local evidence, but nearby shared nodes provide enough information to estimate current local conditions.

## Inferred regional
The parcel state is driven mostly by parcel priors and external public data because local or shared neighborhood evidence is weak.

## Stale
There is not enough fresh evidence to support a confident current state.

## Standalone value
The usefulness of a subproject or hardware build even if it is not connected to the full network.

## Network value
The additional usefulness created when a build contributes to or benefits from the larger shared intelligence layer.

## Private owner data
Data visible only to the homeowner unless they explicitly choose to share it.

## Shared neighborhood layer
The common condition field built from opt-in shared data plus external public context.

## Provenance
The record of where a displayed value, condition, or status came from.

## Hazard engine
The system component that computes smoke, flood, heat, or other hazard-specific parcel conditions.

## Explanation layer
The system component that explains why a parcel received a given status and what evidence contributed.

## Mast-lite
A simple outdoor environmental node focused on core weather and air variables.

## Flood node
A dedicated sensing node mounted at an operational low point to track water depth or distance to surface.

## Thermal pod
A simple 2D scene-sensing unit that produces derived thermal metrics instead of only point measurements.
