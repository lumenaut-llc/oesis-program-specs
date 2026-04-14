# Open Questions

- What minimum evidence threshold should allow the engine to emit `safe`, `caution`, or `unsafe` instead of `unknown`?

  > **Recommended direction:** At least 1 local node with health OK and freshness < 15 minutes. Public context alone moves evidence_mode to public_only but should not produce non-unknown status without local confirmation.

- Should the first version score smoke, heat, and flood independently with hand-tuned rules before any learned models are introduced?

  > **Recommended direction:** Hand-tuned rules first for all three hazards. No learned models until at least 6 months of multi-parcel pilot data exists. Rules are auditable and explainable; models can be layered later.

- How should conflicting evidence be surfaced when local sensors and public feeds disagree?

  > **Recommended direction:** Surface disagreement explicitly in the reasons array. Never silently average conflicting signals. If local and public disagree, report both with a 'conflicting evidence' flag and lower confidence.

- How should parcel-specific features such as basement presence, slope, or defensible space enter the model if they are missing for many parcels?

  > **Recommended direction:** Treat missing features as unknown, not as defaults. Use conservative fallbacks (e.g., assume no basement if unknown) and disclose the assumption in reasons. Do not impute features.

- What recomputation cadence is needed when no new evidence arrives but public context changes?

  > **Recommended direction:** Recompute on public context change if last recomputation > 15 minutes old. Recompute on any new local observation. Do not recompute more often than every 5 minutes.

- Which public context sources should be considered strong enough to move evidence mode from `insufficient` to `local_plus_public`?

  > **Recommended direction:** NWS weather alerts and AirNow PM2.5 are strong enough for local_plus_public when paired with local evidence. Generic forecast APIs are supporting context only, not strong enough to shift evidence mode.

- For the first smoke closed loop, what exact verification rule should count as improvement over a 30–90 minute response window?

  > **Recommended direction:** For v1.5 bridge, a successful verification is defined as indoor PM2.5 returning to within 20% of pre-event baseline within the response window. The 30-90 minute window starts from the recorded intervention timestamp.

- How should future house-state and equipment-state bridge objects influence recommendations without silently changing the baseline parcel-state meaning?

  > **Recommended direction:** House-state should inform recommendation content (e.g., 'close windows' only if windows are reported open) but must never change parcel-state status or confidence. Parcel-state reflects hazard reality; house-state reflects response capacity.
