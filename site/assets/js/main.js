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

  // Contact form: posts to the Pages Function at /api/contact; falls back to mailto.
  var form = document.querySelector('form.contact');
  if (form) {
    form.addEventListener('submit', function (ev) {
      ev.preventDefault();
      var status = form.querySelector('.form-status');
      var data = Object.fromEntries(new FormData(form).entries());
      if (data.website) return; // honeypot
      status.textContent = 'Sending…';
      fetch('/api/contact', { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify(data) })
        .then(function (r) { return r.ok ? r.json() : Promise.reject(r); })
        .then(function () { status.textContent = 'Thank you. We will reply within one business day.'; form.reset(); })
        .catch(function () {
          var body = encodeURIComponent('Name: ' + data.name + '\nOrganization: ' + data.org + '\nEmail: ' + data.email + '\n\n' + data.message);
          status.innerHTML = 'The form endpoint is not enabled yet. <a href="mailto:info@walletpartnersllc.com?subject=Wallet%20Partners%20inquiry&body=' + body + '">Send this message by email instead</a>.';
        });
    });
  }
})();
