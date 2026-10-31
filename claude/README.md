# Carpeta `claude/` — diseños que hace Claude

Aparecen en EdiThor en la pestaña **Claude**. Al tocar uno se abre una **copia editable** (el original queda igual).

- `index.json` — lista de diseños: `id`, `name`, `brand` (nummeros/contax), `w`, `h`, `thumb`, `file`, `nota`, `sec` (apartado sugerido, ej. `whatsapp/estados`) y `fecha` opcional (AAAA-MM-DD: la copia queda con esa fecha de publicación y aparece en el Calendario).
- `disenos/<id>.json` — las páginas del diseño en el mismo formato que guarda EdiThor (`{"pages":[...]}`).
- `disenos/<id>.jpg` — miniatura.
- `img/` — capturas e imágenes que usan estos diseños.

Para crear diseños nuevos, Claude los arma con el mismo motor de EdiThor (sus funciones `T`, `R`, `I`, `Dv`, `logo`, `brandText`) para que queden 100 % editables.
