# Build Guide

## Summary

Build a USB-powered indoor air node around an ESP32-S3 with one SHT45 and one BME688 on the same I2C bus. The MVP goal is a stable bench prototype that can sample once every 10 to 60 seconds and emit structured packets for local inspection and later ingest.

## Required tools

- soldering iron with fine tip
- solder
- flush cutters and small pliers
- breadboard or small perfboard
- multimeter
- USB-C cable for programming and power

## Required materials

- 1 ESP32-S3 development board with 3.3 V logic
- 1 SHT45 breakout
- 1 BME688 breakout
- jumper wires, preferably short
- breadboard or perfboard and headers
- optional standoffs or a small vented enclosure for sheltered use

## Assembly steps

1. Confirm the ESP32-S3 board exposes `3V3`, `GND`, `SDA`, and `SCL`.
2. Solder headers to the ESP32-S3 and sensor breakout boards if they are not preinstalled.
3. Place the controller and both sensors on a breadboard or perfboard with enough clearance for airflow.
4. Connect both sensors to the shared `3V3`, `GND`, `SDA`, and `SCL` rails.
5. Keep I2C leads short and routed away from noisy USB or antenna areas when possible.
6. Power the board over USB and confirm the controller boots before loading application firmware.
7. Flash test firmware that scans the I2C bus and verifies both expected sensor addresses.
8. Once the scan is stable, load the sampling firmware and verify packets over serial before enabling Wi-Fi forwarding.

## Wiring notes

- Both sensors share the same I2C bus.
- Use 3.3 V power only unless a specific breakout board explicitly documents safe regulation and level shifting.
- Start with bench wiring under 20 cm total per sensor lead.
- Avoid sealing the sensors inside an airtight case; both require airflow to be useful.

## Firmware setup

1. Assign a stable `node_id` such as `bench-air-01`.
2. Set the sample cadence to 15 seconds for bench validation or 60 seconds for quiet long-run testing.
3. Enable serial JSON output first.
4. If Wi-Fi transport is enabled, keep serial logging on until the ingest path is stable.
5. Store firmware version, board type, and sensor presence in every boot log and periodic health message.

## First test procedure

1. Boot the node and confirm both sensors are detected.
2. Verify temperature, humidity, and pressure values are plausible for the room.
3. Confirm gas resistance is nonzero and changing gradually rather than remaining fixed.
4. Leave the node stationary for 30 minutes and inspect drift and packet continuity.
5. Trigger a gentle step change by breathing near the sensors briefly or moving the node to another room.
6. Confirm the packets show a clear trend without sensor lockups or resets.

## Field-test notes

This version is for indoor or sheltered testing only. If it is used on a porch or in a garage, avoid direct rain, direct sun on the enclosure, and positions immediately adjacent to HVAC exhaust or combustion sources unless that bias is intentional for a test.

## Maintenance

- inspect wiring whenever packet dropouts or missing sensor reads appear
- recheck sensor detection after firmware changes
- keep vents and sensor faces free of dust
- repeat a short reference check after any major relocation

## Safety notes

- Power only from known-good USB sources.
- Do not place the node where condensation, splashes, or conductive debris can reach exposed wiring.
- Do not use this prototype as a life-safety detector.

## Links to related docs

- `README.md`
- `wiring.md`
- `firmware-notes.md`
- `calibration.md`
