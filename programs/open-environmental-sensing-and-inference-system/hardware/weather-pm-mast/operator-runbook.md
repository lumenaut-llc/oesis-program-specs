# Operator Runbook

## Purpose

Provide the shortest repeatable path from first weather-pm-mast wiring to a locally validated PM-first normalized observation.

## Stage 1: environmental bench scan

1. Flash `firmware/weather_pm_mast_i2c_scanner/weather_pm_mast_i2c_scanner.ino`
2. Confirm `0x44` first, then `0x76` or `0x77` after the BME680 is added

## Stage 2: PM-first packet check

1. Flash `firmware/weather_pm_mast_serial_json/weather_pm_mast_serial_json.ino`
2. Confirm one JSON packet line every 5 seconds
3. Copy one packet line into `packet.json`

## Stage 3: local ingest validation

From `repo/programs/open-environmental-sensing-and-inference-system/software/ingest-service/`:

```bash
python3 scripts/ingest_packet.py packet.json
```

If you captured a full serial log:

```bash
python3 scripts/extract_latest_packet.py serial.log --output packet.json
python3 scripts/ingest_packet.py packet.json
```

## Stage 4: mast move

1. Mount the environmental and PM hardware in the first outdoor mast position
2. Rerun the same packet checks after mounting
3. Watch for contamination, splash, and heat issues during a 30 to 60 minute run
