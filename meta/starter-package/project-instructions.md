Project name: Open Source DIY Tech — Resilient Home Intelligence

Use these instructions as the shared context for all chats in this project.

This project is for a dwelling-scale environmental sensing and parcel-safety platform inside Open Source DIY Tech.
It is meant to become a decentralized, democratic, parcel-first climate adaptation system over time, but the current implementation scope remains staged and technically conservative.

Core principles:
- The parcel is the main object, not the sensor.
- The platform computes parcel-level conditions and statuses using parcel priors, local sensor data if present, nearby shared sensor data if present, and external public data integrated only inside the platform.
- Parcel operators own their raw data.
- Sharing is opt-in and can be scoped by what is shared, at what precision, when, and with whom.
- Shared intelligence should be derived, bounded, revocable, and community-safe rather than a path to household surveillance.
- The system must work under partial adoption: every parcel gets a status, but confidence and precision improve as more nodes participate.
- The first hazards to focus on are smoke, pluvial flooding/runoff, and heat.
- The project includes both software and physical sensor prototypes.
- Outputs should remain modular, open-source-friendly, well-documented, and suitable for smaller standalone builds that also combine into a larger system.
- Always distinguish between private owner data, shared community data, external public data, and derived parcel states.
- Always surface confidence and evidence mode honestly: observed_local, inferred_neighbors, inferred_regional, or stale.
- Always distinguish four tradeoffs: absolute accuracy, local recency, parcel relevance, and parcel operator agency.

Canonical version map:
- `current v1` = parcel sensing and inference baseline
- `v1.5` = measurement-to-intervention foundation
- `v2` = bounded adaptation guidance
- `v2.5` = bounded controls and compatibility mapping
- `v3` = parcel adaptation engine
- `v4` = parcel + route + block resilience

Scope boundary:
- `current v1` should prove parcel-first sensing and inference under partial adoption.
- `v1.5` is the first minimum bridge into house-state, intervention, controllability, and verification data.
- Later stages may add guidance, compatibility mapping, bounded controls, and route/block resilience, but those should not be backfilled into `current v1` as if already implemented.

Preferred operating style:
- Keep recommendations practical and buildable.
- Prefer modular phased roadmaps over all-at-once solutions.
- Preserve consistency with the canonical project files.
- When working in a narrower chat, optimize for that workstream without losing alignment with the whole system.
- When a fresh chat needs the long-horizon staged roadmap, use `path-forward-prompt-packet.md` as the source of truth.
