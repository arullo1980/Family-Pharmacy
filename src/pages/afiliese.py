def body(ctx):
    return """
<div class="page-title"><div class="wrap"><span class="eyebrow">Afiliación</span><h1>Registre su estación.</h1><p>Cinco minutos. No le compromete a nada: le contactamos en un día hábil, revisamos su volumen y le enviamos una propuesta por escrito: 0.25% por debajo de su contrato actual, sin mínimo mensual, alquiler mensual de terminal y liquidación en dólares.</p></div></div>
<section><div class="wrap grid grid-2">
  <div>
    <form class="contact" method="post" action="/api/contact" novalidate>
      <input type="hidden" name="type" value="estacion" />
      <label>Nombre de la estación <input name="org" type="text" required autocomplete="organization" /></label>
      <label>Dirección y ciudad <input name="address" type="text" required autocomplete="street-address" /></label>
      <label>Nombre del propietario o gerente <input name="name" type="text" required autocomplete="name" /></label>
      <label>Teléfono o WhatsApp <input name="phone" type="tel" required autocomplete="tel" /></label>
      <label>Correo electrónico <input name="email" type="email" required autocomplete="email" /></label>
      <label>Galones vendidos al mes (aprox.) <input name="gallons" type="number" min="0" step="1000" /></label>
      <label>Ventas con tarjeta hoy (%) <input name="cardshare" type="number" min="0" max="100" /></label>
      <label>¿Con quién procesa tarjetas hoy? <select name="processor"><option>No acepto tarjetas</option><option>CardNET</option><option>AZUL</option><option>Visanet</option><option>Otro</option></select></label>
      <label>Comentarios <textarea name="message"></textarea></label>
      <label class="hp" aria-hidden="true">Website <input name="website" type="text" tabindex="-1" autocomplete="off" /></label>
      <button class="btn btn-navy" type="submit">Enviar solicitud</button>
      <p class="form-status" role="status" aria-live="polite"></p>
      <p class="form-note">Al enviar acepta nuestra <a href="/legal/privacidad/">política de privacidad</a>. Usamos sus datos solo para responder a su solicitud y preparar la propuesta.</p>
    </form>
  </div>
  <div>
    <div class="card"><h3>Qué pasa después</h3><ol class="timeline"><li><strong>Día 1.</strong> Un asesor le llama, confirma su volumen y responde sus preguntas.</li><li><strong>Días 2–5.</strong> Recibe la propuesta por escrito con su tarifa (contrato actual − 0.25%) y el alquiler de la terminal.</li><li><strong>Días 5–15.</strong> Reunimos los documentos y el banco patrocinador aprueba el expediente.</li><li><strong>Instalación.</strong> Programamos la instalación y la capacitación en su patio.</li></ol></div>
    <div class="card mt-2"><h3>Tenga a mano</h3><ul class="checklist"><li>Resolución del MICM</li><li>RNC y registro mercantil</li><li>Cédulas de los socios y del representante</li><li>Certificación de cuenta bancaria</li><li>Su contrato o estado de cuenta de procesamiento actual</li></ul></div>
  </div>
</div></section>
"""
