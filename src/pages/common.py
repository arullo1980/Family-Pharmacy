import html as _h

ICONS = {
    "pump": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M4 21V5a2 2 0 0 1 2-2h6a2 2 0 0 1 2 2v16"/><path d="M2 21h14"/><path d="M6 8h6"/><path d="M14 9h2a2 2 0 0 1 2 2v6a1.5 1.5 0 0 0 3 0V9l-3-3"/></svg>',
    "bank": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M3 10l9-6 9 6"/><path d="M4 10v9"/><path d="M8 10v9"/><path d="M12 10v9"/><path d="M16 10v9"/><path d="M20 10v9"/><path d="M2 20h20"/></svg>',
    "map": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M12 22s7-6.2 7-12a7 7 0 0 0-14 0c0 5.8 7 12 7 12z"/><circle cx="12" cy="10" r="2.5"/></svg>',
    "shield": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M12 3l8 3v6c0 5-3.5 8.5-8 9-4.5-.5-8-4-8-9V6z"/><path d="M9 12l2 2 4-4"/></svg>',
    "card": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="5" width="20" height="14" rx="2"/><path d="M2 10h20"/><path d="M6 15h4"/></svg>',
    "chart": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M3 21h18"/><path d="M6 17V9"/><path d="M11 17V5"/><path d="M16 17v-7"/><path d="M21 17V3"/></svg>',
    "clock": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/></svg>',
    "doc": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M6 2h8l5 5v13a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2z"/><path d="M14 2v5h5"/><path d="M8 13h8"/><path d="M8 17h6"/></svg>',
}

def icon(name):
    return f'<div class="icon">{ICONS[name]}</div>'

def stat_tiles(items):
    out = ['<div class="stats">']
    for num, lbl, src in items:
        out.append(f'<div class="stat"><div class="num">{num}</div><div class="lbl">{lbl}</div><div class="src">{src}</div></div>')
    out.append('</div>')
    return "".join(out)

def brand_chart(st):
    brands = sorted(st["brands"].items(), key=lambda kv: (-kv[1], kv[0]))
    mx = brands[0][1]
    rows = "".join(
        f'<div class="bar-row" data-label="{_h.escape(b)}: {n} station{"s" if n != 1 else ""}"><span>{_h.escape(b)}</span>'
        f'<div class="track"><div class="fill" style="width:{100*n/mx:.0f}%"></div></div><span class="val">{n}</span></div>'
        for b, n in brands)
    table = "".join(f"<tr><td>{_h.escape(b)}</td><td class='num'>{n}</td></tr>" for b, n in brands)
    return f"""<div class="viz" data-tip>
      <h3>Pipeline stations by fuel brand</h3>
      <div class="sub">Count of stations, n = {st['n']}. Brand inferred from the listing name.</div>
      {rows}
      <details><summary>Table view</summary><table><tr><th>Brand</th><th class="num">Stations</th></tr>{table}</table></details>
    </div>"""

SOURCES = {
    "anadegas_retiro": ("Diario Libre, 5 Jul 2026 — Anadegas iniciará este lunes el retiro de verifones en más de 780 estaciones de combustibles",
                        "https://www.diariolibre.com/economia/energia/2026/07/05/anadegas-inicia-retiro-de-verifones-en-gasolinas/3589750"),
    "dl_41000": ("Diario Libre, 8 Jul 2026 — Pagos con tarjetas en estaciones de combustibles suma RD$41,000 MM",
                 "https://www.diariolibre.com/economia/negocios/2026/07/08/pagos-con-tarjetas-en-estaciones-de-combustibles-suma-rd41000-mm/3592457"),
    "dl_conflicto": ("Diario Libre, 6 Jul 2026 — La amenaza de retirar los verifones: ¿en qué consiste el conflicto entre Anadegas y la banca?",
                     "https://www.diariolibre.com/economia/negocios/2026/07/06/retiro-de-verifones-por-que-el-conflicto-entre-anadegas-y-la-banca/3590771"),
    "dl_acuerdo": ("Diario Libre, 7 Jul 2026 — Anadegas acuerda plazo de 30 días para solucionar conflicto por pagos con tarjetas en gasolineras",
                   "https://www.diariolibre.com/economia/negocios/2026/07/07/anadegas-y-gobierno-acuerdan-buscar-solucion-a-pagos-con-tarjetas/3592052"),
    "dl_dialogo": ("Diario Libre, 20 Jul 2026 — Anadegas y la banca iniciarán diálogo para buscar acuerdo sobre comisión de verifones",
                   "https://www.diariolibre.com/economia/energia/2026/07/20/anadegas-y-banca-buscaran-solucion-a-comisiones-por-verifones/3604944"),
    "dl_paises": ("Diario Libre, 2 Jul 2026 — RD se suma a los países donde las gasolineras pelean con la banca por comisiones de tarjetas",
                  "https://www.diariolibre.com/economia/negocios/2026/07/02/rd-se-une-a-paises-donde-gasolineras-se-quejan-por-comisiones/3587816"),
    "listin_verifone": ("Listín Diario, 30 Jun 2026 — Dueños de estaciones de combustible retirarán uso verifone para pago automático",
                        "https://listindiario.com/economia/20260630/duenos-estaciones-combustible-retiraran-verifone-pago-automatico_911891.html"),
    "infobae_30": ("Infobae, 8 Jul 2026 — Plazo de 30 días en República Dominicana para resolver uso de tarjetas en gasolineras",
                   "https://www.infobae.com/republica-dominicana/2026/07/08/plazo-de-30-dias-en-republica-dominicana-para-resolver-uso-de-tarjetas-en-gasolineras/"),
    "anadegas_1025": ("El Nuevo Diario — Anadegas retirará lectores de tarjetas de estaciones de combustibles (station count ≈1,025 per ANADEGAS)",
                      "https://elnuevodiario.com.do/anadegas-retirara-lectores-de-tarjetas-de-estaciones-de-combustibles-desde-este-lunes-por-conflicto-con-comisiones/"),
    "bcrd_806": ("elDinero — Pagos con tarjetas de crédito y débito en RD (BCRD data: 806 million card transactions in 2025)",
                 "https://eldinero.com.do/15645/pagos-con-tarjetas-de-credito-y-debito-en-republica-dominicana/"),
    "bcrd_2025": ("Invertix — Comportamiento del Sistema de Pago y Liquidación de Valores de la República Dominicana al cierre del 2025 (BCRD figures)",
                  "https://invertix.com.do/comportamiento-del-sistema-de-pago-y-liquidacion-de-valores-de-la-republica-dominicana-al-cierre-del-2025/"),
    "infobae_q1": ("Infobae, 25 Apr 2026 — Uso de cuentas de pago electrónicas aumenta 31.3% en República Dominicana durante primer trimestre de 2026 (BCRD bulletin)",
                   "https://www.infobae.com/republica-dominicana/2026/04/25/uso-de-cuentas-de-pago-electronicas-aumenta-313-en-republica-dominicana-durante-primer-trimestre-de-2026/"),
    "bcrd_boletin": ("Banco Central de la República Dominicana — Boletín de Estadísticas de Sistemas de Pago",
                     "https://cdn.bancentral.gov.do/documents/publicaciones-economicas/economia-internacional/documents/boletin_estadistica2025-06.pdf"),
    "dl_efectivo": ("Diario Libre, 4 Dec 2025 — El 75 % de los pagos de los dominicanos son en efectivo",
                    "https://www.diariolibre.com/economia/negocios/2025/12/04/el-75--de-los-pagos-de-los-dominicanos-son-en-efectivo/3367789"),
    "mastercard": ("Mastercard, May 2026 — Estudio revela el punto de inflexión de los pagos digitales en República Dominicana",
                   "https://www.mastercard.com/news/latin-america/es/sala-de-prensa/comunicados-de-prensa/pr-es/2026/mayo/estudio-de-mastercard-revela-el-punto-de-inflexion-de-los-pagos-digitales-en-republica-dominicana-que-se-necesita-para-desbloquear-la-proxima-fase-de-crecimiento/"),
    "micm_precios": ("MICM — Avisos semanales de precios de combustibles", "https://micm.gob.do/direcciones/combustibles/avisos-semanales-de-precios/avisos-semanales-de-precios-de-combustibles/"),
    "micm_33": ("EHPLUS+ — MICM aprobó 33 estaciones y envasadoras entre 2024 y octubre de 2025", "https://ehplus.do/micm-aprobo-33-estaciones-y-envasadoras-entre-2024-y-octubre-de-2025/"),
    "micm_datos": ("MICM — Datos abiertos (registro de estaciones de combustible 2023-2026)", "https://micm.gob.do/transparencia/datos-abierto"),
    "trade_gov": ("U.S. International Trade Administration — Dominican Republic Country Commercial Guide: eCommerce (Cardnet, Visanet, Azul)", "https://www.trade.gov/country-commercial-guides/dominican-republic-ecommerce"),
    "eldinero_88": ("elDinero — El 88% de los pagos con tarjetas se concentra en 3 sectores", "https://eldinero.com.do/368730/el-88-de-los-pagos-con-tarjetas-se-concentra-en-3-sectores/"),
    "ley_183": ("Ley No. 183-02 Monetaria y Financiera (Cámara de Cuentas copy)", "https://www.camaradecuentas.gob.do/transparencia/phocadownload/Transparencia/Base_legal_institucional/Leyes/Ley_183-02.pdf"),
    "jm_sipard": ("Junta Monetaria, Res. 28 Aug 2025 — Modificación del Reglamento de Sistemas de Pago (SIPARD)", "https://cdn.bancentral.gov.do/documents/normativa/documents/2da-Res-JM-28-08-2025-Mod-Reglamento-SIPARD.pdf"),
    "sb_normativas": ("Superintendencia de Bancos — Normativas", "https://sb.gob.do/normativas-sib"),
}

def sources_block(keys, title="Sources"):
    items = "".join(f'<li><a href="{SOURCES[k][1]}" rel="noopener" target="_blank">{_h.escape(SOURCES[k][0])}</a></li>' for k in keys)
    return f'<h3>{title}</h3><ol class="sources">{items}</ol><p class="small muted">Links open on third-party sites. Figures are quoted as published; where a source gives a range we show the range. Last checked {"2026-09-08"}.</p>'
