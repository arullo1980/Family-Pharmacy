from common import stat_tiles, icon, sources_block

def margin_chart():
    # Gross margin ≈ RD$25/gal; acquirer fee RD$6.59–8.45/gal (ANADEGAS, July 2026)
    W, H, L, R = 640, 150, 130, 80
    scale = (W - L - R) / 25.0
    def row(y, label, fee, note):
        return (f'<text x="{L-10}" y="{y+15}" text-anchor="end" font-size="13" fill="#4a5563">{label}</text>'
                f'<rect x="{L}" y="{y}" width="{25*scale:.1f}" height="22" rx="4" fill="#dde3ea"><title>Gross margin ≈ RD$25.00 per gallon</title></rect>'
                f'<rect x="{L}" y="{y}" width="{fee*scale:.1f}" height="22" rx="4" fill="#eb6834" data-label="{label}: RD${fee:.2f} of RD$25 margin ({fee/25*100:.0f}%)"><title>Acquirer fee RD${fee:.2f} per gallon ({fee/25*100:.0f}% of gross margin)</title></rect>'
                f'<text x="{L+25*scale+8:.1f}" y="{y+15}" font-size="13" font-weight="600" fill="#16202b">{note}</text>')
    svg = (f'<svg viewBox="0 0 {W} {H}" role="img" aria-labelledby="mc-title mc-desc">'
           f'<title id="mc-title">Acquirer fee as a share of a station\'s gross margin per gallon</title>'
           f'<desc id="mc-desc">Of roughly 25 pesos of gross margin per gallon, card fees take 6.59 pesos in the low case and 8.45 pesos in the high case.</desc>'
           + row(20, "Low case (1.95%)", 6.59, "26%") + row(60, "High case (2.50%)", 8.45, "34%")
           + f'<line x1="{L}" y1="100" x2="{L+25*scale:.1f}" y2="100" stroke="#dde3ea"/>'
           + "".join(f'<text x="{L+v*scale:.1f}" y="118" text-anchor="middle" font-size="11" fill="#6b7683">RD${v}</text>' for v in (0, 5, 10, 15, 20, 25))
           + f'<text x="{L}" y="140" font-size="11" fill="#6b7683">Pesos per gallon</text></svg>')
    return f"""<div class="viz" data-tip>
      <h3>Card fees take a quarter to a third of a station's gross margin</h3>
      <div class="sub">Gross margin ≈ RD$25 per gallon; acquirer commission 1.95%–2.50% of the retail price (ANADEGAS figures, July 2026)</div>
      {svg}
      <div class="legend"><span><i class="sw" style="background:#eb6834"></i> Acquirer fee per gallon</span><span><i class="sw" style="background:#dde3ea"></i> Remaining gross margin</span></div>
      <details><summary>Table view</summary><table><tr><th>Case</th><th class="num">Fee / gal</th><th class="num">Share of RD$25 margin</th></tr><tr><td>1.95%</td><td class="num">RD$6.59</td><td class="num">26%</td></tr><tr><td>2.50%</td><td class="num">RD$8.45</td><td class="num">34%</td></tr></table><p class="small muted">ANADEGAS quoted 25%–36% depending on fuel type and negotiated rate; the bars use its per-gallon figures against a RD$25 margin.</p></details>
    </div>"""

def growth_chart():
    # Card transactions (millions): 117 in 2008, 806 in 2025 (BCRD via elDinero)
    W, H = 640, 220
    pts = [(2008, 117), (2025, 806)]
    x = lambda yr: 70 + (yr - 2008) * (W - 120) / 17
    y = lambda v: 180 - v * 150 / 900
    svg = (f'<svg viewBox="0 0 {W} {H}" role="img" aria-labelledby="gc-title gc-desc"><title id="gc-title">Card transactions in the Dominican Republic, 2008 versus 2025</title><desc id="gc-desc">117 million card transactions in 2008 rising to 806 million in 2025.</desc>'
           + "".join(f'<line x1="70" y1="{y(v):.1f}" x2="{W-50}" y2="{y(v):.1f}" stroke="#eef2f6"/><text x="62" y="{y(v)+4:.1f}" text-anchor="end" font-size="11" fill="#6b7683">{v}</text>' for v in (0, 300, 600, 900))
           + f'<line x1="{x(2008):.1f}" y1="{y(117):.1f}" x2="{x(2025):.1f}" y2="{y(806):.1f}" stroke="#2a78d6" stroke-width="2" stroke-dasharray="5 5"/>'
           + "".join(f'<circle cx="{x(yr):.1f}" cy="{y(v):.1f}" r="6" fill="#2a78d6" stroke="#fff" stroke-width="2" data-label="{yr}: {v} million card transactions"><title>{yr}: {v} million</title></circle><text x="{x(yr):.1f}" y="{y(v)-14:.1f}" text-anchor="middle" font-size="13" font-weight="700" fill="#16202b">{v} M</text><text x="{x(yr):.1f}" y="205" text-anchor="middle" font-size="12" fill="#4a5563">{yr}</text>' for yr, v in pts)
           + '</svg>')
    return f"""<div class="viz" data-tip>
      <h3>Card transactions grew almost seven-fold in 17 years</h3>
      <div class="sub">Millions of card transactions per year, Dominican Republic (Banco Central data as reported by elDinero). Dashed line connects the two reported points; intermediate years not shown.</div>
      {svg}
      <details><summary>Table view</summary><table><tr><th>Year</th><th class="num">Card transactions (millions)</th></tr><tr><td>2008</td><td class="num">117</td></tr><tr><td>2025</td><td class="num">806</td></tr></table></details>
    </div>"""

def body(ctx):
    return f"""
<div class="page-title"><div class="wrap">
  <span class="eyebrow">Market opportunity</span>
  <h1>Fuel retail in the Dominican Republic needs a specialised acquirer.</h1>
  <p>The country's card economy is growing at double digits, cash still dominates at the pump, and in 2026 the stations themselves went public with their frustration at percentage-based acquiring fees. Below is the evidence we put in front of prospective sponsoring banks, with every figure sourced.</p>
</div></div>

<section>
  <div class="wrap">
    {stat_tiles([
      ("≈1,025", "fuel stations nationwide", "ANADEGAS estimate; 780+ affiliated"),
      ("RD$41 bn", "card payments at stations per year", "Diario Libre, Jul 2026"),
      ("RD$5–6 bn", "paid yearly in card commissions by stations", "≈RD$584 M per month (Diario Libre)"),
      ("806 M", "card transactions in the DR, 2025", "Banco Central via elDinero"),
      ("RD$1.07 tn", "value of card payments, 2025 (+12.8%)", "BCRD via Invertix"),
      ("75%", "of Dominicans' payments still in cash", "Diario Libre, Dec 2025"),
    ])}
  </div>
</section>

<section class="alt">
  <div class="wrap">
    <div class="section-head"><span class="eyebrow">The 2026 fee dispute</span><h2>What happened, and why it matters to a sponsoring bank.</h2></div>
    <div class="split">
      <div>
        <ol class="timeline">
          <li><strong>30 June 2026</strong> ANADEGAS, the national association of fuel retailers, announces that its members will stop accepting cards, citing commissions of 1.95% to 2.50% per transaction charged by the processing companies.</li>
          <li><strong>2 July 2026</strong> Vice-President Raquel Peña says the Government expects an agreement so that stations keep accepting cards. Press coverage places the DR alongside other countries where fuel retailers have clashed with banks over card fees.</li>
          <li><strong>5–6 July 2026</strong> The association starts a staged removal of terminals from more than 780 affiliated stations. Estimates put the industry's card commissions at about RD$584 million per month, RD$5–6 billion a year.</li>
          <li><strong>7 July 2026</strong> After a meeting with the Minister of Industry and Commerce and the head of Pro Consumidor, ANADEGAS agrees to a 30-day window to negotiate. It proposes a fixed fee per gallon or a margin-based scheme instead of a percentage.</li>
          <li><strong>8 July 2026</strong> Diario Libre reports card payments at fuel stations total roughly RD$41 billion per year.</li>
          <li><strong>20 July 2026</strong> ANADEGAS and the banking sector agree to open a formal dialogue on terminal commissions.</li>
        </ol>
      </div>
      <div>
        {margin_chart()}
        <div class="callout mt-3"><p><strong>The takeaway for a sponsor.</strong> The retailers' own numbers show that the problem is the pricing structure, not card acceptance itself. A program priced per gallon, with transparent interchange pass-through, gives a bank a defensible way to grow fuel-segment volume while the incumbents are locked in a public dispute with the segment.</p></div>
      </div>
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="section-head"><span class="eyebrow">Card economy</span><h2>Electronic payments keep compounding.</h2><p>Banco Central data show a payments market that is still early in its shift away from cash, with cards already carrying most of the value settled through retail instruments.</p></div>
    <div class="grid grid-2">
      {growth_chart()}
      <div class="viz">
        <h3>Payment system indicators</h3>
        <div class="sub">Banco Central de la República Dominicana, as reported in the press</div>
        <div class="table-wrap"><table>
          <thead><tr><th>Indicator</th><th class="num">Value</th><th>Period</th></tr></thead>
          <tbody>
            <tr><td>Card transactions</td><td class="num">806 million</td><td>2025</td></tr>
            <tr><td>Value of card payments</td><td class="num">RD$1,072.5 bn (+12.8%)</td><td>2025</td></tr>
            <tr><td>Cards' share of value settled (retail instruments)</td><td class="num">63.6%</td><td>2025</td></tr>
            <tr><td>Debit cards per 1,000 inhabitants</td><td class="num">757 (+8.9%)</td><td>Q1 2026</td></tr>
            <tr><td>Credit cards per 1,000 inhabitants</td><td class="num">373</td><td>Q1 2026</td></tr>
            <tr><td>POS terminals per million inhabitants</td><td class="num">19,038</td><td>Q1 2026</td></tr>
            <tr><td>Electronic payment accounts per 1,000 inhabitants</td><td class="num">81 (from 62)</td><td>Q1 2026</td></tr>
            <tr><td>Share of payments made in cash</td><td class="num">≈75%</td><td>2025</td></tr>
          </tbody>
        </table></div>
      </div>
    </div>
  </div>
</section>

<section class="alt">
  <div class="wrap">
    <div class="section-head"><span class="eyebrow">Fuel retail</span><h2>A regulated, price-controlled, high-volume category.</h2></div>
    <div class="grid grid-3">
      <div class="card">{icon("pump")}<h3>Weekly price setting</h3><p>The Ministry of Industry, Commerce and MSMEs (MICM) publishes retail fuel prices every week. In 2025 premium gasoline sold at RD$290.10 and regular at RD$272.50 per gallon. Because the retail price and the retailer's margin are both fixed by the State, a percentage fee is a direct, uncontrollable deduction from margin.</p></div>
      <div class="card">{icon("bank")}<h3>Three incumbent acquirers</h3><p>Card acceptance in the DR runs through three platforms: CardNET (bank-owned), AZUL (Grupo Popular, launched 2014) and Visanet Dominicana. All three price fuel like any other retail category. None offers a program built around gallons, fleet cards or forecourt operations.</p></div>
      <div class="card">{icon("chart")}<h3>Growing network</h3><p>MICM approved 33 new stations and LPG plants between 2024 and October 2025, and keeps an open-data registry of licensed stations. Every new licence is a merchant that must choose an acquirer on day one.</p></div>
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="section-head"><span class="eyebrow">Scenario model</span><h2>What the launch cohort could represent.</h2><p>Adjust the assumptions. The default card volume per station is the national average implied by RD$41 billion a year across about 1,025 stations; Polígono Central sites are expected to run above it. This is an illustrative model, not a forecast.</p></div>
    <div class="calc" id="calc">
      <div>
        <div class="field"><label for="c-stations">Stations onboarded</label><input id="c-stations" type="number" min="1" value="20" /></div>
        <div class="field"><label for="c-volume">Card volume per station per month (RD$)</label><input id="c-volume" type="number" min="0" step="100000" value="3300000" /></div>
        <div class="field"><label for="c-mdr">Effective merchant discount rate (%)</label><input id="c-mdr" type="number" min="0" step="0.05" value="1.95" /></div>
        <div class="field"><label for="c-share">Sponsor bank share of gross MDR (%)</label><input id="c-share" type="number" min="0" max="100" step="1" value="20" /></div>
        <div class="field"><label for="c-fx">Exchange rate (RD$ per US$)</label><input id="c-fx" type="number" min="1" step="0.5" value="62" /></div>
        <p class="small muted">The bank-share field is a placeholder for negotiation and does not represent an offer. Interchange, network fees and terminal costs are not deducted here.</p>
      </div>
      <div class="out">
        <h3>Illustrative annual figures</h3>
        <div class="row"><span>Monthly card volume</span><b id="o-monthly"></b></div>
        <div class="row"><span>Annual card volume</span><b id="o-annual"></b></div>
        <div class="row"><span>Gross MDR revenue</span><b id="o-gross"></b></div>
        <div class="row"><span>Sponsor bank share</span><b id="o-bank"></b></div>
      </div>
    </div>
  </div>
</section>

<section class="alt"><div class="wrap">{sources_block(["listin_verifone", "dl_paises", "anadegas_retiro", "dl_conflicto", "dl_acuerdo", "infobae_30", "dl_41000", "dl_dialogo", "anadegas_1025", "bcrd_806", "bcrd_2025", "infobae_q1", "bcrd_boletin", "dl_efectivo", "mastercard", "micm_precios", "micm_33", "micm_datos", "trade_gov"])}</div></section>
"""
