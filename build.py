#!/usr/bin/env python3
"""Static site generator for the Wallet Partners LLC pitch site.

Reads data/estaciones_poligono_central.xlsx, writes station data files
(JSON / CSV / GeoJSON) and assembles every page in site/ from src/pages/.
Run:  python3 build.py
"""
import csv, datetime, html, json, os, re, shutil, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SRC = ROOT / "src" / "pages"
SITE = ROOT / "site"
DATA = ROOT / "data" / "estaciones_poligono_central.xlsx"

SITE_URL = os.environ.get("SITE_URL", "https://walletpartners.do").rstrip("/")
COMPANY = "Wallet Partners LLC"
CONTACT_EMAIL = "info@walletpartnersllc.com"
TODAY = datetime.date.today().isoformat()
DATA_DATE = "2026-09-08"
YEAR = datetime.date.today().year

CENTER = {"lat": 18.4690, "lng": -69.9295}
# Approximate polygon: JFK (N), 27 de Febrero (S), Winston Churchill (W), Máximo Gómez (E)
POLYGON = [[18.4838, -69.9432], [18.4815, -69.9112], [18.4622, -69.9112], [18.4588, -69.9442]]

BRANDS = [
    ("totalenergies", "TotalEnergies"), ("next", "Next"), ("axxon", "Axxon"), ("tropig", "Tropigás"),
    ("shell", "Shell"), ("texaco", "Texaco"), ("sigma", "Sigma"), ("vp racing", "VP Racing"),
    ("óptimo", "Óptimo Gas"), ("trovasa", "Trovasa"), ("la lira", "Independiente"),
]

def brand_of(name):
    n = name.lower()
    for k, v in BRANDS:
        if k in n:
            return v
    return "Other"

def load_stations():
    import openpyxl
    wb = openpyxl.load_workbook(DATA, data_only=True)
    ws = wb.active
    rows = list(ws.iter_rows(values_only=True))
    out = []
    for r in rows[1:]:
        if r[0] is None:
            continue
        lat, lng = float(r[4]), float(r[5])
        hours = r[8] or ""
        out.append({
            "id": int(r[0]), "name": r[1], "address": r[2], "phone": r[3],
            "lat": lat, "lng": lng, "hours": hours,
            "zone": "Dentro del polígono" if r[9] == "Sí" else "Borde / adyacente",
            "inside": r[9] == "Sí", "distKm": float(r[10]),
            "brand": brand_of(r[1]), "open24h": "24" in hours,
            "maps": f"https://www.google.com/maps/search/?api=1&query={lat},{lng}",
            "streetview": f"https://www.google.com/maps/@?api=1&map_action=pano&viewpoint={lat},{lng}",
        })
    return out

def write_data(stations):
    d = SITE / "data"; d.mkdir(parents=True, exist_ok=True)
    payload = {
        "source": "Google Maps search 'gasolinera', queried 2026-09-08; compiled by Wallet Partners LLC",
        "polygonDefinition": "Av. John F. Kennedy (N), Av. 27 de Febrero (S), Av. Winston Churchill (W), Av. Máximo Gómez (E)",
        "center": CENTER, "polygon": POLYGON, "stations": stations,
    }
    (d / "stations.json").write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    with open(d / "stations.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["id", "name", "brand", "address", "phone", "hours", "open_24h", "zone", "dist_km", "lat", "lng", "google_maps"])
        for s in stations:
            w.writerow([s["id"], s["name"], s["brand"], s["address"], s["phone"] or "", s["hours"], "yes" if s["open24h"] else "no", s["zone"], s["distKm"], s["lat"], s["lng"], s["maps"]])
    geo = {"type": "FeatureCollection", "features": [
        {"type": "Feature", "geometry": {"type": "Point", "coordinates": [s["lng"], s["lat"]]},
         "properties": {k: v for k, v in s.items() if k not in ("lat", "lng")}} for s in stations
    ] + [{"type": "Feature", "geometry": {"type": "Polygon", "coordinates": [[[p[1], p[0]] for p in POLYGON] + [[POLYGON[0][1], POLYGON[0][0]]]]},
          "properties": {"name": "Polígono Central (approximate)"}}]}
    (d / "stations.geojson").write_text(json.dumps(geo, ensure_ascii=False), encoding="utf-8")
    return payload

# ---------- layout ----------
NAV = [
    ("/", "Inicio"), ("/como-funciona/", "Cómo funciona"), ("/precios/", "Precios"),
    ("/zona/", "Zona de lanzamiento"), ("/preguntas/", "Preguntas"), ("/bancos/", "Bancos y aliados"),
]
NAV_EN = [
    ("/en/", "For banks & partners"), ("/zona/", "Launch zone map"), ("/contacto/", "Contact"),
]
LOGO = """<svg viewBox="0 0 40 40" aria-hidden="true"><rect x="2" y="8" width="36" height="26" rx="6" fill="#0f2440"/><rect x="2" y="14" width="36" height="6" fill="#eda100"/><circle cx="29" cy="26" r="4" fill="#2a78d6"/><circle cx="24" cy="26" r="4" fill="#eda100" opacity=".9"/></svg>"""

def layout(page, body, stations_json=None):
    path = page["path"]
    url = SITE_URL + path
    lang = page.get("lang", "es")
    items = NAV_EN if lang == "en" else NAV
    nav = "".join(
        '<a href="%s"%s>%s</a>' % (href, ' aria-current="page"' if href == path else '', label) for href, label in items
    )
    cta = '<a class="cta" href="/afiliese/">Afilie su estación</a>' if lang != "en" else '<a class="cta" href="/contacto/">Contact us</a>'
    lang_link = '<a href="/en/" lang="en">English</a>' if lang != "en" else '<a href="/" lang="es">Español</a>'
    head_extra = page.get("head", "")
    scripts = ""
    if page.get("map"):
        head_extra += '\n  <link rel="stylesheet" href="/assets/vendor/leaflet/leaflet.css" />'
        scripts += f'\n<script>window.WP_STATIONS = {json.dumps(stations_json, ensure_ascii=False)};</script>'
        scripts += '\n<script src="/assets/vendor/leaflet/leaflet.js"></script>'
        scripts += '\n<script src="/assets/js/map.js" defer></script>'
    og_image = SITE_URL + page.get("image", "/assets/img/hero-station.jpg")
    title = html.escape(page["title"])
    desc = html.escape(page["description"])
    es_alt = f'\n  <link rel="alternate" hreflang="en" href="{SITE_URL}/en/" />' if path == "/" else ""
    en_alt = f'\n  <link rel="alternate" hreflang="es" href="{SITE_URL}/" />' if path == "/en/" else ""
    breadcrumbs = json.dumps({
        "@context": "https://schema.org", "@type": "BreadcrumbList",
        "itemListElement": [{"@type": "ListItem", "position": 1, "name": "Home", "item": SITE_URL + "/"}] +
        ([{"@type": "ListItem", "position": 2, "name": page["title"].split(" | ")[0], "item": url}] if path != "/" else [])
    })
    org = json.dumps({
        "@context": "https://schema.org", "@type": "Organization", "name": COMPANY, "url": SITE_URL + "/",
        "logo": SITE_URL + "/assets/img/logo.svg", "email": CONTACT_EMAIL,
        "description": "Aceptación de tarjetas y servicios de comercio registrado para estaciones de combustible en la República Dominicana.",
        "areaServed": {"@type": "Country", "name": "Dominican Republic"},
        "contactPoint": [{"@type": "ContactPoint", "contactType": "sales", "telephone": "", "email": CONTACT_EMAIL, "availableLanguage": ["English", "Spanish"]}],
    })
    return f"""<!DOCTYPE html>
<html lang="{lang}">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>{title}</title>
  <meta name="description" content="{desc}" />
  <link rel="canonical" href="{url}" />{es_alt}{en_alt}
  <meta name="robots" content="{page.get('robots', 'index, follow')}" />
  <meta name="theme-color" content="#0f2440" />
  <meta property="og:site_name" content="{COMPANY}" />
  <meta property="og:type" content="website" />
  <meta property="og:title" content="{title}" />
  <meta property="og:description" content="{desc}" />
  <meta property="og:url" content="{url}" />
  <meta property="og:image" content="{og_image}" />
  <meta property="og:locale" content="{'es_DO' if lang == 'es' else 'en_US'}" />
  <meta name="twitter:card" content="summary_large_image" />
  <meta name="twitter:title" content="{title}" />
  <meta name="twitter:description" content="{desc}" />
  <meta name="twitter:image" content="{og_image}" />
  <link rel="icon" href="/favicon.svg" type="image/svg+xml" />
  <link rel="icon" href="/favicon.ico" sizes="any" />
  <link rel="apple-touch-icon" href="/apple-touch-icon.png" />
  <link rel="manifest" href="/manifest.webmanifest" />
  <link rel="stylesheet" href="/assets/css/main.css" />{head_extra}
  <script type="application/ld+json">{org}</script>
  <script type="application/ld+json">{breadcrumbs}</script>
</head>
<body>
<a class="skip" href="#main">{'Skip to content' if lang == 'en' else 'Ir al contenido'}</a>
<header class="site-header">
  <div class="wrap">
    <a class="brand" href="/">{LOGO}<span>Wallet Partners<small>Pagos para estaciones de combustible · RD</small></span></a>
    <button class="nav-toggle" aria-expanded="false" aria-controls="nav">Menú</button>
    <nav class="nav" id="nav" aria-label="Principal">{nav}{lang_link}{cta}</nav>
  </div>
</header>
<main id="main">
{body}
</main>
<footer class="site-footer">
  <div class="wrap">
    <div class="footer-grid">
      <div>
        <h4>{COMPANY}</h4>
        <p>Aceptación de tarjetas, comercio registrado y liquidación diseñados para estaciones de combustible en la República Dominicana, operados bajo la supervisión de un banco patrocinador y las reglas de las redes de tarjetas.</p>
        <p><a href="mailto:{CONTACT_EMAIL}">{CONTACT_EMAIL}</a></p>
      </div>
      <div>
        <h4>Estaciones</h4>
        <ul><li><a href="/como-funciona/">Cómo funciona</a></li><li><a href="/precios/">Precios por galón</a></li><li><a href="/zona/">Zona de lanzamiento</a></li><li><a href="/preguntas/">Preguntas frecuentes</a></li><li><a href="/afiliese/">Afilie su estación</a></li></ul>
      </div>
      <div>
        <h4>Empresa</h4>
        <ul><li><a href="/bancos/">Bancos y aliados</a></li><li><a href="/en/" lang="en">For banks &amp; partners (English)</a></li><li><a href="/nosotros/">Nosotros</a></li><li><a href="/contacto/">Contacto</a></li><li><a href="/.well-known/security.txt">security.txt</a></li></ul>
      </div>
      <div>
        <h4>Legal</h4>
        <ul><li><a href="/legal/privacidad/">Privacidad</a></li><li><a href="/legal/terminos/">Términos de uso</a></li><li><a href="/legal/cookies/">Cookies</a></li><li><a href="/legal/cumplimiento/">Cumplimiento</a></li><li><a href="/legal/aviso-legal/">Aviso legal</a></li><li><a href="/legal/accesibilidad/">Accesibilidad</a></li></ul>
      </div>
    </div>
    <p class="disclaimer">Wallet Partners LLC no es un banco. Los servicios de aceptación de tarjetas se prestan bajo el patrocinio de una entidad financiera miembro autorizada; las condiciones definitivas se establecen en el contrato de afiliación. Las marcas de combustible mencionadas pertenecen a sus titulares y se citan solo para identificar ubicaciones. Las cifras de mercado provienen de fuentes públicas citadas.</p>
    <div class="footer-bottom">
      <span>© {YEAR} {COMPANY}. Todos los derechos reservados.</span>
      <span>Santo Domingo · Estados Unidos</span>
    </div>
  </div>
</footer>
<div class="cookie" id="cookie-banner" role="dialog" aria-label="Cookie notice">
  Este sitio no usa cookies de publicidad ni de analítica. Guarda una sola preferencia en su navegador para recordar que vio este aviso. <a href="/legal/cookies/">Aviso de cookies</a>
  <div class="actions"><button class="btn btn-navy" id="cookie-ok">Entendido</button></div>
</div>
<script src="/assets/js/main.js" defer></script>{scripts}
</body>
</html>
"""

def build():
    stations = load_stations()
    payload = write_data(stations)
    stats = {
        "n": len(stations),
        "inside": sum(s["inside"] for s in stations),
        "edge": sum(not s["inside"] for s in stations),
        "h24": sum(s["open24h"] for s in stations),
        "brands": {},
        "phones": sum(1 for s in stations if s["phone"]),
        "maxDist": max(s["distKm"] for s in stations),
    }
    for s in stations:
        stats["brands"][s["brand"]] = stats["brands"].get(s["brand"], 0) + 1
    ctx = {"stations": stations, "stats": stats, "SITE_URL": SITE_URL, "COMPANY": COMPANY,
           "CONTACT_EMAIL": CONTACT_EMAIL, "DATA_DATE": DATA_DATE, "TODAY": TODAY, "YEAR": YEAR, "html": html, "json": json}

    sys.path.insert(0, str(SRC))
    import pages  # src/pages/pages.py defines PAGES list
    urls = []
    for page in pages.PAGES:
        body = page["body"](ctx) if callable(page["body"]) else page["body"]
        out = SITE / page["path"].lstrip("/") / "index.html" if page["path"].endswith("/") else SITE / page["path"].lstrip("/")
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(layout(page, body, payload if page.get("map") else None), encoding="utf-8")
        if page.get("robots", "index").startswith("index"):
            urls.append((SITE_URL + page["path"], page.get("priority", "0.6")))
        print("wrote", out.relative_to(ROOT))

    sm = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for u, p in urls:
        sm.append(f"  <url><loc>{u}</loc><lastmod>{TODAY}</lastmod><priority>{p}</priority></url>")
    sm.append("</urlset>")
    (SITE / "sitemap.xml").write_text("\n".join(sm) + "\n", encoding="utf-8")
    (SITE / "robots.txt").write_text(f"User-agent: *\nAllow: /\nDisallow: /api/\n\nSitemap: {SITE_URL}/sitemap.xml\n", encoding="utf-8")
    print("stations:", stats)

if __name__ == "__main__":
    build()
