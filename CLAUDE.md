# EdiThor Nummeros — guía para Claude

Jhonny (CONTAX / NUMMEROS, Santa Cruz, Bolivia) no es programador y no lee inglés:
responder siempre en español, en palabras simples, para principiantes.

## Para qué sirve
Editor de piezas de marketing, parecido a Canva, con todo lo de las marcas ya cargado
(plantillas, fotos, logos, colores, letras). Permite diseñar estados y publicaciones de
WhatsApp/Facebook/Instagram/TikTok, impresos (folletos, trípticos, roll-up, porta QR),
mockups de los sistemas, códigos QR, y descargar en PNG, JPG, PDF, SVG, PowerPoint o ZIP.
Tiene una pestaña de IA (Claude escribe prompts y textos; OpenAI o Gemini crean imágenes).
El detalle de cada función está en `README.md`.

## Para qué empresa
Uso interno de **NUMMEROS** y **CONTAX** (piezas de las dos marcas, en versión clara y oscura).

## Cómo está armado (archivos principales)
- `index.html` — TODA la aplicación (HTML + CSS + JS en un solo archivo grande, ~430 KB). Sin compilación.
- `firebase-config.js` — datos de conexión a Firebase (proyecto `edithor-nummeros`). Si se pone `null`, guarda solo en el navegador.
- `firestore.rules` — reglas de seguridad de Firestore (lista de correos autorizados).
- `version.json` — número de versión actual y notas de cada versión.
- `herramientas/nueva-version.py` — sube la versión (cambia `APP_VER` en `index.html` y agrega la nota en `version.json`).
- `lib/qrcode.js` — librería para los QR.
- Carpetas de imágenes de marca: `clasicos/`, `colaboracion/`, `fotos-web/`, `marca/`, etc.; letras en `fonts/`.
- `CNAME` — dominio propio.
- `manuales/` — manuales de marca completos de NUMMEROS y CONTAX (ver `manuales/README.md`). Son copia de los artefactos de claude.ai: cuando se actualice un artefacto de marca, copiar aquí la versión nueva para que queden iguales.

## Dónde se guardan los datos
- **Firebase Firestore** (proyecto «EdiThor Nummeros»), entrando con cuenta de Google autorizada:
  - `designs` — diseños del equipo (cada uno guarda su apartado en `sec`, quién lo creó y quién lo cambió).
  - `trash` — papelera. `tpls` — plantillas. `images` (con subpartes `parts`) — imágenes subidas.
  - `editing` — quién está editando qué diseño en este momento. `users` — usuarios.
  - `meta/carpetas` (secciones y apartados), `meta/uploads`, `meta/marcas`, `meta/ialimit`.
  - `secrets/ia` — claves de IA (Claude, OpenAI, Gemini). Se cargan desde la pantalla IA → Configurar claves, **nunca en el código**.
- Sin Firebase: IndexedDB / `localStorage` del navegador (claves `ed.*`).
- Plan gratis de Firestore: 1 GB; el sistema muestra el espacio usado.

## Cómo se publica
- GitHub Pages desde la rama `main` del repo `JMenachoCNTX/EdiThor-Nummeros` (repo **público**).
- Dominio: https://edithornummeros.contaxbolivia.com (archivo `CNAME`).
- **Cada actualización lleva nuevo número de versión**: antes del commit correr
  `python3 herramientas/nueva-version.py "Qué cambió (en español)"`.
  Los commits siguen el formato `vNN: descripción corta en español` (ej. `v45: …`).
- Si cambia `firestore.rules`, NO se aplica sola: hay que copiarla y pegarla en
  Firebase → Firestore Database → Reglas → Publicar.

## Cuidados importantes
- El repositorio es público: nunca poner claves de API, contraseñas ni datos de clientes en el código.
  Las claves de IA van solo en Firestore (`secrets/ia`).
- La `apiKey` de `firebase-config.js` NO es secreta (va en toda página con Firebase); la seguridad
  la dan el inicio de sesión con Google y `firestore.rules`. No abrir las reglas (`if true`).
- Para dar acceso a otra persona: agregar su correo en `firestore.rules` y volver a publicar las reglas en la consola.
- Las imágenes de marca se renuevan con cada versión (evitan caché vieja): por eso subir siempre la versión.
- Los diseños guardados se abren bloqueados (candado) para evitar borrados accidentales; respetar ese comportamiento.
- Mantener el estilo de los sistemas NUMMEROS: menú menta, verde principal, Akshar en títulos y Questrial en textos, modo claro y oscuro.
