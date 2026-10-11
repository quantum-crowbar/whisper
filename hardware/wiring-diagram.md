# Wiring diagram

Full as-built connection map: every GPIO, rail, and power-chain wire. Companion to
[pinout.md](pinout.md), which holds the same assignments as tables — if the two disagree,
fix both.

![Wiring diagram](wiring-diagram.png)

Line colours: red = battery / switched / 5V, orange = 3V3, grey = GND, blue = I2S,
green = I2C, purple = SPI, teal = button, brown = USB-C charge input.

## Source

Hand-laid-out SVG, not Mermaid: Mermaid's auto-layout can't hold the fixed two-row pin
arrangement with right-angle routing. [wiring-diagram.py](wiring-diagram.py) (stdlib only)
generates [wiring-diagram.svg](wiring-diagram.svg); the PNG is a headless-Chrome render of
the SVG. Edit the script, then:

```sh
python3 wiring-diagram.py > wiring-diagram.svg
google-chrome --headless=new --no-sandbox --hide-scrollbars --force-device-scale-factor=2 \
  --window-size=1800,1190 --screenshot=wiring-diagram.png "file://$PWD/wiring-diagram.svg"
```
