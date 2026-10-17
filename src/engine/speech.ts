import { Capacitor } from '@capacitor/core';
import { TextToSpeech } from '@capacitor-community/text-to-speech';
import { SpeechRecognition } from '@capacitor-community/speech-recognition';

/**
 * Voz gratuita, sin APIs de pago:
 *  1. Si existe un MP3 generado con Piper (scripts/generate_audio.py) se usa ese.
 *  2. Si no, la voz del sistema: speechSynthesis en el PC, TTS nativo de Android en el APK.
 */
export const isNative = Capacitor.isNativePlatform();

let manifest: Record<string, string> | null = null;
let manifestLoaded = false;

async function loadManifest() {
  if (manifestLoaded) return manifest;
  manifestLoaded = true;
  try {
    const r = await fetch('./audio/manifest.json');
    if (r.ok) manifest = await r.json();
  } catch {
    manifest = null;
  }
  return manifest;
}

export function audioKey(text: string): string {
  return text.trim().toLowerCase().replace(/\s+/g, ' ');
}

let current: HTMLAudioElement | null = null;

export async function listVoices(): Promise<{ name: string; lang: string }[]> {
  if (isNative) {
    const { voices } = await TextToSpeech.getSupportedVoices();
    return voices.filter((v) => v.lang.startsWith('en')).map((v) => ({ name: v.name, lang: v.lang }));
  }
  if (!('speechSynthesis' in window)) return [];
  const get = () => speechSynthesis.getVoices().filter((v) => v.lang.startsWith('en'));
  if (get().length) return get().map((v) => ({ name: v.name, lang: v.lang }));
  await new Promise((r) => { speechSynthesis.onvoiceschanged = () => r(null); setTimeout(r, 1200); });
  return get().map((v) => ({ name: v.name, lang: v.lang }));
}

/** Configuración global de voz (la fija el estado de la app cuando cambian los Ajustes). */
const voiceConfig = { multiVoice: true, naturalSpeed: false };
export function setVoiceConfig(c: Partial<typeof voiceConfig>) { Object.assign(voiceConfig, c); }

function hash(s: string): number {
  let h = 0;
  for (const ch of s.toLowerCase()) h = (h * 31 + ch.charCodeAt(0)) >>> 0;
  return h;
}

/** Elige una voz distinta para cada personaje, variando acentos (EE. UU., Reino Unido, Australia…). */
function pickWebVoice(voices: SpeechSynthesisVoice[], opts: SpeakOpts): SpeechSynthesisVoice | undefined {
  const en = voices.filter((v) => v.lang.startsWith('en'));
  const chosen = en.find((v) => v.name === opts.voiceName);
  const fallback = chosen ?? en.find((v) => v.lang === 'en-US') ?? en[0];
  if (!opts.speaker || !voiceConfig.multiVoice || opts.speaker === 'Tú') return fallback;
  const others = en.filter((v) => v !== fallback);
  if (!others.length) return fallback;
  return others[hash(opts.speaker) % others.length];
}

export interface SpeakOpts {
  rate?: number;
  voiceName?: string;
  /** Nombre del personaje: cada uno suena con una voz distinta. */
  speaker?: string;
  /** Audio a velocidad natural (escucha real), si está activado en Ajustes. */
  natural?: boolean;
}

let nativeVoices: { name: string; lang: string; index: number }[] | null = null;

export async function speak(text: string, opts: SpeakOpts = {}): Promise<void> {
  const rate = opts.natural && voiceConfig.naturalSpeed ? 1.0 : opts.rate ?? 0.85;
  stopSpeaking();
  const m = await loadManifest();
  const key = audioKey(text);
  const file = (opts.speaker && voiceConfig.multiVoice ? m?.[`${opts.speaker.toLowerCase()}|${key}`] : undefined) ?? m?.[key];
  if (file) {
    current = new Audio(`./audio/${file}`);
    current.playbackRate = Math.max(0.5, Math.min(1.3, rate / 0.9));
    await new Promise<void>((resolve) => {
      if (!current) return resolve();
      current.onended = () => resolve();
      current.onerror = () => resolve();
      current.play().catch(() => resolve());
    });
    return;
  }
  if (isNative) {
    let voice: number | undefined;
    if (opts.speaker && voiceConfig.multiVoice && opts.speaker !== 'Tú') {
      if (!nativeVoices) {
        const { voices } = await TextToSpeech.getSupportedVoices().catch(() => ({ voices: [] as { name: string; lang: string }[] }));
        nativeVoices = voices.map((v, index) => ({ name: v.name, lang: v.lang, index })).filter((v) => v.lang.startsWith('en'));
      }
      if (nativeVoices.length > 1) voice = nativeVoices[hash(opts.speaker) % nativeVoices.length].index;
    }
    await TextToSpeech.speak({ text, lang: 'en-US', rate, pitch: 1, volume: 1, category: 'playback', voice }).catch(() => undefined);
    return;
  }
  if (!('speechSynthesis' in window)) return;
  const u = new SpeechSynthesisUtterance(text);
  const voice = pickWebVoice(speechSynthesis.getVoices(), opts);
  u.lang = voice?.lang ?? 'en-US';
  u.rate = rate;
  if (voice) u.voice = voice;
  await new Promise<void>((resolve) => {
    u.onend = () => resolve();
    u.onerror = () => resolve();
    speechSynthesis.speak(u);
  });
}

export function stopSpeaking() {
  current?.pause();
  current = null;
  if (isNative) TextToSpeech.stop().catch(() => undefined);
  else if ('speechSynthesis' in window) speechSynthesis.cancel();
}

// ─── Reconocimiento de voz ──────────────────────────────────

type WebSR = {
  lang: string; interimResults: boolean; maxAlternatives: number; continuous: boolean;
  onresult: ((e: { results: ArrayLike<ArrayLike<{ transcript: string }>> }) => void) | null;
  onerror: ((e: { error: string }) => void) | null;
  onend: (() => void) | null;
  start(): void; stop(): void;
};

function webSRClass(): (new () => WebSR) | null {
  const w = window as unknown as { SpeechRecognition?: new () => WebSR; webkitSpeechRecognition?: new () => WebSR };
  return w.SpeechRecognition ?? w.webkitSpeechRecognition ?? null;
}

export async function canListen(): Promise<boolean> {
  if (isNative) {
    try { return (await SpeechRecognition.available()).available; } catch { return false; }
  }
  return Boolean(webSRClass());
}

/** Escucha una frase y devuelve las transcripciones candidatas. */
export async function listen(): Promise<string[]> {
  if (isNative) {
    const perm = await SpeechRecognition.checkPermissions();
    if (perm.speechRecognition !== 'granted') {
      const req = await SpeechRecognition.requestPermissions();
      if (req.speechRecognition !== 'granted') throw new Error('Necesito permiso de micrófono para escucharte.');
    }
    const res = await SpeechRecognition.start({ language: 'en-US', maxResults: 5, partialResults: false, popup: false });
    return res.matches ?? [];
  }
  const SR = webSRClass();
  if (!SR) throw new Error('Este navegador no reconoce voz. Usa Google Chrome o Microsoft Edge.');
  return new Promise((resolve, reject) => {
    const sr = new SR();
    sr.lang = 'en-US';
    sr.interimResults = false;
    sr.maxAlternatives = 5;
    sr.continuous = false;
    let done = false;
    sr.onresult = (e) => {
      done = true;
      const alts = e.results[0];
      resolve(Array.from({ length: alts.length }, (_, i) => alts[i].transcript));
    };
    sr.onerror = (e) => {
      done = true;
      const msg: Record<string, string> = {
        'not-allowed': 'El navegador bloqueó el micrófono. Permítelo en el candado de la barra de direcciones.',
        'no-speech': 'No escuché nada. Acércate al micrófono e inténtalo de nuevo.',
        network: 'El reconocimiento de voz de Chrome necesita internet en el PC.',
      };
      reject(new Error(msg[e.error] ?? `No se pudo escuchar (${e.error}).`));
    };
    sr.onend = () => { if (!done) resolve([]); };
    sr.start();
    setTimeout(() => { try { sr.stop(); } catch { /* ya terminó */ } }, 7000);
  });
}

export async function stopListening() {
  if (isNative) await SpeechRecognition.stop().catch(() => undefined);
}
