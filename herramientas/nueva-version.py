#!/usr/bin/env python3
"""Sube el número de versión de EdiThor.
Uso:  python3 herramientas/nueva-version.py "Qué cambió en esta versión"
Cambia APP_VER en index.html y agrega la nota al inicio de version.json."""
import json,re,sys,datetime,pathlib
raiz=pathlib.Path(__file__).resolve().parent.parent
nota=" ".join(sys.argv[1:]).strip()
if not nota: sys.exit('Falta la nota. Ejemplo: python3 herramientas/nueva-version.py "Girar formas"')
vj=raiz/"version.json";data=json.loads(vj.read_text(encoding="utf-8"))
v=int(data["v"])+1;hoy=datetime.date.today().isoformat()
data["v"]=v;data["fecha"]=hoy;data["notas"].insert(0,{"v":v,"fecha":hoy,"texto":nota})
vj.write_text(json.dumps(data,ensure_ascii=False,indent=1)+"\n",encoding="utf-8")
ix=raiz/"index.html";s=ix.read_text(encoding="utf-8")
s,n=re.subn(r"const APP_VER=\d+;",f"const APP_VER={v};",s)
assert n==1,"No encontré APP_VER en index.html"
ix.write_text(s,encoding="utf-8");print("EdiThor ahora es la versión",v)
