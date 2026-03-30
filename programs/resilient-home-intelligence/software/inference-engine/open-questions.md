# Open Questions

- What minimum evidence threshold should allow the engine to emit `safe`, `caution`, or `unsafe` instead of `unknown`?
- Should the first version score smoke, heat, and flood independently with hand-tuned rules before any learned models are introduced?
- How should conflicting evidence be surfaced when local sensors and public feeds disagree?
- How should parcel-specific features such as basement presence, slope, or defensible space enter the model if they are missing for many parcels?
- What recomputation cadence is needed when no new evidence arrives but public context changes?
