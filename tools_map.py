"""Schematic map of the Polígono Central launch zone (PNG for the deck), drawn with Pillow."""
import json, math, glob
from PIL import Image, ImageDraw, ImageFont

d = json.load(open("site/data/stations.json", encoding="utf-8"))
st, poly, c = d["stations"], d["polygon"], d["center"]
W, H, S = 2000, 1240, 2  # px, supersample
fonts = glob.glob("/usr/share/fonts/**/DejaVuSans.ttf", recursive=True) or glob.glob("/usr/share/fonts/**/*Sans*.ttf", recursive=True)
bold = glob.glob("/usr/share/fonts/**/DejaVuSans-Bold.ttf", recursive=True) or fonts
F = lambda sz, b=False: ImageFont.truetype((bold if b else fonts)[0], sz) if fonts else ImageFont.load_default()

lat0 = c["lat"]
def km(lat, lng):
    return ((lng - c["lng"]) * 111.32 * math.cos(math.radians(lat0)), (lat - c["lat"]) * 110.57)
# plot window in km
x0, x1, y0, y1 = -2.35, 2.35, -1.55, 1.85
pad_l, pad_r, pad_t, pad_b = 90, 40, 90, 70
def px(x, y):
    return (pad_l + (x - x0) / (x1 - x0) * (W - pad_l - pad_r), pad_t + (y1 - y) / (y1 - y0) * (H - pad_t - pad_b))

im = Image.new("RGB", (W * S, H * S), "white")
dr = ImageDraw.Draw(im)
def P(x, y): return tuple(v * S for v in px(x, y))
# plot area
dr.rectangle([pad_l * S, pad_t * S, (W - pad_r) * S, (H - pad_b) * S], fill="#f4f6f9", outline="#dde3ea", width=2 * S)
# grid every 0.5 km
gx = x0
while gx <= x1 + 1e-9:
    if abs(gx - round(gx * 2) / 2) < 1e-9:
        X = P(gx, 0)[0]; dr.line([(X, pad_t * S), (X, (H - pad_b) * S)], fill="#e3e8ee", width=S)
        dr.text((X, (H - pad_b + 8) * S), f"{gx:+.1f}", fill="#6b7683", font=F(20 * S), anchor="mt")
    gx = round(gx + 0.5, 6) if abs(gx - round(gx * 2) / 2) < 1e-9 else math.ceil(gx * 2) / 2
gy = math.ceil(y0 * 2) / 2
while gy <= y1:
    Y = P(0, gy)[1]; dr.line([(pad_l * S, Y), ((W - pad_r) * S, Y)], fill="#e3e8ee", width=S)
    dr.text(((pad_l - 10) * S, Y), f"{gy:+.1f}", fill="#6b7683", font=F(20 * S), anchor="rm")
    gy += 0.5
# polygon
pts = [P(*km(a, b)) for a, b in poly]
overlay = Image.new("RGBA", im.size, (0, 0, 0, 0)); od = ImageDraw.Draw(overlay)
od.polygon(pts, fill=(237, 161, 0, 28)); im.paste(Image.alpha_composite(im.convert("RGBA"), overlay).convert("RGB"))
dr = ImageDraw.Draw(im)
# dashed outline
def dashed(a, b, dash=18 * S, gap=12 * S):
    L = math.hypot(b[0] - a[0], b[1] - a[1]); n = int(L // (dash + gap)) + 1
    for i in range(n):
        t0 = i * (dash + gap) / L; t1 = min(1, (i * (dash + gap) + dash) / L)
        dr.line([(a[0] + (b[0] - a[0]) * t0, a[1] + (b[1] - a[1]) * t0), (a[0] + (b[0] - a[0]) * t1, a[1] + (b[1] - a[1]) * t1)], fill="#b97c00", width=3 * S)
for i in range(4): dashed(pts[i], pts[(i + 1) % 4])
# avenue labels
def mid(a, b): return ((a[0] + b[0]) / 2, (a[1] + b[1]) / 2)
lab = F(24 * S, True)
dr.text((mid(pts[0], pts[1])[0], pts[0][1] - 22 * S), "Av. John F. Kennedy", fill="#6b4a00", font=lab, anchor="mb")
dr.text((mid(pts[2], pts[3])[0], pts[3][1] + 22 * S), "Av. 27 de Febrero", fill="#6b4a00", font=lab, anchor="mt")
def vtext(text, xy):
    t = Image.new("RGBA", (600 * S, 40 * S), (0, 0, 0, 0)); ImageDraw.Draw(t).text((300 * S, 20 * S), text, fill="#6b4a00", font=lab, anchor="mm")
    t = t.rotate(90, expand=True); im.paste(t, (int(xy[0] - t.width / 2), int(xy[1] - t.height / 2)), t)
vtext("Av. Winston Churchill", (mid(pts[0], pts[3])[0] - 26 * S, mid(pts[0], pts[3])[1]))
vtext("Av. Máximo Gómez", (mid(pts[1], pts[2])[0] + 26 * S, mid(pts[1], pts[2])[1]))
dr = ImageDraw.Draw(im)
# centre + stations
cx, cy = P(0, 0); r = 9 * S
dr.ellipse([cx - r, cy - r, cx + r, cy + r], fill="white", outline="#0f2440", width=3 * S)
dr.text((cx + 14 * S, cy - 14 * S), "reference centre", fill="#0f2440", font=F(19 * S))
R = 19 * S
for s in st:
    x, y = P(*km(s["lat"], s["lng"])); col = "#2a78d6" if s["inside"] else "#eb6834"
    dr.ellipse([x - R, y - R, x + R, y + R], fill=col, outline="white", width=3 * S)
    dr.text((x, y), str(s["id"]), fill="white", font=F(18 * S, True), anchor="mm")
# title + legend
dr.text((pad_l * S, 30 * S), "Launch zone: 20 stations, Polígono Central, Santo Domingo (schematic, km from reference centre)", fill="#0f2440", font=F(28 * S, True), anchor="lm")
lx, ly = (W - pad_r - 400) * S, (pad_t + 24) * S
dr.rounded_rectangle([lx - 12 * S, ly - 12 * S, lx + 360 * S, ly + 100 * S], radius=8 * S, fill="white", outline="#dde3ea", width=2 * S)
for i, (colr, txt) in enumerate([("#2a78d6", f"Inside Polígono Central ({sum(s['inside'] for s in st)})"), ("#eb6834", f"Adjacent / edge ({sum(not s['inside'] for s in st)})"), ("#b97c00", "Approximate boundary")]):
    yy = ly + i * 32 * S + 10 * S
    if i < 2: dr.ellipse([lx, yy - 10 * S, lx + 20 * S, yy + 10 * S], fill=colr)
    else: dr.line([(lx, yy), (lx + 20 * S, yy)], fill=colr, width=3 * S)
    dr.text((lx + 32 * S, yy), txt, fill="#16202b", font=F(21 * S), anchor="lm")
im = im.resize((W, H), Image.LANCZOS)
im.save("site/assets/img/poligono-map.png", optimize=True)
print("map ok", im.size)
