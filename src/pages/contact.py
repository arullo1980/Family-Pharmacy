def body(ctx):
    email = ctx["CONTACT_EMAIL"]
    return f"""
<div class="page-title"><div class="wrap">
  <span class="eyebrow">Contact</span>
  <h1>Let's talk about sponsorship.</h1>
  <p>For sponsoring banks, acquiring partners, station owners and press. We reply within one business day.</p>
</div></div>

<section>
  <div class="wrap grid grid-2">
    <div>
      <form class="contact" method="post" action="/api/contact" novalidate>
        <label>Name <input name="name" type="text" required autocomplete="name" /></label>
        <label>Organisation <input name="org" type="text" autocomplete="organization" /></label>
        <label>Email <input name="email" type="email" required autocomplete="email" /></label>
        <label>I am contacting you as <select name="role"><option>Bank / financial institution</option><option>Payments or technology partner</option><option>Gasoline station owner or operator</option><option>Press</option><option>Other</option></select></label>
        <label>Message <textarea name="message" required></textarea></label>
        <label class="hp" aria-hidden="true">Website <input name="website" type="text" tabindex="-1" autocomplete="off" /></label>
        <button class="btn btn-navy" type="submit">Send message</button>
        <p class="form-status" role="status" aria-live="polite"></p>
        <p class="form-note">By sending this form you agree to our <a href="/legal/privacy/">privacy policy</a>. We use your details only to respond to your enquiry.</p>
      </form>
    </div>
    <div>
      <div class="card"><h3>Direct</h3><p><a href="mailto:{email}">{email}</a></p><p class="small muted">For security disclosures see <a href="/.well-known/security.txt">security.txt</a>.</p></div>
      <div class="card mt-2"><h3>What to expect</h3><ul class="checklist"><li>A reply within one business day.</li><li>An NDA before we share merchant files or pricing.</li><li>A working session with your merchant-acquiring and compliance teams, in English or Spanish.</li></ul></div>
      <div class="card mt-2"><h3>Station owners</h3><p>¿Es propietario de una estación en el Distrito Nacional? Escríbanos y le explicamos el programa y la lista de documentos para la afiliación.</p></div>
    </div>
  </div>
</section>
"""
