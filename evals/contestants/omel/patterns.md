# Mapa de patrones del español generado

Este archivo es la referencia completa del skill: 69 patrones con sus formas de detección, sus ejemplos de antes y después y sus límites. Se lee entero en la fase de auditoría y en el modo de detección. Editar de memoria deja pasar la mitad de los hallazgos.

Los patrones 1 a 35 vienen de la taxonomía inglesa canónica, con el inventario léxico y los ejemplos rehechos en español, no traducidos. Los patrones 36 a 69 son fenómenos que solo existen en español: rección, gerundio, clíticos, tratamiento, tildes, signos de apertura, variedad.

**Registro por defecto: neutro.** El skill no impone formas peninsulares a un texto americano ni al revés. Cuando una regla depende de la variedad se dice en el propio patrón, y la decisión correcta es la del encargo o la del manual de estilo del cliente, no la de España por defecto. Un texto ya coherente con una variedad no se neutraliza.

**Qué puede afirmar el skill.** Nombra patrones y cita la frase donde aparecen. Eso es todo lo que puede hacer con honradez: no determina la autoría de un texto ni certifica que lo haya escrito una máquina. Un hallazgo suelto no prueba nada; varios patrones de familias distintas en el mismo pasaje son indicio, no veredicto. Es preferible dejar pasar un texto automático que acusar a una persona.

**Regla que manda sobre todas las demás.** Al limpiar no se añade ningún hecho, nombre, cifra, fecha, atributo, modalidad ni acto de habla que no estuviera en el original. La limpieza borra valoraciones; nunca inventa. Si al quitar la palabrería no queda nada, el resultado correcto es que no quede nada.

**Códigos del linter.** Cada patrón indica la regla que lo vigila, cuando existe. La tabla tiene 51 reglas: 9 de nivel ERROR (prohibición dura, hay que dejarlas a cero) y 42 de nivel AVISO (marcador que se valora por acumulación). Tres reglas no tienen patrón propio y funcionan como higiene tipográfica: `ES-SIGNOS-01` (signo matemático o flecha en prosa corrida), `ES-SIGNOS-02` («vs.» en prosa española, recomendación de estilo y no norma) y `ES-CIFRA-01` (cifra con «+» pegado en un reclamo, «5+ horas» por «más de 5 horas»).

---

## Contenido

### 1. Afirmaciones infladas sobre importancia y legado

**Qué falla:** un dato ordinario se presenta como hito histórico. La estrategia de corrección es conservar el hecho fechado con todos sus atributos y tirar la valoración.
**Qué vigilar:** marcó un antes y un después, supuso un punto de inflexión, se erige como, sentó las bases de, dejó una huella imborrable, consolidándose como referente, en el panorama actual, cobra especial relevancia, no es casualidad que, se enmarca en un contexto más amplio, hito, legado perdurable.
**Antes:**
> El Instituto de Estadística de Cataluña se creó oficialmente en 1989, marcando un antes y un después en la evolución de la estadística regional en España. Esta iniciativa se enmarcó en un movimiento más amplio de descentralización administrativa que ha dejado una huella imborrable en la gobernanza autonómica.

**Después:**
> El Instituto de Estadística de Cataluña se creó oficialmente en 1989, dentro de un movimiento más amplio de descentralización administrativa.

**No marcar:** «oficialmente», «previsto», «provisional» y similares no son valoración, son datos, y se quedan. «Un antes y un después» es además un cliché periodístico hispano muy anterior a los modelos (véase el patrón 7): cuenta como registro, no como prueba aislada.

### 2. Citar nombres propios para demostrar relevancia

**Qué falla:** se enumeran medios o cifras de seguidores para probar que alguien importa, dentro de un marco valorativo que no informa de nada.
**Qué vigilar:** cuenta con una destacada presencia en redes sociales, ha sido recogido por medios de alcance nacional e internacional, avalado por los principales medios del sector, una amplia repercusión mediática.
**Antes:**
> Sus opiniones han sido recogidas por El País, la BBC, Le Monde y Clarín. Además, cuenta con una destacada presencia en redes sociales, donde supera los 500.000 seguidores.

**Después:**
> El País, la BBC, Le Monde y Clarín han recogido sus opiniones. Tiene más de 500.000 seguidores en redes sociales.

**No marcar:** si la fuente explica qué dijo la persona y dónde, esa cita es información y se conserva. Se elimina la envoltura publicitaria, no el dato.

### 3. Análisis superficial con gerundios ilativos

**Qué falla:** el modelo calca el «-ing» inglés con un gerundio que expresa un hecho posterior al verbo principal o su consecuencia. La norma académica lo censura: el gerundio admite valor de simultaneidad, modo, causa, condición o anterioridad inmediata, nunca de efecto posterior. Es el calco número uno del español generado, y además le sirve al modelo para cerrar el párrafo con una falsa conclusión. La segunda variante es la coletilla relativa, que cumple la misma función de aparentar profundidad.
**Qué vigilar:** reflejando así, consolidándose como, permitiendo mejorar, convirtiéndose en; lo que refleja, lo cual pone de manifiesto, lo que se traduce en.
**Antes:**
> La paleta cromática del edificio (azul, verde y dorado) dialoga con la belleza natural de la región, simbolizando el mar Mediterráneo, los olivares y los cielos de la meseta, reflejando así el profundo vínculo de la comunidad con su territorio.
>
> [gerundio de posterioridad] La empresa se fundó en 2004, convirtiéndose una década después en el mayor exportador del país.

**Después:**
> Los colores del edificio (azul, verde y dorado) evocan el mar Mediterráneo, los olivares y los cielos de la meseta.
>
> [gerundio de posterioridad] La empresa se fundó en 2004 y una década después se convirtió en el mayor exportador del país.

**No marcar:** el gerundio de simultaneidad, modo, causa, condición o anterioridad inmediata, que es correcto: «Llegó corriendo», «Aprendió el oficio observando a su padre», «Habiendo terminado el informe, salió», «Siendo así, cerramos el trato». Tampoco el gerundio en perífrasis: «está creciendo», «sigue trabajando», «lleva dos años viviendo aquí», «acabó reconociéndolo». Prueba mecánica: si la acción del gerundio ocurre después de la del verbo principal o es su consecuencia, es infracción; si es simultánea o previa, se deja. Al cortar la coletilla no se asciende de categoría lo que decía el original: una paleta cromática son colores, no pintura.
**Severidad:** prohibición dura para el gerundio de posterioridad.
**Linter:** `ES-GERUNDIO-01` (cadena de dos o más gerundios en la misma oración) marca candidatos, no infracciones.

### 4. Lenguaje publicitario y de nota de prensa institucional

**Qué falla:** el subregistro español de este patrón es la nota de prensa institucional y el folleto turístico. Se suma un rasgo sintáctico: la acumulación de adjetivos valorativos pospuestos, que en español pesa más que en inglés porque el adjetivo pospuesto es el que carga la valoración.
**Qué vigilar:** poner en valor, apostar decididamente por, de la mano de, referente indiscutible, enclavado en, en pleno corazón de, atesora, no deja indiferente, de visita obligada, un enclave privilegiado, riqueza cultural, seña de identidad, compromiso con la excelencia.
**Antes:**
> Enclavado en el corazón de la comarca de la Alpujarra, Trevélez se erige como un municipio vibrante que atesora una riqueza cultural incomparable y una belleza natural que no deja indiferente a nadie. Un destino de visita obligada.

**Después:**
> Trevélez es un municipio de la comarca de la Alpujarra.

**No marcar:** «poner en valor», «apostar por» y «de la mano de» son fórmulas institucionales y periodísticas peninsulares con crecimiento nativo medido y muy anterior a los modelos. El estudio léxico las rechaza como prueba de máquina (patrón 7): aquí cuentan como registro del conjunto, nunca como hallazgo suelto. Efecto colateral que sí conviene corregir: al arrancar con un participio antepuesto, el modelo suele romper la concordancia con el sustantivo que viene después («Enclavada… un municipio»).

### 5. Fuentes vagas

**Qué falla:** se atribuye una afirmación a una autoridad sin nombre. Si el original da la fuente, se nombra; si no la da, la afirmación se elimina.
**Qué vigilar:** según los expertos, los especialistas coinciden en que, diversos estudios señalan, informes del sector apuntan, fuentes cercanas a, está demostrado que, numerosos análisis sugieren, se estima que.
**Antes:**
> Por sus características singulares, el río Haolai despierta el interés de investigadores y conservacionistas. Los expertos coinciden en que desempeña un papel crucial en el ecosistema de la región.

**Después:**
> El río Haolai interesa a investigadores y conservacionistas por sus características singulares.

**No marcar:** la falta de citas no prueba nada por sí sola; casi ningún texto de la web cita sus fuentes. Y nunca se inventa un estudio, un instituto ni una cifra para tapar el hueco, ni se asciende el verbo: si la fuente dice que algo «despierta el interés» de alguien, la versión limpia no puede decir que ese alguien lo «estudia».
**Linter:** `ES-ATRIB-01`.

### 6. Apartados formulaicos de «retos» y «perspectivas de futuro»

**Qué falla:** el texto añade un apartado de problemas genéricos rematado con un balance optimista. En español los epígrafes son tan fijos que funcionan casi como firma.
**Qué vigilar:** Retos y desafíos, Perspectivas de futuro, Conclusiones y reflexiones finales, El camino por delante; a pesar de los desafíos, no está exento de retos, pese a ello, el futuro pasa por, sigue consolidándose como.
**Antes:**
> A pesar de su prosperidad industrial, Korattur no está exenta de desafíos propios de las zonas urbanas, como la congestión del tráfico y la escasez de agua. Aun así, gracias a su ubicación estratégica y a las iniciativas en marcha, Korattur sigue consolidándose como una pieza clave del crecimiento de Chennai.

**Después:**
> Korattur tiene problemas de congestión de tráfico y de escasez de agua.

**No marcar:** los problemas concretos y con nombre se conservan. Al condensar no se añaden adjetivos de frecuencia o gravedad («recurrente», «crónico», «grave») que la fuente no dé.

---

## Lengua y gramática

### 7. Palabras muletilla de la IA en español

**Qué falla:** hay un vocabulario que el español generado usa mucho más que la prosa humana. La lista no es traducible desde el inglés y hay que medirla en español: «delve» no da «ahondar» sino «adentrarnos en» y «sumergirnos en»; «tapestry» da «entramado» y «tejido social»; «landscape» da «panorama»; «testament» da «legado» y «buena muestra de ello». La señal es la acumulación, no la aparición suelta.

**Marcadores fuertes.** Cada uno cumple una de dos condiciones: es una plantilla de varias palabras cuyo borrado nunca destruye información, o es una acepción que el español no tiene y que un editor puede comprobar con un diccionario, sin acceso a ningún original inglés.

- **cabe señalar / cabe destacar / cabe mencionar.** Bisagra de planificación: la oración que sigue nunca depende de ella. El español escrito venía abandonando la fórmula antes de 2020 y el texto generado la produce sin parar. Corrección: borrar el sintagma y dejar la oración.
- **es importante señalar / es importante destacar / es importante tener en cuenta.** Rótulo de relevancia que no jerarquiza nada. Si algo es lo más importante del párrafo, lo muestra la estructura, no una etiqueta.
- **en este artículo exploraremos / a lo largo de este artículo veremos / en esta guía descubrirás.** La promesa de índice: el modelo anuncia el recorrido en vez de recorrerlo. Los apartados prometidos ya existen como títulos más abajo.
- **espero que esto te ayude / espero que este artículo te haya resultado útil.** Residuo del turno conversacional del asistente (patrón 20).
- **en el mundo actual / en la era digital / en un mundo cada vez más [competitivo, digital, complejo].** Relleno de primera línea. Ninguna de las tres introduce una proposición verificable. En texto generado, el primer párrafo entero suele ser desechable.
- **paisaje** en sentido abstracto («el paisaje del marketing digital»). El español no ha lexicalizado esa acepción. Recambios: panorama, ámbito, sector, escena, o deshacer la metáfora.
- **reino** en sentido abstracto («en el reino de la IA»). En español «reino» es monarquía o taxón biológico, y la perífrasis dice lo mismo que «en la IA» con cuatro palabras más.
- **adepto** con el valor de hábil o diestro. Falso amigo puro: en español significa seguidor o partidario.
- **eleva tu negocio / eleva tu marca / eleva tu presencia.** «Elevar» es físico, matemático, administrativo o de registro; no tiene el sentido promocional del inglés. No hay sustitución de una palabra que salve la frase: se reescribe por el beneficio concreto.
- **desbloquea tu potencial / desbloquea los secretos de.** En español se desbloquea lo que estaba bloqueado por un agente o un mecanismo. El potencial de una persona no lo estaba.
- **juega un papel fundamental / clave / crucial.** Se marca la colocación entera, no el verbo: cambiar «juega» por «desempeña» y dejar el resto es maquillaje. El defecto es que sustituye la afirmación de qué hace exactamente ese factor.
- **no se trata solo de X, sino de Y / no es X: es Y.** Probablemente el patrón sintáctico más diagnóstico del español generado actual (patrón 9).
- **cadena evaluativa: clave + fundamental + crucial o esencial en el mismo párrafo.** Ninguna de las tres palabras prueba nada aislada; su alternancia sí. Se deja el evaluativo mejor sostenido y se borran los otros dos sin sustituto.

**Marcadores de clúster: se juzgan por densidad, nunca de vista.** Cada uno tiene usos plenamente legítimos y una regla automática produciría bajas civiles. Solo cuentan cuando se acumulan con otros hallazgos: robusto (aplicado a marco, estrategia o ecosistema), vibrante (aplicado a comunidad, ecosistema, cultura o barrio), transformador, en constante evolución, se erige como, se posiciona como, revolucionar, aprovechar el poder de, al final del día (con el valor de «a fin de cuentas»), tomar acción, en términos de, hoy en día (en apertura y sin contraste temporal), en resumen o en conclusión encadenados, vale la pena mencionar, vale la pena destacar, en última instancia, no dudes en, invaluable.

**Qué vigilar además, como registro:** clave, crucial, fundamental, esencial, robusto, sólido, integral, holístico, panorama, entramado, matices, hito, sinergia, abordar, potenciar, impulsar, fomentar, garantizar, optimizar, destacar, subrayar, poner de relieve, resaltar, adentrarse, profundizar, un sinfín de, en constante evolución, en un mundo cada vez más, cabe destacar, es importante señalar, sin duda, no solo… sino también.

**Antes:**
> Además, cabe destacar que la cocina somalí incorpora la carne de camello. Un legado perdurable de la influencia colonial italiana es la adopción generalizada de la pasta en el panorama gastronómico local, lo que pone de relieve cómo estos platos se han integrado en la dieta tradicional.

**Después:**
> La cocina somalí incluye carne de camello. La pasta, adoptada de forma generalizada por la influencia colonial italiana, forma parte de la dieta tradicional.

**No marcar.** Estos términos son español ordinario y el estudio léxico los rechaza como prueba de generación automática. No se señalan, y menos aún se sustituyen en bloque: sin duda, en definitiva, panorama, clave, fundamental, crucial, apasionante, enriquecedor, exhaustivo, un antes y un después, piedra angular, de vanguardia, de la mano de, sumergirse en, sumérgete en, sinergia, sinérgico, destaca por, impulsar, optimizar, constituye, representa, imprescindible, potenciar, amplio abanico, soluciones integrales, poner en valor, apostar por.

Las razones del rechazo, resumidas, porque conviene poder defenderlas ante el autor del texto: la formalidad es un registro y no una huella (el lenguaje administrativo, jurídico y periodístico hispano escribe así desde hace décadas: constituye, potenciar, poner en valor, apostar por, imprescindible, amplio abanico); un cliché humano consolidado tampoco es una huella (un antes y un después, piedra angular, amplio abanico, sumergirse en); y la sospecha de que una palabra «es donde aterriza» un término que los modelos sobreproducen en inglés no es un hallazgo sobre el español (exhaustivo, piedra angular, sumergirse). Un caso concreto que hay que respetar: «panorama» es justamente el recambio recomendado para el calco «paisaje», así que no puede prohibirse el remedio.

**Aviso sobre el linter.** `ES-LEX-01` dispara con «crucial», «de vanguardia» y «sinergias», que están en la lista de rechazados. Esos avisos se leen como señal de densidad y jamás se convierten en hallazgo por sí solos. Lo mismo vale para `ES-TOPICO-01` con «hoy en día».
**Linter:** `ES-LEX-01`, `ES-TRANS-01`, `ES-TOPICO-01`, `ES-PAPEL-01`, `ES-VERBO-01`, `ES-INTENS-01`.

### 8. Huir de «ser», «estar», «tener» y «haber»

**Qué falla:** el modelo sustituye los verbos cortos por perífrasis largas que no aportan matiz. Conviene separar dos niveles de exigencia.
**Qué vigilar.** Nivel duro, se corrige siempre que no aporte matiz: se erige como, se posiciona como, se configura como, se caracteriza por ser, y el «podemos encontrar» locativo («en la ciudad podemos encontrar tres museos» por «la ciudad tiene tres museos»). Nivel de densidad, solo se avisa si se acumulan: cuenta con y dispone de por «tener»; constituye, supone y representa por «ser».
**Antes:**
> La Galería 825 se erige como el espacio expositivo de arte contemporáneo de la LAAA. El recinto cuenta con cuatro salas independientes y dispone de más de 280 metros cuadrados.

**Después:**
> La Galería 825 es el espacio expositivo de arte contemporáneo de la LAAA. Tiene cuatro salas independientes y más de 280 metros cuadrados.

**No marcar:** «existen» y «se encuentran» no son evasivas de «hay» ni intercambiables con él. «Existen tres variantes» y «hay tres variantes» dicen cosas distintas en prosa argumentativa, así que solo se tocan cuando funcionan como puro relleno existencial. «Cuenta con», «dispone de», «constituye», «supone» y «representa» son español estándar y no marcado: su tell es la frecuencia, no la presencia. Y al devolver el verbo corto no se pierden por el camino los adjetivos del original.
**Linter:** `ES-COPULA-01`.

### 9. «No solo X, sino Y» y negaciones truncadas al final

**Qué falla:** la correlación «no solo… sino también» es en español una estructura marcada y de registro alto, así que su repetición canta mucho más que en inglés. La segunda mitad del patrón es el remate elíptico calcado: el esquema «Sin + sustantivo o infinitivo» como oración autónoma se lee como traducción literal antes que como énfasis.
**Qué vigilar:** no solo… sino también, no se trata solo de X sino de Y, más que X es Y, no es X: es Y; Sin adivinar. Sin fricción. Sin sorpresas.
**Antes:**
> No se trata solo del ritmo que sostiene la voz: es parte de la agresividad y de la atmósfera del tema. No es simplemente una canción, es una declaración de intenciones.
>
> [negación truncada] Las opciones salen del elemento seleccionado. Sin adivinar.

**Después:**
> El ritmo que sostiene la voz forma parte de la agresividad y de la atmósfera del tema.
>
> [negación truncada] Las opciones salen del elemento seleccionado, así que no hay que adivinar.

**No marcar:** la antítesis es una figura legítima y antigua. Cuando el primer término es una tesis que alguien sostiene de verdad y el texto la ha citado antes, la construcción hace trabajo argumentativo real: «No es un problema de presupuesto, como sostiene el informe: es de calendario». Tampoco se prohíben «Y punto.» ni «Así de simple.», coloquialismos españoles muy anteriores a los modelos: solo cuentan cuando cierran una ristra de frases sin verbo (patrón 31). Al convertir la elipsis en cláusula con verbo no se nombra a un agente que la fuente no nombra.
**Linter:** `ES-PARAL-01`.

### 10. Tríadas forzadas

**Qué falla:** todo llega en grupos de tres, sobre todo en adjetivos coordinados y en enumeraciones abstractas de cierre.
**Qué vigilar:** rápida, sencilla y segura; ágil, flexible y escalable; innovación, inspiración e ideas.
**Antes:**
> El encuentro incluye ponencias magistrales, mesas redondas y oportunidades de networking. Los asistentes encontrarán innovación, inspiración y ideas del sector.

**Después:**
> El encuentro incluye ponencias magistrales, mesas redondas y espacios para hablar con otros profesionales del sector.

**No marcar:** una enumeración de tres miembros concretos y específicos no es una tríada vacía; es una enumeración («Traía el pelo mojado, los zapatos en la mano y una excusa que no se creía ni él»). Lo que se marca son los tríos de abstracciones intercambiables. Al deshacer la tríada se conservan los sustantivos con sus modificadores: no se recorta «ponencias magistrales» a «ponencias».
**Detalle útil para detectar:** la conjunción cambia a «e» ante palabra que empieza por el sonido /i/, así que un «innovación, inspiración y ideas» delata a menudo que el modelo copió la plantilla inglesa. Las excepciones están en el patrón 54: no se «corrige» «madera y hierro».
**Linter:** `ES-TRIADA-01`.

### 11. Sinónimos giratorios, epítetos perifrásticos y aperturas repetidas

**Qué falla:** la rotación de sinónimos es más fuerte en español porque la escuela enseña a evitar repeticiones, así que el modelo produce el epíteto perifrástico del periodismo deportivo y cultural. La segunda mitad del patrón se desplaza: en español el objetivo principal no es el sujeto repetido sino la repetición de conectores iniciales y de estructuras verbo-inicial en serie.
**Qué vigilar:** el conjunto blanco, el astro argentino, el escritor bonaerense, la que fuera ministra, el también productor; Además,… Además,… Asimismo,… Por otro lado,…
**Antes:**
> [sinónimos] El protagonista se enfrenta a numerosos obstáculos. El personaje principal debe superar sus miedos. La figura central acaba triunfando. El héroe regresa a casa.
>
> [aperturas repetidas] Además, el ayuntamiento amplió el horario. Además, contrató a dos técnicos. Asimismo, reforzó la limpieza. Por otro lado, revisó el contrato.

**Después:**
> [sinónimos] El protagonista se enfrenta a numerosos obstáculos, debe superar sus miedos, acaba triunfando y regresa a casa.
>
> [aperturas repetidas] El ayuntamiento amplió el horario, contrató a dos técnicos y reforzó la limpieza. También revisó el contrato.

**No marcar:** la repetición deliberada de una apertura para construir ritmo o presión es un recurso, no un defecto («Esperé. Esperé toda la tarde, y luego toda la noche»). Se cambia solo cuando no aporta nada. Al fundir las frases no se altera la modalidad de cada predicado: si el original dice «debe superar sus miedos», la versión fundida sigue diciéndolo. El pronombre sujeto repetido tiene su propio patrón, el 44, con sus propias excepciones.

### 12. Falsos rangos «desde X hasta Y»

**Qué falla:** se presentan como extremos de una escala dos elementos que no lo son.
**Qué vigilar:** desde… hasta, que van desde… hasta, que abarca desde… hasta, tanto… como…
**Antes:**
> Nuestro viaje por el universo nos ha llevado desde la singularidad del Big Bang hasta la gran red cósmica, desde el nacimiento y la muerte de las estrellas hasta la enigmática danza de la materia oscura.

**Después:**
> El recorrido abarca el Big Bang, la red cósmica, el nacimiento y la muerte de las estrellas y la materia oscura.

**No marcar:** un rango real se deja. Al convertir el falso rango en enumeración no se cambia el soporte del que se habla: un recorrido no se convierte en un libro ni un texto en una conferencia.
**Nota tipográfica:** en los intervalos numéricos reales el español usa el guion o la fórmula «de 10 a 20» («págs. 23-45»). La semirraya no está proscrita por la Academia y algunos manuales hispanos la emplean, pero en este skill el guion es la norma de la casa, por coherencia con el patrón 14.

### 13. Pasiva perifrástica calcada del inglés

**Qué falla:** el español apenas usa la pasiva perifrástica «ser + participio» en prosa corriente: lo natural es la pasiva refleja o el impersonal con «se». Cuando el modelo escribe «los resultados son preservados automáticamente», la corrección muchas veces no es la voz activa sino la pasiva refleja, que es perfectamente idiomática. Se añade el abuso de «por parte de» como muleta para reintroducir el agente.
**Qué vigilar:** fue celebrada, son preservados, es realizada, por parte de.
**Antes:**
> No se requiere ningún archivo de configuración. Los resultados son preservados de forma automática por el sistema y la validación es realizada por parte del servidor.
>
> [sobreproducción] El puente fue construido por la empresa en 2019 y fue inaugurado por el alcalde en marzo.

**Después:**
> No hace falta ningún archivo de configuración: el sistema guarda los resultados automáticamente y el servidor realiza la validación.
>
> [sobreproducción] La empresa construyó el puente en 2019 y el alcalde lo inauguró en marzo.

**No marcar:** la pasiva perifrástica es correcta y a veces obligatoria: cuando el agente se expresa y es relevante (la refleja no admite complemento agente, «se construyó por la empresa» es agramatical), en registro jurídico y periodístico («El acusado fue absuelto»), y cuando el paciente es persona y la refleja daría lectura reflexiva o recíproca («los rehenes fueron liberados» no es «se liberaron»). Umbral operativo: marcar a partir de dos «ser + participio» en el mismo párrafo o de tres en cien palabras. El objetivo es la proporción, no la erradicación. Tampoco es defecto omitir el sujeto pronominal, que en español es la norma: eso solo se señala cuando de verdad se oculta al responsable («se decidió recortar la plantilla» sin decir quién). Y si el original no nombra al agente, la versión limpia tampoco puede nombrarlo: se usa pasiva refleja o impersonal.

---

## Estilo y tipografía

### 14. Raya y semirraya: uso anglicado

**Qué falla:** la prohibición inglesa no es trasladable. En español la raya es un signo prescrito por la RAE y en dos usos es insustituible: el diálogo y la aclaración dentro de un texto que ya lleva paréntesis. Lo que marca máquina es el uso anglicado.
**Qué vigilar:** (1) raya pegada por los dos lados al estilo inglés («instituciones—no los habitantes»); (2) raya con espacio a ambos lados o doble guion; (3) raya donde el español pondría coma, paréntesis o dos puntos, y varios incisos en un mismo párrafo; (4) semirraya fuera de un intervalo numérico. La regla española es raya sin espacio hacia el inciso y con espacio hacia el resto del enunciado: si el inciso va en medio se abre y se cierra («las instituciones —no los habitantes— lo promueven»), y si va al final, la raya de cierre se suprime y basta el punto.
**Antes:**
> El término lo promueven sobre todo las instituciones neerlandesas—no los propios habitantes. Nadie escribe «Países Bajos, Europa» en una dirección—y aun así el error—presente incluso en documentos oficiales—se repite. La nueva norma — anunciada sin previo aviso — afecta a miles de trabajadores, y los cambios -- exigidos desde hace años -- entran en vigor de inmediato.

**Después:**
> El término lo promueven sobre todo las instituciones neerlandesas, no los propios habitantes. Nadie escribe «Países Bajos, Europa» en una dirección y, aun así, el error se repite incluso en documentos oficiales. La nueva norma, anunciada sin previo aviso, afecta a miles de trabajadores, y los cambios, exigidos desde hace años, entran en vigor de inmediato.

**No marcar:** la raya de diálogo y el inciso del narrador, que son ortografía novelística obligatoria («—No me mires así —dijo ella, y apagó el cigarrillo contra el plato—. No pienso volver»). Tampoco el intervalo numérico ni un inciso correcto por párrafo. El guion corto entre espacios como inciso sí se sustituye: es hábito de máquina de escribir, no ortografía española.
**Regla operativa:** antes de entregar, buscar la raya, la semirraya y el doble guion; conservar las rayas de diálogo y, como mucho, un inciso por párrafo con el espaciado correcto; convertir el resto en coma, paréntesis, dos puntos o punto.
**Linter:** `ES-RAYA-01` (ERROR), `ES-RAYA-03` (ERROR), `ES-RAYA-02`, `ES-GUION-01`.

### 15. Exceso de negrita

**Qué falla:** la negrita decorativa, que no depende de la lengua. Detalle ortográfico español que conviene corregir a la vez: el desarrollo de una sigla va en minúscula cuando es una descripción común, mientras que el modelo lo calca del inglés con mayúscula en todas las palabras.
**Qué vigilar:** varias palabras en negrita por párrafo; siglas desarrolladas con mayúscula inicial en cada palabra.
**Antes:**
> Combina **OKR (Objetivos y Resultados Clave)**, **KPI (Indicadores Clave de Rendimiento)** y herramientas visuales de estrategia como el **Business Model Canvas (BMC)** y el **Cuadro de Mando Integral (CMI)**.

**Después:**
> Combina OKR (objetivos y resultados clave), KPI (indicadores clave de rendimiento) y herramientas visuales de estrategia como el Business Model Canvas (BMC) y el cuadro de mando integral (CMI).

**No marcar:** los nombres propios y las denominaciones extranjeras citadas como tales conservan su mayúscula («Business Model Canvas»), mientras que su equivalente descriptivo en español va en minúscula («cuadro de mando integral»). El tratamiento asimétrico es correcto: «el business model canvas» no lo escribe ningún editor español. Regla no negociable: quitar negrita no autoriza a quitar contenido, y las siglas entre paréntesis son información.

### 16. Listas con microtítulos en negrita

**Qué falla:** cada punto empieza con un rótulo en negrita que repite la primera palabra del punto, lo que deja la frase tautológica. Detalle español: tras los dos puntos del microtítulo se escribe minúscula, y el modelo suele poner mayúscula por calco.
**Qué vigilar:** viñetas del tipo `**Rendimiento:** El rendimiento se ha optimizado…`
**Antes:**
> - **Experiencia de usuario:** La experiencia de usuario mejora notablemente con una nueva interfaz.
> - **Rendimiento:** El rendimiento se ha optimizado mediante nuevos algoritmos.
> - **Seguridad:** La seguridad se refuerza con cifrado de extremo a extremo.

**Después:**
> La experiencia de usuario mejora con una nueva interfaz, el rendimiento se ha optimizado mediante nuevos algoritmos y la seguridad se refuerza con cifrado de extremo a extremo.

**No marcar:** una lista real, con elementos que no se dejan fundir en un periodo, es una lista y se queda. Al fundir no se inventa el sujeto que la lista no tenía: si en los tres puntos no hay ninguna actualización, versión ni lanzamiento, la frase resultante tampoco puede tenerlos.
**Linter:** `ES-MAYUS-01`.

### 17. Mayúsculas iniciales en titulares y otras mayúsculas calcadas

**Qué falla:** el «title case» sencillamente no existe en español: la ortografía académica prescribe que en títulos y epígrafes solo van en mayúscula la primera palabra y los nombres propios. En inglés es una convención legítima; en español es siempre un calco, y la mayúscula en «Y», «De» o «El» dentro del titular lo confirma. El patrón se amplía a las demás mayúsculas calcadas: meses y días, gentilicios e idiomas, estaciones, cargos, nombres de disciplina, tratamiento corporativo («nuestro Cliente», «el Proyecto») y mayúscula después de dos puntos. Y en dirección contraria: las mayúsculas llevan tilde, también en versales, y el modelo aplica una regla tipográfica inglesa inexistente en español según la cual no se acentúan.
**Qué vigilar:** titular con cuatro o más palabras y tres o más no iniciales en mayúscula sin ser nombres propios; Enero, Lunes, Español, Francés, el Presidente, el Director General, Inteligencia Artificial; «Nota: Los precios…»; ANALISIS, SITUACION, AMERICA.
**Antes:**
> ## Negociaciones Estratégicas Y Alianzas Globales En El Mercado Español
>
> Desde el pasado Lunes 3 de Enero, el equipo Español negocia con el Director General.
>
> [tras dos puntos] Nota: Los precios incluyen IVA. Importante: Revisa la configuración antes de continuar.
>
> [versales] ## ANALISIS DE LA SITUACION ECONOMICA EN AMERICA LATINA

**Después:**
> ## Negociaciones estratégicas y alianzas globales en el mercado español
>
> Desde el pasado lunes 3 de enero, el equipo español negocia con el director general.
>
> [tras dos puntos] Nota: los precios incluyen IVA. Importante: revisa la configuración antes de continuar.
>
> [versales] ## ANÁLISIS DE LA SITUACIÓN ECONÓMICA EN AMÉRICA LATINA

**No marcar.** Conservan la mayúscula los nombres propios, marcas y productos (Instagram, Google Ads, Banco Santander), las siglas, las instituciones y organismos (Ministerio de Economía, Universidad de Salamanca), los títulos de obras (Cien años de soledad) y los títulos en inglés citados como tales (The Lean Startup). De ahí que en «ministro de Economía» el cargo vaya en minúscula y el organismo en mayúscula. También mantienen mayúscula las festividades y fechas convertidas en nombre propio (Navidad, el Dos de Mayo), los periodos históricos (la Revolución Industrial) y el uso protocolario en documentos oficiales. Los nombres de disciplina van en minúscula en su uso común («estudia inteligencia artificial») y en mayúscula cuando designan asignaturas o titulaciones («aprobó Biología», «licenciado en Ingeniería Informática»): son usos distintos, no una contradicción.

La mayúscula tras dos puntos es correcta al introducir una cita en estilo directo, tras el saludo de una carta cuando el texto sigue en línea aparte, cuando los dos puntos preceden a un bloque o a una enumeración en líneas independientes, y siempre ante nombre propio, sigla o número («Responsable: María Ruiz», «Formato: JSON»). Lo que se corrige es el rótulo seguido de texto en la misma línea.

Las siglas y acrónimos en mayúsculas no llevan tilde (CIA, ONU, OTAN, DNI, PIB), aunque sí la llevan cuando se lexicalizan en minúscula (láser, módem). Tampoco se acentúan los números romanos ni el texto en otras lenguas. Nunca se tocan las mayúsculas dentro de código, identificadores, constantes, claves de configuración, nombres de menú o rutas citadas literalmente («Ajustes > Privacidad»).

Bajar una mayúscula no es motivo para tocar nada más de la frase: los deícticos temporales del original («el pasado lunes») se conservan.
**Severidad:** prohibición dura.
**Linter:** `ES-TITULO-01` (ERROR), `ES-TITULO-02`, `ES-FECHA-01`, `ES-MAYUS-01`.

### 18. Emojis decorativos

**Qué falla:** emojis de adorno en epígrafes y viñetas, independientes de la lengua.
**Qué vigilar:** pictograma al principio de una viñeta o de un encabezado.
**Antes:**
> 🚀 **Fase de lanzamiento:** el producto sale en el tercer trimestre
> 💡 **Idea clave:** los usuarios prefieren la simplicidad
> ✅ **Próximos pasos:** concertar una reunión de seguimiento

**Después:**
> El producto sale en el tercer trimestre. Los usuarios prefieren la simplicidad. Próximos pasos: concertar una reunión de seguimiento.

**No marcar:** el emoji dentro de una cita literal o de un mensaje reproducido. Al deshacer la lista se respeta la puntuación española (dos puntos y minúscula, signos de apertura donde haga falta) y se conserva el texto de la etiqueta tal cual estaba, incluido su número: «Próximos pasos», no «Siguiente paso».
**Linter:** `ES-EMOJI-01`.

### 19. Comillas: jerarquía y puntuación

**Qué falla:** el español tiene una jerarquía propia de tres niveles, «angulares» en primero, “inglesas” en segundo y ‘simples’ en tercero, y la puntuación va fuera del cierre. El modelo escribe la comilla recta del teclado inglés, repite el mismo tipo al anidar (con lo que la cita interior queda indistinguible de la exterior) y mete el punto o la coma dentro del cierre al estilo americano.
**Qué vigilar:** mezcla de niveles, anidamiento del mismo tipo de comilla, punto o coma dentro del cierre.
**Antes:**
> El director afirmó que “el proyecto va según lo previsto.” Otros miembros del equipo lo niegan.
>
> [anidamiento] Lo llamó "el mejor trimestre" y añadió: "fue una "sorpresa" para todos".

**Después:**
> El director afirmó que «el proyecto va según lo previsto». Otros miembros del equipo lo niegan.
>
> [anidamiento] Lo llamó «el mejor trimestre» y añadió: «Fue una “sorpresa” para todos».

**No marcar.** La comilla de primer nivel es parámetro de variedad y de manual de estilo, no norma única: en México, Argentina, Chile y buena parte de América, “ ” es el primer nivel dominante y es plenamente correcto, y en web, documentación y texto plano se admiten las rectas. No se impone « » a un texto ya coherente con otra convención, y una regla que marque “ ” debe desactivarse en cuanto el documento use « » como segundo nivel. Sí van dentro del cierre los signos que pertenecen al enunciado entrecomillado: interrogación, exclamación y puntos suspensivos de una elisión; el punto que cierra el período va siempre fuera. Nunca se tocan las comillas dentro de código, JSON, expresiones regulares, rutas, nombres de archivo ni cadenas literales, donde la comilla recta es funcional. El estilo español admite citas anidadas complejas cuando cada nivel usa su signo: «Me dijo, y cito: “no vuelvas a llamarme ‘cariño’ delante de mi madre”».
**Marcador estable:** lo que sí es error en cualquier variedad es anidar el mismo tipo de comilla en dos niveles, mezclar tres convenciones en un documento y meter la puntuación dentro del cierre.
**Linter:** `ES-COMILLAS-01`, `ES-COMILLAS-02`.

---

## Artefactos de chatbot

### 20. Restos de chatbot en el texto

**Qué falla:** el saludo, el ofrecimiento y la despedida del turno conversacional se quedan pegados al texto entregado. «Aquí tienes» es probablemente el resto más frecuente en español.
**Qué vigilar:** ¡Claro!, ¡Claro que sí!, Por supuesto, Aquí tienes…, A continuación te presento…, Espero que te sirva, Espero que esto te ayude, Si necesitas algo más dímelo, ¿Quieres que amplíe algún apartado?, ¿Te lo desarrollo?, En resumen, y para terminar…
**Antes:**
> ¡Claro que sí! Aquí tienes un resumen de la Revolución francesa. La Revolución francesa empezó en 1789, cuando la crisis financiera y la escasez de alimentos desataron el descontento popular. Espero que te sirva. ¿Quieres que amplíe algún apartado?

**Después:**
> La Revolución francesa empezó en 1789, cuando la crisis financiera y la escasez de alimentos desataron el descontento popular.

**No marcar:** el saludo y la despedida de una carta o de un correo real dirigido a una persona concreta, donde son cortesía normal y esperada. Las fórmulas de apertura y cierre epistolares son siglos anteriores a los chatbots. Se borra el marco conversacional; el contenido se conserva íntegro.
**Linter:** `ES-BOT-02` (ERROR).

### 21. Avisos sobre el límite de conocimiento y conjeturas

**Qué falla:** el texto declara que no dispone de información y a continuación rellena el hueco con una conjetura presentada como hecho.
**Qué vigilar:** hasta mi última actualización, a fecha de hoy, si bien la información disponible es limitada, según la información disponible, no consta públicamente, todo apunta a que, es probable que, cabe suponer que, mantiene un perfil bajo, prefiere mantener su vida privada al margen.
**Antes:**
> Si bien los detalles sobre la fundación de la empresa no están ampliamente documentados en las fuentes disponibles, todo apunta a que se constituyó en algún momento de los años noventa.

**Después:**
> Las fuentes disponibles no documentan la fundación de la empresa.

**No marcar:** las limitaciones útiles y los avisos reales se conservan: alcance de un estudio, notas legales y de seguridad, correcciones. Se puede decir que la fuente no documenta algo; lo que no se puede es rellenar el hueco. Y el hueco se describe con el mismo alcance que tenía: si el original habla de «los detalles de la fundación», la versión limpia no lo estrecha a «la fecha».
**Linter:** `ES-BOT-01` (ERROR).

### 22. Tono excesivamente complaciente

**Qué falla:** el texto abre elogiando a su interlocutor. En español peninsular el halago inicial suena todavía más impostado en registro escrito profesional que en inglés, donde «Great question» es casi una muletilla de conversación.
**Qué vigilar:** ¡Excelente pregunta!, ¡Muy buena pregunta!, Tienes toda la razón, Estás en lo cierto, Muy buen apunte, Me encanta que lo plantees así, Vas por muy buen camino.
**Antes:**
> ¡Excelente pregunta! Tienes toda la razón: es un tema complejo. Y muy buen apunte el de los factores económicos, que aquí pesan más que los regulatorios.

**Después:**
> Los factores económicos pesan aquí más que los regulatorios.

**No marcar:** el acuerdo argumentado, que no es halago. Advertencia operativa: si al quitar los elogios no queda ninguna afirmación, el resultado correcto es que no quede nada. Sintetizar una respuesta a partir del halago es exactamente la fabricación que este skill persigue.

---

## Relleno y atenuación

### 23. Muletillas, perífrasis y lenguaje administrativo

**Qué falla:** el relleno español no viene del inglés sino del lenguaje administrativo, así que la tabla de equivalencias hay que rehacerla entera.
**Qué vigilar.** Equivalencias directas: con el objetivo de → para; debido al hecho de que → porque; en el momento actual → ahora; en el caso de que → si; tiene la capacidad de → puede; es importante destacar que → nada. Tics propios del español: «proceder a + infinitivo» («se procedió a la revisión» → «se revisó»), «por parte de» (patrón 13), «a nivel de» como comodín («a nivel de presupuesto» → «en el presupuesto»), «de cara a» → para, «en relación con» y «con respecto a» cuando basta una preposición, «no dudes en + infinitivo» → el verbo solo, y las nominalizaciones vacías («llevar a cabo la implementación de» → implementar). Caso aparte por su frecuencia: «el mismo, la misma, los mismos, las mismas» como pronombre anafórico burocrático, uso que la Academia desaconseja por innecesario y porque deja el referente más lejos, no más cerca.
**Antes:**
> Con el objetivo de conseguir este fin, y debido al hecho de que en el momento actual el sistema tiene la capacidad de procesar los expedientes, es importante destacar que se procedió a la revisión de los mismos por parte del equipo. En el caso de que necesites consultarlo a nivel de presupuesto, no dudes en comunicárnoslo.
>
> [anafórico] Recibimos la solicitud y procedimos a la revisión de la misma; el interesado será informado del resultado de la misma.

**Después:**
> Para conseguirlo, y como ahora el sistema puede procesar los expedientes, el equipo los revisó. Si necesitas consultarlo en el presupuesto, dínoslo.
>
> [anafórico] Recibimos la solicitud y la revisamos; se informará al interesado del resultado.

**No marcar:** «mismo» como adjetivo de identidad o de énfasis, que es correcto y nunca se toca: «el mismo día», «la misma persona», «ella misma lo dijo», «vive en Madrid mismo», «al mismo tiempo», «el mismo informe que citaste». Solo se corrige cuando sustituye a un pronombre, a un posesivo o a un demostrativo, es decir, cuando puede borrarse o sustituirse por un clítico sin añadir nada. «No dude en ponerse en contacto con nosotros» es cortesía establecida en carta, correo formal y atención al cliente por escrito, sobre todo en España, y ahí se deja; lo que desentona es esa fórmula en un mensaje de chat o en una nota interna.
**Regla antifabricación:** acortar no es añadir. El acto de habla que aparezca en la versión breve (una petición, un aviso) tiene que estar ya en el original, y la persona y la modalidad se conservan: un impersonal («será informado») pasa a «se informará», no a «informaremos».
**Linter:** `ES-MISMO-01`.

### 24. Exceso de matizadores

**Qué falla:** se apilan coberturas que solo sirven para reparar una exageración anterior. En español el encadenamiento de subjuntivo y condicional multiplica la sensación de vaguedad.
**Qué vigilar:** podría llegar a, cabría argumentar que, en cierta medida, hasta cierto punto, en algunos casos podría, quizá, tal vez, no es descartable que, todo parece indicar que, para ser justos, dicho esto.
**Antes:**
> Podría llegar a argumentarse que, en cierta medida, la medida quizá tenga algún tipo de efecto sobre los resultados.

**Después:**
> La medida puede afectar a los resultados.

**No marcar:** el matizador que la fuente respalda. Y hay un límite estricto: se poda la pila, pero no se sube la afirmación de posible a segura. Si el original dice que algo podría pasar, la versión limpia dice que puede pasar, no que pasa.
**Linter:** `ES-HEDGE-01` (tres o más coberturas en la misma oración).

### 25. Cierres optimistas genéricos

**Qué falla:** el último párrafo no dice nada y solo tranquiliza.
**Qué vigilar:** El futuro se presenta prometedor, Se abre una etapa apasionante, Sin duda, un paso en la dirección correcta, Solo el tiempo lo dirá, Queda mucho camino por recorrer, El futuro, sin duda, es esperanzador.
**Antes:**
> La compañía cerró el ejercicio con 120 empleados y tres sedes. El futuro se presenta prometedor. Se abre una etapa apasionante en su camino hacia la excelencia. Sin duda, un paso en la dirección correcta.

**Después:**
> La compañía cerró el ejercicio con 120 empleados y tres sedes.

**No marcar:** los planes que la fuente recoge, con sus fechas y sus cifras. Se corta el párrafo y se termina en el último dato concreto; no se inventan fechas ni cifras para sustituir el cierre. Si no hay ningún dato antes del remate, el apartado se queda sin remate.
**Linter:** `ES-CIERRE-01`.

### 26. Guion mal puesto: prefijos, siglas y compuestos calcados

**Qué falla:** el patrón inglés de los modificadores compuestos no tiene equivalente, porque el español no forma modificadores con guion. El hueco lo ocupa el fenómeno emparentado y muy productivo: el guion puesto donde la ortografía académica exige univerbación. La RAE prescribe unir el prefijo a la base cuando esta es una sola palabra (preventa, antifraude, cofundador, expresidente, multicanal, sociocultural, posventa), separarlo con espacio y sin guion cuando la base es pluriverbal (ex primer ministro, anti pena de muerte, pro derechos humanos), y reservar el guion para prefijo más sigla o mayúscula (anti-OTAN, pos-COVID) y para gentilicios en oposición (hispano-francés). La segunda mitad del hueco la ocupa la acumulación de locuciones participiales que hacen el trabajo del compuesto inglés.
**Qué vigilar:** pre-venta, anti-fraude, co-fundador, ex-director, ex-primer ministro; basado en datos, orientado a resultados, centrado en el cliente, impulsado por IA, de extremo a extremo, apiladas de tres en tres.
**Antes:**
> El equipo multi-disciplinar presentó un informe data-driven al co-fundador y al ex-director durante la pre-venta del producto anti-fraude. Es una solución end-to-end, customer-centric y data-driven.

**Después:**
> El equipo multidisciplinar presentó un informe basado en datos al cofundador y al exdirector durante la preventa del producto antifraude. Es una solución de extremo a extremo que se centra en el cliente y trabaja con datos.

**No marcar:** el guion legítimo ante sigla, ante mayúscula y en gentilicios en oposición. La corrección de la pila de participios es desapilarla con un verbo, no traducirlas una a una.

### 27. Fingir que se revela una verdad profunda

**Qué falla:** se anuncia una revelación y detrás va una afirmación trivial que se sostiene sola.
**Qué vigilar:** La verdadera pregunta es, En el fondo, En esencia, Lo que realmente importa es, El quid de la cuestión, El verdadero problema de fondo, La clave está en, Aquí está el meollo.
**Antes:**
> La verdadera pregunta es si los equipos serán capaces de adaptarse. En el fondo, lo que realmente importa es la madurez organizativa.

**Después:**
> La pregunta es si los equipos serán capaces de adaptarse. Lo que importa es la madurez organizativa.

**No marcar:** quitar «realmente» y «en el fondo» no autoriza a convertir una afirmación de importancia en una relación de causa o de dependencia que el original no establecía.

### 28. Anunciar lo que se va a decir

**Qué falla:** el texto anuncia el contenido en vez de darlo.
**Qué vigilar:** Vamos a sumergirnos en, Vamos a adentrarnos en, Desglosémoslo, Vamos por partes, Esto es lo que necesitas saber, Sin más preámbulos, Veamos, Analicemos, Antes de nada, Un apunte rápido, Ojo con esto.
**Antes:**
> Vamos a sumergirnos en el funcionamiento de la caché en Next.js. Esto es lo que necesitas saber: Next.js guarda datos en caché en varias capas, entre ellas la memorización de peticiones y la caché del router.
>
> [registro coloquial] Una cosa que me costó un disgusto, así que atención a esta parte: el servidor de desarrollo de webpack no envía la cabecera CORS por defecto.

**Después:**
> Next.js guarda datos en caché en varias capas, entre ellas la memorización de peticiones y la caché del router.
>
> [registro coloquial] El servidor de desarrollo de webpack no envía la cabecera CORS por defecto.

**No marcar:** la versión coloquial no se salva por ser coloquial: hay que quitar el anuncio, no solo bajarle el registro. «Sumergirse» y «adentrarse» son el equivalente español de «delve», así que este patrón y el 7 se solapan.

### 29. El titular repetido en la primera frase

**Qué falla:** el apartado abre con una frase eco que repite el título en forma sentenciosa.
**Qué vigilar:** La velocidad importa, La seguridad es fundamental, Hablemos de rendimiento.
**Antes:**
> ## Rendimiento
>
> La velocidad importa.
>
> Cuando una página tarda en cargar, el usuario se va.

**Después:**
> ## Rendimiento
>
> Cuando una página tarda en cargar, el usuario se va.

**No marcar:** el titular se deja como está. Se elimina la frase eco y el apartado arranca en el contenido real.

### 30. Escribir sobre la versión anterior

**Qué falla:** la documentación describe el comportamiento actual; el pasado va en changelogs, notas de versión y guías de migración.
**Qué vigilar:** anteriormente, antes se hacía, se ha sustituido el enfoque anterior, a diferencia de la versión previa, ya no es necesario.
**Antes:**
> Esta función se añadió para sustituir el enfoque anterior, que recorría todos los elementos con un coste O(n²). Ahora usa un mapa hash.

**Después:**
> Esta función usa un mapa hash para localizar los elementos sin recorrerlos todos.

**No marcar:** en un changelog o en una guía de migración la comparación es el contenido y se queda. Al borrar la comparación desaparece también la métrica que solo describía al enfoque viejo, y no se introducen estructuras de datos ni complejidades que el original no nombrara.

### 31. Golpes de efecto y frases nominales encadenadas

**Qué falla:** la prosa española tolera periodos largos y usa la coordinación y la subordinación donde el inglés corta, así que una ristra de frases nominales sin verbo se lee como traducción literal de copy inglés antes que como énfasis.
**Qué vigilar:** tres o más frases sin verbo seguidas, con o sin remate.
**Antes:**
> Entonces llegó AlphaEvolve. Sin preferencia por la simetría. Sin prejuicios estéticos. Sin nostalgia por el gusto humano. Las reglas de antes dejaron de servir. Así de simple.

**Después:**
> AlphaEvolve no tenía preferencia por la simetría, ni prejuicios estéticos, ni nostalgia por el gusto humano, y desde su llegada las reglas anteriores dejaron de servir.

**No marcar:** una frase corta aislada para dar énfasis, y los remates coloquiales después de un argumento real. «Así de simple.», «Y punto.», «Nada más.», «Ni más ni menos.», «Fin de la historia.», «Y ya está.» son expresiones idiomáticas del español coloquial y no son un tell en sí mismas: lo que delata al modelo es su uso como cierre automático de una cadena de fragmentos. Al refundir se conservan todos los miembros de la enumeración y no se fusionan dos en uno.

### 32. Sentencias formulaicas

**Qué falla:** una metáfora de plantilla sustituye a la afirmación concreta.
**Qué vigilar:** X es el nuevo Y, X es el lenguaje de Y, X es la moneda de cambio de Y, X no es una herramienta es un espejo, la arquitectura de, el ADN de, X se convierte en una trampa, no es cuestión de X sino de Y.
**Antes:**
> La simetría es el lenguaje de la confianza. La eficiencia se convierte en una trampa cuando los equipos olvidan la capa humana.

**Después:**
> Los equipos que solo persiguen la eficiencia olvidan la parte humana.

**No marcar:** cuando la sentencia no resume ninguna afirmación recuperable, como en las metáforas identificativas del tipo «X es el lenguaje de Y», el resultado correcto es borrarla, no traducirla a un enunciado con sujeto, público y efecto inventados. La última plantilla de la lista se solapa con el patrón 9.

### 33. Aperturas de falsa sinceridad

**Qué falla:** una pausa teatral en posición inicial anuncia sinceridad antes de una respuesta ordinaria. «¿La verdad?» como pregunta suelta es traducción literal de «Honestly?» y prácticamente no aparece en textos escritos por hablantes.
**Qué vigilar:** ¿La verdad?, Seamos sinceros, Vamos a ser honestos, Te voy a ser sincero, Mira, A ver, Sinceramente, Te lo digo claro, Sin rodeos.
**Antes:**
> ¿Merece la pena por ese precio? ¿La verdad? Depende de cuánto lo vayas a usar.

**Después:**
> Que merezca la pena por ese precio depende de cuánto lo vayas a usar.

**No marcar:** «mira», «oye» o «la verdad es que» dentro de la frase son normales en el español coloquial. Lo que se marca es la pausa teatral en posición inicial, no la palabra.

### 34. Responder a objeciones que nadie ha planteado

**Qué falla:** el texto se defiende de un interlocutor que no existe.
**Qué vigilar:** Que quede claro, No me malinterpretes, No estoy diciendo que, Ojo, no digo que, Esto no va tanto de, No es que X es que Y, Alguien podría objetar que… pero, Dicho esto.
**Antes:**
> Esto no va tanto de la longitud del prompt, y no estoy diciendo que la documentación no importe. Que quede claro: se podría enfocar de otra manera, pero la cuestión es si el agente puede usar la instrucción cuando actúa.

**Después:**
> La cuestión es si el agente puede usar la instrucción cuando actúa.

**No marcar:** la objeción con dueño. Si el texto dice de quién es la objeción o la responde entera, se conserva; lo mismo vale para las respuestas de un FAQ y para las réplicas en un debate. Se elimina solo la defensa sin interlocutor, y si dentro hay una afirmación real, se enuncia directamente.

### 35. Rechazar alternativas falsas

**Qué falla:** se levanta una opción que nadie propuso solo para descartarla.
**Qué vigilar:** Podría resultar tentador, Uno podría verse tentado de, Una opción evidente sería, Podrías pensar que… pero, Sería fácil limitarse a, Alguien podría sugerir, La solución obvia pasaría por.
**Antes:**
> Los tokens de sesión se rotan cada 24 horas. Podría resultar tentador rotarlos reiniciando el servicio de autenticación con un cron, pero eso tiraría todas las sesiones activas. La rotación se hace en caliente y los clientes se refrescan de forma transparente.

**Después:**
> Los tokens de sesión se rotan cada 24 horas en caliente, y los clientes se refrescan de forma transparente.

**No marcar:** una alternativa rechazada puede ser legítima. Se conservan las que un lector se plantearía de verdad en un documento de diseño o en un tutorial. La señal es la acumulación de rechazos breves y sin conexión, que suelen ser restos de una versión anterior del texto.

---

## Patrones exclusivos del español

Estos 34 patrones no existen en la taxonomía inglesa porque describen fenómenos que solo pueden darse en español: rección verbal, sistema pronominal átono, gerundio, tratamiento, acentuación, signos de apertura y variedad geográfica. Un revisor angloparlante no puede verlos.

### 36. Gerundio especificativo

**Qué falla:** el inglés usa la cláusula en -ing como modificador de nombre y el modelo la calca, colocando el gerundio donde el español exige una oración de relativo. La norma solo admite el gerundio como adjunto verbal, no como adjetivo que especifica a un sustantivo.
**Qué vigilar:** sustantivo seguido inmediatamente de gerundio: «una ley regulando», «un informe conteniendo», «un documento explicando».
**Antes:**
> Se aprobó una ley regulando el trabajo remoto y se envió un informe conteniendo las cifras.

**Después:**
> Se aprobó una ley que regula el trabajo remoto y se envió un informe que contiene las cifras.

**No marcar:** los lexicalizados «agua hirviendo», «clavo ardiendo», «pan ardiendo»; los pies de foto y epígrafes («Un hombre leyendo el periódico en la plaza»); el gerundio como predicativo con verbos de percepción y de representación («Vi a Marta saliendo del edificio», «La foto muestra al equipo celebrando»); y el gerundio jurídico con valor de acción en curso del propio sujeto («el Gobierno, actuando conforme a la ley, resolvió…»). Regla operativa: si el gerundio va inmediatamente detrás de un sustantivo y puede sustituirse por «que + verbo conjugado» sin cambiar nada más, es infracción.
**Severidad:** prohibición dura.

### 37. Titular con gerundio calcado del «-ing»

**Qué falla:** los títulos ingleses de blog y de sección son gerundios nominales. El español no nominaliza el gerundio, pero el corpus está lleno de traducciones automáticas de esos titulares, así que el modelo los reproduce en encabezados, índices y nombres de módulo.
**Qué vigilar:** línea de encabezado que empieza por gerundio: «Entendiendo X», «Construyendo Y», «Empezando con Z».
**Antes:**
> Entendiendo el algoritmo de Instagram

**Después:**
> Cómo entender el algoritmo de Instagram

**No marcar:** el titular con gerundio que forma una oración real con sujeto o perífrasis («Seguimos creciendo», «España está envejeciendo»), los pies de foto y los títulos de obras publicadas que se citan literalmente. La reescritura conserva el verbo del original: «Entendiendo X» pasa a «Cómo entender X», no a «Cómo funciona X», que afirmaría que el texto explica el funcionamiento, dato que el titular no daba.
**Severidad:** marcador de patrón.
**Linter:** `ES-TITULO-03`, que dispara solo sobre encabezado que empieza por gerundio.

### 38. Participio absoluto colgante en apertura

**Qué falla:** traducción mecánica de «Based on the data…» como apertura de oración. En inglés el participio suspendido es normal; en español «basado» debe concordar con un sustantivo, y al abrir la oración se queda sin referente, porque el sujeto que sigue no es lo que está basado en los datos. Es un anacoluto, no una preferencia de estilo.
**Qué vigilar:** Basado en…, Dado…, Considerando…, Habiendo dicho esto (calco de «That said»), seguidos de coma y de una oración cuyo sujeto no es el participio.
**Antes:**
> Basado en los datos del último trimestre, la demanda caerá un 8 %.

**Después:**
> Según los datos del último trimestre, la demanda caerá un 8 %.

**No marcar:** «basado en» es impecable cuando el participio concuerda con un sustantivo presente: «un modelo basado en datos», «una película basada en hechos reales», «la propuesta, basada en el informe anterior, se aprobó». También es correcto el gerundio referido al sujeto («El comité, basándose en los datos, decidió aplazar la votación») y el participio absoluto con sujeto propio («Terminada la reunión, salimos»).
**Severidad:** prohibición dura.
**Linter:** `ES-BASE-01`.

### 39. «En base a»

**Qué falla:** el modelo la aprende de textos administrativos y periodísticos traducidos, donde es frecuentísima, y la usa como conector de párrafo automático. Su densidad en la salida generada es muy superior a la de un autor humano y arrastra el registro hacia el boletín oficial.
**Qué vigilar:** «en base a» en posición de bisagra, sobre todo al empezar párrafo.
**Antes:**
> En base a esto, ajustaremos el presupuesto.

**Después:**
> A partir de esto, ajustaremos el presupuesto.

**No marcar:** esto es norma de la casa, no norma de la lengua. La locución está censurada por el Diccionario panhispánico de dudas y por Fundéu, pero está plenamente extendida en el español administrativo y jurídico de ambos lados del Atlántico y ningún diccionario la marca como incorrecta. No se trata como falta ni bloquea la entrega. El recambio depende de la variedad: en América y en registro jurídico, «con base en»; en España, «a partir de», «según», «sobre la base de», «conforme a». Nunca se toca dentro de una cita literal ni en el texto de una norma reproducida.
**Regla antifabricación:** se conserva el mismo deíctico o sintagma que había. Cambiar «en base a esto» por «a partir de esos datos» resuelve un referente que el original dejaba abierto.
**Severidad:** marcador de patrón.
**Linter:** `ES-BASE-01`.

### 40. «Está siendo + participio»

**Qué falla:** calco directo de «is being investigated». El español tiene «se está investigando» o la activa; la perífrasis existe pero es marcada y poco frecuente. El modelo la usa por defecto porque mapea uno a uno el tiempo inglés.
**Qué vigilar:** «está siendo», «están siendo» seguidos de participio en -ado o -ido.
**Antes:**
> El caso está siendo investigado por la fiscalía y los archivos están siendo revisados.

**Después:**
> La fiscalía investiga el caso y se están revisando los archivos.

**No marcar:** no es un error de norma, solo un tell estilístico: se mantiene cuando el agente es relevante y el paciente debe seguir siendo tema, sobre todo en titulares y crónica judicial. Y no se confunde con «estar siendo + adjetivo» («está siendo muy amable», «estás siendo injusto»), que es construcción legítima y distinta.
**Severidad:** marcador de patrón.
**Linter:** `ES-PASIVA-01`.

### 41. Dequeísmo

**Qué falla:** el modelo no tiene el régimen preposicional interiorizado y genera por analogía con las construcciones vecinas. El fenómeno abunda además en el habla y en los foros del corpus, y la IA lo reproduce sobre todo en registro pretendidamente formal, por hipercorrección.
**Qué vigilar:** «de que» tras pensar, creer, considerar, opinar, temer, decir, sostener (subordinada de complemento directo) y tras resultar, suceder, ocurrir, parecer, constar (subordinada de sujeto).
**Antes:**
> Pienso de que el informe llegará tarde y consideramos de que todavía hay margen.

**Después:**
> Pienso que el informe llegará tarde y consideramos que todavía hay margen.

**No marcar:** jamás se quita el «de» cuando el régimen lo exige: «estoy seguro de que», «me alegro de que», «me acuerdo de que», «se dio cuenta de que», «el hecho de que», «a pesar de que», «en el caso de que», «a condición de que», «estar convencido de que», «tener miedo de que». Tampoco entran aquí los verbos de doble régimen «informar (de) que», «advertir (de) que», «avisar (de) que», «dudar (de) que», donde ambas formas son correctas (patrón 42). Prueba de sustitución: si la pregunta correcta es «¿Qué piensas?» y no «¿De qué piensas?», sobra el «de».
**Severidad:** prohibición dura.
**Linter:** `ES-DEQUE-01`.

### 42. Queísmo

**Qué falla:** el reverso del anterior y el más frecuente en salida de IA. El inglés no marca preposición ante la subordinada, así que el modelo suprime el «de» que el verbo español exige. Es especialmente sistemático con «darse cuenta», «acordarse», «estar seguro» y «a pesar».
**Qué vigilar:** me di cuenta que, estoy seguro que, me acordé que, a pesar que, no cabe duda que.
**Antes:**
> Me di cuenta que el archivo estaba dañado y no me acordé que había una copia.

**Después:**
> Me di cuenta de que el archivo estaba dañado y no me acordé de que había una copia.

**No marcar:** los verbos de doble régimen, donde ambas formas son correctas según el Diccionario panhispánico de dudas: «informar (de) que», «advertir (de) que», «avisar (de) que», «dudar (de) que», «cuidar (de) que», «olvidarse (de) que». Tampoco se añade «de» a las construcciones impersonales o con «ser» más adjetivo sin sujeto personal: «es seguro que llegará» (frente a «estoy seguro de que llegará»), «está claro que», «resulta evidente que». Prueba de sustitución: si la pregunta correcta es «¿De qué te diste cuenta?», falta el «de».
**Severidad:** prohibición dura.
**Linter:** `ES-QUEISMO-01`.

### 43. Posesivo redundante con partes del cuerpo, prendas y parientes

**Qué falla:** el inglés obliga al posesivo; el español marca al poseedor con el dativo o el reflexivo y usa artículo. El modelo traduce el posesivo posición por posición y produce una duplicación que ningún hablante nativo escribe.
**Qué vigilar:** clítico reflexivo o dativo (me, te, se, nos, le, les) seguido de verbo, posesivo y sustantivo de partes del cuerpo o de prendas.
**Antes:**
> Se lavó sus manos, se puso su abrigo y le dio la mano a su interlocutor levantando su brazo derecho.

**Después:**
> Se lavó las manos, se puso el abrigo y le dio la mano a su interlocutor levantando el brazo derecho.

**No marcar:** el posesivo es obligatorio o natural cuando no hay reflexivo ni dativo que identifique al poseedor («Sus manos temblaban», «Su abrigo estaba en la silla»), cuando hay contraste o desambiguación («Le sujetó su mano, no la mía»), cuando el sustantivo lleva modificador («sus enormes manos agrietadas») y con parientes fuera de contexto reflexivo («Llamó a su hermana»).
**Severidad:** marcador de patrón.

### 44. Pronombre sujeto redundante

**Qué falla:** el inglés exige sujeto explícito; el español es lengua de sujeto nulo y lo expresa solo por contraste, énfasis o desambiguación. El modelo arrastra el sujeto obligatorio del inglés y salpica el texto de «yo creo», «nosotros pensamos», «ellos deberían», lo que suena a doblaje. Conviene decirlo con precisión: el pronombre repetido no es agramatical, solo redundante y marcado, y por eso hay que comprobar contraste y énfasis antes de borrarlo.
**Qué vigilar:** cadenas de pronombres correferentes en oraciones seguidas.
**Antes:**
> Yo creo que nosotros deberíamos revisar el contrato antes de que ellos lo firmen.

**Después:**
> Creo que deberíamos revisar el contrato antes de que lo firmen.

**No marcar:** el pronombre es necesario cuando hay contraste («Yo pago lo mío, tú pagas lo tuyo»), énfasis («Lo dijo él, no yo»), ambigüedad de persona en imperfecto, condicional o subjuntivo, donde primera y tercera coinciden («yo tenía», «si yo fuera»), coordinación de sujetos («Ella y yo lo revisamos»), y tras «también», «tampoco», «ni siquiera», «hasta», «incluso» («Tampoco yo lo sabía»). Tampoco en diálogo, donde el pronombre marca turno. Regla operativa: borrar solo el segundo y sucesivos pronombres correferentes de una misma cadena, y solo si el verbo ya identifica la persona sin ambigüedad.
**Severidad:** marcador de patrón.

### 45. «Él» y «ella» referidos a cosas

**Qué falla:** el inglés tiene un pronombre neutro para inanimados y el modelo busca un equivalente léxico. Como en español los pronombres tónicos de tercera persona llevan género, acaba escribiendo «ella» por «la impresora» en posición de sujeto, donde el español simplemente elide el sujeto.
**Qué vigilar:** «él», «ella», «ellos», «ellas» como sujeto justo después de punto, punto y coma o dos puntos, con antecedente inanimado cercano.
**Antes:**
> Compramos una impresora nueva; ella funciona mucho mejor que la anterior. El informe llegó ayer: él contiene tres anexos.

**Después:**
> Compramos una impresora nueva; funciona mucho mejor que la anterior. El informe llegó ayer: contiene tres anexos.

**No marcar:** con preposición, el pronombre tónico referido a cosas es plenamente correcto: «el archivo y todo lo que hay en él», «la caja y lo que había dentro de ella», «un problema y la solución para él». También es legítimo en personificación literaria y cuando el referente es un animal o una entidad tratada como persona (una empresa, un barco, una selección deportiva).
**Severidad:** marcador de patrón.

### 46. Leísmo, laísmo y loísmo fuera de norma

**Qué falla:** el sistema pronominal átono no se aprende por frecuencia superficial. El corpus mezcla variedades leístas de Castilla, laístas de Valladolid y sistemas etimológicos americanos; el modelo promedia y produce combinaciones que ningún sistema real usa. Los tres fenómenos están fuera de la norma en todas las variedades cultas.
**Qué vigilar:** laísmo («la dije»), loísmo verdadero, es decir «lo» o «los» en el lugar del dativo («Lo di las gracias», «Lo pegaron un tiro», «Los dije que vinieran»), y leísmo de cosa («al paquete le dejé»).
**Antes:**
> A María la dije que no viniera, al paquete le dejé en recepción y a mi hermano lo di las gracias.

**Después:**
> A María le dije que no viniera, el paquete lo dejé en recepción y a mi hermano le di las gracias.

**No marcar:** están admitidos y no se corrigen el leísmo de persona masculina singular («A Juan le vi ayer», junto a «lo vi»), el leísmo de cortesía con usted («Le saludo atentamente», «Le atenderemos enseguida») y el dativo obligatorio de gustar, interesar, importar, doler, parecer, bastar, convenir («A los clientes les interesa»). No es loísmo el «lo» neutro que remite a una oración o a un concepto («Lo sé», «Se lo dije», «Lo dijo el ministro»): la prueba es que no puede sustituirse por «le». El leísmo plural de persona masculina («A mis alumnos les felicité») se señala como observación y nunca se reescribe de forma automática: la RAE admite solo el singular, pero el plural es frecuentísimo en prosa peninsular editada. En citas literales y en diálogo que reproduce habla real no se corrige ninguno de los tres.
**Severidad:** prohibición dura.
**Linter:** `ES-LAISMO-01`.

### 47. Mezcla de tuteo, voseo y ustedeo

**Qué falla:** el modelo no mantiene un estado de tratamiento a lo largo del texto: cada oración se genera con el pronombre más probable en su vecindad léxica, y el corpus mezcla España, Río de la Plata y México. El resultado son imperativos y desinencias de tres sistemas conviviendo, a veces en un mismo párrafo.
**Qué vigilar:** en cada párrafo, el pronombre sujeto (tú, vos, usted, vosotros, ustedes), el posesivo (tu, su, vuestro), el clítico (te, le, os, les) y la desinencia verbal deben pertenecer al mismo sistema.
**Antes:**
> Si quieres mejorar tu perfil, complete el formulario y después vos podés compartirlo con vuestros contactos.

**Después:**
> Si quieres mejorar tu perfil, completa el formulario y después compártelo con tus contactos.

**No marcar:** el cambio de tratamiento en diálogos y citas de hablantes distintos, en textos dirigidos a dos destinatarios en bloques claramente separados (cuerpo tuteante y cláusulas legales de usted) y en material localizado donde el voseo o el «vosotros» son la variedad elegida. Se prohíbe la mezcla dentro de una misma línea de discurso. La reescritura adopta el tratamiento mayoritario del texto o el que fije el encargo; no introduce uno nuevo.
**Severidad:** prohibición dura.
**Linter:** `ES-TRATO-01`.

### 48. Segunda persona genérica calcada del «you» impersonal

**Qué falla:** el inglés usa «you» como impersonal en registro expositivo; el español culto prefiere «se», «uno» o el infinitivo. El modelo traduce el «you» literalmente y rompe el registro de un texto por lo demás impersonal.
**Qué vigilar:** «tú» genérico en informe, artículo académico, nota técnica o dictamen, o alternando con «se» y «uno» en el mismo párrafo.
**Antes:**
> Cuando lees el informe, ves que los datos no cuadran y entiendes por qué se retrasó el proyecto.

**Después:**
> Al leer el informe se ve que los datos no cuadran y se entiende por qué se retrasó el proyecto.

**No marcar:** en texto instructivo, publicitario, divulgativo o conversacional la apelación directa al lector es deliberada y correcta: «Descarga la plantilla y úsala» no se convierte en impersonal. Señal diagnóstica: el «tú» es genérico si puede sustituirse por «uno» o por «se» sin que el texto pierda destinatario; si el texto tiene destinatario real, no se toca.
**Severidad:** marcador de patrón.

### 49. Ausencia de los signos de apertura ¿ y ¡

**Qué falla:** el inglés solo tiene signo de cierre; además el modelo genera de izquierda a derecha y decide que la oración es interrogativa cuando ya ha emitido el principio. Es el error ortográfico más visible del español generado, y su normalización en redes refuerza el patrón.
**Qué vigilar:** oración que acaba en «?» o en «!» sin su signo de apertura.
**Antes:**
> Qué significa esto para tu negocio? Increíble, verdad!

**Después:**
> ¿Qué significa esto para tu negocio? ¡Increíble!, ¿verdad?

**No marcar:** el signo de apertura va donde empieza la pregunta o la exclamación, no siempre al principio de la oración: «Si vienes, ¿me avisas?», «Juan, ¿has terminado?». Un apéndice confirmativo tras exclamación se cierra primero y lleva sus propios signos: «¡Increíble!, ¿verdad?». La duplicación solo se admite cuando un mismo enunciado es a la vez interrogativo y exclamativo, y entonces los dos signos de apertura van juntos y los dos de cierre también: «¿¡Qué dices!?» o «¡¿Qué dices?!». No se añaden signos a las interrogativas indirectas («Me preguntó qué significaba esto», «No sé cuándo llega») ni a los títulos enunciativos que contienen un interrogativo («Cómo funciona el algoritmo» es correcto sin signos). No se tocan cadenas de código, URL, nombres de archivo ni texto en otros idiomas.
**Severidad:** prohibición dura.
**Linter:** `ES-INTERR-01`, `ES-EXCL-01`.

### 50. Tildes diacríticas omitidas

**Qué falla:** el modelo trabaja con subunidades y con un corpus web donde la tilde falta con frecuencia; además muchas de estas formas son monosílabos de altísima frecuencia cuyo par acentuado no cambia la probabilidad local. El resultado parece escrito sin teclado español y a veces cambia de significado.
**Qué vigilar:** sé, qué, él, cómo, dónde, más, aún, dé, té, mí, tú, sí en contextos tónicos.
**Antes:**
> No se que quieres decir; se lo diré a el cuando venga y luego te cuento como fue.

**Después:**
> No sé qué quieres decir; se lo diré a él cuando venga y luego te cuento cómo fue.

**No marcar:** las formas átonas homógrafas, que son las mayoritarias: «que», «como», «cuando», «donde», «cuanto», «quien» como relativos o conjunciones («dijo que vendría», «hazlo como quieras», «la casa donde vivo»); «el» artículo, «tu» y «mi» posesivos, «se» pronombre, «si» condicional, «mas» con el valor de pero, «te» pronombre, «de» preposición, «aun» con el valor de incluso. No se añade tilde a «ti», «fue», «vio», «dio», «fe», «vi», que nunca la llevan. «Solo», «este», «ese», «aquel» y «guion» se tratan en el patrón 51 y aquí no se les añade nada. No se tocan identificadores de código, URL, nombres de usuario ni texto en otras lenguas.
**Severidad:** prohibición dura.

### 51. Tildes obsoletas e hipercorrección acentual

**Qué falla:** el corpus contiene décadas de textos anteriores a la ortografía de 2010, donde «sólo», «éste», «aquéllos» y «guión» llevaban tilde. El modelo mezcla ambas épocas y, cuando se le pide «español correcto», sobreacentúa. Este patrón y el 50 trabajan en direcciones opuestas: hay que comprobar siempre en qué lista está la palabra antes de tocarla.
**Qué vigilar:** sólo, éste, ése, aquél, guión, fué, fuí, vió, dió, y la tilde en el demostrativo antepuesto al sustantivo, que nunca fue norma.
**Antes:**
> Sólo quería decirte que éste informe es mejor que aquél; el guión ya está listo y fué revisado.

**Después:**
> Solo quería decirte que este informe es mejor que aquel; el guion ya está listo y fue revisado.

**No marcar:** las tildes diacríticas vigentes («él, tú, mí, sí, sé, dé, té, más, aún» con el valor de todavía) y los interrogativos y exclamativos, también en interrogativas indirectas. Se respeta la ortografía original en citas literales, textos históricos, títulos de obras publicadas y nombres propios («Editorial El Guión»). Y se acepta «sólo» si el manual de estilo del cliente lo conserva para casos de ambigüedad: la Academia lo desaconseja pero no lo declara incorrecto, así que es decisión de casa, no falta.
**Severidad:** marcador de patrón.
**Linter:** `ES-TILDE-01`.

### 52. Coma serial antes de «y»

**Qué falla:** muchos manuales de estilo ingleses exigen la coma antes del último elemento; el español no la pone en enumeraciones homogéneas. El modelo aplica la puntuación inglesa a la enumeración española, sobre todo en listas de tres elementos, que ya son de por sí un tic (patrón 10).
**Qué vigilar:** secuencia «sintagma, sintagma, y sintagma» sin verbo propio en el último miembro.
**Antes:**
> El plan incluye informes mensuales, plantillas editables, y soporte por correo.

**Después:**
> El plan incluye informes mensuales, plantillas editables y soporte por correo.

**No marcar:** la coma ante «y» es correcta y a veces necesaria cuando el último miembro no es homogéneo con los anteriores o expresa conclusión o consecuencia («Pagó el traje, los zapatos, la corbata, y salió de la tienda»); cuando «y» une oraciones largas con sujetos distintos; cuando evita ambigüedad; cuando la enumeración acaba en «etc.»; cuando «y» equivale a «pero» («Se lo dije mil veces, y no me hizo caso»); y cuando cierra justo antes de «y» un inciso abierto con coma, raya o paréntesis.
**Severidad:** prohibición dura.
**Linter:** `ES-COMA-01` (ERROR).

### 53. Coma entre sujeto y verbo

**Qué falla:** el inglés tolera una coma tras un sujeto largo; el español prohíbe separar con una sola coma el sujeto del predicado. El modelo la coloca para marcar la respiración del sintagma largo, igual que hacen las traducciones automáticas.
**Qué vigilar:** coma única y solitaria entre un sujeto largo y su verbo.
**Antes:**
> Los usuarios que compraron el plan anual el año pasado, recibirán el descuento en su próxima factura.

**Después:**
> Los usuarios que compraron el plan anual el año pasado recibirán el descuento en su próxima factura.

**No marcar:** el inciso entre dos comas, que es correcto («Los usuarios, según el informe, recibirán el descuento»). También se admite la coma cuando el sujeto es una enumeración cerrada por un elemento recapitulativo («Contratos, facturas, albaranes, todo eso se archiva aquí»). Y es obligatoria tras un complemento circunstancial antepuesto largo, que no es el sujeto («Después de revisar todos los expedientes, el equipo decidió…»). Antes de marcar hay que comprobar que lo que precede a la coma es realmente el sujeto y que no hay una coma de apertura previa.
**Severidad:** prohibición dura.

### 54. «y» a «e» y «o» a «u»: la regla y sus excepciones

**Qué falla:** el modelo copia la plantilla inglesa «and/or» y escribe siempre «y» y «o»; cuando imita registro cuidado, hipercorrige y aplica «e» y «u» donde la norma las prohíbe. La alternancia depende del sonido de la palabra siguiente, no de su letra, y eso es justo lo que un modelo entrenado sobre grafías no resuelve.
**Qué vigilar:** «y» ante palabra que empieza por i- o hi-, y «o» ante palabra que empieza por o- u ho-.
**Antes:**
> El taller combina madera e hierro, reúne a siete o ocho artesanos y expone obras de Irene y Isabel.

**Después:**
> El taller combina madera y hierro, reúne a siete u ocho artesanos y expone obras de Irene e Isabel.

**No marcar:** «y» pasa a «e» solo ante palabra que empieza por el sonido /i/ («Irene e Isabel», «padre e hijo», «aguja e hilo»). Se mantiene «y» ante «hie-» y «hia-», donde el sonido inicial es diptongo («agua y hielo», «madera y hierro», «cobre y hierro»), y ante «y yo». También se mantiene «y» cuando encabeza un enunciado interrogativo o exclamativo («¿Y Inés?»). «o» pasa a «u» solo ante «o-» y «ho-» con sonido /o/ («siete u ocho», «mujer u hombre», «ayer u hoy»), y se mantiene «o» ante «hu-» («vino o huevos»), porque suena /u/. La «o» disjuntiva entre cifras ya no lleva tilde: «7 o 8», nunca «7 ó 8». No se tocan nombres propios de marcas ni citas literales.
**Severidad:** prohibición dura.
**Linter:** `ES-CONJ-01` (ERROR).

### 55. Anglicismos crudos con equivalente pleno en español

**Qué falla:** el modelo ha visto mucho más contenido de negocio, marketing y tecnología en inglés que en español, y en la salida española interpola el término inglés porque su vector es el más frecuente en ese contexto temático. Es distinto del anglicismo real del sector: aquí existe un equivalente español asentado y natural.
**Qué vigilar:** lista cerrada de sustituibles: feedback, deadline, approach, team, expertise, insight, target, meeting, workflow, engagement.
**Antes:**
> Necesitamos el feedback del team antes del deadline; el approach actual no escala y falta expertise en el equipo.

**Después:**
> Necesitamos los comentarios del equipo antes del plazo; el enfoque actual no escala y falta experiencia en el equipo.

**No marcar:** los anglicismos ya adaptados y recogidos en el diccionario (fútbol, escáner, wifi, blog, pódcast, tuit, marketing, software, hardware, estrés); los términos que son el nombre real de la cosa en su sector y no tienen equivalente estable (prompt, token, endpoint, CRM, brief en publicidad, commit y pull request en desarrollo); y los cargos oficiales, marcas, productos o puestos citados literalmente («Chief Marketing Officer», «Customer Success»). Tampoco el inglés dentro de código, de la interfaz citada o de una cita literal. Si el equivalente español suena a traducción forzada en ese sector, es preferible el préstamo en cursiva.
**Severidad:** marcador de patrón.
**Linter:** `ES-ANGL-02`.

### 56. Falsos amigos y calcos semánticos

**Qué falla:** el modelo alinea pares léxicos por forma y transfiere el significado inglés a una palabra española que existe pero significa otra cosa. Es el tell más difícil de ver para un linter pensado en inglés, porque todas las palabras son españolas.
**Qué vigilar:** eventualmente, asumir, soportar, severo, remover, consistente, librería, tópico, accionable, customizar, accesar, aplicar para, en adición a.
**Antes:**
> Eventualmente el equipo asumió que el sistema no soportaba ese formato, lo que causó un severo retraso; aplicamos para una extensión y entregamos un plan accionable.

**Después:**
> Al final el equipo supuso que el sistema no admitía ese formato, lo que causó un retraso grave; solicitamos una prórroga y entregamos un plan ejecutable.

**No marcar:** todas estas palabras son correctas en su sentido español. «Eventualmente» es de forma ocasional o llegado el caso («eventualmente puede haber cortes»); «asumir» es aceptar o hacerse cargo («asumió el cargo»); «soportar» es tolerar o sostener un peso («la viga soporta la carga»); «severo» es riguroso referido a personas, normas o climas («un profesor severo», «un invierno severo»); «consistente» es que tiene consistencia o solidez («una masa consistente», «un argumento consistente»); «remover» es agitar o revolver, y en América también quitar, uso ya recogido en el diccionario; «librería» es tienda de libros; «tópico» es lugar común, y en medicina de uso externo.
**Pistas mecánicas:** «eventualmente» es calco si acompaña a un pretérito perfectivo y equivale a «finalmente»; «asumir» lo es si lleva subordinada con «que» y un sujeto que no se hace cargo de nada; «soportar» lo es si el sujeto es un sistema, un formato o una versión; «severo» lo es si modifica a un daño, un retraso, una caída o un error. La sublista realmente detectable sin contexto es «accionable», «customizar», «accesar», «aplicar para» y «librería» en documentación de software.
**Severidad:** marcador de patrón.

### 57. Régimen preposicional calcado del inglés

**Qué falla:** el modelo copia la preposición del verbo inglés en lugar de la que rige el verbo español. No es léxico sino rección, y por eso pasa desapercibido en revisiones rápidas: cada palabra es española y solo la preposición delata la traducción.
**Qué vigilar:** aplicar para, en orden a, acorde a, de acuerdo a.
**Antes:**
> El equipo aplicó para la beca en orden a mejorar sus resultados, acorde a lo que se decidió en la reunión.

**Después:**
> El equipo solicitó la beca para mejorar sus resultados, acorde con lo que se decidió en la reunión.

**No marcar:** «aplicar» es correcto en su sentido español («aplicar una norma», «aplicar una crema», «aplicarse en el estudio», «aplicar un descuento») y solo es calco cuando significa presentar una candidatura, uso ya muy extendido en América y que en textos americanos se marca como observación, no como falta. «En orden a» existe en el español jurídico con el valor de «en lo relativo a» y ahí es correcto; solo se corrige cuando equivale a «para» más infinitivo. «Acorde a» está muy extendido y varias guías lo admiten junto a «acorde con», que es la forma tradicional: es preferencia de casa, no error. No se unifican las preposiciones en verbos de doble régimen legítimo: cuidar de o a, dudar de o en, diferente a o de, entrar en o a.
**Severidad:** marcador de patrón.

### 58. Calcos fraseológicos verbales

**Qué falla:** traducción sintagma a sintagma de colocaciones inglesas. El español tiene colocaciones propias con otro verbo de apoyo, pero el modelo elige el verbo cuya traducción léxica coincide con el inglés.
**Qué vigilar:** lista cerrada: hacer sentido, tomar acción, tomar ventaja, correr un test, correr una prueba, hacer una diferencia, tomar lugar.
**Antes:**
> Esa estrategia no hace sentido; deberíamos tomar acción esta semana, correr un test y tomar ventaja del momento.

**Después:**
> Esa estrategia no tiene sentido; deberíamos actuar esta semana, hacer una prueba y aprovechar el momento.

**No marcar:** son colocaciones genuinas del español «tomar medidas», «tomar la palabra», «tomar partido», «tomar una decisión», «tomar conciencia», «correr un riesgo», «correr la voz», «hacer una prueba», «hacer frente», «desempeñar un papel». «Jugar un papel» está admitido hoy por la mayoría de guías, aunque «desempeñar» sea preferible en registro alto: no se marca como error duro. Tampoco se tocan los calcos ya lexicalizados y aceptados («hacer clic», «dar de baja», «tener sentido»). «Tomar acciones legales» o «disciplinarias», con el sustantivo contable y determinado, es uso español normal y se deja.
**Severidad:** marcador de patrón.
**Linter:** `ES-ANGL-01`.

### 59. Marcadores discursivos calcados

**Qué falla:** los conectores de párrafo del inglés académico tienen traducción literal disponible y el modelo la usa como plantilla de transición, en lugar de los marcadores frecuentes del español. Da el ritmo inconfundible del ensayo traducido.
**Qué vigilar:** Adicionalmente, es importante notar que, en términos de, de acuerdo a, en adición a.
**Antes:**
> Adicionalmente, es importante notar que, en términos de costes, el modelo es viable. De acuerdo a lo anterior, procederemos.

**Después:**
> Además, conviene señalar que el modelo es viable en cuanto a costes. Según lo anterior, procederemos.

**No marcar:** «adicionalmente» existe en español y es normal en registro técnico y administrativo americano: se marca solo cuando abre párrafos de forma repetida o alterna con «además» sin motivo. «De acuerdo con» es plenamente correcto; el calco es «de acuerdo a». «En términos de» es legítimo en su sentido matemático o técnico («expresar x en términos de y», «en términos absolutos»). «En adición a» no tiene uso español válido.
**Regla antifabricación:** el recambio conserva el valor del original. «De acuerdo a lo anterior» pasa a «según lo anterior», no a «por lo tanto», que introduciría una consecuencia que el texto no afirmaba. «Es importante notar» se sustituye por «conviene señalar» o se suprime, sin añadir énfasis nuevo.
**Severidad:** marcador de patrón.
**Linter:** `ES-TRANS-01`.

### 60. «Interesantemente» e «importantemente»: el adverbio oracional inventado

**Qué falla:** el inglés antepone adverbios oracionales en -ly con toda libertad. El modelo genera el equivalente morfológico en -mente aunque esa forma no exista con ese valor en español, porque el sufijo es productivo y la traducción palabra a palabra siempre funciona en la superficie.
**Qué vigilar:** lista prohibida, cerrada y corta: interesantemente, importantemente, crucialmente.
**Antes:**
> Interesantemente, el consumo bajó un 3 %. Importantemente, el equipo no lo previó.

**Después:**
> Curiosamente, el consumo bajó un 3 %. Lo más importante: el equipo no lo previó.

**No marcar:** el español tiene adverbios oracionales propios que no se tocan: afortunadamente, lamentablemente, evidentemente, obviamente, lógicamente, francamente, curiosamente, sorprendentemente, previsiblemente. «Notablemente», «considerablemente» y «significativamente» son legítimos cuando modifican al verbo («mejoró notablemente», «creció significativamente»): solo se marca su uso antepuesto y aislado por coma con el valor de «cabe destacar». Tampoco se tocan estas formas dentro de una cita literal ni en textos que traducen expresamente un original inglés marcado como tal.
**Severidad:** prohibición dura.

### 61. Cadena de adverbios en -mente y coordinación mal formada

**Qué falla:** el inglés acumula adverbios en -ly sin coste rítmico y el modelo los traduce uno a uno. El español los penaliza por longitud y, además, en coordinación exige que solo el último miembro lleve el sufijo, regla que el calco ignora.
**Qué vigilar:** dos o más adverbios en -mente coordinados o en la misma oración.
**Antes:**
> Adicionalmente, el equipo trabajó rápidamente y eficientemente, y finalmente entregó el proyecto exitosamente.

**Después:**
> Además, el equipo trabajó rápida y eficientemente y, al final, entregó el proyecto con éxito.

**No marcar:** un adverbio en -mente aislado es perfectamente natural, y algunos no tienen sustituto: únicamente, prácticamente, difícilmente, precisamente, solamente. La regla de coordinación se aplica solo cuando los dos adverbios modifican al mismo verbo, van coordinados por «y», «o» o «pero» y no hay nada intercalado («lenta y cuidadosamente»); no cuando están separados por otros elementos, en incisos distintos o modificando verbos distintos.
**Regla antifabricación:** al reescribir no se cambia lo que el adverbio afirma. «Exitosamente» pasa a «con éxito», no a «a tiempo», que introduciría una puntualidad que el original no decía. Solo se eliminan los adverbios de relleno.
**Severidad:** marcador de patrón.

### 62. Adjetivo valorativo antepuesto al sustantivo

**Qué falla:** el inglés solo tiene una posición para el adjetivo, delante del nombre. El español lo pospone por defecto cuando clasifica o cuantifica, y lo antepone para valorar o para el epíteto. El modelo mantiene el orden inglés y produce un sintagma que se entiende pero suena a folleto traducido. Es más diagnóstico que la acumulación de adjetivos pospuestos, porque un hispanohablante casi nunca escribe así en prosa informativa.
**Qué vigilar:** lista cerrada, antepuesta a un sustantivo de producto, de negocio o de dato: robusto, sólido, significativo, exitoso, innovador, potente, poderoso, completo, integral, avanzado, detallado, profundo, comprensivo.
**Antes:**
> Una innovadora plataforma con una robusta arquitectura logró un significativo aumento de las suscripciones.

**Después:**
> Una plataforma innovadora con una arquitectura robusta logró un aumento significativo de las suscripciones.

**No marcar:** la anteposición es correcta y a veces obligatoria en los epítetos y usos no restrictivos («la blanca nieve», «el famoso director»); en las colocaciones fijas («alta velocidad», «pequeña empresa», «gran problema», «buen trabajo», «mero trámite», «pura casualidad», «libre comercio»); en los cuantificadores e indefinidos, que en español van delante por norma («múltiples factores», «distintos países», «numerosas quejas», «escasos recursos», «diversos motivos»), de modo que marcar «los múltiples desafíos» es un falso positivo; en los adjetivos que cambian de significado según la posición («un simple empleado» no es «un empleado simple», «un pobre hombre» no es «un hombre pobre», «un viejo amigo»); y en el estilo literario o publicitario donde la anteposición es deliberada.
**Corrección:** posponer el adjetivo, no borrarlo. Se borra solo si además es un elogio vacío, y entonces se aplica el patrón 4.
**Severidad:** marcador de patrón.
**Linter:** `ES-ADJ-01`.

### 63. Plural de siglas a la inglesa y apóstrofo de plural

**Qué falla:** en inglés las siglas y las décadas pluralizan con -s o -'s. En español las siglas son invariables en la escritura y el plural lo marca el determinante; el apóstrofo no es signo de plural.
**Qué vigilar:** CEOs, ONGs, PYMEs, los 90's.
**Antes:**
> Varios CEOs de ONGs presentaron sus informes en los 90's y dos PYMEs se sumaron.

**Después:**
> Varios CEO de ONG presentaron sus informes en los noventa y dos pymes se sumaron.

**No marcar:** las siglas lexicalizadas como sustantivos comunes se escriben en minúscula y sí pluralizan con normalidad: los ovnis, las pymes, los láseres, los radares, las oenegés, los cedés, los pecés. Conservan su plural inglés los nombres propios, marcas y títulos citados literalmente («los Grammys» como nombre del premio). No se tocan las siglas dentro de código, identificadores, nombres de columna, claves de API ni URL. Y no se confunde la «-s» de plural con la «-s» que forma parte de la propia sigla: «EE. UU.» y «FF. AA.» duplican letras, no añaden plural.
**Severidad:** prohibición dura.
**Linter:** `ES-SIGLA-01` (ERROR).

### 64. Formato de fechas, decimales, millares y porcentajes a la inglesa

**Qué falla:** los datos numéricos del corpus vienen mayoritariamente en convención anglosajona: mes primero, punto decimal, coma de millares, símbolo de porcentaje pegado y moneda antepuesta. El modelo los reproduce dentro de una oración española y a veces mezcla las dos convenciones en el mismo párrafo, lo que hace la cifra ilegible.
**Qué vigilar:** «Enero 5, 2026»; apóstrofo de millares; «$50»; mezcla de punto y coma como separadores en un mismo texto.
**Antes:**
> Enero 5, 2026 - las ventas subieron 12.5% hasta $1,250,000.

**Después:**
> 5 de enero de 2026: las ventas subieron un 12,5 % hasta 1 250 000 $.

**No marcar.** Hay que distinguir lo que es norma de lo que es hoja de estilo. Son calco en cualquier variedad el orden «mes día, año» en prosa española, el apóstrofo de millares, el símbolo de moneda antepuesto y la mezcla de separadores. En cambio son parámetro de variedad y de casa, no falta: el separador decimal (México, Centroamérica, el Caribe y parte del área andina usan legítimamente el punto decimal y la coma de millares), el separador de millares (espacio fino según la RAE, punto en muchas casas europeas) y el espacio ante el signo de porcentaje (la RAE lo recomienda; muchos manuales escriben «50%»). Se normaliza al mercado y a la hoja de estilo del destino, y esos casos no bloquean la entrega. Nunca se tocan las fechas ISO en contextos técnicos (2026-01-05), los números de versión, los códigos, los identificadores, las referencias catastrales o bancarias, los precios con código de moneda en documentación financiera internacional (USD 1,250.00) ni los datos dentro de bloques de código, CSV o tablas de exportación.
**Regla antifabricación:** nunca se convierte una cifra, solo su formato.
**Severidad:** prohibición dura.
**Linter:** `ES-FECHA-02` (ERROR), `ES-CIFRA-02`, `ES-CIFRA-03`.

### 65. «Billón» y falsos amigos numéricos

**Qué falla:** «billion» en inglés es 10⁹ y «billón» en español es 10¹²; «trillion» es 10¹² y «trillón» es 10¹⁸. El modelo traduce la palabra por su cognado y multiplica la cifra por mil. No es un tic de estilo: es una corrupción del dato, y sobrevive a cualquier revisión estilística porque la frase está perfectamente escrita.
**Qué vigilar:** «billón» acompañado de una glosa que no cuadra, de una suma que no cuadra o de una fuente en inglés identificable.
**Antes:**
> El fondo gestiona 3 billones de dólares, es decir, 3000 millones.

**Después:**
> El fondo gestiona 3000 millones de dólares.

**No marcar:** «billón» es correcto en español para 10¹² y no se toca cuando el contexto lo confirma («el PIB mundial supera los 100 billones de dólares»). Solo se corrige cuando hay evidencia dentro del propio texto o en la fuente citada de que se quiere decir 10⁹. Si no se puede verificar, se marca para consulta y no se convierte: cambiar una cifra sin respaldo es inventar un dato, exactamente lo que este skill prohíbe. Tampoco se toca «millardo» (10⁹, válido aunque poco usado), ni «trillón», ni las cifras dentro de citas literales, tablas o código. Puerto Rico y algunos textos técnicos traducidos usan «billón» con el valor inglés de forma sistemática: ahí es una decisión de localización documentada y se resuelve con el cliente.
**Severidad:** prohibición dura.

### 66. «El cual» en relativas especificativas

**Qué falla:** el modelo asocia «el cual» con registro formal y lo usa como sinónimo elegante de «que» para evitar repetición, la misma pulsión de variación sinonímica que muestra en inglés. Pero en relativa especificativa sin preposición el español no admite «el cual»: es agramatical, no solo pesado.
**Qué vigilar:** «el cual», «la cual», «los cuales», «las cuales» sin preposición, coma, raya ni paréntesis de cierre inmediatamente delante.
**Antes:**
> Presentamos un informe el cual analiza el mercado y una hoja de ruta la cual detalla los plazos.

**Después:**
> Presentamos un informe que analiza el mercado y una hoja de ruta que detalla los plazos.

**No marcar:** «el cual» es correcto y a veces preferible tras preposición («la razón por la cual», «el fondo con el cual se financia», «según el cual»), en relativas explicativas separadas por coma («El informe, el cual se publicó ayer, ya está en la web») y cuando la distancia respecto del antecedente exige marcar género y número para evitar ambigüedad. Tampoco se toca «lo cual», que es siempre explicativo y correcto, ni las fórmulas fijas del lenguaje jurídico («del cual se deriva», «a los cuales se refiere el artículo…»).
**Severidad:** prohibición dura.
**Linter:** `ES-RELAT-01`.

### 67. Mezcla de léxico peninsular y americano

**Qué falla:** el modelo elige cada palabra por probabilidad local, no por coherencia de variedad, y su corpus mezcla España y América. En un mismo párrafo aparecen «ordenador» y «computadora», «móvil» y «celular», «coger» y «agarrar», «zumo» y «jugo», «conducir» y «manejar». Ningún hablante real produce esa mezcla, y es un tell que un revisor angloparlante no puede ni ver.
**Qué vigilar:** dos designaciones de variedades distintas para el mismo referente en el mismo texto.
**Antes:**
> Coge el móvil, enciende el ordenador y luego agarra el carro para manejar hasta la oficina.

**Después:**
> Coge el móvil, enciende el ordenador y luego coge el coche para conducir hasta la oficina.

**No marcar:** la variedad es un parámetro del encargo, no un valor por defecto. El ejemplo se resuelve en peninsular porque el texto ya empezaba en peninsular; en rioplatense o mexicano la solución correcta es la contraria («Agarrá el celular, prendé la computadora y después agarrá el auto para manejar hasta la oficina»). No se neutraliza un texto ya coherente con una variedad ni se inventa un «español neutro» sin lugar. Tampoco se tocan las citas literales, los testimonios, el contenido localizado para un mercado concreto, los nombres de producto ni los términos sin equivalente en la otra variedad. Atención a «coger», normal en España y tabú en el Río de la Plata y en México: es decisión de localización, no error de norma.
**Severidad:** marcador de patrón.

### 68. Lenguaje inclusivo: «@» y «x» como morfema de género y mezcla de fórmulas

**Qué falla:** el modelo ha visto guías de estilo con políticas opuestas y no mantiene estado: dentro de un mismo texto alterna masculino genérico, desdoblamiento, «@», «x», «-e» y sustantivos colectivos, según lo que sea más probable en cada frase.
**Qué vigilar:** l@s, alumnxs, y la convivencia de dos o más estrategias en un mismo documento.
**Antes:**
> Todos y todas l@s participantes deben registrarse; les alumnes recibirán un correo y los usuarios/as podrán acceder el lunes.

**Después:**
> Todos los participantes deben registrarse; los alumnos recibirán un correo y los usuarios podrán acceder el lunes.

**No marcar.** Lo que se prohíbe sin excepción es «@» y «x» como marca de género: no son signos del sistema ortográfico, no se pueden leer en voz alta y los lectores de pantalla los destrozan. Lo que no se corrige es la política elegida: el desdoblamiento («todos y todas»), las formas en -e («les alumnes»), los colectivos y epicenos («el alumnado», «las personas usuarias», «la plantilla») y el masculino genérico son opciones editoriales legítimas, y si el cliente o el manual de estilo usa una, se conserva y se aplica de forma coherente. La barra «los/las» es admisible en formularios e impresos, no en prosa continua. Lo único que este skill decide por su cuenta es la mezcla: se unifica según la política declarada, y si no hay política declarada, se pregunta antes de unificar.
**Severidad:** prohibición dura, solo para «@» y «x».
**Linter:** `ES-INCL-01`, que señala la marca y no la corrige, porque es decisión editorial.

### 69. Mezcla de infinitivo e imperativo en instrucciones

**Qué falla:** el inglés usa una única forma imperativa, así que el modelo no tiene que decidir nada; al pasar al español debe elegir entre imperativo de tú, de usted o infinitivo instructivo, y como no mantiene estado, alterna las tres a lo largo de una misma lista de pasos.
**Qué vigilar:** dentro de una misma serie de pasos, alternancia de «abra», «abre» y «abrir».
**Antes:**
> Abra el panel de control. Luego seleccionar «Usuarios» y haz clic en Guardar.

**Después:**
> Abra el panel de control. Luego seleccione «Usuarios» y haga clic en Guardar.

**No marcar:** el infinitivo instructivo es un estilo legítimo y coherente en recetas, señalización, prospectos, protocolos y manuales («Batir los huevos. Añadir la harina. No exponer al sol»): no se convierte en imperativo si todo el documento lo mantiene. El error es la alternancia dentro de una misma serie, y la forma que se adopta es la mayoritaria en esa serie, no una nueva. Tampoco se toca el infinitivo cuando depende de otro verbo («Debe seleccionar «Usuarios»»), ni los títulos nominales de los pasos («Paso 2: configuración de la cuenta»), ni las etiquetas de botón citadas literalmente («Guardar», «Cancelar»).
**Severidad:** prohibición dura.

---

## Qué no marcar nunca

Ninguno de estos rasgos es prueba por sí solo. Un hallazgo aislado no sostiene un veredicto; lo que cuenta es la coincidencia de varios patrones de familias distintas en el mismo pasaje.

- **Gramática impecable y estilo uniforme.** Mucha gente escribe bien o pasa por un corrector. La pulcritud no es una huella.
- **Prosa sosa.** El español generado tiene tells concretos. La sequedad sin esos tells es prosa seca, y no hay nada que arreglar.
- **Palabras cultas o técnicas.** El patrón 7 nombra un inventario concreto y una lista de rechazados. Fuera de ahí, no se simplifica el vocabulario de nadie.
- **Un conector suelto.** «Además», «asimismo» o «no obstante» solo cuentan apilados. Un «sin embargo» no es nada.
- **Comillas curvas por sí solas.** Word, Google Docs, macOS y la mayoría de los gestores de contenido las ponen automáticamente.
- **La raya en español.** Es signo prescrito y obligatorio en el diálogo. Solo cuenta su forma anglicada (patrón 14).
- **Una frase corta para dar énfasis.** Los fragmentos se marcan a partir de tres seguidos (patrón 31).
- **Repeticiones deliberadas.** La anáfora es un recurso antiguo: «Esperé. Esperé toda la tarde, y luego toda la noche».
- **«Mira», «oye» o «la verdad es que» dentro de la frase.** El tell es la pausa teatral inicial, no la palabra.
- **Fórmulas de carta.** Saludos y despedidas son siglos anteriores a los chatbots.
- **Avisos y límites útiles.** Alcance de un estudio, notas legales y de seguridad, correcciones reales, objeciones con dueño y respuestas de un FAQ.
- **Alternativas reales.** Las opciones que un lector se plantearía de verdad en un documento de diseño o en un tutorial.
- **Falta de citas.** Casi toda la web carece de fuentes; su ausencia no prueba nada.
- **Marcas de variedad.** «Ordenador» y «computadora», «invaluable» e «inestimable», «apostar por» y «optar por», el punto decimal y la coma decimal: son localización, no error.
- **Registro de oficio.** Lengua administrativa, jurídica, periodística o de consultoría: identifican un gremio, no una máquina.
- **Texto de segunda mano.** No se reescriben las frases vigiladas dentro de citas, títulos, nombres propios ni ejemplos donde la fórmula se está comentando y no usando.
- **Código y datos.** Bloques de código, JSON, expresiones regulares, rutas, identificadores, claves, URL, tablas exportadas y cadenas literales quedan intactos, incluidas sus comillas, sus mayúsculas y sus separadores numéricos.

**Detalles humanos que se conservan.** El dato raro y específico, la contradicción sin resolver, la referencia fechada de una subcultura, el inciso o la autocorrección entre paréntesis, la variedad de longitud de frase y las decisiones de primera persona que el autor puede explicar. Al limpiar se quita la palabrería, no la voz.