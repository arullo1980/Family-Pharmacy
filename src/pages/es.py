from common import stat_tiles

def body(ctx):
    st = ctx["stats"]
    return f"""
<div class="page-title"><div class="wrap">
  <span class="eyebrow">Resumen ejecutivo</span>
  <h1>Adquirencia diseñada para estaciones de combustible.</h1>
  <p>Wallet Partners LLC lanza un programa de aceptación de tarjetas y comercio registrado (merchant of record) dedicado a las estaciones de gasolina de la República Dominicana. Veinte estaciones del Polígono Central de Santo Domingo están listas para afiliarse en cuanto contemos con el banco patrocinador.</p>
  <div class="meta-line"><a href="/">English version</a></div>
</div></div>

<section><div class="wrap">
{stat_tiles([
  (str(st["n"]), "estaciones en cartera", "Polígono Central, Santo Domingo"),
  (str(st["h24"]), "abiertas 24 horas", f"{round(100*st['h24']/st['n'])}% de la cartera"),
  ("1.95–2.50%", "comisión actual por transacción", "ANADEGAS, 2026"),
  ("RD$41 mil MM", "pagos con tarjeta en estaciones al año", "Diario Libre, jul 2026"),
])}
</div></section>

<section class="alt"><div class="wrap prose">
<h2>La oportunidad</h2>
<p>A finales de junio de 2026 la Asociación Nacional de Detallistas de Gasolina (ANADEGAS) anunció el retiro de los verifones en más de 780 estaciones afiliadas, en protesta por comisiones de entre 1.95% y 2.50% por transacción. Con un margen bruto regulado de unos RD$25 por galón, la comisión equivale a RD$6.59–8.45 por galón, es decir, entre 25% y 36% de lo que retiene la estación. El Gobierno abrió un plazo de diálogo de 30 días y el gremio propuso una tarifa fija por galón o un esquema basado en el margen, en lugar de un porcentaje.</p>
<p>Los pagos con tarjeta en estaciones suman alrededor de RD$41 mil millones al año y las comisiones cobradas por las procesadoras rondan RD$584 millones mensuales. Hay unas 1,025 estaciones en el país y tres adquirentes: CardNET, AZUL y Visanet. Ninguno ofrece un producto pensado para el galón.</p>

<h2>Nuestra propuesta</h2>
<ul class="checklist">
<li><strong>Precio por galón.</strong> Tarifa expresada en pesos por galón con tope, con estados de cuenta tipo interchange-plus que el propietario puede verificar contra el aviso semanal del MICM.</li>
<li><strong>Liquidación al día siguiente en pesos</strong>, por estación y por turno.</li>
<li><strong>Terminales EMV y sin contacto</strong> aptas para el patio de bombas, con preautorización y cierre, e integración con controladores de surtidores cuando el equipo lo permita.</li>
<li><strong>Cumplimiento desde el primer día:</strong> PCI DSS, Ley 155-17 (PLA/FT), Ley 172-13 (datos personales), reglas de las redes de tarjetas y supervisión del banco patrocinador. <a href="/legal/compliance/">Ver el marco de cumplimiento</a>.</li>
<li><strong>Soporte local</strong> en Santo Domingo, en español.</li>
</ul>

<h2>La cartera inicial</h2>
<p>Las {st['n']} estaciones están dentro o en el borde del Polígono Central (Av. John F. Kennedy, Av. 27 de Febrero, Av. Winston Churchill y Av. Máximo Gómez): {st['inside']} dentro del polígono y {st['edge']} adyacentes; {st['h24']} operan 24 horas; {len(st['brands'])} marcas, encabezadas por TotalEnergies con {st['brands'].get('TotalEnergies', 0)} estaciones. Todas quedan a menos de {st['maxDist']:.1f} km del centro de referencia. <a href="/stations/">Ver el mapa interactivo y el directorio</a>.</p>

<h2>Lo que pedimos a un banco patrocinador</h2>
<ul class="checklist">
<li>Membresía adquirente de Visa y Mastercard en la República Dominicana, o un acuerdo de corresponsalía que permita patrocinar el programa.</li>
<li>Registro de Wallet Partners como facilitador de pagos / administrador del programa.</li>
<li>Cuenta de liquidación del programa con reservas y reglas de liberación acordadas.</li>
<li>Aprobación de comercios en un plazo de diez días hábiles por expediente.</li>
</ul>
<p><a class="btn btn-navy" href="/contact/">Solicitar el paquete para bancos patrocinadores</a></p>
<p class="small muted">Wallet Partners LLC no es un banco. Los servicios de aceptación de tarjetas se prestarán bajo el patrocinio de una entidad financiera miembro autorizada. Las cifras de mercado se citan de fuentes públicas indicadas en la <a href="/market/">página de mercado</a>.</p>
</div></section>
"""
