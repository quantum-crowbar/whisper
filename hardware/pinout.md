# Wiring & Pinout

Target MCU: **Waveshare ESP32-S3-Zero** (USB-C, no built-in mic/SD, no JST charging).

## I2S microphone (MEMS breakout)

| Mic pin | ESP32-S3-Zero |
|---|---|
| VDD | 3V3 |
| GND | GND |
| SCK (BCLK) | GPIO4 |
| WS (LRCLK) | GPIO5 |
| SD (DOUT) | GPIO6 |
| L/R | GND (mono, left channel) |

## SPI microSD reader

| SD pin | ESP32-S3-Zero |
|---|---|
| VCC | 3V3 or 5V |
| GND | GND |
| SCK | GPIO7 |
| MISO | GPIO8 |
| MOSI | GPIO9 |
| CS | GPIO10 |

## I2C OLED (SSD1306, 0.96" 128×64, addr 0x3C)

| OLED pin | ESP32-S3-Zero |
|---|---|
| GND | GND |
| VCC | 3V3 |
| SCL | GPIO12 |
| SDA | GPIO11 |

## Record button

One leg to **GPIO2**, diagonal leg to **GND**, configured `INPUT_PULLUP`.
Short press = record toggle; long press = sync mode (planned).

## Power chain

```
LiPo (JST) → TP4056 B+/B−
TP4056 OUT+ → slide switch → ESP32-S3-Zero 5V
TP4056 OUT− → ESP32-S3-Zero GND (direct, not through switch)
TP4056 USB-C → charging input (independent of the ESP32's own USB-C)
```

Only the positive rail is switched; charging works regardless of switch position.

## Board setting

"ESP32S3 Dev Module", **USB CDC on boot enabled** (for Serial over native USB-C).
