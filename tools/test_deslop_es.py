#!/usr/bin/env python3
"""Fixtures for deslop_es. Run: python3 tools/test_deslop_es.py

Each rule has text it must catch and normal Chilean text it must leave alone. Widening a
rule is easy; the must-not-match lines are what keep it honest.
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from deslop_es import audit, score

# (category, must match, must not match)
CASES = [
    # puntuación
    ("formato", "La entrega es el viernes — sin falta.", "Atendemos de 9–18 h, de lunes a viernes."),
    ("formato", "El precio – como te dije – no cambia.", "El precio, como te dije, no cambia."),
    ("formato", "# Cómo Usar La IA en tu Negocio", "# Cómo usar la IA en tu negocio"),
    ("formato", "**Asunto:** Actualización Sobre Tu Pedido", "**Asunto:** Actualización sobre tu pedido"),
    ("formato", "## Nuestros Servicios Profesionales", "## Servicios en la Región Metropolitana"),
    # estructuras
    ("estructuras", "La IA no es solo una herramienta, es una revolución.", "No solo hacemos tortas, sino también kuchenes."),
    ("estructuras", "En Panadería Doña Rosa no solo horneamos pan, creamos experiencias.", "No solo vino Ana, vino también su hermana."),
    ("estructuras", "No se trata de vender más, se trata de vender mejor.", "No se trata de un error del sistema."),
    ("estructuras", "No es magia. Es método.", "No es necesario que vengas. Te mando el archivo."),
    ("estructuras", "Sin contratos. Sin letra chica. Solo resultados.", "Sin contrato, el arriendo sale más caro."),
    ("estructuras", "¿El resultado? Ventas que suben.", "¿El pedido llegó bien? Avísame."),
    ("estructuras", "Ordena tus finanzas.\nPiénsalo.", "Piénsalo con calma y me avisas el lunes."),
    ("estructuras", "Renovamos la bodega, garantizando entregas más rápidas.", "Estamos garantizando el stock hasta el viernes."),
    ("estructuras", "Lanzamos el portal, permitiendo que más pymes vendan en línea.", "El portal permite que más pymes vendan en línea."),
    # muletillas
    ("muletillas", "Cabe destacar que el plazo vence el lunes.", "El plazo vence el lunes."),
    ("muletillas", "Es importante mencionar que no hay reembolso.", "Es importante que traigas tu carnet."),
    ("muletillas", "Sin lugar a dudas, es el mejor café del barrio.", "Sin duda nos vemos el jueves."),
    ("muletillas", "En el mundo actual, todo pasa por redes.", "En el mundial de 2014 cerramos temprano."),
    ("muletillas", "En la era digital, tu web es tu vitrina.", "En la era de los dinosaurios no había internet."),
    ("muletillas", "Este curso marca un antes y un después.", "Antes y después de la mudanza revisamos todo."),
    ("muletillas", "La logística juega un papel clave en tu negocio.", "Juega fútbol los sábados."),
    ("muletillas", "Lamentamos los inconvenientes que esto pueda causar.", "Lamentamos el atraso; llega el martes."),
    ("muletillas", "Espero que este correo te encuentre bien.", "Espero que estés bien."),
    ("muletillas", "No dudes en contactarnos si tienes preguntas.", "Si tienes preguntas, escríbeme."),
    ("muletillas", "Queremos llevar tu marca al siguiente nivel.", "El taller está en el siguiente piso."),
    # léxico
    ("léxico", "Sumérgete en el mundo del café de especialidad.", "Me sumergí en la piscina."),
    ("léxico", "Desbloquea tu potencial con nuestro curso.", "Desbloqueé el celular con la huella."),
    ("léxico", "Eleva tu negocio con nuestra asesoría.", "El precio se eleva en diciembre."),
    ("léxico", "Te ayudamos a potenciar tu marca.", "La potencia del motor es de 200 W."),
    ("léxico", "Un barrio vibrante y lleno de vida.", "Un barrio tranquilo y lleno de vida."),
    ("léxico", "Ofrecemos una solución integral para tu empresa.", "Tenemos pan integral y de molde."),
    ("léxico", "Buscamos generar sinergia entre equipos.", "Buscamos que los equipos trabajen juntos."),
    ("léxico", "Brindamos un servicio de calidad.", "Brindamos por los novios a las doce."),
    ("léxico", "Eso no hace sentido para el cliente.", "Eso no tiene sentido para el cliente."),
    ("léxico", "Es hora de tomar acción.", "Es hora de actuar."),
    ("léxico", "Al final del día, lo que importa es el cliente.", "Al final del día cerramos la caja."),
    ("léxico", "Lo calculamos de acuerdo a la tabla.", "Lo calculamos según la tabla."),
    ("léxico", "Puedes aplicar a este cargo hasta el viernes.", "Puedes postular a este cargo hasta el viernes."),
    ("léxico", "El estudio fue realizado por nuestro equipo.", "El estudio lo hizo nuestro equipo."),
    # redes
    ("redes", "¿Qué opinas? 👇", "¿Qué opinas del local nuevo?"),
    ("redes", "¡Te leo en los comentarios!", "Te leo mañana con calma."),
    ("redes", "Me complace anunciar que me uno a Acme.", "Les cuento que me uno a Acme."),
    ("redes", "Café rico #cafe #santiago #chile #barista #ñuñoa #especialidad", "Café rico #cafe #santiago #ñuñoa"),
    ("formato", "Lo que incluye:\n✅ Diseño\n✅ Hosting\n✅ Soporte", "Lo que incluye: diseño, hosting y soporte. ✅"),
    ("formato", "### ✅ Diseño\n### 🚀 Hosting\n### 💬 Soporte", "### Diseño\n### Hosting\n### Soporte"),
    ("formato", "- **Plazo:** 2 semanas\n- **Precio:** $300.000\n- **Pago:** 50% al inicio", "- Plazo: 2 semanas\n- Precio: $300.000\n- Pago: 50% al inicio"),
    ("léxico", "Gracias por su tiempo y consideración.", "Gracias por su tiempo."),
    ("léxico", "Espero que estés teniendo un buen mes.", "Espero que estés bien. Estamos teniendo problemas con el envío."),
    ("léxico", "Queremos informaros de que el local cierra.", "Queremos informarles que el local cierra."),
    ("léxico", "¿Habéis probado el nuevo menú?", "¿Han probado el nuevo menú?"),
    ("léxico", "El coste del envío es de $3.000.", "El costo del envío es de $3.000."),
    ("léxico", "Te mando el link al móvil.", "La web se ve bien en dispositivos móviles."),
    ("léxico", "Gracias por todo.\nUn saludo,\nCarla", "Gracias por todo. Les mando un saludo a todos.\nSaludos,\nCarla"),
    ("estructuras", "La buena noticia es que ya tenemos fecha.", "La noticia es buena: ya tenemos fecha."),
    ("estructuras", "Esto es lo que aprendí en diez años de oficio:", "Aprendí harto en diez años de oficio."),
]

DEMO = ("En el mundo actual, la IA no es solo una herramienta, es una revolución. Sumérgete en este "
        "fascinante viaje: cabe destacar que potenciar tu negocio nunca fue tan crucial. ¿El resultado? "
        "Eficiencia, innovación y crecimiento. Piénsalo.")

fails = []
for cat, bad, good in CASES:
    if not audit(bad)[cat]:
        fails.append(f"MISSED [{cat}] {bad!r}")
    hit = {k: v for k, v in audit(good).items() if v and k != "notas"}
    if hit:
        fails.append(f"FALSE ALARM {hit} on {good!r}")

# the 6 Nov paragraph SlopMonster scored 5/5 clean
if score(audit(DEMO)) > 2:
    fails.append(f"demo paragraph scored {score(audit(DEMO))}/5, expected 2 or lower")

# ¿ and ¡ left out are notes, never points
h = audit("hola, cómo estás? te mando el archivo altiro!")
if score(h) != 5 or not h["notas"]:
    fails.append("missing ¿¡ should be a note and cost no points")
if audit("¿Viste el link https://ejemplo.cl/?q=1 que te mandé?")["notas"]:
    fails.append("URL query string counted as a question")

# front matter is not text
if score(audit("---\nfacts: \"a — b\"\n---\nHola, nos vemos el lunes.")) != 5:
    fails.append("front matter was scanned")

print("\n".join(fails) if fails else f"all {len(CASES) * 2 + 5} checks pass")
sys.exit(1 if fails else 0)
