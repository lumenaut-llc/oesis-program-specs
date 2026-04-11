# Deployment Maturity Ladder

## Purpose

Define the deployability overlay used by the repo to distinguish bench prototypes, field-hardened parcel kits, and later trust or adaptation readiness without renumbering the core capability roadmap.

## Governing rule

The capability roadmap and the deployment maturity ladder are separate axes.

- capability stages describe what the product can do
- deployment maturity describes how field-hardened, serviceable, and trustworthy a hardware and operations lane is

When the maturity ladder is used, it should be labeled as deployment maturity.

## Deployment maturity ladder

### `deployment maturity v0.1`

Bench prototype and first bring-up path.

Typical traits:

- development boards are still acceptable
- serial JSON validation is the center of gravity
- calibration is provisional
- enclosure, power, and wiring may still be prototype-grade
- the node is useful for learning and software validation
- the node should not be described as field-ready

### `deployment maturity v1.0`

First field-hardened parcel kit.

This is the minimum maturity required before calling a node deployed or field-ready for the first homeowner parcel kit.

Required bundle:

- protected power path
- local buffering or durable local storage
- connectorized or otherwise serviceable wiring
- enclosure support parts appropriate to the environment
- physical identity label
- practical service access posture
- spare-parts posture for active node families
- installation metadata sufficient to interpret the node honestly

### `deployment maturity v1.5`

Trust and device-operations hardening.

Typical additions:

- heartbeat and stronger health reporting
- calibration or correction versioning
- maintenance logging and service penalties
- better freshness, replay, and buffering semantics
- clearer device lifecycle and replacement handling
- stronger linkage between deployment quality and inference trust

### `deployment maturity v2.0`

Decision-policy and adaptation support on top of a hardened evidence path.

Typical additions:

- explicit decision-policy layer
- stronger verification and replay support
- support objects for building response and intervention quality
- clearer operational policy versioning and override posture

## Shared field-hardening bundle

No node should be described as deployed or field-ready unless the repo documents a concrete answer for each of these categories:

### Power and protection

- fused or otherwise protected power input where appropriate
- reverse-polarity protection where applicable
- surge or transient protection for outdoor power entry
- stable regulator or supply selection for the node class

### Local buffering and storage

- ring buffer, FRAM, microSD, or other durable local store where loss of recent observations would materially weaken trust
- explicit storage choice for Pi-based nodes
- clean shutdown posture where corruption risk is nontrivial

### Wiring and connectors

- strain-relieved cable paths
- locking or serviceable connectors where practical
- avoidance of loose long-term jumper-wire posture for deployed nodes

### Enclosure and mounting support

- cable glands or equivalent protected entries
- venting or membrane vent where needed
- drip-path and moisture control posture
- corrosion-aware hardware where relevant
- stable mounting geometry

### Identity and serviceability

- physical node label or QR label
- reset, flash, or service access posture
- visible field status indicator if practical
- spare-parts and replacement posture

## Node-family maturity map

| Node family | Current maturity posture | First honest maturity target | Key gap to close |
| --- | --- | --- | --- |
| `bench-air-node` | `deployment maturity v0.1` by default | `deployment maturity v1.0` only after the shared field-hardening bundle is documented for the install, including fixed harness, stable mount or enclosure, physical label, and local logging posture | stop treating dev-board-only bring-up as the deployed baseline |
| `mast-lite` | early outdoor prototype | `deployment maturity v1.0` | protected power, cable glands, connectorized leads, local buffering, and sheltered install discipline |
| `weather-pm-mast` | second-wave hardware lane | `deployment maturity v1.5` target | PM power path, RJ11 or weather-sensor interface posture, airflow path, service module, and maintenance workflow |
| `flood-node` | experimental field prototype | parcel-specific `deployment maturity v1.0` only after geometry discipline is documented | rigid mount, zero reference, field marker or staff gauge, and repeatable geometry |
| `thermal-pod` | R&D lane | keep below `deployment maturity v1.0` until scene and privacy posture are stronger | stable power, durable storage, clean shutdown, thermal isolation, and repeatable field-of-view geometry |

## Relationship to the capability roadmap

The maturity ladder is intentionally conservative.
A node family may appear in the architecture before it is mature enough to support stronger parcel confidence claims.

Examples:

- a node may be architecturally in scope for `current v1` while still living at `deployment maturity v0.1`
- `deployment maturity v1.0` is about honest deployability, not adaptation guidance
- `deployment maturity v1.5` improves trust and device operations, but does not replace capability stage `v1.5`

## Related docs

- `integrated-parcel-system-spec.md`
- `sensor-placement-and-representativeness-guide.md`
- `../build-guides/field-hardening-checklist.md`
- `../build-guides/pilot-field-kit.md`
