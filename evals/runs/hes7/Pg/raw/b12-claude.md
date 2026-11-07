---
prompt: "Edita el texto que te voy a pegar para que suene a una persona y no a una IA, sin cambiar lo que dice.\n\nReglas:\n1. No inventes nada. Ningún dato, nombre, número, fecha, adorno ni promesa que no esté en el texto. No agregues disculpas ni admisiones que el original no hace.\n2. Haz que cada frase cumpla su función, con lo que el texto ya da a entender: un seguimiento pregunta si alcanzaron a revisar, una invitación invita, un aviso da la fecha.\n3. Borra los elogios que solo dicen que algo es bueno (\"de primera calidad\", \"una experiencia única\"). Deja lo que se comprueba y lo que describe cómo es algo, para qué sirve, a quién cubre o qué se pide (\"crujiente\", \"de grano entero\", \"puntualidad\"), dicho más simple.\n4. El resultado tiene que poder enviarse tal cual. Si una frase vacía no tiene dato detrás, bórrala. Antes de entregar, compara con el original: mismo alcance (\"en la Región Metropolitana\" no es \"en Santiago\"), misma fuerza (\"debemos\" no es \"podemos\") y las mismas garantías al lector.\n5. Si el texto ya suena humano, devuélvelo igual y dímelo.\n6. Español neutro que se lea bien en Chile: tú y ustedes, nada de vosotros ni voseo, nada de España (ordenador, móvil, vale, coste). Si el texto viene en español de España, pásalo a esta variante, salvo que quien escribe sea de allá. En textos informales, escribe como se escribe en Chile (\"te mandé\", \"¿alcanzaste a revisarla?\", \"me avisas\"), sin caricatura.\n\nQuita estas marcas de IA:\n- \"No es solo X, es Y\", \"no se trata de X, sino de Y\", \"Sin X. Sin Y. Solo Z.\"\n- Cierres de una línea: \"Piénsalo.\", \"Así de simple.\", \"Y eso lo cambia todo.\"\n- Preguntas que se responden solas: \"¿El resultado? …\"\n- Bisagras vacías: \"cabe destacar que\", \"es importante mencionar que\", \"sin lugar a dudas\", \"por último, pero no menos importante\".\n- Aperturas de época: \"en el mundo actual\", \"en la era digital\", \"en el panorama actual\".\n- Importancia inflada: \"marca un antes y un después\", \"juega un papel clave\", \"cambia las reglas del juego\".\n- Palabras de IA: sumérgete, adéntrate, desbloquea tu potencial, eleva, potencia, fascinante, vibrante, integral, sinergia, brindar, un testimonio de.\n- Listas de tres por regla y rangos falsos (\"desde principiantes hasta expertos\").\n- Gerundios colgados al final: \"…, garantizando / permitiendo / logrando…\".\n- Guion de servicio al cliente: \"entiendo perfectamente tu preocupación\", \"estamos trabajando arduamente\", \"lamentamos los inconvenientes\".\n- Relleno de cortesía: \"espero que este correo te encuentre bien\", \"quería tomarme un momento\", \"no dudes en contactarme\".\n- Cebo de redes: \"¿Qué opinas? ¡Te leo en los comentarios! 👇\", \"me complace anunciar\".\n- Calcos del inglés: hacer sentido, tomar acción, al final del día, en adición a, de acuerdo a, eventualmente (por \"finalmente\"), aplicar a un cargo (es \"postular\"), \"fue realizado por\" (usa \"se hizo\" o \"hicimos\").\n- Mayúsculas a la inglesa en títulos: \"Cómo Usar La IA\" → \"Cómo usar la IA\".\n- Rayas (— y –): ninguna.\n- Emojis como viñetas, negritas en cada punto, más de cinco hashtags.\n\nOjo, esto NO es marca de IA: \"clave\", \"fundamental\", \"además\", \"profundizar\", el \"se\" impersonal, los saludos y despedidas normales, los chilenismos del autor.\n\nDevuélveme primero el texto final, listo para copiar. Debajo, en dos o tres líneas, qué cambiaste.\n\nTexto:\n\n# Alcance del proyecto\n\n## 1. Objetivo\nDiseñar, desarrollar y poner en marcha una tienda online para [Nombre de la viña], que permita vender sus vinos directamente al público, con pago electrónico y despacho a todo el país.\n\n## 2. Alcance incluido\n\n### 2.1 Catálogo de productos\n- Configuración de hasta **25 vinos** (SKUs) en la tienda.\n- Ficha de cada producto con: nombre, cepa, cosecha, descripción, precio, stock, formato y notas de cata.\n- Organización por categorías (por ejemplo: tipo de vino, cepa, línea o valle), según se defina con el cliente.\n- Carga inicial del catálogo por parte del equipo de desarrollo, a partir de la información y las imágenes entregadas por el cliente.\n- Capacitación para que el cliente pueda agregar, editar o eliminar productos de forma autónoma.\n\n### 2.2 Diseño y desarrollo del sitio\n- Diseño personalizado alineado con la identidad visual de la viña (logo, colores y tipografías existentes).\n- Sitio responsive, optimizado para computador, tablet y celular.\n- Páginas base: inicio, catálogo, ficha de producto, carrito, checkout, nosotros, contacto, y términos y condiciones / políticas de despacho y devolución.\n- Configuración básica de SEO (títulos, descripciones, URLs amigables) y conexión con Google Analytics.\n- Formulario de contacto.\n- Verificación de mayoría de edad al ingresar al sitio o al finalizar la compra.\n\n### 2.3 Pagos con Webpay\n- Integración con **Webpay Plus (Transbank)** para pagos con tarjetas de crédito y débito.\n- Configuración del flujo completo de compra: carrito, checkout, pago y confirmación.\n- Pruebas en ambiente de integración y puesta en producción.\n- Envío automático de correo de confirmación al cliente y de aviso de nueva venta a la viña.\n\n> *El cliente debe contar con su contrato de comercio vigente con Transbank y entregar las credenciales (código de comercio y llaves) para pasar a producción.*\n\n### 2.4 Despacho a regiones\n- Configuración de zonas de despacho para **todo Chile, incluidas las regiones**.\n- Cálculo de costo de envío según región/comuna, peso o cantidad de botellas, según las tarifas que defina el cliente.\n- Opción de retiro en viña (si el cliente lo requiere).\n- Entrega al cliente del número de seguimiento para que lo ingrese en cada pedido, con notificación al comprador.\n- Gestión de pedidos desde el panel de administración, con estados (pagado, preparado, despachado, entregado).\n\n> *La contratación del servicio de courier (Chilexpress, Starken, Correos de Chile u otro) y la logística física del despacho son responsabilidad del cliente.*\n\n### 2.5 Puesta en marcha\n- Configuración de dominio y hosting [o conexión con el dominio existente del cliente].\n- Certificado SSL.\n- Pruebas funcionales de punta a punta antes del lanzamiento.\n- Capacitación de [X] horas sobre la gestión de pedidos, productos y stock.\n- Soporte posterior al lanzamiento por [30] días para corrección de errores.\n\n## 3. Alcance excluido\n- **Fotografía de producto**: la toma, edición y retoque de fotos de las botellas, etiquetas o ambientes. El cliente debe entregar las imágenes listas para usar (ver supuestos).\n- Catálogos con más de 25 vinos (se cotizan por separado).\n- Otros medios de pago (Mercado Pago, transferencia, PayPal, etc.), salvo acuerdo adicional.\n- Contratación y gestión de couriers, embalaje y logística de bodega.\n- Redacción de textos comerciales o de cata (el cliente los entrega; se puede cotizar aparte).\n- Campañas de marketing digital, publicidad paga, gestión de redes sociales o email marketing.\n- Emisión automática de boletas o facturas electrónicas con el SII (integración cotizable aparte).\n- Venta internacional, versión multiidioma y suscripciones o clubes de vino.\n- Costos de terceros: dominio, hosting, comisiones de Transbank y licencias de plataforma o plugins de pago.\n\n## 4. Supuestos y responsabilidades del cliente\n- Entregar fotos de producto en buena calidad (fondo limpio, resolución mínima de [1500 px]) antes de [fecha].\n- Entregar los textos, precios, stock y datos de cada vino en formato ordenado (planilla Excel o similar).\n- Entregar logo y lineamientos de marca en formato digital.\n- Contar con contrato activo con Transbank y facilitar las credenciales a tiempo.\n- Definir tarifas y condiciones de despacho antes de iniciar la configuración.\n- Designar un contacto único para revisiones y aprobaciones, con respuestas en un máximo de [3] días hábiles.\n- Cumplir"
---

# Alcance del proyecto

## 1. Objetivo

Diseñar, desarrollar y poner en marcha una tienda online para [Nombre de la viña], que permita vender sus vinos directamente al público, con pago electrónico y despacho a todo el país.

## 2. Alcance incluido

### 2.1 Catálogo de productos

- Configuración de hasta 25 vinos (SKUs) en la tienda.
- Ficha de cada producto con nombre, cepa, cosecha, descripción, precio, stock, formato y notas de cata.
- Organización por categorías (por ejemplo: tipo de vino, cepa, línea o valle), según se defina con el cliente.
- Carga inicial del catálogo por el equipo de desarrollo, con la información y las imágenes que entregue el cliente.
- Capacitación para que el cliente pueda agregar, editar o eliminar productos por su cuenta.

### 2.2 Diseño y desarrollo del sitio

- Diseño personalizado según la identidad visual de la viña (logo, colores y tipografías existentes).
- Sitio adaptable y optimizado para computador, tablet y celular.
- Páginas base: inicio, catálogo, ficha de producto, carrito, finalización de compra, nosotros, contacto y términos y condiciones / políticas de despacho y devolución.
- Configuración básica de SEO (títulos, descripciones y URLs amigables) y conexión con Google Analytics.
- Formulario de contacto.
- Verificación de mayoría de edad al ingresar al sitio o al finalizar la compra.

### 2.3 Pagos con Webpay

- Integración con Webpay Plus (Transbank) para pagos con tarjetas de crédito y débito.
- Configuración del proceso completo de compra: carrito, finalización de compra, pago y confirmación.
- Pruebas en ambiente de integración y puesta en producción.
- Envío automático de un correo de confirmación al cliente y un aviso de nueva venta a la viña.

El cliente debe contar con su contrato de comercio vigente con Transbank y entregar las credenciales (código de comercio y llaves) para pasar a producción.

### 2.4 Despacho a regiones

- Configuración de zonas de despacho para todo Chile, incluidas las regiones.
- Cálculo del costo de envío por región/comuna, peso o cantidad de botellas, según las tarifas que defina el cliente.
- Opción de retiro en viña, si el cliente lo requiere.
- Entrega al cliente del número de seguimiento para que lo ingrese en cada pedido, con notificación al comprador.
- Gestión de pedidos desde el panel de administración, con estados: pagado, preparado, despachado y entregado.

La contratación del servicio de courier (Chilexpress, Starken, Correos de Chile u otro) y la logística física del despacho son responsabilidad del cliente.

### 2.5 Puesta en marcha

- Configuración de dominio y hosting [o conexión con el dominio existente del cliente].
- Certificado SSL.
- Pruebas de funcionamiento de todo el proceso antes del lanzamiento.
- Capacitación de [X] horas sobre la gestión de pedidos, productos y stock.
- Soporte durante [30] días después del lanzamiento para corregir errores.

## 3. Alcance excluido

- Fotografía de producto: toma, edición y retoque de fotos de las botellas, etiquetas o ambientes. El cliente debe entregar las imágenes listas para usar (ver supuestos).
- Catálogos con más de 25 vinos (se cotizan por separado).
- Otros medios de pago (Mercado Pago, transferencia, PayPal, etc.), salvo acuerdo adicional.
- Contratación y gestión de couriers, embalaje y logística de bodega.
- Redacción de textos comerciales o de cata (el cliente los entrega; se puede cotizar aparte).
- Campañas de marketing digital, publicidad pagada, gestión de redes sociales o marketing por correo electrónico.
- Emisión automática de boletas o facturas electrónicas con el SII (la integración se puede cotizar aparte).
- Venta internacional, versión en varios idiomas y suscripciones o clubes de vino.
- Costos de terceros: dominio, hosting, comisiones de Transbank y licencias de plataforma o plugins de pago.

## 4. Supuestos y responsabilidades del cliente

- Entregar fotos de producto de buena calidad (fondo limpio, resolución mínima de [1500 px]) antes de [fecha].
- Entregar los textos, precios, stock y datos de cada vino en formato ordenado (planilla Excel o similar).
- Entregar logo y lineamientos de marca en formato digital.
- Contar con contrato activo con Transbank y facilitar las credenciales a tiempo.
- Definir tarifas y condiciones de despacho antes de iniciar la configuración.
- Designar un contacto único para revisiones y aprobaciones, con respuestas en un máximo de [3] días hábiles.
- Cumplir

Simplifiqué algunas expresiones y reemplacé términos en inglés, sin cambiar el alcance, los plazos ni las responsabilidades.
El original termina en «Cumplir». Lo dejé igual para no inventar la obligación que falta; ese punto queda pendiente antes de enviarlo.
