# Open Questions

- What is the first acceptable trust model for homeowner-run nodes: shared secret, per-node token, signed payloads, or private-network-only?
- Should raw packets be stored forever for defensive publication and debugging, or pruned after normalization plus audit retention?
- How should the ingest service handle clock drift from nodes without reliable NTP?
- When a node sends partial data, should normalization emit one observation with missing fields or split into multiple observation records by sensor family?
- Which transport should be canonical for the MVP: HTTPS push, MQTT, local gateway upload, or serial-to-bridge forwarding?
