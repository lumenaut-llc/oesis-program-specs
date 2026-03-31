# Firmware Scaffold

## Purpose

Provide a minimal ESP32 bring-up sketch that emits the agreed `rhi.bench-air.v1` packet shape over serial before sensor-library integration and network transport are added.

## Current contents

- `bench_air_node_serial_json/bench_air_node_serial_json.ino`
  Minimal Arduino-style sketch for ESP32-S3 that prints one JSON packet per line at `115200`

## First run

1. Open `bench_air_node_serial_json.ino` in the Arduino IDE or another ESP32-capable workflow
2. Select the ESP32-S3 board
3. Confirm the sketch still uses `GPIO8` for `SDA` and `GPIO9` for `SCL`
4. Flash the board
5. Open the serial monitor at `115200`
6. Confirm you see one valid JSON object per line every 5 seconds

## Current limitations

- the sketch uses placeholder sensor values so it can compile without external sensor libraries
- `observed_at` is a placeholder timestamp until real time is available
- Wi-Fi transport is not enabled

The immediate goal is to prove packet shape and ingest compatibility first. Sensor-library integration can replace the placeholder read functions next.
