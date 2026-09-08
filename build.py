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

SITE_URL = os.environ.get("SITE_URL", "https://bomberopartners.com.do").rstrip("/")
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
    (d / "stations.js").write_text("window.WP_STATIONS = " + json.dumps(payload, ensure_ascii=False) + ";\n", encoding="utf-8")
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
    ("/en/", "Home"), ("/en/how-it-works/", "How it works"), ("/en/pricing/", "Pricing"),
    ("/en/launch-zone/", "Launch zone"), ("/en/faq/", "FAQ"), ("/en/banks/", "Banks & partners"),
]
CHROME = {
    "es": dict(skip="Ir al contenido", tagline="Pagos para estaciones de combustible · RD", menu="Menú", nav="Principal",
               cta='<a class="cta" href="/afiliese/">Afilie su estación</a>',
               cookie='Este sitio no usa cookies de publicidad ni de analítica. Guarda una sola preferencia en su navegador para recordar que vio este aviso. <a href="/legal/cookies/">Aviso de cookies</a>', ok="Entendido",
               f_about="Aceptación de tarjetas, comercio registrado y liquidación diseñados para las bombas de la República Dominicana, operados por Wallet Partners LLC bajo la supervisión de un banco patrocinador y las reglas de las redes de tarjetas.",
               f_cols=[("Estaciones", [("/como-funciona/", "Cómo funciona"), ("/precios/", "Precios"), ("/zona/", "Zona de lanzamiento"), ("/preguntas/", "Preguntas frecuentes"), ("/afiliese/", "Afilie su estación")]),
                       ("Empresa", [("/bancos/", "Bancos y aliados"), ("/nosotros/", "Nosotros"), ("/contacto/", "Contacto"), ("/en/", "English version"), ("/.well-known/security.txt", "security.txt")]),
                       ("Legal", [("/legal/privacidad/", "Privacidad"), ("/legal/terminos/", "Términos de uso"), ("/legal/cookies/", "Cookies"), ("/legal/cumplimiento/", "Cumplimiento"), ("/legal/aviso-legal/", "Aviso legal"), ("/legal/accesibilidad/", "Accesibilidad")])],
               disclaimer="Bombero Partners es un nombre comercial (DBA) de Wallet Partners LLC. Wallet Partners LLC no es un banco. Los servicios de aceptación de tarjetas se prestan bajo el patrocinio de una entidad financiera miembro autorizada; las condiciones definitivas se establecen en el contrato de afiliación. Las marcas de combustible mencionadas pertenecen a sus titulares y se citan solo para identificar ubicaciones. Las cifras de mercado provienen de fuentes públicas citadas.",
               rights="Todos los derechos reservados.", place="Santo Domingo · Estados Unidos"),
    "en": dict(skip="Skip to content", tagline="Fuel-station payments · Dominican Republic", menu="Menu", nav="Primary",
               cta='<a class="cta" href="/en/sign-up/">Sign up your station</a>',
               cookie='This site uses no advertising or analytics cookies. It stores one preference in your browser to remember that you have seen this notice. <a href="/en/legal/cookies/">Cookie notice</a>', ok="OK",
               f_about="Card acceptance, merchant-of-record and settlement services designed for gasoline stations in the Dominican Republic, operated by Wallet Partners LLC under the oversight of a sponsoring bank and card-network rules.",
               f_cols=[("Stations", [("/en/how-it-works/", "How it works"), ("/en/pricing/", "Pricing"), ("/en/launch-zone/", "Launch zone"), ("/en/faq/", "FAQ"), ("/en/sign-up/", "Sign up your station")]),
                       ("Company", [("/en/banks/", "Banks & partners"), ("/en/about/", "About"), ("/en/contact/", "Contact"), ("/", "Versión en español"), ("/.well-known/security.txt", "security.txt")]),
                       ("Legal", [("/en/legal/privacy/", "Privacy"), ("/en/legal/terms/", "Terms of use"), ("/en/legal/cookies/", "Cookies"), ("/en/legal/compliance/", "Compliance"), ("/en/legal/notice/", "Legal notice"), ("/en/legal/accessibility/", "Accessibility")])],
               disclaimer="Bombero Partners is a trade name (DBA) of Wallet Partners LLC. Wallet Partners LLC is not a bank. Card-acceptance services are provided under the sponsorship of a licensed member financial institution; final terms are set in the merchant agreement. Fuel brands mentioned belong to their owners and appear only to identify locations. Market figures come from the public sources cited.",
               rights="All rights reserved.", place="Santo Domingo · United States"),
}
LOGO = """<svg viewBox="0 0 40 40" aria-hidden="true"><rect x="2" y="8" width="36" height="26" rx="6" fill="#0f2440"/><rect x="2" y="14" width="36" height="6" fill="#eda100"/><circle cx="29" cy="26" r="4" fill="#2a78d6"/><circle cx="24" cy="26" r="4" fill="#eda100" opacity=".9"/></svg>"""

import hashlib
def asset(path):
    """/assets/... -> /assets/...?v=<8-char content hash> so browsers drop stale copies despite the 1-year cache."""
    f = SITE / path.lstrip("/")
    if f.exists():
        return f"{path}?v={hashlib.sha1(f.read_bytes()).hexdigest()[:8]}"
    return path

def layout(page, body, stations_json=None):
    path = page["path"]
    url = SITE_URL + path
    lang = page.get("lang", "es")
    items = NAV_EN if lang == "en" else NAV
    nav = "".join(
        '<a href="%s"%s>%s</a>' % (href, ' aria-current="page"' if href == path else '', label) for href, label in items
    )
    ch = CHROME[lang]
    cta = ch["cta"]
    alt = page.get("alt")
    lang_link = (f'<a href="{alt}" lang="en" hreflang="en">English</a>' if lang != "en" else f'<a href="{alt}" lang="es" hreflang="es">Español</a>') if alt else ""
    head_extra = page.get("head", "")
    scripts = ""
    if page.get("map"):
        head_extra += f'\n  <link rel="stylesheet" href="{asset("/assets/vendor/leaflet/leaflet.css")}" />'
        scripts += f'\n<script src="{asset("/data/stations.js")}"></script>'
        scripts += f'\n<script src="{asset("/assets/vendor/leaflet/leaflet.js")}"></script>'
        scripts += f'\n<script src="{asset("/assets/js/map.js")}" defer></script>'
    og_image = SITE_URL + page.get("image", "/assets/img/hero-station.jpg")
    title = html.escape(page["title"])
    desc = html.escape(page["description"])
    other = "en" if lang == "es" else "es"
    es_alt = (f'\n  <link rel="alternate" hreflang="{lang}" href="{url}" />\n  <link rel="alternate" hreflang="{other}" href="{SITE_URL}{alt}" />'
              f'\n  <link rel="alternate" hreflang="x-default" href="{SITE_URL}{alt if lang == "en" else path}" />') if alt else ""
    en_alt = ""
    breadcrumbs = json.dumps({
        "@context": "https://schema.org", "@type": "BreadcrumbList",
        "itemListElement": [{"@type": "ListItem", "position": 1, "name": "Home", "item": SITE_URL + "/"}] +
        ([{"@type": "ListItem", "position": 2, "name": page["title"].split(" | ")[0], "item": url}] if path != "/" else [])
    })
    org = json.dumps({
        "@context": "https://schema.org", "@type": "Organization", "name": "Bombero Partners", "legalName": COMPANY, "alternateName": "Bombero Partners, a DBA of Wallet Partners LLC", "url": SITE_URL + "/",
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
  <link rel="stylesheet" href="{asset('/assets/css/main.css')}" />{head_extra}
  <script type="application/ld+json">{org}</script>
  <script type="application/ld+json">{breadcrumbs}</script>
</head>
<body>
<a class="skip" href="#main">{ch["skip"]}</a>
<header class="site-header">
  <div class="wrap">
    <a class="brand" href="{'/en/' if lang == 'en' else '/'}">{LOGO}<span>Bombero Partners<small>{ch["tagline"]}</small></span></a>
    <button class="nav-toggle" aria-expanded="false" aria-controls="nav">{ch["menu"]}</button>
    <nav class="nav" id="nav" aria-label="{ch["nav"]}">{nav}{lang_link}{cta}</nav>
  </div>
</header>
<main id="main">
{body}
</main>
<footer class="site-footer">
  <div class="wrap">
    <div class="footer-grid">
      <div>
        <h4>Bombero Partners</h4>
        <p>{ch["f_about"]}</p>
        <p><a href="mailto:{CONTACT_EMAIL}">{CONTACT_EMAIL}</a></p>
      </div>
      {"".join(f'<div><h4>{h}</h4><ul>' + "".join(f'<li><a href="{a}">{t}</a></li>' for a, t in links) + '</ul></div>' for h, links in ch["f_cols"])}
    </div>
    <p class="disclaimer">{ch["disclaimer"]}</p>
    <div class="footer-bottom">
      <span>© {YEAR} {COMPANY}. {ch["rights"]}</span>
      <span>{ch["place"]}</span>
    </div>
  </div>
</footer>
<div class="cookie" id="cookie-banner" role="dialog" aria-label="Cookie notice">
  {ch["cookie"]}
  <div class="actions"><button class="btn btn-navy" id="cookie-ok">{ch["ok"]}</button></div>
</div>
<script src="{asset('/assets/js/main.js')}" defer></script>{scripts}
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
