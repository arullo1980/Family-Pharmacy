from common import icon

def body(ctx):
    return f"""
<div class="page-title"><div class="wrap">
  <span class="eyebrow">About</span>
  <h1>Wallet Partners LLC</h1>
  <p>A payments company with a single focus: helping fuel retailers in the Dominican Republic accept cards on terms that fit their business, under the oversight of a sponsoring bank.</p>
</div></div>

<section>
  <div class="wrap split">
    <div>
      <h2>Why we exist</h2>
      <p>Gasoline stations are among the highest-volume merchants in any economy, yet they are served with the same terminals, the same pricing and the same support as a corner shop. In the Dominican Republic that mismatch became a national news story in 2026, when the retailers' association threatened to stop accepting cards over commissions that consume a quarter to a third of their regulated margin.</p>
      <p>Wallet Partners was formed to build the specialised program the segment has been asking for: gallon-based pricing, forecourt-grade equipment, next-day settlement in pesos and local support, delivered as a merchant-of-record program manager under a licensed sponsoring bank.</p>
      <h2>How we work</h2>
      <ul class="checklist">
        <li><strong>Segment depth over breadth.</strong> One vertical, learned thoroughly, before any other.</li>
        <li><strong>Bank-grade controls from day one.</strong> Our operating model assumes the bank's auditors are in the room.</li>
        <li><strong>Transparency to the merchant.</strong> Interchange-plus statements and per-gallon fees the owner can check against the weekly MICM price notice.</li>
        <li><strong>Local presence.</strong> Field installation, training and support in Santo Domingo, in Spanish.</li>
      </ul>
    </div>
    <figure><picture><source srcset="/assets/img/hero-station.webp" type="image/webp" /><img src="/assets/img/hero-station.jpg" alt="Modern gasoline station on an avenue at dusk" loading="lazy" width="1280" height="720" /></picture><figcaption>Illustrative image.</figcaption></figure>
  </div>
</section>

<section class="alt">
  <div class="wrap">
    <div class="section-head"><h2>Company facts</h2></div>
    <div class="grid grid-3">
      <div class="card">{icon("doc")}<h3>Legal entity</h3><p>Wallet Partners LLC, a limited liability company organised in the United States. Dominican operations will be conducted through a locally registered affiliate as required by the sponsorship structure and Dominican law.</p></div>
      <div class="card">{icon("map")}<h3>Market</h3><p>Dominican Republic, starting with the Polígono Central of Santo Domingo, Distrito Nacional. Expansion to the wider capital region and Santiago follows the first cohort.</p></div>
      <div class="card">{icon("shield")}<h3>Status</h3><p>Pre-launch. Twenty stations are in the warm pipeline; we are selecting a sponsoring bank. Wallet Partners is not a bank and does not hold customer funds outside a sponsor-controlled program account.</p></div>
    </div>
    <div class="callout info mt-3"><p><strong>Leadership and advisers.</strong> Biographies of the founding team, our payments and compliance advisers, and Dominican legal counsel are provided in the sponsor-bank pack. <a href="/contact/">Request it here.</a></p></div>
  </div>
</section>
"""
