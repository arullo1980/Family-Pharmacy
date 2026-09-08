"""English versions of every public page (served under /en/)."""
from common import stat_tiles, icon, sources_block
import json

def home(ctx):
    st = ctx["stats"]
    return f"""
<section class="hero">
  <picture><source srcset="/assets/img/hero-station.webp" type="image/webp" /><img class="hero-img" src="/assets/img/hero-station.jpg" alt="" fetchpriority="high" /></picture>
  <div class="wrap">
    <span class="eyebrow">For gasoline stations · Dominican Republic</span>
    <h1>Accept cards and pay 0.25% less than your current contract.</h1>
    <p class="lead">Bombero Partners is a card-acceptance program built only for gasoline stations: a rate 25 basis points below your current processing contract, no monthly minimum, transactions cleared in US dollars, forecourt terminals and support in Santo Domingo. We operate under the sponsorship of a licensed bank.</p>
    <div class="hero-actions"><a class="btn btn-primary" href="/en/sign-up/">Sign up your station</a><a class="btn btn-ghost" href="/en/pricing/">Calculate your savings</a></div>
    {stat_tiles([("−0.25%", "versus your current contract", "25 basis points less on every transaction"), ("USD", "transactions cleared in dollars", "statement per station and per shift"), ("24 h", "continuous operation", "wireless EMV and contactless terminals"), ("Local", "installation and support", "in the Distrito Nacional")])}
  </div>
</section>
<section><div class="wrap">
  <div class="section-head"><span class="eyebrow">The problem</span><h2>A 1.95% to 2.50% fee takes a quarter to a third of your margin.</h2><p>The retail price and the retailer's margin are set by the State every week. On a gross margin of about RD$25 per gallon, a percentage fee equals RD$6.59–8.45 per gallon: 25% to 36% of what the station keeps, according to the figures ANADEGAS published in July 2026. Our offer is simple: 25 basis points less than the fee you pay today, with no monthly minimum.</p></div>
  <div class="grid grid-3">
    <div class="card">{icon("pump")}<h3>25 basis points less</h3><p>Bring your current processing contract and we quote 0.25% below that rate. No monthly minimum: sell less in a month, pay less.</p></div>
    <div class="card">{icon("clock")}<h3>Cleared in dollars</h3><p>Transactions are cleared in US dollars, with a statement by shift and by pump so your accountant and cashier balance without surprises.</p></div>
    <div class="card">{icon("shield")}<h3>Less cash, less risk</h3><p>More card sales mean less cash in the till on the night shift, fewer shortfalls and less exposure for your staff.</p></div>
  </div>
</div></section>
<section class="alt"><div class="wrap split">
  <figure><picture><source srcset="/assets/img/pos-tap.webp" type="image/webp" /><img src="/assets/img/pos-tap.jpg" alt="Customer paying contactless on a wireless terminal next to a fuel pump" loading="lazy" width="1280" height="720" /></picture><figcaption>Illustrative image.</figcaption></figure>
  <div>
    <span class="eyebrow">How it works</span><h2>Three steps to start taking cards.</h2>
    <ol class="timeline"><li><strong>Register online.</strong> Five minutes. We ask for the station's details, its MICM resolution and its RNC.</li><li><strong>Approval and installation.</strong> The sponsoring bank approves the file; our team installs the terminals and trains your staff on the forecourt.</li><li><strong>Charge and get paid.</strong> Chip, contactless and mobile wallets. Transactions clear in dollars to the account you designate.</li></ol>
    <a class="btn btn-navy" href="/en/how-it-works/">All the details</a>
  </div>
</div></section>
<section><div class="wrap">
  <div class="section-head"><span class="eyebrow">Launch zone</span><h2>We start in Santo Domingo's Polígono Central.</h2><p>The first installations go to the {st['n']} stations inside and around the Polígono Central (Av. Kennedy, 27 de Febrero, Churchill and Máximo Gómez). Is your station on the map? Register it and you get priority in the first wave. Elsewhere? Register anyway: we open new areas by demand.</p></div>
  <div class="map-wrap"><div id="map" class="compact" role="region" aria-label="Map of the launch zone in the Polígono Central"></div>
  <div class="map-legend"><span><i class="dot inside"></i> Inside the Polígono Central ({st['inside']})</span><span><i class="dot edge"></i> Edge / adjacent ({st['edge']})</span><span><i class="poly-key"></i> Approximate boundary</span></div></div>
  <p class="mt-2"><a href="/en/launch-zone/">See the full launch-zone list</a></p>
</div></section>
<section class="alt"><div class="wrap">
  <div class="section-head"><span class="eyebrow">What is included</span><h2>Everything a station needs, nothing it doesn't.</h2></div>
  <div class="grid grid-3">
    <div class="card">{icon("card")}<h3>Forecourt terminals</h3><p>Wireless, rugged, chip and contactless, receipt printing and Spanish prompts. Pump-controller integration where your equipment supports it.</p></div>
    <div class="card">{icon("chart")}<h3>Owner dashboard</h3><p>Sales by pump, shift and product; card mix; chargebacks; downloadable statements for your accountant and DGII filings.</p></div>
    <div class="card">{icon("doc")}<h3>Clear statements</h3><p>You see interchange, the network fee and our fee separately. A monthly terminal rental and no other fixed charge.</p></div>
    <div class="card">{icon("shield")}<h3>Fraud protection</h3><p>Limits per pump and per card, EMV compliance and a dispute desk that works chargebacks on the station's behalf.</p></div>
    <div class="card">{icon("map")}<h3>Support on the street</h3><p>Technicians in Santo Domingo, in Spanish, with terminal replacement in hours, not weeks.</p></div>
    <div class="card">{icon("bank")}<h3>Bank backing</h3><p>Funds settle through a licensed sponsoring bank under Visa and Mastercard rules. Bombero Partners does not hold your money.</p></div>
  </div>
</div></section>
<section class="dark"><div class="wrap"><div class="section-head"><span class="eyebrow">First wave</span><h2>Reserve your place in the first wave of installations.</h2><p>Registering commits you to nothing. We call you, review your volume together and send a written proposal with numbers for your station.</p></div><div class="hero-actions"><a class="btn btn-primary" href="/en/sign-up/">Sign up your station</a><a class="btn btn-ghost" href="/en/faq/">FAQ</a></div></div></section>
"""

def how(ctx):
    return f"""
<div class="page-title"><div class="wrap"><span class="eyebrow">How it works</span><h1>From the pump to your account, no surprises.</h1><p>How Bombero Partners' card-acceptance program for gasoline stations works, from registration to settlement.</p></div></div>
<section><div class="wrap"><div class="section-head"><h2>Every transaction, step by step</h2></div>
<ol class="timeline">
<li><strong>The customer pays on the forecourt.</strong> The attendant keys the amount or the pump controller sends it to the wireless terminal. Chip, contactless and mobile wallets are accepted; magnetic stripe is disabled by policy.</li>
<li><strong>Authorisation.</strong> The terminal sends the transaction, encrypted end to end, to the sponsoring bank's platform, which routes it to Visa, Mastercard or the local debit network.</li>
<li><strong>Settlement.</strong> The bank receives funds from the networks and transactions clear in US dollars to the account you designate, net of the agreed fee (0.25% below your current contract).</li>
<li><strong>Reconciliation.</strong> You receive a statement by shift and by pump, with interchange, the network fee and our fee shown separately.</li>
<li><strong>Disputes.</strong> If a customer disputes a charge, our dispute desk builds the case with the receipt and terminal evidence and defends it with the network.</li>
</ol></div></section>
<section class="alt"><div class="wrap"><div class="section-head"><span class="eyebrow">Onboarding</span><h2>What we need to sign up your station</h2><p>The sponsoring bank reviews every file. With these documents approval normally takes under ten business days.</p></div>
<div class="grid grid-2">
<div class="card"><h3>Station documents</h3><ul class="checklist"><li>Valid MICM operating resolution</li><li>RNC and commercial registry</li><li>Company constitutive documents</li><li>Proof of address and photos of the site</li></ul></div>
<div class="card"><h3>Owner documents</h3><ul class="checklist"><li>ID or passport of partners holding 10% or more</li><li>ID of the legal representative</li><li>Certification of the bank account that will receive settlement</li><li>Estimated monthly volume and average ticket</li></ul></div>
</div>
<div class="callout info mt-3"><p><strong>Under contract with another processor?</strong> Review it with us. In most cases you keep your current bank account and only the card processor changes.</p></div></div></section>
<section><div class="wrap"><div class="section-head"><span class="eyebrow">Equipment</span><h2>Terminals designed for the forecourt</h2></div>
<div class="grid grid-3">
<div class="card">{icon("card")}<h3>Wireless and rugged</h3><p>Battery for the whole shift, 4G and wifi, resistant to dust and light rain.</p></div>
<div class="card">{icon("pump")}<h3>Fuel flow</h3><p>Pre-authorisation and completion for automated pumps, tip disabled, printed receipt and Spanish prompts.</p></div>
<div class="card">{icon("chart")}<h3>Integration</h3><p>Connection to the pump controller when the station's equipment allows it, so no amounts are keyed by hand.</p></div>
</div></div></section>
<section class="dark"><div class="wrap"><div class="section-head"><h2>Ready to start?</h2><p>Register your station and an adviser contacts you within one business day.</p></div><a class="btn btn-primary" href="/en/sign-up/">Sign up your station</a></div></section>
"""

def pricing(ctx):
    return """
<div class="page-title"><div class="wrap"><span class="eyebrow">Pricing</span><h1>0.25% below your current contract. No monthly minimum.</h1><p>Four terms, no small print. The final rate is set in the merchant agreement approved by the sponsoring bank, starting from the rate you pay today.</p></div></div>
<section><div class="wrap">
<div class="grid grid-2">
<div class="card"><h3>1. 25 basis points less</h3><p>Your rate will be 0.25 percentage points below your current processing contract. If you pay 2.25% today, with us you pay 2.00%.</p></div>
<div class="card"><h3>2. No monthly minimum</h3><p>There is no minimum billing. You pay only for the transactions you process.</p></div>
<div class="card"><h3>3. Terminal on monthly rental</h3><p>The terminal is supplied on a fixed monthly rental that includes replacement and support. No equipment purchase.</p></div>
<div class="card"><h3>4. Cleared in dollars</h3><p>Transactions are cleared in US dollars to the account you designate.</p></div>
</div>
<div class="callout mt-3"><p><strong>Transparency.</strong> The statement shows interchange (what the issuing bank charges), the network fee and our fee separately, so you can compare with your current contract line by line.</p></div>
</div></section>
<section class="alt"><div class="wrap">
<div class="section-head"><span class="eyebrow">Calculator</span><h2>How much do you save with 25 basis points less?</h2><p>Enter your monthly gallons, the share of sales paid by card and the fee you pay today. The calculator shows what you pay today, what you would pay at our rate and the annual saving. It is an estimate from your own numbers, not a quote.</p></div>
<div class="calc" id="calc-precios">
  <div>
    <div class="field"><label for="p-gal">Gallons sold per month</label><input id="p-gal" type="number" min="0" step="1000" value="120000" /></div>
    <div class="field"><label for="p-precio">Average price per gallon (RD$)</label><input id="p-precio" type="number" min="0" step="0.1" value="281" /></div>
    <div class="field"><label for="p-tarjeta">Sales paid by card (%)</label><input id="p-tarjeta" type="number" min="0" max="100" step="1" value="40" /></div>
    <div class="field"><label for="p-com">Fee you pay today (%)</label><input id="p-com" type="number" min="0" step="0.05" value="2.25" /></div>
    <div class="field"><label for="p-margen">Gross margin per gallon (RD$)</label><input id="p-margen" type="number" min="0" step="0.5" value="25" /></div>
    <p class="small muted">Starting values: average of premium (RD$290.10) and regular (RD$272.50) gasoline per MICM notices in 2025; fee and margin from figures published by ANADEGAS in 2026. Replace them with your station's numbers.</p>
  </div>
  <div class="out"><h3>With your numbers</h3>
    <div class="row"><span>Card sales per month</span><b id="p-o-ventas"></b></div>
    <div class="row"><span>Fees you pay per month</span><b id="p-o-com"></b></div>
    <div class="row"><span>Fee per gallon sold on card</span><b id="p-o-porgal"></b></div>
    <div class="row"><span>Share of your margin lost to fees</span><b id="p-o-margen"></b></div>
    <div class="row"><span>With Bombero Partners (−0.25%) per month</span><b id="p-o-nueva"></b></div>
    <div class="row"><span>Saving per year</span><b id="p-o-ahorro"></b></div>
  </div>
</div>
<p class="mt-3"><a class="btn btn-navy" href="/en/sign-up/">Request a proposal with your exact rate</a></p>
</div></section>
<section><div class="wrap prose">
<h2>Pricing questions</h2>
<h3>What is the exact rate?</h3><p>Your current rate minus 0.25 percentage points. To quote it we need to see your current contract or statement; we put it in writing before you sign anything.</p><h3>How much does the terminal cost?</h3><p>It is supplied on a fixed monthly rental that includes support and replacement. The amount is stated in the proposal.</p><h3>Why dollars?</h3><p>The program settles through a sponsoring bank that clears in US dollars. Funds arrive in USD in the account you designate.</p>
<h3>What is interchange?</h3><p>The part of the fee kept by the bank that issued the customer's card, set by Visa and Mastercard. We show it separately so you know exactly which part of the cost is ours.</p>
<h3>Are there chargeback fees?</h3><p>Only when a chargeback is lost. Our dispute desk works every case with the receipt and terminal evidence.</p>
<h3>Tax withholding?</h3><p>We apply the withholdings DGII requires for card payments in your category and itemise them on every statement. Confirm with your accountant; we are happy to walk through the treatment.</p>
</div></section>
"""

def zone(ctx):
    st = ctx["stats"]
    return f"""
<div class="page-title"><div class="wrap"><span class="eyebrow">Launch zone</span><h1>We start in the Polígono Central.</h1><p>The first installations concentrate on the {st['n']} stations inside and around Santo Domingo's Polígono Central, the district bounded by Av. John F. Kennedy (north), Av. 27 de Febrero (south), Av. Winston Churchill (west) and Av. Máximo Gómez (east). One field team installs and supports the whole zone.</p>
<div class="meta-line">{st['n']} stations · {st['inside']} inside the polygon, {st['edge']} adjacent · {st['h24']} open 24 hours · Public listings, {ctx['DATA_DATE']}</div></div></div>
<section><div class="wrap">
<div class="map-wrap"><div id="map" role="region" aria-label="Interactive map of the launch zone"></div>
<div class="map-legend"><span><i class="dot inside"></i> Inside the Polígono Central</span><span><i class="dot edge"></i> Edge / adjacent</span><span><i class="poly-key"></i> Approximate boundary</span></div></div>
<div class="filters" role="group" aria-label="Filter stations">
  <button class="chip" data-zone="all" aria-pressed="true">All</button><button class="chip" data-zone="inside" aria-pressed="false">Inside polygon</button><button class="chip" data-zone="edge" aria-pressed="false">Adjacent</button><button class="chip" id="f-24h" aria-pressed="false">Open 24 h</button>
  <label>Brand <select id="f-brand"><option value="all">All brands</option></select></label>
  <label><span class="sr-only">Search</span><input type="search" id="f-q" placeholder="Search name or street" /></label>
  <span class="count" id="station-count"></span>
</div>
<div class="station-grid" id="station-grid"></div>
<div class="callout info mt-3"><p><strong>Is this your station?</strong> <a href="/en/sign-up/">Register it</a> and you get priority in the first wave of installations. Not listed? Register anyway: we open new areas of the Distrito Nacional and Santiago by demand. Hours and phones come from public listings and are confirmed during onboarding.</p></div>
</div></section>
<section class="alt"><div class="wrap grid grid-3">
<div class="card"><h3>Why here first</h3><ul class="checklist"><li>The capital's busiest avenues: 27 de Febrero, Kennedy, Churchill, Lincoln, Tiradentes.</li><li>{st['h24']} of {st['n']} stations operate 24 hours.</li><li>Everything within a {st['maxDist']:.1f} km radius: same-day installation and support.</li></ul></div>
<div class="card"><picture><source srcset="/assets/img/aerial.webp" type="image/webp" /><img src="/assets/img/aerial.jpg" alt="Aerial view of a business district with wide avenues and office towers" loading="lazy" width="1280" height="720" style="border-radius:8px;margin-bottom:10px" /></picture><p class="small muted">The Polígono Central concentrates offices, hotels, banks and residential towers, where card payment is most common. Illustrative image.</p></div>
<div class="card"><h3>Next areas</h3><p>After the first wave we open the rest of the Distrito Nacional, Santo Domingo Este and Oeste, and Santiago. If your station is outside the polygon, register now to join the waiting list for your area.</p><a class="btn btn-navy" href="/en/sign-up/">Register my station</a></div>
</div></section>
"""

FAQ = [
    ("Do I have to change banks?", "No. Settlement is deposited into whichever bank account you designate, at any bank in the country. Only the company processing cards at your station changes."),
    ("In which currency do I receive the money?", "Transactions are cleared in US dollars to the account you designate. The statement details every shift."),
    ("Which cards can I accept?", "Visa and Mastercard, credit and debit, domestic and international, with chip, contactless and mobile wallets. Other networks are added as the sponsoring bank enables them."),
    ("How much does the terminal cost?", "The terminal is supplied on a fixed monthly rental that includes support and replacement. There is no minimum billing."),
    ("Is there a minimum term?", "The contract is one year, renewable, and can be cancelled with 30 days' notice without penalty by returning the equipment."),
    ("How is the fee calculated?", "25 basis points (0.25%) below the rate in your current processing contract, with no monthly minimum. On the statement you see interchange, the network fee and our fee separately."),
    ("What about chargebacks?", "Our dispute desk builds the case with the receipt and terminal evidence and defends it with the network. The chargeback is only charged if the dispute is lost."),
    ("Which documents do I need?", "MICM resolution, RNC and commercial registry, constitutive documents, IDs of partners with 10% or more and of the legal representative, and a bank-account certification."),
    ("How long does approval take?", "Normally under ten business days once the file is complete. Installation is scheduled the same week as approval."),
    ("Who is the sponsoring bank?", "A licensed financial institution, member of Visa and Mastercard, that approves each merchant, receives funds from the networks and oversees the program. Its name appears in the merchant agreement."),
    ("Does Bombero Partners hold my money?", "No. Funds settle through a program account controlled by the sponsoring bank and are transferred in dollars to the account you designate."),
    ("Does it work with my pump controller?", "With the most common systems, yes. If not, the terminal works standalone: the attendant keys the amount."),
    ("Can I accept fleet cards?", "Planned for a second phase together with a station loyalty program. We will let you know when it is available."),
    ("What if my station is not in the Polígono Central?", "Register anyway. We open areas by demand and let you know when your sector comes up."),
]

def faq(ctx):
    items = "".join(f'<details class="card" style="margin-bottom:12px"><summary style="cursor:pointer;font-weight:700;color:var(--navy)">{q}</summary><p style="margin:10px 0 0">{a}</p></details>' for q, a in FAQ)
    ld = json.dumps({"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in FAQ]}, ensure_ascii=False)
    return f"""
<div class="page-title"><div class="wrap"><span class="eyebrow">FAQ</span><h1>What station owners ask us.</h1><p>If your question is not here, <a href="/en/contact/">write to us</a> and we reply within one business day.</p></div></div>
<section><div class="wrap prose" style="max-width:860px">{items}</div></section>
<script type="application/ld+json">{ld}</script>
<section class="dark"><div class="wrap"><div class="section-head"><h2>Convinced?</h2><p>Register your station and we send a proposal with numbers for your volume.</p></div><a class="btn btn-primary" href="/en/sign-up/">Sign up your station</a></div></section>
"""

def signup(ctx):
    return """
<div class="page-title"><div class="wrap"><span class="eyebrow">Sign up</span><h1>Register your station.</h1><p>Five minutes. It commits you to nothing: we contact you within one business day, review your volume and send a written proposal: 0.25% below your current contract, no monthly minimum, monthly terminal rental and clearing in dollars.</p></div></div>
<section><div class="wrap grid grid-2">
<div><form class="contact" method="post" action="/api/contact" novalidate>
  <input type="hidden" name="type" value="estacion" />
  <label>Station name <input name="org" type="text" required autocomplete="organization" /></label>
  <label>Address and city <input name="address" type="text" required autocomplete="street-address" /></label>
  <label>Owner or manager name <input name="name" type="text" required autocomplete="name" /></label>
  <label>Phone or WhatsApp <input name="phone" type="tel" required autocomplete="tel" /></label>
  <label>Email <input name="email" type="email" required autocomplete="email" /></label>
  <label>Gallons sold per month (approx.) <input name="gallons" type="number" min="0" step="1000" /></label>
  <label>Card sales today (%) <input name="cardshare" type="number" min="0" max="100" /></label>
  <label>Who processes your cards today? <select name="processor"><option>I do not accept cards</option><option>CardNET</option><option>AZUL</option><option>Visanet</option><option>Other</option></select></label>
  <label>Comments <textarea name="message"></textarea></label>
  <label class="hp" aria-hidden="true">Website <input name="website" type="text" tabindex="-1" autocomplete="off" /></label>
  <button class="btn btn-navy" type="submit">Send request</button>
  <p class="form-status" role="status" aria-live="polite"></p>
  <p class="form-note">By sending you accept our <a href="/en/legal/privacy/">privacy policy</a>. We use your details only to respond and prepare the proposal.</p>
</form></div>
<div>
  <div class="card"><h3>What happens next</h3><ol class="timeline"><li><strong>Day 1.</strong> An adviser calls you, confirms your volume and answers your questions.</li><li><strong>Days 2–5.</strong> You receive the written proposal with your rate (current contract − 0.25%) and the terminal rental.</li><li><strong>Days 5–15.</strong> We gather the documents and the sponsoring bank approves the file.</li><li><strong>Installation.</strong> We schedule installation and training on your forecourt.</li></ol></div>
  <div class="card mt-2"><h3>Have at hand</h3><ul class="checklist"><li>MICM resolution</li><li>RNC and commercial registry</li><li>IDs of partners and representative</li><li>Bank-account certification</li><li>Your current processing contract or statement</li></ul></div>
</div>
</div></section>
"""

def banks(ctx):
    st = ctx["stats"]
    return f"""
<div class="page-title"><div class="wrap"><span class="eyebrow">Banks &amp; partners</span><h1>A vertical fuel-retail acquiring program, operated under your sponsorship.</h1><p>Wallet Partners LLC is seeking a sponsoring bank, a Visa and Mastercard member in the Dominican Republic, to launch a payment-facilitation program dedicated to gasoline stations, clearing in US dollars. This page is the summary; the full presentation is shared under NDA.</p></div></div>
<section><div class="wrap">{stat_tiles([("≈1,025", "fuel stations nationwide", "ANADEGAS estimate, 2026"), ("RD$41 bn", "annual card payments at stations", "Diario Libre, Jul 2026"), ("1.95–2.50%", "fees stations pay today", "25–36% of gross margin per gallon"), (str(st["n"]), "stations in the launch zone", "Polígono Central, Santo Domingo")])}</div></section>
<section class="alt"><div class="wrap">
<div class="section-head"><span class="eyebrow">Why now</span><h2>The segment publicly asked for a different pricing model.</h2><p>In June and July 2026 the national fuel-retailers association threatened to pull card terminals from more than 780 stations over percentage fees that consume a quarter to a third of a State-regulated margin. The Government opened a dialogue with the banks. A program priced 25 basis points below each station's current contract, with no monthly minimum, dollar clearing, transparent interchange and bank-grade controls gives a sponsoring bank a defensible route into a high-volume segment while the incumbents negotiate.</p></div>
<div class="grid grid-3">
<div class="card">{icon("bank")}<h3>What the bank does</h3><p>Network membership and BINs, approval of each merchant, program settlement account with reserves, second-line oversight and regulatory reporting.</p></div>
<div class="card">{icon("pump")}<h3>What Bombero Partners does</h3><p>Prospecting and onboarding, KYB/KYC files prepared to the bank's standard, terminals and field support, first-line monitoring, disputes, merchant settlement and reporting to the bank.</p></div>
<div class="card">{icon("shield")}<h3>Compliance framework</h3><p>PCI DSS with P2PE terminals, Law 155-17 (AML/CFT), Law 172-13 (data protection), Visa and Mastercard payment-facilitator rules, MCC 5541/5542. <a href="/en/legal/compliance/">Full framework</a>.</p></div>
</div></div></section>
<section><div class="wrap split">
<div><span class="eyebrow">The ask</span><h2>A sponsorship agreement, then one merchant file at a time.</h2>
<ul class="checklist"><li>Visa and Mastercard acquiring membership in the DR, or a correspondent arrangement that permits program sponsorship.</li><li>Registration of Bombero Partners as payment facilitator / program manager.</li><li>A program settlement account with agreed reserve and release terms.</li><li>Merchant approval within ten business days per file.</li><li>A named relationship contact and a compliance contact.</li></ul></div>
<div class="card"><h3>The sponsor-bank deck covers</h3><ul class="checklist"><li>Executive summary and the 2026 fee-dispute timeline</li><li>Banco Central payment-system data and fuel-market structure</li><li>Map and list of the {st['n']} launch-zone stations</li><li>Program design, responsibility matrix and rollout plan</li><li>Volume and revenue scenario model</li><li>Compliance framework and available document set</li></ul><a class="btn btn-navy" href="/en/contact/?tipo=banco">Request the deck</a></div>
</div></section>
"""

def about(ctx):
    return f"""
<div class="page-title"><div class="wrap"><span class="eyebrow">About</span><h1>Bombero Partners</h1><p>The Dominican trade name of Wallet Partners LLC: a payments company with a single goal: that gasoline stations in the Dominican Republic accept cards on terms that fit their business.</p></div></div>
<section><div class="wrap split">
<div><h2>Why we exist</h2>
<p>Gasoline stations are among the highest-volume merchants in any economy, yet they are served with the same terminals, the same pricing and the same support as a corner shop. In 2026 that mismatch became national news when the retailers' association threatened to stop accepting cards.</p>
<p>Bombero Partners was formed to build the specialised program the sector has been asking for: a rate 25 basis points below the current contract, no monthly minimum, forecourt equipment, dollar clearing and local support, operated as a payment facilitator under a licensed sponsoring bank.</p>
<h2>How we work</h2>
<ul class="checklist"><li><strong>One sector, in depth.</strong> Fuel first; nothing else until it is done well.</li><li><strong>Bank-grade controls from day one.</strong> Our operating model assumes the bank's auditors are in the room.</li><li><strong>Transparency to the merchant.</strong> Statements the owner can check against the weekly MICM notice.</li><li><strong>Local presence.</strong> Installation, training and support in Santo Domingo, in Spanish.</li></ul></div>
<figure><picture><source srcset="/assets/img/hero-station.webp" type="image/webp" /><img src="/assets/img/hero-station.jpg" alt="Modern gasoline station on an avenue at dusk" loading="lazy" width="1280" height="720" /></picture><figcaption>Illustrative image.</figcaption></figure>
</div></section>
<section class="alt"><div class="wrap"><div class="grid grid-3">
<div class="card">{icon("doc")}<h3>Entity</h3><p>Bombero Partners is a trade name (DBA) of Wallet Partners LLC, a limited liability company organised in the United States. Dominican operations are conducted through a locally registered affiliate as required by the sponsorship structure and Dominican law.</p></div>
<div class="card">{icon("map")}<h3>Market</h3><p>Dominican Republic, starting with Santo Domingo's Polígono Central and expanding to the rest of the Distrito Nacional and Santiago.</p></div>
<div class="card">{icon("shield")}<h3>Status</h3><p>Pre-launch. We are selecting the sponsoring bank and registering first-wave stations. Bombero Partners is not a bank and does not hold merchant funds outside the bank-controlled program account.</p></div>
</div></div></section>
"""

def contact(ctx):
    email = ctx["CONTACT_EMAIL"]
    return f"""
<div class="page-title"><div class="wrap"><span class="eyebrow">Contact</span><h1>Let's talk.</h1><p>For stations, banks, technology partners and press. We reply within one business day, in English or Spanish.</p></div></div>
<section><div class="wrap grid grid-2">
<div><form class="contact" method="post" action="/api/contact" novalidate>
  <input type="hidden" name="type" value="contacto" />
  <label>Name <input name="name" type="text" required autocomplete="name" /></label>
  <label>Company or organisation <input name="org" type="text" autocomplete="organization" /></label>
  <label>Email <input name="email" type="email" required autocomplete="email" /></label>
  <label>I am writing as <select name="role" id="role"><option value="estacion">Station owner or operator</option><option value="banco">Bank or financial institution</option><option value="aliado">Technology or payments partner</option><option value="prensa">Press</option><option value="otro">Other</option></select></label>
  <label>Message <textarea name="message" required></textarea></label>
  <label class="hp" aria-hidden="true">Website <input name="website" type="text" tabindex="-1" autocomplete="off" /></label>
  <button class="btn btn-navy" type="submit">Send</button>
  <p class="form-status" role="status" aria-live="polite"></p>
  <p class="form-note">By sending you accept our <a href="/en/legal/privacy/">privacy policy</a>.</p>
</form></div>
<div>
  <div class="card"><h3>Direct</h3><p><a href="mailto:{email}">{email}</a></p><p class="small muted">For security disclosures see <a href="/.well-known/security.txt">security.txt</a>.</p></div>
  <div class="card mt-2"><h3>Stations</h3><p>If you want a proposal with numbers, use the <a href="/en/sign-up/">sign-up form</a>: it asks for the data we need to calculate your fee.</p></div>
  <div class="card mt-2"><h3>Banks and partners</h3><p>Select "Bank or financial institution" and we send the full presentation after an NDA.</p></div>
</div>
</div></section>
"""

def _page(eyebrow, title, intro, content, updated="2026-09-08"):
    return f"""
<div class="page-title"><div class="wrap"><span class="eyebrow">{eyebrow}</span><h1>{title}</h1><p>{intro}</p><div class="meta-line">Last updated {updated}</div></div></div>
<section><div class="wrap prose">{content}</div></section>
"""

def privacy(ctx):
    e = ctx["CONTACT_EMAIL"]
    return _page("Legal", "Privacy policy", "How Wallet Partners LLC handles personal data received through this website and in the course of its business.", f"""
<h2>1. Controller</h2><p>Wallet Partners LLC, doing business as Bombero Partners ("Bombero Partners", "we"), operates this website. For questions about this policy or to exercise your rights write to <a href="mailto:{e}">{e}</a>.</p>
<h2>2. Data we collect on this website</h2>
<ul><li><strong>Forms.</strong> Name, company or station, address, phone, email, any volume figures you enter and the content of your message. We use them to reply, prepare a proposal and keep a record of the enquiry.</li>
<li><strong>Server logs.</strong> Our hosting provider, Cloudflare, processes IP addresses and request metadata to deliver the site, protect it from abuse and produce aggregate statistics, under its own privacy policy.</li>
<li><strong>Local storage.</strong> One key in your browser records that you dismissed the cookie notice. It contains no identifier. See the <a href="/en/legal/cookies/">cookie notice</a>.</li></ul>
<p>We use no advertising trackers, analytics scripts or social-media pixels. Map tiles are loaded from CARTO and OpenStreetMap servers, which receive your IP address when requested.</p>
<h2>3. Data we process in our business</h2><p>When a station applies to join our program we collect the information the sponsoring bank and the card networks require to evaluate a merchant: legal-entity details and RNC, operating licences, identity and contact details of owners, directors and beneficial owners, the bank account for settlement, and transaction data generated by card acceptance. We process it to perform the merchant agreement, comply with legal obligations (including Law 155-17 against money laundering) and prevent fraud.</p>
<h2>4. Legal basis and applicable law</h2><p>We process data of Dominican residents under Law No. 172-13 on Protection of Personal Data and, where applicable, Law No. 183-02 and the regulations of the Monetary Board and the Superintendency of Banks. Data of persons in the United States is processed under applicable federal and state law. Where consent is the basis, you may withdraw it at any time.</p>
<h2>5. Sharing</h2><p>Only with the sponsoring bank and card networks as required to provide the service; with providers acting on our instructions (hosting, email delivery, terminal management, identity verification); with professional advisers; and with authorities where the law requires. We do not sell personal data.</p>
<h2>6. International transfers</h2><p>Bombero Partners is organised in the United States and uses cloud providers, so data may be processed outside the Dominican Republic under contractual safeguards and the security measures below.</p>
<h2>7. Retention</h2><p>Website enquiries are kept up to 24 months. Merchant and transaction records are kept for the periods required by card-network rules and Dominican and U.S. law, generally at least five years after the relationship ends, or ten where Law 155-17 requires it.</p>
<h2>8. Security</h2><p>Encryption in transit and at rest, role-based access, activity logging and vendor due diligence. This website never stores card data; program terminals use point-to-point encryption and we operate under PCI DSS.</p>
<h2>9. Your rights</h2><p>You may request access, correction, deletion or portability of your data, and object to or restrict processing, by writing to <a href="mailto:{e}">{e}</a>. We respond within the statutory period. You may also complain to the competent authority.</p>
<h2>10. Children</h2><p>This website is aimed at businesses, not at persons under 18.</p>
<h2>11. Changes</h2><p>The date above shows the latest revision. Material changes will be highlighted on this page.</p>
""")

def terms(ctx):
    e = ctx["CONTACT_EMAIL"]
    return _page("Legal", "Terms of use", "Conditions for using this website.", f"""
<h2>1. Acceptance</h2><p>By using this website you agree to these terms. If you do not agree, do not use it.</p>
<h2>2. Purpose</h2><p>This site presents Wallet Partners LLC's card-acceptance program for gasoline stations in the Dominican Republic. It is informational. Nothing on it constitutes an offer of banking or financial services, an invitation to invest, or financial, legal or tax advice. Final service terms (rate, terminal rental and settlement currency) are set only in the merchant agreement approved by the sponsoring bank.</p>
<h2>3. Calculators and figures</h2><p>Calculators produce estimates from the values you enter and are not quotes. Market figures are quoted from identified public sources and may be revised by their authors. Station information comes from public listings and may change.</p>
<h2>4. No banking relationship</h2><p>Wallet Partners LLC is not a bank, not a licensed financial intermediary in the Dominican Republic and not a member of any card network in its own right. Services will be provided only once a sponsorship agreement with a licensed member financial institution is in force.</p>
<h2>5. Intellectual property</h2><p>Text, graphics, code and the station dataset are © Wallet Partners LLC unless otherwise stated. Map data © OpenStreetMap contributors (ODbL); basemap style © CARTO. Fuel brands belong to their owners and are cited only to identify locations, implying no affiliation or endorsement.</p>
<h2>6. Acceptable use</h2><p>Do not attempt unauthorised access to the site or its hosting, or use it for unlawful purposes. Security researchers should follow the process in <a href="/.well-known/security.txt">security.txt</a>.</p>
<h2>7. Third-party links</h2><p>Links to media, regulators and map services are provided for convenience. We do not control and are not responsible for their content.</p>
<h2>8. Limitation of liability</h2><p>The site is provided "as is". To the extent permitted by law we exclude all warranties and are not liable for losses arising from use of the site or reliance on its content.</p>
<h2>9. Governing law</h2><p>These terms are governed by the laws of the State in which Wallet Partners LLC is organised, without prejudice to mandatory consumer-protection rules under Law No. 358-05 for users in the Dominican Republic.</p>
<h2>10. Contact</h2><p><a href="mailto:{e}">{e}</a></p>
""")

def cookies(ctx):
    return _page("Legal", "Cookie notice", "This site uses very few cookies. Here is exactly what it stores.", """
<h2>What we store</h2>
<div class="table-wrap"><table><thead><tr><th>Name</th><th>Type</th><th>Purpose</th><th>Duration</th></tr></thead><tbody>
<tr><td><span class="kbd">wp_cookie_notice</span></td><td>localStorage (not a cookie)</td><td>Remembers that you dismissed the cookie notice</td><td>Until you clear site data</td></tr>
<tr><td><span class="kbd">__cf_bm</span>, <span class="kbd">cf_clearance</span> (only if triggered)</td><td>Cloudflare cookie</td><td>Bot protection and security challenges for the hosting platform</td><td>Up to 30 minutes / as set by Cloudflare</td></tr>
</tbody></table></div>
<h2>What we do not use</h2><p>No analytics cookies, no advertising cookies, no social-media plug-ins, no cross-site tracking.</p>
<h2>Third-party content</h2><p>The interactive map loads tiles from CARTO / OpenStreetMap. Those requests reveal your IP address to the provider but set no cookies on this site.</p>
<h2>Your choices</h2><p>You can clear or block local storage and cookies in your browser. The site's content does not change; the notice simply reappears.</p>
""")

def compliance(ctx):
    return _page("Compliance", "Compliance & regulatory framework", "How Wallet Partners LLC operates within card-network rules, Dominican financial regulation and the oversight of a sponsoring bank. This page summarises the programme; full policies are shared with banks and regulators under NDA.", f"""
<div class="callout info"><p><strong>Status.</strong> Bombero Partners is pre-launch. The controls below are being built to the standard a sponsoring bank will require and are validated before the first live transaction.</p></div>
<h2>1. Regulatory map</h2>
<h3>Dominican Republic</h3>
<ul><li><strong>Law No. 183-02, Monetary and Financial Law</strong>, and the Monetary Board's <strong>Payment Systems Regulation (SIPARD)</strong>, amended August 2025. The Banco Central oversees the payment system; acquiring is performed by or under financial intermediaries supervised by the <strong>Superintendencia de Bancos</strong>. Bombero Partners will operate as program manager / payment facilitator under a licensed member bank and will register any locally required entity.</li>
<li><strong>Law No. 155-17 against money laundering and terrorist financing</strong>, its regulations and UAF guidance: merchant due diligence, beneficial-ownership identification, transaction monitoring, record-keeping and suspicious-transaction reporting through the sponsoring bank.</li>
<li><strong>Law No. 172-13 on personal data protection</strong>: lawful processing, security measures and data-subject rights.</li>
<li><strong>Law No. 358-05 on consumer protection</strong> (Pro Consumidor): transparent pricing, receipts and complaint handling at the point of sale.</li>
<li><strong>Tax.</strong> DGII rules on card-transaction withholding (Norma General 08-04 and successors) and the fuel tax regime (Laws 112-00 and 557-05, under which retail fuel bears selective and ad-valorem taxes rather than ITBIS). Withholding parameters for stations are confirmed with the sponsoring bank and tax counsel before launch.</li>
<li><strong>Fuel sector.</strong> Only stations with a valid MICM operating resolution are eligible; the resolution and DGII registration form part of every merchant file.</li></ul>
<h3>United States and international</h3>
<ul><li><strong>BSA/AML programme</strong> aligned with the sponsor's requirements and, where applicable, FinCEN registration; <strong>OFAC</strong> and other sanctions screening of all merchants and beneficial owners.</li>
<li><strong>Card-network rules</strong> (Visa Core Rules and Mastercard Rules) for payment facilitators and sponsored merchants, including MCC 5541 (service stations) and 5542 (automated fuel dispensers), AFD authorisation and completion rules, and MATCH checks.</li>
<li><strong>PCI DSS v4.0</strong> as a Level 1 service provider at launch, with P2PE terminals so no cardholder data touches Bombero Partners' systems in clear text.</li></ul>
<h2>2. Merchant onboarding (KYB / KYC)</h2>
<ul><li>Legal-entity verification: constitutive documents, RNC, commercial registry, MICM resolution, proof of address and site photographs.</li><li>Identification of directors and beneficial owners at 10% or more; identity documents; PEP, sanctions and adverse-media screening.</li><li>Financial profile: expected monthly volume, average ticket, card-present share; bank-account ownership verification.</li><li>Risk rating and approval workflow: Bombero Partners prepares and recommends; the bank approves, conditions or declines. Refresh at least every two years or on trigger events.</li></ul>
<h2>3. Monitoring and fraud</h2>
<ul><li>Fuel rules: per-card and per-pump velocity limits, ticket caps consistent with tank capacity, duplicate detection, unusual night-time patterns and card-testing detection.</li><li>Portfolio monitoring against network chargeback and fraud thresholds; early-warning reporting to the bank.</li><li>Escalation to the bank's compliance function; suspicious-transaction reporting through the bank to the UAF and, where applicable, FinCEN.</li></ul>
<h2>4. Funds, settlement and reserves</h2>
<ul><li>Network settlement is received by the sponsoring bank into a program account it controls. Bombero Partners does not hold merchant funds outside that structure.</li><li>Settlement to merchants in US dollars, with reserves and release rules set with the bank per risk tier.</li><li>Daily reconciliation and monthly reporting to the bank.</li></ul>
<h2>5. Information security</h2>
<ul><li>Validated P2PE terminals; tokenisation; no PAN, track or CVV stored.</li><li>Segmented cloud environment, encryption at rest, dual-control key management, MFA for all administrative access, central logging and alerting.</li><li>Annual penetration testing, vulnerability management, vendor assessments and an incident-response plan with notification timelines agreed with the bank and under Law 172-13.</li><li>Coordinated vulnerability disclosure via <a href="/.well-known/security.txt">security.txt</a>.</li></ul>
<h2>6. Governance</h2>
<ul><li>Designated compliance officer; board-approved AML, sanctions, privacy and information-security policies; annual independent review.</li><li>Training for all staff and field technicians.</li><li>Records retained at least five years (ten where Law 155-17 requires), available to the bank and regulators; contractual right-to-audit for the bank.</li><li>Merchant complaints handled per the bank's terms and Pro Consumidor rules.</li></ul>
<h2>7. Documents available to banks</h2>
<ul><li>AML/CFT programme and risk assessment</li><li>Sanctions screening procedure</li><li>Merchant underwriting policy and file template</li><li>Transaction-monitoring rule set (fuel)</li><li>Information-security policy set and PCI DSS plan</li><li>Privacy programme (Law 172-13)</li><li>Business-continuity and incident-response plans</li><li>Draft sponsorship term sheet and reserve model</li></ul>
{sources_block(["ley_183", "jm_sipard", "sb_normativas"], "References")}
""")

def notice(ctx):
    e = ctx["CONTACT_EMAIL"]
    return _page("Legal", "Legal notice", "Identification of the website operator and related disclosures.", f"""
<h2>Website operator</h2><p><strong>Wallet Partners LLC</strong>, doing business as <strong>Bombero Partners</strong><br />A limited liability company organised under the laws of the United States.<br />Email: <a href="mailto:{e}">{e}</a></p>
<p>Registered agent, state of formation and registration number are provided on request and will be published here at launch together with the details of the Dominican operating affiliate.</p>
<h2>Regulatory status</h2><p>Wallet Partners LLC is not a bank, savings institution, money transmitter or licensed financial intermediary in the Dominican Republic and is not currently a registered payment facilitator with any card network. Services will be provided only under a sponsorship agreement with a licensed member financial institution, whose identity will be disclosed in the merchant agreement.</p>
<h2>Trademarks</h2><p>"Bombero Partners" is a trade name (DBA) of Wallet Partners LLC; the name and logo are the property of Wallet Partners LLC. TotalEnergies, Shell, Texaco, Next, Axxon, Tropigás, Sigma, VP Racing, Óptimo Gas, Trovasa, Visa, Mastercard, CardNET, AZUL, Visanet and other names belong to their owners and are cited only to identify locations and market participants, implying no sponsorship, affiliation or endorsement.</p>
<h2>Content and images</h2><p>Station data was compiled from public listings on {ctx['DATA_DATE']}. Photographic images on this site are computer-generated illustrations and do not depict specific stations, people or brands. Map data © OpenStreetMap contributors (ODbL); basemap © CARTO.</p>
<h2>Hosting</h2><p>This site is served by Cloudflare, Inc.</p>
""")

def accessibility(ctx):
    e = ctx["CONTACT_EMAIL"]
    return _page("Legal", "Accessibility statement", "We want every station owner and partner to be able to use this site.", f"""
<p>Wallet Partners LLC aims to conform to the Web Content Accessibility Guidelines (WCAG) 2.2 at level AA. Measures taken:</p>
<ul><li>Semantic HTML with a skip link, landmarks and a logical heading order.</li><li>Keyboard-operable navigation, filters and forms; visible focus.</li><li>Text contrast at or above 4.5:1; information never conveyed by colour alone (markers carry numbers; charts have table views).</li><li>Text alternatives for images; decorative images marked as such.</li><li>The map has an accessible name and an equivalent list.</li><li>No motion that cannot be paused; no auto-playing media.</li></ul>
<h2>Known limitations</h2><p>The interactive map uses a third-party library (Leaflet); keyboard panning may be limited in some browsers. The station list below the map provides the same information.</p>
<h2>Feedback</h2><p>If you encounter a barrier, email <a href="mailto:{e}">{e}</a> and we will respond within five business days.</p>
""")
