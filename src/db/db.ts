import Dexie, { type EntityTable } from 'dexie';
import type { CardRow, HistoryRow, LessonRow, Settings } from '../types';
import { DEFAULT_SETTINGS } from '../types';

/** Todo el progreso vive en IndexedDB del dispositivo (navegador del PC o WebView del APK). */
export class AppDB extends Dexie {
  cards!: EntityTable<CardRow, 'itemId'>;
  lessons!: EntityTable<LessonRow, 'lessonId'>;
  history!: EntityTable<HistoryRow, 'id'>;
  kv!: EntityTable<{ key: string; value: unknown }, 'key'>;

  constructor(name = 'english-from-zero') {
    super(name);
    this.version(1).stores({
      cards: 'itemId, unitId, due',
      lessons: 'lessonId, unitId',
      history: 'id, at, type',
      kv: 'key',
    });
  }
}

export const db = new AppDB();

export async function getSettings(d: AppDB = db): Promise<Settings> {
  const row = await d.kv.get('settings');
  return { ...DEFAULT_SETTINGS, ...((row?.value as Partial<Settings>) ?? {}) };
}

export async function saveSettings(patch: Partial<Settings>, d: AppDB = db): Promise<Settings> {
  const next = { ...(await getSettings(d)), ...patch };
  await d.kv.put({ key: 'settings', value: next });
  return next;
}
