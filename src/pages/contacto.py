def body(ctx):
    email = ctx["CONTACT_EMAIL"]
    return f"""
<div class="page-title"><div class="wrap"><span class="eyebrow">Contacto</span><h1>Hablemos.</h1><p>Para estaciones, bancos, aliados tecnológicos y prensa. Respondemos en un día hábil, en español o en inglés.</p></div></div>
<section><div class="wrap grid grid-2">
  <div>
    <form class="contact" method="post" action="/api/contact" novalidate>
      <input type="hidden" name="type" value="contacto" />
      <label>Nombre <input name="name" type="text" required autocomplete="name" /></label>
      <label>Empresa u organización <input name="org" type="text" autocomplete="organization" /></label>
      <label>Correo electrónico <input name="email" type="email" required autocomplete="email" /></label>
      <label>Le escribo como <select name="role" id="role"><option value="estacion">Propietario u operador de estación</option><option value="banco">Banco o entidad financiera</option><option value="aliado">Aliado tecnológico o de pagos</option><option value="prensa">Prensa</option><option value="otro">Otro</option></select></label>
      <label>Mensaje <textarea name="message" required></textarea></label>
      <label class="hp" aria-hidden="true">Website <input name="website" type="text" tabindex="-1" autocomplete="off" /></label>
      <button class="btn btn-navy" type="submit">Enviar</button>
      <p class="form-status" role="status" aria-live="polite"></p>
      <p class="form-note">Al enviar acepta nuestra <a href="/legal/privacidad/">política de privacidad</a>.</p>
    </form>
  </div>
  <div>
    <div class="card"><h3>Directo</h3><p><a href="mailto:{email}">{email}</a></p><p class="small muted">Para reportes de seguridad, vea <a href="/.well-known/security.txt">security.txt</a>.</p></div>
    <div class="card mt-2"><h3>Estaciones</h3><p>Si quiere una propuesta con números, use el <a href="/afiliese/">formulario de afiliación</a>: le pedimos los datos que necesitamos para calcular su tarifa.</p></div>
    <div class="card mt-2"><h3>Bancos y aliados</h3><p>Seleccione "Banco o entidad financiera" y le enviamos la presentación completa tras un acuerdo de confidencialidad. <a href="/en/" lang="en">Information in English</a>.</p></div>
  </div>
</div></section>
"""
