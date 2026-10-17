import type { Curriculum, DictEntry, Item, LevelId, Unit } from '../types';
import curriculumJson from '../../content/curriculum.json';
import dictionaryJson from '../../content/dictionary.json';
import { normalize, tokenize } from './text';

// Todas las unidades de /content/units se cargan solas: para agregar una unidad
// basta con crear su JSON y registrarla en curriculum.json.
const unitModules = import.meta.glob('../../content/units/*.json', { eager: true, import: 'default' });

export const curriculum = curriculumJson as Curriculum;

export const units: Record<string, Unit> = {};
for (const mod of Object.values(unitModules)) {
  const u = mod as Unit;
  units[u.id] = u;
}

export const LEVEL_ORDER: LevelId[] = ['A0', 'A1', 'A2', 'B1', 'B2', 'C1'];

/** Unidades en el orden de la ruta. */
export const route = curriculum.units;

export const itemsById: Record<string, Item & { unitId: string }> = {};
for (const u of Object.values(units)) for (const it of u.items) itemsById[it.id] = { ...it, unitId: u.id };

export function getItem(id: string): Item & { unitId: string } {
  const it = itemsById[id];
  if (!it) throw new Error(`Ítem no encontrado en el contenido: ${id}`);
  return it;
}

export function findLesson(lessonId: string) {
  for (const u of Object.values(units)) {
    const idx = u.lessons.findIndex((l) => l.id === lessonId);
    if (idx >= 0) return { unit: u, lesson: u.lessons[idx], index: idx };
  }
  return null;
}

// ─── Diccionario ─────────────────────────────────────────────

export interface DictionaryRow {
  key: string;
  en: string;
  es: string;
  emoji?: string;
  say?: string;
  tip?: string;
  note?: string;
  examples?: { en: string; es: string }[];
  itemId?: string;
  unitId?: string;
  tags?: string[];
}

const extra = dictionaryJson as DictEntry[];

export const dictionary: DictionaryRow[] = [];
/** Índice forma → entrada, para tocar cualquier palabra de una historia y abrir su significado. */
const formIndex = new Map<string, DictionaryRow>();

function addForm(form: string, row: DictionaryRow, overwrite = false) {
  const k = normalize(form);
  if (!k) return;
  if (overwrite || !formIndex.has(k)) formIndex.set(k, row);
}

for (const it of Object.values(itemsById)) {
  if (it.kind === 'sound') continue;
  const row: DictionaryRow = {
    key: it.id, en: it.en, es: it.es, emoji: it.emoji, say: it.say, tip: it.tip,
    examples: it.examples, itemId: it.id, unitId: it.unitId, tags: it.tags,
  };
  dictionary.push(row);
  addForm(it.en.replace(/[.!?]+$/, ''), row, true);
  for (const f of it.forms ?? []) addForm(f, row, true);
}
for (const e of extra) {
  if (formIndex.has(normalize(e.en))) continue;
  const row: DictionaryRow = { key: 'x:' + e.en, en: e.en, es: e.es, emoji: e.emoji, say: e.say, note: e.note };
  dictionary.push(row);
  addForm(e.en, row);
  for (const f of e.forms ?? []) addForm(f, row);
}
dictionary.sort((a, b) => a.en.localeCompare(b.en));

export function lookupWord(word: string): DictionaryRow | undefined {
  const k = normalize(word);
  if (formIndex.has(k)) return formIndex.get(k);
  // Plurales y terceras personas sencillas: cats → cat, works → work
  for (const cut of ['s', 'es', 'ed', 'd', 'ing']) {
    if (k.endsWith(cut) && formIndex.has(k.slice(0, -cut.length))) return formIndex.get(k.slice(0, -cut.length));
  }
  return undefined;
}

export function searchDictionary(q: string): DictionaryRow[] {
  const n = normalize(q);
  if (!n) return dictionary;
  return dictionary
    .map((r) => {
      const en = normalize(r.en), es = normalize(r.es);
      const score = en === n || es === n ? 0 : en.startsWith(n) || es.startsWith(n) ? 1 : en.includes(n) || es.includes(n) ? 2 : 9;
      return { r, score };
    })
    .filter((x) => x.score < 9)
    .sort((a, b) => a.score - b.score || a.r.en.localeCompare(b.r.en))
    .map((x) => x.r);
}

export { tokenize };
