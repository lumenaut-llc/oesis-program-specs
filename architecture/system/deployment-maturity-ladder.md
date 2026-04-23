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

This is the minimum maturity required before calling a node deployed or field-ready for the first parcel operator parcel kit.

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

## Deployment-class standards

The three deployment classes named in [`sensor-placement-and-representativeness-guide.md`](sensor-placement-and-representativeness-guide.md) (Indoor, Sheltered, Outdoor) carry platform-level standards for power, enclosure IP rating, and transport. Each node build spec declares its deployment class; the standards below are the defaults. A node may deviate from a default only with an explicit justification documented in its build spec (and where warranted, a gap register entry).

These standards are independent of the capability-stage and accepted-slice axes. They belong to the deployment-maturity ladder because field-hardening is the axis they gate.

### Power source tier by deployment class

| Deployment class | Power source default | Minimum protection | Runtime floor |
|---|---|---|---|
| Indoor | USB from protected supply, or low-voltage DC from adapter | Reverse-polarity protection where applicable; avoid daisy-chain power sharing | Defined by the installation's wall outlet reliability |
| Sheltered | 12 V regulated DC from an outdoor-rated adapter, or USB if the mount is within an enclosed space | Surge protection on entry; fused input; strain relief on cable path | 24 h minimum buffering or local store where ingest loss is consequential |
| Outdoor | Battery + solar with documented runtime floor, or mains with outdoor-rated PSU routed through conduit | Surge + transient + weather protection on entry; fused; sealed connectors | 72 h runtime floor under worst-case solar; retention of last observations through power events |

Pre-v0.1 bench bring-up may deviate (USB on a dev board is fine). Promotion to `deployment maturity v1.0` requires matching the class default or documenting why not.

### Enclosure IP rating tier by deployment class

| Deployment class | Enclosure rating floor | Typical features |
|---|---|---|
| Indoor | Not rated / IP20 acceptable | Dust-ingress management if near HVAC return; no water handling required |
| Sheltered | IP44 minimum | Rain-splash resistant; venting or membrane vent to prevent condensation; drip-path controlled |
| Outdoor | IP54 minimum for passive scenarios; IP65+ for exposed mast installations | Cable glands; venting via membrane; corrosion-aware hardware; UV-stable plastics |

Where a node family requires a radiation shield, weather cowl, or other protective fixture (for example, an outdoor SHT45 mount), the fixture is treated as part of the enclosure for admissibility. Per [`calibration-program.md`](calibration-program.md) §C, readings taken before the protective fixture is verified against its acceptance test are inadmissible to the calibration dataset.

### Transport tier by deployment class

Short-term v0.1 posture is serial-only (see gap register G3). This table sets the long-term policy once transport lanes widen:

| Deployment class | Permitted transports | Notes |
|---|---|---|
| Indoor | Serial (for v0.1 floor); Wi-Fi; wired LAN | Wi-Fi credentials and authorization are governed by the ingest-side design note tracked in G2 |
| Sheltered | Serial; Wi-Fi where the mount is within reliable coverage; LoRa permitted | Same authorization requirements as Indoor |
| Outdoor | Serial during bring-up only; Wi-Fi where coverage is verified; LoRa or cellular permitted for parcels beyond Wi-Fi reach | Transport choice must preserve packet-lineage semantics; no transport may reshape `oesis.bench-air.v1` payload |

Transport choice does not alter the packet schema or the admissibility rule. A packet delivered over LoRa is held to the same schema and integrity requirements as one delivered over serial.

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

## Maintenance and deployment prioritization

The following table ranks sensing surfaces by deployment friction versus
decision value. Use it to sequence which surfaces to build, enable, or
defer.

| Surface | Friction | Decision value | Priority |
| --- | --- | --- | --- |
| Bench-air indoor node | Low (USB power, no install) | High (first parcel evidence) | Build first |
| Thermal slope inference | Zero (computed from existing sensor) | Medium (HVAC state at low confidence) | Enable immediately |
| IO ratio baseline | Zero (computed from existing sensors) | High (smoke loop outcome prediction) | Enable immediately |
| Smart thermostat adapter | Low (cloud API, no hardware) | High (HVAC state at high confidence) | Add when available |
| Mast-lite outdoor node | Medium (mounting, weather protection) | High (outdoor/indoor divergence) | Add for v1.0 |
| Outage sensor | Medium (battery, fallback radio) | High (cross-cuts all three loops) | Add for v1.5 |
| CT clamp circuit monitor | High (panel access, electrician) | High (HVAC + sump at high confidence) | Add selectively |
| Flood node | High (site-specific install, calibration) | Medium (geography-gated) | Add only when justified |
| Weather-pm-mast | High (mast, airflow, maintenance) | Medium (second-wave outdoor) | Defer |
| Thermal pod | Very high (privacy, calibration, R&D) | Low (research-gated) | Defer |

**Design rule:** never add a higher-friction surface before all
lower-friction surfaces that provide equal or greater decision value are
stable.

## Related docs

- `integrated-parcel-system-spec.md`
- `version-and-promotion-matrix.md`
- `node-taxonomy.md`
- `sensor-placement-and-representativeness-guide.md`
- [`parcel-kit/field-hardening-checklist.md`](https://github.com/lumenaut-llc/oesis-hardware/blob/main/parcel-kit/field-hardening-checklist.md)
- [`parcel-kit/pilot-field-kit.md`](https://github.com/lumenaut-llc/oesis-hardware/blob/main/parcel-kit/pilot-field-kit.md)
