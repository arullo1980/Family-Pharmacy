from common import icon

def body(ctx):
    return f"""
<div class="page-title"><div class="wrap"><span class="eyebrow">Nosotros</span><h1>Bombero Partners</h1><p>El nombre comercial de Wallet Partners LLC en la República Dominicana: una empresa de pagos con un solo objetivo: que las estaciones de combustible de la República Dominicana acepten tarjetas en condiciones que se ajusten a su negocio.</p></div></div>
<section><div class="wrap split">
  <div>
    <h2>Por qué existimos</h2>
    <p>Las estaciones de gasolina están entre los comercios de mayor volumen de cualquier economía y, sin embargo, se les atiende con las mismas terminales, los mismos precios y el mismo soporte que a un colmado. En 2026 esa contradicción se volvió noticia nacional cuando el gremio de detallistas amenazó con dejar de aceptar tarjetas.</p>
    <p>Bombero Partners nació para construir el programa especializado que el sector lleva años pidiendo: una comisión 25 puntos básicos por debajo del contrato actual, sin mínimo mensual, equipo para el patio, liquidación en dólares y soporte local, operado como facilitador de pagos bajo un banco patrocinador autorizado.</p>
    <h2>Cómo trabajamos</h2>
    <ul class="checklist"><li><strong>Un solo sector, a fondo.</strong> Combustibles primero; nada más hasta hacerlo bien.</li><li><strong>Controles de nivel bancario desde el primer día.</strong> Nuestro modelo asume que los auditores del banco están en la sala.</li><li><strong>Transparencia con el comercio.</strong> Estados de cuenta que el dueño puede verificar contra el aviso semanal del MICM.</li><li><strong>Presencia local.</strong> Instalación, capacitación y soporte en Santo Domingo, en español.</li></ul>
  </div>
  <figure><picture><source srcset="/assets/img/hero-station.webp" type="image/webp" /><img src="/assets/img/hero-station.jpg" alt="Estación de combustible moderna en una avenida al atardecer" loading="lazy" width="1280" height="720" /></picture><figcaption>Imagen ilustrativa.</figcaption></figure>
</div></section>
<section class="alt"><div class="wrap"><div class="grid grid-3">
  <div class="card">{icon("doc")}<h3>Entidad</h3><p>Bombero Partners es un nombre comercial (DBA) de Wallet Partners LLC, sociedad de responsabilidad limitada constituida en Estados Unidos. Las operaciones en el país se realizan a través de una filial registrada localmente según lo exija la estructura de patrocinio y la ley dominicana.</p></div>
  <div class="card">{icon("map")}<h3>Mercado</h3><p>República Dominicana, empezando por el Polígono Central de Santo Domingo y ampliando al resto del Distrito Nacional y Santiago.</p></div>
  <div class="card">{icon("shield")}<h3>Estado</h3><p>Prelanzamiento. Estamos seleccionando el banco patrocinador y registrando las estaciones de la primera ola. Bombero Partners no es un banco y no retiene fondos de los comercios fuera de la cuenta del programa controlada por el banco.</p></div>
</div></div></section>
"""
