import { Link } from 'react-router-dom';
import { useApp } from '../state';
import { curriculum, route, units } from '../engine/content';
import { lessonsDone, unitStatuses, type UnitStatus } from '../engine/progress';
import { Page } from '../components/common';

const STATUS_TEXT: Record<UnitStatus, string> = {
  done: 'Completada',
  'in-progress': 'En curso',
  available: 'Disponible',
  locked: 'Termina la anterior para abrirla',
  planned: 'Próximamente',
};

export default function RoutePage() {
  const { lessons, settings } = useApp();
  const st = unitStatuses(lessons, settings.explorerMode);
  return (
    <Page title="Tu ruta" intro="De cero a avanzado, un tema a la vez. Las unidades terminadas siempre se pueden repetir.">
      {curriculum.levels.map((lv) => {
        const refs = route.filter((r) => r.level === lv.id);
        return (
          <section key={lv.id} className="level">
            <header className="level__head">
              <span className="level__id">{lv.id}</span>
              <div>
                <h2>{lv.name}</h2>
                <p className="muted">{lv.description}</p>
              </div>
            </header>
            <ol className="path">
              {refs.map((r) => {
                const s = st[r.id];
                const u = units[r.id];
                const open = s !== 'locked' && s !== 'planned';
                const body = (
                  <>
                    <span className="path__dot" aria-hidden>{s === 'done' ? '✓' : r.emoji}</span>
                    <span className="path__body">
                      <span className="path__title">{r.title}</span>
                      <span className="path__cando">{r.canDo}</span>
                      {r.grammar && r.grammar.length > 0 && <span className="path__grammar">{r.grammar.join(' · ')}</span>}
                    </span>
                    <span className="path__state">
                      {u && (s === 'in-progress' || s === 'done') ? `${lessonsDone(r.id, lessons)}/${u.lessons.length}` : STATUS_TEXT[s]}
                    </span>
                  </>
                );
                return (
                  <li key={r.id} className={`path__item path__item--${s}`}>
                    {open ? <Link to={`/unidad/${r.id}`} className="path__link">{body}</Link> : <div className="path__link" aria-disabled>{body}</div>}
                  </li>
                );
              })}
            </ol>
          </section>
        );
      })}
    </Page>
  );
}
