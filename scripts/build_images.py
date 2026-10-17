#!/usr/bin/env python3
"""
Regenera las ilustraciones (OpenMoji) que usa la app.

Las imágenes ya vienen incluidas en public/openmoji, así que esto SOLO hace falta
cuando agregas contenido con emoji nuevos. Es gratis y offline.

Uso:
    npm i -D openmoji          # trae las ~4.500 ilustraciones una sola vez
    python scripts/build_images.py

Lee los emoji usados en /content, copia el SVG de OpenMoji que corresponde a
public/openmoji/<clave>.svg y avisa de los que no encontró. La app calcula la misma
<clave> (puntos de código en hex, sin el selector FE0F), así que todo calza solo.
"""
from __future__ import annotations

import glob
import os
import re
import shutil
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "public", "openmoji")
SRC_CANDIDATES = [
    os.path.join(ROOT, "node_modules", "openmoji", "color", "svg"),
    os.path.join(ROOT, "node_modules", "openmoji", "svg"),
]

# Emoji de la interfaz (los que no están en el contenido)
UI = "☀️ 🧭 🔁 📚 📖 📈 🏅 🎯 📝 🏁 🔊 🐢 💡 👂 👄 🎙️ 🧩 🌄 🌆 🔀 🔤".split()

EMOJI_RE = re.compile(
    "(?:[\U0001F000-\U0001FAFF☀-➿⬀-⯿←-⇿™ℹ]"
    "[\U0001F3FB-\U0001F3FF️‍\U0001F000-\U0001FAFF☀-➿]*)"
)


def key(s: str) -> str:
    return "-".join(f"{ord(c):04X}" for c in s if c != "️")


def find_src(src_dir: str, s: str) -> str | None:
    full = "-".join(f"{ord(c):04X}" for c in s)
    nofe = key(s)
    base = f"{ord(s[0]):04X}"
    for name in (full, nofe, base):
        p = os.path.join(src_dir, name + ".svg")
        if os.path.exists(p):
            return p
    return None


def main() -> int:
    src = next((d for d in SRC_CANDIDATES if os.path.isdir(d)), None)
    if not src:
        print("No encontré OpenMoji. Instálalo con:  npm i -D openmoji")
        return 1

    emojis: set[str] = set(UI)
    for f in glob.glob(os.path.join(ROOT, "content", "**", "*.json"), recursive=True):
        for m in EMOJI_RE.findall(open(f, encoding="utf-8").read()):
            emojis.add(m)

    os.makedirs(OUT, exist_ok=True)
    copied, missing = 0, []
    for e in sorted(emojis):
        k = key(e)
        if not k:
            continue
        p = find_src(src, e)
        if p:
            shutil.copy(p, os.path.join(OUT, k + ".svg"))
            copied += 1
        else:
            missing.append(e)
    print(f"Emoji usados: {len(emojis)} | imágenes listas: {copied} | sin OpenMoji: {len(missing)}")
    if missing:
        print("Sin imagen (se verán con el emoji del sistema):", " ".join(missing))
    return 0


if __name__ == "__main__":
    sys.exit(main())
