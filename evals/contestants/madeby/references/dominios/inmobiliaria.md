# Pack inmobiliario

## disparador

Cargar el pack cuando el texto es inmobiliario en cualquier formato: aviso,
landing, bio de agente, respuesta de WhatsApp, guía de barrio, artículo SEO,
publicación en redes o mensaje de venta.

## no-cargar

No cargar para strings de UI de un producto inmobiliario (botones,
etiquetas, mensajes de sistema, onboarding): ahí no aplica el vocabulario
ni los patrones de este pack — las reglas nucleo/prosa del skill ya cubren
ese texto.

## patrones

### Clichés de venta inmobiliaria

**Frases a detectar:** "oportunidad única", "no te lo pierdas", "imperdible", "oferta exclusiva", "propiedad de ensueño", "joya inmobiliaria", "único en su tipo", "no encontrarás algo igual", "ideal para ti", "lo que siempre buscaste", "hecho a tu medida", "descubre tu próximo hogar", "bienvenido a tu nuevo hogar", "aquí comienza tu nueva vida", "tu hogar ideal te espera", "un hogar pensado para ti y tu familia", "tu próximo hogar está aquí", "el hogar con el que siempre soñaste"

**Problema:** Estas frases aparecen en miles de avisos. Cuando todo es "oportunidad única", nada lo es. Las variantes con "hogar" prometen un sentimiento que el anuncio no puede verificar.

**Antes:**
> ¡Oportunidad única! No dejes pasar esta joya inmobiliaria, ideal para ti y tu familia.

**Después:**
> Casa en venta en La Rinconada. 3 dormitorios, 2 baños, garaje doble. Papeles al día.

**Antes (cierre tipo "hogar"):**
> No lo pienses más. Tu próximo hogar te espera. Una oportunidad única para vivir el estilo de vida que mereces.

**Después:**
> Disponible para visita esta semana. Precio negociable.

---

### La propiedad como sujeto repetitivo

**Frases a detectar:** "La propiedad cuenta con...", "El inmueble dispone de...", "La vivienda ofrece...", "El departamento brinda...", "La casa posee...", "El terreno presenta..."

**Problema:** Cuando cada oración empieza con "la propiedad", el texto suena generado por un robot que no sabe cómo variar.

**Antes:**
> La propiedad cuenta con 3 dormitorios. La vivienda dispone de 2 baños completos. El inmueble ofrece garaje para dos autos. La casa posee jardín trasero.

**Después:**
> 3 dormitorios, 2 baños completos, garaje doble y jardín trasero. Todo en una planta.

---

### Contexto de barrio genérico

**Frases a detectar:** "ubicación estratégica", "zona privilegiada"

**Problema:** Frases que aplican a cualquier barrio de cualquier ciudad del mundo. Sin datos concretos.

**Antes:**
> Ubicada en una zona privilegiada con excelente conectividad, cerca de todos los servicios que necesitas para tu vida cotidiana, en un entorno tranquilo y seguro ideal para familias.

**Después:**
> A 5 minutos del Hipermaxi de Av. Beni, frente al parque del barrio. Zona residencial, poco tráfico.

---

### Exclusividad sin evidencia

**Frases a detectar:** "zona exclusiva", "barrio premium", "de primer nivel", "propiedades de alta gama", "lo mejor de la ciudad", "el sector más cotizado", "acabados de lujo"

**Problema:** Decir que algo es exclusivo no lo hace exclusivo. Si es cierto, los datos lo demuestran solos.

**Antes:**
> Ubicada en una de las zonas más exclusivas y cotizadas de la ciudad, este departamento de primera clase es una inversión premium.

**Después:**
> En [zona por confirmar], a media cuadra de la avenida principal. El precio refleja la zona.

---

### Recorrido de habitación en habitación

**Problema:** Descripciones que te llevan de cuarto en cuarto como si estuvieras en el lugar. Suenan a una IA que no sabe qué priorizar.

**Antes:**
> Al ingresar, te recibe una amplia sala de estar con luz natural. Continuando, encontrarás el comedor integrado a una moderna cocina. Subiendo las escaleras, accedes a los tres dormitorios, cada uno con clóset empotrado. El dormitorio principal cuenta con baño en suite.

**Después:**
> Casa de dos plantas. Abajo: sala-comedor integrado y cocina. Arriba: 3 dormitorios con closets, dormitorio principal con baño privado.

---

### Urgencia inmobiliaria

**Frases a detectar:** "Últimas unidades", "Precio por tiempo limitado"

**Problema:** La urgencia falsa erosiona la confianza. Si no hay urgencia real, no se menciona.

**Antes:**
> ¡No pierdas esta oportunidad! Últimas unidades disponibles, llama hoy mismo.

**Después:**
> Quedan 3 unidades disponibles en el edificio. El precio incluye garaje.

---

## vocabulario-por-variante

El vocabulario inmobiliario por país vive aquí, no en los packs de
variante (`references/variantes/`) — un solo eje por archivo: el pack de
variante cubre registro y voz general, este pack cubre el término
específico del rubro.

| término neutro | Bolivia | México |
|---|---|---|
| estacionamiento | parqueo | estacionamiento |
| dormitorio | dormitorio | recámara |
| sala de estar | living | sala |
| barrio/zona | barrio, zona | colonia |
| departamento pequeño | garzonier | estudio |

## falsos-positivos

- **Urgencia real con fecha:** "Últimas unidades" y "precio por tiempo
  limitado" se marcan como urgencia inmobiliaria porque casi siempre son
  presión inventada. Pero si el texto trae una fecha o un motivo
  verificable — "el remate es el 12 de agosto", "el precio promocional
  vence el 30 de este mes", "quedan 2 de las 8 unidades del edificio" —
  no es el mismo patrón: es un dato concreto, no una frase hueca. No se
  borra ni se suaviza; se conserva tal cual.
- **Descripción con un solo sujeto repetido:** el patrón "la propiedad
  como sujeto repetitivo" se dispara cuando varias oraciones seguidas
  cambian de sujeto (la propiedad/el inmueble/la vivienda) para sonar
  variado. Una sola mención de "el departamento" o "la casa" como sujeto,
  en un texto corto, es español normal — no hay nada que reescribir.

## ejemplos

<!-- DATOS DEL ORIGINAL (tomado del "Antes"): 2 dormitorios, 2 baños completos, sala
de estar con luz natural, comedor integrado a la cocina, balcón, vistas a la
ciudad, parqueo subterráneo, seguridad 24 horas, Santa Cruz. El original NO
menciona barrio/zona específica, piso, orientación ni estado del inmueble
(nuevo/usado) — cualquier reescritura que necesite uno de esos datos usa
[dato por confirmar] o [zona por confirmar] en vez de inventarlo. -->

**Original (generado por IA):**
> ¡Imagina vivir en este espectacular departamento ubicado en una de las zonas más exclusivas y privilegiadas de Santa Cruz! La propiedad cuenta con 2 dormitorios, 2 baños completos, sala de estar con luz natural, comedor integrado a la moderna cocina, y un amplio balcón con increíbles vistas a la ciudad. El inmueble dispone de parqueo subterráneo y el edificio brinda seguridad 24 horas, garantizando la tranquilidad que tú y tu familia se merecen. Se puede apreciar la calidad de los acabados de lujo en cada rincón de esta joya inmobiliaria. ¡Una oportunidad única que no puedes dejar pasar! Tu próximo hogar te espera.

**Borrador reescrito:**
> Departamento de 2 dormitorios en [zona por confirmar], Santa Cruz. Balcón con vista a la ciudad, sala con luz natural, comedor integrado a la cocina. 2 baños completos. Parqueo subterráneo, portería 24 horas.

**¿Qué sigue siendo IA?**
- falta el área en m²
- falta la zona exacta dentro de Santa Cruz
- no menciona el estado del inmueble; ese dato no está en el original

**Versión final:**
> Departamento de 2 dormitorios y 2 baños en [zona por confirmar], Santa Cruz. Sala con luz natural, comedor integrado a la cocina. Balcón con vista a la ciudad. Parqueo subterráneo incluido, portería 24 horas.

**Cambios realizados:**
- Eliminado: apertura fantasiosa ("¡Imagina vivir...")
- Eliminado: adjetivos vacíos ("espectacular", "increíbles", "moderna")
- Eliminado: clichés de venta ("oportunidad única", "joya inmobiliaria", "no puedes dejar pasar")
- Eliminado: propiedad como sujeto repetitivo ("La propiedad cuenta con...", "El inmueble dispone de...")
- Eliminado: voz pasiva impersonal ("Se puede apreciar")
- Eliminado: gerundio de profundidad falsa ("garantizando la tranquilidad")
- Eliminado: conclusión genérica positiva ("Tu próximo hogar te espera")
- Eliminado: exceso de signos de exclamación
- Marcado [zona por confirmar]: el original solo menciona "Santa Cruz", sin barrio ni zona específica
- No agregado: área en m², piso, orientación ni estado del inmueble — esos datos no estaban en el original
