# humanizer-es

[English](README.md)

**Que tu español escrito con IA suene a ti, sin cambiar lo que dice.**

Primera frente a otros cuatro humanizadores en una prueba a ciegas evaluada por Claude y por GPT. Los jueces no encontraron ningún dato inventado en 180 evaluaciones.

<sub>Un proyecto vivo de [AIwithDiego](https://www.aiwithdiego.com): investigado, construido, probado y mejorando con tus comentarios. ¿La necesitas para tu equipo? [Hablemos](https://www.aiwithdiego.com).</sub>

<p align="center"><img src="docs/demo-es.gif" alt="Animación: una línea de escaneo marca siete marcas de IA en un caption de Instagram escrito por ChatGPT, las marcas estallan y los cuatro datos (el nombre de la panadería, las 6:00, los tres panes y la dirección) se deslizan al texto reescrito. El puntaje del revisor sube de 2/5 a 5/5." width="760"></p>

```text
/plugin marketplace add AIwithDiego/humanizer-es
/plugin install humanizer-es@humanizer-es
```

**Funciona en:** Claude Code (skill) · ChatGPT, Claude.ai y cualquier chat ([`prompt.md`](prompt.md)) · cualquier terminal (el revisor)

**En esta página:** [El problema](#el-problema) · [Por qué importa](#por-qué-importa) · [Investigación](#investigación) · [Enfoque](#enfoque) · [Qué incluye](#qué-incluye) · [Cómo lo probamos](#cómo-lo-probamos) · [Resultados](#resultados) · [Qué sigue](#qué-sigue) · [Cuéntanos](#cuéntanos)

## El problema

Cada vez más español lo redactan ChatGPT y Claude: correos a clientes, captions de Instagram, avisos de trabajo, posts de LinkedIn. Quien lee lo nota rápido. El texto de IA en español tiene sus propias marcas, y casi ninguna es la del inglés:

- **Calcos del inglés:** "es importante destacar que", "en el mundo actual", Mayúsculas En Los Títulos.
- **Gramática y ritmo:** gerundios colgados ("…, garantizando frescura"), tríadas por todas partes, preguntas que se responden solas.
- **El español equivocado:** vosotros y giros de España en el correo de una tienda de Santiago.
- **Teatro:** "no solo X, creamos Y", elogios vacíos, "¡Te leo en los comentarios!".

El arreglo de siempre, "haz que suene más humano", lo empeora. En nuestra prueba, pedírselo así a ChatGPT o a Claude inventó o cambió datos en unas 4 de cada 10 evaluaciones.

## Por qué importa

Un texto que suena a IA cuesta confianza: el cliente se pregunta si alguien leyó su correo. Pero un humanizador que inventa cuesta más. Una versión que agrega una disculpa que el negocio nunca dio, o un "nos encantó la propuesta" que nadie dijo, no se le puede mandar a un cliente. Para una pyme, el dato es el mensaje: la hora, el precio, la dirección.

Por eso la vara fue doble: sonar a persona y no cambiar nada que sea cierto.

## Investigación

Antes de escribir una línea de la skill:

- **Qué existe.** Encontramos cuatro humanizadores en español en GitHub. Congelamos tres, más el de inglés que usábamos antes, tal como estaban publicados, para probarlos de forma justa. ([`evals/contestants/`](evals/contestants/))
- **Cómo se ve el español de IA.** Partimos de la guía de Wikipedia [Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing) y del marco de blader/humanizer, y catalogamos las marcas propias del español, ordenadas por fuerza: algunas bastan solas, otras cuentan solo cuando se juntan. ([`skills/humanizer-es/SKILL.md`](skills/humanizer-es/SKILL.md))
- **Cómo suena una persona.** Juntamos textos que escribieron chilenos antes de que existiera ChatGPT (foros, avisos de trabajo, el "quiénes somos" de una pastelería, noticias locales) como control. Un buen humanizador los deja casi intactos. ([`evals/human-sources.md`](evals/human-sources.md))

## Enfoque

Cuatro reglas guían cada versión:

1. **Primero, decidir quién lo escribió.** Si no aparece ninguna marca de IA, el texto es de una persona: corrige erratas claras y para.
2. **Arreglar borrando, no adornando.** Se borra la marca. Si queda un hueco, se llena con un dato que ya está en el texto. Si no hay dato, se simplifica.
3. **Nunca agregar un dato.** Ni nombres, ni números, ni disculpas, ni promesas, ni adornos. Mismo alcance, misma fuerza.
4. **Español neutro que se lee bien en Chile.** Tú y ustedes; nada de vosotros ni voseo.

## Qué incluye

| | Qué es | Dónde |
|---|---|---|
| **La skill** | El flujo completo para Claude Code: marcas por fuerza, borrador, autorrevisión y una segunda pasada opcional con GPT | [`skills/humanizer-es/`](skills/humanizer-es/SKILL.md) |
| **El prompt para pegar** | Un solo prompt para ChatGPT, Claude.ai o cualquier chat | [`prompt.md`](prompt.md) |
| **El revisor** | `deslop-es`: revisor de marcas de IA en español con patrones. Gratis, sin internet, puntaje de 1 a 5 | [`tools/deslop_es.py`](tools/deslop_es.py) |
| **La evidencia** | Cada encargo, texto, versión, prompt de juez y evaluación | [`evals/`](evals/README.md) |

Cómo empezar:

1. En Claude Code, corre las dos líneas de arriba.
2. Pega un texto en español y pídele a Claude que lo humanice, o escribe `/humanizer-es`.
3. Copia la versión de arriba. Debajo viene una nota con lo que cambió.

¿No usas Claude Code? Pega [`prompt.md`](prompt.md) en ChatGPT o Claude.ai y después tu texto, debajo de "Texto:". El revisor: `python3 tools/deslop_es.py --text "tu texto"`.

## Cómo lo probamos

<p align="center"><img src="docs/how-we-tested-es.png" alt="Cómo lo probamos, en seis pasos: 30 encargos en 15 géneros; 60 textos de IA, uno de GPT y uno de Claude por encargo, más 8 textos que escribieron personas antes de ChatGPT; 2 sets, uno de desarrollo para ajustar y uno bloqueado, abierto una vez; 6 versiones por texto, cada humanizador tal como se publica; 3 perfiles de juez, cada uno como juez Claude y juez GPT, con etiquetas mezcladas; resultado, primera de 6 con 0 datos inventados en 180 evaluaciones. Abajo: 137 pruebas automáticas del revisor en CI, pruebas manuales de Diego con sus propios textos, 9 rondas de prueba con las 3 primeras descartadas." width="760"></p>

- **Automático.** El revisor tiene 137 pruebas. CI las corre en cada pull request, junto con una revisión de la estructura del plugin y un escaneo de secretos.
- **Evaluaciones a ciegas.** 9 rondas. Los jueces nunca saben quién escribió qué, y jueces de dos familias de modelos evalúan cada versión, porque un modelo que juzga solo prefiere su propio estilo.
- **Manual.** Diego la probó con sus propios textos, fuera de los sets de prueba.
- **Sin hacernos trampa.** Botamos las tres primeras rondas porque esos textos los habíamos escrito nosotros. El número del titular sale de un set bloqueado que nadie leyó mientras ajustábamos.

## Resultados

<p align="center"><img src="docs/results-es.png" alt="Ranking promedio, más bajo es mejor: humanizer-es 2,44; humanizer-es con pasada GPT 2,48; blader/humanizer 3,22; alvaromieres9 3,97; madebydiego 4,35; omelyanchuk2593 4,53. Datos inventados o cambiados, de 180 evaluaciones: humanizer-es 0, omelyanchuk2593 12, blader 14, alvaromieres9 27, madebydiego 36." width="760"></p>

30 textos escritos por IA y 4 escritos por personas, ninguno usado para ajustar; cada humanizador corrió tal como se publica. Se probó la v1.3; la v1.4 solo agrega la corrección de erratas en textos de personas, revisada en el set de desarrollo y sin nueva evaluación. El prompt para pegar le gana a pedir "haz que suene más humano" por unos dos puestos. Todo, evaluación por evaluación: [`evals/`](evals/README.md) (en inglés).

## Lo que no hace

- Agregar datos, disculpas, promesas o personalidad que tu texto no tiene.
- Reescribir un texto que escribió una persona. Corrige erratas y ahí para.
- Prometer que pasa los detectores de IA. Edita para lectores.
- Enviar tu texto a otro modelo sin preguntarte.

Por favor, no la uses para esconder el uso de IA donde hay que declararlo (trabajos de estudio, investigación, periodismo).

---

## Decisiones

| Decisión | Por qué | Lo que cuesta |
|---|---|---|
| Nunca agregar un dato, ni para sonar más humano | Un humanizador que inventa no sirve para un correo a un cliente | Menos color que alvaromieres9, que a veces los jueces encontraron más chileno |
| Una skill y un prompt para pegar | La mayoría de quienes escriben en español usan ChatGPT, no Claude Code | El prompt tiene menos controles y no tiene segunda pasada |
| Jueces de dos familias de modelos | Un modelo que juzga solo prefiere su propio estilo | El doble de costo, y las familias no se ponen de acuerdo sobre la segunda pasada con GPT, así que queda opcional |
| Un set de prueba bloqueado, abierto una sola vez | Para que el número del titular no esté ajustado a la prueba | Ya se usó; el próximo número necesita textos nuevos |
| Un revisor con patrones, sin modelo | Gratis, instantáneo, sin internet, corre en CI | No ve las marcas de tono: 12 de 30 textos de IA salieron limpios |

## Cómo se hizo

La hice yo, Diego Bauer, con Claude Code. Puse la vara (ganarles a ciegas a los humanizadores en español que existen, sin inventar), decidí la variante, la privacidad y qué cuenta como dato, y la probé con mis propios textos. Claude escribió la mayor parte de la skill, del revisor y de los scripts de prueba. Antes de publicarla, una revisión de seguridad de IA revisó la segunda pasada (inyección de prompts, datos enviados a OpenAI) y qué podíamos publicar según cada licencia.

## Lo que aprendí

- **Un modelo no ve sus propias mañas.** El primer prompt para pegar dejaba casi intacto el texto de GPT: GPT muchas veces decidía que su propio texto "ya suena humano". La solución fue decidir primero quién lo escribió y editar el texto de IA aunque se vea correcto.
- **El error grave es inventar, no sonar a robot.** La v1.2 cambió o inventó datos en 21 evaluaciones del set de desarrollo; la v1.3 en 3, y en 0 de 180 en el set bloqueado. Reglas como "deja lo que describe, borra el elogio vacío" y "mismo alcance, misma fuerza" sirvieron más que cualquier lista de palabras prohibidas.
- **Los jueces no opinan igual según la familia.** Los jueces Claude preferían nuestra versión sin la pasada de GPT; los jueces GPT, con ella. Con una sola familia habríamos sacado una conclusión equivocada y muy segura.
- **Dejar intacto el texto de una persona no basta.** Los jueces pusieron primero a otro humanizador en los textos humanos porque corregía erratas. La v1.4 corrige erratas claras y nada más.
- **Botamos nuestras tres primeras rondas de prueba** porque los textos los habíamos escrito nosotros. Desde entonces la prueba usa encargos reales, textos de GPT y de Claude, y textos que escribieron personas antes de ChatGPT.

## Qué sigue

- **El revisor, afinado por quienes lo usan.** Los tres primeros issues ya están resueltos, dos por un colaborador externo. Lo que sigue: las marcas que nos reportes y ejemplos de más países (Perú, Venezuela, Uruguay…).
- **Una nueva ronda a ciegas** con textos nuevos, para evaluar la v1.4 y lo que cambie con tus comentarios.

## Cuéntanos

Este es un proyecto vivo. Cada aviso de que una versión cambió un dato, dejó una marca o sonó raro alimenta la próxima versión.

- **Una versión salió mal:** [abre un issue](https://github.com/AIwithDiego/humanizer-es/issues/new?template=rewrite.yml) (cambia nombres y números reales por otros inventados).
- **Una idea o un comentario rápido:** [déjanos tu comentario](https://github.com/AIwithDiego/humanizer-es/issues/new?template=feedback.yml).
- **¿Prefieres no usar GitHub?** Escríbeme por Instagram a [@ai_with_diego](https://www.instagram.com/ai_with_diego/) o a diego@aiwithdiego.com.

Los pull requests también son bienvenidos, sobre todo falsas alarmas del revisor con español normal de tu país. Ver [CONTRIBUTING.md](CONTRIBUTING.md). Problemas de seguridad: [SECURITY.md](SECURITY.md).

## Créditos

Construida sobre ideas de [blader/humanizer](https://github.com/blader/humanizer), [stop-slop](https://github.com/hardikpandya/stop-slop), [SlopMonster](https://github.com/ItsssssJack/SlopMonster) y los humanizadores en español de [omelyanchuk2593](https://github.com/omelyanchuk2593/humanizer-es), [alvaromieres9](https://github.com/alvaromieres9/humanizer-es), [Milevan](https://github.com/Milevan/humanizer-es) y [madebydiego](https://github.com/madebydiego/humanizador). Detalle en [THIRD-PARTY.md](THIRD-PARTY.md).

## Licencia

MIT · Hecha en Dublín por [Diego Bauer](https://www.aiwithdiego.com) · [LinkedIn](https://www.linkedin.com/in/diego-bauer-domeyko/)
