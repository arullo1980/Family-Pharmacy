from common import icon

def body(ctx):
    return f"""
<div class="page-title"><div class="wrap"><span class="eyebrow">Cómo funciona</span><h1>De la bomba a su cuenta, sin sorpresas.</h1><p>Así funciona el programa de aceptación de tarjetas de Bombero Partners para estaciones de combustible, desde el registro hasta la liquidación.</p></div></div>

<section><div class="wrap">
  <div class="section-head"><h2>Cada transacción, paso a paso</h2></div>
  <ol class="timeline">
    <li><strong>El cliente paga en el patio.</strong> El bombero digita el monto o el controlador de surtidores lo envía a la terminal inalámbrica. Se aceptan chip, sin contacto y billeteras móviles; la banda magnética está desactivada por política.</li>
    <li><strong>Autorización.</strong> La terminal envía la transacción, cifrada de punto a punto, a la plataforma del banco patrocinador, que la enruta a Visa, Mastercard o la red de débito local.</li>
    <li><strong>Liquidación.</strong> El banco recibe los fondos de las redes y las transacciones se liquidan en dólares estadounidenses a la cuenta que usted indique, descontando la comisión acordada (0.25% por debajo de su contrato actual).</li>
    <li><strong>Conciliación.</strong> Recibe un estado de cuenta por turno y por bomba, con el intercambio, la tarifa de la red y nuestra tarifa por separado.</li>
    <li><strong>Disputas.</strong> Si un cliente reclama, nuestra mesa de disputas arma el caso con el recibo y la evidencia de la terminal y lo defiende ante la red.</li>
  </ol>
</div></section>

<section class="alt"><div class="wrap">
  <div class="section-head"><span class="eyebrow">Afiliación</span><h2>Lo que necesitamos para afiliar su estación</h2><p>El banco patrocinador revisa cada expediente. Con estos documentos la aprobación normalmente toma menos de diez días hábiles.</p></div>
  <div class="grid grid-2">
    <div class="card"><h3>Documentos de la estación</h3><ul class="checklist"><li>Resolución de operación vigente del MICM</li><li>RNC y registro mercantil</li><li>Documentos constitutivos de la empresa</li><li>Comprobante de dirección y fotos del establecimiento</li></ul></div>
    <div class="card"><h3>Documentos de los propietarios</h3><ul class="checklist"><li>Cédula o pasaporte de los socios con 10% o más</li><li>Cédula del representante legal</li><li>Certificación de la cuenta bancaria donde recibirá la liquidación</li><li>Volumen mensual estimado y ticket promedio</li></ul></div>
  </div>
  <div class="callout info mt-3"><p><strong>¿Tiene contrato con otro procesador?</strong> Revíselo con nosotros. En la mayoría de los casos puede mantener su cuenta bancaria actual y solo cambia quién procesa las tarjetas.</p></div>
</div></section>

<section><div class="wrap">
  <div class="section-head"><span class="eyebrow">Equipo</span><h2>Terminales pensadas para el patio de bombas</h2></div>
  <div class="grid grid-3">
    <div class="card">{icon("card")}<h3>Inalámbricas y resistentes</h3><p>Batería para todo el turno, conexión 4G y wifi, resistentes al polvo y a la lluvia ligera.</p></div>
    <div class="card">{icon("pump")}<h3>Flujo de combustible</h3><p>Preautorización y cierre para bombas automáticas, propina desactivada, recibo impreso y menús en español.</p></div>
    <div class="card">{icon("chart")}<h3>Integración</h3><p>Conexión con el controlador de surtidores cuando el equipo de la estación lo permite, para evitar digitar montos.</p></div>
  </div>
</div></section>

<section class="dark"><div class="wrap"><div class="section-head"><h2>¿Listo para empezar?</h2><p>Registre su estación y un asesor le contacta en un día hábil.</p></div><a class="btn btn-primary" href="/afiliese/">Afilie su estación</a></div></section>
"""
