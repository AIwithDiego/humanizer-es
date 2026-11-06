---
name: humanizer-es
description: Revisa textos en español para reducir los patrones típicos de IA, corregir los calcos del inglés más frecuentes y aplicar el perfil de voz que hayas rellenado. Úsala como última pasada antes de entregar cualquier texto que vaya a leer otra persona.
---

# Humanizer-ES

La skill `humanizer` original cubre bien los patrones de IA que son universales, como el "no es X, es Y", las tríadas o el abuso de rayas. Lo que no resuelve es la traducción: aplicada tal cual al español caza fantasmas y deja pasar los calcos y giros que solo nos suenan raros a nosotros.

Uno de los ejemplos más citados en inglés es *delve into*. Tradúcelo y te queda "profundizar en", que en español es de lo más normal. Mientras tanto se cuelan el "es importante de mencionar", que es un calco de *it's important to mention*, o el "al final del día" que sale de *at the end of the day* cuando lo que decimos es "a fin de cuentas". Y hay casos más finos, como el gerundio de "lanzó el producto, consiguiendo un aumento de ventas", que es correcto en español pero que un modelo usa con mucha más frecuencia que una persona. Esa capa española es la que añade esta skill sobre la original.

Esta skill hace tres cosas en este orden, y el orden importa:

1. **Quitar los patrones de IA.** Esto no tiene nada que ver con quien firma el texto.
2. **Escribir español de verdad**, no traducido.
3. **Sonar a ti**, que es la única parte que tienes que rellenar tú.

**Cuándo usarla:** siempre que entregues un texto en español que vaya a leer otra persona. Un post, un artículo, un correo, un mensaje, un documento. Es la última pasada antes de entregar. Para textos en inglés, usa la skill `humanizer` original.

**Regla de oro:** si una frase suena a traducción del inglés no se parchea, se reescribe desde cero en español. Léela en voz alta mentalmente, y si no la dirías así en una conversación, fuera.

**Paso 0, en cuanto tengas el registro en marcha:** lee `registro-correcciones.md` entero antes de empezar, no solo antes de la última pasada. Son tus correcciones reales y mandan sobre cualquier regla de este manual. Si una fila contradice algo de aquí, gana la fila.

## Proceso en 3 pasadas

Trabajar el texto en este orden. No mezclar pasadas: primero limpiar la IA, luego el idioma, luego la voz.

### Pasada 1 — Des-IA-ficar (arsenal anti-patrones)

Buscar y eliminar todos estos patrones (heredados del humanizer original, adaptados al español):

**Contenido:**
1. **Inflación de trascendencia.** "marca un hito", "un antes y un después", "punto de inflexión", "juega un papel crucial/fundamental/clave", "pone de manifiesto", "subraya la importancia", "refleja una tendencia más amplia", "deja una huella imborrable", "en el panorama actual", "en la era de la IA", "sentando las bases de". Sustituir por el dato concreto o borrar.
2. **Gerundios decorativos de falsa profundidad.** Frase + coma + gerundio que no aporta: "...destacando su compromiso", "...reflejando su esencia", "...fomentando la innovación", "...garantizando el éxito", "...evidenciando que". Cortar la frase o convertir el gerundio en una oración con sujeto y dato.
3. **Lenguaje promocional.** "vibrante", "impresionante", "revolucionario", "de vanguardia", "sin precedentes", "robusto", "imprescindible", "enclavado en el corazón de", "un ecosistema único". Si no lo dirías en un bar, no va.
4. **Atribuciones vagas.** "los expertos coinciden", "diversos estudios señalan", "se dice que", "muchos consideran". O se cita la fuente concreta con cifra (con la cifra y la fuente enlazada), o se quita.
5. **Evitación del verbo ser.** "se erige como", "constituye", "se posiciona como", "actúa como", "supone" (cuando toca "es"). Escribir "es", "son", "tiene".
6. **Paralelismos negativos y tríadas.** "No es solo X, es Y", "no se trata de X, sino de Y", y los grupos de tres mecánicos ("innovación, inspiración y resultados"). Ojo, el contraste A/B vale cuando es tuyo y tiene chicha. Lo que sobra es el patrón mecánico repetido.
7. **Ciclado de sinónimos.** El protagonista / el personaje principal / la figura central. Repetir la palabra está bien; los humanos repiten.
8. **Rangos falsos.** "desde X hasta Y" cuando X e Y no están en ninguna escala real.
9. **Pasivas innecesarias y sujetos escondidos.** "fue desarrollado por el equipo" → "lo desarrolló el equipo". "No se necesita configuración" → "no necesitas configurar nada".
10. **Muletillas de relleno.** "cabe destacar que", "es importante señalar/mencionar que", "en este sentido", "asimismo", "no obstante" mecánico, "además" encadenado, "por otro lado" sin otro lado real, "en definitiva", "en resumen", "en conclusión", "en última instancia".
11. **Hedging vacío.** "podría potencialmente", "en cierto modo", "posiblemente podría llegar a". Una calificación como mucho; si hay duda real, decirla con datos ("no lo he medido, pero...").
12. **Cierres genéricos optimistas.** "el futuro es prometedor", "queda un emocionante camino por delante", "sin duda dará que hablar", "las posibilidades son infinitas". Cerrar con algo concreto o con pregunta al lector.
13. **Señalización y meta-comentario.** "veamos", "profundicemos", "sin más dilación", "acompáñame en este viaje", "aquí tienes lo que necesitas saber". Ir al grano directamente.
14. **Frases de tribuna.** "la verdadera pregunta es", "en el fondo, lo que realmente importa", "el quid de la cuestión". Suelen preceder a una obviedad con ceremonia.
15. **Artefactos de chatbot.** "¡Espero que te sirva!", "¡Claro!", "Aquí tienes el texto:", "¿Quieres que te lo desarrolle?". Fuera siempre.
16. **Encabezado + frase que repite el encabezado.** Si tras un título hay una frase de una línea que solo lo parafrasea, borrarla.

**Formato:**
17. **Guiones largos (em-dash) estilo anglosajón.** Ojo con la justificación, porque la raya es puntuación válida en español y usarla no es una falta. Lo que ocurre es que se ha convertido, por pura frecuencia, en una de las señales más asociadas a texto generado. Por defecto, cero: sustituir por comas, paréntesis, dos puntos o punto y frase nueva. Si en algún caso la raya es claramente la mejor opción y tú la habrías escrito, déjala y anótalo en tu perfil de voz.
18. **Negritas decorativas.** La negrita se usa, pero quirúrgica: una idea clave por sección, no cada término. Nada de listas con "**Encabezado:** texto" mecánicas.
19. **Emojis.** Con cuentagotas y solo en registro informal. Jamás decorando encabezados o viñetas.
20. **Title Case.** En español los títulos van en minúscula salvo la primera palabra y los nombres propios. "Como monte mi segundo cerebro", no "Como Monte Mi Segundo Cerebro".
21. **Listas anidadas innecesarias.** Si cabe en un párrafo narrativo, va en párrafo. Si el texto pide párrafos narrativos, van párrafos, no esqueletos de viñetas.

### Pasada 2 — Españolizar (ortografía, puntuación y caza de calcos)

**Ortografía perfecta, sin excepción:**
- Todas las tildes, incluidas las mayúsculas (ADEMÁS, ÁFRICA) y los interrogativos indirectos (qué, cómo, cuándo, por qué).
- La ñ siempre. "Espana" o "manana" delatan la skill genérica al instante.
- Signos de apertura obligatorios: ¿...? ¡...! en todo texto entregable. (En mensajería informal mucha gente se los come; la skill entrega siempre correcto y ya los relajas tú si quieres.)
- Diferenciar porqué / por qué / porque / por que; sino / si no; aún / aun; sólo no (ya sin tilde, RAE).
- Números a la española: decimales con coma ("72,5 kg"), "el 41%" con artículo, "mil millones" y no "un billón" (billion).

**Puntuación española:**
- Comillas: coherentes en todo el texto. Elegir un tipo de comillas y mantenerlo. Nunca mezclar "...", «...» y '...' en la misma pieza.
- La raya española (—) existe pero se usa distinto al em-dash inglés: para incisos va pegada por dentro —así— y para diálogos. Lo más seguro es no usarla y tirar de comas, paréntesis o punto y frase nueva.
- Tras dos puntos, por regla general minúscula. Va mayúscula en los casos que prevé la norma, entre ellos las citas textuales y el saludo de una carta o un correo ("Querido Rafael: Te agradezco...").
- Meses, días de la semana y gentilicios en minúscula.

**Caza de calcos — lista concreta de los típicos:**

| Calco (mal) | Español nativo (bien) |
|---|---|
| "hace sentido" | "tiene sentido" |
| "es acerca de" / "va acerca de" | "va de", "trata de" |
| "en el largo/corto plazo" | "a largo/corto plazo" |
| "estar cómodo con la herramienta" | "manejarse bien con", "sentirse a gusto con" |
| "al final del día" (at the end of the day) | "a fin de cuentas", "al final" |
| "eventualmente" (eventually) | "al final", "tarde o temprano" |
| "asumir" (to assume) | "suponer", "dar por hecho" |
| "soportar" (to support) | "ser compatible con", "admitir" |
| "remover" (to remove) | "quitar", "eliminar" |
| "aplicar a un puesto" | "solicitar", "presentarse a" |
| "consistente" (consistent) | "coherente", "constante" |
| "agresivo" (aggressive goals) | "ambicioso" |
| "customizar" | "personalizar", "adaptar" |
| "en orden de/a" (in order to) | "para" |
| "es por eso que" | "por eso" |
| "tener en mente" (keep in mind) | "tener en cuenta", "tener presente" |
| "hacer los números" (do the math) | "echar cuentas" |
| "apalancar" / "rentabilizar el conocimiento" (leverage) | "aprovechar", "sacar partido a" |
| "empoderar al usuario" | "dar el control al usuario" (o reescribir) |
| "doméstico" (domestic flights) | "nacional" |
| "curar contenido" (curate) | "depurar", "filtrar"  |
| "en crudo" (raw) | "en bruto", "sin trabajar"  |
| "cubos" / "buckets" | "carpetas", "sitios"  |

**Estructuras calcadas (no solo palabras):**
- Futuro continuo comercial: "estaremos enviando la información" → "te enviaremos la información".
- Posesivos innecesarios: "lava tus manos", "abre tu Obsidian" → "lávate las manos", "abre Obsidian".
- Pasiva perifrástica en cadena: "puede ser configurado" → "se puede configurar" o "lo puedes configurar".
- Sujeto pronominal redundante: "tú puedes hacer que él trabaje" → en español el sujeto se omite si el contexto lo da.
- Preposiciones calcadas: "preocuparse sobre" → "preocuparse por"; "consistir de" → "consistir en"; "depender en" → "depender de".

**Un caso aparte, porque no es un calco: el gerundio de posterioridad.** Está documentado en español desde hace siglos, y el Diccionario panhispánico de dudas lo admite cuando hay inmediatez o una relación lógica entre las dos acciones, normalmente de causa y consecuencia, así que "lanzó el post, consiguiendo 500 likes" es correcto. Solo hay que corregir el que no tiene ni una cosa ni la otra, como el ejemplo del propio diccionario: "Recogió al niño del colegio, jugando un rato en el parque" → "y jugaron un rato en el parque". Aparte de eso, vigilar la frecuencia: si el texto encadena gerundios de este tipo uno detrás de otro, suena a modelo aunque cada uno sea correcto.

**Anglicismos: criterio, no purismo.** Los términos técnicos de tu sector (prompt, vault, feedback, landing, pipeline, dashboard) se quedan en inglés si es como los dices hablando, porque traducirlos a la fuerza suena postizo. Lo que se caza es el calco estructural y el anglicismo innecesario que tiene equivalente natural ("call" por llamada, "asap" por "cuanto antes", "learnings" por "aprendizajes").


### Pasada 3 — Darle tu voz

Aplicar el perfil de voz de abajo, que tienes que rellenar tú. En la práctica:

- Datos y ejemplos concretos donde el borrador tenga abstracciones.
- El ritmo de frase que hayas definido en tu perfil.
- Una o dos expresiones tuyas donde encajen de forma natural, sin forzar, porque una muletilla forzada canta más que un guion largo.
- **Explicar desde cero cualquier concepto técnico.** Si un término aparece por primera vez, meter una frase de puente en lenguaje llano antes de soltarlo. Regla dura: si no lo entendería un amigo listo no técnico en una charla, reescribir.

**Solo en textos que buscan tracción** (LinkedIn, X, un blog), añadir además abrir fuerte con una pregunta o un contraste, nunca con calentamiento, y cerrar con algo honesto. En mensajes privados y correos de trabajo no se aplica, porque ahí se entra directo al tema y se cierra como se cierra una conversación normal.

---

## Tu perfil de voz (rellénalo, es lo único que no se hereda)

> En la versión que uso yo, esta parte contiene mi voz real con citas literales de mis textos publicados. Aquí va vacía a propósito, porque una voz prestada no sirve de nada.
>
> **Cómo rellenarla sin inventarte nada.** Coge tres o cuatro textos tuyos que te gusten de verdad, escritos por ti y sin IA de por medio. Un correo largo, un post, un mensaje al que le pusiste ganas. Pégaselos a Claude o a ChatGPT y pídele que rellene las secciones de abajo a partir de ellos, con citas literales tuyas. No lo describas de memoria, porque tú no sabes cómo escribes, sabes cómo crees que escribes.

### Registro y tono
`[Cómo le hablas al lector. De tú o de usted, directo o con rodeos, admites lo que no sabes, eres irónico.]`

### Léxico característico (citas literales de tus textos)
`[Entre 8 y 12 expresiones que uses de verdad, copiadas tal cual de algo que hayas escrito. No las inventes, búscalas.]`

- `"..."`
- `"..."`
- `"..."`

### Ritmo y longitud de frase
`[Frases largas encadenadas por comas o frases cortas. Cómo cierras una idea. Pega dos o tres frases tuyas de ejemplo.]`

**Un antipatrón que conviene vigilar, porque le pasa a casi todo el mundo:** frase larga, punto, y frase corta lapidaria que reformula lo que ya has dicho. Es uno de los patrones de IA más reconocibles que hay. Si aparece, funde las dos frases en un solo periodo con "y", "pero" o "porque", y si la segunda no aporta nada nuevo, bórrala.

### Cómo abres y cómo cierras
`[Tus dos o tres aperturas típicas y tus dos o tres cierres típicos, sacados de textos reales.]`

### Cómo explicas lo técnico
`[Metáfora primero y término después, o al revés. Datos con fuente o sin ella. Para quién escribes, técnicos o no.]`

### Humor
`[Si tienes, de qué tipo. Emojis sí o no, y cuántos.]`

### Qué JAMÁS dirías
`[La lista negra. Jerga corporativa, tics de gurú, cierres de manual, promesas infladas. Sé específico, escribe lo que a ti te dé grima.]`

### Registro por canal
`[Cómo cambia todo lo anterior según dónde escribas, porque no es lo mismo un post que un WhatsApp que un correo de trabajo.]`

---

## Checklist final obligatoria (antes de entregar, siempre)

1. **Leerlo "en voz alta" mentalmente + test canónico.** ¿Suena a una persona contándole algo a un colega, o cualquiera podría decir de este texto **"nadie habla así en español"**? Si hay una sola frase que tú no dirías en una conversación, reescribirla.
2. **0 faltas de ortografía.** Tildes (también en mayúsculas e interrogativos), ñ, ¿¡ de apertura, porqué/por qué, comas decimales. Repasar letra a letra las palabras con tilde.
3. **0 patrones de IA.** Barrido final de la lista de la Pasada 1: em-dashes (cero), gerundios decorativos, tríadas, "cabe destacar", negritas mecánicas, cierre de manual.
4. **0 calcos.** Pasar la tabla de calcos. Si una frase suena a traducción del inglés, no se retoca: se reescribe desde cero en español.
5. **Test WhatsApp/LinkedIn:** ¿mandarías este texto tal cual, sin tocar nada? Si la respuesta es "casi", no está terminado.
6. **Auditoría adversarial:** preguntarse "¿qué delata que esto lo escribió una IA?" — listar los restos que queden y corregirlos antes de entregar. Solo entonces mostrar el resultado.

---

## Regla de mejora continua: esta skill aprende

Cada vez que corrijas un texto ya humanizado, ya sea cambiando una palabra, reescribiendo una frase o señalando algo que suena a IA, **la corrección se escribe en `registro-correcciones.md`**, con el antes, el después, la fecha y sobre todo el porqué.

Esa cuarta columna es la que casi nadie pone y la que más rinde. Si solo apuntas que cambiaste una palabra por otra, has arreglado esa frase. Si apuntas la razón, has arreglado las mil frases siguientes, incluidas las que todavía no has escrito.

Para que esto aguante, la captura no puede depender de que te acuerdes, porque un fichero que hay que rellenar a mano dura tres semanas. En el [kit de consistencia](https://github.com/alvaromieres9/kit-consistencia) tienes cómo montarlo: un hook que detecta las correcciones que traen una frase-señal, la skill `voz` que interpreta y escribe la fila, y un barrido de cierre para lo que se escape.

**Obligatorio antes de la pasada 3:** leer `registro-correcciones.md` entero. Tus correcciones mandan sobre cualquier regla genérica de este archivo.
