# Launch checklist — before sharing with the sponsoring bank

## Content to confirm or fill in
- [ ] **Company identification** on `/legal/aviso-legal/` and `/nosotros/`: state of formation, registration number, registered agent, Dominican affiliate (if formed). Currently described generically.
- [ ] **Leadership bios**: add a team slide to the deck and/or a section on `/nosotros/`.
- [ ] **Station opening hours and phones** were taken from public listings on 2026-09-08 — re-verify during onboarding.
- [ ] **Polygon boundary** on the map is an approximation drawn from the four avenues; adjust the coordinates in `build.py` (`POLYGON`) if you want it tighter.
- [x] **Pricing terms** on `/precios/`, `/en/pricing/`, home, FAQ and deck: 25 bps below the station's current contract, no monthly minimum, terminal on monthly rental, transactions cleared in US dollars (your instruction of 2026-09-08). Still yours to confirm: the FAQ's one-year contract cancellable with 30 days' notice, and the "approval under ten business days" claim.
- [ ] **Scenario slide** (deck slide 13): RD$3.3 M card volume per station per month (national average implied by RD$41 bn / ≈1,025 stations), 1.95% MDR, RD$62/US$. Replace with your own model.
- [ ] **Tax treatment** paragraph on `/legal/cumplimiento/` and deck slide 14 (Norma 08-04 withholding vs. fuel's ITBIS exemption) is flagged "to be confirmed with tax counsel" — confirm before a bank compliance team reads it.
- [ ] **Images** are AI-generated illustrations (disclosed on `/legal/aviso-legal/`). Replace with real site photos of the twenty stations when you have them (`site/assets/img/`, 16:9, ≤ 200 KB WebP).
- [ ] **Launch-zone wording**: the public site calls the 20 stations the "zona de lanzamiento" and never states they have signed; the deck (slide 7) calls them a warm pipeline. Keep it that way unless the stations agree to be named publicly.
- [ ] **Sources**: news links point to Diario Libre, Listín, Infobae, elDinero, BCRD, MICM. They were current on 2026-09-08; re-check before the meeting.

## Technical
- [ ] Register the domain (see `docs/DEPLOYMENT.md` §1) and set `SITE_URL`.
- [ ] Create the Pages project; add `CLOUDFLARE_API_TOKEN` / `CLOUDFLARE_ACCOUNT_ID` secrets if using the workflow.
- [ ] Add DNS, CAA, SPF/DMARC/null-MX records; enable DNSSEC and HSTS.
- [ ] Set Resend secrets so the contact form delivers email (otherwise mailto fallback).
- [ ] Update `Expires:` in `site/.well-known/security.txt` annually.
- [ ] Run securityheaders.com and PageSpeed after the first deploy.
- [ ] Decide whether to enable Cloudflare Web Analytics (cookieless; CSP change documented).

## Suggested next content
- Real photographs and a one-paragraph profile per station.
- A downloadable PDF version of the sponsor-bank pack (gated behind the contact form).
- A Santiago / wider-DN expansion map once the second cohort is identified.
