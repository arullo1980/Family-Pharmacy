def body(ctx):
    return """
<div class="page-title"><div class="wrap"><span class="eyebrow">Precios</span><h1>0.25% menos que su contrato actual. Sin mínimo mensual.</h1><p>Cuatro condiciones, sin letra pequeña. La tarifa definitiva se fija en el contrato de afiliación aprobado por el banco patrocinador, a partir de la tarifa que usted paga hoy.</p></div></div>

<section><div class="wrap">
  <div class="grid grid-2">
    <div class="card"><h3>1. 25 puntos básicos menos</h3><p>Su comisión será 0.25 puntos porcentuales más baja que la de su contrato de procesamiento actual. Si hoy paga 2.25%, con nosotros paga 2.00%.</p></div>
    <div class="card"><h3>2. Sin mínimo mensual</h3><p>No hay cuota mínima de facturación. Paga solo por las transacciones que procesa.</p></div>
    <div class="card"><h3>3. Terminal en alquiler mensual</h3><p>La terminal se entrega en alquiler con una cuota mensual fija que incluye reposición y soporte. No hay compra de equipo.</p></div>
    <div class="card"><h3>4. Liquidación en dólares</h3><p>Las transacciones se liquidan en dólares estadounidenses a la cuenta que usted indique.</p></div>
  </div>
  <div class="callout mt-3"><p><strong>Transparencia.</strong> El estado de cuenta muestra por separado el intercambio (lo que cobra el banco emisor), la tarifa de la red y nuestra tarifa, para que pueda comparar con su contrato actual línea por línea.</p></div>
</div></section>

<section class="alt"><div class="wrap">
  <div class="section-head"><span class="eyebrow">Calculadora</span><h2>¿Cuánto ahorra con 25 puntos básicos menos?</h2><p>Escriba sus galones mensuales, el porcentaje de ventas con tarjeta y la comisión que le cobran hoy. La calculadora muestra lo que paga hoy, lo que pagaría con nuestra tarifa y el ahorro anual. Es una estimación con sus propios datos, no una cotización.</p></div>
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
      <div class="row"><span>Con Wallet Partners (−0.25%) al mes</span><b id="p-o-nueva"></b></div>
      <div class="row"><span>Ahorro al año</span><b id="p-o-ahorro"></b></div>
    </div>
  </div>
  <p class="mt-3"><a class="btn btn-navy" href="/afiliese/">Pida una propuesta con su tarifa exacta</a></p>
</div></section>

<section><div class="wrap prose">
  <h2>Preguntas sobre precios</h2>
  <h3>¿Cuál es la tarifa exacta?</h3><p>Su tarifa actual menos 0.25 puntos porcentuales. Para cotizarla necesitamos ver su contrato o estado de cuenta actual; se la presentamos por escrito antes de que firme nada.</p><h3>¿Cuánto cuesta la terminal?</h3><p>Se entrega en alquiler con una cuota mensual fija que incluye soporte y reposición. El monto se indica en la propuesta.</p><h3>¿Por qué en dólares?</h3><p>El programa se liquida a través de un banco patrocinador que compensa en dólares estadounidenses. Los fondos llegan en USD a la cuenta que usted designe.</p>
  <h3>¿Qué es el intercambio?</h3><p>Es la parte de la comisión que se queda el banco que emitió la tarjeta del cliente, fijada por Visa y Mastercard. Se lo mostramos por separado para que sepa exactamente qué parte del costo es nuestra.</p>
  <h3>¿Hay cargos por contracargo?</h3><p>Solo cuando un contracargo se pierde. Nuestra mesa de disputas trabaja cada caso con el recibo y la evidencia de la terminal.</p>
  <h3>¿Retención de impuestos?</h3><p>Aplicamos las retenciones que exija la DGII para pagos con tarjeta en su categoría y se lo detallamos en cada estado de cuenta. Confírmelo con su contador; con gusto le explicamos el tratamiento.</p>
</div></section>
"""
