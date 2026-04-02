# Parcel Kit Procurement Checklist

## Purpose

Turn the parcel-kit BOM into a practical buying and receiving checklist for the first two deployment tiers.

This document is optimized for a strong timeline and a first integrated parcel kit that a non-author can assemble with minimal guesswork.

## Scope

This checklist covers:

- Tier 1: one `bench-air-node`
- Tier 2: one `bench-air-node` plus one `mast-lite`

This checklist does not treat `flood-node`, `weather-pm-mast`, or `thermal-pod` as part of the default first purchase.

## Build rule

Standardize aggressively for the first parcel kit:

- use the same ESP32-S3 controller family in both nodes
- use the same SHT45 and BME680 sensor pairing in both nodes
- use USB power for first bring-up on both nodes
- defer richer outdoor, flood, and thermal hardware until the first indoor and sheltered-outdoor pair is stable

## Before ordering

Confirm these decisions first:

- Tier target:
  `Tier 1` if the goal is fastest indoor proof and software validation
  `Tier 2` if the goal is the first integrated parcel kit with indoor and sheltered-outdoor coverage
- Controller choice:
  one ESP32-S3 DevKitC-1 variant with 3.3 V logic for every first-wave node
- Sensor stack:
  SHT45 plus BME680 for both Tier 1 and Tier 2
- Outdoor posture:
  `mast-lite` should start under an eave, porch roof, or similar sheltered location
- Transport posture:
  serial JSON first, then `https_push` after bring-up succeeds

Do not buy mixed controller families or alternate sensor stacks for the first parcel kit unless there is a specific test reason.

## Tier 1 purchase list

Buy these items before starting a `bench-air-node` build:

| Qty to use | Recommended buy qty | Item | Why it is needed |
| --- | --- | --- | --- |
| 1 | 1 to 2 | ESP32-S3 DevKitC-1 | controller, USB power, and flashing path |
| 1 | 1 to 2 | SHT45 breakout | primary temperature and humidity |
| 1 | 1 to 2 | BME680 breakout | pressure and gas-trend support |
| 1 | 1 to 2 | USB-C data cable | flashing and power |
| 1 | 1 | USB power supply | simple bring-up power |
| 1 | 1 | breadboard or small perfboard | first assembly platform |
| 1 set | 1 to 2 sets | short jumper wires and header pins | shared I2C bus wiring |
| 1 | 1 | solder and basic hand tools | header and wiring work |

Recommended strong-timeline spares:

- one extra ESP32-S3 board
- one extra SHT45 breakout
- one extra BME680 breakout
- one extra USB data cable
- extra header pins and short jumper wires

## Tier 2 add-on purchase list

Buy these items in addition to the Tier 1 purchase list before starting `mast-lite`:

| Qty to use | Recommended buy qty | Item | Why it is needed |
| --- | --- | --- | --- |
| 1 | 1 to 2 | second ESP32-S3 DevKitC-1 | dedicated outdoor controller |
| 1 | 1 to 2 | second SHT45 breakout | outdoor primary temperature and humidity |
| 1 | 1 to 2 | second BME680 breakout | outdoor pressure and gas-trend support |
| 1 | 1 | radiation shield or ventilated guard | reduce solar and surface-heating bias on the SHT45 |
| 1 | 1 | vented enclosure | protect controller and wiring while preserving airflow |
| 1 | 1 | sheltered mount or eave hardware | secure outdoor placement |
| 1 set | 1 to 2 sets | strain relief, cable ties, and mounting fasteners | keep outdoor wiring stable |

Optional for later, not first purchase:

- UV sensor for `mast-lite`
- upgraded outdoor power path
- richer mast hardware that belongs with `weather-pm-mast`

## Shared purchasing checks

Before finalizing an order, confirm:

- every sensor breakout is compatible with 3.3 V logic
- the controller exposes `3V3`, `GND`, `GPIO8`, and `GPIO9`
- the SHT45 and BME680 breakouts can operate over I2C
- you have enough headers for every breakout board
- you have at least one known-good USB data cable per node under test
- outdoor parts are for sheltered deployment first, not full-exposure weather claims

## Receiving checklist

When parts arrive:

1. Label each controller and sensor set for its intended node:
   `bench-air-01` or `mast-lite-01`
2. Keep one bag or bin per node so indoor and outdoor parts do not get mixed.
3. Inspect sensor headers, pins, and breakout boards for bent pins or cracked solder pads.
4. Set aside one controller and one sensor pair as spares if timeline pressure is high.
5. Record any board revisions or breakout variants that could affect wiring labels or I2C addresses.

## Bring-up sequence after purchase

Do not assemble both nodes at once.

Use this order:

1. Finish `bench-air-node` first.
2. Validate the SHT45 alone at `0x44`.
3. Add the BME680 and validate `0x76` or `0x77`.
4. Run the serial JSON sketch and local ingest validation.
5. Only after Tier 1 is stable, start `mast-lite` with the same sensor stack and pin map.
6. Bench-validate `mast-lite` before closing any enclosure or mounting outdoors.
7. Move `mast-lite` to a sheltered outdoor position and rerun packet checks.

Primary build docs:

- `../../hardware/bench-air-node/build-guide.md`
- `../../hardware/bench-air-node/operator-runbook.md`
- `../../hardware/mast-lite/build-guide.md`
- `../../hardware/mast-lite/operator-runbook.md`
- `parcel-installation-checklist.md`

## Software handoff checklist

Before calling the hardware purchase complete, confirm:

- a stable `node_id` is chosen for each controller
- the parcel node-registry record is ready or updated for the purchased nodes
- serial packet output matches the expected family contract
- local ingest validation succeeds for each node before any live transport work

Primary software and system references:

- `../data-model/node-registry-schema.md`
- `../system-overview/integrated-parcel-system-spec.md`
- `../../../../Makefile`

## Legal and release handoff notes

Procurement and build docs are not automatically public-preview-safe.

Before sharing photos, diagrams, or detailed purchase bundles outside the core implementation group, check:

- `../../legal/public-preview-scope.md`
- `../release/2026-04-14/reviewer-packet-index.md`

Do not assume close-up internals, wiring layouts, or integrated-kit details belong on the public preview site.

## Do not buy these by default yet

Defer these unless the parcel needs them and the project is ready for the extra complexity:

- `flood-node` parts such as the MB7389 and low-point mounting hardware
- `weather-pm-mast` parts such as the SPS30 and richer mast hardware
- `thermal-pod` parts such as the Raspberry Pi 5 and MLX90640

Those systems remain optional, second-wave, or separate-lane hardware.
