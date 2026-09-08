from common import sources_block

def body(ctx):
    st = ctx["stats"]
    return f"""
<div class="page-title"><div class="wrap">
  <span class="eyebrow">Launch pipeline</span>
  <h1>Twenty stations, one district.</h1>
  <p>Every gasoline station below has confirmed interest in onboarding once Wallet Partners' sponsoring bank and merchant-of-record arrangement are in place. They are the twenty stations closest to the centre of Santo Domingo's Polígono Central, the district bounded by Av. John F. Kennedy (north), Av. 27 de Febrero (south), Av. Winston Churchill (west) and Av. Máximo Gómez (east).</p>
  <div class="meta-line">Source list compiled {ctx['DATA_DATE']} from public map listings · {st['n']} stations · {st['inside']} inside the polygon, {st['edge']} adjacent · {st['h24']} open 24 hours · Coordinates in WGS 84</div>
</div></div>

<section>
  <div class="wrap">
    <div class="map-wrap">
      <div id="map" role="region" aria-label="Interactive map of pipeline gasoline stations"></div>
      <div class="map-legend"><span><i class="dot inside"></i> Inside Polígono Central</span><span><i class="dot edge"></i> Adjacent / edge</span><span><i class="poly-key"></i> Approximate boundary</span></div>
    </div>
    <div class="filters" role="group" aria-label="Filter stations">
      <button class="chip" data-zone="all" aria-pressed="true">All</button>
      <button class="chip" data-zone="inside" aria-pressed="false">Inside polygon</button>
      <button class="chip" data-zone="edge" aria-pressed="false">Adjacent</button>
      <button class="chip" id="f-24h" aria-pressed="false">Open 24 h</button>
      <label>Brand <select id="f-brand"><option value="all">All brands</option></select></label>
      <label><span class="sr-only">Search</span><input type="search" id="f-q" placeholder="Search name or street" /></label>
      <span class="count" id="station-count"></span>
    </div>
    <div class="station-grid" id="station-grid"></div>
  </div>
</section>

<section class="alt">
  <div class="wrap">
    <div class="section-head"><h2>Directory</h2><p>The same data as a table. Downloads: <a href="/data/stations.csv">CSV</a> · <a href="/data/stations.geojson">GeoJSON</a> · <a href="/data/stations.json">JSON</a>. Distances are measured from the reference centre at 18.4690, -69.9295.</p></div>
    <div class="table-wrap"><table>
      <thead><tr><th class="num">#</th><th>Station</th><th>Brand</th><th>Address</th><th>Phone</th><th>Hours</th><th>Zone</th><th class="num">km</th><th class="num">Lat, Lng</th></tr></thead>
      <tbody id="station-tbody"></tbody>
    </table></div>
    <div class="callout info mt-3">
      <p><strong>How to read this list.</strong> "Inside polygon" means the station falls within the four boundary avenues; "Adjacent" means it sits just outside the boundary, typically on the far side of one of those avenues. Blank phone numbers mean the business does not publish one. Opening hours are as listed publicly and should be re-verified during onboarding. The polygon drawn on the map is an approximation of the avenues for orientation only.</p>
    </div>
  </div>
</section>

<section>
  <div class="wrap grid grid-3">
    <div class="card"><h3>What the district looks like</h3><picture><source srcset="/assets/img/aerial.webp" type="image/webp" /><img src="/assets/img/aerial.jpg" alt="Aerial view of a business district with wide avenues and office towers" loading="lazy" width="1280" height="720" style="border-radius:8px;margin-bottom:10px" /></picture><p class="small muted">The Polígono Central concentrates corporate offices, hotels, banks and upper-income residential towers, which is why card penetration at these stations is expected to be well above the national average. Illustrative image.</p></div>
    <div class="card"><h3>Why these twenty first</h3><ul class="checklist"><li>Highest-traffic avenues in the capital (27 de Febrero, Kennedy, Churchill, Lincoln, Tiradentes).</li><li>Nine of twenty operate 24 hours: continuous card acceptance and night-shift cash-risk reduction.</li><li>Dense cluster within a 2.1 km radius: one field team can install and support every site.</li><li>Brand mix led by TotalEnergies ({st['brands'].get('TotalEnergies', 0)} sites) with independent and multi-brand operators, which lets us prove the model across operator types.</li></ul></div>
    <div class="card"><h3>Onboarding readiness</h3><p>For each station we are assembling the merchant file our sponsoring bank will need: legal entity and RNC, MICM operating resolution, beneficial owners and IDs, bank account for settlement, expected monthly volume and average ticket, and site photos. Files are shared under NDA on request.</p><a class="btn btn-navy" href="/contact/">Request station files</a></div>
  </div>
</section>

<section class="alt"><div class="wrap">{sources_block(["micm_datos", "micm_precios"], "Reference data")}</div></section>
"""
