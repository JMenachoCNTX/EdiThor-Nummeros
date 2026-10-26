# Editor de Marca · NUMMEROS by CONTAX

Editor de piezas de marketing para **NUMMEROS** y **CONTAX**, parecido a Canva pero con todo lo de nuestras marcas ya cargado: plantillas, fotos, logos, colores y letras.

## Qué hace

- **Plantillas** de cada marca en versión clara y oscura: estado de WhatsApp, publicación 4:5 y cuadrada, comunicado, portada de Facebook y colaboración.
- **Edición libre**: mover, agrandar, cambiar textos, letras, colores, encuadre de fotos, transparencia y orden de capas.
- **Fotos y logos de marca**: los clásicos de los números, el Contador Virtual, íconos en relieve, la N y el isotipo de CONTAX en vector.
- **Subir imágenes** propias (por ejemplo las que se generan en ChatGPT o Gemini), también pegándolas con ⌘ + V.
- **IA** (solo en la versión de GitHub): Claude escribe el prompt de la imagen y los textos con la voz de cada marca; OpenAI genera la imagen y la pone directo en el diseño.
- **Descargar** en PNG o JPG.

## IA: claves

En la pestaña **IA → Configurar claves** se pegan dos claves:

- **Claude**: se crea en console.anthropic.com → API Keys (la API se paga aparte de la suscripción de Claude).
- **OpenAI**: se crea en platform.openai.com → API keys (la API se paga aparte de ChatGPT). OpenAI puede pedir verificar la organización antes de generar imágenes.

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
| `herramientas/para-artifact.py` | Prepara `index.html` para publicarlo como artifact |

El contenido de la página está entre las marcas `<!-- PAGINA -->` y `<!-- /PAGINA -->`. Para publicar como artifact se usa solo esa parte:

```
python3 herramientas/para-artifact.py index.html pagina.html
```
