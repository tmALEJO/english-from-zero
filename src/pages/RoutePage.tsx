import { Link } from 'react-router-dom';
import { useApp } from '../state';
import { curriculum, units } from '../engine/content';
import { fullRoute, lessonsDone, unitStatuses, examStatus, type UnitStatus } from '../engine/progress';
import { Page } from '../components/common';

const STATUS_TEXT: Record<UnitStatus, string> = {
  done: 'Completada',
  'in-progress': 'En curso',
  available: 'Disponible',
  locked: 'Termina lo anterior',
  planned: 'Próximamente',
};

export default function RoutePage() {
  const { lessons, settings } = useApp();
  const st = unitStatuses(lessons, settings.explorerMode);

  return (
    <Page title="Tu ruta" intro="De cero a avanzado. Cada bloque termina con un examen que certifica lo aprendido. Lo terminado siempre se puede repetir.">
      {curriculum.levels.map((lv) => {
        const entries = fullRoute.filter((e) => (e.type === 'unit' ? e.ref.level === lv.id : e.exam.level === lv.id));
        if (!entries.length) return null;
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
              {entries.map((e) => {
                if (e.type === 'exam') {
                  const es = examStatus(e.exam, lessons);
                  const open = es === 'available' || settings.explorerMode;
                  const body = (
                    <>
                      <span className="path__dot path__dot--exam" aria-hidden>{es === 'passed' ? '🏅' : '📝'}</span>
                      <span className="path__body">
                        <span className="path__title">{e.exam.title}</span>
                        <span className="path__cando">{e.exam.kind === 'final' ? `Certifica el nivel ${e.exam.level}` : 'Examen de control'} · {e.exam.questions} preguntas · {e.exam.passPct}% para aprobar</span>
                      </span>
                      <span className="path__state">{es === 'passed' ? 'Aprobado' : open ? 'Disponible' : 'Bloqueado'}</span>
                    </>
                  );
                  return (
                    <li key={e.exam.id} className={`path__item path__item--exam path__item--${es}`}>
                      {open || es === 'passed' ? <Link to={`/examen/${e.exam.id}`} className="path__link">{body}</Link> : <div className="path__link" aria-disabled>{body}</div>}
                    </li>
                  );
                }
                const r = e.ref;
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
