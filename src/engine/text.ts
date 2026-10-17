/** Utilidades de texto puras (sin dependencias de UI), probadas en tests/. */

export function normalize(s: string): string {
  return s
    .toLowerCase()
    .normalize('NFD')
    .replace(/[̀-ͯ]/g, '')
    .replace(/[’']/g, "'")
    .replace(/[^a-z0-9' ]+/g, ' ')
    .replace(/\s+/g, ' ')
    .trim();
}

/** Expande contracciones para que "I'm" y "I am" cuenten igual al hablar. */
const CONTRACTIONS: Record<string, string> = {
  "i'm": 'i am', "you're": 'you are', "he's": 'he is', "she's": 'she is', "it's": 'it is',
  "we're": 'we are', "they're": 'they are', "isn't": 'is not', "aren't": 'are not',
  "don't": 'do not', "doesn't": 'does not', "can't": 'can not', "cannot": 'can not',
  "i'd": 'i would', "what's": 'what is', "that's": 'that is', "let's": 'let us',
};

export function expand(s: string): string {
  return normalize(s)
    .split(' ')
    .map((w) => CONTRACTIONS[w] ?? w)
    .join(' ');
}

export function tokenize(s: string): string[] {
  return normalize(s).split(' ').filter(Boolean);
}

export function levenshtein(a: string, b: string): number {
  if (a === b) return 0;
  const m = a.length, n = b.length;
  if (!m) return n;
  if (!n) return m;
  let prev = Array.from({ length: n + 1 }, (_, j) => j);
  for (let i = 1; i <= m; i++) {
    const cur = [i];
    for (let j = 1; j <= n; j++) {
      cur[j] = Math.min(prev[j] + 1, cur[j - 1] + 1, prev[j - 1] + (a[i - 1] === b[j - 1] ? 0 : 1));
    }
    prev = cur;
  }
  return prev[n];
}

export interface SpeechCheck {
  score: number; // 0..1
  ok: boolean;
  heard: string;
  /** Palabras del objetivo que no se reconocieron. */
  missing: string[];
}

/**
 * Compara lo que el reconocedor de voz transcribió con la frase objetivo.
 * Mide INTELIGIBILIDAD (¿te entendieron?), no acento. Tolera pequeñas diferencias por palabra.
 */
export function checkSpeech(target: string, candidates: string[]): SpeechCheck {
  const t = expand(target).split(' ').filter(Boolean);
  let best: SpeechCheck = { score: 0, ok: false, heard: candidates[0] ?? '', missing: t };
  for (const cand of candidates) {
    const h = expand(cand).split(' ').filter(Boolean);
    const used = new Set<number>();
    const missing: string[] = [];
    let hits = 0;
    for (const w of t) {
      let found = -1;
      for (let j = 0; j < h.length; j++) {
        if (used.has(j)) continue;
        const tol = w.length <= 3 ? 0 : w.length <= 6 ? 1 : 2;
        if (levenshtein(w, h[j]) <= tol) { found = j; break; }
      }
      if (found >= 0) { used.add(found); hits++; } else missing.push(w);
    }
    const extra = Math.max(0, h.length - used.size);
    const score = t.length ? Math.max(0, (hits - extra * 0.25) / t.length) : 0;
    if (score > best.score) best = { score, ok: score >= 0.75, heard: cand, missing };
  }
  return best;
}

/** Compara una frase armada con fichas contra la correcta (ignora mayúsculas y puntuación). */
export function sameSentence(a: string, b: string): boolean {
  return expand(a) === expand(b);
}

export function shuffle<T>(arr: T[], rand: () => number = Math.random): T[] {
  const a = [...arr];
  for (let i = a.length - 1; i > 0; i--) {
    const j = Math.floor(rand() * (i + 1));
    [a[i], a[j]] = [a[j], a[i]];
  }
  return a;
}

export function sample<T>(arr: T[], n: number, rand: () => number = Math.random): T[] {
  return shuffle(arr, rand).slice(0, n);
}

/** Divide una frase en fichas para el ejercicio de ordenar. Conserva la puntuación final aparte. */
export function sentenceTiles(en: string): string[] {
  return en
    .replace(/[.!?]+$/, '')
    .split(/\s+/)
    .filter(Boolean);
}

export function uid(): string {
  return Date.now().toString(36) + Math.random().toString(36).slice(2, 8);
}
