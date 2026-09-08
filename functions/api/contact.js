/**
 * Cloudflare Pages Function: POST /api/contact
 * Accepts the contact form, validates it, and forwards it by email through Resend
 * when RESEND_API_KEY and CONTACT_TO are configured as Pages environment variables.
 * Without those variables it returns 503 so the front end can fall back to mailto.
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
  if (!name || !email || !message || !/^[^@\s]+@[^@\s]+\.[^@\s]+$/.test(email)) {
    return json({ error: 'Name, a valid email and a message are required.' }, 422);
  }
  if (!env.RESEND_API_KEY || !env.CONTACT_TO) {
    return json({ error: 'Contact endpoint not configured' }, 503);
  }
  const res = await fetch('https://api.resend.com/emails', {
    method: 'POST',
    headers: { 'Authorization': `Bearer ${env.RESEND_API_KEY}`, 'Content-Type': 'application/json' },
    body: JSON.stringify({
      from: env.CONTACT_FROM || 'Wallet Partners Website <noreply@walletpartnersllc.com>',
      to: [env.CONTACT_TO],
      reply_to: email,
      subject: `Website inquiry from ${name}${org ? ' (' + org + ')' : ''}`,
      text: `Name: ${name}\nOrganization: ${org}\nEmail: ${email}\nIP country: ${request.cf && request.cf.country}\n\n${message}`
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
