# Hardware

Hardware subsystems are designed as standalone builds that also become inputs to the broader parcel platform.

Read `NOTICE.md` before treating this subtree as a complete released hardware design package.

## Design rules

- keep nodes modular
- separate sensors when placement requirements differ
- prefer stable, documented modules over custom boards in v0.x
- keep each node useful on its own
- publish calibration and maintenance notes alongside build steps
- distinguish bench prototypes from field-ready nodes with an explicit deployment maturity label
- treat field-hardening parts as part of the node, not as optional support gear once a node is described as deployed

## Cross-subsystem reference

Use `../architecture/system/integrated-parcel-system-spec.md` as the canonical document for how all current hardware families attach to one parcel, one software stack, and one governance surface.
Use `../architecture/current/README.md` as the current versioned
reference-architecture entrypoint for the broader system.
Use `../architecture/system/deployment-maturity-ladder.md` and `../hardware/parcel-kit/field-hardening-checklist.md` as the canonical references for when a node family is still `deployment maturity v0.1` versus ready to target `deployment maturity v1.0` or above.
