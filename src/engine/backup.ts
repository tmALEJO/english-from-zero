import LZString from 'lz-string';
import type { CardRow, HistoryRow, LessonRow, Settings } from '../types';

/**
 * Copia de seguridad del progreso. El mismo formato funciona en el PC y en el APK:
 * exporta en uno e importa en el otro (por archivo .json o por códigos QR).
 */
export interface Backup {
  app: 'english-from-zero';
  version: 1;
  exportedAt: number;
  device: string;
  cards: CardRow[];
  lessons: LessonRow[];
  history: HistoryRow[];
  settings: Partial<Settings>;
}

export function makeBackup(data: Omit<Backup, 'app' | 'version' | 'exportedAt'>, now = Date.now()): Backup {
  return { app: 'english-from-zero', version: 1, exportedAt: now, ...data };
}

export function parseBackup(raw: unknown): Backup {
  const b = raw as Partial<Backup>;
  if (!b || b.app !== 'english-from-zero') throw new Error('Este archivo no es una copia de English from Zero.');
  if (b.version !== 1) throw new Error(`Versión de copia no soportada (${String(b.version)}). Actualiza la app.`);
  if (!Array.isArray(b.cards) || !Array.isArray(b.lessons)) throw new Error('La copia está incompleta o dañada.');
  return { history: [], settings: {}, device: 'desconocido', exportedAt: 0, ...b } as Backup;
}

export interface MergeResult {
  cards: CardRow[];
  lessons: LessonRow[];
  history: HistoryRow[];
  stats: { cardsAdded: number; cardsUpdated: number; lessonsAdded: number; historyAdded: number };
}

/**
 * Combina sin perder nada: para cada palabra se queda con el repaso más reciente;
 * para cada lección, con lo mejor de ambos lados; el historial se une.
 */
export function mergeBackup(local: { cards: CardRow[]; lessons: LessonRow[]; history: HistoryRow[] }, incoming: Backup): MergeResult {
  const stats = { cardsAdded: 0, cardsUpdated: 0, lessonsAdded: 0, historyAdded: 0 };

  const cards = new Map(local.cards.map((c) => [c.itemId, c]));
  for (const c of incoming.cards) {
    const cur = cards.get(c.itemId);
    if (!cur) { cards.set(c.itemId, c); stats.cardsAdded++; continue; }
    const a = cur.last_review ?? 0, b = c.last_review ?? 0;
    if (b > a || (b === a && c.reps > cur.reps)) { cards.set(c.itemId, c); stats.cardsUpdated++; }
  }

  const lessons = new Map(local.lessons.map((l) => [l.lessonId, l]));
  for (const l of incoming.lessons) {
    const cur = lessons.get(l.lessonId);
    if (!cur) { lessons.set(l.lessonId, l); stats.lessonsAdded++; continue; }
    lessons.set(l.lessonId, {
      ...cur,
      firstCompletedAt: Math.min(cur.firstCompletedAt, l.firstCompletedAt),
      lastCompletedAt: Math.max(cur.lastCompletedAt, l.lastCompletedAt),
      timesCompleted: Math.max(cur.timesCompleted, l.timesCompleted),
      bestScore: Math.max(cur.bestScore, l.bestScore),
    });
  }

  const history = new Map(local.history.map((h) => [h.id, h]));
  for (const h of incoming.history) if (!history.has(h.id)) { history.set(h.id, h); stats.historyAdded++; }

  return { cards: [...cards.values()], lessons: [...lessons.values()], history: [...history.values()], stats };
}

// ─── QR: formato compacto, comprimido y dividido en partes ───

const QR_PREFIX = 'EFZ1';
const CHUNK = 800;

const r2 = (n: number) => Math.round(n * 100) / 100;
const min = (ms: number | null) => (ms ? Math.round(ms / 60000) : 0);

function compact(b: Backup) {
  return {
    t: min(b.exportedAt),
    d: b.device,
    c: b.cards.map((c) => [c.itemId, c.unitId, min(c.due), r2(c.stability), r2(c.difficulty), c.elapsed_days, c.scheduled_days, c.learning_steps, c.reps, c.lapses, c.state, min(c.last_review), c.lastMode ?? '']),
    l: b.lessons.map((l) => [l.lessonId, l.unitId, min(l.firstCompletedAt), min(l.lastCompletedAt), l.timesCompleted, l.bestScore]),
    // El QR lleva solo las últimas 30 sesiones del historial para no hacerse enorme.
    h: [...b.history].sort((a, z) => z.at - a.at).slice(0, 30).map((h) => [h.id, min(h.at), h.type, h.refId, h.title, h.correct, h.total, h.durationSec, h.newItems]),
    s: b.settings,
  };
}

function expandCompact(o: ReturnType<typeof compact>): Backup {
  const ms = (m: number) => m * 60000;
  return {
    app: 'english-from-zero',
    version: 1,
    exportedAt: ms(o.t),
    device: o.d,
    cards: o.c.map((a) => ({
      itemId: a[0] as string, unitId: a[1] as string, due: ms(a[2] as number), stability: a[3] as number,
      difficulty: a[4] as number, elapsed_days: a[5] as number, scheduled_days: a[6] as number,
      learning_steps: a[7] as number, reps: a[8] as number, lapses: a[9] as number, state: a[10] as number,
      last_review: (a[11] as number) ? ms(a[11] as number) : null, lastMode: (a[12] || undefined) as CardRow['lastMode'],
    })),
    lessons: o.l.map((a) => ({
      lessonId: a[0] as string, unitId: a[1] as string, firstCompletedAt: ms(a[2] as number),
      lastCompletedAt: ms(a[3] as number), timesCompleted: a[4] as number, bestScore: a[5] as number,
    })),
    history: o.h.map((a) => ({
      id: a[0] as string, at: ms(a[1] as number), type: a[2] as HistoryRow['type'], refId: a[3] as string,
      title: a[4] as string, correct: a[5] as number, total: a[6] as number, durationSec: a[7] as number, newItems: a[8] as number,
    })),
    settings: o.s,
  };
}

/** Devuelve los textos de cada código QR ("EFZ1:<id>:<i>/<n>:<datos>"). */
export function toQrChunks(b: Backup): string[] {
  const data = LZString.compressToEncodedURIComponent(JSON.stringify(compact(b)));
  const id = Math.random().toString(36).slice(2, 6);
  const n = Math.max(1, Math.ceil(data.length / CHUNK));
  return Array.from({ length: n }, (_, i) => `${QR_PREFIX}:${id}:${i + 1}/${n}:${data.slice(i * CHUNK, (i + 1) * CHUNK)}`);
}

export interface QrPart { id: string; index: number; total: number; data: string }

export function parseQrPart(text: string): QrPart | null {
  const m = /^EFZ1:([a-z0-9]+):(\d+)\/(\d+):(.*)$/s.exec(text.trim());
  if (!m) return null;
  return { id: m[1], index: Number(m[2]), total: Number(m[3]), data: m[4] };
}

/** Une las partes escaneadas (en cualquier orden) y reconstruye la copia. */
export function fromQrParts(parts: QrPart[]): Backup {
  const total = parts[0]?.total ?? 0;
  const sorted = [...parts].sort((a, b) => a.index - b.index);
  if (sorted.length !== total) throw new Error(`Faltan códigos: tienes ${sorted.length} de ${total}.`);
  const json = LZString.decompressFromEncodedURIComponent(sorted.map((p) => p.data).join(''));
  if (!json) throw new Error('No se pudo leer el código QR. Vuelve a escanearlo.');
  return parseBackup(expandCompact(JSON.parse(json)));
}
