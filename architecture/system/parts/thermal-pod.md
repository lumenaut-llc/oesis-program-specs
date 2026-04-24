# thermal-pod

## One-line summary

Research-gated scene-level thermal sensor (fixed field-of-view IR array). Kept outside the default pilot until contract, usefulness, and privacy posture are clearer. Deliberately held at a deployment-maturity tier below `v1.0` — the point is to avoid inheriting a deployability claim from the rest of the kit while the privacy and scene-framing questions are unresolved.

## Deployment posture

- **Deployment class:** `outdoor` (research) — fixed-scene semi-outdoor placement, per [`../node-taxonomy.md`](../node-taxonomy.md) research-gated table and [`../integrated-parcel-system-spec.md`](../integrated-parcel-system-spec.md) "Deployment posture per node".
- **Power tier:** `mains` — Pi-based platform; power budget for ongoing thermal readout + durable storage.
- **IP tier:** `IP54` baseline; installation-specific.
- **Transport tier:** `Wi-Fi` — research lane; no LoRa/cellular fallback in scope.
- **Protective fixtures:**
  - Hooded enclosure with documented field-of-view (privacy-reviewed).
- **Sensor variants:**
  - Scene thermal: MLX90640 or equivalent 32×24 thermal array.

## Version evolution

| Build version | Status | Spec path | Notes |
|---|---|---|---|
| `v0-1` (planned) | not yet drafted | `oesis-builds/specs/thermal-pod/v0-1.md` — **does not exist** | Skeleton proposal at [`../../../meta/proposals/oesis-builds-node-skeletons.md`](../../../meta/proposals/oesis-builds-node-skeletons.md) Skeleton 4. |

Hardware research at [oesis-hardware/v0.1/thermal-pod/](https://github.com/lumenaut-llc/oesis-hardware/tree/main/v0.1/thermal-pod).

## Calibration posture

Governed by [`../calibration-program.md`](../calibration-program.md) (physical-sensor program).

- **Deployment-maturity target:** **intentionally < `v1.0`** — stays at `v0.1` (bench prototype) until scene-contract, usefulness, and retention posture clear the privacy review. This is not a calibration deficiency; it is a research-lane posture.
- **`research_gated: true`** flag in the planned §F block — signals admissibility tooling to reject thermal-pod readings from production coefficient-fit datasets per [`../calibration-program.md`](../calibration-program.md) §C.
- **Reference instruments:** thermal-scene reference = co-located hand-held IR thermometer plus documented surface emissivity. Not yet populated.
- **Burn-in:** 24 h — thermal arrays require warmup for stable offset.
- **Protective fixture verification:** field-of-view privacy review is the gating fixture acceptance, not a physical loading test. A node without privacy-reviewed FOV is inadmissible.
- **Admissibility status:** not admissible to production datasets by design while research-gated.
- **§F build-spec metadata block:** planned — skeleton in the proposal.

## Role in each program-phase

| Phase | Role | Notes |
|---|---|---|
| All pre-1.0 slices and `v1.0` | **not in scope** | Kept outside the critical path for the first parcel kit per [`../../current/milestone-roadmap.md`](../../current/milestone-roadmap.md) "Separate research lane". |
| `v1.5` (capability-stage bridge) | not in scope | v1.5 bridge uses indoor-response-node + circuit-monitor, not thermal. |
| Future (post-v1.5, privacy review pending) | promotable to production lane **only if** contract + usefulness + retention posture clear | Will then follow standard calibration-program §G progression. |

## Cross-repo link map

| Concern | Location |
|---|---|
| Architecture posture row | [`../node-taxonomy.md`](../node-taxonomy.md) research- or privacy-gated; [`../integrated-parcel-system-spec.md`](../integrated-parcel-system-spec.md) research lane |
| Hardware research | [oesis-hardware/v0.1/thermal-pod/](https://github.com/lumenaut-llc/oesis-hardware/tree/main/v0.1/thermal-pod) |
| Build spec | **missing** — skeleton in [`../../../meta/proposals/oesis-builds-node-skeletons.md`](../../../meta/proposals/oesis-builds-node-skeletons.md) |
| Runtime normalizer | not yet implemented |
| Packet schema | `oesis.thermal-pod.v1` → `thermal.scene.snapshot` — planned; not yet in contracts |
| Gap register entries | none today (research lane is not blocking any promotion) |

## Known gotchas

- **Privacy, not calibration, is the load-bearing blocker.** A calibrated thermal-pod without a reviewed field-of-view is still inadmissible. The order of work is privacy review first, then calibration.
- **Emissivity matters.** Scene thermal readings depend on surface emissivity assumptions. Calibration without documented surface properties is not traceable.
- **Not a hazard sensor.** Thermal-pod produces scene context. It does not make hazard claims about occupants or spaces; see [`../vision-and-use-cases.md`](../vision-and-use-cases.md) for research-lane framing.

## Related

- [`../node-taxonomy.md`](../node-taxonomy.md) research-gated section
- [`../../current/milestone-roadmap.md`](../../current/milestone-roadmap.md) "Separate research lane"
- [`../vision-and-use-cases.md`](../vision-and-use-cases.md) — use-case surface
- [`circuit-monitor.md`](circuit-monitor.md) — sibling specialized lane (v1.5 bridge)
