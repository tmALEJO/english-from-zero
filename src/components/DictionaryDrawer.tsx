import { useEffect, useMemo, useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { useApp } from '../state';
import { searchDictionary, units, type DictionaryRow } from '../engine/content';
import { Emoji, EnglishText, SpeakButton } from './common';
import { describeInterval } from '../engine/srs';

export function DictEntryView({ entry, onPractice }: { entry: DictionaryRow; onPractice?: (itemId: string) => void }) {
  const { cards } = useApp();
  const card = entry.itemId ? cards.find((c) => c.itemId === entry.itemId) : undefined;
  return (
    <article className="entry">
      <div className="entry__top">
        {entry.emoji && <Emoji e={entry.emoji} className="pic pic--lg" />}
        <div>
          <h2 className="entry__en" lang="en">{entry.en}</h2>
          <p className="entry__es">{entry.es}</p>
          {entry.say && <p className="entry__say">Suena como: <b>{entry.say}</b></p>}
        </div>
        <SpeakButton text={entry.en} />
      </div>
      {entry.tip && <p className="entry__tip">💡 {entry.tip}</p>}
      {entry.note && <p className="entry__tip">💡 {entry.note}</p>}
      {entry.examples?.map((ex) => (
        <p key={ex.en} className="entry__ex">
          <EnglishText text={ex.en} /> <SpeakButton text={ex.en} /> <span className="es">{ex.es}</span>
        </p>
      ))}
      <footer className="entry__meta">
        {entry.unitId && <span>Aparece en: {units[entry.unitId]?.title}</span>}
        {card ? <span>Próximo repaso {describeInterval((card.due - Date.now()) / 86400000)}</span> : entry.itemId && <span>Aún no la has aprendido</span>}
        {onPractice && entry.itemId && card && (
          <button type="button" className="btn btn--ghost btn--sm" onClick={() => onPractice(entry.itemId!)}>
            Practicar esta palabra
          </button>
        )}
      </footer>
    </article>
  );
}

/** Diccionario lateral: se abre sin salir de la lección. */
export function DictionaryDrawer() {
  const { dict, closeDict, openDict } = useApp();
  const [q, setQ] = useState('');
  const navigate = useNavigate();
  useEffect(() => { if (dict.open) setQ(dict.query ?? ''); }, [dict.open, dict.query]);
  useEffect(() => {
    const onKey = (e: KeyboardEvent) => e.key === 'Escape' && closeDict();
    window.addEventListener('keydown', onKey);
    return () => window.removeEventListener('keydown', onKey);
  }, [closeDict]);
  const results = useMemo(() => (q ? searchDictionary(q).slice(0, 30) : []), [q]);
  if (!dict.open) return null;
  return (
    <div className="drawer" role="dialog" aria-modal="true" aria-label="Diccionario">
      <button type="button" className="drawer__scrim" aria-label="Cerrar diccionario" onClick={closeDict} />
      <div className="drawer__panel">
        <header className="drawer__head">
          <h2>Diccionario</h2>
          <button type="button" className="icon-btn" onClick={closeDict} aria-label="Cerrar">✕</button>
        </header>
        <input
          className="input"
          placeholder="Busca en inglés o en español"
          value={q}
          onChange={(e) => { setQ(e.target.value); }}
          autoFocus={!dict.entry}
        />
        {dict.entry && !q && (
          <DictEntryView entry={dict.entry} onPractice={(id) => { closeDict(); navigate(`/practicar?items=${id}&title=${encodeURIComponent(dict.entry!.en)}`); }} />
        )}
        {q && (
          <ul className="list">
            {results.map((r) => (
              <li key={r.key}>
                <button type="button" className="list__row" onClick={() => { setQ(''); openDict({ entry: r }); }}>
                  <span className="list__pic">{r.emoji ? <Emoji e={r.emoji} /> : '·'}</span>
                  <span lang="en" className="list__main">{r.en}</span>
                  <span className="list__side">{r.es}</span>
                </button>
              </li>
            ))}
            {!results.length && <li className="muted">No está en el diccionario todavía. Prueba con otra forma de la palabra.</li>}
          </ul>
        )}
      </div>
    </div>
  );
}
