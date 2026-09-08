# Wallet Partners LLC — fuel-retail payments site (Dominican Republic)

Two deliverables in one repository:

1. **Public website** (Spanish, for gasoline-station owners, with a short bilingual page for banks and partners). Built for Cloudflare Pages.
2. **Sponsor-bank presentation** (`deck/Wallet-Partners-Sponsor-Bank-Deck.pptx`, English, 17 slides) carrying the full pitch: 2026 fee-dispute timeline, Banco Central data, launch-cohort map and station list, program design, responsibility matrix, scenario economics, compliance framework, rollout and the ask. A PDF export sits beside it.

**What is on the site**

| Path | Audience | Content |
|---|---|---|
| `/` | Stations | Value proposition (per-gallon fee, next-day pesos, forecourt terminals, local support), how it works, launch-zone map, sign-up CTA |
| `/como-funciona/` | Stations | Transaction flow, onboarding documents, terminals |
| `/precios/` | Stations | Per-gallon pricing model and a calculator showing what today's percentage fee costs per gallon |
| `/zona/` | Stations | Interactive map and directory of the 20 Polígono Central stations with "¿Es su estación? Regístrela" hooks |
| `/preguntas/` | Stations | FAQ (with FAQ structured data) |
| `/afiliese/` | Stations | Sign-up form (posts to the Pages Function at `/api/contact`, mailto fallback) |
| `/bancos/`, `/en/` | Banks & partners | One-page summary in Spanish and English; CTA to request the deck |
| `/nosotros/`, `/contacto/` | All | Company and contact form |
| `/legal/*` | All | Privacidad (Ley 172-13), términos, cookies, cumplimiento (Ley 155-17, PCI DSS, SIPARD), aviso legal, accesibilidad |
| `robots.txt`, `sitemap.xml`, `.well-known/security.txt`, `_headers`, `_redirects`, `manifest.webmanifest` | — | Technical / hygiene files |

## Repository layout

```
data/estaciones_poligono_central.xlsx   source list of the 20 pipeline stations (single source of truth)
build.py                                static site generator (Python 3, needs openpyxl)
src/pages/*.py                          page content (one module per page) + shared helpers
site/                                   BUILD OUTPUT, committed; Cloudflare Pages serves this directory
  assets/css, assets/js, assets/img     styles, scripts, AI-generated illustrative images
  assets/vendor/leaflet                 self-hosted Leaflet 1.9.4 (BSD-2-Clause)
  data/stations.{json,csv,geojson}      generated from the spreadsheet
functions/api/contact.js                Cloudflare Pages Function for the contact and sign-up forms
deck/build_deck.js                      pptxgenjs generator for the sponsor-bank deck (npm install in deck/ first)
deck/Wallet-Partners-Sponsor-Bank-Deck.pptx / .pdf   the presentation
tools_map.py                            renders site/assets/img/poligono-map.png (schematic map used in the deck)
wrangler.toml                           Cloudflare Pages project config
.github/workflows/deploy.yml            CI: build + deploy (needs two repository secrets)
docs/DEPLOYMENT.md                      Cloudflare Pages, custom domain, DNS and email records
docs/LAUNCH-CHECKLIST.md                Things to fill in / verify before showing the bank
docs/DATA.md                            Data provenance and how to update the station list
```

## Local development

```bash
pip install openpyxl
python3 build.py              # regenerates site/ and site/data/*
python3 -m http.server 8080 --directory site
```

Set `SITE_URL=https://your-domain` when building to change canonical URLs, sitemap and
Open Graph links (default `https://walletpartners.do`).

## Rebuilding the deck

```bash
cd deck && npm install && node build_deck.js      # writes Wallet-Partners-Sponsor-Bank-Deck.pptx
```

The deck reads `site/data/stations.json` and `site/assets/img/poligono-map.png`, so run `python3 build.py`
and `python3 tools_map.py` first if the station list changed.

## Updating the station list

Replace `data/estaciones_poligono_central.xlsx` (same column layout), run `python3 build.py`,
commit `site/`. The map, cards, table, stats and downloads all regenerate.

## Deploying

See `docs/DEPLOYMENT.md`. Short version: connect the GitHub repo to Cloudflare Pages with
build command `pip install openpyxl && python3 build.py` and output directory `site`, or add
`CLOUDFLARE_API_TOKEN` and `CLOUDFLARE_ACCOUNT_ID` as repository secrets and let the
workflow deploy on push.
