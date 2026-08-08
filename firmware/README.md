# Firmware — ESP32-S3-Zero

Arduino/PlatformIO project for the recorder puck.

**Status: v0.1 written, not yet flashed/validated on hardware.**

## Implemented (v0.1)
- I2S mic capture → 16kHz mono WAV on SD
- Record button toggle (debounced)
- OLED status screen (idle/recording, filename, elapsed time, free SD space)
- WAV header written with placeholder sizes, patched on file close

## Not yet implemented
- BLE sync (GATT server, file list + chunked transfer, control commands)
- MTU negotiation (247+) for throughput
- VAD auto-trigger
- Deep sleep / power management
- Battery % on screen (needs ADC on battery rail — TBD)

## Libraries
`Adafruit_GFX`, `Adafruit_SSD1306`, plus core `SD`, `SPI`, `Wire`,
`driver/i2s.h` from the ESP32 Arduino core.

## Build / flash
Board: **ESP32S3 Dev Module**, USB CDC on boot **enabled**.

Pin assignments live in [../hardware/pinout.md](../hardware/pinout.md).

> The v0.1 sketch is not yet committed here. Drop the `.ino` / PlatformIO
> sources into this directory (e.g. `src/main.cpp` + `platformio.ini`).
