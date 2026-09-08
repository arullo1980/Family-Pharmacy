# Deployment: Cloudflare Pages, domain, DNS and email

## 1. Choose the domain

The site is built with `SITE_URL=https://walletpartners.do` by default. Candidates, in order of preference:

| Domain | Why |
|---|---|
| `walletpartners.do` | Dominican ccTLD, short, signals local commitment to the bank. Register through a NIC.DO accredited registrar (e.g. `nic.do`); Cloudflare Registrar does not sell `.do`. |
| `walletpartners.com.do` | Fallback if the `.do` is taken. |
| `dr.walletpartnersllc.com` or `gasolineras.walletpartnersllc.com` | Zero-cost option on the domain you already use for email; works immediately once the zone is in Cloudflare. |

Change the domain in one place: build with `SITE_URL=https://<domain>` (the GitHub workflow reads the
repository variable `SITE_URL`), and update `Canonical:`/`Policy:` in `site/.well-known/security.txt`.

## 2. Create the Pages project

**Option A — Git integration (recommended)**

1. Cloudflare dashboard → Workers & Pages → Create → Pages → Connect to Git → select this repository.
2. Production branch: `main` (or the branch you are working on).
3. Build settings: framework preset *None*; build command `pip install openpyxl && python3 build.py`; build output directory `site`.
4. Environment variables (build): `SITE_URL=https://walletpartners.do`, `PYTHON_VERSION=3.12`.
5. Save and deploy. Every push then builds and publishes; other branches get preview URLs.

**Option B — GitHub Actions (already in `.github/workflows/deploy.yml`)**

1. Cloudflare dashboard → My Profile → API Tokens → Create Token → template *Cloudflare Pages: Edit*. Copy the token.
2. Account ID: Workers & Pages overview, right-hand column.
3. GitHub repo → Settings → Secrets and variables → Actions: add secrets `CLOUDFLARE_API_TOKEN`, `CLOUDFLARE_ACCOUNT_ID`; add variable `SITE_URL`.
4. Create the Pages project once: `npx wrangler pages project create wallet-partners-dr --production-branch main`.
5. Push. The workflow builds, runs sanity checks and deploys with `wrangler pages deploy`.

**Option C — one-off from a laptop**: `npm run build && npm run deploy` (uses `wrangler.toml`).

## 3. Contact form secrets (Pages → Settings → Variables and Secrets, *Production*)

| Name | Value |
|---|---|
| `RESEND_API_KEY` | API key from resend.com (free tier is enough); verify the sending domain there first |
| `CONTACT_TO` | `info@walletpartnersllc.com` |
| `CONTACT_FROM` | `Wallet Partners Website <noreply@walletpartners.do>` |

Until these exist the function returns 503 and the page offers a `mailto:` fallback.

## 4. Custom domain

Pages → Custom domains → Set up a custom domain → `walletpartners.do` and `www.walletpartners.do`.
If the zone is on Cloudflare, the CNAME records are created automatically; otherwise add the records below.

## 5. DNS records (zone: walletpartners.do)

| Type | Name | Content | Proxy | Purpose |
|---|---|---|---|---|
| CNAME | `@` | `wallet-partners-dr.pages.dev` | Proxied | Apex → Pages (Cloudflare flattens CNAME at apex) |
| CNAME | `www` | `wallet-partners-dr.pages.dev` | Proxied | www → Pages |
| CAA | `@` | `0 issue "letsencrypt.org"` | — | Restrict certificate issuance |
| CAA | `@` | `0 issue "pki.goog"` | — | Cloudflare also issues via Google Trust Services |
| CAA | `@` | `0 issuewild "letsencrypt.org"` | — | Wildcard restriction |
| CAA | `@` | `0 iodef "mailto:info@walletpartnersllc.com"` | — | Report unauthorised issuance |
| TXT | `@` | `v=spf1 -all` | — | Site domain sends no email → hard-fail SPF (change if you send from it) |
| TXT | `_dmarc` | `v=DMARC1; p=reject; rua=mailto:dmarc@walletpartnersllc.com; adkim=s; aspf=s` | — | Prevent spoofing of the brand domain |
| TXT | `*._domainkey` | `v=DKIM1; p=` | — | Null DKIM for a no-mail domain |
| MX | `@` | `.` (null MX, priority 0) | — | Declares that the domain receives no mail (RFC 7505) |
| TXT | `_mta-sts` | (only if you add mail later) | — | — |

If you want to *send* from `noreply@walletpartners.do` (Resend), replace the SPF/DKIM rows with the
values Resend gives you and keep DMARC at `p=reject` once the DKIM check passes.

Also enable in the Cloudflare zone: **DNSSEC** (DNS → Settings → Enable DNSSEC, then paste the DS record at the
registrar), **Always Use HTTPS**, **HSTS** (the site already sends the header; the dashboard toggle adds the
preload flag at the edge), **TLS 1.2 minimum**, **Automatic HTTPS Rewrites**, **Bot Fight Mode**.

## 6. Security and quality checks after the first deploy

- https://securityheaders.com — expect A/A+ (headers come from `site/_headers`).
- https://observatory.mozilla.org — CSP is strict: scripts only from `self`, map tiles only from CARTO/OSM.
- https://hstspreload.org — submit once HSTS is confirmed on apex and www.
- https://pagespeed.web.dev — images are pre-sized WebP/JPEG; no third-party fonts; Leaflet self-hosted.
- Search Console: add the property and submit `https://<domain>/sitemap.xml`.

## 7. Analytics (optional, cookieless)

Cloudflare Web Analytics can be enabled from the Pages project without changing the cookie notice
(it sets no cookies). If enabled, add `https://static.cloudflareinsights.com` to `script-src` and
`https://cloudflareinsights.com` to `connect-src` in `site/_headers`.
