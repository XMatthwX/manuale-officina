#!/usr/bin/env python3
"""Costruisce l'app installabile in docs/ partendo da src/app.html e src/seed.json.
Uso: python3 tools/build.py   (poi commit e push: GitHub Pages pubblica docs/)"""
import json, hashlib, pathlib, shutil, datetime
ROOT = pathlib.Path(__file__).resolve().parent.parent
SRC, OUT = ROOT / "src", ROOT / "docs"
app = (SRC / "app.html").read_text(encoding="utf-8")
seed = json.loads((SRC / "seed.json").read_text(encoding="utf-8"))
version = hashlib.sha1((app + json.dumps(seed, sort_keys=True)).encode()).hexdigest()[:10]
stamp = datetime.date.today().isoformat()
head = f"""<!doctype html><html lang="it"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<meta name="theme-color" content="#1a2127">
<meta name="description" content="Manuale d'officina interattivo con coppie di serraggio">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
<meta name="apple-mobile-web-app-title" content="Coppie">
<link rel="manifest" href="manifest.webmanifest">
<link rel="icon" type="image/png" href="icon-192.png">
<link rel="apple-touch-icon" href="apple-touch-icon.png">
<style>:root{{color-scheme:light;padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}}body{{margin:0;font:14px system-ui,sans-serif}}img{{max-width:100%}}[hidden]{{display:none!important}}</style>
<script>window.APP_VERSION={json.dumps(version)};window.APP_BUILD={json.dumps(stamp)};</script>
<script src="seed.js?v={version}"></script>
</head><body>
"""
tail = """
<script>
if ("serviceWorker" in navigator) addEventListener("load", () => navigator.serviceWorker.register("sw.js").catch(() => {}));
</script>
</body></html>
"""
OUT.mkdir(exist_ok=True)
(OUT / "index.html").write_text(head + app + tail, encoding="utf-8")
(OUT / "seed.js").write_text("window.SEED_DATA = " + json.dumps(seed, ensure_ascii=False) + ";\n", encoding="utf-8")
(OUT / "sw.js").write_text((ROOT / "tools" / "sw.template.js").read_text().replace("__VERSION__", version), encoding="utf-8")
for f in ["manifest.webmanifest", "icon-192.png", "icon-512.png", "icon-maskable-512.png", "apple-touch-icon.png"]:
    shutil.copy(ROOT / "tools" / "static" / f, OUT / f)
(OUT / ".nojekyll").write_text("")
print("Versione", version, "costruita in", OUT)
