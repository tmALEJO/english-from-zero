#!/usr/bin/env python3
"""
Valida el contenido de /content antes de compilar.

Revisa:
  - que cada unidad del currículo con status "ready" tenga su archivo y viceversa
  - ids únicos y referencias a ítems que existen
  - máximo 4 ítems nuevos por lección (carga cognitiva)
  - índices de respuesta válidos en fill / discover / preguntas
  - palabras de historias y diálogos que no están en el diccionario (aviso)

Uso:  python scripts/validate_content.py          (o: npm run content:check)
      python scripts/validate_content.py --strict (los avisos también fallan)
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CONTENT = ROOT / "content"
MAX_NEW = 4

errors: list[str] = []
warnings: list[str] = []


def norm(s: str) -> str:
    s = s.lower().replace("’", "'")
    s = re.sub(r"[^a-z0-9' ]+", " ", s)
    return re.sub(r"\s+", " ", s).strip()


def load(p: Path):
    try:
        return json.loads(p.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        errors.append(f"{p.relative_to(ROOT)}: JSON inválido ({e})")
        return None


def main() -> int:
    strict = "--strict" in sys.argv
    curriculum = load(CONTENT / "curriculum.json")
    dictionary = load(CONTENT / "dictionary.json") or []
    units = {}
    for f in sorted((CONTENT / "units").glob("*.json")):
        u = load(f)
        if u:
            if u["id"] != f.stem:
                errors.append(f"{f.name}: el id '{u['id']}' debe ser igual al nombre del archivo")
            units[u["id"]] = u

    ready = {r["id"] for r in curriculum["units"] if r["status"] == "ready"}
    all_refs = {r["id"] for r in curriculum["units"]}
    for uid in ready - units.keys():
        errors.append(f"curriculum.json: '{uid}' está como ready pero no existe content/units/{uid}.json")
    for uid in units.keys() - all_refs:
        errors.append(f"La unidad '{uid}' no está registrada en curriculum.json")
    for uid in units.keys() & all_refs:
        if uid not in ready:
            warnings.append(f"'{uid}' tiene archivo pero en curriculum.json sigue como planned")

    items: dict[str, dict] = {}
    forms: set[str] = set()
    for u in units.values():
        for it in u["items"]:
            if it["id"] in items:
                errors.append(f"Ítem repetido: {it['id']}")
            items[it["id"]] = it
            forms.add(norm(re.sub(r"[.!?]+$", "", it["en"])))
            forms.update(norm(f) for f in it.get("forms", []))
    for e in dictionary:
        forms.add(norm(e["en"]))
        forms.update(norm(f) for f in e.get("forms", []))

    def known(w: str) -> bool:
        if w in forms or w.isdigit():
            return True
        return any(w.endswith(c) and w[: -len(c)] in forms for c in ("s", "es", "ed", "d", "ing"))

    unknown: dict[str, set[str]] = {}

    def scan(text: str, where: str):
        for w in norm(text).split():
            if not known(w):
                unknown.setdefault(w, set()).add(where)

    lesson_ids: set[str] = set()
    for u in units.values():
        for l in u["lessons"]:
            where = f"{u['id']}/{l['id']}"
            if l["id"] in lesson_ids:
                errors.append(f"Lección repetida: {l['id']}")
            lesson_ids.add(l["id"])
            max_new = MAX_NEW + (1 if u["level"] in ("B2", "C1") else 0)
            if len(l["newItems"]) > max_new:
                errors.append(f"{where}: {len(l['newItems'])} ítems nuevos (máximo {max_new})")
            for iid in l["newItems"]:
                if iid not in items:
                    errors.append(f"{where}: newItems referencia '{iid}', que no existe")
            for a in l["activities"]:
                t = a["type"]
                for iid in a.get("items", []):
                    if iid not in items:
                        errors.append(f"{where}: actividad {t} usa '{iid}', que no existe")
                if t in ("fill", "discover") and not 0 <= a["answer"] < len(a["options"]):
                    errors.append(f"{where}: {t} tiene answer fuera de rango")
                if t == "story":
                    for p in a["paragraphs"]:
                        scan(p["en"], where)
                    for q in a.get("questions", []):
                        if not 0 <= q["answer"] < len(q["options"]):
                            errors.append(f"{where}: pregunta '{q['q']}' con answer fuera de rango")
                if t == "dialogue":
                    for line in a["lines"]:
                        scan(line["en"], where)
                if t == "discover":
                    for ex in a["examples"]:
                        scan(ex["en"], where)

    for w, places in sorted(unknown.items()):
        warnings.append(f"Palabra sin entrada de diccionario: '{w}' (en {', '.join(sorted(places))})")

    print(f"Unidades: {len(units)} · Lecciones: {len(lesson_ids)} · Ítems: {len(items)} · Diccionario extra: {len(dictionary)}")
    for w in warnings:
        print("  aviso:", w)
    for e in errors:
        print("  ERROR:", e)
    if errors or (strict and warnings):
        print("\nEl contenido tiene problemas. Corrígelos antes de compilar.")
        return 1
    print("\nContenido OK.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
