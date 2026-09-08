def body(ctx):
    return """
<div class="page-title"><div class="wrap"><span class="eyebrow">Precios</span><h1>Una tarifa por galón. Un tope. Todo a la vista.</h1><p>Cobramos en pesos por galón vendido con tarjeta, no un porcentaje de la venta. La tarifa definitiva depende del volumen de su estación y se fija en el contrato de afiliación aprobado por el banco patrocinador.</p></div></div>

<section><div class="wrap">
  <div class="grid grid-3">
    <div class="card"><h3>Tarifa por galón</h3><p>Una cantidad fija en pesos por cada galón pagado con tarjeta. Sube el combustible, no sube su tarifa.</p></div>
    <div class="card"><h3>Tope efectivo</h3><p>La tarifa nunca supera un porcentaje máximo de la venta, para que en los productos de menor precio tampoco pague de más.</p></div>
    <div class="card"><h3>Intercambio transparente</h3><p>El estado de cuenta muestra por separado el intercambio (lo que cobra el banco emisor), la tarifa de la red y nuestra tarifa.</p></div>
  </div>
  <div class="callout mt-3"><p><strong>Sin letra pequeña.</strong> Sin cargo por terminal en la primera ola, sin cuota mensual mínima, sin cargo por estado de cuenta. Si cancela, devuelve la terminal y listo.</p></div>
</div></section>

<section class="alt"><div class="wrap">
  <div class="section-head"><span class="eyebrow">Calculadora</span><h2>¿Cuánto paga hoy en comisiones por galón?</h2><p>Escriba sus galones mensuales, el porcentaje de ventas con tarjeta y la comisión que le cobran hoy. La calculadora muestra cuánto se convierte eso en pesos por galón y qué parte de su margen representa. Es una estimación con sus propios datos, no una cotización.</p></div>
  <div class="calc" id="calc-precios">
    <div>
      <div class="field"><label for="p-gal">Galones vendidos al mes</label><input id="p-gal" type="number" min="0" step="1000" value="120000" /></div>
      <div class="field"><label for="p-precio">Precio promedio por galón (RD$)</label><input id="p-precio" type="number" min="0" step="0.1" value="281" /></div>
      <div class="field"><label for="p-tarjeta">Ventas pagadas con tarjeta (%)</label><input id="p-tarjeta" type="number" min="0" max="100" step="1" value="40" /></div>
      <div class="field"><label for="p-com">Comisión que paga hoy (%)</label><input id="p-com" type="number" min="0" step="0.05" value="2.25" /></div>
      <div class="field"><label for="p-margen">Margen bruto por galón (RD$)</label><input id="p-margen" type="number" min="0" step="0.5" value="25" /></div>
      <p class="small muted">Valores iniciales: precio promedio entre gasolina premium (RD$290.10) y regular (RD$272.50) según los avisos del MICM en 2025; comisión y margen según cifras publicadas por ANADEGAS en 2026. Cámbielos por los de su estación.</p>
    </div>
    <div class="out">
      <h3>Con sus datos</h3>
      <div class="row"><span>Ventas con tarjeta al mes</span><b id="p-o-ventas"></b></div>
      <div class="row"><span>Comisión que paga al mes</span><b id="p-o-com"></b></div>
      <div class="row"><span>Comisión por galón vendido con tarjeta</span><b id="p-o-porgal"></b></div>
      <div class="row"><span>Parte de su margen que se va en comisión</span><b id="p-o-margen"></b></div>
      <div class="row"><span>Comisión al año</span><b id="p-o-anual"></b></div>
    </div>
  </div>
  <p class="mt-3"><a class="btn btn-navy" href="/afiliese/">Pida una propuesta con la tarifa por galón para su estación</a></p>
</div></section>

<section><div class="wrap prose">
  <h2>Preguntas sobre precios</h2>
  <h3>¿Cuál es la tarifa exacta?</h3><p>Depende del volumen de la estación y de la mezcla de tarjetas (débito local, crédito nacional, tarjetas internacionales). Se la presentamos por escrito después de revisar sus datos, antes de que firme nada.</p>
  <h3>¿Qué es el intercambio?</h3><p>Es la parte de la comisión que se queda el banco que emitió la tarjeta del cliente, fijada por Visa y Mastercard. Se lo mostramos por separado para que sepa exactamente qué parte del costo es nuestra.</p>
  <h3>¿Hay cargos por contracargo?</h3><p>Solo cuando un contracargo se pierde. Nuestra mesa de disputas trabaja cada caso con el recibo y la evidencia de la terminal.</p>
  <h3>¿Retención de impuestos?</h3><p>Aplicamos las retenciones que exija la DGII para pagos con tarjeta en su categoría y se lo detallamos en cada estado de cuenta. Confírmelo con su contador; con gusto le explicamos el tratamiento.</p>
</div></section>
"""
