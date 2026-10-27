# EdiThor Nummeros

**EdiThor** es el editor de piezas de marketing para **NUMMEROS** y **CONTAX**, parecido a Canva pero con todo lo de nuestras marcas ya cargado: plantillas, fotos, logos, colores y letras.

## Qué hace

- **Inicio**: bienvenida con una foto de los clásicos de NUMMEROS, accesos rápidos a las plantillas y los diseños del equipo con un filtro por persona.
- **Se ve como los demás sistemas de NUMMEROS**: menú lateral menta, verde principal, Akshar en los títulos y Questrial en los textos (modo claro y oscuro).
- **Al entrar** aparece la pantalla de espera «los clásicos trabajando» del kit de marca durante unos 3 segundos.
- **Plantillas** de cada marca en versión clara y oscura: estado de WhatsApp, publicación 4:5 y cuadrada, comunicado, portada de Facebook, colaboración, foto de perfil de WhatsApp, folleto A4, tríptico (2 páginas), banner web y banner roll-up 85 × 200 cm.
- **QR**: pestaña QR para crear códigos de WhatsApp, página web, Telegram, correo, Wi-Fi o texto, con el logo de la marca en el centro. Plantillas de **porta QR para acrílico** (10 × 15 cm, 2 caras) y **QR para redes**.
- **Mockups**: marcos de laptop, celular, tablet y navegador para mostrar capturas de los sistemas; plantillas de mockup laptop, mockup celular y **guía paso a paso** (A4) para manuales.
- **Descargas**: PNG, PNG sin fondo, JPG, SVG (con las letras incluidas) y PDF; también **solo lo seleccionado** en PNG sin fondo o SVG.
- **Páginas**: un diseño puede tener varias páginas (agregar, duplicar, mover, eliminar). Se descarga la página actual en PNG/JPG o todas juntas en **PDF** (las piezas de imprenta salen a su tamaño real en cm).
- **Modo claro, oscuro o según el sistema**, con el botón de la barra superior.
- **Barras distribuidas**: arriba del lienzo, las opciones rápidas del elemento elegido (letra, tamaño, color, recortar, quitar fondo, agrupar…); abajo, las páginas, la vista previa y el zoom.
- **Paneles automáticos** (botón en la barra superior): a los lados quedan solo los íconos; los paneles se abren al tocar un ícono, y al tocar un elemento del diseño se abren sus opciones.
- **Menús al pasar el cursor**: las pestañas de los lados, Descargar y el tema se muestran al pasar el cursor; un clic los deja fijos.
- **Cuadrícula** (botón abajo o ⌘ + '): fina, media o gruesa, con líneas del centro y opción de pegar los elementos a la cuadrícula. No sale en las descargas.
- **Vista previa en pantalla completa**, con flechas para pasar las páginas.
- El lienzo no se escapa de la pantalla: el diseño queda centrado y solo se desplaza cuando está ampliado.
- **Edición libre**: mover, agrandar, cambiar textos, letras, colores, encuadre de fotos, transparencia y orden de capas.
- **Copiar, cortar y pegar** elementos con ⌘ + C, ⌘ + X y ⌘ + V (también entre diseños distintos). Pegar texto copiado de otra app crea un texto nuevo.
- **Varios a la vez**: Shift + clic o arrastrar un recuadro para elegir varios; moverlos, escalarlos, alinearlos, **agrupar** (⌘ + G) o **unir en una sola imagen**.
- **Recortar**: doble clic sobre una imagen; se arrastra la imagen dentro del marco y se mueven los bordes.
- **Quitar fondo**: gratis en el navegador (herramienta de IMG.LY, la primera vez descarga unos 40 MB) o con IA de OpenAI.
- **Fotos y gráficos de marca**: los clásicos de los números y el Contador Virtual; ilustraciones, íconos en relieve, elementos y patrones de NUMMEROS; ilustraciones, íconos en relieve blanco y azul noche, elementos, pasos, recortes del isotipo y tramas de CONTAX; la N y el isotipo de CONTAX en vector. En la pestaña Fotos hay atajos para saltar a cada grupo.
- **Subir imágenes** propias (por ejemplo las que se generan en ChatGPT o Gemini), también pegándolas con ⌘ + V.
- **IA** (solo en la versión de GitHub): Claude escribe el prompt de la imagen y los textos con la voz de cada marca. OpenAI o Gemini (a elección) crean la imagen y la ponen directo en el diseño. También pueden **mejorar** una imagen ya puesta (subida, de la marca o generada); Claude puede mirarla y preparar la instrucción.
- **Descargar** en PNG o JPG.

## IA: claves

En la pestaña **IA → Configurar claves** se pegan las claves. Basta Claude más OpenAI o Gemini:

- **Claude**: se crea en platform.claude.com → API Keys. Con el plan Max vienen USD 100 de crédito al mes para la API.
- **OpenAI**: se crea en platform.openai.com → API keys (la API se paga aparte de ChatGPT). OpenAI puede pedir verificar la organización antes de generar imágenes.
- **Gemini**: se crea en aistudio.google.com → Get API key. Los modelos de imagen de Gemini no tienen nivel gratis en la API: hay que activar la facturación.

Con la nube activa, las claves se guardan en Firestore (`secrets/ia`): aparecen solas en cualquier navegador y solo las leen las cuentas autorizadas en `firestore.rules`. Nunca están en este repositorio: un secreto de GitHub no sirve para esto, porque la página corre en el navegador y no tiene servidor.

## Dónde se usa

- **En línea:** https://edithornummeros.contaxbolivia.com (GitHub Pages con dominio propio).
- Se entra con una cuenta de Google autorizada. Los diseños y las imágenes se guardan en **Firebase** (proyecto «EdiThor Nummeros»), así se ven desde cualquier computadora.
- **Diseños compartidos**: todos los usuarios ven y pueden cambiar los diseños de todos. Cada diseño guarda quién lo creó y quién lo cambió por última vez. Si dos personas cambian el mismo diseño al mismo tiempo, queda el último que se guardó.
- Usuarios con acceso: jhonnymenacho04@gmail.com, info@contaxbolivia.com, sol@contaxbolivia.com y contaxcontabilidad5@gmail.com.
- Sin internet o sin entrar, el editor guarda en el navegador; después, en «Mis diseños», se suben a la nube con un clic.
- También existe una versión dentro de Claude (artifact), sin IA.

## Firebase

- `firebase-config.js`: datos de la app web de Firebase (no son secretos).
- `firestore.rules`: quién puede entrar. Solo las cuentas de la lista pueden ver y guardar. Para dar acceso a alguien, se agrega su correo y se publican de nuevo las reglas en Firebase → Firestore → Reglas.
- Se usa **Authentication** (Google) y **Firestore**. Las imágenes se guardan dentro de Firestore en partes, así no hace falta el plan de pago de Storage.
- En Authentication → Configuración → Dominios autorizados deben estar `edithornummeros.contaxbolivia.com` y `jmenachocntx.github.io`.

## Cómo está organizado

| Carpeta | Contenido |
|---|---|
| `index.html` | Todo el editor (diseño y código) en un solo archivo |
| `clasicos/`, `colaboracion/`, `mini/` | Fotos de NUMMEROS y sus miniaturas |
| `graficos/` | Ilustraciones, íconos en relieve, elementos y patrones de NUMMEROS |
| `fotos-web/`, `objetos-web/` | Fotos del Contador Virtual y objetos 3D de CONTAX |
| `graficos-contax/` | Ilustraciones, íconos en relieve, elementos, pasos, recortes y tramas de CONTAX (exportados del kit Marca CONTAX) |
| `marca/` | Logotipos SVG de NUMMEROS para la interfaz, favicon e ícono de la app |
| `png/` | Logos de ambas marcas |
| `fonts/` | Letras: Akshar, Questrial y Adventor (reemplazo de Century Gothic) |
| `firebase-config.js`, `firestore.rules` | Conexión con Firebase y reglas de acceso |
| `lib/qrcode.js` | Librería para generar los códigos QR (qrcode-generator, licencia MIT) |
| `herramientas/para-artifact.py` | Prepara `index.html` para publicarlo como artifact |

El contenido de la página está entre las marcas `<!-- PAGINA -->` y `<!-- /PAGINA -->`. Para publicar como artifact se usa solo esa parte:

```
python3 herramientas/para-artifact.py index.html pagina.html
```
