# Wiring diagram

Full as-built connection map: every GPIO, rail, and power-chain wire. Companion to
[pinout.md](pinout.md), which holds the same assignments as tables — if the two disagree,
fix both.

![Wiring diagram](wiring-diagram.png)

Line colours: red = battery / 5V, orange = 3V3, grey = GND, blue = I2S, green = I2C,
purple = SPI, teal = button, brown = USB-C charge input.

## Source

The Mermaid below is the source of truth; the PNG is rendered from it.

```mermaid
%%{init: {"flowchart": {"nodeSpacing": 28, "rankSpacing": 110, "curve": "basis"}}}%%
flowchart LR
  subgraph PWR["POWER CHAIN"]
    direction TB
    USB["USB-C charger"]
    TP["<b>TP4056 (ZX-006)</b><br/>charge / protect"]
    BAT["<b>LiPo 3.7V 400mAh</b><br/>602530, JST-PH"]
    SW["<b>Slide switch</b><br/>3-pin, on OUT+ line"]
    BO["<b>BS02 V4 boost</b><br/>A/B jumpers = 5V"]
  end
  subgraph MCU["WAVESHARE ESP32-S3-ZERO"]
    direction TB
    V5["5V"]
    GND["GND"]
    V33["3V3 (onboard LDO)"]
    G1["GPIO1"]
    G4["GPIO4"]
    G5["GPIO5"]
    G6["GPIO6"]
    G8["GPIO8"]
    G9["GPIO9"]
    G10["GPIO10"]
    G11["GPIO11"]
    G12["GPIO12"]
    G13["GPIO13"]
  end
  RSV["<i>Reserved / avoid</i><br/>GPIO0, 3, 45, 46 strapping<br/>GPIO19, 20 USB D−/D+<br/>GPIO21 onboard RGB LED<br/>GPIO43, 44 UART0<br/>GPIO33–37 not exposed"]
  MIC["<b>I2S MEMS MIC</b><br/>VDD · GND · L/R · SCK · WS · SD"]
  OLED["<b>SSD1306 OLED</b> 128×64 @0x3C<br/>VCC · GND · SDA · SCL"]
  SDR["<b>microSD READER</b> (SPI)<br/>VCC · GND · CS · MOSI · SCK · MISO"]
  BTN["<b>RECORD BUTTON</b><br/>4-pin tactile, leg A / diagonal leg B"]
  USB ---|"USB-C IN (charging)"| TP
  BAT ---|"B+ / B−"| TP
  TP ---|"OUT+ 3.0–4.2V"| SW
  SW ---|"IN+"| BO
  TP ---|"OUT− → IN− (direct)"| BO
  BO ---|"OUT+ 5V"| V5
  BO ---|"OUT− → GND"| GND
  V33 ---|"VDD"| MIC
  V33 ---|"VCC"| OLED
  V33 ---|"VCC"| SDR
  GND ---|"GND + L/R (left ch.)"| MIC
  BO ---|"GND from booster OUT−"| OLED
  GND ---|"GND"| SDR
  GND ---|"leg B"| BTN
  G1 ---|"leg A · INPUT_PULLUP"| BTN
  G4 ---|"SCK (BCLK)"| MIC
  G5 ---|"WS (LRCLK)"| MIC
  G6 ---|"SD (DOUT → S3 DIN)"| MIC
  G8 ---|"SDA"| OLED
  G9 ---|"SCL"| OLED
  G10 ---|"CS"| SDR
  G11 ---|"MOSI"| SDR
  G12 ---|"SCK"| SDR
  G13 ---|"MISO"| SDR
  linkStyle 0 stroke:#795548,stroke-width:3px
  linkStyle 1 stroke:#d32f2f,stroke-width:3px
  linkStyle 2 stroke:#d32f2f,stroke-width:3px
  linkStyle 3 stroke:#d32f2f,stroke-width:3px
  linkStyle 4 stroke:#455a64,stroke-width:3px
  linkStyle 5 stroke:#e53935,stroke-width:3px
  linkStyle 6 stroke:#455a64,stroke-width:3px
  linkStyle 7 stroke:#ef6c00,stroke-width:3px
  linkStyle 8 stroke:#ef6c00,stroke-width:3px
  linkStyle 9 stroke:#ef6c00,stroke-width:3px
  linkStyle 10 stroke:#455a64,stroke-width:3px
  linkStyle 11 stroke:#455a64,stroke-width:3px
  linkStyle 12 stroke:#455a64,stroke-width:3px
  linkStyle 13 stroke:#455a64,stroke-width:3px
  linkStyle 14 stroke:#00838f,stroke-width:3px
  linkStyle 15 stroke:#1565c0,stroke-width:3px
  linkStyle 16 stroke:#1565c0,stroke-width:3px
  linkStyle 17 stroke:#1565c0,stroke-width:3px
  linkStyle 18 stroke:#2e7d32,stroke-width:3px
  linkStyle 19 stroke:#2e7d32,stroke-width:3px
  linkStyle 20 stroke:#6a1b9a,stroke-width:3px
  linkStyle 21 stroke:#6a1b9a,stroke-width:3px
  linkStyle 22 stroke:#6a1b9a,stroke-width:3px
  linkStyle 23 stroke:#6a1b9a,stroke-width:3px
  classDef pin fill:#fff8e1,stroke:#8d6e63,color:#212121
  classDef mod fill:#e3f2fd,stroke:#1565c0,color:#0d1b2a
  classDef per fill:#e8f5e9,stroke:#2e7d32,color:#0d1b2a
  classDef note fill:#f3e5f5,stroke:#8e24aa,color:#212121
  class V5,V33,GND,G1,G4,G5,G6,G8,G9,G10,G11,G12,G13 pin
  class USB,TP,BAT,SW,BO mod
  class MIC,OLED,SDR,BTN per
  class RSV note
```

Re-render after editing (needs `@mermaid-js/mermaid-cli`):

```sh
awk '/^```mermaid/{f=1;next} /^```/{f=0} f' wiring-diagram.md > /tmp/wiring.mmd
mmdc -i /tmp/wiring.mmd -o wiring-diagram.png -s 2 -w 1800 -b white
```
