from common import stat_tiles, icon

def body(ctx):
    st = ctx["stats"]
    return f"""
<section class="hero">
  <picture><source srcset="/assets/img/hero-station.webp" type="image/webp" /><img class="hero-img" src="/assets/img/hero-station.jpg" alt="" fetchpriority="high" /></picture>
  <div class="wrap">
    <span class="eyebrow">Para estaciones de combustible · República Dominicana</span>
    <h1>Acepte tarjetas y pague 0.25% menos que con su contrato actual.</h1>
    <p class="lead">Bombero Partners es un programa de aceptación de tarjetas hecho solo para estaciones de gasolina: una tarifa 25 puntos básicos por debajo de su contrato de procesamiento actual, sin mínimo mensual, transacciones liquidadas en dólares, terminales para el patio de bombas y soporte en Santo Domingo. Operamos bajo el patrocinio de un banco autorizado.</p>
    <div class="hero-actions">
      <a class="btn btn-primary" href="/afiliese/">Afilie su estación</a>
      <a class="btn btn-ghost" href="/precios/">Calcule su ahorro</a>
    </div>
    {stat_tiles([
      ("−0.25%", "frente a su contrato actual", "25 puntos básicos menos en cada transacción"),
      ("USD", "transacciones liquidadas en dólares", "estado de cuenta por estación y por turno"),
      ("24 h", "operación continua", "terminales inalámbricas EMV y sin contacto"),
      ("Local", "instalación y soporte", "en el Distrito Nacional"),
    ])}
  </div>
</section>

<section>
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">El problema</span>
      <h2>Una comisión de 1.95% a 2.50% se lleva entre la cuarta parte y la tercera parte de su margen.</h2>
      <p>El precio de venta y el margen del detallista los fija el Estado cada semana. Con un margen bruto de unos RD$25 por galón, una comisión porcentual equivale a RD$6.59–8.45 por galón: entre 25% y 36% de lo que le queda a la estación, según las cifras que ANADEGAS hizo públicas en julio de 2026. Nuestra oferta es simple: 25 puntos básicos menos que la comisión que paga hoy, sin mínimo mensual.</p>
    </div>
    <div class="grid grid-3">
      <div class="card">{icon("pump")}<h3>25 puntos básicos menos</h3><p>Traiga su contrato de procesamiento actual y le cotizamos 0.25% por debajo de esa tarifa. Sin cuota mínima mensual: si un mes vende menos, paga menos.</p></div>
      <div class="card">{icon("clock")}<h3>Liquidación en dólares</h3><p>Las transacciones se liquidan en dólares estadounidenses, con estado de cuenta por turno y por bomba para que su contador y su cajero cuadren sin sorpresas.</p></div>
      <div class="card">{icon("shield")}<h3>Menos efectivo, menos riesgo</h3><p>Más ventas con tarjeta significan menos efectivo en caja durante el turno de la noche, menos faltantes y menos exposición para su personal.</p></div>
    </div>
  </div>
</section>

<section class="alt">
  <div class="wrap split">
    <figure><picture><source srcset="/assets/img/pos-tap.webp" type="image/webp" /><img src="/assets/img/pos-tap.jpg" alt="Cliente pagando sin contacto en una terminal inalámbrica junto a una bomba de combustible" loading="lazy" width="1280" height="720" /></picture><figcaption>Imagen ilustrativa.</figcaption></figure>
    <div>
      <span class="eyebrow">Cómo funciona</span>
      <h2>Tres pasos para empezar a cobrar.</h2>
      <ol class="timeline">
        <li><strong>Regístrese en línea.</strong> Cinco minutos. Le pedimos los datos de la estación, su resolución del MICM y su RNC.</li>
        <li><strong>Aprobación e instalación.</strong> El banco patrocinador aprueba el expediente; nuestro equipo instala las terminales y capacita a su personal en el patio.</li>
        <li><strong>Cobre y reciba.</strong> Chip, sin contacto y billeteras móviles. Las transacciones se liquidan en dólares a la cuenta que usted indique.</li>
      </ol>
      <a class="btn btn-navy" href="/como-funciona/">Ver todos los detalles</a>
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">Zona de lanzamiento</span>
      <h2>Empezamos en el Polígono Central de Santo Domingo.</h2>
      <p>Las primeras instalaciones se hacen en las {st['n']} estaciones dentro y alrededor del Polígono Central (Av. Kennedy, 27 de Febrero, Churchill y Máximo Gómez). ¿Su estación aparece en el mapa? Regístrela y le damos prioridad en la primera ola. ¿Está en otra zona? Regístrese igual: abrimos por sectores según la demanda.</p>
    </div>
    <div class="map-wrap">
      <div id="map" class="compact" role="region" aria-label="Mapa de la zona de lanzamiento en el Polígono Central"></div>
      <div class="map-legend"><span><i class="dot inside"></i> Dentro del Polígono Central ({st['inside']})</span><span><i class="dot edge"></i> Borde / adyacente ({st['edge']})</span><span><i class="poly-key"></i> Límite aproximado</span></div>
    </div>
    <p class="mt-2"><a href="/zona/">Ver la lista completa de la zona de lanzamiento</a></p>
  </div>
</section>

<section class="alt">
  <div class="wrap">
    <div class="section-head"><span class="eyebrow">Lo que incluye</span><h2>Todo lo que necesita una estación, nada de lo que no.</h2></div>
    <div class="grid grid-3">
      <div class="card">{icon("card")}<h3>Terminales para el patio</h3><p>Inalámbricas, resistentes, con chip y sin contacto, impresión de recibo y menús en español. Integración con el controlador de surtidores cuando su equipo lo permite.</p></div>
      <div class="card">{icon("chart")}<h3>Panel del propietario</h3><p>Ventas por bomba, turno y producto; mezcla de tarjetas; contracargos; estados de cuenta descargables para su contador y para la DGII.</p></div>
      <div class="card">{icon("doc")}<h3>Estados de cuenta claros</h3><p>Verá el intercambio, la tarifa de la red y nuestra tarifa por separado. Alquiler mensual de la terminal y ningún otro cargo fijo.</p></div>
      <div class="card">{icon("shield")}<h3>Protección contra fraude</h3><p>Límites por bomba y por tarjeta, cumplimiento EMV y una mesa de disputas que trabaja los contracargos en nombre de la estación.</p></div>
      <div class="card">{icon("map")}<h3>Soporte en la calle</h3><p>Técnicos en Santo Domingo, en español, con reposición de terminal en horas, no en semanas.</p></div>
      <div class="card">{icon("bank")}<h3>Respaldo bancario</h3><p>Los fondos se liquidan a través de un banco patrocinador autorizado y las reglas de Visa y Mastercard. Bombero Partners no retiene su dinero.</p></div>
    </div>
  </div>
</section>

<section class="dark">
  <div class="wrap">
    <div class="section-head"><span class="eyebrow">Primera ola</span><h2>Reserve su lugar en la primera ola de instalaciones.</h2><p>Registrarse no le compromete a nada. Le contactamos, revisamos juntos su volumen y le presentamos la propuesta con números para su estación.</p></div>
    <div class="hero-actions"><a class="btn btn-primary" href="/afiliese/">Afilie su estación</a><a class="btn btn-ghost" href="/preguntas/">Preguntas frecuentes</a></div>
  </div>
</section>
"""
