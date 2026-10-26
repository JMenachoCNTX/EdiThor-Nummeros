"""Saca solo el contenido de la página (entre las marcas PAGINA) para publicarlo como artifact de Claude."""
import sys, pathlib
src = pathlib.Path(sys.argv[1]).read_text(encoding="utf-8")
ini, fin = src.index("<!-- PAGINA -->") + len("<!-- PAGINA -->"), src.index("<!-- /PAGINA -->")
pathlib.Path(sys.argv[2]).write_text(src[ini:fin].strip() + "\n", encoding="utf-8")
