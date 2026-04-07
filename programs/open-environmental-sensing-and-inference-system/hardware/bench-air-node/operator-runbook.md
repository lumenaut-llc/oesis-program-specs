# Operator Runbook

## Purpose

Provide the shortest repeatable path from freshly wired bench hardware to a locally validated normalized observation.

## Before you start

- ESP32-S3 DevKitC-1 wired with `GPIO8` as `SDA` and `GPIO9` as `SCL`
- SHT45 connected first
- BME680 ready to add after the first scan passes
- Arduino IDE or equivalent ESP32 workflow installed
- local repo available so `python3 scripts/ingest_packet.py` can be run

## Arduino libraries

Install these libraries before flashing the serial JSON sketch:

- `Adafruit SHT4x Library`
- `Adafruit BME680 Library`
- `Adafruit Unified Sensor`

## Stage 1: scan SHT45 only

1. Flash `firmware/bench_air_node_i2c_scanner/bench_air_node_i2c_scanner.ino`
2. Open the serial monitor at `115200`
3. Confirm you see `Found device at 0x44`

Expected output shape:

```text
I2C scan starting...
Found device at 0x44
Total devices found: 1
```

Stop here if `0x44` does not appear.

## Stage 2: add BME680 and scan again

1. Power off the board
2. Add the BME680 to the same `3V3`, `GND`, `SDA`, and `SCL` bus
3. Power back on with the same scanner sketch
4. Confirm you see `0x44` plus `0x76` or `0x77`

Expected output shape:

```text
I2C scan starting...
Found device at 0x44
Found device at 0x77
Total devices found: 2
```

Stop here if the second address does not appear.

## Stage 3: flash serial JSON sketch

1. Flash `firmware/bench_air_node_serial_json/bench_air_node_serial_json.ino`
2. Open the serial monitor at `115200`
3. Ignore the boot comment lines that start with `#`
4. Copy one full JSON packet line into a file named `packet.json`

Optional before flashing:

- copy `firmware/bench_air_node_serial_json/secrets.example.h` to `firmware/bench_air_node_serial_json/secrets.h`
- fill in your Wi-Fi credentials there if you want real UTC timestamps via NTP

Expected boot comments:

```text
# bench_air_node_serial_json
# I2C pin plan: SDA=GPIO8 SCL=GPIO9
```

Expected packet behavior:

- one JSON object per line
- one packet about every 5 seconds
- `sht45` and `bme680` both present when wiring is healthy
- `observed_at` is a real UTC timestamp only if Wi-Fi time sync is configured and succeeds

## Stage 4: validate locally

From `repo/programs/open-environmental-sensing-and-inference-system/software/ingest-service/` run:

```bash
python3 scripts/ingest_packet.py packet.json
```

If you prefer stdin:

```bash
python3 scripts/ingest_packet.py < packet.json
```

If you captured a whole serial monitor log with `#` boot lines, extract the newest packet first:

```bash
python3 scripts/extract_latest_packet.py serial.log --output packet.json
python3 scripts/ingest_packet.py packet.json
```

Recommended macOS capture flow:

```bash
cd ../../hardware/bench-air-node/firmware
./tools/capture_serial.sh /dev/cu.usbmodem101 serial.log
```

## Pass criteria

- scanner finds `0x44` first
- scanner finds `0x44` plus `0x76` or `0x77` after BME680 is added
- serial JSON sketch prints one valid packet line every 5 seconds
- `python3 scripts/ingest_packet.py packet.json` succeeds
- normalized output includes `temperature_c_primary`, `relative_humidity_pct_primary`, `pressure_hpa`, and `gas_resistance_ohm`

## Known first-build limitations

- `observed_at` remains a placeholder if Wi-Fi time sync is not configured or fails
- Wi-Fi is only used here for optional time sync, not packet transport
- gas resistance is useful for trend inspection, not calibrated AQI

## If something fails

- no `0x44`: recheck SHT45 power, solder, and `GPIO8`/`GPIO9` wiring
- no BME680 address: recheck `SDI` to `SDA`, `SCK` to `SCL`, and power
- JSON does not validate: copy a full packet line, not a boot comment
- mixed serial log is messy: run `python3 scripts/extract_latest_packet.py serial.log --output packet.json`
- only one sensor reports `present: false`: inspect that sensor’s solder joints and bus wiring
