#!/usr/bin/env python3
"""Draw docs/how-it-works-en.svg and docs/how-it-works-es.svg.

Usage (from docs/src): python3 how_it_works.py
Same palette as the other images (demo.html, results.html). Plain SVG, system fonts,
so it renders the same on GitHub as anywhere else.
"""
import pathlib
from html import escape

BG, CARD, LINE, TEXT, DIM, FAINT = "#050810", "#0b1120", "#1a2338", "#f3f6fc", "#b5bfd0", "#6b7a90"
CYAN, MAG, GREEN, BLUE = "#00e5ff", "#ff2dcd", "#4ade80", "#5da9ff"

T = {
    "en": {
        "title": "humanizer-es: how it works",
        "desc": "A Spanish text goes in. The skill marks AI tells, strongest first. No tells means a person wrote it: "
                "fix clear typos and stop. Otherwise it drafts by deleting tells, never adding a fact, audits every "
                "claim against the original, and writes the final version. An optional second opinion from another "
                "model runs only with permission. Out comes the rewrite with a note on what changed. A separate "
                "regex checker scores texts out of 5, offline.",
        "sub": "Make AI-written Spanish sound like you, without changing what it says.",
        "cards": [
            ("1 · INPUT", "Your text", ["An email, a caption,", "a job post, a reply"], "/humanizer-es"),
            ("2 · WHO WROTE IT", "Marks the tells", ["Strongest first:", "theatre, calques,", "rhythm, inflation"], "SKILL.md · A to F"),
            ("3 · DRAFT", "Cuts, never adds", ["Delete the tell. Gap?", "Use a fact already", "in the text."], "step 2"),
            ("4 · AUDIT", "Checks every fact", ["Same scope, same", "strength, same", "promises."], "step 3"),
            ("5 · OUT", "Rewrite + note", ["The version on top,", "what changed below."], "copy and send"),
        ],
        "branch": "No tells: a person wrote it. Fix clear typos and stop.",
        "boxes": [
            ("CHECKER", "deslop-es", ["Regex, offline, free. Scores a text out of 5.", "137 fixture tests run in CI."], "tools/deslop_es.py", False),
            ("OPTIONAL", "Second opinion", ["Another model rereads the final version.", "Asks before sending anything."], "step 5", True),
            ("PROOF", "Blind test", ["Ranked 1st of 6, judged by Claude and GPT.", "0 invented facts in 180 verdicts."], "evals/README.md", False),
        ],
    },
    "es": {
        "title": "humanizer-es: cómo funciona",
        "desc": "Entra un texto en español. La skill marca las señales de IA, de la más fuerte a la más débil. Si no hay "
                "ninguna, lo escribió una persona: corrige erratas claras y para. Si las hay, escribe un borrador "
                "borrando marcas sin agregar datos, compara cada afirmación con el original y escribe la versión "
                "final. Una segunda opinión de otro modelo es opcional y solo con permiso. Sale la versión nueva con "
                "una nota de lo que cambió. Aparte, un revisor con patrones le pone puntaje sobre 5, sin internet.",
        "sub": "Que tu español escrito con IA suene a ti, sin cambiar lo que dice.",
        "cards": [
            ("1 · ENTRADA", "Tu texto", ["Un correo, un caption,", "un aviso, una respuesta"], "/humanizer-es"),
            ("2 · QUIÉN LO ESCRIBIÓ", "Marca las señales", ["De la más fuerte:", "teatro, calcos,", "ritmo, inflado"], "SKILL.md · A a F"),
            ("3 · BORRADOR", "Borra, no agrega", ["Borra la marca. ¿Hueco?", "Usa un dato que ya", "está en el texto."], "paso 2"),
            ("4 · REVISIÓN", "Revisa cada dato", ["Mismo alcance, misma", "fuerza, mismas", "promesas."], "paso 3"),
            ("5 · SALIDA", "Versión + nota", ["La versión arriba,", "lo que cambió abajo."], "copiar y enviar"),
        ],
        "branch": "Sin señales: lo escribió una persona. Corrige erratas claras y para.",
        "boxes": [
            ("REVISOR", "deslop-es", ["Patrones, sin internet, gratis. Puntaje sobre 5.", "137 pruebas corren en CI."], "tools/deslop_es.py", False),
            ("OPCIONAL", "Segunda opinión", ["Otro modelo relee la versión final.", "Pregunta antes de enviar nada."], "paso 5", True),
            ("PRUEBA", "A ciegas", ["Primera de 6, con jueces Claude y GPT.", "0 datos inventados en 180 evaluaciones."], "evals/README.md", False),
        ],
    },
}

W, H = 1200, 590
CX = [48, 274, 500, 726, 952]  # five cards, 200 wide, 26 apart
CW, CY, CH = 200, 130, 200
SANS = "-apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif"


def svg(lang):
    t = T[lang]
    o = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" font-family="{SANS}">',
         f"  <title>{escape(t['title'])}</title>",
         f"  <desc>{escape(t['desc'])}</desc>",
         "  <defs>",
         '    <marker id="a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto-start-reverse">',
         f'      <path d="M0,0 L10,5 L0,10 z" fill="{FAINT}"/></marker>',
         '    <marker id="g" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto-start-reverse">',
         f'      <path d="M0,0 L10,5 L0,10 z" fill="{GREEN}"/></marker>',
         "    <style>",
         f"      .card {{ fill: {CARD}; stroke: {LINE}; stroke-width: 1.5; }}",
         f"      .step {{ font-size: 11.5px; font-weight: 700; letter-spacing: 1.2px; fill: {CYAN}; }}",
         f"      .h {{ font-size: 18px; font-weight: 700; fill: {TEXT}; }}",
         f"      .t {{ font-size: 13.5px; fill: {DIM}; }}",
         f"      .mono {{ font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace; font-size: 12px; fill: {FAINT}; }}",
         f"      .line {{ stroke: {FAINT}; stroke-width: 2; fill: none; }}",
         "    </style>",
         "  </defs>",
         f'  <rect width="{W}" height="{H}" rx="20" fill="{BG}"/>',
         f'  <text x="48" y="62" font-size="32" font-weight="800" fill="{TEXT}">humanizer-es</text>',
         f'  <text x="48" y="92" font-size="17" fill="{DIM}">{escape(t["sub"])}</text>']

    for i, (step, head, lines, mono) in enumerate(t["cards"]):
        x = CX[i]
        accent = MAG if i in (1, 2) else (GREEN if i == 4 else CYAN)
        o.append(f'  <rect class="card" x="{x}" y="{CY}" width="{CW}" height="{CH}" rx="14"/>')
        o.append(f'  <rect x="{x}" y="{CY}" width="{CW}" height="4" rx="2" fill="{accent}"/>')
        o.append(f'  <text class="step" x="{x + 18}" y="{CY + 34}">{escape(step)}</text>')
        o.append(f'  <text class="h" x="{x + 18}" y="{CY + 62}">{escape(head)}</text>')
        for j, line in enumerate(lines):
            o.append(f'  <text class="t" x="{x + 18}" y="{CY + 92 + j * 20}">{escape(line)}</text>')
        o.append(f'  <text class="mono" x="{x + 18}" y="{CY + CH - 20}">{escape(mono)}</text>')
        if i < 4:
            o.append(f'  <path class="line" d="M{x + CW + 2} {CY + CH / 2} H{CX[i + 1] - 4}" marker-end="url(#a)"/>')

    # person-written branch: from card 2 down, along, up into card 5
    by = CY + CH + 52
    x2, x5 = CX[1] + CW / 2, CX[4] + CW / 2
    o.append(f'  <path d="M{x2} {CY + CH + 2} V{by} H{x5} V{CY + CH + 6}" fill="none" stroke="{GREEN}" '
             f'stroke-width="2" stroke-dasharray="6 5" marker-end="url(#g)"/>')
    o.append(f'  <rect x="{x2 + 40}" y="{by - 16}" width="{x5 - x2 - 80}" height="32" rx="16" fill="{BG}" stroke="{GREEN}" stroke-width="1.5"/>')
    o.append(f'  <text x="{(x2 + x5) / 2}" y="{by + 5}" text-anchor="middle" font-size="14" font-weight="600" fill="{GREEN}">{escape(t["branch"])}</text>')

    bw, gap, y0, bh = 350, 27, 425, 130
    for k, (label, head, lines, mono, dashed) in enumerate(t["boxes"]):
        x = 48 + k * (bw + gap)
        stroke = f'stroke="{BLUE}" stroke-dasharray="6 5"' if dashed else f'stroke="{LINE}"'
        o.append(f'  <rect x="{x}" y="{y0}" width="{bw}" height="{bh}" rx="14" fill="{CARD}" {stroke} stroke-width="1.5"/>')
        o.append(f'  <text class="step" x="{x + 20}" y="{y0 + 30}" style="fill:{BLUE if dashed else CYAN}">{escape(label)}</text>')
        o.append(f'  <text class="h" x="{x + 20}" y="{y0 + 56}">{escape(head)}</text>')
        for j, line in enumerate(lines):
            o.append(f'  <text class="t" x="{x + 20}" y="{y0 + 82 + j * 20}">{escape(line)}</text>')
        o.append(f'  <text class="mono" x="{x + bw - 20}" y="{y0 + 30}" text-anchor="end">{escape(mono)}</text>')

    o.append("</svg>")
    return "\n".join(o) + "\n"


if __name__ == "__main__":
    out = pathlib.Path(__file__).resolve().parents[1]
    for lang in T:
        (out / f"how-it-works-{lang}.svg").write_text(svg(lang))
        print(out / f"how-it-works-{lang}.svg")
