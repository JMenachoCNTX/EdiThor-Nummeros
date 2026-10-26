# Editor de Marca · NUMMEROS by CONTAX

Editor de piezas de marketing para **NUMMEROS** y **CONTAX**, parecido a Canva pero con todo lo de nuestras marcas ya cargado: plantillas, fotos, logos, colores y letras.

## Qué hace

- **Plantillas** de cada marca en versión clara y oscura: estado de WhatsApp, publicación 4:5 y cuadrada, comunicado, portada de Facebook, colaboración, foto de perfil de WhatsApp, folleto A4, tríptico (2 páginas), banner web y banner roll-up 85 × 200 cm.
- **QR**: pestaña QR para crear códigos de WhatsApp, página web, Telegram, correo, Wi-Fi o texto, con el logo de la marca en el centro. Plantillas de **porta QR para acrílico** (10 × 15 cm, 2 caras) y **QR para redes**.
- **Mockups**: marcos de laptop, celular, tablet y navegador para mostrar capturas de los sistemas; plantillas de mockup laptop, mockup celular y **guía paso a paso** (A4) para manuales.
- **Descargas**: PNG, PNG sin fondo, JPG, SVG (con las letras incluidas) y PDF; también **solo lo seleccionado** en PNG sin fondo o SVG.
- **Páginas**: un diseño puede tener varias páginas (agregar, duplicar, mover, eliminar). Se descarga la página actual en PNG/JPG o todas juntas en **PDF** (las piezas de imprenta salen a su tamaño real en cm).
- **Modo claro, oscuro o según el sistema**, con el botón de la barra superior.
- **Barras distribuidas**: arriba del lienzo, las opciones rápidas del elemento elegido (letra, tamaño, color, recortar, quitar fondo, agrupar…); abajo, las páginas, la vista previa y el zoom.
- **Paneles automáticos** (botón en la barra superior): a los lados quedan solo los íconos; los paneles se abren al tocar un ícono, y al tocar un elemento del diseño se abren sus opciones.
- **Vista previa en pantalla completa**, con flechas para pasar las páginas.
- El lienzo no se escapa de la pantalla: el diseño queda centrado y solo se desplaza cuando está ampliado.
- **Edición libre**: mover, agrandar, cambiar textos, letras, colores, encuadre de fotos, transparencia y orden de capas.
- **Copiar, cortar y pegar** elementos con ⌘ + C, ⌘ + X y ⌘ + V (también entre diseños distintos). Pegar texto copiado de otra app crea un texto nuevo.
- **Varios a la vez**: Shift + clic o arrastrar un recuadro para elegir varios; moverlos, escalarlos, alinearlos, **agrupar** (⌘ + G) o **unir en una sola imagen**.
- **Recortar**: doble clic sobre una imagen; se arrastra la imagen dentro del marco y se mueven los bordes.
- **Quitar fondo**: gratis en el navegador (herramienta de IMG.LY, la primera vez descarga unos 40 MB) o con IA de OpenAI.
- **Fotos y logos de marca**: los clásicos de los números, el Contador Virtual, íconos en relieve, la N y el isotipo de CONTAX en vector.
- **Subir imágenes** propias (por ejemplo las que se generan en ChatGPT o Gemini), también pegándolas con ⌘ + V.
- **IA** (solo en la versión de GitHub): Claude escribe el prompt de la imagen y los textos con la voz de cada marca. OpenAI o Gemini (a elección) crean la imagen y la ponen directo en el diseño. También pueden **mejorar** una imagen ya puesta (subida, de la marca o generada); Claude puede mirarla y preparar la instrucción.
- **Descargar** en PNG o JPG.

## IA: claves

En la pestaña **IA → Configurar claves** se pegan las claves. Basta Claude más OpenAI o Gemini:

- **Claude**: se crea en console.anthropic.com → API Keys (la API se paga aparte de la suscripción de Claude).
- **OpenAI**: se crea en platform.openai.com → API keys (la API se paga aparte de ChatGPT). OpenAI puede pedir verificar la organización antes de generar imágenes.
- **Gemini**: se crea en aistudio.google.com → Get API key. Los modelos de imagen de Gemini no tienen nivel gratis en la API: hay que activar la facturación.

Las claves se guardan solo en el navegador de quien las pega. No están en este repositorio.

## Dónde se usa

1. **Como artifact de Claude** (versión principal): guarda los diseños y las imágenes subidas en la nube.
2. **Desde este repositorio con GitHub Pages** (https://jmenachocntx.github.io/Sistema-Edici-n-MKT/): tiene la IA. Los diseños y las imágenes se guardan en el navegador de esa computadora.

## Cómo está organizado

| Carpeta | Contenido |
|---|---|
| `index.html` | Todo el editor (diseño y código) en un solo archivo |
| `clasicos/`, `colaboracion/`, `mini/` | Fotos de NUMMEROS y sus miniaturas |
| `graficos/` | Ilustraciones, íconos en relieve, elementos y patrones de NUMMEROS |
| `fotos-web/`, `objetos-web/` | Fotos del Contador Virtual y objetos 3D de CONTAX |
| `png/` | Logos de ambas marcas |
| `fonts/` | Letras: Akshar, Questrial y Adventor (reemplazo de Century Gothic) |
| `lib/qrcode.js` | Librería para generar los códigos QR (qrcode-generator, licencia MIT) |
| `herramientas/para-artifact.py` | Prepara `index.html` para publicarlo como artifact |

El contenido de la página está entre las marcas `<!-- PAGINA -->` y `<!-- /PAGINA -->`. Para publicar como artifact se usa solo esa parte:

```
python3 herramientas/para-artifact.py index.html pagina.html
```
