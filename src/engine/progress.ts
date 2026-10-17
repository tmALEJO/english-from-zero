import type { CardRow, CurriculumUnitRef, LessonRow, LevelId, Step } from '../types';
import { LEVEL_ORDER, curriculum, getItem, route, units } from './content';
import { autoStep } from './steps';
import { isDue, nextMode } from './srs';
import { shuffle } from './text';

export type UnitStatus = 'done' | 'in-progress' | 'available' | 'locked' | 'planned';

export function lessonsDone(unitId: string, lessons: LessonRow[]): number {
  const u = units[unitId];
  if (!u) return 0;
  const set = new Set(lessons.map((l) => l.lessonId));
  return u.lessons.filter((l) => set.has(l.id)).length;
}

export function isUnitDone(unitId: string, lessons: LessonRow[]): boolean {
  const u = units[unitId];
  return Boolean(u) && lessonsDone(unitId, lessons) === u.lessons.length;
}

/**
 * Ruta guiada: una unidad se desbloquea cuando terminas la anterior.
 * Las unidades terminadas siempre se pueden repetir. El "modo explorador" desbloquea todo.
 */
export function unitStatuses(lessons: LessonRow[], explorer = false): Record<string, UnitStatus> {
  const out: Record<string, UnitStatus> = {};
  let prevDone = true;
  for (const ref of route) {
    if (ref.status === 'planned' || !units[ref.id]) { out[ref.id] = 'planned'; continue; }
    const done = isUnitDone(ref.id, lessons);
    const started = lessonsDone(ref.id, lessons) > 0;
    out[ref.id] = done ? 'done' : started ? 'in-progress' : prevDone || explorer ? 'available' : 'locked';
    prevDone = done;
  }
  return out;
}

/** Próxima lección sugerida: la primera no hecha de la primera unidad no terminada. */
export function nextLesson(lessons: LessonRow[], explorer = false) {
  const st = unitStatuses(lessons, explorer);
  const done = new Set(lessons.map((l) => l.lessonId));
  for (const ref of route) {
    const s = st[ref.id];
    if (s === 'in-progress' || s === 'available') {
      const u = units[ref.id];
      const l = u.lessons.find((x) => !done.has(x.id));
      if (l) return { unit: u, lesson: l };
    }
  }
  return null;
}

export interface LevelProgress {
  id: LevelId;
  name: string;
  description: string;
  ready: number;
  planned: number;
  done: number;
  canDo: { unitId: string; text: string; done: boolean; planned: boolean }[];
}

export function levelProgress(lessons: LessonRow[]): LevelProgress[] {
  return curriculum.levels.map((lv) => {
    const refs = route.filter((r) => r.level === lv.id);
    const ready = refs.filter((r) => r.status === 'ready' && units[r.id]);
    return {
      ...lv,
      ready: ready.length,
      planned: refs.length - ready.length,
      done: ready.filter((r) => isUnitDone(r.id, lessons)).length,
      canDo: refs.map((r) => ({ unitId: r.id, text: r.canDo, done: isUnitDone(r.id, lessons), planned: r.status !== 'ready' })),
    };
  });
}

/**
 * Nivel actual: el último nivel cuyas unidades del currículo están todas terminadas.
 * Mientras no completes A0 completo, estás "en camino a A0".
 */
export function currentLevel(lessons: LessonRow[]): { reached: LevelId | null; working: LevelId } {
  let reached: LevelId | null = null;
  for (const lv of LEVEL_ORDER) {
    const refs = route.filter((r) => r.level === lv);
    if (!refs.length) continue;
    const allDone = refs.every((r) => r.status === 'ready' && isUnitDone(r.id, lessons));
    if (allDone) reached = lv;
    else return { reached, working: lv };
  }
  return { reached, working: reached ?? 'A0' };
}

export function unitRef(id: string): CurriculumUnitRef | undefined {
  return route.find((r) => r.id === id);
}

// ─── Sesiones de repaso y práctica ──────────────────────────

export interface PlannedStep { step: Step; itemId?: string; mode?: string }

/** Repaso del día: tarjetas vencidas, cada una en un modo distinto al anterior. */
export function buildReview(cards: CardRow[], size: number, rand: () => number = Math.random): PlannedStep[] {
  const due = cards.filter((c) => isDue(c)).sort((a, b) => a.due - b.due).slice(0, size);
  return shuffle(due, rand).map((c) => {
    const item = getItem(c.itemId);
    const mode = nextMode(c, rand);
    const pool = units[item.unitId]?.items ?? [];
    return { step: autoStep(item, mode, pool, rand), itemId: c.itemId, mode };
  });
}

/** Calentamiento al inicio de una lección: reciclaje de unidades anteriores. */
export function buildWarmup(cards: CardRow[], excludeUnit: string, size: number, rand: () => number = Math.random): PlannedStep[] {
  if (size <= 0) return [];
  const pool = cards.filter((c) => c.unitId !== excludeUnit);
  const due = pool.filter((c) => isDue(c));
  const chosen = (due.length >= size ? due : [...due, ...shuffle(pool.filter((c) => !isDue(c)), rand)]).slice(0, size);
  return buildReview(chosen.map((c) => ({ ...c, due: 0 })), size, rand);
}

/** Práctica libre de una lista de ítems (unidad, tema o una sola palabra). No altera el calendario de repaso. */
export function buildPractice(itemIds: string[], rounds = 2, rand: () => number = Math.random): PlannedStep[] {
  const out: PlannedStep[] = [];
  const modes = ['listen-pick', 'picture-pick', 'read-pick', 'build'] as const;
  for (let r = 0; r < rounds; r++) {
    for (const id of shuffle(itemIds, rand)) {
      const item = getItem(id);
      const usable = modes.filter((m) => (m === 'build' ? item.en.split(' ').length >= 2 : item.kind !== 'sound' || m === 'listen-pick'));
      const mode = usable[(r + out.length) % usable.length];
      out.push({ step: autoStep(item, mode, units[item.unitId]?.items ?? [], rand), itemId: id, mode });
    }
  }
  return out;
}

/** Ítems que más te cuestan (para "Mis difíciles"). */
export function hardItems(cards: CardRow[]): string[] {
  return cards
    .filter((c) => c.lapses > 0 || c.difficulty > 6)
    .sort((a, b) => b.lapses - a.lapses || b.difficulty - a.difficulty)
    .map((c) => c.itemId);
}
