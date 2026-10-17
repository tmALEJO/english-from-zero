#!/usr/bin/env python3
"""
OPCIONAL: genera audio de alta calidad, gratis y offline, con Piper TTS.

Sin este paso la app igual habla: usa la voz del sistema (Chrome/Edge en el PC,
el motor de voz de Android en el celular). Con este paso, todas las frases suenan
con la misma voz natural en cualquier dispositivo, incluso sin voces instaladas.

Uso:
    pip install piper-tts
    python scripts/generate_audio.py              # genera lo que falta
    python scripts/generate_audio.py --voice en_US-amy-medium
    python scripts/generate_audio.py --force      # regenera todo

Resultado: public/audio/*.wav (o .mp3 si tienes ffmpeg) + public/audio/manifest.json.
La app detecta el manifest sola. Vuelve a ejecutarlo cuando agregues contenido.
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


def collect_texts() -> list[str]:
    texts: set[str] = set()
    for f in sorted((CONTENT / "units").glob("*.json")):
        u = json.loads(f.read_text(encoding="utf-8"))
        for it in u["items"]:
            texts.add(it["en"])
            for ex in it.get("examples", []):
                texts.add(ex["en"])
        for l in u["lessons"]:
            for a in l["activities"]:
                t = a["type"]
                if t == "minimal-pair":
                    for p in a["pairs"]:
                        texts.update([p["a"], p["b"]])
                elif t in ("build", "fill", "speak"):
                    texts.add(a["en"].replace("___", a["options"][a["answer"]]) if t == "fill" else a["en"])
                elif t == "dialogue":
                    texts.update(line["en"] for line in a["lines"])
                elif t == "story":
                    texts.update(p["en"] for p in a["paragraphs"])
                elif t == "discover":
                    texts.update(ex["en"].replace("→", ".") for ex in a["examples"])
                    texts.update(ex["en"] for ex in a.get("ruleExamples", []))
    for e in json.loads((CONTENT / "dictionary.json").read_text(encoding="utf-8")):
        texts.add(e["en"])
    return sorted(t for t in texts if t.strip())


def ensure_model(voice: str) -> Path:
    MODELS.mkdir(parents=True, exist_ok=True)
    onnx = MODELS / f"{voice}.onnx"
    if onnx.exists() and (MODELS / f"{voice}.onnx.json").exists():
        return onnx
    lang, name, quality = voice.split("-")
    url = HF.format(lang=lang, name=name, quality=quality, voice=voice)
    print(f"Descargando la voz {voice} (una sola vez, ~60 MB)…")
    for suffix in ("", ".json"):
        urllib.request.urlretrieve(url + suffix + "?download=true", MODELS / f"{voice}.onnx{suffix}")
    return onnx


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--voice", default="en_US-lessac-medium")
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

    texts = collect_texts()
    todo = [t for t in texts if audio_key(t) not in manifest or not (OUT / manifest[audio_key(t)]).exists()]
    print(f"{len(texts)} frases en el contenido, {len(todo)} por generar.")

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
    print(f"\nListo: {len(manifest)} audios en public/audio. Recarga la app.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
