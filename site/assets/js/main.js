/* Wallet Partners LLC — shared behaviour (no tracking, no third-party scripts) */
(function () {
  'use strict';
  var EN = document.documentElement.lang === 'en';

  // Mobile navigation
  var toggle = document.querySelector('.nav-toggle');
  var nav = document.querySelector('.nav');
  if (toggle && nav) {
    toggle.addEventListener('click', function () {
      var open = nav.classList.toggle('open');
      toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
  }

  // Cookie notice: this site only sets a single functional preference key.
  var banner = document.getElementById('cookie-banner');
  if (banner) {
    var seen = null;
    try { seen = localStorage.getItem('wp_cookie_notice'); } catch (e) {}
    if (!seen) banner.classList.add('show');
    var btn = document.getElementById('cookie-ok');
    if (btn) btn.addEventListener('click', function () {
      try { localStorage.setItem('wp_cookie_notice', '1'); } catch (e) {}
      banner.classList.remove('show');
    });
  }

  // Pricing calculator: what today's percentage fee costs, and the saving at 25 bps less
  var pc = document.getElementById('calc-precios');
  if (pc) {
    var g = function (id) { return document.getElementById(id); };
    var rd = function (n) { return 'RD$' + Math.round(n).toLocaleString('en-US'); };
    var runP = function () {
      var gal = +g('p-gal').value || 0, price = +g('p-precio').value || 0, share = (+g('p-tarjeta').value || 0) / 100;
      var fee = (+g('p-com').value || 0) / 100, margin = +g('p-margen').value || 0;
      var cardSales = gal * price * share, com = cardSales * fee, perGal = price * fee;
      var newCom = cardSales * Math.max(0, fee - 0.0025);
      g('p-o-ventas').textContent = rd(cardSales);
      g('p-o-com').textContent = rd(com);
      g('p-o-porgal').textContent = 'RD$' + perGal.toFixed(2);
      g('p-o-margen').textContent = margin ? Math.round(100 * perGal / margin) + '%' : '—';
      if (g('p-o-anual')) g('p-o-anual').textContent = rd(com * 12);
      if (g('p-o-nueva')) g('p-o-nueva').textContent = rd(newCom);
      if (g('p-o-ahorro')) g('p-o-ahorro').textContent = rd((com - newCom) * 12);
    };
    pc.addEventListener('input', runP);
    runP();
  }

  // Simple hover tooltips for inline charts
  document.querySelectorAll('.viz[data-tip]').forEach(function (viz) {
    var tip = document.createElement('div');
    tip.className = 'tip';
    viz.style.position = 'relative';
    viz.appendChild(tip);
    viz.querySelectorAll('[data-label]').forEach(function (el) {
      el.addEventListener('mouseenter', function () { tip.textContent = el.getAttribute('data-label'); tip.classList.add('show'); });
      el.addEventListener('mousemove', function (ev) { var r = viz.getBoundingClientRect(); tip.style.left = (ev.clientX - r.left) + 'px'; tip.style.top = (ev.clientY - r.top) + 'px'; });
      el.addEventListener('mouseleave', function () { tip.classList.remove('show'); });
    });
  });

  // Pre-fill the station name from ?estacion= / ?station= (links on the launch-zone map)
  var qs = new URLSearchParams(location.search);
  var pre = qs.get('estacion') || qs.get('station');
  var orgField = document.querySelector('form.contact input[name="org"]');
  if (pre && orgField && !orgField.value) orgField.value = pre;

  // Contact / sign-up forms: post to the Pages Function at /api/contact; fall back to mailto.
  var MSG = EN ? { sending: 'Sending…', ok: 'Thank you. We will reply within one business day.', fallback: 'The form endpoint is not enabled yet. ', link: 'Send this message by email instead', subject: 'Bombero Partners inquiry', subjStation: 'Station sign-up' }
             : { sending: 'Enviando…', ok: 'Gracias. Le respondemos en un día hábil.', fallback: 'El formulario aún no está activo. ', link: 'Envíe el mensaje por correo electrónico', subject: 'Consulta Bombero Partners', subjStation: 'Afiliación de estación' };
  var form = document.querySelector('form.contact');
  if (form) {
    form.addEventListener('submit', function (ev) {
      ev.preventDefault();
      var status = form.querySelector('.form-status');
      var data = Object.fromEntries(new FormData(form).entries());
      if (data.website) return; // honeypot
      status.textContent = MSG.sending;
      fetch('/api/contact', { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify(data) })
        .then(function (r) { return r.ok ? r.json() : Promise.reject(r); })
        .then(function () { status.textContent = MSG.ok; form.reset(); })
        .catch(function () {
          var lines = Object.keys(data).filter(function (k) { return k !== 'website' && data[k]; }).map(function (k) { return k + ': ' + data[k]; });
          var subj = encodeURIComponent(data.type === 'estacion' ? MSG.subjStation : MSG.subject);
          status.innerHTML = MSG.fallback + '<a href="mailto:info@walletpartnersllc.com?subject=' + subj + '&body=' + encodeURIComponent(lines.join('\n')) + '">' + MSG.link + '</a>.';
        });
    });
  }
})();
