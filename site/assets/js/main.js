/* Wallet Partners LLC — shared behaviour (no tracking, no third-party scripts) */
(function () {
  'use strict';

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

  // Scenario calculator (market / solution pages)
  var calc = document.getElementById('calc');
  if (calc) {
    var $ = function (id) { return document.getElementById(id); };
    var fmtRD = function (n) { return 'RD$' + Math.round(n).toLocaleString('en-US'); };
    var fmtUS = function (n) { return 'US$' + Math.round(n).toLocaleString('en-US'); };
    var run = function () {
      var stations = +$('c-stations').value || 0;
      var perStation = +$('c-volume').value || 0;      // RD$ per station per month (card)
      var mdr = (+$('c-mdr').value || 0) / 100;         // merchant discount rate
      var fx = +$('c-fx').value || 1;                   // RD$ per US$
      var bankShare = (+$('c-share').value || 0) / 100; // sponsor bank share of net MDR
      var monthly = stations * perStation;
      var annual = monthly * 12;
      var gross = annual * mdr;
      $('o-monthly').textContent = fmtRD(monthly) + ' / ' + fmtUS(monthly / fx);
      $('o-annual').textContent = fmtRD(annual) + ' / ' + fmtUS(annual / fx);
      $('o-gross').textContent = fmtRD(gross) + ' / ' + fmtUS(gross / fx);
      $('o-bank').textContent = fmtRD(gross * bankShare) + ' / ' + fmtUS(gross * bankShare / fx);
    };
    calc.addEventListener('input', run);
    run();
  }

  // Simple bar tooltips for the inline charts
  document.querySelectorAll('.viz[data-tip]').forEach(function (viz) {
    var tip = document.createElement('div');
    tip.className = 'tip';
    viz.style.position = 'relative';
    viz.appendChild(tip);
    viz.querySelectorAll('[data-label]').forEach(function (el) {
      el.addEventListener('mouseenter', function (ev) {
        tip.textContent = el.getAttribute('data-label');
        tip.classList.add('show');
      });
      el.addEventListener('mousemove', function (ev) {
        var r = viz.getBoundingClientRect();
        tip.style.left = (ev.clientX - r.left) + 'px';
        tip.style.top = (ev.clientY - r.top) + 'px';
      });
      el.addEventListener('mouseleave', function () { tip.classList.remove('show'); });
    });
  });

  // Forms (contacto, afiliación): post to the Pages Function at /api/contact; fall back to mailto.
  document.querySelectorAll('form.contact').forEach(function (form) {
    var en = document.documentElement.lang === 'en';
    form.addEventListener('submit', function (ev) {
      ev.preventDefault();
      var status = form.querySelector('.form-status');
      var data = Object.fromEntries(new FormData(form).entries());
      if (data.website) return; // honeypot
      var missing = Array.prototype.filter.call(form.querySelectorAll('[required]'), function (el) { return !el.value.trim(); });
      if (missing.length) { status.textContent = en ? 'Please complete the required fields.' : 'Complete los campos obligatorios.'; missing[0].focus(); return; }
      status.textContent = en ? 'Sending…' : 'Enviando…';
      fetch('/api/contact', { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify(data) })
        .then(function (r) { return r.ok ? r.json() : Promise.reject(r); })
        .then(function () { status.textContent = en ? 'Thank you. We will reply within one business day.' : 'Gracias. Le contactamos en un día hábil.'; form.reset(); })
        .catch(function () {
          var lines = Object.keys(data).filter(function (k) { return k !== 'website' && data[k]; }).map(function (k) { return k + ': ' + data[k]; });
          var body = encodeURIComponent(lines.join('\n'));
          var subj = encodeURIComponent(data.type === 'estacion' ? 'Afiliación de estación' : 'Consulta Wallet Partners');
          status.innerHTML = (en ? 'The form endpoint is not enabled yet. ' : 'El envío automático aún no está habilitado. ') +
            '<a href="mailto:info@walletpartnersllc.com?subject=' + subj + '&body=' + body + '">' + (en ? 'Send this by email instead' : 'Envíelo por correo con un clic') + '</a>.';
        });
    });
  });

  // Pricing calculator: what a percentage fee costs per gallon
  var pc = document.getElementById('calc-precios');
  if (pc) {
    var g = function (id) { return document.getElementById(id); };
    var rd = function (n) { return 'RD$' + Math.round(n).toLocaleString('es-DO'); };
    var runP = function () {
      var gal = +g('p-gal').value || 0, price = +g('p-precio').value || 0, share = (+g('p-tarjeta').value || 0) / 100;
      var fee = (+g('p-com').value || 0) / 100, margin = +g('p-margen').value || 0;
      var cardSales = gal * price * share, com = cardSales * fee, cardGal = gal * share;
      var perGal = cardGal ? com / cardGal : 0;
      g('p-o-ventas').textContent = rd(cardSales);
      g('p-o-com').textContent = rd(com);
      g('p-o-porgal').textContent = 'RD$' + perGal.toFixed(2);
      g('p-o-margen').textContent = margin ? (perGal / margin * 100).toFixed(0) + '%' : '—';
      g('p-o-anual').textContent = rd(com * 12);
    };
    pc.addEventListener('input', runP); runP();
  }
})();
