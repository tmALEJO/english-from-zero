import { createContext, useCallback, useContext, useEffect, useState, type ReactNode } from 'react';
import { useLiveQuery } from 'dexie-react-hooks';
import { db, getSettings, saveSettings } from './db/db';
import type { CardRow, HistoryRow, LessonRow, Settings } from './types';
import { DEFAULT_SETTINGS } from './types';
import type { DictionaryRow } from './engine/content';

interface AppState {
  settings: Settings;
  updateSettings: (p: Partial<Settings>) => Promise<void>;
  cards: CardRow[];
  lessons: LessonRow[];
  history: HistoryRow[];
  ready: boolean;
  /** Diccionario lateral: se abre desde cualquier pantalla, incluso en medio de una lección. */
  dict: { open: boolean; entry?: DictionaryRow; query?: string };
  openDict: (x?: { entry?: DictionaryRow; query?: string }) => void;
  closeDict: () => void;
}

const Ctx = createContext<AppState | null>(null);

export function AppProvider({ children }: { children: ReactNode }) {
  const [settings, setSettings] = useState<Settings>(DEFAULT_SETTINGS);
  const [settingsReady, setSettingsReady] = useState(false);
  const [dict, setDict] = useState<AppState['dict']>({ open: false });

  const cards = useLiveQuery(() => db.cards.toArray(), []);
  const lessons = useLiveQuery(() => db.lessons.toArray(), []);
  const history = useLiveQuery(() => db.history.orderBy('at').reverse().toArray(), []);
  const kv = useLiveQuery(() => db.kv.get('settings'), []);

  useEffect(() => {
    getSettings().then((s) => { setSettings(s); setSettingsReady(true); });
  }, [kv]);

  const updateSettings = useCallback(async (p: Partial<Settings>) => {
    setSettings(await saveSettings(p));
  }, []);

  const value: AppState = {
    settings,
    updateSettings,
    cards: cards ?? [],
    lessons: lessons ?? [],
    history: history ?? [],
    ready: settingsReady && cards !== undefined && lessons !== undefined,
    dict,
    openDict: (x) => setDict({ open: true, ...x }),
    closeDict: () => setDict({ open: false }),
  };
  return <Ctx.Provider value={value}>{children}</Ctx.Provider>;
}

export function useApp(): AppState {
  const v = useContext(Ctx);
  if (!v) throw new Error('useApp fuera de AppProvider');
  return v;
}
