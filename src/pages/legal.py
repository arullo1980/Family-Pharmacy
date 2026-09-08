from common import sources_block

def _page(eyebrow, title, intro, content, updated="2026-09-08"):
    return f"""
<div class="page-title"><div class="wrap"><span class="eyebrow">{eyebrow}</span><h1>{title}</h1><p>{intro}</p><div class="meta-line">Última actualización: {updated}</div></div></div>
<section><div class="wrap prose">{content}</div></section>
"""

def privacy(ctx):
    e = ctx["CONTACT_EMAIL"]
    return _page("Legal", "Política de privacidad", "Cómo Wallet Partners LLC trata los datos personales que recibe a través de este sitio y en el curso de su actividad.", f"""
<h2>1. Responsable</h2><p>Wallet Partners LLC, que opera bajo el nombre comercial Bombero Partners ("Bombero Partners", "nosotros"), es responsable de este sitio. Para consultas sobre esta política o para ejercer sus derechos escriba a <a href="mailto:{e}">{e}</a>.</p>
<h2>2. Datos que recogemos en este sitio</h2>
<ul>
<li><strong>Formularios.</strong> Nombre, empresa o estación, dirección, teléfono, correo electrónico, datos de volumen que usted indique y el contenido de su mensaje. Los usamos para responderle, preparar una propuesta y llevar un registro de la solicitud.</li>
<li><strong>Registros del servidor.</strong> Nuestro proveedor de alojamiento, Cloudflare, procesa direcciones IP y metadatos de las solicitudes para entregar el sitio, protegerlo de abusos y producir estadísticas agregadas, conforme a su propia política de privacidad.</li>
<li><strong>Almacenamiento local.</strong> Una clave en su navegador registra que cerró el aviso de cookies. No contiene identificadores. Vea el <a href="/legal/cookies/">aviso de cookies</a>.</li>
</ul>
<p>No usamos rastreadores publicitarios, scripts de analítica ni píxeles de redes sociales. Los mosaicos del mapa se cargan desde servidores de Esri (ArcGIS Online) o de OpenStreetMap, que reciben su dirección IP al solicitarlos.</p>
<h2>3. Datos que tratamos en nuestra actividad</h2><p>Cuando una estación solicita afiliarse recogemos la información que el banco patrocinador y las redes de tarjetas exigen para evaluar un comercio: datos de la persona jurídica y RNC, licencias de operación, documentos de identidad y contacto de propietarios, directores y beneficiarios finales, cuenta bancaria para la liquidación y los datos de transacciones generados por la aceptación de tarjetas. Los tratamos para ejecutar el contrato de afiliación, cumplir obligaciones legales (incluida la Ley 155-17 contra el lavado de activos) y prevenir el fraude.</p>
<h2>4. Base legal y normativa aplicable</h2><p>Tratamos los datos de residentes dominicanos conforme a la Ley No. 172-13 de Protección de Datos Personales y, cuando aplique, la Ley No. 183-02 y los reglamentos de la Junta Monetaria y la Superintendencia de Bancos. Los datos de personas en Estados Unidos se tratan conforme a la legislación federal y estatal aplicable. Cuando la base sea el consentimiento, puede retirarlo en cualquier momento.</p>
<h2>5. Con quién compartimos</h2><p>Solo con el banco patrocinador y las redes de tarjetas, en la medida necesaria para prestar el servicio; con proveedores que actúan bajo nuestras instrucciones (alojamiento, envío de correo, gestión de terminales, verificación de identidad); con asesores profesionales; y con autoridades cuando la ley lo exija. No vendemos datos personales.</p>
<h2>6. Transferencias internacionales</h2><p>Bombero Partners está constituida en Estados Unidos y usa proveedores en la nube, por lo que los datos pueden tratarse fuera de la República Dominicana con salvaguardas contractuales y las medidas de seguridad descritas abajo.</p>
<h2>7. Conservación</h2><p>Las consultas del sitio se conservan hasta 24 meses. Los registros de comercios y transacciones se conservan durante los plazos que exigen las redes de tarjetas y la ley dominicana y estadounidense, en general al menos cinco años tras terminar la relación, o diez cuando lo exija la Ley 155-17.</p>
<h2>8. Seguridad</h2><p>Cifrado en tránsito y en reposo, control de acceso por roles, registro de actividad y diligencia sobre proveedores. Este sitio nunca almacena datos de tarjetas; las terminales del programa usan cifrado de punto a punto y operamos bajo PCI DSS.</p>
<h2>9. Sus derechos</h2><p>Puede solicitar acceso, rectificación, supresión o portabilidad de sus datos, y oponerse o limitar su tratamiento, escribiendo a <a href="mailto:{e}">{e}</a>. Respondemos dentro del plazo legal. También puede reclamar ante la autoridad competente.</p>
<h2>10. Menores</h2><p>Este sitio está dirigido a empresas y no a menores de 18 años.</p>
<h2>11. Cambios</h2><p>La fecha de arriba indica la última revisión. Los cambios sustanciales se destacarán en esta página.</p>
""")

def terms(ctx):
    e = ctx["CONTACT_EMAIL"]
    return _page("Legal", "Términos de uso", "Condiciones para el uso de este sitio web.", f"""
<h2>1. Aceptación</h2><p>Al usar este sitio acepta estos términos. Si no está de acuerdo, no lo utilice.</p>
<h2>2. Finalidad</h2><p>Este sitio presenta el programa de aceptación de tarjetas de Wallet Partners LLC para estaciones de combustible en la República Dominicana. Es informativo. Nada en él constituye una oferta de servicios bancarios o financieros, una invitación a invertir ni asesoría financiera, legal o fiscal. Las condiciones definitivas del servicio (comisión, alquiler de terminal y moneda de liquidación) se establecen únicamente en el contrato de afiliación aprobado por el banco patrocinador.</p>
<h2>3. Calculadoras y cifras</h2><p>Las calculadoras producen estimaciones a partir de los valores que usted introduce y no son cotizaciones. Las cifras de mercado se citan de fuentes públicas identificadas y pueden ser revisadas por sus autores. La información de estaciones proviene de listados públicos y puede cambiar.</p>
<h2>4. Sin relación bancaria</h2><p>Wallet Partners LLC no es un banco, no es un intermediario financiero autorizado en la República Dominicana y no es miembro de ninguna red de tarjetas por sí misma. Los servicios se prestarán solo cuando esté vigente un acuerdo de patrocinio con una entidad financiera miembro autorizada.</p>
<h2>5. Propiedad intelectual</h2><p>Textos, gráficos, código y el conjunto de datos de estaciones son © Wallet Partners LLC salvo indicación contraria. El mapa base es © Esri y colaboradores; los datos de OpenStreetMap son © sus colaboradores (ODbL). Las marcas de combustible pertenecen a sus titulares y se citan solo para identificar ubicaciones, sin implicar afiliación ni respaldo.</p>
<h2>6. Uso aceptable</h2><p>No intente acceder sin autorización al sitio o a su alojamiento, ni lo utilice para fines ilícitos. Los investigadores de seguridad deben seguir el proceso de <a href="/.well-known/security.txt">security.txt</a>.</p>
<h2>7. Enlaces a terceros</h2><p>Los enlaces a medios, reguladores y servicios de mapas se ofrecen por conveniencia. No controlamos ni respondemos por su contenido.</p>
<h2>8. Limitación de responsabilidad</h2><p>El sitio se ofrece "tal cual". En la medida que permita la ley, excluimos toda garantía y no respondemos por pérdidas derivadas del uso del sitio o de la confianza en su contenido.</p>
<h2>9. Ley aplicable</h2><p>Estos términos se rigen por las leyes del estado de constitución de Wallet Partners LLC, sin perjuicio de las normas imperativas de protección al consumidor de la Ley No. 358-05 para usuarios en la República Dominicana.</p>
<h2>10. Contacto</h2><p><a href="mailto:{e}">{e}</a></p>
""")

def cookies(ctx):
    return _page("Legal", "Aviso de cookies", "Este sitio usa muy pocas cookies. Esto es exactamente lo que guarda.", """
<h2>Lo que guardamos</h2>
<div class="table-wrap"><table><thead><tr><th>Nombre</th><th>Tipo</th><th>Finalidad</th><th>Duración</th></tr></thead><tbody>
<tr><td><span class="kbd">wp_cookie_notice</span></td><td>localStorage (no es una cookie)</td><td>Recuerda que cerró el aviso de cookies</td><td>Hasta que borre los datos del sitio</td></tr>
<tr><td><span class="kbd">__cf_bm</span>, <span class="kbd">cf_clearance</span> (solo si se activan)</td><td>Cookie de Cloudflare</td><td>Protección contra bots y desafíos de seguridad de la plataforma de alojamiento</td><td>Hasta 30 minutos / según Cloudflare</td></tr>
</tbody></table></div>
<h2>Lo que no usamos</h2><p>Ni cookies de analítica, ni de publicidad, ni complementos de redes sociales, ni rastreo entre sitios.</p>
<h2>Contenido de terceros</h2><p>El mapa interactivo carga mosaicos desde Esri (ArcGIS Online) o OpenStreetMap. Esas solicitudes revelan su dirección IP al proveedor, pero no colocan cookies en este sitio.</p>
<h2>Sus opciones</h2><p>Puede borrar o bloquear el almacenamiento local y las cookies en su navegador. El contenido del sitio no cambia; el aviso simplemente volverá a aparecer.</p>
""")

def compliance(ctx):
    return _page("Cumplimiento", "Marco de cumplimiento y regulación", "Cómo Wallet Partners LLC opera dentro de las reglas de las redes de tarjetas, la regulación financiera dominicana y la supervisión de un banco patrocinador. Esta página resume el programa; las políticas completas se comparten con bancos y reguladores bajo acuerdo de confidencialidad.", f"""
<div class="callout info"><p><strong>Estado.</strong> Bombero Partners está en prelanzamiento. Los controles descritos son los que estamos construyendo al estándar que exigirá el banco patrocinador y se validan antes de la primera transacción en vivo.</p></div>
<h2>1. Mapa regulatorio</h2>
<h3>República Dominicana</h3>
<ul>
<li><strong>Ley No. 183-02, Monetaria y Financiera</strong>, y el <strong>Reglamento de Sistemas de Pago (SIPARD)</strong> de la Junta Monetaria, modificado en agosto de 2025. El Banco Central supervisa el sistema de pagos; la adquirencia la realizan entidades de intermediación financiera supervisadas por la <strong>Superintendencia de Bancos</strong> o bajo su patrocinio. Bombero Partners operará como administrador de programa / facilitador de pagos bajo un banco miembro autorizado y registrará la entidad local que se requiera.</li>
<li><strong>Ley No. 155-17 contra el lavado de activos y el financiamiento del terrorismo</strong>, sus reglamentos y las guías de la Unidad de Análisis Financiero (UAF): debida diligencia de comercios, identificación de beneficiarios finales, monitoreo de transacciones, conservación de registros y reporte de operaciones sospechosas a través del banco patrocinador.</li>
<li><strong>Ley No. 172-13 de protección de datos personales</strong>: tratamiento lícito, medidas de seguridad y derechos de los titulares.</li>
<li><strong>Ley No. 358-05 de protección al consumidor</strong> (Pro Consumidor): precios transparentes, recibos y atención de reclamaciones en el punto de venta.</li>
<li><strong>Impuestos.</strong> Normas de la DGII sobre retenciones en pagos con tarjeta (Norma General 08-04 y sucesoras) y el régimen fiscal de los combustibles (Leyes 112-00 y 557-05, bajo el cual el combustible al detalle tributa impuestos selectivos y ad valorem en lugar de ITBIS). Los parámetros de retención para estaciones se confirman con el banco patrocinador y asesores fiscales antes del lanzamiento.</li>
<li><strong>Sector combustibles.</strong> Solo se afilian estaciones con resolución de operación vigente del MICM; la resolución y el registro en la DGII forman parte de cada expediente.</li>
</ul>
<h3>Estados Unidos e internacional</h3>
<ul>
<li><strong>Programa PLA/FT (Bank Secrecy Act)</strong> alineado con los requisitos del banco patrocinador y, cuando aplique, registro ante FinCEN; verificación de listas <strong>OFAC</strong> y otras sanciones para todos los comercios y beneficiarios finales.</li>
<li><strong>Reglas de las redes</strong> (Visa Core Rules y Mastercard Rules) para facilitadores de pago y comercios patrocinados, incluidas las categorías 5541 (estaciones de servicio) y 5542 (surtidores automáticos), las reglas de autorización y cierre para surtidores automáticos y las consultas a la lista MATCH.</li>
<li><strong>PCI DSS v4.0</strong> como proveedor de servicios nivel 1 al lanzamiento, con terminales de cifrado punto a punto (P2PE) para que ningún dato de tarjeta pase en claro por los sistemas de Bombero Partners.</li>
</ul>
<h2>2. Afiliación de comercios (KYB / KYC)</h2>
<ul><li>Verificación de la persona jurídica: documentos constitutivos, RNC, registro mercantil, resolución del MICM, comprobante de dirección y fotos del sitio.</li><li>Identificación de directores y beneficiarios finales con 10% o más; documentos de identidad; verificación de PEP, sanciones y noticias adversas.</li><li>Perfil financiero: volumen mensual esperado, ticket promedio, proporción de tarjeta presente; verificación de titularidad de la cuenta de liquidación.</li><li>Calificación de riesgo y flujo de aprobación: Bombero Partners prepara y recomienda; el banco aprueba, condiciona o rechaza. Actualización al menos cada dos años o ante eventos.</li></ul>
<h2>3. Monitoreo y fraude</h2>
<ul><li>Reglas para combustibles: límites de velocidad por tarjeta y por bomba, montos máximos coherentes con la capacidad del tanque, detección de duplicados, patrones nocturnos inusuales y pruebas de tarjetas.</li><li>Seguimiento del portafolio frente a los umbrales de contracargos y fraude de las redes; alertas tempranas al banco.</li><li>Escalamiento al área de cumplimiento del banco; reporte de operaciones sospechosas a la UAF y, cuando aplique, a FinCEN.</li></ul>
<h2>4. Fondos, liquidación y reservas</h2>
<ul><li>La liquidación de las redes la recibe el banco patrocinador en una cuenta del programa que controla. Bombero Partners no retiene fondos de comercios fuera de esa estructura.</li><li>Liquidación a comercios en dólares estadounidenses, con reservas y reglas de liberación acordadas con el banco por nivel de riesgo.</li><li>Conciliación diaria y reporte mensual al banco.</li></ul>
<h2>5. Seguridad de la información</h2>
<ul><li>Terminales P2PE validadas; tokenización; sin almacenamiento de PAN, banda ni CVV.</li><li>Entorno en la nube segmentado, cifrado en reposo, gestión de llaves con control dual, MFA para todo acceso administrativo, registro y alertas centralizados.</li><li>Pruebas de penetración anuales, gestión de vulnerabilidades, evaluación de proveedores y plan de respuesta a incidentes con plazos de notificación acordados con el banco y conforme a la Ley 172-13.</li><li>Divulgación coordinada de vulnerabilidades vía <a href="/.well-known/security.txt">security.txt</a>.</li></ul>
<h2>6. Gobierno</h2>
<ul><li>Oficial de cumplimiento designado; políticas de PLA/FT, sanciones, privacidad y seguridad aprobadas por la dirección; revisión independiente anual.</li><li>Capacitación de todo el personal y técnicos de campo.</li><li>Registros conservados al menos cinco años (diez cuando lo exija la Ley 155-17), disponibles para el banco y los reguladores; derecho de auditoría contractual del banco.</li><li>Reclamaciones de comercios atendidas según lo acordado con el banco y las normas de Pro Consumidor.</li></ul>
<h2>7. Documentos disponibles para bancos</h2>
<ul><li>Programa PLA/FT y evaluación de riesgos</li><li>Procedimiento de verificación de sanciones</li><li>Política de afiliación y plantilla de expediente</li><li>Reglas de monitoreo de transacciones (combustibles)</li><li>Políticas de seguridad de la información y plan PCI DSS</li><li>Programa de privacidad (Ley 172-13)</li><li>Planes de continuidad y de respuesta a incidentes</li><li>Borrador de términos de patrocinio y modelo de reservas</li></ul>
{sources_block(["ley_183", "jm_sipard", "sb_normativas"], "Referencias")}
""")

def notice(ctx):
    e = ctx["CONTACT_EMAIL"]
    return _page("Legal", "Aviso legal", "Identificación del operador del sitio y otras declaraciones.", f"""
<h2>Operador del sitio</h2><p><strong>Wallet Partners LLC</strong>, operando bajo el nombre comercial <strong>Bombero Partners</strong><br />Sociedad de responsabilidad limitada constituida bajo las leyes de Estados Unidos.<br />Correo: <a href="mailto:{e}">{e}</a></p>
<p>El agente registrado, el estado de constitución y el número de registro se facilitan a solicitud y se publicarán aquí al lanzamiento junto con los datos de la filial operativa dominicana.</p>
<h2>Situación regulatoria</h2><p>Wallet Partners LLC no es un banco, entidad de ahorro, remesadora ni intermediario financiero autorizado en la República Dominicana, y no es actualmente facilitador de pagos registrado ante ninguna red de tarjetas. Los servicios se prestarán únicamente bajo un acuerdo de patrocinio con una entidad financiera miembro autorizada, cuya identidad se indicará en el contrato de afiliación.</p>
<h2>Marcas</h2><p>"Bombero Partners" es un nombre comercial (DBA) de Wallet Partners LLC; el nombre y el logotipo son propiedad de Wallet Partners LLC. TotalEnergies, Shell, Texaco, Next, Axxon, Tropigás, Sigma, VP Racing, Óptimo Gas, Trovasa, Visa, Mastercard, CardNET, AZUL, Visanet y otros nombres pertenecen a sus titulares y se citan solo para identificar ubicaciones y participantes del mercado, sin implicar patrocinio, afiliación ni respaldo.</p>
<h2>Contenido e imágenes</h2><p>Los datos de estaciones se compilaron de listados públicos el {ctx['DATA_DATE']}. Las fotografías del sitio son ilustraciones generadas por computadora y no representan estaciones, personas ni marcas concretas. Mapa base © Esri y colaboradores; datos de OpenStreetMap © sus colaboradores (ODbL).</p>
<h2>Alojamiento</h2><p>Este sitio se sirve a través de Cloudflare, Inc.</p>
""")

def accessibility(ctx):
    e = ctx["CONTACT_EMAIL"]
    return _page("Legal", "Declaración de accesibilidad", "Queremos que cualquier propietario de estación o aliado pueda usar este sitio.", f"""
<p>Wallet Partners LLC procura cumplir las Pautas de Accesibilidad para el Contenido Web (WCAG) 2.2 en el nivel AA. Medidas adoptadas:</p>
<ul><li>HTML semántico con enlace para saltar al contenido, regiones y jerarquía lógica de encabezados.</li><li>Navegación, filtros y formularios operables con teclado; foco visible.</li><li>Contraste de texto igual o superior a 4.5:1; la información nunca depende solo del color (los marcadores llevan número; los gráficos tienen vista de tabla).</li><li>Texto alternativo en las imágenes; las decorativas se marcan como tales.</li><li>El mapa tiene nombre accesible y una lista equivalente.</li><li>Sin movimiento que no pueda pausarse; sin medios de reproducción automática.</li></ul>
<h2>Limitaciones conocidas</h2><p>El mapa interactivo usa una biblioteca de terceros (Leaflet); el desplazamiento con teclado puede ser limitado en algunos navegadores. La lista de estaciones bajo el mapa ofrece la misma información.</p>
<h2>Comentarios</h2><p>Si encuentra una barrera, escriba a <a href="mailto:{e}">{e}</a> y responderemos en cinco días hábiles.</p>
""")

def notfound(ctx):
    return """
<section><div class="wrap center" style="padding:60px 20px">
  <span class="eyebrow">404</span>
  <h1>Página no encontrada</h1>
  <p class="muted">La página que buscaba no existe o cambió de dirección. <span lang="en">The page you requested does not exist.</span></p>
  <div class="hero-actions" style="justify-content:center"><a class="btn btn-navy" href="/">Ir al inicio</a><a class="btn btn-outline" href="/afiliese/">Afilie su estación</a><a class="btn btn-outline" href="/en/" lang="en">English</a></div>
</div></section>
"""
