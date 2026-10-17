import type { AutoMode, HistoryRow, Lesson, Unit } from '../types';
import { db, getSettings, saveSettings, type AppDB } from './db';
import { newCard, review, type Outcome } from '../engine/srs';
import { makeBackup, mergeBackup, type Backup, type MergeResult } from '../engine/backup';
import { uid } from '../engine/text';
import { isNative } from '../engine/speech';

export interface ItemResult { itemId: string; outcome: Outcome; mode?: AutoMode }

export interface SessionSummary {
  type: HistoryRow['type'];
  refId: string;
  title: string;
  correct: number;
  total: number;
  startedAt: number;
  results: ItemResult[];
}

/** Guarda una lección terminada: progreso, tarjetas nuevas para repaso e historial. */
export async function completeLesson(unit: Unit, lesson: Lesson, s: SessionSummary, d: AppDB = db) {
  const now = Date.now();
  const score = s.total ? Math.round((s.correct / s.total) * 100) : 100;
  await d.transaction('rw', d.lessons, d.cards, d.history, async () => {
    const prev = await d.lessons.get(lesson.id);
    await d.lessons.put({
      lessonId: lesson.id,
      unitId: unit.id,
      firstCompletedAt: prev?.firstCompletedAt ?? now,
      lastCompletedAt: now,
      timesCompleted: (prev?.timesCompleted ?? 0) + 1,
      bestScore: Math.max(prev?.bestScore ?? 0, score),
    });
    // Las palabras nuevas entran al sistema de repaso; su primer repaso depende de cómo te fue hoy.
    for (const itemId of lesson.newItems) {
      if (await d.cards.get(itemId)) continue;
      const outcomes = s.results.filter((r) => r.itemId === itemId).map((r) => r.outcome);
      const worst: Outcome = outcomes.includes('again') ? 'again' : outcomes.includes('hard') ? 'hard' : 'good';
      await d.cards.put(review(newCard(itemId, unit.id), worst));
    }
    // Los ítems viejos que aparecieron en el calentamiento cuentan como repaso.
    await applyResults(s.results.filter((r) => !lesson.newItems.includes(r.itemId)), d, true);
    await addHistory({ ...s, newItems: lesson.newItems.length }, d);
  });
}

async function applyResults(results: ItemResult[], d: AppDB, onlyDue: boolean) {
  const now = Date.now();
  const seen = new Set<string>();
  for (const r of results) {
    if (seen.has(r.itemId)) continue;
    seen.add(r.itemId);
    const card = await d.cards.get(r.itemId);
    if (!card) continue;
    if (onlyDue && card.due > now) continue;
    await d.cards.put(review(card, r.outcome, r.mode));
  }
}

/** Repaso espaciado: cada resultado reprograma la tarjeta. */
export async function completeReview(s: SessionSummary, d: AppDB = db) {
  await d.transaction('rw', d.cards, d.history, async () => {
    await applyResults(s.results, d, false);
    await addHistory({ ...s, newItems: 0 }, d);
  });
}

/** Práctica libre: solo cuenta las tarjetas que ya tocaba repasar; el resto queda igual. */
export async function completePractice(s: SessionSummary, d: AppDB = db) {
  await d.transaction('rw', d.cards, d.history, async () => {
    await applyResults(s.results, d, true);
    await addHistory({ ...s, newItems: 0 }, d);
  });
}

async function addHistory(s: SessionSummary & { newItems: number }, d: AppDB) {
  await d.history.put({
    id: uid(),
    at: Date.now(),
    type: s.type,
    refId: s.refId,
    title: s.title,
    correct: s.correct,
    total: s.total,
    durationSec: Math.round((Date.now() - s.startedAt) / 1000),
    newItems: s.newItems,
  });
}

/** Guarda una prueba de unidad o un examen (se guarda la mejor nota; se pueden repetir). */
export async function completeAssessment(rowId: string, groupId: string, s: SessionSummary, d: AppDB = db): Promise<number> {
  const now = Date.now();
  const score = s.total ? Math.round((s.correct / s.total) * 100) : 0;
  await d.transaction('rw', d.lessons, d.cards, d.history, async () => {
    const prev = await d.lessons.get(rowId);
    await d.lessons.put({
      lessonId: rowId,
      unitId: groupId,
      firstCompletedAt: prev?.firstCompletedAt ?? now,
      lastCompletedAt: now,
      timesCompleted: (prev?.timesCompleted ?? 0) + 1,
      bestScore: Math.max(prev?.bestScore ?? 0, score),
    });
    await applyResults(s.results, d, true);
    await addHistory({ ...s, newItems: 0 }, d);
  });
  return score;
}

// ─── Exportar / importar ────────────────────────────────────

export async function exportBackup(d: AppDB = db): Promise<Backup> {
  const [cards, lessons, history, settings] = await Promise.all([d.cards.toArray(), d.lessons.toArray(), d.history.toArray(), getSettings(d)]);
  return makeBackup({ cards, lessons, history, settings, device: isNative ? 'Android' : 'PC (navegador)' });
}

export async function importBackup(b: Backup, mode: 'merge' | 'replace', d: AppDB = db): Promise<MergeResult['stats']> {
  const local =
    mode === 'merge'
      ? { cards: await d.cards.toArray(), lessons: await d.lessons.toArray(), history: await d.history.toArray() }
      : { cards: [], lessons: [], history: [] };
  const merged = mergeBackup(local, b);
  await d.transaction('rw', d.cards, d.lessons, d.history, d.kv, async () => {
    await Promise.all([d.cards.clear(), d.lessons.clear(), d.history.clear()]);
    await d.cards.bulkPut(merged.cards);
    await d.lessons.bulkPut(merged.lessons);
    await d.history.bulkPut(merged.history);
    if (mode === 'replace') await saveSettings(b.settings, d);
  });
  return merged.stats;
}

export async function resetAll(d: AppDB = db) {
  await d.transaction('rw', d.cards, d.lessons, d.history, d.kv, async () => {
    await Promise.all([d.cards.clear(), d.lessons.clear(), d.history.clear(), d.kv.clear()]);
  });
}
