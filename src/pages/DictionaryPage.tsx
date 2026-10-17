import { useMemo, useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { useApp } from '../state';
import { searchDictionary, type DictionaryRow } from '../engine/content';
import { DictEntryView } from '../components/DictionaryDrawer';
import { Page } from '../components/common';

export default function DictionaryPage() {
  const { cards } = useApp();
  const navigate = useNavigate();
  const [q, setQ] = useState('');
  const [onlyMine, setOnlyMine] = useState(false);
  const [sel, setSel] = useState<DictionaryRow | null>(null);
  const learned = useMemo(() => new Set(cards.map((c) => c.itemId)), [cards]);
  const rows = useMemo(
    () => searchDictionary(q).filter((r) => !onlyMine || (r.itemId && learned.has(r.itemId))),
    [q, onlyMine, learned],
  );

  return (
    <Page title="Diccionario" intro="Todas las palabras de la app, con audio y ejemplos. También lo puedes abrir en medio de una lección con 📖.">
      <div className="dict-tools">
        <input className="input" placeholder="Busca en inglés o en español" value={q} onChange={(e) => { setQ(e.target.value); setSel(null); }} />
        <label className="check">
          <input type="checkbox" checked={onlyMine} onChange={(e) => setOnlyMine(e.target.checked)} />
          Solo las que ya aprendí ({learned.size})
        </label>
      </div>
      <div className="dict-layout">
        <ul className="list list--dict">
          {rows.map((r) => (
            <li key={r.key}>
              <button type="button" className={`list__row ${sel?.key === r.key ? 'is-selected' : ''}`} onClick={() => setSel(r)}>
                <span className="list__pic" aria-hidden>{r.emoji ?? '·'}</span>
                <span className="list__main" lang="en">{r.en}</span>
                <span className="list__side">{r.es}</span>
                {r.itemId && learned.has(r.itemId) && <span className="list__dot" title="Aprendida">●</span>}
              </button>
            </li>
          ))}
          {!rows.length && <li className="muted">Sin resultados.</li>}
        </ul>
        {sel && (
          <div className="dict-detail">
            <DictEntryView entry={sel} onPractice={(id) => navigate(`/practicar?items=${id}&title=${encodeURIComponent(sel.en)}`)} />
          </div>
        )}
      </div>
    </Page>
  );
}
