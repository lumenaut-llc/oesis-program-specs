# Hardware

Hardware subsystems are designed as standalone builds that also become inputs to the broader parcel platform.

Read `NOTICE.md` before treating this subtree as a complete released hardware design package.

## Design rules

- keep nodes modular
- separate sensors when placement requirements differ
- prefer stable, documented modules over custom boards in v0.x
- keep each node useful on its own
- publish calibration and maintenance notes alongside build steps

## Cross-subsystem reference

Use `../docs/system-overview/integrated-parcel-system-spec.md` as the canonical document for how all current hardware families attach to one parcel, one software stack, and one governance surface.
Use `../technical-architecture/v0.1/README.md` as the current versioned
reference-architecture entrypoint for the broader system.
