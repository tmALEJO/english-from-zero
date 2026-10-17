import type { Activity, CardRow, CurriculumUnitRef, ExamRef, Item, LessonRow, LevelId, Step, Unit } from '../types';
import { LEVEL_ORDER, curriculum, getItem, route, units } from './content';
import { autoStep, canUseMode } from './steps';
import { isDue, nextMode } from './srs';
import { sample, shuffle } from './text';

export type UnitStatus = 'done' | 'in-progress' | 'available' | 'locked' | 'planned';
export type ExamStatus = 'passed' | 'available' | 'locked';

/** Nota mínima para aprobar la prueba de una unidad. */
export const UNIT_TEST_PASS = 70;

export const testId = (unitId: string) => `${unitId}:test`;
export const examRowId = (examId: string) => `exam:${examId}`;

const rowMap = (lessons: LessonRow[]) => new Map(lessons.map((l) => [l.lessonId, l]));

export function examPassed(exam: ExamRef, lessons: LessonRow[]): boolean {
  const r = lessons.find((l) => l.lessonId === examRowId(exam.id));
  return Boolean(r && r.bestScore >= exam.passPct);
}

/** Un nivel queda certificado si apruebas su examen final o el de un nivel superior (ubicación). */
export function levelCertified(level: LevelId, lessons: LessonRow[]): boolean {
  const idx = LEVEL_ORDER.indexOf(level);
  return curriculum.exams.some((e) => e.kind === 'final' && LEVEL_ORDER.indexOf(e.level) >= idx && examPassed(e, lessons));
}

export function lessonsDone(unitId: string, lessons: LessonRow[]): number {
  const u = units[unitId];
  if (!u) return 0;
  const m = rowMap(lessons);
  return u.lessons.filter((l) => m.has(l.id)).length;
}

export function unitTestPassed(unitId: string, lessons: LessonRow[]): boolean {
  const r = lessons.find((l) => l.lessonId === testId(unitId));
  return Boolean(r && r.bestScore >= UNIT_TEST_PASS);
}

/** Una unidad está terminada cuando hiciste todas sus lecciones y aprobaste su prueba. */
export function isUnitDone(unitId: string, lessons: LessonRow[]): boolean {
  const u = units[unitId];
  if (!u) return false;
  if (levelCertified(u.level, lessons)) return true;
  return lessonsDone(unitId, lessons) === u.lessons.length && unitTestPassed(unitId, lessons);
}

export function allLessonsDone(unitId: string, lessons: LessonRow[]): boolean {
  const u = units[unitId];
  return Boolean(u) && lessonsDone(unitId, lessons) === u.lessons.length;
}

/** La ruta completa: unidades y, entre ellas, los exámenes en el lugar donde toca hacerlos. */
export type RouteEntry = { type: 'unit'; ref: CurriculumUnitRef } | { type: 'exam'; exam: ExamRef };

export const fullRoute: RouteEntry[] = (() => {
  const out: RouteEntry[] = [];
  for (const ref of route) {
    out.push({ type: 'unit', ref });
    for (const exam of curriculum.exams.filter((e) => e.afterUnit === ref.id)) out.push({ type: 'exam', exam });
  }
  return out;
})();

export function examStatus(exam: ExamRef, lessons: LessonRow[]): ExamStatus {
  if (examPassed(exam, lessons) || (exam.kind === 'checkpoint' && levelCertified(exam.level, lessons))) return 'passed';
  const ready = exam.units.every((u) => !units[u] || isUnitDone(u, lessons));
  return ready ? 'available' : 'locked';
}

/**
 * Ruta guiada: una unidad se abre cuando terminas la anterior, y los exámenes de control
 * frenan el avance hasta aprobarlos. Lo terminado siempre se puede repetir.
 * El "modo explorador" desbloquea todo.
 */
export function unitStatuses(lessons: LessonRow[], explorer = false): Record<string, UnitStatus> {
  const out: Record<string, UnitStatus> = {};
  let open = true;
  for (const e of fullRoute) {
    if (e.type === 'exam') {
      if (examStatus(e.exam, lessons) !== 'passed') open = false;
      continue;
    }
    const ref = e.ref;
    if (ref.status === 'planned' || !units[ref.id]) { out[ref.id] = 'planned'; continue; }
    const done = isUnitDone(ref.id, lessons);
    const started = lessonsDone(ref.id, lessons) > 0;
    out[ref.id] = done ? 'done' : started ? 'in-progress' : open || explorer ? 'available' : 'locked';
    open = done;
  }
  return out;
}

export type NextStep =
  | { kind: 'lesson'; unit: Unit; lesson: Unit['lessons'][number] }
  | { kind: 'test'; unit: Unit }
  | { kind: 'exam'; exam: ExamRef };

/** Qué toca ahora: la siguiente lección, la prueba de una unidad o un examen pendiente. */
export function nextStep(lessons: LessonRow[], explorer = false): NextStep | null {
  const st = unitStatuses(lessons, explorer);
  const m = rowMap(lessons);
  for (const e of fullRoute) {
    if (e.type === 'exam') {
      const s = examStatus(e.exam, lessons);
      if (s === 'available') return { kind: 'exam', exam: e.exam };
      if (s === 'locked' && !explorer) return null;
      continue;
    }
    const s = st[e.ref.id];
    if (s === 'in-progress' || s === 'available') {
      const u = units[e.ref.id];
      const l = u.lessons.find((x) => !m.has(x.id));
      if (l) return { kind: 'lesson', unit: u, lesson: l };
      if (!unitTestPassed(u.id, lessons)) return { kind: 'test', unit: u };
    }
  }
  return null;
}

/** Compatibilidad: siguiente lección (sin pruebas ni exámenes). */
export function nextLesson(lessons: LessonRow[], explorer = false) {
  const n = nextStep(lessons, explorer);
  return n?.kind === 'lesson' ? { unit: n.unit, lesson: n.lesson } : null;
}

export interface LevelProgress {
  id: LevelId;
  name: string;
  description: string;
  ready: number;
  planned: number;
  done: number;
  words: number;
  certified: boolean;
  finalExam?: ExamRef;
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
      words: ready.reduce((a, r) => a + units[r.id].items.filter((i) => i.kind !== 'sound').length, 0),
      certified: levelCertified(lv.id, lessons),
      finalExam: curriculum.exams.find((e) => e.level === lv.id && e.kind === 'final'),
      canDo: refs.map((r) => ({ unitId: r.id, text: r.canDo, done: isUnitDone(r.id, lessons), planned: r.status !== 'ready' })),
    };
  });
}

/** Nivel actual: el último certificado con su examen final, y el que estás construyendo. */
export function currentLevel(lessons: LessonRow[]): { reached: LevelId | null; working: LevelId } {
  let reached: LevelId | null = null;
  for (const lv of LEVEL_ORDER) if (levelCertified(lv, lessons)) reached = lv;
  const idx = reached ? LEVEL_ORDER.indexOf(reached) + 1 : 0;
  return { reached, working: LEVEL_ORDER[Math.min(idx, LEVEL_ORDER.length - 1)] };
}

export function unitRef(id: string): CurriculumUnitRef | undefined {
  return route.find((r) => r.id === id);
}

// ─── Sesiones de repaso y práctica ──────────────────────────

export interface PlannedStep { step: Step; itemId?: string; mode?: string }

/** Repaso del día: tarjetas vencidas, cada una en un modo distinto al anterior. */
export function buildReview(cards: CardRow[], size: number, rand: () => number = Math.random): PlannedStep[] {
  const due = cards.filter((c) => isDue(c) && safeItem(c.itemId)).sort((a, b) => a.due - b.due).slice(0, size);
  return shuffle(due, rand).map((c) => {
    const item = getItem(c.itemId);
    const mode = nextMode(c, rand);
    const pool = units[item.unitId]?.items ?? [];
    return { step: autoStep(item, mode, pool, rand), itemId: c.itemId, mode };
  });
}

function safeItem(id: string) {
  try { getItem(id); return true; } catch { return false; }
}

/** Calentamiento al inicio de una lección: reciclaje de unidades anteriores. */
export function buildWarmup(cards: CardRow[], excludeUnit: string, size: number, rand: () => number = Math.random): PlannedStep[] {
  if (size <= 0) return [];
  const pool = cards.filter((c) => c.unitId !== excludeUnit && safeItem(c.itemId));
  const due = pool.filter((c) => isDue(c));
  const chosen = (due.length >= size ? due : [...due, ...shuffle(pool.filter((c) => !isDue(c)), rand)]).slice(0, size);
  return buildReview(chosen.map((c) => ({ ...c, due: 0 })), size, rand);
}

/** Práctica libre de una lista de ítems (unidad, tema o una sola palabra). No altera el calendario de repaso. */
export function buildPractice(itemIds: string[], rounds = 2, rand: () => number = Math.random): PlannedStep[] {
  const out: PlannedStep[] = [];
  const modes = ['listen-pick', 'picture-pick', 'read-pick', 'build', 'dictation'] as const;
  for (let r = 0; r < rounds; r++) {
    for (const id of shuffle(itemIds, rand)) {
      const item = getItem(id);
      const usable = modes.filter((m) => canUseMode(item, m));
      const mode = usable[(r + out.length) % usable.length];
      out.push({ step: autoStep(item, mode, units[item.unitId]?.items ?? [], rand), itemId: id, mode });
    }
  }
  return out;
}

/** Ítems que más te cuestan (para "Mis difíciles"). */
export function hardItems(cards: CardRow[]): string[] {
  return cards
    .filter((c) => (c.lapses > 0 || c.difficulty > 6) && safeItem(c.itemId))
    .sort((a, b) => b.lapses - a.lapses || b.difficulty - a.difficulty)
    .map((c) => c.itemId);
}

// ─── Pruebas de unidad y exámenes ───────────────────────────

type Graded = Extract<Activity, { type: 'fill' } | { type: 'write' } | { type: 'dictation' }>;

function unitActivities(u: Unit) {
  const fills: Extract<Activity, { type: 'fill' }>[] = [];
  const writes: Extract<Activity, { type: 'write' }>[] = [];
  const questions: Step[] = [];
  for (const l of u.lessons) {
    for (const a of l.activities) {
      if (a.type === 'fill') fills.push(a);
      if (a.type === 'write') writes.push(a);
      if (a.type === 'story') for (const q of a.questions ?? []) questions.push({ kind: 'question', ...q, context: a.title });
    }
  }
  return { fills, writes, questions };
}

function gradedToStep(a: Graded): Step {
  if (a.type === 'fill') return { kind: 'fill', en: a.en, es: a.es, options: a.options, answer: a.answer, explain: a.explain };
  if (a.type === 'write') return { kind: 'write', es: a.es, en: a.en, accept: a.accept, hint: a.hint };
  return { kind: 'dictation', en: a.en, es: a.es };
}

function itemQuestion(item: Item, pool: Item[], i: number, rand: () => number): Step {
  const modes = (['listen-pick', 'read-pick', 'picture-pick', 'dictation', 'listen-pick', 'build'] as const).filter((m) => canUseMode(item, m));
  return autoStep(item, modes[i % modes.length], pool, rand);
}

/** Prueba de una unidad: escucha, lectura, dictado, gramática y comprensión de la historia. */
export function buildUnitTest(u: Unit, rand: () => number = Math.random): PlannedStep[] {
  const items = u.items.filter((i) => i.kind !== 'sound' || u.id === 'u00-sonidos');
  const { fills, writes, questions } = unitActivities(u);
  const chosen = sample(items, Math.min(10, items.length), rand);
  const steps: PlannedStep[] = chosen.map((it, i) => ({ step: itemQuestion(it, u.items, i, rand) }));
  for (const f of sample(fills, 3, rand)) steps.push({ step: gradedToStep(f) });
  for (const w of sample(writes, 1, rand)) steps.push({ step: gradedToStep(w) });
  for (const q of sample(questions, 2, rand)) steps.push({ step: q });
  return shuffle(steps, rand);
}

/** Examen de control o final: preguntas repartidas entre todas sus unidades. */
export function buildExam(exam: ExamRef, rand: () => number = Math.random): PlannedStep[] {
  const us = exam.units.map((id) => units[id]).filter(Boolean);
  if (!us.length) return [];
  const pool = us.flatMap((u) => u.items.filter((i) => i.kind !== 'sound'));
  const acts = us.map(unitActivities);
  const fills = acts.flatMap((a) => a.fills);
  const writes = acts.flatMap((a) => a.writes);
  const questions = acts.flatMap((a) => a.questions);
  const n = exam.questions;
  const nFill = Math.min(fills.length, Math.round(n * 0.25));
  const nWrite = Math.min(writes.length, Math.round(n * 0.1));
  const nQ = Math.min(questions.length, Math.round(n * 0.1));
  const nItems = Math.max(0, n - nFill - nWrite - nQ);
  const steps: PlannedStep[] = sample(pool, nItems, rand).map((it, i) => ({ step: itemQuestion(it, units[getItem(it.id).unitId]?.items ?? pool, i, rand) }));
  for (const f of sample(fills, nFill, rand)) steps.push({ step: gradedToStep(f) });
  for (const w of sample(writes, nWrite, rand)) steps.push({ step: gradedToStep(w) });
  for (const q of sample(questions, nQ, rand)) steps.push({ step: q });
  return shuffle(steps, rand);
}

export function findExam(id: string): ExamRef | undefined {
  return curriculum.exams.find((e) => e.id === id);
}
