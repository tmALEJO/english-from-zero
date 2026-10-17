#!/usr/bin/env python3
"""
OPCIONAL: genera audio de alta calidad, gratis y offline, con Piper TTS.

Sin este paso la app igual habla: usa la voz del sistema (Chrome/Edge en el PC,
el motor de voz de Android en el celular). Con este paso, todas las frases suenan
con la misma voz natural en cualquier dispositivo, incluso sin voces instaladas.

Uso:
    pip install piper-tts
    python scripts/generate_audio.py                 # TODO el contenido (recomendado)
    python scripts/generate_audio.py --scope items   # solo palabras y frases (audio más liviano)
    python scripts/generate_audio.py --voice en_US-amy-medium
    python scripts/generate_audio.py --force         # regenera todo

Resultado: public/audio/*.mp3 (o .wav si no tienes ffmpeg) + public/audio/manifest.json.
La app detecta el manifest sola. Vuelve a ejecutarlo cuando agregues contenido.

Tamaño: con --scope all el audio puede pesar ~80-150 MB y suma eso al APK.
Con --scope items queda mucho más liviano (~20-40 MB) y cubre todas las palabras
del vocabulario; las historias y diálogos usarían la voz del sistema.
Instala ffmpeg para que guarde MP3 (mucho más livianos que WAV).

Si NO quieres el audio dentro del APK (que el celular use su voz del sistema),
agrega  public/audio/  a .gitignore antes de hacer commit.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import shutil
import subprocess
import sys
import urllib.request
import wave
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CONTENT = ROOT / "content"
OUT = ROOT / "public" / "audio"
MODELS = ROOT / "scripts" / ".piper"
HF = "https://huggingface.co/rhasspy/piper-voices/resolve/main/en/{lang}/{name}/{quality}/{voice}.onnx"


def audio_key(text: str) -> str:
    """Debe coincidir con audioKey() de src/engine/speech.ts."""
    return re.sub(r"\s+", " ", text.strip().lower())


def collect_texts(scope: str = "all") -> list[str]:
    """scope='items' = solo vocabulario (liviano); 'all' = también historias, diálogos, etc."""
    texts: set[str] = set()
    for f in sorted((CONTENT / "units").glob("*.json")):
        u = json.loads(f.read_text(encoding="utf-8"))
        for it in u["items"]:
            texts.add(it["en"])
            for ex in it.get("examples", []):
                texts.add(ex["en"])
        if scope == "items":
            continue
        for l in u["lessons"]:
            for a in l["activities"]:
                t = a["type"]
                if t == "minimal-pair":
                    for p in a["pairs"]:
                        texts.update([p["a"], p["b"]])
                elif t in ("build", "speak", "dictation", "write"):
                    texts.add(a["en"])
                elif t == "fill":
                    texts.add(a["en"].replace("___", a["options"][a["answer"]]))
                elif t == "dialogue":
                    texts.update(line["en"] for line in a["lines"])
                elif t == "roleplay":
                    for turn in a["turns"]:
                        if "en" in turn:
                            texts.add(turn["en"])
                        for op in turn.get("options", []):
                            texts.add(op["en"])
                elif t == "story":
                    texts.update(p["en"] for p in a["paragraphs"])
                elif t == "discover":
                    texts.update(ex["en"].replace("→", ".") for ex in a["examples"])
                    texts.update(ex["en"] for ex in a.get("ruleExamples", []))
    for e in json.loads((CONTENT / "dictionary.json").read_text(encoding="utf-8")):
        texts.add(e["en"])
    # Biblioteca (historias, diálogos y artículos para leer y escuchar)
    lib = CONTENT / "library.json"
    if scope != "items" and lib.exists():
        for r in json.loads(lib.read_text(encoding="utf-8")):
            texts.update(s["en"] for s in r.get("sentences", []))
    return sorted(t for t in texts if t.strip())


def ensure_model(voice: str) -> Path:
    MODELS.mkdir(parents=True, exist_ok=True)
    onnx = MODELS / f"{voice}.onnx"
    if onnx.exists() and (MODELS / f"{voice}.onnx.json").exists():
        return onnx
    lang, name, quality = voice.split("-")
    url = HF.format(lang=lang, name=name, quality=quality, voice=voice)
    print(f"Descargando la voz {voice} (una sola vez, ~60 MB)… Necesita internet.")
    for suffix in ("", ".json"):
        req = urllib.request.Request(url + suffix + "?download=true", headers={"User-Agent": "english-from-zero"})
        try:
            with urllib.request.urlopen(req) as r, open(MODELS / f"{voice}.onnx{suffix}", "wb") as out:
                shutil.copyfileobj(r, out)
        except Exception as e:  # noqa: BLE001
            sys.exit(f"No pude descargar la voz ({e}). Revisa tu internet o prueba otra con --voice (p. ej. en_US-amy-medium).")
    return onnx


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--voice", default="en_US-lessac-medium")
    ap.add_argument("--scope", choices=["all", "items"], default="all")
    ap.add_argument("--force", action="store_true")
    args = ap.parse_args()

    try:
        from piper import PiperVoice  # type: ignore
    except ImportError:
        print("Falta Piper. Instálalo con:  pip install piper-tts")
        return 1

    voice = PiperVoice.load(str(ensure_model(args.voice)))
    ffmpeg = shutil.which("ffmpeg")
    OUT.mkdir(parents=True, exist_ok=True)
    manifest_path = OUT / "manifest.json"
    manifest: dict[str, str] = {} if args.force or not manifest_path.exists() else json.loads(manifest_path.read_text())

    texts = collect_texts(args.scope)
    if not ffmpeg:
        print("Aviso: no encontré ffmpeg, guardaré WAV (pesan mucho más). Instala ffmpeg para MP3.")
    todo = [t for t in texts if audio_key(t) not in manifest or not (OUT / manifest[audio_key(t)]).exists()]
    print(f"Alcance '{args.scope}': {len(texts)} frases, {len(todo)} por generar.")

    for i, text in enumerate(todo, 1):
        h = hashlib.sha1(audio_key(text).encode()).hexdigest()[:12]
        wav_path = OUT / f"{h}.wav"
        with wave.open(str(wav_path), "wb") as w:
            if hasattr(voice, "synthesize_wav"):
                voice.synthesize_wav(text, w)  # piper-tts >= 1.3
            else:
                voice.synthesize(text, w)  # versiones anteriores
        name = wav_path.name
        if ffmpeg:
            mp3 = OUT / f"{h}.mp3"
            subprocess.run([ffmpeg, "-y", "-loglevel", "error", "-i", str(wav_path), "-b:a", "64k", str(mp3)], check=True)
            wav_path.unlink()
            name = mp3.name
        manifest[audio_key(text)] = name
        print(f"  [{i}/{len(todo)}] {text}")

    manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=1), encoding="utf-8")
    total_mb = sum(f.stat().st_size for f in OUT.glob("*") if f.suffix in (".mp3", ".wav")) / 1_048_576
    print(f"\nListo: {len(manifest)} audios en public/audio ({total_mb:.0f} MB). Recarga la app.")
    if total_mb > 60:
        print("Es bastante peso para el APK. Si prefieres, usa --scope items o agrega public/audio/ a .gitignore.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
