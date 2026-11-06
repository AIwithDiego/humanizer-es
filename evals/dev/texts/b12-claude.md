---
id: b12
genre: proposal
split: dev
source: claude-sonnet-5-5
prompt: "redacta la parte de alcance de una propuesta para hacer la tienda online de una viña chica. incluye catálogo de hasta 25 vinos, pago con webpay y despacho a regiones. no incluye fotos de producto"
facts: "tienda online · viña chica · catálogo de hasta 25 vinos · pago con Webpay · despacho a regiones · no incluye fotos de producto"
raw_wrapper_lines_stripped: 0
extracted_from: raw/b12-claude.md
---

# Alcance del proyecto

## 1. Objetivo
Diseñar, desarrollar y poner en marcha una tienda online para [Nombre de la viña], que permita vender sus vinos directamente al público, con pago electrónico y despacho a todo el país.

## 2. Alcance incluido

### 2.1 Catálogo de productos
- Configuración de hasta **25 vinos** (SKUs) en la tienda.
- Ficha de cada producto con: nombre, cepa, cosecha, descripción, precio, stock, formato y notas de cata.
- Organización por categorías (por ejemplo: tipo de vino, cepa, línea o valle), según se defina con el cliente.
- Carga inicial del catálogo por parte del equipo de desarrollo, a partir de la información y las imágenes entregadas por el cliente.
- Capacitación para que el cliente pueda agregar, editar o eliminar productos de forma autónoma.

### 2.2 Diseño y desarrollo del sitio
- Diseño personalizado alineado con la identidad visual de la viña (logo, colores y tipografías existentes).
- Sitio responsive, optimizado para computador, tablet y celular.
- Páginas base: inicio, catálogo, ficha de producto, carrito, checkout, nosotros, contacto, y términos y condiciones / políticas de despacho y devolución.
- Configuración básica de SEO (títulos, descripciones, URLs amigables) y conexión con Google Analytics.
- Formulario de contacto.
- Verificación de mayoría de edad al ingresar al sitio o al finalizar la compra.

### 2.3 Pagos con Webpay
- Integración con **Webpay Plus (Transbank)** para pagos con tarjetas de crédito y débito.
- Configuración del flujo completo de compra: carrito, checkout, pago y confirmación.
- Pruebas en ambiente de integración y puesta en producción.
- Envío automático de correo de confirmación al cliente y de aviso de nueva venta a la viña.

> *El cliente debe contar con su contrato de comercio vigente con Transbank y entregar las credenciales (código de comercio y llaves) para pasar a producción.*

### 2.4 Despacho a regiones
- Configuración de zonas de despacho para **todo Chile, incluidas las regiones**.
- Cálculo de costo de envío según región/comuna, peso o cantidad de botellas, según las tarifas que defina el cliente.
- Opción de retiro en viña (si el cliente lo requiere).
- Entrega al cliente del número de seguimiento para que lo ingrese en cada pedido, con notificación al comprador.
- Gestión de pedidos desde el panel de administración, con estados (pagado, preparado, despachado, entregado).

> *La contratación del servicio de courier (Chilexpress, Starken, Correos de Chile u otro) y la logística física del despacho son responsabilidad del cliente.*

### 2.5 Puesta en marcha
- Configuración de dominio y hosting [o conexión con el dominio existente del cliente].
- Certificado SSL.
- Pruebas funcionales de punta a punta antes del lanzamiento.
- Capacitación de [X] horas sobre la gestión de pedidos, productos y stock.
- Soporte posterior al lanzamiento por [30] días para corrección de errores.

## 3. Alcance excluido
- **Fotografía de producto**: la toma, edición y retoque de fotos de las botellas, etiquetas o ambientes. El cliente debe entregar las imágenes listas para usar (ver supuestos).
- Catálogos con más de 25 vinos (se cotizan por separado).
- Otros medios de pago (Mercado Pago, transferencia, PayPal, etc.), salvo acuerdo adicional.
- Contratación y gestión de couriers, embalaje y logística de bodega.
- Redacción de textos comerciales o de cata (el cliente los entrega; se puede cotizar aparte).
- Campañas de marketing digital, publicidad paga, gestión de redes sociales o email marketing.
- Emisión automática de boletas o facturas electrónicas con el SII (integración cotizable aparte).
- Venta internacional, versión multiidioma y suscripciones o clubes de vino.
- Costos de terceros: dominio, hosting, comisiones de Transbank y licencias de plataforma o plugins de pago.

## 4. Supuestos y responsabilidades del cliente
- Entregar fotos de producto en buena calidad (fondo limpio, resolución mínima de [1500 px]) antes de [fecha].
- Entregar los textos, precios, stock y datos de cada vino en formato ordenado (planilla Excel o similar).
- Entregar logo y lineamientos de marca en formato digital.
- Contar con contrato activo con Transbank y facilitar las credenciales a tiempo.
- Definir tarifas y condiciones de despacho antes de iniciar la configuración.
- Designar un contacto único para revisiones y aprobaciones, con respuestas en un máximo de [3] días hábiles.
- Cumplir
