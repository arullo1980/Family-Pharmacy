from common import icon, sources_block

def body(ctx):
    return f"""
<div class="page-title"><div class="wrap">
  <span class="eyebrow">Solution</span>
  <h1>A fuel-retail acquiring program, operated under your sponsorship.</h1>
  <p>Wallet Partners acts as the merchant-facing program manager and merchant of record. The sponsoring bank holds the card-network membership, settles funds and retains oversight. Below is how the pieces fit together and what each party does.</p>
</div></div>

<section>
  <div class="wrap">
    <div class="section-head"><h2>How a transaction flows</h2></div>
    <ol class="timeline">
      <li><strong>Customer pays at the forecourt.</strong> The attendant keys the sale or the pump controller pushes the amount to a wireless EMV/contactless terminal. Chip, tap and mobile wallets are accepted; magnetic stripe is disabled by policy.</li>
      <li><strong>Authorisation.</strong> The terminal sends the transaction through Wallet Partners' certified gateway to the sponsoring bank's acquiring host, which routes it to Visa, Mastercard or the domestic debit network under the bank's BINs and merchant identifiers.</li>
      <li><strong>Settlement.</strong> The bank receives funds from the networks and settles to Wallet Partners' program account. We pay each station in Dominican pesos on the next business day, net of the agreed per-gallon fee, with a statement showing interchange, network fees and our margin separately.</li>
      <li><strong>Reporting and reconciliation.</strong> Stations get daily reconciliation by shift and pump; the bank gets portfolio-level dashboards, exception reports and the data needed for its own regulatory reporting.</li>
      <li><strong>Disputes and risk.</strong> Chargebacks are worked by our operations team following network rules; reserves and velocity limits per station protect the bank's exposure.</li>
    </ol>
  </div>
</section>

<section class="alt">
  <div class="wrap">
    <div class="section-head"><span class="eyebrow">Division of responsibilities</span><h2>Who does what.</h2></div>
    <div class="table-wrap"><table>
      <thead><tr><th>Function</th><th>Wallet Partners LLC</th><th>Sponsoring bank</th></tr></thead>
      <tbody>
        <tr><td>Card-network membership and BIN sponsorship</td><td>—</td><td>Holds membership; registers Wallet Partners as payment facilitator / program manager</td></tr>
        <tr><td>Merchant prospecting and sales</td><td>Owns the pipeline and relationship with each station</td><td>—</td></tr>
        <tr><td>Merchant KYC / KYB and underwriting</td><td>Collects documents, screens beneficial owners and sanctions lists, prepares the file</td><td>Approves each merchant against its policy; can decline or set conditions</td></tr>
        <tr><td>Terminals and integration</td><td>Supplies certified EMV/contactless terminals; installs and supports on site</td><td>Certifies the terminal and gateway on its host</td></tr>
        <tr><td>Pricing to the station</td><td>Sets per-gallon pricing within bank-approved parameters</td><td>Approves pricing floors and interchange pass-through</td></tr>
        <tr><td>Settlement</td><td>Pays stations next day from program account; maintains reserves</td><td>Settles network funds into the program account; controls the account</td></tr>
        <tr><td>Transaction monitoring and AML</td><td>First-line monitoring, alerts, suspicious-activity escalation</td><td>Second-line review; regulatory reporting to Dominican and home-country authorities</td></tr>
        <tr><td>Disputes and chargebacks</td><td>Handles representment and merchant recovery</td><td>Network-facing dispute processing</td></tr>
        <tr><td>PCI DSS</td><td>Maintains its own compliance; terminals are P2PE, no cardholder data stored</td><td>Validates Wallet Partners as a service provider; annual attestation review</td></tr>
        <tr><td>Audit and oversight</td><td>Provides access to records, monthly reporting, right-to-audit</td><td>Periodic reviews; can suspend merchants or the program</td></tr>
      </tbody>
    </table></div>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="section-head"><span class="eyebrow">Product</span><h2>What the station gets.</h2></div>
    <div class="grid grid-3">
      <div class="card">{icon("card")}<h3>Per-gallon pricing</h3><p>A fee expressed in pesos per gallon, capped so the station's effective rate stops rising when the Ministry raises pump prices. Interchange-plus statements make the cost transparent to the owner and to the bank.</p></div>
      <div class="card">{icon("clock")}<h3>Next-day pesos</h3><p>Settlement in Dominican pesos on the next business day, per station, with shift-level reconciliation to reduce cash handling and night-time cash risk at 24-hour sites.</p></div>
      <div class="card">{icon("pump")}<h3>Forecourt-ready terminals</h3><p>Rugged wireless EMV/contactless terminals for attendants, with pre-authorisation and completion flows, tip suppression, receipt printing and Spanish-language prompts. Pump-controller integration where the station's equipment supports it.</p></div>
      <div class="card">{icon("chart")}<h3>Owner dashboard</h3><p>Sales by pump, shift and product; card mix; chargeback status; downloadable statements formatted for the station's accountant and DGII filings.</p></div>
      <div class="card">{icon("shield")}<h3>Fraud and chargeback controls</h3><p>Velocity limits per pump and per card, EMV liability-shift compliance, receipt capture and a dispute desk that works cases on the station's behalf.</p></div>
      <div class="card">{icon("doc")}<h3>Fleet and loyalty ready</h3><p>The platform is designed to add fleet-card acceptance and station loyalty programs in a second phase, giving the sponsoring bank additional issuing and co-brand opportunities.</p></div>
    </div>
  </div>
</section>

<section class="alt">
  <div class="wrap split">
    <div>
      <span class="eyebrow">Rollout plan</span>
      <h2>From sponsorship to live stations in one quarter.</h2>
      <ol class="timeline">
        <li><strong>Weeks 1–4: program set-up.</strong> Sponsorship agreement, payment-facilitator registration with the networks, gateway and terminal certification on the bank's host, program account and reserve structure.</li>
        <li><strong>Weeks 3–8: merchant underwriting.</strong> Bank review of the twenty pipeline files; site surveys; connectivity checks; terminal provisioning.</li>
        <li><strong>Weeks 8–12: staged go-live.</strong> Five stations in the first wave inside the polygon, then the remaining fifteen in two waves. Daily settlement and monitoring from the first transaction.</li>
        <li><strong>Quarter 2 onward: expansion.</strong> Extend across Distrito Nacional and Santiago using the same playbook; add fleet cards; review pricing with the bank against actual interchange.</li>
      </ol>
    </div>
    <div>
      <div class="card"><h3>What we ask of a sponsoring bank</h3><ul class="checklist"><li>Visa and Mastercard acquiring membership in the Dominican Republic, or a correspondent arrangement that permits program sponsorship.</li><li>Registration of Wallet Partners as payment facilitator / program manager.</li><li>A program settlement account with agreed reserve and release terms.</li><li>Merchant-approval SLA of ten business days per file.</li><li>A named relationship and compliance contact.</li></ul></div>
      <div class="card mt-2"><h3>What we bring</h3><ul class="checklist"><li>Twenty stations ready to sign, with files prepared to the bank's standard.</li><li>A pricing model the segment has publicly asked for.</li><li>Operations, field support and dispute handling in Spanish, on the ground in Santo Domingo.</li><li>A documented compliance programme (<a href="/legal/compliance/">details</a>).</li><li>Transparent, auditable reporting.</li></ul></div>
    </div>
  </div>
</section>

<section class="dark"><div class="wrap"><div class="section-head"><h2>Request the detailed program pack</h2><p>The pack includes the merchant-file template, pricing schedule, reserve model, PCI attestation plan, AML programme summary and the draft sponsorship term sheet.</p></div><a class="btn btn-primary" href="/contact/">Contact us</a></div></section>
"""
