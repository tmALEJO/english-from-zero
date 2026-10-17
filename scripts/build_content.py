#!/usr/bin/env python3
"""
Compila el contenido escrito en formato compacto (content/src/*.py) a los JSON que usa la app.

Por qué existe: escribir miles de palabras y cientos de lecciones a mano en JSON es lento y
propenso a errores. Aquí cada unidad se escribe como una lista de palabras (una por línea) y
unas pocas actividades especiales (gramática por descubrimiento, diálogos, historias, juegos
de rol, escritura). El compilador arma las lecciones solo:

  - grupos de máximo 4 palabras nuevas por lección (carga cognitiva baja)
  - presentación con imagen + audio, práctica variada (escuchar, leer, imagen, armar, dictado)
  - reciclaje de palabras anteriores de la misma unidad en cada lección
  - las actividades especiales repartidas a lo largo de la unidad
  - una lección final de repaso con historia, juego de rol, escritura y dictado
  - exámenes de control cada 6 unidades y examen final de cada nivel

Uso:  python scripts/build_content.py      (o: npm run content:build)

Las unidades escritas a mano en content/units/ (u00 a u07) se respetan tal cual.
"""
from __future__ import annotations

import json
import re
import sys
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CONTENT = ROOT / "content"
SRC = CONTENT / "src"
UNITS_DIR = CONTENT / "units"
GENERATED_MARK = "_generated"

LEVELS = [
    {"id": "A0", "name": "Primeros pasos", "description": "Sonidos, saludos y frases para sobrevivir el primer minuto de conversación."},
    {"id": "A1", "name": "Principiante", "description": "Hablas de ti, tu familia, tu casa y tu día. Pides comida, preguntas precios y direcciones."},
    {"id": "A2", "name": "Elemental", "description": "Cuentas lo que pasó, haces planes, comparas y te defiendes en viajes, compras y el médico."},
    {"id": "B1", "name": "Intermedio", "description": "Conversas sobre temas conocidos, cuentas experiencias, das opiniones y explicas razones."},
    {"id": "B2", "name": "Intermedio alto", "description": "Debates con fluidez, entiendes noticias y series, y escribes textos claros y detallados."},
    {"id": "C1", "name": "Avanzado", "description": "Usas el idioma con flexibilidad y precisión en lo social, académico y profesional."},
]
LEVEL_IDS = [l["id"] for l in LEVELS]
CHECKPOINT_EVERY = 6

warnings: list[str] = []
errors: list[str] = []


# ─── Utilidades ──────────────────────────────────────────────

def norm(s: str) -> str:
    s = unicodedata.normalize("NFD", s.lower())
    s = "".join(c for c in s if unicodedata.category(c) != "Mn")
    s = s.replace("’", "'")
    s = re.sub(r"[^a-z0-9' ]+", " ", s)
    return re.sub(r"\s+", " ", s).strip()


def slug(s: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", norm(s)).strip("-")[:40] or "x"


def lines(block: str) -> list[str]:
    out = []
    for raw in (block or "").splitlines():
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        out.append(line)
    return out


def pair(line: str) -> tuple[str, str, list[str]]:
    parts = [p.strip() for p in line.split("||")]
    if len(parts) < 2:
        raise ValueError(f"Falta la traducción con '||' en: {line}")
    return parts[0], parts[1], parts[2:]


# ─── Mini lenguaje para escribir unidades ───────────────────

def D(topic, intro, examples, question, options, answer, rule, rule_examples="", fills=""):
    """Gramática inductiva: ejemplos → pregunta → regla (+ ejercicios de completar)."""
    exs = []
    for ln in lines(examples):
        en, es, rest = pair(ln)
        mark = [m.strip() for m in rest[0].split(",")] if rest and rest[0] else []
        exs.append({"en": en, "es": es, "mark": mark})
    rex = [{"en": a, "es": b} for a, b, _ in map(pair, lines(rule_examples))]
    acts = [{"type": "discover", "topic": topic, "intro": intro, "examples": exs, "question": question,
             "options": options, "answer": answer, "rule": rule, "ruleExamples": rex}]
    acts += parse_fills(fills)
    return {"kind": "discover", "acts": acts}


def parse_fills(block: str) -> list[dict]:
    out = []
    for ln in lines(block):
        p = [x.strip() for x in ln.split("|")]
        if len(p) < 3:
            errors.append(f"Completar mal escrito: {ln}")
            continue
        a = {"type": "fill", "en": p[0], "options": [o.strip() for o in p[1].split("/")], "answer": int(p[2])}
        if len(p) > 3 and p[3]:
            a["es"] = p[3]
        if len(p) > 4 and p[4]:
            a["explain"] = p[4]
        if "___" not in a["en"]:
            errors.append(f"Completar sin '___': {ln}")
        out.append(a)
    return out


def dialogue(title, scene, script):
    ls = []
    for ln in lines(script):
        who, rest = ln.split(":", 1)
        en, es, _ = pair(rest)
        ls.append({"who": who.strip(), "en": en, "es": es})
    return {"kind": "dialogue", "acts": [{"type": "dialogue", "title": title, "scene": scene, "lines": ls}]}


def story(title, emoji, text, questions=()):
    ps = [{"en": en, "es": es} for en, es, _ in map(pair, lines(text))]
    qs = [{"q": q, "options": list(o), "answer": a} for q, o, a in questions]
    return {"kind": "story", "acts": [{"type": "story", "title": title, "emoji": emoji, "paragraphs": ps, "questions": qs}]}


def roleplay(title, scene, script):
    turns: list[dict] = []
    for ln in lines(script):
        if ln[0] in "+-":
            en, es, rest = pair(ln[1:].strip())
            opt = {"en": en, "es": es, "ok": ln[0] == "+"}
            if rest and rest[0]:
                opt["why"] = rest[0]
            if not turns or "you" not in turns[-1]:
                turns.append({"you": True, "options": []})
            turns[-1]["options"].append(opt)
        else:
            who, rest = ln.split(":", 1)
            en, es, _ = pair(rest)
            turns.append({"who": who.strip(), "en": en, "es": es})
    for t in turns:
        if "you" in t and not any(o["ok"] for o in t["options"]):
            errors.append(f"Juego de rol '{title}': un turno no tiene ninguna opción correcta (+)")
    return {"kind": "roleplay", "acts": [{"type": "roleplay", "title": title, "scene": scene, "turns": turns}]}


def tip(emoji, title, text):
    return {"kind": "tip", "acts": [{"type": "tip", "emoji": emoji, "title": title, "text": text}]}


UNITS: list[dict] = []
READINGS: list[dict] = []


def unit(id, level, title, emoji, can_do, summary, items, grammar=(), extras=(), writes="", dictations="", speak=""):
    UNITS.append(dict(id=id, level=level, title=title, emoji=emoji, can_do=can_do, summary=summary,
                      items=items, grammar=list(grammar), extras=list(extras), writes=writes,
                      dictations=dictations, speak=speak))


def reading(id, level, title, emoji, kind, summary, text, questions=()):
    sents = []
    for ln in lines(text):
        who = None
        m = re.match(r"^([A-Z][\w .']{0,20}):\s+(.*)$", ln)
        if kind == "dialogue" and m:
            who, ln = m.group(1), m.group(2)
        en, es, _ = pair(ln)
        s = {"en": en, "es": es}
        if who:
            s["who"] = who
        sents.append(s)
    READINGS.append({"id": id, "level": level, "title": title, "emoji": emoji, "kind": kind, "summary": summary,
                     "sentences": sents, "questions": [{"q": q, "options": list(o), "answer": a} for q, o, a in questions]})


# ─── Compilación de una unidad ──────────────────────────────

def parse_items(u: dict, seen: dict[str, str]) -> list[dict]:
    short = u["id"].split("-")[0]
    out, ids = [], set()
    for ln in lines(u["items"]):
        p = [x.strip() for x in ln.split("|")]
        if len(p) < 2:
            errors.append(f"{u['id']}: palabra sin traducción: {ln}")
            continue
        en, es = p[0], p[1]
        # "chicken (animal)": el paréntesis distingue significados; no se muestra ni se lee en voz alta.
        label = ""
        m = re.match(r"^(.*?)\s*\(([^)]*)\)\s*$", en)
        if m:
            en, label = m.group(1).strip(), m.group(2).strip()
            if re.fullmatch(r"[ABC][012]", label):
                continue  # repetición intencional de una palabra ya vista: se repasa desde su unidad
        key = norm(en + " " + label) if label else norm(en)
        if key in seen:
            warnings.append(f"{u['id']}: '{en}' ya está en {seen[key]}; se omite (se repasa desde allá)")
            continue
        seen[key] = u["id"]
        iid = f"{short}.{slug(en + ('-' + label if label else ''))}"
        while iid in ids:
            iid += "x"
        ids.add(iid)
        it = {"id": iid, "en": en, "es": es, "kind": "chunk" if len(en.split()) > 1 else "word"}
        if len(p) > 2 and p[2]:
            it["emoji"] = p[2]
        if len(p) > 3 and p[3]:
            it["say"] = p[3]
        if len(p) > 4 and p[4]:
            it["tip"] = p[4]
        if label and label not in ("participle", "past"):
            it.setdefault("tip", f"Aquí con el sentido de: {label}.")
        out.append(it)
    return out


def modes_for(level: str, group: list[dict]) -> list[dict]:
    ids = [g["id"] for g in group]
    chunks = [g["id"] for g in group if g["kind"] == "chunk"]
    acts = []
    if level in ("A0", "A1"):
        acts.append({"type": "auto", "items": ids, "modes": ["listen-pick", "picture-pick"]})
        acts.append({"type": "auto", "items": ids, "modes": ["read-pick", "build"], "count": len(ids) + len(chunks)})
        acts.append({"type": "auto", "items": (chunks or ids)[:2], "modes": ["dictation"]})
    elif level == "A2":
        acts.append({"type": "auto", "items": ids, "modes": ["listen-pick", "picture-pick", "read-pick"], "count": len(ids) * 2})
        acts.append({"type": "auto", "items": ids, "modes": ["build", "dictation"], "count": max(3, len(ids))})
    else:
        acts.append({"type": "auto", "items": ids, "modes": ["read-pick", "listen-pick"], "count": len(ids) * 2})
        acts.append({"type": "auto", "items": ids, "modes": ["dictation", "build"], "count": len(ids)})
        acts.append({"type": "auto", "items": ids, "modes": ["picture-pick"], "count": 2})
    return acts


FOCUS_CYCLE = ["listening", "vocabulary", "reading", "listening"]


def compile_unit(u: dict, seen: dict[str, str]) -> dict:
    items = parse_items(u, seen)
    level = u["level"]
    size = 5 if level in ("B2", "C1") else 4  # avanzados toleran un poco más de carga
    groups = [items[i:i + size] for i in range(0, len(items), size)]
    extras = u["extras"]
    final_kinds = {"roleplay"}
    # La última historia y el último juego de rol van en la lección final de repaso.
    last_story = max((i for i, e in enumerate(extras) if e["kind"] == "story"), default=None)
    last_role = max((i for i, e in enumerate(extras) if e["kind"] == "roleplay"), default=None)
    placed = [e for i, e in enumerate(extras) if i not in (last_story, last_role)]
    final_extra = [extras[i] for i in (last_story, last_role) if i is not None]

    lessons = []
    n = max(1, len(groups))
    # Reparte las actividades especiales a lo largo de las lecciones (la gramática, temprano).
    slots: dict[int, list[dict]] = {}
    for k, e in enumerate(placed):
        if e["kind"] == "discover":
            pos = min(n - 1, 1 + k * max(1, n // max(1, len(placed))))
        else:
            pos = min(n - 1, round((k + 1) * n / (len(placed) + 1)))
        slots.setdefault(pos, []).append(e)

    for gi, group in enumerate(groups):
        acts: list[dict] = []
        if gi == 0 and u["grammar"]:
            pass
        for half in (group[:2], group[2:4], group[4:]):
            if half:
                acts.append({"type": "present", "items": [g["id"] for g in half]})
        acts += modes_for(level, group)
        earlier = [g["id"] for gg in groups[:gi] for g in gg]
        if earlier:
            acts.append({"type": "auto", "items": earlier[-6:], "modes": ["read-pick", "listen-pick"], "count": 3})
        focus = FOCUS_CYCLE[gi % len(FOCUS_CYCLE)]
        for e in slots.get(gi, []):
            acts += e["acts"]
            if e["kind"] == "discover":
                focus = "grammar"
        first = ", ".join(g["en"] for g in group[:3])
        lessons.append({
            "id": f"{u['id']}-l{gi + 1}",
            "title": f"{gi + 1}. {first}" + ("…" if len(group) > 3 else ""),
            "focus": focus,
            "newItems": [g["id"] for g in group],
            "activities": acts,
        })

    # Lección final: historia, conversación, escritura y dictado con todo lo de la unidad.
    final: list[dict] = []
    for e in final_extra:
        final += e["acts"]
    for ln in lines(u["writes"]):
        p = [x.strip() for x in ln.split("|")]
        if len(p) < 2:
            errors.append(f"{u['id']}: escritura mal escrita: {ln}")
            continue
        w = {"type": "write", "es": p[0], "en": p[1]}
        if len(p) > 2 and p[2]:
            w["accept"] = [a.strip() for a in p[2].split(";") if a.strip()]
        if len(p) > 3 and p[3]:
            w["hint"] = p[3]
        final.append(w)
    for ln in lines(u["dictations"]):
        en, es, _ = pair(ln)
        final.append({"type": "dictation", "en": en, "es": es})
    for ln in lines(u["speak"]):
        en, es, _ = pair(ln)
        final.append({"type": "speak", "en": en, "es": es, "note": "Opcional."})
    if items:
        final.append({"type": "auto", "items": [i["id"] for i in items][-8:], "modes": ["listen-pick", "read-pick", "dictation"], "count": 6})
    if final:
        lessons.append({"id": f"{u['id']}-repaso", "title": "Repaso y conversación", "focus": "speaking", "newItems": [], "activities": final})

    return {
        GENERATED_MARK: True,
        "id": u["id"], "level": level, "title": u["title"], "emoji": u["emoji"], "canDo": u["can_do"],
        "summary": u["summary"], "grammar": u["grammar"], "items": items, "lessons": lessons,
    }


# ─── Principal ──────────────────────────────────────────────

def main() -> int:
    ns = {"unit": unit, "D": D, "dialogue": dialogue, "story": story, "roleplay": roleplay, "tip": tip, "reading": reading}
    for f in sorted(SRC.glob("*.py")):
        if f.name.startswith("_"):
            continue
        try:
            exec(compile(f.read_text(encoding="utf-8"), str(f), "exec"), dict(ns))
        except Exception as e:  # noqa: BLE001
            errors.append(f"{f.name}: {e}")

    # Unidades escritas a mano (no generadas): se conservan y sus palabras cuentan como vistas.
    manual: list[dict] = []
    seen: dict[str, str] = {}
    for f in sorted(UNITS_DIR.glob("*.json")):
        data = json.loads(f.read_text(encoding="utf-8"))
        if data.get(GENERATED_MARK):
            continue
        manual.append(data)
        for it in data["items"]:
            seen.setdefault(norm(it["en"]), data["id"])

    # Borra los generados viejos y escribe los nuevos.
    for f in UNITS_DIR.glob("*.json"):
        if json.loads(f.read_text(encoding="utf-8")).get(GENERATED_MARK):
            f.unlink()
    ids = {m["id"] for m in manual}
    compiled = []
    for u in sorted(UNITS, key=lambda x: (LEVEL_IDS.index(x["level"]), x["id"])):
        if u["id"] in ids:
            errors.append(f"Unidad repetida: {u['id']}")
            continue
        ids.add(u["id"])
        cu = compile_unit(u, seen)
        compiled.append(cu)
        (UNITS_DIR / f"{u['id']}.json").write_text(json.dumps(cu, ensure_ascii=False, indent=1), encoding="utf-8")

    all_units = sorted(manual + compiled, key=lambda x: (LEVEL_IDS.index(x["level"]), int(re.match(r"u(\d+)", x["id"]).group(1))))

    # Exámenes: control cada CHECKPOINT_EVERY unidades y final de cada nivel.
    exams = []
    for lv in LEVEL_IDS:
        lus = [u for u in all_units if u["level"] == lv]
        if not lus:
            continue
        block: list[str] = []
        n_check = 0
        for i, u in enumerate(lus):
            block.append(u["id"])
            is_last = i == len(lus) - 1
            if len(block) == CHECKPOINT_EVERY and not is_last and len(lus) - i - 1 >= 2:
                n_check += 1
                exams.append({"id": f"{lv}-control-{n_check}", "level": lv, "kind": "checkpoint",
                              "title": f"Examen de control {lv} · {n_check}", "afterUnit": u["id"],
                              "units": block, "questions": 20, "passPct": 70})
                block = []
        exams.append({"id": f"{lv}-final", "level": lv, "kind": "final", "title": f"Examen final {lv}",
                      "afterUnit": lus[-1]["id"], "units": [u["id"] for u in lus],
                      "questions": 25 if lv == "A0" else 40, "passPct": 75})

    curriculum = {
        "levels": LEVELS,
        "units": [{"id": u["id"], "level": u["level"], "title": u["title"], "emoji": u["emoji"], "canDo": u["canDo"],
                   "grammar": u.get("grammar", []), "status": "ready"} for u in all_units],
        "exams": exams,
    }
    (CONTENT / "curriculum.json").write_text(json.dumps(curriculum, ensure_ascii=False, indent=1), encoding="utf-8")
    (CONTENT / "library.json").write_text(json.dumps(READINGS, ensure_ascii=False, indent=1), encoding="utf-8")

    # Resumen por nivel.
    print("Nivel  Unidades  Palabras  Acumulado")
    acc = 0
    for lv in LEVEL_IDS:
        lus = [u for u in all_units if u["level"] == lv]
        w = sum(len([i for i in u["items"] if i["kind"] != "sound"]) for u in lus)
        acc += w
        print(f"{lv:5}  {len(lus):8}  {w:8}  {acc:9}")
    print(f"Lecciones: {sum(len(u['lessons']) for u in all_units)} · Exámenes: {len(exams)} · Lecturas: {len(READINGS)}")
    if warnings:
        print(f"\n{len(warnings)} avisos (palabras repetidas que se omitieron). Ejemplos:")
        for w in warnings[:15]:
            print("  aviso:", w)
    for e in errors:
        print("  ERROR:", e)
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
