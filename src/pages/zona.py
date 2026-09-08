def body(ctx):
    st = ctx["stats"]
    return f"""
<div class="page-title"><div class="wrap">
  <span class="eyebrow">Zona de lanzamiento</span>
  <h1>Empezamos en el Polígono Central.</h1>
  <p>Las primeras instalaciones se concentran en las {st['n']} estaciones dentro y alrededor del Polígono Central de Santo Domingo, el distrito delimitado por la Av. John F. Kennedy (norte), la Av. 27 de Febrero (sur), la Av. Winston Churchill (oeste) y la Av. Máximo Gómez (este). Un solo equipo de campo instala y da soporte a toda la zona.</p>
  <div class="meta-line">{st['n']} estaciones · {st['inside']} dentro del polígono, {st['edge']} adyacentes · {st['h24']} abiertas 24 horas · Datos de listados públicos, {ctx['DATA_DATE']}</div>
</div></div>

<section><div class="wrap">
  <div class="map-wrap">
    <div id="map" role="region" aria-label="Mapa interactivo de la zona de lanzamiento"></div>
    <div class="map-legend"><span><i class="dot inside"></i> Dentro del Polígono Central</span><span><i class="dot edge"></i> Borde / adyacente</span><span><i class="poly-key"></i> Límite aproximado</span></div>
  </div>
  <div class="filters" role="group" aria-label="Filtrar estaciones">
    <button class="chip" data-zone="all" aria-pressed="true">Todas</button>
    <button class="chip" data-zone="inside" aria-pressed="false">Dentro del polígono</button>
    <button class="chip" data-zone="edge" aria-pressed="false">Adyacentes</button>
    <button class="chip" id="f-24h" aria-pressed="false">Abiertas 24 h</button>
    <label>Marca <select id="f-brand"><option value="all">Todas las marcas</option></select></label>
    <label><span class="sr-only">Buscar</span><input type="search" id="f-q" placeholder="Buscar nombre o calle" /></label>
    <span class="count" id="station-count"></span>
  </div>
  <div class="station-grid" id="station-grid"></div>
  <div class="callout info mt-3"><p><strong>¿Es su estación?</strong> <a href="/afiliese/">Regístrela</a> y le damos prioridad en la primera ola de instalaciones. ¿No aparece? Regístrese igual: abrimos nuevas zonas del Distrito Nacional y Santiago según la demanda. Los horarios y teléfonos provienen de listados públicos y se confirman durante la afiliación.</p></div>
</div></section>

<section class="alt"><div class="wrap grid grid-3">
  <div class="card"><h3>Por qué aquí primero</h3><ul class="checklist"><li>Avenidas de mayor tráfico de la capital: 27 de Febrero, Kennedy, Churchill, Lincoln, Tiradentes.</li><li>{st['h24']} de {st['n']} estaciones operan 24 horas.</li><li>Todo dentro de un radio de {st['maxDist']:.1f} km: instalación y soporte el mismo día.</li></ul></div>
  <div class="card"><picture><source srcset="/assets/img/aerial.webp" type="image/webp" /><img src="/assets/img/aerial.jpg" alt="Vista aérea de un distrito de negocios con avenidas anchas y torres de oficinas" loading="lazy" width="1280" height="720" style="border-radius:8px;margin-bottom:10px" /></picture><p class="small muted">El Polígono Central concentra oficinas, hoteles, bancos y torres residenciales, donde el pago con tarjeta es más frecuente. Imagen ilustrativa.</p></div>
  <div class="card"><h3>Siguientes zonas</h3><p>Después de la primera ola abrimos el resto del Distrito Nacional, Santo Domingo Este y Oeste, y Santiago. Si su estación está fuera del polígono, regístrela ahora para entrar en la lista de espera de su zona.</p><a class="btn btn-navy" href="/afiliese/">Registrar mi estación</a></div>
</div></section>
"""
