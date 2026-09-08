/* Bombero Partners — station map (Leaflet + OpenStreetMap tiles, no API key) */
(function () {
  'use strict';
  var root = document.getElementById('map');
  if (!root || typeof L === 'undefined' || !window.WP_STATIONS) return;

  var data = window.WP_STATIONS;
  var EN = document.documentElement.lang === 'en';
  var T = EN ? { inside: 'Inside polygon', edge: 'Adjacent', h24: 'Open 24 h', km: 'km from centre', maps: 'Google Maps', sv: 'Street View', show: 'Show on map', nophone: 'No published phone', of: ' of ', stations: ' stations', poly: 'Polígono Central (approximate boundary)', centre: 'Reference centre used for distances', isyours: 'Is this your station? Sign it up', signup: '/en/sign-up/?station=' }
             : { inside: 'Dentro del polígono', edge: 'Adyacente', h24: 'Abierta 24 h', km: 'km del centro', maps: 'Google Maps', sv: 'Street View', show: 'Ver en el mapa', nophone: 'Sin teléfono publicado', of: ' de ', stations: ' estaciones', poly: 'Polígono Central (límite aproximado)', centre: 'Centro de referencia para las distancias', isyours: '¿Es su estación? Regístrela', signup: '/afiliese/?estacion=' };
  var stations = data.stations;
  var compact = root.classList.contains('compact');

  var map = L.map(root, { scrollWheelZoom: !compact, zoomControl: true });
  L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
  }).addTo(map);

  // Approximate boundary of the Polígono Central (JFK / 27 de Febrero / Churchill / Máximo Gómez)
  var poly = L.polygon(data.polygon, {
    color: '#b97c00', weight: 2, dashArray: '6 6', fillColor: '#eda100', fillOpacity: 0.08
  }).addTo(map).bindTooltip('Polígono Central (límite aproximado)', { sticky: true });

  L.circleMarker([data.center.lat, data.center.lng], { radius: 5, color: '#0f2440', fillColor: '#fff', fillOpacity: 1, weight: 2 })
    .addTo(map).bindTooltip('Centro de referencia para las distancias');

  function icon(s) {
    return L.divIcon({
      className: '',
      html: '<div class="marker-pin ' + (s.inside ? 'inside' : 'edge') + '"><span>' + s.id + '</span></div>',
      iconSize: [26, 26], iconAnchor: [13, 26], popupAnchor: [0, -24]
    });
  }
  function popup(s) {
    return '<h4>' + s.id + '. ' + s.name + '</h4>' +
      '<span class="tag">' + s.brand + '</span>' +
      '<span class="tag">' + (s.inside ? 'Dentro del polígono' : 'Adyacente') + '</span>' +
      (s.open24h ? '<span class="tag">24 h</span>' : '') +
      '<div>' + s.address + '</div>' +
      '<div class="muted">' + s.hours + (s.phone ? ' · ' + s.phone : '') + ' · ' + s.distKm.toFixed(2) + ' km del centro</div>' +
      '<div class="links"><a href="' + s.maps + '" target="_blank" rel="noopener">Google Maps</a>' +
      '<a href="' + s.streetview + '" target="_blank" rel="noopener">Street View</a></div>';
  }

  var layer = L.featureGroup().addTo(map);
  var markers = {};
  stations.forEach(function (s) {
    var m = L.marker([s.lat, s.lng], { icon: icon(s), title: s.name }).bindPopup(popup(s));
    markers[s.id] = m;
  });

  var state = { zone: 'all', h24: false, brand: 'all', q: '' };
  var grid = document.getElementById('station-grid');
  var countEl = document.getElementById('station-count');
  var tbody = document.getElementById('station-tbody');

  function matches(s) {
    if (state.zone === 'inside' && !s.inside) return false;
    if (state.zone === 'edge' && s.inside) return false;
    if (state.h24 && !s.open24h) return false;
    if (state.brand !== 'all' && s.brand !== state.brand) return false;
    if (state.q) {
      var q = state.q.toLowerCase();
      if ((s.name + ' ' + s.address + ' ' + s.brand).toLowerCase().indexOf(q) < 0) return false;
    }
    return true;
  }

  function render() {
    layer.clearLayers();
    var shown = stations.filter(matches);
    shown.forEach(function (s) { layer.addLayer(markers[s.id]); });
    if (countEl) countEl.textContent = shown.length + ' de ' + stations.length + ' estaciones';
    if (grid) {
      grid.innerHTML = shown.map(function (s) {
        return '<article class="station" id="st-' + s.id + '" data-id="' + s.id + '">' +
          '<div class="top"><h3>' + s.name + '</h3><span class="n ' + (s.inside ? 'inside' : 'edge') + '">' + s.id + '</span></div>' +
          '<div class="addr">' + s.address + '</div>' +
          '<div class="meta"><span class="tag brand">' + s.brand + '</span>' +
          '<span class="tag">' + (s.inside ? 'Dentro del polígono' : 'Adyacente') + '</span>' +
          (s.open24h ? '<span class="tag h24">Abierta 24 h</span>' : '<span class="tag">' + s.hours + '</span>') +
          '<span class="tag">' + s.distKm.toFixed(2) + ' km</span></div>' +
          (s.phone ? '<div class="small muted">' + s.phone + '</div>' : '<div class="small muted">Sin teléfono publicado</div>') +
          '<div class="links"><a href="#map" data-focus="' + s.id + '">Ver en el mapa</a>' +
          '<a href="' + s.maps + '" target="_blank" rel="noopener">Google Maps</a>' +
          '<a href="' + s.streetview + '" target="_blank" rel="noopener">Street View</a>' +
          '<a href="/afiliese/?estacion=' + encodeURIComponent(s.name) + '"><strong>¿Es su estación? Regístrela</strong></a></div></article>';
      }).join('');
    }
    if (tbody) {
      tbody.innerHTML = shown.map(function (s) {
        return '<tr><td class="num">' + s.id + '</td><td>' + s.name + '</td><td>' + s.brand + '</td><td>' + s.address + '</td>' +
          '<td>' + (s.phone || '—') + '</td><td>' + s.hours + '</td><td>' + (s.inside ? T.inside : T.edge) + '</td>' +
          '<td class="num">' + s.distKm.toFixed(2) + '</td><td class="num">' + s.lat.toFixed(6) + ', ' + s.lng.toFixed(6) + '</td></tr>';
      }).join('');
    }
  }

  document.addEventListener('click', function (ev) {
    var a = ev.target.closest('[data-focus]');
    if (!a) return;
    ev.preventDefault();
    var id = +a.getAttribute('data-focus');
    var m = markers[id];
    if (!m) return;
    map.setView(m.getLatLng(), 17, { animate: true });
    m.openPopup();
    root.scrollIntoView({ behavior: 'smooth', block: 'center' });
    document.querySelectorAll('.station.active').forEach(function (el) { el.classList.remove('active'); });
    var card = document.getElementById('st-' + id);
    if (card) card.classList.add('active');
  });

  var zoneChips = document.querySelectorAll('[data-zone]');
  zoneChips.forEach(function (c) {
    c.addEventListener('click', function () {
      zoneChips.forEach(function (x) { x.setAttribute('aria-pressed', 'false'); });
      c.setAttribute('aria-pressed', 'true');
      state.zone = c.getAttribute('data-zone');
      render();
    });
  });
  var h24 = document.getElementById('f-24h');
  if (h24) h24.addEventListener('click', function () {
    state.h24 = !state.h24; h24.setAttribute('aria-pressed', state.h24 ? 'true' : 'false'); render();
  });
  var brandSel = document.getElementById('f-brand');
  if (brandSel) {
    var brands = {};
    stations.forEach(function (s) { brands[s.brand] = (brands[s.brand] || 0) + 1; });
    Object.keys(brands).sort(function (a, b) { return brands[b] - brands[a] || a.localeCompare(b); }).forEach(function (b) {
      var o = document.createElement('option'); o.value = b; o.textContent = b + ' (' + brands[b] + ')'; brandSel.appendChild(o);
    });
    brandSel.addEventListener('change', function () { state.brand = brandSel.value; render(); });
  }
  var q = document.getElementById('f-q');
  if (q) q.addEventListener('input', function () { state.q = q.value.trim(); render(); });

  render();
  map.fitBounds(poly.getBounds().extend(layer.getBounds()), { padding: [24, 24] });
})();
