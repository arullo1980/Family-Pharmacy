/**
 * Cloudflare Pages Function: POST /api/contact
 * Accepts the contact and sign-up forms, validates them, and forwards each by email
 * through Resend when RESEND_API_KEY is configured as a Pages secret. Optional:
 * CONTACT_TO (default info@walletpartnersllc.com) and CONTACT_FROM (default Resend's
 * onboarding sender; set to an address on a domain verified in Resend for production).
 * Without the key it returns 503 so the front end falls back to mailto.
 */
export async function onRequestPost(context) {
  const { request, env } = context;
  let body;
  try { body = await request.json(); } catch (e) { return json({ error: 'Invalid JSON' }, 400); }

  const name = clean(body.name, 120);
  const org = clean(body.org, 160);
  const email = clean(body.email, 200);
  const message = clean(body.message, 4000);
  if (body.website) return json({ ok: true }); // honeypot filled by a bot: pretend success
  if (!name || !email || !/^[^@\s]+@[^@\s]+\.[^@\s]+$/.test(email) || (!message && body.type !== 'estacion')) {
    return json({ error: 'Name, a valid email and a message are required.' }, 422);
  }
  if (!env.RESEND_API_KEY) {
    return json({ error: 'Contact endpoint not configured' }, 503);
  }
  const to = env.CONTACT_TO || 'info@walletpartnersllc.com';
  // Until bomberopartners.com.do is verified in Resend, its onboarding sender can deliver
  // only to the Resend account owner's own address (which is why CONTACT_TO defaults to it).
  const from = env.CONTACT_FROM || 'Bombero Partners <onboarding@resend.dev>';
  const res = await fetch('https://api.resend.com/emails', {
    method: 'POST',
    headers: { 'Authorization': `Bearer ${env.RESEND_API_KEY}`, 'Content-Type': 'application/json' },
    body: JSON.stringify({
      from,
      to: [to],
      reply_to: email,
      subject: `${body.type === 'estacion' ? 'Afiliación de estación' : 'Consulta web'}: ${org || name}`,
      text: Object.keys(body).filter(k => k !== 'website' && body[k]).map(k => `${k}: ${clean(String(body[k]), 4000)}`).join('\n') + `\n\nIP country: ${request.cf && request.cf.country}`
    })
  });
  if (!res.ok) return json({ error: 'Mail provider rejected the message' }, 502);
  return json({ ok: true });
}

export async function onRequest(context) {
  if (context.request.method === 'POST') return onRequestPost(context);
  return json({ error: 'Method not allowed' }, 405);
}

function clean(v, max) { return typeof v === 'string' ? v.trim().slice(0, max) : ''; }
function json(obj, status = 200) {
  return new Response(JSON.stringify(obj), { status, headers: { 'Content-Type': 'application/json', 'Cache-Control': 'no-store' } });
}
