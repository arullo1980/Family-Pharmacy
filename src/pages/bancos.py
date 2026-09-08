from common import stat_tiles, icon

def body(ctx):
    st = ctx["stats"]
    return f"""
<div class="page-title"><div class="wrap"><span class="eyebrow">Bancos y aliados</span><h1>Un programa vertical de adquirencia para combustibles, operado bajo su patrocinio.</h1><p>Wallet Partners LLC busca un banco patrocinador, miembro de Visa y Mastercard en la República Dominicana, para lanzar un programa de facilitación de pagos dedicado a estaciones de combustible, con compensación en dólares estadounidenses. Esta página resume el programa; la presentación completa se comparte bajo acuerdo de confidencialidad.</p><div class="meta-line"><a href="/en/banks/" lang="en">Read this page in English</a></div></div></div>

<section><div class="wrap">
  {stat_tiles([
    ("≈1,025", "estaciones en el país", "estimación de ANADEGAS, 2026"),
    ("RD$41 mil MM", "pagos con tarjeta en estaciones al año", "Diario Libre, jul 2026"),
    ("1.95–2.50%", "comisión actual por transacción", "25–36% del margen bruto por galón"),
    (str(st["n"]), "estaciones en la zona de lanzamiento", "Polígono Central, Santo Domingo"),
  ])}
</div></section>

<section class="alt"><div class="wrap">
  <div class="section-head"><span class="eyebrow">Por qué ahora</span><h2>El segmento pidió públicamente otro modelo de precios.</h2><p>En junio y julio de 2026 la asociación de detallistas de combustible amenazó con retirar los verifones de más de 780 estaciones por comisiones porcentuales que consumen entre la cuarta y la tercera parte de un margen regulado. El Gobierno abrió un diálogo con la banca. Un programa con una comisión 25 puntos básicos por debajo del contrato vigente de cada estación, sin mínimo mensual, compensación en dólares, intercambio transparente y controles de nivel bancario ofrece al banco patrocinador una vía defendible para crecer en un segmento de alto volumen mientras los adquirentes tradicionales negocian.</p></div>
  <div class="grid grid-3">
    <div class="card">{icon("bank")}<h3>Lo que hace el banco</h3><p>Membresía de las redes y BIN, aprobación de cada comercio, cuenta de liquidación del programa con reservas, supervisión de segunda línea y reporte regulatorio.</p></div>
    <div class="card">{icon("pump")}<h3>Lo que hace Bombero Partners</h3><p>Prospección y afiliación, expedientes KYB/KYC listos para revisión, terminales y soporte de campo, monitoreo de primera línea, disputas, liquidación a comercios y reporte al banco.</p></div>
    <div class="card">{icon("shield")}<h3>Marco de cumplimiento</h3><p>PCI DSS con terminales P2PE, Ley 155-17 (PLA/FT), Ley 172-13 (datos), reglas de Visa y Mastercard para facilitadores de pago, MCC 5541/5542. <a href="/legal/cumplimiento/">Ver el marco completo</a>.</p></div>
  </div>
</div></section>

<section><div class="wrap split">
  <div>
    <span class="eyebrow">Lo que pedimos</span>
    <h2>Un acuerdo de patrocinio y un expediente a la vez.</h2>
    <ul class="checklist">
      <li>Membresía adquirente de Visa y Mastercard en RD, o corresponsalía que permita patrocinar el programa.</li>
      <li>Registro de Bombero Partners como facilitador de pagos / administrador del programa.</li>
      <li>Cuenta de liquidación del programa con reservas y reglas de liberación acordadas.</li>
      <li>Aprobación de comercios en diez días hábiles por expediente.</li>
      <li>Un contacto de relación y uno de cumplimiento.</li>
    </ul>
  </div>
  <div class="card"><h3>La presentación para bancos incluye</h3><ul class="checklist"><li>Resumen ejecutivo y cronología del conflicto de comisiones de 2026</li><li>Datos del sistema de pagos del Banco Central y del mercado de combustibles</li><li>Mapa y lista de las {st['n']} estaciones de la zona de lanzamiento</li><li>Diseño del programa, matriz de responsabilidades y plan de despliegue</li><li>Modelo de escenarios de volumen e ingresos</li><li>Marco de cumplimiento y lista de documentos disponibles</li></ul><a class="btn btn-navy" href="/contacto/?tipo=banco">Solicitar la presentación</a></div>
</div></section>
"""
