#!/usr/bin/env python3
"""deslop-es: flags the hard AI tells in Spanish text. It reports, it never rewrites.

Five categories, one point each, so a clean text scores 5/5:
  formato      rayas (— –), títulos en mayúsculas a la inglesa, negrita-etiqueta en cada viñeta, emojis como viñetas
(¿ and ¡ left out are listed as notes, not scored: Chilean informal writing drops them.)
  estructuras  "no es solo X, es Y", "Sin X. Sin Y.", "¿El resultado?", cierres de una línea, gerundio colgado
  muletillas   bisagras vacías, aperturas de época, importancia inflada, guion de servicio, relleno de cortesía
  léxico       palabras de IA, calcos del inglés, español de España en un texto para Chile (vosotros, coste, "Un saludo")
  redes        cebo de comentarios, anuncios "me complace", más de cinco hashtags

Hard rules only: each one is a pattern a person in Chile almost never writes. A clean score
means none of these tells, not that the text is good; read it anyway.

Usage:
  python3 tools/deslop_es.py archivo.md [más.md ...]
  python3 tools/deslop_es.py --text "En el mundo actual…"
  cat texto.txt | python3 tools/deslop_es.py
  --json for machine output. Exit code 1 if any file scores below 5.
Standard library only. No network.
"""
import argparse, json, re, sys

W = r"[\wáéíóúüñÁÉÍÓÚÜÑ]"          # a Spanish word character
NW = r"(?<![\wáéíóúüñÁÉÍÓÚÜÑ])"     # start of word
EW = r"(?![\wáéíóúüñÁÉÍÓÚÜÑ])"      # end of word


def rx(p):
    return re.compile(p, re.I)


# ── léxico ──────────────────────────────────────────────────────────────────
LEXICO = [
    (rx(NW + r"(sumérge(te|nos)|sumergirte|sumergirnos|sumérjase|adéntra(te|nos)|adentrarte|adentrarnos)" + EW), "sumérgete / adéntrate"),
    (rx(NW + r"desbloque(a|ar|ará|amos|e)\s+(tu|su|todo|el|nuevas?)" + EW), "desbloquea tu…"),
    (rx(NW + r"(eleva|elevar|elevamos|elevará|eleve)\s+(tu|tus|su|sus|al?|la|el|los|las)\s+(\w+\s+)?(nivel|negocio|marca|experiencia|estrategia|productividad|carrera|juego)" + EW), "eleva tu…"),
    (rx(NW + r"(potenci(ar|amos|ará|ando|e|en)|potencia\s+(tu|tus|su|sus))" + EW), "potenciar"),
    (rx(NW + r"(fascinantes?|vibrantes?)" + EW), "fascinante / vibrante"),
    (rx(NW + r"(solución|soluciones|enfoque|servicio|servicios|visión|manera|forma|experiencia)\s+integral(es)?" + EW), "… integral"),
    (rx(NW + r"sinergias?" + EW), "sinergia"),
    (rx(NW + r"brind(ar|amos|a|an|ará|ando|e|en|ado|ada)\s+(un|una|unos|unas|el|la|los|las|apoyo|soluciones?|servicios?|atención|información|herramientas|experiencias?|acompañamiento|asesoría)" + EW), "brindar (por dar / ofrecer)"),
    (rx(NW + r"(un|es un|es todo un)\s+testimonio\s+de" + EW), "un testimonio de"),
    (rx(NW + r"(hace|hacer|hacen|hizo|haga)\s+sentido" + EW), "calco: hacer sentido"),
    (rx(NW + r"(tomar|toma|tomemos|tomamos|tomen|tome)\s+acción" + EW), "calco: tomar acción"),
    (rx(NW + r"al\s+final\s+del\s+día\s*,"), "calco: al final del día, (figurado)"),
    (rx(NW + r"en\s+adición\s+a" + EW), "calco: en adición a"),
    (rx(NW + r"de\s+acuerdo\s+a" + EW), "calco: de acuerdo a (es «de acuerdo con» / «según»)"),
    (rx(NW + r"(aplic(ar|o|é|aste|ó|amos|aron|ando|a)|apliqué)\s+(a|al|para)\s+(un|una|el|la|este|esta|ese|esa)?\s*(cargo|puesto|trabajo|empleo|vacante|beca|posición)" + EW), "calco: aplicar a un cargo (es «postular»)"),
    (rx(NW + r"(fue|fueron|ha sido|han sido)\s+realizad[oa]s?\s+por" + EW), "pasiva: fue realizado por"),
    (rx(NW + r"(su|tu)\s+tiempo\s+y\s+consideración" + EW), "calco: gracias por su tiempo y consideración"),
    (rx(NW + r"(estés|esté|estén|estemos)\s+teniendo" + EW), "calco: que estés teniendo (un buen mes)"),
    (rx(NW + r"(os|vosotr[oa]s|vuestr[oa]s?|habéis|[\wáéíóúñ]{2,}(áis|éis)|(avis|inform|ofrec|atend|ayud|esper|escrib|cont)(ar|er|ir)os)" + EW), "España: vosotros"),
    (rx(NW + r"(costes?|ordenador(es)?|enhorabuena|sentimos\s+las\s+molestias|avisar(te|le|les)\s+de\s+que|(el|tu|su|al|del)\s+móvil)" + EW), "España: coste / móvil / ordenador"),
    (re.compile(r"^\s*Un\s+saludo(\s+cordial)?\s*,?\s*$", re.M | re.I), "España: «Un saludo» como despedida (en Chile, «Saludos»)"),
]

# ── muletillas ──────────────────────────────────────────────────────────────
MULETILLAS = [
    (rx(NW + r"cabe\s+(destacar|mencionar|señalar|resaltar|recalcar)" + EW), "bisagra: cabe destacar"),
    (rx(NW + r"es\s+(importante|fundamental|crucial|clave)\s+(destacar|mencionar|señalar|resaltar|recalcar)" + EW), "bisagra: es importante mencionar"),
    (rx(NW + r"sin\s+(lugar\s+a\s+dudas?|duda\s+alguna)" + EW), "bisagra: sin lugar a dudas"),
    (rx(NW + r"(por\s+)?último,?\s+pero\s+no\s+menos\s+importante" + EW), "bisagra: último pero no menos importante"),
    (rx(NW + r"en\s+(el|este)\s+mundo\s+(actual|de\s+hoy|moderno|digital|globalizado|interconectado)" + EW), "época: en el mundo actual"),
    (rx(NW + r"en\s+(la|esta)\s+era\s+(digital|actual|moderna|de\s+la\s+(IA|inteligencia\s+artificial|información))" + EW), "época: en la era digital"),
    (rx(NW + r"en\s+el\s+(panorama|contexto|escenario)\s+actual" + EW), "época: en el panorama actual"),
    (rx(NW + r"en\s+un\s+mundo\s+(cada\s+vez\s+más|en\s+constante|donde\s+la\s+(tecnología|IA))" + EW), "época: en un mundo cada vez más…"),
    (rx(NW + r"hoy\s+más\s+que\s+nunca" + EW), "época: hoy más que nunca"),
    (rx(NW + r"(marca|marcan|marcar|marcará|marcó|marcando)\s+un\s+antes\s+y\s+un\s+después" + EW), "inflado: marca un antes y un después"),
    (rx(NW + r"(juega|juegan|jugar|jugará|desempeña|desempeñan)\s+un\s+(papel|rol)\s+(clave|fundamental|crucial|esencial|vital|protagónico|determinante)" + EW), "inflado: juega un papel clave"),
    (rx(NW + r"(cambia|cambian|cambiar|cambiará|cambiando)\s+las\s+reglas\s+del\s+juego" + EW), "inflado: cambia las reglas del juego"),
    (rx(NW + r"(llev(ar|a|e|amos|ará|arlo|arla|arte|ando))\s+(\w+\s+){0,3}al\s+(siguiente|próximo|otro)\s+nivel" + EW), "inflado: al siguiente nivel"),
    (rx(NW + r"entiendo\s+(perfectamente|completamente|totalmente)\s+(tu|su)\s+(preocupación|frustración|molestia|situación)" + EW), "servicio: entiendo perfectamente tu preocupación"),
    (rx(NW + r"(estamos|seguimos)\s+trabajando\s+(arduamente|incansablemente|sin\s+descanso)" + EW), "servicio: trabajando arduamente"),
    (rx(NW + r"lamentamos\s+(profundamente\s+|sinceramente\s+)?(los|cualquier|todo)\s+(inconvenientes?|molestias?)" + EW), "servicio: lamentamos los inconvenientes"),
    (rx(NW + r"agradecemos\s+(tu|su)\s+(paciencia|comprensión)\s+y\s+(comprensión|paciencia)" + EW), "servicio: agradecemos tu paciencia y comprensión"),
    (rx(NW + r"espero\s+que\s+(este|el)\s+(correo|mensaje|email)\s+(te|le|les|los)\s+encuentre\s+bien" + EW), "cortesía: espero que este correo te encuentre bien"),
    (rx(NW + r"quería\s+tomarme\s+un\s+momento" + EW), "cortesía: quería tomarme un momento"),
    (rx(NW + r"no\s+(dudes|dude|duden)\s+en\s+(contact|escrib|consult|comunic|pregunt|llam|hac)\w*"), "cortesía: no dudes en contactarme"),
]

# ── estructuras ─────────────────────────────────────────────────────────────
GER = r"(garantizando|permitiendo|logrando|asegurando|brindando|ofreciendo|impulsando|fomentando|potenciando|consolidando|posicionando|contribuyendo|facilitando|optimizando|maximizando|aportando|transformando)"
CLOSERS = r"(Piénsalo|Piénsenlo|Así\s+de\s+(simple|fácil|claro|sencillo)|Y\s+eso\s+lo\s+cambia\s+todo|Eso\s+lo\s+cambia\s+todo|Punto|Sin\s+más|Ni\s+más\s+ni\s+menos|Spoiler|Y\s+funciona|Hablemos)"
ESTRUCTURAS = [
    (rx(NW + r"no\s+((?:es|son|era|fue|será)\s+)?(solo|sólo|simplemente|únicamente|solamente)" + EW + r"\s+(" + W + r"+)[^.!?\n]{0,90}?[,;:]\s*(?!(?:sino|tambi[eé]n|adem[aá]s)\b)(" + W + r"+)(?![^.!?\n]*\b(?:tambi[eé]n|adem[aá]s)\b)" + EW), "no es solo X, es Y"),
    (rx(NW + r"no\s+se\s+trata\s+(solo\s+|sólo\s+|simplemente\s+)?de" + EW + r"[^.!?\n]{1,90}?(,|;|\.)\s*(se\s+trata\s+de|sino\s+de|sino\s+que|sino|se\s+trata)" + EW), "no se trata de X, sino de Y"),
    (re.compile(NW + r"No\s+(es|son)\s+[^.!?\n]{1,40}\.\s+(Es|Son)" + EW), "No es X. Es Y."),
    (re.compile(NW + r"Sin\s+[^.!?\n]{1,35}\.\s+Sin\s+[^.!?\n]{1,35}\."), "Sin X. Sin Y."),
    (rx(r"¿\s*(y\s+)?(el|la|lo|los|las)\s+(\w+)(\s+\w+)?\?(?=\s+\S)"), "pregunta que se responde sola: ¿El resultado?"),
    (rx(r"¿\s*(por\s+qué|cómo|qué\s+significa\s+esto)\s*\?(?=\s+\S)"), "pregunta que se responde sola: ¿Por qué?"),
    (re.compile(r"(?:^|(?<=[.!?\n]))\s*" + CLOSERS + r"[.!]\s*(?=$|\n)", re.M), "cierre de una línea: Piénsalo."),
    (rx(NW + r"(la\s+buena\s+noticia\s+es\s+que|esto\s+(es|fue)\s+lo\s+que\s+(aprend|descubr)\w*|me\s+quedo\s+con\s+esto\s*:|lo\s+que\s+(nos|me)\s+dejó[^.:\n]{0,30}:)"), "revelación anunciada: la buena noticia es que…"),
    (rx(r",\s+" + GER + EW + r"[^.!?\n]{0,120}[.!?]?\s*$"), "gerundio colgado al final: …, garantizando"),
]

# ── redes ───────────────────────────────────────────────────────────────────
REDES = [
    (rx(r"te\s+leo\s+en\s+(los\s+)?comentarios|d[ée]jame\s+(tu\s+opini[óo]n\s+|saber\s+)?en\s+(los\s+)?comentarios|cu[ée]ntame\s+en\s+(los\s+)?comentarios"), "cebo: te leo en los comentarios"),
    (rx(r"¿\s*(qué\s+opinas|y\s+tú|tú\s+qué\s+opinas|qué\s+piensas)\s*\?\s*(👇|⬇️|👀)"), "cebo: ¿Qué opinas? 👇"),
    (rx(NW + r"(me|nos)\s+(complace|enorgullece|emociona)\s+(anunciar|compartir|presentar|contarles)" + EW), "anuncio: me complace anunciar"),
    (rx(NW + r"(estoy|estamos)\s+(feliz|felices|emocionad[oa]s?|orgullos[oa]s?)\s+de\s+anunciar" + EW), "anuncio: estoy feliz de anunciar"),
]
EMOJI = re.compile("[\U0001F300-\U0001FAFF☀-➿⭐✅]")


def strip_front(t):
    if t.startswith("---\n"):
        parts = t.split("---\n", 2)
        if len(parts) == 3:
            return parts[2]
    return t


def line_of(text, pos):
    s = text.rfind("\n", 0, pos) + 1; e = text.find("\n", pos)
    e = len(text) if e < 0 else e
    snip = text[s:e].strip()
    return snip if len(snip) <= 90 else snip[:87] + "…"


def find(rules, text, cat, hits):
    for pat, label in rules:
        for m in pat.finditer(text):
            hits[cat].append((label, m.group(0).strip()[:70]))


STOP = {"la", "el", "los", "las", "de", "del", "y", "en", "a", "al", "con", "para", "por", "tu", "tus", "su", "sus", "un", "una", "que", "o", "e", "sin", "sobre", "como", "mi", "mis", "lo"}


def headings(text):
    for line in text.splitlines():
        s = line.strip()
        m = re.match(r"^(#{1,6})\s+(.*)$", s) or re.match(r"^\*\*([^*]+?)\*\*$", s)
        if m:
            yield s, m.group(m.lastindex)
            continue
        m = re.match(r"^\**(asunto|subject)\s*:\**\s*(.+)$", s, re.I)
        if m:
            yield s, m.group(2).strip("* ")


def title_case(h):
    h = re.sub(r"^[^\wáéíóúÁÉÍÓÚñÑ¿¡]+", "", h)
    h = re.split(r"[:—–|]", h)[0]  # only the part before a colon: "Guía: Cómo…" is fine
    words = re.findall(W + r"+", h)
    if len(words) < 3:
        return False
    rest = [w for w in words[1:] if not (w.isupper() and len(w) > 1)]  # skip acronyms (IA, SEO)
    if any(w.lower() in STOP and w[0].isupper() for w in rest):
        return True  # "Cómo Usar La IA": a capitalised article or preposition mid-title
    content = [w for w in rest if w.lower() not in STOP]
    if any(w.lower() in STOP for w in rest):
        return False  # lowercase "en la" between capitals: a proper name ("Región Metropolitana")
    return len(content) >= 2 and all(w[0].isupper() for w in content) and words[0][0].isupper()


def missing_openers(text, close, open_):
    text = re.sub(r"https?://\S+|www\.\S+", "link", text)
    out = []
    for m in re.finditer(re.escape(close), text):
        nxt = text[m.end():m.end() + 1]
        if nxt and (nxt.isalnum() or nxt in "=&/"):  # URL query, not a question
            continue
        prev = text[m.start() - 1] if m.start() else ""
        if prev in "?!" + close:  # "?!" or "!!": count once
            continue
        i = m.start() - 1
        while i >= 0 and text[i] not in ".!?¿¡\n" + open_:
            i -= 1
        if i < 0 or text[i] != open_:
            seg = text[i + 1:m.end()].strip()
            if len(re.findall(W + r"+", seg)) >= 1:
                out.append(seg[-60:])
    return out


def audit(text):
    text = strip_front(text)
    hits = {k: [] for k in ("formato", "estructuras", "muletillas", "léxico", "redes", "notas")}
    for m in re.finditer(r"[—]|(?<!\d)\s?–\s?(?!\d)", text):
        hits["formato"].append(("raya (— –)", line_of(text, m.start())[:60]))
    for raw, h in headings(text):
        if title_case(h):
            hits["formato"].append(("título en mayúsculas a la inglesa", raw[:60]))
    # Notes, not scored: people in Chile drop ¿ and ¡ all the time in informal writing.
    for seg in missing_openers(text, "?", "¿"):
        hits["notas"].append(("falta ¿ (normal en mensajes informales; en un texto formal, ponlo)", seg))
    for seg in missing_openers(text, "!", "¡"):
        hits["notas"].append(("falta ¡ (normal en mensajes informales)", seg))
    find(ESTRUCTURAS, text, "estructuras", hits)
    find(MULETILLAS, text, "muletillas", hits)
    find(LEXICO, text, "léxico", hits)
    find(REDES, text, "redes", hits)
    tags = re.findall(r"(?<![\w#&])#[\wáéíóúñÁÉÍÓÚÑ]+", text)
    if len(tags) > 5:
        hits["redes"].append((f"{len(tags)} hashtags (más de cinco)", " ".join(tags[:6])))
    lines = text.splitlines()
    lead = re.compile(r"^\s*(?:#{1,6}\s*|\*\*\s*|[-*•]\s+)?" + EMOJI.pattern)
    bullets = [l for l in lines if lead.match(l)]
    if len(bullets) >= 3:
        hits["formato"].append((f"emojis como viñetas ({len(bullets)} líneas)", bullets[0].strip()[:50]))
    labels = [l for l in lines if re.match(r"^\s*([-*•]|\d+[.)])\s+\*\*[^*\n]{1,40}(:\*\*|\*\*\s*:)", l)]
    if len(labels) >= 3:
        hits["formato"].append((f"negrita-etiqueta en cada viñeta ({len(labels)} líneas)", labels[0].strip()[:50]))
    inline = re.findall(r"(?<=\S )\*\*[^*\n]{2,60}\*\*", text)
    if len(inline) >= 3:
        hits["notas"].append((f"{len(inline)} negritas sueltas en la prosa (hábito de chat; ¿hacen falta?)", inline[0][:40]))
    return hits


def score(hits):
    return 5 - sum(1 for k, v in hits.items() if v and k != "notas")


def report(hits, label=""):
    if label:
        print(f"── {label}")
    for cat, items in hits.items():
        if not items:
            continue
        print(f"  {cat}:")
        for lab, snip in items[:8]:
            print(f"    · {lab}  «{snip}»")
        if len(items) > 8:
            print(f"    · …y {len(items) - 8} más")
    s = score(hits)
    print(f"  puntaje {s}/5  " + ("LIMPIO (de estas marcas; léelo igual)" if s == 5 else "tiene marcas de IA"))
    return s


def main():
    try:
        sys.stdout.reconfigure(errors="replace")
    except Exception:
        pass
    ap = argparse.ArgumentParser(description="Marcas duras de IA en textos en español.")
    ap.add_argument("files", nargs="*"); ap.add_argument("--text"); ap.add_argument("--json", action="store_true")
    a = ap.parse_args()
    if a.text is not None:
        items = [("--text", a.text)]
    elif a.files:
        items = []
        for f in a.files:
            try:
                items.append((f, open(f, encoding="utf-8").read()))
            except (OSError, UnicodeDecodeError) as e:
                sys.exit(f"deslop-es: no pude leer {f} ({e.__class__.__name__}); ¿es un archivo de texto en UTF-8?")
    else:
        items = [("stdin", sys.stdin.read())]
    if not any(t.strip() for _, t in items):
        sys.exit("deslop-es: no hay texto que revisar")
    worst, out = 5, {}
    for name, t in items:
        h = audit(t)
        worst = min(worst, score(h))
        if a.json:
            out[name] = {"score": score(h), "hits": {k: [list(x) for x in v] for k, v in h.items()}}
        else:
            report(h, name if len(items) > 1 else "")
    if a.json:
        print(json.dumps(out, ensure_ascii=False, indent=1))
    sys.exit(0 if worst == 5 else 1)


if __name__ == "__main__":
    main()
