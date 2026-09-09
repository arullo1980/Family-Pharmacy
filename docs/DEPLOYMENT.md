# Deployment: Cloudflare Pages, domain, DNS and email

## 1. Domain

Registered: **`bomberopartners.com.do`** at NIC.DO (registrar stays NIC.DO; DNS and hosting run on Cloudflare).
The site is built with `SITE_URL=https://bomberopartners.com.do` by default; the GitHub workflow reads the
repository variable `SITE_URL` if you ever change it. `security.txt` carries the same domain.

## 2. Create the Pages project

**Option A — Git integration (recommended)**

1. Cloudflare dashboard → Workers & Pages → Create → Pages → Connect to Git → select this repository.
2. Production branch: `main` (or the branch you are working on).
3. Build settings: framework preset *None*; build command `pip install openpyxl && python3 build.py`; build output directory `site`.
4. Environment variables (build): `SITE_URL=https://bomberopartners.com.do`, `PYTHON_VERSION=3.12`.
5. Save and deploy. Every push then builds and publishes; other branches get preview URLs.

**Option B — GitHub Actions (already in `.github/workflows/deploy.yml`)**

1. Cloudflare dashboard → My Profile → API Tokens → Create Token → template *Cloudflare Pages: Edit*. Copy the token.
2. Account ID: Workers & Pages overview, right-hand column.
3. GitHub repo → Settings → Secrets and variables → Actions: add secrets `CLOUDFLARE_API_TOKEN`, `CLOUDFLARE_ACCOUNT_ID`; add variable `SITE_URL`.
4. Create the Pages project once: `npx wrangler pages project create wallet-partners-dr --production-branch main`.
5. Push. The workflow builds, runs sanity checks and deploys with `wrangler pages deploy`.

**Connecting the domain (one-time, in this order)**

1. Cloudflare dashboard → *Add a domain* → type `bomberopartners.com.do` → Free plan → Continue. Cloudflare scans for existing records (there are none yet) and shows **two nameservers** (e.g. `ana.ns.cloudflare.com` and `bob.ns.cloudflare.com`; yours will differ).
2. NIC.DO → *Mis dominios* → `bomberopartners.com.do` → *Servidores DNS / Nameservers* → replace the NIC.DO defaults with the two Cloudflare nameservers → save.
3. Wait until Cloudflare emails "bomberopartners.com.do is now active" (usually under an hour for `.do`, up to 24 h worst case).
4. Workers & Pages → `wallet-partners-dr` → *Custom domains* → *Set up a custom domain* → `bomberopartners.com.do` → Activate. Repeat for `www.bomberopartners.com.do`. Cloudflare creates the CNAME records and issues the certificate itself.
5. Add the CAA, SPF, DMARC and null-MX records from §5, then enable DNSSEC (DNS → Settings) and paste the DS record into NIC.DO's DNSSEC section.

**Option C — one-off from a laptop**: `npm run build && npm run deploy` (uses `wrangler.toml`).

## 3. Form email (Resend)

The contact and sign-up forms post to the Pages Function `/api/contact`, which sends the message through
Resend. The deploy workflow copies the key from GitHub into the Pages project, so nothing is typed into
Cloudflare by hand.

1. Create a Resend account at https://resend.com using **info@walletpartnersllc.com** (the address that
   should receive the forms).
2. Resend → API Keys → Create API Key → name `bombero-website`, permission *Sending access* → copy the key.
3. GitHub → repo → Settings → Secrets and variables → Actions → New repository secret:
   `RESEND_API_KEY` = the key.
4. Re-run the "Build and deploy" workflow (or push to `main`). The step *Sync form-email secrets* stores it
   in the Pages project. Forms now deliver to info@walletpartnersllc.com from `onboarding@resend.dev`.

**Production sender (optional, recommended before showing the forms to merchants).** Resend's onboarding
sender can only deliver to the account owner's address. To send from `@bomberopartners.com.do` to anyone:

1. Resend → Domains → Add Domain → `bomberopartners.com.do` (region: US East).
2. Resend shows three DNS records (a TXT for DKIM at `resend._domainkey`, and an MX plus a TXT at
   `send.bomberopartners.com.do`). Add them in Cloudflare → DNS, all *DNS only*, exactly as shown.
   They live on subdomains, so the apex null-MX and `v=spf1 -all` stay in place.
3. Click *Verify* in Resend. Then in GitHub → Settings → Secrets and variables → Actions → **Variables**:
   `CONTACT_FROM` = `Bombero Partners <noreply@bomberopartners.com.do>` and, if a different inbox should
   receive forms, `CONTACT_TO`. Re-run the workflow.

## 4. Custom domain

Pages → Custom domains → Set up a custom domain → `bomberopartners.com.do`, then again for `www.bomberopartners.com.do`.
If the zone is on Cloudflare, the CNAME records are created automatically; otherwise add the records below.

## 5. DNS records (zone: bomberopartners.com.do)

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

If you want to *send* from `noreply@bomberopartners.com.do` (Resend), replace the SPF/DKIM rows with the
values Resend gives you and keep DMARC at `p=reject` once the DKIM check passes.

Also enable in the Cloudflare zone: **DNSSEC** (DNS → Settings → Enable DNSSEC, then paste the DS record at the
registrar), **Always Use HTTPS**, **HSTS** (the site already sends the header; the dashboard toggle adds the
preload flag at the edge), **TLS 1.2 minimum**, **Automatic HTTPS Rewrites**, **Bot Fight Mode**.

## 6. Security and quality checks after the first deploy

- https://securityheaders.com — expect A/A+ (headers come from `site/_headers`).
- https://observatory.mozilla.org — CSP is strict: scripts only from `self`, map tiles only from OpenStreetMap.
- https://hstspreload.org — submit once HSTS is confirmed on apex and www.
- https://pagespeed.web.dev — images are pre-sized WebP/JPEG; no third-party fonts; Leaflet self-hosted.
- Search Console: add the property and submit `https://<domain>/sitemap.xml`.

## 7. Analytics (optional, cookieless)

Cloudflare Web Analytics can be enabled from the Pages project without changing the cookie notice
(it sets no cookies). If enabled, add `https://static.cloudflareinsights.com` to `script-src` and
`https://cloudflareinsights.com` to `connect-src` in `site/_headers`.
