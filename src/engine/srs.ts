import { createEmptyCard, fsrs, generatorParameters, Rating, type Card, type Grade } from 'ts-fsrs';
import type { AutoMode, CardRow } from '../types';
import { canUseMode } from './steps';
import { getItem } from './content';

/**
 * Repetición espaciada con FSRS. Sin pasos de minutos: los intervalos crecen en días
 * (≈1 → 3 → 7 → 15…) según qué tan bien recuerdas cada ítem.
 */
const scheduler = fsrs(
  generatorParameters({ request_retention: 0.9, enable_fuzz: true, enable_short_term: false, maximum_interval: 365 }),
);

export type Outcome = 'again' | 'hard' | 'good' | 'easy';

const RATING: Record<Outcome, Grade> = {
  again: Rating.Again,
  hard: Rating.Hard,
  good: Rating.Good,
  easy: Rating.Easy,
};

function toCard(r: CardRow): Card {
  return {
    due: new Date(r.due),
    stability: r.stability,
    difficulty: r.difficulty,
    elapsed_days: r.elapsed_days,
    scheduled_days: r.scheduled_days,
    learning_steps: r.learning_steps,
    reps: r.reps,
    lapses: r.lapses,
    state: r.state,
    last_review: r.last_review != null ? new Date(r.last_review) : undefined,
  } as Card;
}

function fromCard(c: Card, base: Pick<CardRow, 'itemId' | 'unitId' | 'lastMode'>): CardRow {
  return {
    ...base,
    due: c.due.getTime(),
    stability: c.stability,
    difficulty: c.difficulty,
    elapsed_days: c.elapsed_days,
    scheduled_days: c.scheduled_days,
    learning_steps: c.learning_steps,
    reps: c.reps,
    lapses: c.lapses,
    state: c.state,
    last_review: c.last_review ? c.last_review.getTime() : null,
  };
}

export function newCard(itemId: string, unitId: string, now = new Date()): CardRow {
  return fromCard(createEmptyCard(now), { itemId, unitId });
}

/** Aplica el resultado de un repaso y devuelve la tarjeta con su próxima fecha. */
export function review(row: CardRow, outcome: Outcome, mode?: AutoMode, now = new Date()): CardRow {
  const { card } = scheduler.next(toCard(row), now, RATING[outcome]);
  return fromCard(card, { itemId: row.itemId, unitId: row.unitId, lastMode: mode ?? row.lastMode });
}

/** Traduce el desempeño en un ejercicio a una calificación FSRS. */
export function outcomeFrom(correctFirstTry: boolean, attempts: number): Outcome {
  if (correctFirstTry) return 'good';
  return attempts <= 2 ? 'hard' : 'again';
}

export function isDue(row: CardRow, now = Date.now()): boolean {
  return row.due <= now;
}

const MODE_CYCLE: AutoMode[] = ['listen-pick', 'picture-pick', 'read-pick', 'build'];

/** Elige un modo distinto al último para que cada repaso sea en un contexto diferente. */
export function nextMode(row: CardRow, rand: () => number = Math.random): AutoMode {
  const item = getItem(row.itemId);
  const usable = MODE_CYCLE.filter((m) => canUseMode(item, m) && m !== row.lastMode);
  if (!usable.length) return 'listen-pick';
  // Ítems más nuevos o difíciles: más escucha. Ítems maduros: más producción (armar frases).
  if (row.stability > 10 && usable.includes('build')) return 'build';
  return usable[Math.floor(rand() * usable.length)];
}

export function describeInterval(days: number): string {
  if (days < 1) return 'hoy';
  if (days < 2) return 'mañana';
  if (days < 7) return `en ${Math.round(days)} días`;
  if (days < 30) return `en ${Math.round(days / 7)} semana${Math.round(days / 7) > 1 ? 's' : ''}`;
  return `en ${Math.round(days / 30)} mes${Math.round(days / 30) > 1 ? 'es' : ''}`;
}
