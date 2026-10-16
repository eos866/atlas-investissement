"""Assemble l'application Atlas de l'investissement en un seul fichier.

Usage : python3 build.py
- index.html          : version autonome (GitHub Pages, tout serveur web statique)
- dist/artifact.html  : fragment sans <html>/<head>, pour une publication en artefact Claude
"""
from pathlib import Path

ROOT = Path(__file__).parent
SRC = ROOT / "src" / "atlas.html"
DATA = ROOT / "data"

page = SRC.read_text(encoding="utf-8")
page = page.replace("/*REGIONS*/", (DATA / "regions.json").read_text(encoding="utf-8"))
page = page.replace("/*INFRA*/", (DATA / "infra.json").read_text(encoding="utf-8"))

# Fragment pour artefact Claude
(ROOT / "dist").mkdir(exist_ok=True)
(ROOT / "dist" / "artifact.html").write_text(page, encoding="utf-8")

# Document HTML complet : en-tête (titre, polices, styles) puis corps
split_at = page.index('<div class="app">')
head, body = page[:split_at], page[split_at:]
standalone = (
    "<!doctype html>\n<html lang=\"fr\">\n<head>\n"
    "<meta charset=\"utf-8\">\n"
    "<meta name=\"viewport\" content=\"width=device-width, initial-scale=1, viewport-fit=cover\">\n"
    "<meta name=\"description\" content=\"Atlas cartographique de l'investissement au Sénégal : zones économiques, "
    "plateformes régionales APIX, projets prioritaires, infrastructures et données socio-démographiques ANSD.\">\n"
    "<style>html,body{margin:0}[hidden]{display:none!important}img{max-width:100%}</style>\n"
    + head
    + "</head>\n<body>\n"
    + body
    + "\n</body>\n</html>\n"
)
(ROOT / "index.html").write_text(standalone, encoding="utf-8")
print("index.html et dist/artifact.html générés")
