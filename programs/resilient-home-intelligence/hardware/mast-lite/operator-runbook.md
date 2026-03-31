# Operator Runbook

## Purpose

Provide the shortest repeatable path from first mast-lite wiring to a locally validated normalized observation.

## Before you start

- ESP32-S3 DevKitC-1 wired with `GPIO8` as `SDA` and `GPIO9` as `SCL`
- SHT45 connected first
- BME680 ready to add after the first scan passes
- radiation shield or similarly shaded vented placement planned for the SHT45
- Arduino IDE or PlatformIO workflow installed

## Stage 1: bench scan

1. Flash `firmware/mast_lite_i2c_scanner/mast_lite_i2c_scanner.ino`
2. Open the serial monitor at `115200`
3. Confirm `0x44` first, then `0x76` or `0x77` after adding the BME680

## Stage 2: bench packet check

1. Flash `firmware/mast_lite_serial_json/mast_lite_serial_json.ino`
2. Confirm one JSON packet line every 5 seconds
3. Copy one packet line into `packet.json`

## Stage 3: local ingest validation

From `repo/programs/resilient-home-intelligence/software/ingest-service/`:

```bash
python3 scripts/ingest_packet.py packet.json
```

If you captured a full serial log:

```bash
python3 scripts/extract_latest_packet.py serial.log --output packet.json
python3 scripts/ingest_packet.py packet.json
```

## Stage 4: sheltered outdoor move

1. Place the SHT45 in the shielded or best-ventilated position
2. Keep the controller and BME680 dry and sheltered
3. Rerun the same packet checks after mounting

## Pass criteria

- scanner finds `0x44` and `0x76` or `0x77`
- serial JSON sketch prints valid packets every 5 seconds
- local ingest validation succeeds
- sheltered outdoor placement does not cause resets or vanishing devices during a 30 to 60 minute run
