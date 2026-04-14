# Firmware Scaffold

## Purpose

Provide a minimal ESP32 bring-up path that validates PZEM Modbus communication and emits the agreed `oesis.circuit-monitor.v1` packet shape over serial before network transport is added.

## Staging role

This firmware is a planned **v1.5 bridge** equipment-state bring-up path. It is not part of the current-truth firmware baseline for program-phase `v0.1`.

It is meant to prove the equipment-state evidence lineage for the v1.5 bridge:

- PZEM Modbus RTU communication
- current-draw based equipment state classification
- cycle detection and timing
- equipment observation packet emission

## Planned contents

No firmware files exist yet. The following sketches are planned:

- `circuit_monitor_pzem_test/circuit_monitor_pzem_test.ino`
  Minimal PZEM Modbus communication test for `GPIO16` (RX) and `GPIO17` (TX), reads and prints voltage, current, power from one or two PZEM addresses
- `circuit_monitor_address_change/circuit_monitor_address_change.ino`
  Utility sketch for reprogramming a PZEM module Modbus address (connect only one module at a time)
- `circuit_monitor_serial_json/circuit_monitor_serial_json.ino`
  Full serial JSON sketch that reads PZEM modules, classifies equipment state, tracks cycles, and prints one JSON packet per line at `115200`
- `circuit_monitor_serial_json/config.example.h`
  Copy-to-local template for circuit identity, threshold configuration, and optional Wi-Fi credentials
- `platformio.ini`
  Pinned ESP32-S3 build scaffold with separate environments for each sketch

## Expected build setup

- platform: `espressif32@6.7.0`
- board: `esp32-s3-devkitc-1`
- framework: Arduino

Recommended commands from this directory (once firmware files exist):

```bash
pio run -e circuit_monitor_pzem_test
pio run -e circuit_monitor_serial_json
```

## Arduino libraries

Install these libraries before compiling:

- `PZEM-004T-v30` (mandreev/PZEM-004T-v30 or equivalent Modbus RTU library for PZEM)

## Configuration

The serial JSON sketch will use a local configuration file for per-install settings:

1. Copy `circuit_monitor_serial_json/config.example.h` to `circuit_monitor_serial_json/config.h`
2. Set circuit identities, PZEM addresses, threshold values, and optional Wi-Fi credentials
3. Do not commit `config.h`

## First run

Once firmware files are implemented:

1. Flash `circuit_monitor_pzem_test.ino`
2. Open the serial monitor at `115200`
3. Confirm PZEM module(s) respond with voltage, current, and power readings
4. Flash `circuit_monitor_serial_json.ino`
5. Confirm one valid JSON object per line matching `../serial-json-contract.md`

For the full bench workflow from flash to local validation, use `../operator-runbook.md`.
