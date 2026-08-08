# Bill of Materials

Canonical parts list for the Pocket Voice Recorder puck. Wiring for each part is in
[pinout.md](pinout.md). Mirrors [specs.md §2.1](../specs.md#21-bill-of-materials).

Legend: ✅ have · ⏳ pending purchase

| # | Part | Qty | Detail | Interface | Status |
|---|---|---|---|---|---|
| 1 | MCU | 1 | Waveshare ESP32-S3-Zero (USB-C; no built-in mic/SD; no JST charging) | — | ✅ |
| 2 | Microphone | 1 | I2S MEMS mic breakout (GND/VDD/SD/L·R/WS/SCK) | I2S | ✅ |
| 3 | SD reader | 1 | SPI microSD reader module (GND/VCC/MISO/MOSI/SCK/CS), ~29×48mm | SPI | ✅ |
| 4 | microSD card | 1 | 16–32GB, Class 10 | — | ⏳ |
| 5 | Display | 1 | 0.96" 128×64 I2C OLED (SSD1306, addr 0x3C) | I2C | ✅ |
| 6 | Charge/protect | 1 | TP4056 with protection, USB-C; wired B+/B− and OUT+/OUT− leads | power | ✅ |
| 7 | Battery | 1 | LiPo, JST-PH connector, 500–800mAh | power | ⏳ |
| 8 | Power switch | 1 | Mini slide switch, 3-pin | power | ✅ |
| 9 | Record button | 1 | 4-pin tactile push button | GPIO | ✅ |

## Pending purchases

Two items block Phase 0 bench-testing (see [roadmap](../docs/roadmap.md)):

- **microSD card** (#4) — blocks the SD write test
- **LiPo battery** (#7) — blocks the power-chain test and battery-% work

Everything else is in hand; mic/OLED/button can be bench-tested without the pending parts.

## Notes

- The **SD reader (#3, ~29×48mm)** is the largest single module and likely drives the
  enclosure size — confirm its real footprint before finalizing CAD ([specs.md §7](../specs.md#7-open-questions)).
- The ESP32-S3-Zero has **no onboard mic, SD, or JST charging** — hence the separate
  mic breakout, SD reader, and TP4056.
- Consumables not listed above: hookup wire, header pins, solder, and the 3D-printed
  [enclosure](enclosure/).
