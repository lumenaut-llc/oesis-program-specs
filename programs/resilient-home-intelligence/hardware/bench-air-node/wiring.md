# Wiring

## Controller

Recommended controller: ESP32-S3 dev board with exposed `3V3`, `GND`, `GPIO`, and native USB for programming.

## Sensors

- SHT45 for temperature and relative humidity
- BME688 for temperature, humidity, pressure, and gas-resistance trend

The MVP keeps both sensors on the same I2C bus. The SHT45 acts as the preferred temperature and humidity source; the BME688 primarily adds pressure and gas-trend evidence.

## Power rails

- `3V3` from ESP32-S3 to both sensor boards
- common `GND` to both sensor boards
- USB power into the ESP32-S3 only

If a breakout board supports both `VIN` and `3V3`, prefer `3V3` unless the board documentation requires otherwise.

## Pin map

Suggested default pin map:

| Function | ESP32-S3 | SHT45 | BME688 |
| --- | --- | --- | --- |
| 3.3 V | `3V3` | `VIN` or `3V3` | `VIN` or `3V3` |
| Ground | `GND` | `GND` | `GND` |
| I2C SDA | `GPIO8` | `SDA` | `SDA` |
| I2C SCL | `GPIO9` | `SCL` | `SCL` |

If the chosen ESP32-S3 board already uses different default I2C pins in example firmware, match the firmware and document the final mapping in code comments and packet metadata.

## Notes on cable lengths and shielding

- Keep sensor leads short for the MVP, ideally under 20 cm.
- Use twisted pairs or neatly bundled leads if repeated I2C errors appear.
- Keep sensor wiring away from Wi-Fi antennas, switching regulators, and USB cable strain points.
- For perfboard builds, prefer direct soldered headers over long loose jumpers.

## Known risks

- Some breakout boards include pull-up resistors; using many breakout boards on one bus can over-pull the lines.
- The BME688 self-heats slightly, so it should not be packed tightly against the SHT45.
- Breadboard connections are convenient but can create intermittent faults that look like firmware bugs.
- Shared I2C works for the bench prototype, but cable length margins shrink quickly in outdoor installs.
