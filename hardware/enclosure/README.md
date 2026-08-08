# Enclosure

3D-printed card-shaped case. CAD sources and exported STLs live here.

## Target form factor
- Elongated "half-card," ~92×32mm footprint, ~10–12mm thick
  (stacks MCU + TP4056 + LiPo + SD reader)
- Front face: OLED window, record button, mic port, optional status LED
- One short edge: dual USB-C cutouts (ESP32 port + TP4056 charging port)
- Opposite short edge: SD card slot + power switch

## Open risks
- SD reader module (~29×48mm) may drive case size more than any other part —
  **confirm real module dimensions before finalizing CAD**
- Mic may need a felt/mesh dust cover behind its acoustic port
- CAD tool: TBD (Fusion 360 / FreeCAD / OpenSCAD)
