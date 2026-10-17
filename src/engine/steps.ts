import type { AutoMode, Item, Lesson, Step, Unit } from '../types';
import { getItem, itemsById } from './content';
import { sample, sentenceTiles, shuffle } from './text';

type Rand = () => number;

/** Ítems que pueden servir de distractores para `target` (mismo tipo, distinto significado). */
function distractorPool(target: Item, pool: Item[]): Item[] {
  const same = pool.filter((p) => p.id !== target.id && p.kind === target.kind && p.en !== target.en && p.es !== target.es);
  if (same.length >= 3) return same;
  // Si la unidad tiene pocos, se completa con ítems de todo el contenido.
  const global = Object.values(itemsById).filter((p) => p.id !== target.id && p.kind === target.kind && p.en !== target.en);
  return [...same, ...global.filter((g) => !same.some((s) => s.id === g.id))];
}

function options(target: Item, pool: Item[], n: number, rand: Rand): Item[] {
  const needEmoji = Boolean(target.emoji);
  let cand = distractorPool(target, pool);
  if (needEmoji) {
    const withEmoji = cand.filter((c) => c.emoji && c.emoji !== target.emoji);
    if (withEmoji.length >= n - 1) cand = withEmoji;
  }
  return shuffle([target, ...sample(cand, n - 1, rand)], rand);
}

export function canUseMode(item: Item, mode: AutoMode): boolean {
  if (mode === 'build') return item.en.trim().split(/\s+/).length >= 2;
  if (mode === 'dictation') return item.kind !== 'sound';
  if (item.kind === 'sound') return mode === 'listen-pick';
  return true;
}

/** Genera un ejercicio de un ítem en un modo dado. Es la base de la "repetición variada". */
export function autoStep(item: Item, mode: AutoMode, pool: Item[], rand: Rand = Math.random): Step {
  switch (mode) {
    case 'listen-pick':
      return { kind: 'listen-pick', target: item, options: options(item, pool, 3, rand) };
    case 'read-pick':
      return { kind: 'read-pick', target: item, options: options(item, pool, 3, rand) };
    case 'picture-pick':
      return { kind: 'picture-pick', target: item, options: options(item, pool, 3, rand) };
    case 'build': {
      const tiles = sentenceTiles(item.en);
      const extraWord = sample(
        pool.flatMap((p) => sentenceTiles(p.en)).filter((w) => !tiles.includes(w)),
        tiles.length > 3 ? 1 : 0,
        rand,
      );
      return { kind: 'build', en: item.en, es: item.es, tiles: shuffle([...tiles, ...extraWord], rand), itemId: item.id };
    }
    case 'speak':
      return { kind: 'speak', en: item.en, es: item.es, itemId: item.id, note: item.say ? `Suena parecido a: ${item.say}` : undefined };
    case 'dictation':
      return { kind: 'dictation', en: item.en, es: item.es, itemId: item.id };
  }
}

/** Convierte una lección (datos) en la lista de pasos que la pantalla reproduce. */
export function expandLesson(lesson: Lesson, unit: Unit, rand: Rand = Math.random): Step[] {
  const pool = unit.items;
  const steps: Step[] = [];
  for (const a of lesson.activities) {
    switch (a.type) {
      case 'present':
        steps.push({ kind: 'present', items: a.items.map(getItem), note: a.note });
        break;
      case 'auto': {
        const items = a.items.map(getItem);
        const pairs: { item: Item; mode: AutoMode }[] = [];
        for (const mode of a.modes) for (const item of items) if (canUseMode(item, mode)) pairs.push({ item, mode });
        // Mezcla, pero evita repetir el mismo ítem dos veces seguidas.
        let mixed = shuffle(pairs, rand);
        for (let i = 1; i < mixed.length; i++) {
          if (mixed[i].item.id === mixed[i - 1].item.id) {
            const j = mixed.findIndex((p, k) => k > i && p.item.id !== mixed[i - 1].item.id);
            if (j > 0) [mixed[i], mixed[j]] = [mixed[j], mixed[i]];
          }
        }
        if (a.count) mixed = mixed.slice(0, a.count);
        for (const p of mixed) steps.push(autoStep(p.item, p.mode, pool, rand));
        break;
      }
      case 'minimal-pair':
        for (const p of a.pairs) steps.push({ kind: 'minimal-pair', title: a.title, ...p });
        break;
      case 'build': {
        const tiles = sentenceTiles(a.en);
        steps.push({ kind: 'build', en: a.en, es: a.es, tiles: shuffle([...tiles, ...(a.distractors ?? [])], rand) });
        break;
      }
      case 'fill':
        steps.push({ kind: 'fill', en: a.en, es: a.es, options: a.options, answer: a.answer, explain: a.explain });
        break;
      case 'dialogue':
        steps.push({ kind: 'dialogue', title: a.title, scene: a.scene, lines: a.lines });
        break;
      case 'story':
        steps.push({ kind: 'story', title: a.title, emoji: a.emoji, paragraphs: a.paragraphs });
        for (const q of a.questions ?? []) steps.push({ kind: 'question', ...q, context: a.title });
        break;
      case 'discover':
        steps.push({ kind: 'discover', ...a });
        break;
      case 'speak':
        steps.push({ kind: 'speak', en: a.en, es: a.es, note: a.note });
        break;
      case 'tip':
        steps.push({ kind: 'tip', title: a.title, text: a.text, emoji: a.emoji });
        break;
      case 'dictation':
        steps.push({ kind: 'dictation', en: a.en, es: a.es });
        break;
      case 'write':
        steps.push({ kind: 'write', es: a.es, en: a.en, accept: a.accept, hint: a.hint });
        break;
      case 'roleplay':
        steps.push({ kind: 'roleplay', title: a.title, scene: a.scene, turns: a.turns });
        break;
    }
  }
  return steps;
}
