# Firmware Scaffold

## Purpose

Provide a minimal ESP32 bring-up sketch that emits the agreed `rhi.bench-air.v1` packet shape over serial before sensor-library integration and network transport are added.

## Current contents

- `bench_air_node_i2c_scanner/bench_air_node_i2c_scanner.ino`
  Minimal I2C scanner for `GPIO8` and `GPIO9`
- `bench_air_node_serial_json/bench_air_node_serial_json.ino`
  Arduino-style sketch for ESP32-S3 that reads SHT45 and BME680, then prints one JSON packet per line at `115200`

## Arduino libraries

Install these libraries before compiling the serial JSON sketch:

- `Adafruit SHT4x Library`
- `Adafruit BME680 Library`
- `Adafruit Unified Sensor`

## First run

1. Open `bench_air_node_i2c_scanner.ino` in the Arduino IDE or another ESP32-capable workflow
2. Select the ESP32-S3 board
3. Confirm the sketch still uses `GPIO8` for `SDA` and `GPIO9` for `SCL`
4. Flash the scanner sketch and open the serial monitor at `115200`
5. Confirm the SHT45 appears at `0x44`
6. Add the BME680 and confirm it appears at `0x76` or `0x77`
7. Open `bench_air_node_serial_json.ino`
8. Flash the serial JSON sketch
9. Confirm you see one valid JSON object per line every 5 seconds

## Current limitations

- `observed_at` is still a placeholder timestamp until real time is available
- Wi-Fi transport is not enabled

The immediate goal is to prove sensor bring-up, packet shape, and ingest compatibility first. Time sync and network transport can come next.

For the full bench workflow from flash to local ingest validation, use `../operator-runbook.md`.
