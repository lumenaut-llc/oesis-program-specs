# Chat Prompts

Use the shared project context below at the top of each new workstream chat.

## Shared project context
I am building Open Environmental Sensing and Inference System (OESIS), a parcel-first, dwelling-scale environmental sensing and parcel-awareness program. Resilient Home Intelligence (RHI) is a legacy compatibility name during the transition. The work is intended to grow into a decentralized, democratic climate adaptation system over time. The parcel is the main object, not the sensor. The platform should determine parcel-level conditions and statuses using parcel priors, local sensors if present, nearby shared sensors if present, and external public data integrated only inside the platform. Parcel operators own their raw data. Sharing is opt-in and should improve collective intelligence without forcing exposure of exact parcel-linked raw data. The system must work under partial adoption: every parcel gets a status, but confidence and precision improve as more nodes participate. The first hazards to focus on are smoke, pluvial flooding/runoff, and heat.

Use this version taxonomy:
- `current v1` = parcel sensing and inference baseline
- `v1.5` = measurement-to-intervention foundation
- `v2` = bounded adaptation guidance
- `v2.5` = bounded controls and compatibility mapping
- `v3` = parcel adaptation engine
- `v4` = parcel + route + block resilience

Important framing:
- `current v1` should prove sensing and inference, not pretend to be a full adaptation or automation system.
- `v1.5` is the minimum bridge stage where the system begins collecting house-state, controllability, intervention, and verification data.
- Always distinguish absolute accuracy, local recency, parcel relevance, and parcel operator agency.
- Always evaluate whether a design choice strengthens or weakens decentralization, replicability, and parcel operator control.

For the full long-horizon staged roadmap, use `path-forward-prompt-packet.md`.

## Master coordination
Please act as the master coordinator for this project: keep the overall architecture coherent, track workstreams, identify dependencies, sequence milestones, and help me connect software, hardware, legal, documentation, governance, and cost planning into one roadmap without confusing current `v1` scope with later stages.

## Major project architecture
Please help me design the full product architecture, user model, core objects, hazard logic, and staged scope for a parcel-first dwelling-scale, parcel-first platform that begins with sensing/inference and later grows into parcel adaptation.

## Software engineering
Please help me design the code architecture, database schema, staged data models, API routes, processing pipeline, permissions model, and frontend information architecture for this platform while preserving the current `v1` parcel-state baseline.

## Inference and modeling
Please help me design hazard-specific scoring formulas, confidence logic, neighbor inference, uncertainty penalties, observed-vs-inferred rules, and a staged path from parcel sensing to building-response and intervention models later.

## Physical prototype and hardware systems
Please help me design modular hardware systems in stages: bench air node, outdoor mast-lite, weather/PM mast, flood node, and 2D thermal pod. Keep the hardware practical, dwelling-scale and DIY-friendly, and compatible with a future `v1.5` bridge into house-state and intervention verification.

## Bench node
Please focus only on an ESP32-S3 with an SHT45 and BME688 so I can learn the wiring, firmware, and data upload path.

## Flood node
Please focus on an outdoor ultrasonic distance-based setup, likely using the MB7389 and an ESP32, for a standalone runoff/flood node.

## 2D thermal pod
Please focus on a Raspberry Pi 5 and MLX90640 thermal array as the first version of a simple 2D sensing pod.

## Procurement
Please help me create a staged procurement plan with small useful bundles, accessory details, and approximate costs.

## Documentation
Please help me define the documentation structure for hardware builds, software architecture, calibration procedures, data schemas, API specs, permissions/provenance, testing protocols, maintenance, installation guides, and staged capability boundaries from `current v1` through `v4`.

## Legal / IP / open source
Please help me design the legal and IP strategy, including licensing, defensive publication, contribution terms, patent-risk considerations, and the relationship between parcel-linked data stewardship, platform governance, and later bounded control surfaces.

## Governance / privacy
Please help me design permissions, custody types, provenance, data export/deletion rights, private vs shared views, control-permission boundaries, and the product rules that make ownership, trust, and decentralization real.

## Pilot / deployment
Please help me scope a one-block or small neighborhood pilot with partial adoption, including host-home selection, installation planning, minimum viable node count, pilot success metrics, maintenance expectations, and a path from `current v1` pilot evidence into `v1.5` response and intervention data.

## Path forward evaluation
Please use `path-forward-prompt-packet.md` and critically evaluate the path from the current `v1` parcel-sensing baseline to a serious parcel adaptation system. Tell me what stays in baseline, what gets added at `v1.5`, what moves to later stages, what is too speculative, and what the best first closed-loop implementation should be.
