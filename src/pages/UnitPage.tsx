import { Link, useParams } from 'react-router-dom';
import { useApp } from '../state';
import { units } from '../engine/content';
import { unitStatuses } from '../engine/progress';
import { describeInterval } from '../engine/srs';
import { Page, SpeakButton } from '../components/common';

const FOCUS: Record<string, string> = {
  listening: '👂 Escuchar', reading: '📖 Leer', pronunciation: '👄 Pronunciar',
  grammar: '🔎 Descubrir gramática', speaking: '🎙️ Hablar', vocabulary: '🧩 Vocabulario',
};

export default function UnitPage() {
  const { unitId = '' } = useParams();
  const { lessons, cards, settings, openDict } = useApp();
  const u = units[unitId];
  if (!u) return <Page title="Unidad no encontrada"><Link to="/ruta">Volver a la ruta</Link></Page>;
  const status = unitStatuses(lessons, settings.explorerMode)[u.id];
  const done = new Map(lessons.map((l) => [l.lessonId, l]));
  const firstPending = u.lessons.find((l) => !done.has(l.id));
  const learned = u.items.filter((it) => cards.some((c) => c.itemId === it.id));

  return (
    <Page
      title={`${u.emoji} ${u.title}`}
      intro={u.summary}
      actions={<Link to="/ruta" className="btn btn--ghost btn--sm">Ruta</Link>}
    >
      <p className={`cando ${status === 'done' ? 'cando--done' : ''}`}>
        {status === 'done' ? '🏅' : '🎯'} {u.canDo}
      </p>

      <h2>Lecciones</h2>
      <ol className="lessons">
        {u.lessons.map((l, i) => {
          const row = done.get(l.id);
          const locked = !row && l !== firstPending && !settings.explorerMode;
          return (
            <li key={l.id} className={`lesson ${row ? 'lesson--done' : ''} ${locked ? 'lesson--locked' : ''}`}>
              <span className="lesson__n">{row ? '✓' : i + 1}</span>
              <span className="lesson__body">
                <span className="lesson__title">{l.title}</span>
                <span className="muted">{FOCUS[l.focus]}{l.newItems.length ? ` · ${l.newItems.length} nuevas` : ''}{row ? ` · hecha ${row.timesCompleted} ${row.timesCompleted === 1 ? 'vez' : 'veces'}` : ''}</span>
              </span>
              {locked ? <span className="muted">🔒</span> : <Link to={`/leccion/${l.id}`} className="btn btn--sm btn--primary">{row ? 'Repetir' : 'Empezar'}</Link>}
            </li>
          );
        })}
      </ol>

      {learned.length > 0 && (
        <section>
          <div className="row-between">
            <h2>Palabras de esta unidad</h2>
            <Link to={`/practicar?items=${learned.map((i) => i.id).join(',')}&title=${encodeURIComponent('Practicar: ' + u.title)}`} className="btn btn--sm btn--ghost">
              Practicar unidad
            </Link>
          </div>
          <ul className="words">
            {learned.map((it) => {
              const c = cards.find((x) => x.itemId === it.id)!;
              return (
                <li key={it.id} className="words__row">
                  <span className="words__pic" aria-hidden>{it.emoji}</span>
                  <button type="button" className="words__main" onClick={() => openDict({ entry: { key: it.id, en: it.en, es: it.es, emoji: it.emoji, say: it.say, tip: it.tip, examples: it.examples, itemId: it.id, unitId: u.id } })}>
                    <b lang="en">{it.en}</b> <span className="muted">{it.es}</span>
                  </button>
                  <SpeakButton text={it.en} />
                  <span className="words__due muted">{describeInterval((c.due - Date.now()) / 86400000)}</span>
                  <Link to={`/practicar?items=${it.id}&title=${encodeURIComponent(it.en)}`} className="btn btn--sm btn--ghost" aria-label={`Practicar ${it.en}`}>Practicar</Link>
                </li>
              );
            })}
          </ul>
        </section>
      )}
    </Page>
  );
}
