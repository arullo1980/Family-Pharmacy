from common import stat_tiles, brand_chart, icon, sources_block, SOURCES

def body(ctx):
    st = ctx["stats"]
    return f"""
<section class="hero">
  <picture>
    <source srcset="/assets/img/hero-station.webp" type="image/webp" />
    <img class="hero-img" src="/assets/img/hero-station.jpg" alt="" fetchpriority="high" />
  </picture>
  <div class="wrap">
    <span class="eyebrow">Sponsor-bank briefing · Dominican Republic</span>
    <h1>Card acceptance built for gasoline stations.</h1>
    <p class="lead">Wallet Partners LLC is launching a merchant-of-record and acquiring program dedicated to fuel retailers in the Dominican Republic. Twenty stations in Santo Domingo's Polígono Central are signed up to onboard the day our sponsoring bank relationship is in place.</p>
    <div class="hero-actions">
      <a class="btn btn-primary" href="/stations/">See the 20 stations on the map</a>
      <a class="btn btn-ghost" href="/market/">Read the market case</a>
    </div>
    {stat_tiles([
      (str(st["n"]), "warm-pipeline stations", "Santo Domingo, Polígono Central"),
      (str(st["h24"]), "open 24 hours", f"{round(100*st['h24']/st['n'])}% of the pipeline"),
      ("1.95–2.50%", "fees charged today", "per card transaction (ANADEGAS, 2026)"),
      ("RD$41 bn", "annual card payments at stations", "nationwide (Diario Libre, Jul 2026)"),
    ])}
  </div>
</section>

<section>
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">The moment</span>
      <h2>Fuel retailers just told the market they want a better acquiring deal.</h2>
      <p>In late June 2026 the national fuel-retailers association, ANADEGAS, announced it would remove card terminals from more than 780 affiliated stations in protest at commissions of 1.95% to 2.50% per transaction. On a regulated gross margin of roughly RD$25 per gallon, that fee equals RD$6.59 to RD$8.45 per gallon, or 25% to 36% of what the station keeps. The Government brokered a 30-day dialogue in July; the association asked for a per-gallon or margin-based pricing model instead of a flat percentage.</p>
    </div>
    <div class="grid grid-3">
      <div class="card">{icon("pump")}<h3>A segment with one pain point</h3><p>Fuel is a low-margin, high-ticket, price-controlled product. Percentage-based merchant discount rates hit stations harder than any other retail category. Pricing designed around gallons, not percentages, is the product they asked for publicly.</p></div>
      <div class="card">{icon("bank")}<h3>A concentrated, bankable market</h3><p>Roughly 1,025 stations nationwide, three incumbent acquirers, and card payments at stations of about RD$41 billion a year. A specialised acquirer needs only a small share of stations to reach meaningful volume.</p></div>
      <div class="card">{icon("map")}<h3>A launch cohort already identified</h3><p>The twenty stations on this site sit within or on the edge of the Polígono Central, the densest commercial district in the country. Nine operate 24 hours; eleven are inside the four boundary avenues and nine are immediately adjacent.</p></div>
    </div>
  </div>
</section>

<section class="alt">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">Launch pipeline</span>
      <h2>Where the first twenty stations are.</h2>
      <p>All twenty locations are within {st['maxDist']:.1f} km of the reference centre at Av. Lope de Vega and Av. 27 de Febrero. Click a marker for hours, phone and a Street View link. The full directory, filters and downloads are on the <a href="/stations/">stations page</a>.</p>
    </div>
    <div class="map-wrap">
      <div id="map" class="compact" role="region" aria-label="Map of pipeline gasoline stations in Santo Domingo"></div>
      <div class="map-legend"><span><i class="dot inside"></i> Inside Polígono Central ({st['inside']})</span><span><i class="dot edge"></i> Adjacent / edge ({st['edge']})</span><span><i class="poly-key"></i> Approximate boundary</span></div>
    </div>
    <div class="grid grid-2 mt-4">
      {brand_chart(st)}
      <div class="viz">
        <h3>Pipeline at a glance</h3>
        <div class="sub">From the station list compiled on {ctx['DATA_DATE']}</div>
        <div class="table-wrap"><table>
          <tr><th>Stations in pipeline</th><td class="num">{st['n']}</td></tr>
          <tr><th>Inside the Polígono Central</th><td class="num">{st['inside']}</td></tr>
          <tr><th>Adjacent / on the boundary</th><td class="num">{st['edge']}</td></tr>
          <tr><th>Open 24 hours</th><td class="num">{st['h24']}</td></tr>
          <tr><th>Distinct fuel brands</th><td class="num">{len(st['brands'])}</td></tr>
          <tr><th>Largest brand (TotalEnergies)</th><td class="num">{st['brands'].get('TotalEnergies', 0)}</td></tr>
          <tr><th>Furthest station from centre</th><td class="num">{st['maxDist']:.2f} km</td></tr>
        </table></div>
      </div>
    </div>
  </div>
</section>

<section>
  <div class="wrap split">
    <div>
      <span class="eyebrow">What we bring to the sponsoring bank</span>
      <h2>A vertical program, not another generic terminal.</h2>
      <ul class="checklist">
        <li><strong>Segment underwriting.</strong> Fuel retail is MCC 5541 / 5542. We onboard only licensed stations (MICM resolution, DGII registration, beneficial-owner KYC) and bring the file to the bank ready for review.</li>
        <li><strong>Gallon-aware pricing.</strong> Interchange-plus with a capped effective rate per gallon, so the station's cost stops scaling with pump prices set weekly by the Ministry.</li>
        <li><strong>Fuel-grade hardware.</strong> EMV and contactless terminals for forecourt attendants, integrated with pump controllers where available, with pre-authorisation and completion flows that keep chargebacks low.</li>
        <li><strong>Daily settlement and reporting.</strong> Next-day funding in Dominican pesos, per-station reconciliation and tax-ready statements.</li>
        <li><strong>Compliance first.</strong> PCI DSS, AML/CFT under Law 155-17, data protection under Law 172-13, sanctions screening and card-network rules, documented on our <a href="/legal/compliance/">compliance page</a>.</li>
      </ul>
      <a class="btn btn-navy mt-2" href="/solution/">How the program works</a>
    </div>
    <figure>
      <picture><source srcset="/assets/img/pos-tap.webp" type="image/webp" /><img src="/assets/img/pos-tap.jpg" alt="Customer tapping a contactless card on a wireless payment terminal at a fuel pump" loading="lazy" width="1280" height="720" /></picture>
      <figcaption>Contactless acceptance at the pump. Illustrative image.</figcaption>
    </figure>
  </div>
</section>

<section class="dark">
  <div class="wrap">
    <div class="section-head"><span class="eyebrow">Next step</span><h2>We are ready to present the full program.</h2><p>Merchant files for the twenty stations, the pricing model, the risk framework and our rollout timeline are available under NDA. We would welcome a working session with your merchant-acquiring and compliance teams.</p></div>
    <div class="hero-actions"><a class="btn btn-primary" href="/contact/">Request the sponsor-bank pack</a><a class="btn btn-ghost" href="/es/">Resumen en español</a></div>
  </div>
</section>

<section class="alt">
  <div class="wrap">{sources_block(["anadegas_retiro", "dl_41000", "dl_conflicto", "infobae_30", "bcrd_806", "anadegas_1025"])}</div>
</section>
"""
