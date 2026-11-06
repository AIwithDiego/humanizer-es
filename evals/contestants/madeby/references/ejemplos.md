# Corpus de prueba

Muestras fijas, todas sintéticas: no hay texto de clientes ni datos
reales.

**Alcance.** Estas trece muestras son la suite de humo y BLOQUEAN el
cambio: después de tocar el núcleo, un archivo de patrones o un pack,
correr el skill sobre las trece y comparar contra cada **Esperado**. Los
`ejemplos` locales de cada pack (variantes y dominios) viven en el archivo
del pack y se corren cuando ese pack cambia.

**Línea de ruta.** Toda corrida abre con una línea `Ruta:` bien formada
según el contrato de `SKILL.md`. Una corrida sin esa línea, o con una que
no respeta la gramática, no pasa, aunque la reescritura sea buena.

Cada muestra trae la línea **Pedido** (lo que el usuario dice al invocar el
skill, porque la resolución de variante depende de eso), el texto de
entrada, y el **Esperado**.

---

## 1. Aviso inmobiliario (bolivia) — debe cargar pack inmobiliario

**Pedido:** «Humaniza este aviso, es para Bolivia.»

> ¡Imagina despertar cada mañana en esta espectacular joya inmobiliaria!
> La propiedad cuenta con 3 dormitorios y 2 baños completos. El inmueble
> dispone de estacionamiento para dos vehículos. La vivienda ofrece una
> amplia terraza con increíbles vistas a la ciudad y acabados de lujo en
> cada rincón de este departamento. Ubicada en una zona privilegiada con
> excelente conectividad, cerca de todos los servicios que necesitas para
> tu vida cotidiana. Precio: 145.000 dólares, negociable. ¡Una oportunidad
> única que no puedes dejar pasar! No esperes más: tu hogar ideal te
> espera. ¡Llama hoy mismo!

**Esperado:** clichés fuera («joya inmobiliaria», «oportunidad única», «tu
hogar ideal te espera»); datos intactos (3 dormitorios, 2 baños, terraza
con vista a la ciudad, 145.000 dólares negociable); sin datos inventados —
la zona no está en el original, queda como `[zona por confirmar]`;
vocabulario boliviano (parqueo, autos); la urgencia y el exceso de
exclamación desaparecen.

---

## 2. Aviso inmobiliario (mexico) — variante explícita

**Pedido:** «Humaniza este aviso para México.»

> ¡Descubre tu próximo hogar! Este hermoso departamento cuenta con 2
> dormitorios, 1 baño completo y sala de estar con mucha luz natural. La
> propiedad dispone de estacionamiento techado y se encuentra ubicada en
> un barrio tranquilo y seguro, ideal para ti y tu familia. El inmueble
> ofrece cocina integral, brindando el confort y la funcionalidad que
> mereces. Renta: 9.500 pesos mensuales. ¡Aprovecha esta oportunidad
> única, no encontrarás algo igual!

**Esperado:** vocabulario mexicano (recámara, sala, colonia,
estacionamiento); datos intactos (2 recámaras, 1 baño, cocina integral,
renta de 9.500 pesos); el nombre de la colonia no está en el original,
queda como `[colonia por confirmar]`; clichés y vocabulario IA fuera
(«brindando el confort y la funcionalidad»).

---

## 3. Párrafo de blog (neutral EXPLÍCITO) — prosa general

**Pedido:** «Humaniza este párrafo de blog, en español neutro.»

> En el mundo actual, donde la tecnología avanza a pasos agigantados,
> trabajar desde casa se ha convertido en una tendencia fundamental. En
> primer lugar, cabe destacar que el teletrabajo ofrece flexibilidad,
> autonomía y comodidad. En segundo lugar, es importante señalar que las
> empresas reportan mejoras en la productividad. Finalmente, en
> definitiva, el trabajo remoto llegó para quedarse, transformando la
> manera en que vivimos, trabajamos y nos relacionamos.

**Esperado:** el pedido dice «neutro» explícitamente y el skill lo
respeta; sin marcadores de país, pero con ritmo y datos — no corporativo
pan-LATAM. Apertura globalizante fuera, conectores formulaicos fuera,
regla de tres desarmada. La afirmación sobre productividad no trae fuente:
se marca `[fuente por confirmar]` o se atenúa, nunca se inventa la cita.

---

## 4. Strings de UI (español) — las listas NO se marcan

**Pedido:** «Humaniza estos strings de la app.» (Suponer la variante de
la sesión ya resuelta: neutral.)

> - ¡Bienvenido a la aplicación!
> - Conoce más sobre nuestras funcionalidades
> - ¡Tu cuenta ha sido creada exitosamente!
> - Se recomienda verificar su dirección de correo electrónico
> - Sumérgete en una experiencia única de gestión de tareas
> - Aprovecha al máximo las herramientas diseñadas para potenciar tu productividad
> - Eliminar dicho elemento de la lista
> - ¡Gracias por tu preferencia!

**Esperado:** microcopy directo, string por string; la estructura de lista
se conserva (las listas son correctas en UI); sin alma ni voz agregada;
vocabulario IA fuera («sumérgete», «experiencia única», «potenciar»);
exclamaciones reducidas.

---

## 5. Mensaje de WhatsApp — registro coloquial, INVERSIÓN de tipo

**Pedido:** «Humaniza esta respuesta de WhatsApp a un cliente que preguntó
por un departamento en alquiler.» (Suponer la variante de la sesión ya
resuelta: neutral.)

> Estimado cliente: Le informamos que hemos recibido su consulta con
> respecto al departamento en alquiler. Cabe destacar que dicho inmueble
> se encuentra disponible, brindando la posibilidad de agendar una visita.
> Le recomendamos aprovechar esta oportunidad única, ya que contamos con
> alta demanda. Quedamos atentos a su amable respuesta. Saludos cordiales.

**Esperado:** cálido y breve, registro de chat (sigue de usted: es un
cliente); el fraseo de marketing («aprovecha esta oportunidad única», la
presión de «alta demanda») se elimina SIN convertir el mensaje en copy de
ventas — un mensaje es un mensaje; «cabe destacar», «dicho inmueble» y
«brindando» fuera.

---

## 6. Texto bilingüe — solo los tramos en español se tocan

**Pedido:** «Humaniza esto.» (Suponer la variante de la sesión ya
resuelta: neutral.)

> Nuestro equipo utiliza Notion para la documentación, brindando una
> experiencia única de colaboración. Cabe destacar que la integración con
> Slack permite maximizar la productividad, lo cual se traduce en mejores
> resultados. The API documentation is only available in English for now.
> Además, la herramienta cuenta con plantillas diseñadas para quienes
> buscan potenciar su flujo de trabajo.

**Esperado:** la oración en inglés queda idéntica, carácter por carácter;
los nombres de producto (Notion, Slack) intactos; los tramos en español
humanizados («brindando», «cabe destacar», «maximizar», «diseñadas para
quienes» fuera; la rotación «la herramienta» vuelve a llamarse por su
nombre). La línea de ruta declara el tipo en la forma `tipo=mixto(...)`
— el texto mezcla documentación con prosa de artículo, por ejemplo
`tipo=mixto(artículo+UI)` — y por esa mezcla `patrones=ambos`.

---

## 7. Texto humano bien escrito — NO tocar (control)

**Pedido:** «Humaniza esto.»

> Mi abuela vendió empanadas en la puerta del colegio Ayacucho durante
> veintidós años. Nunca tuvo cartel. Los profesores salían al recreo y ya
> sabían: las de queso se acababan primero, y si llovía, no había. A mí me
> tocaba ayudarla los viernes, y lo que más recuerdo no son las empanadas
> sino el olor de la canasta, una mezcla de horno y periódico. Hoy
> cualquier negocio «cuenta su historia» en Instagram. Ella no contaba
> nada. Creo que por eso le iba bien.

**Esperado:** cambios mínimos o ninguno. Tiene anécdota concreta, opinión
con dueño («Creo que»), ritmo irregular y digresión con propósito: todo
eso se preserva. Las frases cortas («Nunca tuvo cartel.») son ritmo
genuino, no staccato fabricado. Si el skill lo reescribe fuerte, el skill
está mal calibrado.

---

## 8. Variante guardada en configuración — aplicar sin preguntar

**Pedido:** «Humaniza este texto para la web de la lavandería.» (Sin país
en el pedido, sin `Spanish variant:` en ningún CLAUDE.md. Suponer que
`~/.claude/humanizador.md` existe y contiene `variant: bolivia`.)

> ¿Cansado de perder tiempo lavando? Nuestro servicio de lavandería está
> diseñado para quienes buscan comodidad, rapidez y calidad. Recogemos tu
> ropa en la puerta de tu casa y la devolvemos impecable en 24 horas,
> garantizando resultados excepcionales. Reserva desde tu móvil y
> aprovecha al máximo tu tiempo libre. ¡Una experiencia única que
> transformará tu rutina!

**Esperado:** el skill toma la variante del archivo de configuración y
escribe en bolivia sin hacer ninguna pregunta — la preferencia guardada
resuelve el paso 3 de la cadena. «Móvil» pasa a «celular»; el dato real
(recojo a domicilio, entrega en 24 horas) queda intacto; «diseñado para
quienes», la regla de tres y la conclusión transformadora desaparecen.

---

## 9. Texto mayormente en inglés — derivar

**Pedido:** «Humaniza esto.»

> We shipped the new onboarding flow last week and the numbers look
> promising. Activation is up and support tickets are down, though we
> still need to fix the empty-state copy before the next release. The
> team is happy with the result. Cabe destacar que la versión en español
> de la página de precios ya se encuentra disponible, brindando acceso a
> todos los usuarios de la región.

**Esperado:** el skill NO lo reescribe a medias; dice que el texto es
mayormente inglés y sugiere `/humanizer`. Solo si el usuario insiste toca
la única oración en español (y nada más que esa).

---

## 10. Nada configurado, sesión interactiva — preguntar una sola vez

**Pedido:** «Humaniza esta bio para mi página de servicios.» (Sin país en
el pedido, sin `Spanish variant:` en ningún CLAUDE.md. Suponer que
`~/.claude/humanizador.md` no existe. La sesión es interactiva y la
herramienta de preguntas está disponible. Suponer que a la pregunta de
variante el usuario responde «Bolivia».)

> Soy un profesional apasionado por brindar soluciones integrales de
> diseño gráfico. Mi enfoque está diseñado para quienes buscan potenciar
> su marca y maximizar su impacto visual. A lo largo de mi trayectoria he
> trabajado con clientes de diversos sectores, ofreciendo resultados
> excepcionales y garantizando la plena satisfacción de cada proyecto.
> ¡Contáctame hoy mismo y llevemos tu presencia visual al siguiente
> nivel!

**Esperado:** antes de tocar el texto, el skill hace UNA pregunta de
variante con AskUserQuestion — ni cero ni dos, y sin caer a neutral por
su cuenta. La respuesta vale para el resto de la sesión, y en algún punto
de la corrida se menciona `/humanizador-setup` como forma de dejar la
preferencia guardada. Con la variante ya elegida, la bio sale humanizada:
«brindar», «diseñado para quienes», «potenciar» y «maximizar» fuera, los
sectores concretos no se inventan (quedan como dato por confirmar o se
omiten), y el cierre con exclamación desaparece.

**Segundo pedido (misma sesión):** «Ahora humaniza también este texto
para la misma página.»

> Ofrezco servicios integrales de branding, diseñados para potenciar la
> identidad de tu negocio y garantizar resultados excepcionales en cada
> entrega.

**Esperado (segundo pedido):** ninguna pregunta nueva — la respuesta de
la primera corrida vale toda la sesión — y la línea de ruta lleva
`variante=bolivia`; «servicios integrales», «diseñados para potenciar» y
«garantizar resultados excepcionales» fuera, sin inventar entregables que
el original no nombra.

---

## 11. Strings de UI — el archivo núcleo alcanza solo

**Pedido:** «Humaniza estos textos del panel de ajustes, en español
neutro.»

> - ¡Sumérgete en la nueva experiencia de personalización!
> - Pasos para exportar tus datos:
>   1. Abre la pestaña Cuenta
>   2. Selecciona «Exportar»
>   3. Elige el formato del archivo
> - ¡Configuración guardada exitosamente!
> - ¡Ya casi terminas! ¡Completa tu perfil para continuar!

**Esperado:** la apertura-invitación («Sumérgete en...») desaparece, las
exclamaciones bajan a una o ninguna, y la lista numerada de pasos queda
como lista: en UI las listas son el formato correcto. Todo se resuelve
con `references/patrones-nucleo.md` como único archivo de patrones; qué
archivos se leyeron en la corrida se anota como evidencia, no como
criterio de aprobación.

---

## 12. Texto ambiguo — el tipo incierto se declara, no se adivina

**Pedido:** «Humaniza. (Suponer config: variant: neutral.)»

> Gracias por tu interés. Nuestro equipo revisará tu solicitud y te
> contactará a la brevedad posible para brindarte más información.

**Esperado:** la corrida abre con
`Ruta: tipo=incierto | variante=neutral | dominio=— | patrones=ambos` —
el texto podría ser un mensaje, una confirmación de UI o relleno de
marketing, y esa ambigüedad es el punto: se declara `incierto` en vez de
adivinar, y por contrato el tipo incierto carga ambos archivos de
patrones. La reescritura elimina «brindarte» y «a la brevedad posible»;
el compromiso real (revisamos tu solicitud y te contactamos) se conserva.

---

## 13. Sesión NO interactiva, nada configurado — fallback declarado

**Pedido:** «Humaniza esta descripción para la tienda en línea.» (Sin
país en el pedido, sin `Spanish variant:` en ningún CLAUDE.md, sin
`~/.claude/humanizador.md`. La sesión NO es interactiva: la herramienta
de preguntas no está disponible.)

> Descubre nuestra colección de termos, diseñada para quienes buscan
> mantener sus bebidas a la temperatura ideal. Fabricados con materiales
> de alta calidad, nuestros termos brindan un rendimiento excepcional,
> garantizando hasta 12 horas de frío o calor. ¡Aprovecha al máximo cada
> aventura con un producto innovador que transformará tu día a día!

**Esperado:** ninguna pregunta — no hay a quién preguntarle — y el país
NUNCA se infiere del contenido: el skill escribe en neutral, lo avisa en
una línea, y la ruta lleva `variante=neutral(fallback)`. El dato real
(hasta 12 horas de frío o calor) queda intacto; «diseñada para quienes»,
«brindan», «garantizando», «innovador» y el cierre transformador
desaparecen.
