from common import stat_tiles, icon

def body(ctx):
    st = ctx["stats"]
    return f"""
<div class="page-title"><div class="wrap"><span class="eyebrow">For banks &amp; partners</span><h1>A vertical fuel-retail acquiring program, operated under your sponsorship.</h1><p>Wallet Partners LLC is seeking a sponsoring bank, a Visa and Mastercard member in the Dominican Republic, to launch a payment-facilitation program dedicated to gasoline stations. This page is the summary; the full presentation is shared under NDA.</p><div class="meta-line"><a href="/bancos/" lang="es">Leer esta página en español</a></div></div></div>

<section><div class="wrap">
  {stat_tiles([
    ("≈1,025", "fuel stations nationwide", "ANADEGAS estimate, 2026"),
    ("RD$41 bn", "annual card payments at stations", "Diario Libre, Jul 2026"),
    ("1.95–2.50%", "fees stations pay today", "25–36% of gross margin per gallon"),
    (str(st["n"]), "stations in the launch zone", "Polígono Central, Santo Domingo"),
  ])}
</div></section>

<section class="alt"><div class="wrap">
  <div class="section-head"><span class="eyebrow">Why now</span><h2>The segment publicly asked for a different pricing model.</h2><p>In June and July 2026 the national fuel-retailers association threatened to pull card terminals from more than 780 stations over percentage fees that consume a quarter to a third of a State-regulated margin. The Government opened a dialogue with the banks. A per-gallon program with transparent interchange and bank-grade controls gives a sponsoring bank a defensible route into a high-volume segment while the incumbents negotiate.</p></div>
  <div class="grid grid-3">
    <div class="card">{icon("bank")}<h3>What the bank does</h3><p>Network membership and BINs, approval of each merchant, program settlement account with reserves, second-line oversight and regulatory reporting.</p></div>
    <div class="card">{icon("pump")}<h3>What Wallet Partners does</h3><p>Prospecting and onboarding, KYB/KYC files prepared to the bank's standard, terminals and field support, first-line monitoring, disputes, merchant settlement and reporting to the bank.</p></div>
    <div class="card">{icon("shield")}<h3>Compliance framework</h3><p>PCI DSS with P2PE terminals, Law 155-17 (AML/CFT), Law 172-13 (data protection), Visa and Mastercard payment-facilitator rules, MCC 5541/5542. <a href="/legal/cumplimiento/">Full framework (Spanish)</a>.</p></div>
  </div>
</div></section>

<section><div class="wrap split">
  <div>
    <span class="eyebrow">The ask</span>
    <h2>A sponsorship agreement, then one merchant file at a time.</h2>
    <ul class="checklist">
      <li>Visa and Mastercard acquiring membership in the DR, or a correspondent arrangement that permits program sponsorship.</li>
      <li>Registration of Wallet Partners as payment facilitator / program manager.</li>
      <li>A program settlement account with agreed reserve and release terms.</li>
      <li>Merchant approval within ten business days per file.</li>
      <li>A named relationship contact and a compliance contact.</li>
    </ul>
  </div>
  <div class="card"><h3>The sponsor-bank deck covers</h3><ul class="checklist"><li>Executive summary and the 2026 fee-dispute timeline</li><li>Banco Central payment-system data and fuel-market structure</li><li>Map and list of the {st['n']} launch-zone stations</li><li>Program design, responsibility matrix and rollout plan</li><li>Volume and revenue scenario model</li><li>Compliance framework and available document set</li></ul><a class="btn btn-navy" href="/contacto/?tipo=banco">Request the deck</a></div>
</div></section>
"""
