/* Sponsor-bank presentation for Wallet Partners LLC — generated with pptxgenjs.
   Run: node deck/build_deck.js  (writes deck/Wallet-Partners-Sponsor-Bank-Deck.pptx) */
const pptxgen = require('pptxgenjs');
const fs = require('fs');
const path = require('path');

const ROOT = path.resolve(__dirname, '..');
const data = JSON.parse(fs.readFileSync(path.join(ROOT, 'site/data/stations.json'), 'utf8'));
const S = data.stations;
const inside = S.filter(s => s.inside).length, h24 = S.filter(s => s.open24h).length;

// Palette: navy dominant, amber accent, blue/orange for data
const C = { navy: '0F2440', navy2: '163558', amber: 'EDA100', amberD: 'B97C00', blue: '2A78D6', orange: 'EB6834',
  ink: '16202B', ink2: '4A5563', ink3: '6B7683', line: 'DDE3EA', bg: 'F4F6F9', white: 'FFFFFF', aqua: '1BAF7A' };
const FONT = 'Calibri';

// Icons (react-icons -> SVG -> PNG via sharp); falls back to a plain circle if unavailable
let icons = null;
try {
  const React = require('react'); const RD = require('react-dom/server'); const sharp = require('sharp');
  const fa = require('react-icons/fa');
  icons = async (name, color) => {
    const svg = RD.renderToStaticMarkup(React.createElement(fa[name], { color: '#' + color, size: 256 }));
    const buf = await sharp(Buffer.from(svg)).png().toBuffer();
    return 'image/png;base64,' + buf.toString('base64');
  };
} catch (e) { console.log('icons unavailable:', e.message.split('\n')[0]); }

const pres = new pptxgen();
pres.layout = 'LAYOUT_WIDE'; // 13.33 x 7.5
pres.author = 'Wallet Partners LLC'; pres.company = 'Wallet Partners LLC';
pres.title = 'Wallet Partners LLC — Fuel-retail acquiring program, Dominican Republic';
const W = 13.33, H = 7.5, M = 0.6;
let n = 0;

function base(dark = false) {
  const s = pres.addSlide(); n++;
  s.background = { color: dark ? C.navy : C.white };
  if (!dark) {
    s.addText('Wallet Partners LLC · Sponsor-bank briefing · September 2026 · Confidential', { x: M, y: H - 0.45, w: 8, h: 0.3, fontFace: FONT, fontSize: 9, color: C.ink3, isTextBox: true, margin: 0 });
    s.addText(String(n), { x: W - M - 0.6, y: H - 0.45, w: 0.6, h: 0.3, fontFace: FONT, fontSize: 9, color: C.ink3, align: 'right', isTextBox: true, margin: 0 });
  }
  return s;
}
function title(s, text, sub, dark = false) {
  s.addText(text, { x: M, y: 0.45, w: W - 2 * M, h: 0.8, fontFace: FONT, fontSize: 28, bold: true, color: dark ? C.white : C.navy, isTextBox: true, margin: 0, valign: 'top' });
  if (sub) s.addText(sub, { x: M, y: 1.2, w: W - 2 * M, h: 0.5, fontFace: FONT, fontSize: 14, color: dark ? 'C3CFDD' : C.ink2, isTextBox: true, margin: 0, valign: 'top' });
}
async function iconCircle(s, name, x, y, d = 0.6, fill = C.amber, ic = C.navy) {
  s.addShape(pres.ShapeType.ellipse, { x, y, w: d, h: d, fill: { color: fill }, line: { color: fill } });
  if (icons) { const img = await icons(name, ic); s.addImage({ data: img, x: x + d * 0.25, y: y + d * 0.25, w: d * 0.5, h: d * 0.5 }); }
}
function tile(s, x, y, w, h, num, label, src, dark = false) {
  s.addShape(pres.ShapeType.roundRect, { x, y, w, h, rectRadius: 0.08, fill: { color: dark ? C.navy2 : C.bg }, line: { color: dark ? C.navy2 : C.line, width: 0.75 } });
  s.addText(num, { x: x + 0.2, y: y + 0.12, w: w - 0.4, h: 0.6, fontFace: FONT, fontSize: 26, bold: true, color: dark ? C.white : C.navy, isTextBox: true, margin: 0, valign: 'top' });
  s.addText(label, { x: x + 0.2, y: y + 0.7, w: w - 0.4, h: h - 1.0, fontFace: FONT, fontSize: 11, bold: true, color: dark ? 'DFE7F1' : C.ink2, isTextBox: true, margin: 0, valign: 'top' });
  if (src) s.addText(src, { x: x + 0.2, y: y + h - 0.3, w: w - 0.4, h: 0.25, fontFace: FONT, fontSize: 9, color: dark ? 'A9B8C9' : C.ink3, isTextBox: true, margin: 0, valign: 'top' });
}
function bullets(items, opts = {}) {
  return items.map((t, i) => ({ text: t, options: { bullet: true, breakLine: i < items.length - 1, paraSpaceAfter: 6, ...opts } }));
}
const tblHead = (cells) => cells.map(t => ({ text: t, options: { bold: true, color: C.white, fill: { color: C.navy }, fontFace: FONT, fontSize: 10.5 } }));
const tblRow = (cells, fs = 10) => cells.map(t => ({ text: String(t), options: { color: C.ink, fontFace: FONT, fontSize: fs } }));

(async () => {
  // 1. Title
  {
    const s = base(true);
    s.addImage({ path: path.join(ROOT, 'site/assets/img/hero-station.jpg'), x: 6.9, y: 0, w: 6.43, h: H, sizing: { type: 'cover', w: 6.43, h: H }, transparency: 20 });
    s.addShape(pres.ShapeType.rect, { x: 6.9, y: 0, w: 0.9, h: H, fill: { color: C.navy, transparency: 15 }, line: { color: C.navy, transparency: 100 } });
    s.addText('SPONSOR-BANK BRIEFING · DOMINICAN REPUBLIC', { x: M, y: 1.4, w: 6, h: 0.35, fontFace: FONT, fontSize: 11, bold: true, color: C.amber, charSpacing: 2, isTextBox: true, margin: 0 });
    s.addText('Card acceptance built for gasoline stations.', { x: M, y: 1.85, w: 5.9, h: 2.0, fontFace: FONT, fontSize: 40, bold: true, color: C.white, isTextBox: true, margin: 0, valign: 'top' });
    s.addText('A fuel-retail acquiring program for the Dominican Republic, cleared in US dollars and operated by Wallet Partners LLC under the sponsorship of a licensed member bank.', { x: M, y: 3.95, w: 5.7, h: 1.1, fontFace: FONT, fontSize: 15, color: 'DFE7F1', isTextBox: true, margin: 0, valign: 'top' });
    s.addText('Wallet Partners LLC  ·  September 2026  ·  Confidential', { x: M, y: 6.6, w: 6, h: 0.35, fontFace: FONT, fontSize: 11, color: 'A9B8C9', isTextBox: true, margin: 0 });
    s.addNotes('Opening. Frame the meeting: we are asking for sponsorship of a vertical acquiring program, we bring a launch cohort of 20 stations and a pricing model the segment has publicly asked for.');
  }
  // 2. Executive summary
  {
    const s = base(); title(s, 'Executive summary', 'Three things to take away from this briefing');
    const cols = [
      ['FaFire', 'The moment', ['In July 2026 fuel retailers (ANADEGAS) threatened to pull card terminals from 780+ stations over 1.95–2.50% fees.', 'Those fees equal RD$6.59–8.45 per gallon: 25–36% of a State-set RD$25 gross margin.', 'Government-brokered talks with the banks are ongoing; the segment asked for per-gallon pricing.']],
      ['FaGasPump', 'The program', ['Wallet Partners operates as payment facilitator / program manager under your membership and oversight.', 'Merchant pricing 25 bps below each station\'s current contract, no monthly minimum, terminals on monthly rental, transactions cleared in US dollars.', 'Launch cohort: 20 stations in Santo Domingo\'s Polígono Central, 9 of them open 24 h.']],
      ['FaHandshake', 'The ask', ['Sponsorship agreement and registration of Wallet Partners as payment facilitator.', 'Program settlement account with agreed reserves; merchant approval SLA of 10 business days.', 'Named relationship and compliance contacts. Target: first live station within one quarter.']],
    ];
    for (let i = 0; i < 3; i++) {
      const x = M + i * 4.1, y = 1.9, w = 3.9;
      s.addShape(pres.ShapeType.roundRect, { x, y, w, h: 4.6, rectRadius: 0.1, fill: { color: C.bg }, line: { color: C.line, width: 0.75 } });
      await iconCircle(s, cols[i][0], x + 0.25, y + 0.25);
      s.addText(cols[i][1], { x: x + 1.0, y: y + 0.3, w: w - 1.2, h: 0.5, fontFace: FONT, fontSize: 18, bold: true, color: C.navy, isTextBox: true, margin: 0 });
      s.addText(bullets(cols[i][2]), { x: x + 0.25, y: y + 1.05, w: w - 0.5, h: 3.4, fontFace: FONT, fontSize: 12.5, color: C.ink, isTextBox: true, margin: 0, valign: 'top' });
    }
    s.addNotes('Keep to 90 seconds. The rest of the deck is evidence for these three columns.');
  }
  // 3. Timeline of the 2026 dispute
  {
    const s = base(); title(s, 'The moment: retailers went public on card fees', 'Timeline of the June–July 2026 dispute between ANADEGAS and the acquirers');
    const ev = [
      ['30 Jun', 'ANADEGAS announces members will stop accepting cards, citing 1.95–2.50% commissions.'],
      ['2 Jul', 'Vice-President says the Government expects an agreement; press notes similar fights abroad.'],
      ['5–6 Jul', 'Staged removal of terminals from 780+ stations begins. Fees estimated at RD$584 M per month.'],
      ['7 Jul', 'After meeting MICM and Pro Consumidor, a 30-day window is agreed. ANADEGAS proposes per-gallon or margin-based fees.'],
      ['8 Jul', 'Diario Libre: card payments at stations total about RD$41 bn per year.'],
      ['20 Jul', 'ANADEGAS and the banking sector agree to open formal talks on terminal commissions.'],
    ];
    const y0 = 3.05, x0 = M + 0.3, step = (W - 2 * M - 0.6) / (ev.length - 1);
    s.addShape(pres.ShapeType.line, { x: x0, y: y0, w: step * (ev.length - 1), h: 0, line: { color: C.line, width: 2 } });
    ev.forEach((e, i) => {
      const x = x0 + i * step;
      s.addShape(pres.ShapeType.ellipse, { x: x - 0.17, y: y0 - 0.17, w: 0.34, h: 0.34, fill: { color: i === 3 ? C.amber : C.navy }, line: { color: C.white, width: 2 } });
      s.addText(e[0], { x: x - 0.9, y: y0 - 0.75, w: 1.8, h: 0.4, fontFace: FONT, fontSize: 13, bold: true, color: C.navy, align: 'center', isTextBox: true, margin: 0 });
      s.addText(e[1], { x: x - 0.95, y: y0 + 0.35, w: 1.9, h: 2.3, fontFace: FONT, fontSize: 10.5, color: C.ink2, align: 'center', isTextBox: true, margin: 0, valign: 'top' });
    });
    s.addShape(pres.ShapeType.roundRect, { x: M, y: 5.75, w: W - 2 * M, h: 1.0, rectRadius: 0.08, fill: { color: 'FFF8E6' }, line: { color: C.amber, width: 0.75 } });
    s.addText([{ text: 'Why it matters to a sponsor. ', options: { bold: true } }, { text: 'The retailers\' own numbers show that price, not card acceptance, is the issue. A program priced 25 bps below each station\'s current contract, with no monthly minimum, gives a bank a defensible way to grow fuel-segment volume while the incumbents are locked in a public dispute with the segment.' }], { x: M + 0.25, y: 5.85, w: W - 2 * M - 0.5, h: 0.8, fontFace: FONT, fontSize: 12, color: C.ink, isTextBox: true, margin: 0, valign: 'middle' });
    s.addNotes('Sources: Listín Diario 30 Jun 2026; Diario Libre 2, 5, 6, 7, 8 and 20 Jul 2026; Infobae 8 Jul 2026. Full list in the appendix.');
  }
  // 4. Fee vs margin chart
  {
    const s = base(); title(s, 'Card fees take a quarter to a third of gross margin', 'Pesos per gallon: acquirer fee versus what the station keeps, on a regulated gross margin of about RD$25');
    s.addChart(pres.ChartType.bar, [
      { name: 'Acquirer fee per gallon', labels: ['Low case (1.95%)', 'High case (2.50%)'], values: [6.59, 8.45] },
      { name: 'Remaining gross margin', labels: ['Low case (1.95%)', 'High case (2.50%)'], values: [18.41, 16.55] },
    ], { x: M, y: 1.9, w: 7.6, h: 4.6, barDir: 'bar', barGrouping: 'stacked', chartColors: [C.orange, C.line], showValue: true, dataLabelPosition: 'ctr', dataLabelFontSize: 11, dataLabelColor: C.ink, dataLabelFormatCode: '"RD$"0.00',
      showLegend: true, legendPos: 'b', legendFontSize: 10, legendColor: C.ink2, catAxisLabelColor: C.ink2, catAxisLabelFontSize: 12, valAxisLabelColor: C.ink3, valAxisLabelFontSize: 9, valAxisMaxVal: 25, valAxisMinVal: 0, valGridLine: { color: 'EEF2F6', size: 0.5 }, catGridLine: { style: 'none' }, showTitle: false });
    tile(s, 8.6, 1.9, 4.13, 1.45, '25–36%', 'of gross margin goes to card fees', 'ANADEGAS, July 2026');
    tile(s, 8.6, 3.5, 4.13, 1.45, 'RD$6.59–8.45', 'per gallon at 1.95–2.50%', 'Infobae / Diario Libre, Jul 2026');
    tile(s, 8.6, 5.1, 4.13, 1.45, 'RD$5–6 bn', 'paid yearly in commissions by stations', '≈RD$584 M per month');
    s.addNotes('Retail price and retailer margin are fixed weekly by the Ministry (MICM). A percentage fee therefore rises with pump prices while the margin does not. Bars use ANADEGAS per-gallon figures against a RD$25 margin.');
  }
  // 5. Card economy
  {
    const s = base(); title(s, 'The card economy keeps compounding', 'Banco Central data: a payments market still early in its shift from cash');
    s.addChart(pres.ChartType.bar, [{ name: 'Card transactions (millions)', labels: ['2008', '2025'], values: [117, 806] }],
      { x: M, y: 1.9, w: 5.6, h: 4.6, barDir: 'col', chartColors: [C.blue], showValue: true, dataLabelPosition: 'outEnd', dataLabelFontSize: 12, dataLabelColor: C.ink, showLegend: false, showTitle: true, title: 'Card transactions per year (millions)', titleFontSize: 12, titleColor: C.navy, catAxisLabelColor: C.ink2, valAxisLabelColor: C.ink3, valAxisLabelFontSize: 9, valGridLine: { color: 'EEF2F6', size: 0.5 }, catGridLine: { style: 'none' }, valAxisMaxVal: 900 });
    const tiles = [['RD$1.07 tn', 'value of card payments, 2025', '+12.8% year on year'], ['63.6%', 'cards\' share of value settled', 'retail instruments, 2025'], ['757 / 373', 'debit / credit cards per 1,000 people', 'Q1 2026'], ['19,038', 'POS terminals per million people', 'Q1 2026'], ['≈75%', 'of payments still made in cash', 'Diario Libre, Dec 2025'], ['81', 'e-payment accounts per 1,000 (from 62)', 'Q1 2026, +31%']];
    tiles.forEach((t, i) => { const col = i % 2, row = Math.floor(i / 2); tile(s, 6.6 + col * 3.15, 1.9 + row * 1.62, 3.0, 1.52, t[0], t[1], t[2]); });
    s.addNotes('Sources: elDinero (BCRD) for 2008/2025 transaction counts; Invertix (BCRD) for 2025 value and instrument shares; Infobae 25 Apr 2026 for Q1 2026 bulletin figures; Diario Libre 4 Dec 2025 for cash share.');
  }
  // 6. Fuel retail structure
  {
    const s = base(); title(s, 'Fuel retail: regulated, price-controlled, high volume', 'A concentrated market with three incumbent acquirers and no vertical product');
    const cards = [
      ['FaStore', '≈1,025 stations', 'ANADEGAS estimate for the country; 780+ affiliated. MICM approved 33 new stations and LPG plants in 2024–Oct 2025 and keeps an open registry. Every new licence must pick an acquirer on day one.'],
      ['FaUniversity', 'Three acquirers', 'CardNET (bank-owned), AZUL (Grupo Popular, 2014) and Visanet Dominicana. All three price fuel like any other retail category; none offers a fuel-specific program, fleet cards or forecourt integration.'],
      ['FaCalendarAlt', 'Weekly price setting', 'MICM publishes retail prices every week. 2025: premium RD$290.10, regular RD$272.50 per gallon. Price and margin are fixed; the percentage fee is the only cost the station cannot control.'],
    ];
    for (let i = 0; i < 3; i++) {
      const x = M + i * 4.1, y = 1.9, w = 3.9;
      s.addShape(pres.ShapeType.roundRect, { x, y, w, h: 3.2, rectRadius: 0.1, fill: { color: C.bg }, line: { color: C.line, width: 0.75 } });
      await iconCircle(s, cards[i][0], x + 0.25, y + 0.25);
      s.addText(cards[i][1], { x: x + 1.0, y: y + 0.3, w: w - 1.2, h: 0.5, fontFace: FONT, fontSize: 17, bold: true, color: C.navy, isTextBox: true, margin: 0 });
      s.addText(cards[i][2], { x: x + 0.25, y: y + 1.0, w: w - 0.5, h: 2.1, fontFace: FONT, fontSize: 11.5, color: C.ink, isTextBox: true, margin: 0, valign: 'top' });
    }
    s.addTable([tblHead(['Indicator', 'Value', 'Period']),
      tblRow(['Card payments at fuel stations', '≈RD$41,000 MM per year', '2026 (Diario Libre)']),
      tblRow(['Commissions paid by stations', '≈RD$584 MM / month; RD$5–6 bn / year', '2026 (Diario Libre)']),
      tblRow(['Fee per transaction', '1.95%–2.50%', '2026 (ANADEGAS)']),
      tblRow(['Implied card volume per station', '≈RD$40 MM / year (≈RD$3.3 MM / month)', 'RD$41 bn ÷ ≈1,025 stations'])],
      { x: M, y: 5.3, w: W - 2 * M, colW: [4.2, 4.6, 3.33], fontFace: FONT, border: { type: 'solid', color: C.line, pt: 0.5 }, rowH: 0.3, autoPage: false });
    s.addNotes('The per-station figure is a national average; Polígono Central sites are expected to run above it. Use it only as the basis for the scenario slide.');
  }
  // 7. Launch zone map
  {
    const s = base(); title(s, 'Launch cohort: 20 stations in one district', 'Santo Domingo\'s Polígono Central, bounded by Av. Kennedy, 27 de Febrero, Churchill and Máximo Gómez');
    s.addImage({ path: path.join(ROOT, 'site/assets/img/poligono-map.png'), x: M, y: 1.85, w: 7.9, h: 4.9 });
    tile(s, 8.8, 1.85, 3.93, 1.3, `${S.length}`, 'stations within 2.1 km of the centre', `${inside} inside the polygon, ${S.length - inside} adjacent`);
    tile(s, 8.8, 3.3, 3.93, 1.3, `${h24}`, 'open 24 hours', `${Math.round(100 * h24 / S.length)}% of the cohort`);
    tile(s, 8.8, 4.75, 3.93, 1.3, `${new Set(S.map(x => x.brand)).size}`, 'fuel brands', `TotalEnergies ${S.filter(x => x.brand === 'TotalEnergies').length}, Next 2, nine others`);
    s.addText('Warm pipeline: these stations have indicated they are ready to sign once the sponsorship and merchant-of-record arrangement are in place. Merchant files are being assembled to the bank\'s standard.', { x: 8.8, y: 6.2, w: 3.93, h: 0.75, fontFace: FONT, fontSize: 9.5, color: C.ink2, isTextBox: true, margin: 0, valign: 'top' });
    s.addNotes('Station list compiled from public map listings on 8 Sep 2026. The polygon is an approximation of the four avenues. Interactive version at /zona/ on the website.');
  }
  // 8-9. Station tables
  for (let part = 0; part < 2; part++) {
    const s = base(); title(s, `Launch cohort: station list (${part + 1} of 2)`, 'Hours and phones from public listings; re-verified during onboarding');
    const rows = S.slice(part * 10, part * 10 + 10).map(x => tblRow([x.id, x.name, x.brand, x.address, x.phone || '—', x.hours, x.inside ? 'Inside' : 'Adjacent', x.distKm.toFixed(2)], 9.5));
    s.addTable([tblHead(['#', 'Station', 'Brand', 'Address', 'Phone', 'Hours', 'Zone', 'km'])].concat(rows), { x: M, y: 1.85, w: W - 2 * M, colW: [0.4, 2.9, 1.35, 3.0, 1.3, 1.5, 0.98, 0.7], fontFace: FONT, border: { type: 'solid', color: C.line, pt: 0.5 }, rowH: 0.38, autoPage: false });
    s.addNotes('Distances measured from the reference centre 18.4690, -69.9295. Coordinates and Google Maps links are in the CSV/GeoJSON files.');
  }
  // 10. Transaction flow
  {
    const s = base(); title(s, 'How a transaction flows', 'Wallet Partners runs the merchant side; the sponsoring bank holds membership, funds and oversight');
    const steps = [['FaCreditCard', 'Customer pays at the forecourt', 'Attendant keys the sale or the pump controller pushes it to a wireless EMV/contactless terminal. Stripe disabled by policy.'],
      ['FaNetworkWired', 'Authorisation', 'P2PE-encrypted transaction goes through our certified gateway to the bank\'s acquiring host and on to Visa, Mastercard or domestic debit under the bank\'s BINs.'],
      ['FaUniversity', 'Settlement', 'Networks settle to the bank\'s program account in US dollars. We pay each station in dollars, net of the agreed rate.'],
      ['FaChartBar', 'Reporting', 'Stations reconcile by shift and pump; the bank gets portfolio dashboards, exception reports and regulatory data.'],
      ['FaShieldAlt', 'Disputes and risk', 'Chargebacks worked under network rules; per-station reserves and velocity limits protect the bank\'s exposure.']];
    const w = (W - 2 * M - 0.4 * 4) / 5;
    for (let i = 0; i < 5; i++) {
      const x = M + i * (w + 0.4), y = 1.95;
      s.addShape(pres.ShapeType.roundRect, { x, y, w, h: 4.3, rectRadius: 0.1, fill: { color: i === 2 ? C.navy : C.bg }, line: { color: i === 2 ? C.navy : C.line, width: 0.75 } });
      await iconCircle(s, steps[i][0], x + 0.2, y + 0.2, 0.55, C.amber, C.navy);
      s.addText(String(i + 1), { x: x + w - 0.6, y: y + 0.2, w: 0.4, h: 0.4, fontFace: FONT, fontSize: 18, bold: true, color: i === 2 ? C.amber : C.line, align: 'right', isTextBox: true, margin: 0 });
      s.addText(steps[i][1], { x: x + 0.2, y: y + 0.95, w: w - 0.4, h: 0.8, fontFace: FONT, fontSize: 14, bold: true, color: i === 2 ? C.white : C.navy, isTextBox: true, margin: 0, valign: 'top' });
      s.addText(steps[i][2], { x: x + 0.2, y: y + 1.8, w: w - 0.4, h: 2.4, fontFace: FONT, fontSize: 11, color: i === 2 ? 'DFE7F1' : C.ink, isTextBox: true, margin: 0, valign: 'top' });
      if (i < 4) s.addText('›', { x: x + w + 0.02, y: y + 1.9, w: 0.36, h: 0.5, fontFace: FONT, fontSize: 28, color: C.amberD, align: 'center', isTextBox: true, margin: 0 });
    }
    s.addNotes('Settlement (step 3) is highlighted because it is where the bank\'s control sits: the program account is the bank\'s, reserves are set with the bank, and Wallet Partners never holds merchant funds outside it.');
  }
  // 11. Responsibility matrix
  {
    const s = base(); title(s, 'Who does what', 'Division of responsibilities between Wallet Partners LLC and the sponsoring bank');
    const rows = [
      ['Card-network membership and BINs', '—', 'Holds membership; registers Wallet Partners as payment facilitator'],
      ['Merchant prospecting and sales', 'Owns pipeline and station relationships', '—'],
      ['Merchant KYC/KYB and underwriting', 'Collects documents, screens owners and sanctions lists, prepares file', 'Approves, conditions or declines each merchant'],
      ['Terminals and integration', 'Supplies certified EMV/contactless terminals; installs and supports', 'Certifies terminal and gateway on its host'],
      ['Pricing to the station', 'Quotes 25 bps below the station\'s current contract, no monthly minimum, terminal rental', 'Approves pricing floors and interchange pass-through'],
      ['Settlement', 'Pays stations in US dollars from program account; maintains reserves', 'Settles network funds into program account; controls the account'],
      ['Transaction monitoring and AML', 'First-line monitoring, alerts, escalation', 'Second-line review; regulatory reporting'],
      ['Disputes and chargebacks', 'Representment and merchant recovery', 'Network-facing dispute processing'],
      ['PCI DSS', 'Own compliance; P2PE terminals, no cardholder data stored', 'Validates Wallet Partners as service provider'],
      ['Audit and oversight', 'Records access, monthly reporting, right-to-audit', 'Periodic reviews; can suspend merchants or program'],
    ].map(r => tblRow(r, 10));
    s.addTable([tblHead(['Function', 'Wallet Partners LLC', 'Sponsoring bank'])].concat(rows), { x: M, y: 1.85, w: W - 2 * M, colW: [3.2, 4.5, 4.43], fontFace: FONT, border: { type: 'solid', color: C.line, pt: 0.5 }, rowH: 0.42, autoPage: false });
    s.addNotes('This matrix is the starting point for the sponsorship term sheet. Rows can move; the principle is that the bank keeps approval, funds and oversight.');
  }
  // 12. What the station gets
  {
    const s = base(); title(s, 'What the station gets', 'A product built around forecourts, night shifts and a simple price');
    s.addImage({ path: path.join(ROOT, 'site/assets/img/pos-tap.jpg'), x: M, y: 1.9, w: 4.4, h: 2.475, rounding: false });
    s.addText('Illustrative image', { x: M, y: 4.4, w: 4.4, h: 0.3, fontFace: FONT, fontSize: 9, color: C.ink3, isTextBox: true, margin: 0 });
    const feats = [['FaGasPump', '25 bps below today', 'Rate 0.25 points below the station\'s current contract, no monthly minimum; interchange-plus statements the owner can compare line by line.'],
      ['FaClock', 'Cleared in dollars', 'Transactions cleared in US dollars, per station, with shift-level reconciliation; terminals on monthly rental with replacement included.'],
      ['FaWifi', 'Forecourt-ready terminals', 'Rugged wireless EMV/contactless, pre-auth and completion, Spanish prompts, pump-controller integration where supported.'],
      ['FaChartLine', 'Owner dashboard', 'Sales by pump, shift and product; card mix; chargebacks; statements formatted for the accountant and DGII.'],
      ['FaShieldAlt', 'Fraud and dispute desk', 'Velocity limits per pump and card, EMV liability-shift compliance, disputes worked on the station\'s behalf.'],
      ['FaIdCard', 'Fleet and loyalty ready', 'Phase two adds fleet-card acceptance and station loyalty, with issuing and co-brand upside for the bank.']];
    for (let i = 0; i < 6; i++) {
      const col = i % 2, row = Math.floor(i / 2), x = 5.3 + col * 3.85, y = 1.9 + row * 1.6;
      await iconCircle(s, feats[i][0], x, y + 0.05, 0.5);
      s.addText(feats[i][1], { x: x + 0.65, y: y, w: 3.05, h: 0.35, fontFace: FONT, fontSize: 13, bold: true, color: C.navy, isTextBox: true, margin: 0 });
      s.addText(feats[i][2], { x: x + 0.65, y: y + 0.38, w: 3.05, h: 1.15, fontFace: FONT, fontSize: 10, color: C.ink2, isTextBox: true, margin: 0, valign: 'top' });
    }
    s.addNotes('Fleet and loyalty are deliberately phase two: they need the acquiring rails live first and they are where the bank\'s issuing side can participate.');
  }
  // 13. Scenario economics
  {
    const s = base(); title(s, 'What the launch cohort could represent', 'Illustrative scenarios, not a forecast. Assumptions are editable in the website calculator.');
    const sc = [10, 20, 40]; const perMonth = 3.3; const mdr = 0.0195;
    const vol = sc.map(k => k * perMonth * 12); const rev = vol.map(v => v * mdr);
    s.addChart(pres.ChartType.bar, [{ name: 'Annual card volume (RD$ MM)', labels: sc.map(k => k + ' stations'), values: vol.map(v => Math.round(v)) }],
      { x: M, y: 1.9, w: 6.6, h: 4.6, barDir: 'col', chartColors: [C.blue], showValue: true, dataLabelPosition: 'outEnd', dataLabelFontSize: 11, dataLabelColor: C.ink, dataLabelFormatCode: '#,##0', showLegend: false, showTitle: true, title: 'Annual card volume by cohort size (RD$ millions)', titleFontSize: 12, titleColor: C.navy, catAxisLabelColor: C.ink2, valAxisLabelColor: C.ink3, valAxisLabelFontSize: 9, valGridLine: { color: 'EEF2F6', size: 0.5 }, catGridLine: { style: 'none' } });
    const fx = 62;
    s.addTable([tblHead(['Scenario', 'Annual volume', 'Gross MDR @1.95%', 'US$ equiv.'])].concat(sc.map((k, i) => tblRow([k + ' stations', 'RD$' + Math.round(vol[i]).toLocaleString('en-US') + ' MM', 'RD$' + rev[i].toFixed(1) + ' MM', 'US$' + Math.round(rev[i] * 1e6 / fx / 1000).toLocaleString('en-US') + ' k'], 10.5))),
      { x: 7.6, y: 1.9, w: 5.13, colW: [1.3, 1.45, 1.45, 0.93], fontFace: FONT, border: { type: 'solid', color: C.line, pt: 0.5 }, rowH: 0.4, autoPage: false });
    s.addText([{ text: 'Assumptions. ', options: { bold: true } }, { text: 'Card volume per station RD$3.3 MM per month, the national average implied by RD$41 bn a year across about 1,025 stations; Polígono Central sites are expected to run above it. Effective MDR 1.95%, i.e. 25 bps below a station currently paying 2.20%. Exchange rate RD$62 per US$. Interchange, network fees, terminal costs and the bank\'s share are not deducted; the revenue split is a negotiation item.' }],
      { x: 7.6, y: 3.75, w: 5.13, h: 2.75, fontFace: FONT, fontSize: 10.5, color: C.ink2, isTextBox: true, margin: 0, valign: 'top' });
    s.addNotes('Walk through the 20-station case only; the 10 and 40 cases show sensitivity. Merchant pricing is 25 bps below each station\'s current contract, so the gross MDR shown at 1.95% is a ceiling for stations currently at 2.20%.');
  }
  // 14. Compliance
  {
    const s = base(); title(s, 'Compliance framework', 'Built to the standard a sponsoring bank\'s second line will require; validated before the first live transaction');
    const left = ['Law 183-02 and the Monetary Board\'s Payment Systems Regulation (SIPARD, amended Aug 2025); BCRD oversight, Superintendencia de Bancos supervision of the sponsor.', 'Law 155-17 AML/CFT: merchant due diligence, beneficial owners at 10%+, monitoring, 5–10 year record-keeping, STRs through the bank to the UAF.', 'Law 172-13 data protection; Law 358-05 consumer protection (Pro Consumidor).', 'DGII card-withholding rules (Norma 08-04 and successors) reconciled with the fuel tax regime (Laws 112-00 / 557-05); parameters confirmed with the bank and tax counsel.', 'Only stations with a valid MICM operating resolution are eligible.'];
    const right = ['BSA/AML programme aligned with the sponsor; FinCEN registration where applicable; OFAC and sanctions screening of all merchants and owners.', 'Visa Core Rules and Mastercard Rules for payment facilitators; MCC 5541/5542; AFD authorisation and completion rules; MATCH checks.', 'PCI DSS v4.0 as a Level 1 service provider; P2PE terminals; no PAN, track or CVV stored.', 'Information security: segmented cloud, encryption at rest, dual-control keys, MFA, central logging, annual pen test, incident-response plan with agreed notification timelines.', 'Governance: compliance officer, board-approved policies, annual independent review, staff training, contractual right-to-audit for the bank.'];
    for (const [i, [hdr, items, icon]] of [['Dominican Republic', left, 'FaFlag'], ['United States and international', right, 'FaGlobeAmericas']].entries()) {
      const x = M + i * 6.2, w = 5.93;
      await iconCircle(s, icon, x, 1.85, 0.5);
      s.addText(hdr, { x: x + 0.65, y: 1.85, w: w - 0.65, h: 0.5, fontFace: FONT, fontSize: 16, bold: true, color: C.navy, isTextBox: true, margin: 0, valign: 'middle' });
      s.addText(bullets(items), { x, y: 2.5, w, h: 4.2, fontFace: FONT, fontSize: 11, color: C.ink, isTextBox: true, margin: 0, valign: 'top' });
    }
    s.addNotes('Document set available under NDA: AML programme and risk assessment, sanctions procedure, underwriting policy and file template, fuel monitoring rule set, infosec policies and PCI plan, privacy programme, BCP/IR plans, draft sponsorship term sheet and reserve model.');
  }
  // 15. Rollout
  {
    const s = base(); title(s, 'From sponsorship to live stations in one quarter', 'Staged go-live inside the Polígono Central, then expansion on the same playbook');
    const ph = [['Weeks 1–4', 'Program set-up', 'Sponsorship agreement; payment-facilitator registration; gateway and terminal certification on the bank\'s host; program account and reserve structure.'],
      ['Weeks 3–8', 'Merchant underwriting', 'Bank review of the 20 pipeline files; site surveys; connectivity checks; terminal provisioning.'],
      ['Weeks 8–12', 'Staged go-live', 'Five stations inside the polygon in wave one, then the remaining fifteen in two waves. Daily settlement and monitoring from the first transaction.'],
      ['Quarter 2+', 'Expansion', 'Rest of Distrito Nacional and Santiago; fleet cards; pricing review with the bank against actual interchange.']];
    const w = (W - 2 * M - 0.3 * 3) / 4;
    ph.forEach((p, i) => {
      const x = M + i * (w + 0.3), y = 2.0;
      s.addShape(pres.ShapeType.roundRect, { x, y, w, h: 4.2, rectRadius: 0.1, fill: { color: i === 3 ? C.navy : C.bg }, line: { color: i === 3 ? C.navy : C.line, width: 0.75 } });
      s.addShape(pres.ShapeType.ellipse, { x: x + 0.25, y: y + 0.25, w: 0.55, h: 0.55, fill: { color: C.amber }, line: { color: C.amber } });
      s.addText(String(i + 1), { x: x + 0.25, y: y + 0.25, w: 0.55, h: 0.55, fontFace: FONT, fontSize: 16, bold: true, color: C.navy, align: 'center', valign: 'middle', isTextBox: true, margin: 0 });
      s.addText(p[0], { x: x + 0.95, y: y + 0.25, w: w - 1.15, h: 0.55, fontFace: FONT, fontSize: 12, bold: true, color: i === 3 ? C.amber : C.amberD, isTextBox: true, margin: 0, valign: 'middle' });
      s.addText(p[1], { x: x + 0.25, y: y + 1.0, w: w - 0.5, h: 0.5, fontFace: FONT, fontSize: 15, bold: true, color: i === 3 ? C.white : C.navy, isTextBox: true, margin: 0 });
      s.addText(p[2], { x: x + 0.25, y: y + 1.6, w: w - 0.5, h: 2.4, fontFace: FONT, fontSize: 11.5, color: i === 3 ? 'DFE7F1' : C.ink, isTextBox: true, margin: 0, valign: 'top' });
    });
    s.addNotes('The 10-business-day merchant approval SLA is what keeps weeks 3–8 on schedule.');
  }
  // 16. The ask
  {
    const s = base(true);
    s.addText('THE ASK', { x: M, y: 0.6, w: 6, h: 0.35, fontFace: FONT, fontSize: 11, bold: true, color: C.amber, charSpacing: 2, isTextBox: true, margin: 0 });
    s.addText('A sponsorship agreement, then one merchant file at a time.', { x: M, y: 1.0, w: 7.2, h: 1.6, fontFace: FONT, fontSize: 30, bold: true, color: C.white, isTextBox: true, margin: 0, valign: 'top' });
    s.addText(bullets(['Visa and Mastercard acquiring membership in the DR, or a correspondent arrangement permitting program sponsorship', 'Registration of Wallet Partners LLC as payment facilitator / program manager', 'Program settlement account with agreed reserve and release terms', 'Merchant-approval SLA of ten business days per file', 'A named relationship contact and a compliance contact'], { color: 'DFE7F1' }), { x: M, y: 2.8, w: 6.8, h: 3.4, fontFace: FONT, fontSize: 14, color: 'DFE7F1', isTextBox: true, margin: 0, valign: 'top' });
    s.addShape(pres.ShapeType.roundRect, { x: 8.0, y: 1.0, w: 4.73, h: 5.4, rectRadius: 0.1, fill: { color: C.navy2 }, line: { color: C.navy2 } });
    s.addText('Proposed next steps', { x: 8.3, y: 1.25, w: 4.2, h: 0.5, fontFace: FONT, fontSize: 18, bold: true, color: C.white, isTextBox: true, margin: 0 });
    s.addText(bullets(['NDA and exchange of the document set (AML programme, underwriting policy, PCI plan, reserve model)', 'Working session with merchant-acquiring and compliance teams, in English or Spanish', 'Joint review of three sample merchant files from the cohort', 'Draft term sheet within 30 days of the working session', 'Target: first live station within one quarter of signature'], { color: 'DFE7F1' }), { x: 8.3, y: 1.9, w: 4.2, h: 3.5, fontFace: FONT, fontSize: 12.5, isTextBox: true, margin: 0, valign: 'top' });
    s.addText('info@walletpartnersllc.com', { x: 8.3, y: 5.65, w: 4.2, h: 0.4, fontFace: FONT, fontSize: 13, bold: true, color: C.amber, isTextBox: true, margin: 0 });
    s.addText('Wallet Partners LLC  ·  Confidential', { x: M, y: 6.75, w: 6, h: 0.35, fontFace: FONT, fontSize: 10, color: 'A9B8C9', isTextBox: true, margin: 0 });
    s.addNotes('Close by agreeing the date for the working session and who from the bank attends.');
  }
  // 17. Appendix: sources
  {
    const s = base(); title(s, 'Appendix: sources', 'All market figures quoted as published; links current as of 8 September 2026');
    const src = ['Listín Diario, 30 Jun 2026 — Dueños de estaciones de combustible retirarán uso verifone para pago automático', 'Diario Libre, 2 Jul 2026 — RD se suma a los países donde las gasolineras pelean con la banca por comisiones de tarjetas', 'Diario Libre, 5 Jul 2026 — Anadegas iniciará este lunes el retiro de verifones en más de 780 estaciones', 'Diario Libre, 6 Jul 2026 — La amenaza de retirar los verifones: ¿en qué consiste el conflicto entre Anadegas y la banca?', 'Diario Libre, 7 Jul 2026 — Anadegas acuerda plazo de 30 días para solucionar conflicto por pagos con tarjetas', 'Infobae, 8 Jul 2026 — Plazo de 30 días en República Dominicana para resolver uso de tarjetas en gasolineras', 'Diario Libre, 8 Jul 2026 — Pagos con tarjetas en estaciones de combustibles suma RD$41,000 MM', 'Diario Libre, 20 Jul 2026 — Anadegas y la banca iniciarán diálogo sobre comisión de verifones', 'El Nuevo Diario, 2026 — Anadegas retirará lectores de tarjetas (≈1,025 stations nationwide)',
      'elDinero — Pagos con tarjetas de crédito y débito en RD (BCRD: 117 M transactions in 2008, 806 M in 2025)', 'Invertix — Sistema de Pago y Liquidación de Valores al cierre del 2025 (BCRD: RD$1,072.5 bn, +12.8%, 63.6% share)', 'Infobae, 25 Apr 2026 — Cuentas de pago electrónicas +31.3% (BCRD Q1 2026 bulletin: cards and POS per capita)', 'Banco Central de la República Dominicana — Boletín de Estadísticas de Sistemas de Pago', 'Diario Libre, 4 Dec 2025 — El 75 % de los pagos de los dominicanos son en efectivo', 'Mastercard, May 2026 — Estudio sobre el punto de inflexión de los pagos digitales en RD', 'MICM — Avisos semanales de precios de combustibles (2025 prices)', 'EHPLUS+ — MICM aprobó 33 estaciones y envasadoras entre 2024 y octubre de 2025', 'MICM — Datos abiertos: registro de estaciones de combustible 2023–2026', 'U.S. ITA — Dominican Republic Country Commercial Guide: eCommerce (Cardnet, Visanet, Azul)', 'Station list: Google Maps search "gasolinera", 8 Sep 2026, 20 nearest to 18.4690, -69.9295'];
    const half = Math.ceil(src.length / 2);
    s.addText(bullets(src.slice(0, half), { paraSpaceAfter: 4 }), { x: M, y: 1.85, w: 6.0, h: 4.9, fontFace: FONT, fontSize: 9.5, color: C.ink2, isTextBox: true, margin: 0, valign: 'top' });
    s.addText(bullets(src.slice(half), { paraSpaceAfter: 4 }), { x: M + 6.2, y: 1.85, w: 5.93, h: 4.9, fontFace: FONT, fontSize: 9.5, color: C.ink2, isTextBox: true, margin: 0, valign: 'top' });
    s.addNotes('Clickable versions of every source are on the website (docs/DATA.md in the repository lists them with URLs).');
  }

  const out = path.join(__dirname, 'Wallet-Partners-Sponsor-Bank-Deck.pptx');
  await pres.writeFile({ fileName: out });
  console.log('wrote', out, n, 'slides');
})().catch(e => { console.error(e); process.exit(1); });
