# Open Questions

- What is the first acceptable trust model for parcel operator-run nodes: shared secret, per-node token, signed payloads, or private-network-only?

  > **Recommended direction:** Private-network-only for v0.1 (serial extract or local HTTP). Shared-secret API key for v1.0 live deployment. Per-node tokens with rotation for v1.5+.

- Should raw packets be stored forever for defensive publication and debugging, or pruned after normalization plus audit retention?

  > **Recommended direction:** Retain raw packets for 90 days post-normalization for audit and debugging. Prune after 90 days unless a retention hold is in effect.

- How should the ingest service handle clock drift from nodes without reliable NTP?

  > **Recommended direction:** Accept the packet with the node's reported timestamp, but stamp ingested_at with server time. Flag drift > 60 seconds in the normalized observation's health object. Do not reject packets for clock drift alone.

- When a node sends partial data, should normalization emit one observation with missing fields or split into multiple observation records by sensor family?

  > **Recommended direction:** Emit one normalized observation with missing fields marked null rather than splitting into multiple records. Simpler provenance chain and downstream consumers already handle nulls.

- Which transport should be canonical for the MVP: HTTPS push, MQTT, local gateway upload, or serial-to-bridge forwarding?

  > **Recommended direction:** Serial-to-bridge forwarding for v0.1. HTTPS push for v1.0. MQTT deferred until multi-node density justifies it.

- What is the smallest acceptable first contract for `indoor-response-node`: PM2.5 + temperature + RH only, or should it already carry richer health fields?

  > **Recommended direction:** PM2.5 + temperature + RH as minimum. Health fields (uptime, wifi_rssi, heap_free) should be present from day one — they cost nothing and enable trust scoring.

- Should action-log and verification records enter ingest through the same service boundary as node observations, or through a separate support-object write path?

  > **Recommended direction:** Separate support-object write path through the parcel-platform API, not through ingest. Ingest handles sensor observations only. This preserves the evidence boundary between hardware telemetry and human-initiated records.
