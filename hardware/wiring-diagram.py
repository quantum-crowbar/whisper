"""Renders the as-built wiring diagram to SVG on stdout (stdlib only).

See wiring-diagram.md for the render-to-PNG command.
"""
import sys
W, H = 1800, 1190
COL = {"bat":"#d32f2f","v5":"#e53935","v33":"#ef6c00","gnd":"#455a64",
       "i2s":"#1565c0","i2c":"#2e7d32","spi":"#6a1b9a","btn":"#00838f","usb":"#795548"}
o = []
def add(s): o.append(s)
def wire(d, kind, label=None, lx=None, ly=None):
    add(f'<path d="{d}" fill="none" stroke="{COL[kind]}" stroke-width="3.5" stroke-linejoin="round"/>')
    if label:
        w = len(label)*6.6 + 10
        add(f'<rect x="{lx-w/2}" y="{ly-10}" width="{w}" height="18" fill="#fff"/>'
            f'<text x="{lx}" y="{ly+4}" class="wl" text-anchor="middle">{label}</text>')
def box(x,y,w,h,cls,title,sub=None):
    add(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="6" class="{cls}"/>')
    cy = y + h/2 + (0 if sub else 5)
    add(f'<text x="{x+w/2}" y="{cy-(8 if sub else 0)}" class="bt" text-anchor="middle">{title}</text>')
    if sub:
        for i,s in enumerate(sub.split("|")):
            add(f'<text x="{x+w/2}" y="{cy+10+i*15}" class="st" text-anchor="middle">{s}</text>')
def pin(cx,cy,label,w=84,cls="pin"):
    add(f'<rect x="{cx-w/2}" y="{cy-14}" width="{w}" height="28" rx="4" class="{cls}"/>'
        f'<text x="{cx}" y="{cy+5}" class="pt" text-anchor="middle">{label}</text>')
def dot(x,y,label,dx,dy,anchor):
    add(f'<circle cx="{x}" cy="{y}" r="9" fill="#212121"/>'
        f'<text x="{x+dx}" y="{y+dy}" class="nt" text-anchor="{anchor}">{label}</text>')

add(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}">')
add('''<style>
text{font-family:Helvetica,Arial,sans-serif;fill:#212121}
.bt{font-size:15px;font-weight:700}.st{font-size:12px;fill:#455a64}
.pt{font-size:13px;font-weight:600}.wl{font-size:12px;fill:#212121}
.nt{font-size:13px;font-weight:700}.ti{font-size:20px;font-weight:700}
.per{fill:#e8f5e9;stroke:#2e7d32;stroke-width:2}
.mod{fill:#e3f2fd;stroke:#1565c0;stroke-width:2}
.mcu{fill:#ede7f6;stroke:#5e35b1;stroke-width:3}
.pin{fill:#fff8e1;stroke:#8d6e63;stroke-width:2}
.rsv{fill:#f5f5f5;stroke:#9e9e9e;stroke-width:1.5;stroke-dasharray:6 4}
</style>''')
add(f'<rect width="{W}" height="{H}" fill="#fff"/>')
add('<text x="20" y="32" class="ti">voice recorder/note taker prototype circuit</text>')

# ---- nets / buses (drawn first, under boxes)
# 3V3: top channel y=70 -> MIC VDD x=400, OLED VCC x=950; left bus x=230
wire("M400,150 V70 H950 V150", "v33", "VDD", 400, 128)
add(f'<text x="950" y="140" class="wl" text-anchor="start" dx="6">VCC</text>')
wire("M230,70 H400", "v33")
wire("M230,70 V835", "v33")
wire("M500,835 H230", "v33", "VCC", 365, 835)
wire("M265,530 H230", "v33")
# GND: channel y=110, hops over OLED VCC (x=950) ; right bus x=1570
wire("M520,150 V110 H942 a8,8 0 0 1 16,0 H1570 V1000", "gnd")
add('<text x="528" y="138" class="wl">GND + L/R</text>')
wire("M1150,150 V110", "gnd"); add('<text x="1158" y="138" class="wl">GND</text>')
wire("M1400,150 V110", "gnd"); add('<text x="1408" y="138" class="wl">leg B</text>')
wire("M1100,835 H1302 a8,8 0 0 1 16,0 H1570", "gnd", "GND", 1450, 835)
wire("M1535,530 H1570", "gnd")
wire("M1430,1000 H1570", "gnd", "OUT−", 1500, 1000)

# ---- signals
wire("M400,260 V456","i2s","SCK (BCLK)",400,358)
wire("M500,260 V456","i2s","WS (LRCLK)",500,358)
wire("M600,260 V456","i2s","SD (DOUT)",600,358)
wire("M960,260 V456","i2c","SDA",960,358)
wire("M1100,260 V456","i2c","SCL",1100,358)
wire("M1340,260 V456","btn","leg A (INPUT_PULLUP)",1340,358)
wire("M600,604 V780","spi","CS",600,690)
wire("M700,604 V780","spi","MOSI",700,690)
wire("M800,604 V780","spi","SCK",800,690)
wire("M900,604 V780","spi","MISO",900,690)

# ---- power chain
wire("M710,1000 H800","bat","B+ / B−",755,1000)
wire("M970,985 H1060","bat","OUT+",1015,985)
wire("M1170,985 H1260","bat","IN+",1215,985)
wire("M930,1040 V1075 H1330 V1040","gnd","OUT− → IN− (direct, not switched)",1130,1075)
wire("M885,1100 V1040","usb","USB-C IN",885,1070)
wire("M1310,960 V604","v5","OUT+ 5V",1310,900)

# ---- boxes
box(330,150,450,110,"per","I2S MEMS MIC","VDD · GND · L/R · SCK · WS · SD")
box(900,150,300,110,"per","SSD1306 OLED 128×64 @0x3C","VCC · GND · SDA · SCL")
box(1280,150,170,110,"per","RECORD BUTTON","4-pin tactile|leg A · diagonal leg B")
box(500,780,600,110,"per","microSD READER (SPI)","VCC · GND · CS · MOSI · SCK · MISO")
add('<rect x="300" y="470" width="1200" height="120" rx="10" class="mcu"/>')
add('<text x="900" y="525" class="bt" text-anchor="middle" style="font-size:20px">WAVESHARE ESP32-S3-ZERO</text>')
add('<text x="900" y="550" class="st" text-anchor="middle">onboard LDO → 3V3 · native USB-C · top row: GPIO1, 4, 5, 6, 8, 9 · bottom row: GPIO10–13, 5V</text>')
for x,l in [(400,"GPIO4"),(500,"GPIO5"),(600,"GPIO6"),(960,"GPIO8"),(1100,"GPIO9"),(1340,"GPIO1")]: pin(x,470,l)
for x,l in [(600,"GPIO10"),(700,"GPIO11"),(800,"GPIO12"),(900,"GPIO13"),(1310,"5V")]: pin(x,590,l)
pin(300,530,"3V3",70); pin(1500,530,"GND",70)
dot(230,530,"3V3 NET",-14,5,"end")
dot(1570,530,"GND NET",14,5,"start")

box(560,960,150,80,"mod","LiPo 3.7V 400mAh","602530 · JST-PH")
box(800,960,170,80,"mod","TP4056 (ZX-006)","charge / protect")
box(1060,960,110,80,"mod","Slide switch","3-pin, on OUT+")
box(1260,960,170,80,"mod","BS02 V4 boost","A/B jumpers = 5V")
box(800,1100,170,50,"mod","USB-C charger")

# reserved + notes
add('<rect x="20" y="880" width="420" height="140" rx="6" class="rsv"/>')
add('<text x="36" y="905" class="bt">Reserved / avoid</text>')
for i,t in enumerate(["GPIO0, 3, 45, 46 — strapping","GPIO19, 20 — USB D−/D+","GPIO21 — onboard WS2812 RGB LED",
                      "GPIO43, 44 — UART0 TX/RX","GPIO33–37 — not exposed (octal PSRAM)"]):
    add(f'<text x="36" y="{928+i*18}" class="st">{t}</text>')
add('<text x="20" y="1060" class="st">Net view: all grounds are common. The OLED GND is physically soldered to the booster OUT−.</text>')
add('<text x="20" y="1078" class="st">Slide switch is on the OUT+ line only; charging works with the switch off.</text>')
# legend
lx, ly = 20, 1108
for i,(k,t) in enumerate([("bat","battery / switched"),("v5","5V"),("v33","3V3"),("gnd","GND"),("i2s","I2S"),("i2c","I2C"),("spi","SPI"),("btn","button"),("usb","USB-C")]):
    x = lx + (i%3)*140; y = ly + (i//3)*22
    add(f'<line x1="{x}" y1="{y}" x2="{x+28}" y2="{y}" stroke="{COL[k]}" stroke-width="4"/>'
        f'<text x="{x+36}" y="{y+4}" class="st">{t}</text>')
add('</svg>')
sys.stdout.write("\n".join(o))
