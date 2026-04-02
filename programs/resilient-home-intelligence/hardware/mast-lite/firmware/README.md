# Firmware Scaffold

## Purpose

Provide a minimal ESP32 bring-up sketch set for mast-lite so the outdoor node can be validated before deeper enclosure and sensor expansion work.

## Current contents

- `mast_lite_i2c_scanner/mast_lite_i2c_scanner.ino`
- `mast_lite_serial_json/mast_lite_serial_json.ino`
- `mast_lite_serial_json/secrets.example.h`
- `platformio.ini`
- `tools/capture_serial.sh`

## Build setup

Use the pinned PlatformIO configuration in this directory:

```bash
pio run -e mast_lite_i2c_scanner
pio run -e mast_lite_serial_json
```

## Optional time sync

Copy `mast_lite_serial_json/secrets.example.h` to `mast_lite_serial_json/secrets.h` and fill in local Wi-Fi credentials if you want NTP-backed `observed_at`.

## Serial capture on macOS

```bash
./tools/capture_serial.sh /dev/cu.usbmodem101 serial.log
```

For the full bench-to-outdoor workflow, use `../operator-runbook.md`.
