FAQ = [
    ("¿Tengo que cambiar de banco?", "No. La liquidación se deposita en la cuenta bancaria que usted indique, en cualquier banco del país. Solo cambia quién procesa las tarjetas en su estación."),
    ("¿En qué moneda recibo el dinero?", "Las transacciones se liquidan en dólares estadounidenses a la cuenta que usted designe. El estado de cuenta detalla cada turno."),
    ("¿Qué tarjetas puedo aceptar?", "Visa y Mastercard, crédito y débito, nacionales e internacionales, con chip, sin contacto y billeteras móviles. Otras redes se agregan a medida que el banco patrocinador las habilite."),
    ("¿Cuánto cuesta la terminal?", "La terminal se entrega en alquiler con una cuota mensual fija que incluye soporte y reposición. No hay cuota mínima de facturación."),
    ("¿Hay permanencia mínima?", "El contrato es de un año renovable y puede cancelarse con aviso de 30 días sin penalidad, devolviendo el equipo."),
    ("¿Cómo se calcula la tarifa?", "25 puntos básicos (0.25%) por debajo de la comisión de su contrato de procesamiento actual, sin mínimo mensual. En el estado de cuenta verá el intercambio, la tarifa de la red y nuestra tarifa por separado."),
    ("¿Qué pasa con los contracargos?", "Nuestra mesa de disputas arma el caso con el recibo y la evidencia de la terminal y lo defiende ante la red. Solo se cobra el contracargo si se pierde la disputa."),
    ("¿Qué documentos necesito?", "Resolución del MICM, RNC y registro mercantil, documentos constitutivos, cédulas de los socios con 10% o más y del representante legal, y certificación de la cuenta bancaria."),
    ("¿Cuánto tarda la aprobación?", "Normalmente menos de diez días hábiles desde que el expediente está completo. La instalación se programa la misma semana de la aprobación."),
    ("¿Quién es el banco patrocinador?", "Una entidad financiera autorizada, miembro de Visa y Mastercard, que aprueba cada comercio, recibe los fondos de las redes y supervisa el programa. Su nombre aparece en el contrato de afiliación."),
    ("¿Wallet Partners retiene mi dinero?", "No. Los fondos se liquidan a través de una cuenta del programa controlada por el banco patrocinador y se transfieren en dólares a la cuenta que usted indique."),
    ("¿Funciona con mi controlador de surtidores?", "Con los sistemas más comunes, sí. Si no, la terminal funciona de forma independiente: el bombero digita el monto."),
    ("¿Puedo aceptar tarjetas de flota?", "Está previsto para una segunda fase junto con un programa de fidelidad para estaciones. Le avisamos cuando esté disponible."),
    ("¿Y si mi estación no está en el Polígono Central?", "Regístrela igual. Abrimos zonas por demanda y le avisamos cuando llegue su sector."),
]

def body(ctx):
    import json
    items = "".join(f'<details class="card" style="margin-bottom:12px"><summary style="cursor:pointer;font-weight:700;color:var(--navy)">{q}</summary><p style="margin:10px 0 0">{a}</p></details>' for q, a in FAQ)
    ld = json.dumps({"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in FAQ]}, ensure_ascii=False)
    return f"""
<div class="page-title"><div class="wrap"><span class="eyebrow">Preguntas frecuentes</span><h1>Lo que nos preguntan los dueños de estaciones.</h1><p>Si no encuentra su pregunta, <a href="/contacto/">escríbanos</a> y le respondemos en un día hábil.</p></div></div>
<section><div class="wrap prose" style="max-width:860px">{items}</div></section>
<script type="application/ld+json">{ld}</script>
<section class="dark"><div class="wrap"><div class="section-head"><h2>¿Le convence?</h2><p>Registre su estación y le enviamos una propuesta con números para su volumen.</p></div><a class="btn btn-primary" href="/afiliese/">Afilie su estación</a></div></section>
"""
