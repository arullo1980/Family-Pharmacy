# Wallet Partners LLC — fuel-retail payments site (Dominican Republic)

Static website that presents Wallet Partners LLC's card-acceptance / merchant-of-record
program for gasoline stations in Santo Domingo's Polígono Central to prospective
sponsoring banks. Built for Cloudflare Pages.

**What is on the site**

| Path | Content |
|---|---|
| `/` | Pitch overview, headline stats, embedded station map, brand chart |
| `/stations/` | Interactive map (Leaflet), filters, station cards, directory table, CSV/GeoJSON/JSON downloads |
| `/market/` | Market case: 2026 ANADEGAS card-fee dispute timeline, BCRD payment-system indicators, charts, scenario calculator, sources |
| `/solution/` | Program design, responsibility matrix (Wallet Partners vs sponsoring bank), product, rollout plan |
| `/about/`, `/contact/` | Company page and contact form (Pages Function at `/api/contact`) |
| `/es/` | Spanish executive summary |
| `/legal/*` | Privacy (Law 172-13), terms, cookies, compliance framework (Law 155-17, PCI DSS, SIPARD), legal notice, accessibility |
| `robots.txt`, `sitemap.xml`, `.well-known/security.txt`, `_headers`, `_redirects`, `manifest.webmanifest` | Technical / hygiene files |

## Repository layout

```
data/estaciones_poligono_central.xlsx   source list of the 20 pipeline stations (single source of truth)
build.py                                static site generator (Python 3, needs openpyxl)
src/pages/*.py                          page content (one module per page) + shared helpers
site/                                   BUILD OUTPUT, committed; Cloudflare Pages serves this directory
  assets/css, assets/js, assets/img     styles, scripts, AI-generated illustrative images
  assets/vendor/leaflet                 self-hosted Leaflet 1.9.4 (BSD-2-Clause)
  data/stations.{json,csv,geojson}      generated from the spreadsheet
functions/api/contact.js                Cloudflare Pages Function for the contact form
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

## Updating the station list

Replace `data/estaciones_poligono_central.xlsx` (same column layout), run `python3 build.py`,
commit `site/`. The map, cards, table, stats and downloads all regenerate.

## Deploying

See `docs/DEPLOYMENT.md`. Short version: connect the GitHub repo to Cloudflare Pages with
build command `pip install openpyxl && python3 build.py` and output directory `site`, or add
`CLOUDFLARE_API_TOKEN` and `CLOUDFLARE_ACCOUNT_ID` as repository secrets and let the
workflow deploy on push.
