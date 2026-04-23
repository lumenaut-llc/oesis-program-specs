# circuit-monitor

## One-line summary

**Tier 3 direct-measurement adapter** (not a parcel-sensing hardware node in the taxonomy sense). Non-invasive current-draw monitoring via CT clamps on HVAC and sump circuits; produces HIGH-confidence equipment-state signals for house-state reasoning at capability-stage v1.5. Governed by the **adapter-trust program**, not the calibration program. Optional equipment-state module — not part of the default Tier 1-2 parcel kit.

## Deployment posture

This node has a **dual posture**: it is an adapter (Tier 3) by how it feeds evidence into inference, and a physical device by how it is installed. Both postures are declared.

### Adapter posture (per [`../adapter-trust-program.md`](../adapter-trust-program.md) §F)

- **Tier:** `tier_3_direct` — direct measurement via CT clamp current.
- **Source authority:** the PZEM-004T/016 module reading the CT clamp; pinned contract version = `pzem-004t-v3-serial`.
- **Cross-check reference:** none required — Tier 3 is the highest tier; no higher source to cross-check against.

### Physical posture (per [`../deployment-maturity-ladder.md`](../deployment-maturity-ladder.md) Deployment-class standards and [`../integrated-parcel-system-spec.md`](../integrated-parcel-system-spec.md) "Deployment posture per node")

- **Deployment class:** `mains-adjacent` (indoor, inside or near electrical panel).
- **Power tier:** low-power from measured circuit.
- **IP tier:** electrical-enclosure IP20.
- **Transport tier:** Wi-Fi.
- **Protective fixtures:** electrical-code-compliant CT clamp installation — licensed electrician required in many jurisdictions.
- **Sensor variants:** PZEM-004T or PZEM-016 module + split-core CT clamps.

## Version evolution

| Build version | Status | Spec path | Notes |
|---|---|---|---|
| `v0-1` (planned) | not yet drafted | `oesis-builds/specs/adapters/circuit-monitor/v0-1.md` — **does not exist** | Spec lives under `specs/adapters/` subtree (per [`../adapter-trust-program.md`](../adapter-trust-program.md) §F) rather than `specs/<node>/`. Skeleton proposal at [`../../../meta/proposals/oesis-builds-node-skeletons.md`](../../../meta/proposals/oesis-builds-node-skeletons.md) Skeleton 5. |

Hardware at [oesis-hardware/v1.5/circuit-monitor/](https://github.com/lumenaut-llc/oesis-hardware/tree/main/v1.5/circuit-monitor).

## Trust posture

Governed by [`../adapter-trust-program.md`](../adapter-trust-program.md) — **not** calibration-program (this is a deliberate architectural split: calibration-program is for physical-sensor drift; adapter-trust-program is for source-authority and contract-version discipline).

- **Deployment-maturity target:** `v1.5` (trust hardening).
- **Source authority file:** `oesis-builds/procedures/adapters/circuit-monitor/source.md` — to author.
- **Onboarding gate:** installation-code-compliance acceptance test; initial verification window 24 h.
- **Cross-check:** none required per tier (Tier 3 is the reference).
- **Drift policy:** schema-drift detection on PZEM firmware version changes; cross-adapter consistency audits when multiple circuit-monitors exist per parcel.
- **Credential model:** none (direct serial; no cloud auth).
- **Admissibility status:** not admissible today (no build spec, no source authority file, no onboarding verification).
- **§F build-spec metadata block:** planned — skeleton in the proposal.

## Role in each program-phase

| Phase | Role | Notes |
|---|---|---|
| All pre-1.0 slices and `v1.0` | **not in scope** | Default Tier 1–2 parcel kit does not include circuit-monitor. |
| `v1.5` (capability-stage bridge) | **Tier 3 equipment-state source** | Feeds `hvac_mode`, `sump_state`, `equipment_running`, and power draw into house-state. Highest-confidence tier per [`../node-taxonomy.md`](../node-taxonomy.md) tiered acquisition model. |
| `v2` (guidance) / `v2.5` (bounded controls) | unchanged role as evidence source | Control-side adapters (Matter / Home Assistant / BACnet) are separate Tier 2 adapters; circuit-monitor remains read-side. |

## Cross-repo link map

| Concern | Location |
|---|---|
| Architecture posture row | [`../node-taxonomy.md`](../node-taxonomy.md) `v1.5` bridge table; [`../integrated-parcel-system-spec.md`](../integrated-parcel-system-spec.md) "Deployment posture per node" |
| Hardware design | [oesis-hardware/v1.5/circuit-monitor/](https://github.com/lumenaut-llc/oesis-hardware/tree/main/v1.5/circuit-monitor) |
| Build spec | **missing** — skeleton in [`../../../meta/proposals/oesis-builds-node-skeletons.md`](../../../meta/proposals/oesis-builds-node-skeletons.md) at `specs/adapters/circuit-monitor/v0-1.md` path |
| Runtime normalizer | `oesis.ingest.v1_0.normalize_circuit_monitor_packet` (implemented per [`../../current/implementation-posture.md`](../../current/implementation-posture.md) "Additional normalization") |
| Packet schema | `oesis.circuit-monitor.v1` → `equipment.circuit.snapshot` — [oesis-contracts/v1.0/circuit-monitor-observation-schema.md](https://github.com/lumenaut-llc/oesis-contracts/blob/main/v1.0/circuit-monitor-observation-schema.md) |
| Equipment-state bridge | [oesis-contracts/v1.0/schemas/equipment-state-observation.schema.json](https://github.com/lumenaut-llc/oesis-contracts/blob/main/v1.0/schemas/equipment-state-observation.schema.json) |
| Gap register entries | **G18** (adapter-trust execution — circuit-monitor is one of the adapters this gap covers), **G17** (adapter-derived observation-schema facts) |

## Known gotchas

- **Electrical code compliance is a hard prerequisite.** Installation on live mains circuits requires licensed electrician in many jurisdictions. This is a deployment gate, not a spec item.
- **Adapter vs physical-sensor confusion.** Circuit-monitor blurs the line. By the taxonomy it is an adapter (Tier 3, equipment-state). By installation it is a physical device that consumes mains-adjacent power. Its §F metadata block carries both an adapter section and a `physical_posture` section.
- **Optional, not default.** Do not treat circuit-monitor as required for a v1.5 parcel kit. Tier 1 (passive inference) and Tier 2 (cloud API) are acceptable alternatives for `hvac_mode` and similar fields; Tier 3 is added selectively where HIGH confidence matters (for example smoke-protect verification).
- **Recirculate vs fresh-air indistinguishable** from current draw alone — classification collapses to "fan on" without damper-position knowledge. Tier 1 (thermal-slope inference) shares this limitation.

## Related

- [`../node-taxonomy.md`](../node-taxonomy.md) `v1.5` bridge tiered acquisition model
- [`../adapter-trust-program.md`](../adapter-trust-program.md) — governing policy for this part
- [`../../v1.5/house-state-and-verification-model.md`](../../v1.5/house-state-and-verification-model.md) — where circuit-monitor evidence feeds
- [`../architectural-choices-by-stage.md`](../architectural-choices-by-stage.md) row v1.5
- [`thermal-pod.md`](thermal-pod.md) — other research/specialty-lane part sheet
