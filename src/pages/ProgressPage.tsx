import { Link } from 'react-router-dom';
import { useApp } from '../state';
import { currentLevel, levelProgress } from '../engine/progress';
import { formatDate, Page, ProgressBar } from '../components/common';

const TYPE: Record<string, string> = { lesson: 'Lección', review: 'Repaso', practice: 'Práctica' };

export default function ProgressPage() {
  const { lessons, cards, history } = useApp();
  const lvl = currentLevel(lessons);
  const levels = levelProgress(lessons);
  const mature = cards.filter((c) => c.stability >= 21).length;
  const minutes = Math.round(history.reduce((a, h) => a + h.durationSec, 0) / 60);

  return (
    <Page
      title="Tu progreso"
      intro={lvl.reached ? `Nivel alcanzado: ${lvl.reached}. Ahora trabajas en ${lvl.working}.` : `Estás construyendo tu nivel ${lvl.working}.`}
      actions={<div className="row-gap"><Link to="/copia" className="btn btn--ghost btn--sm">Exportar / importar</Link><Link to="/ajustes" className="btn btn--ghost btn--sm">Ajustes</Link></div>}
    >
      <div className="stats">
        <div><b>{cards.length}</b><span>palabras y frases aprendidas</span></div>
        <div><b>{mature}</b><span>ya firmes en tu memoria</span></div>
        <div><b>{lessons.length}</b><span>lecciones terminadas</span></div>
        <div><b>{minutes}</b><span>minutos de práctica</span></div>
      </div>

      <h2>Lo que ya puedes hacer</h2>
      {levels.map((lv) => {
        const total = lv.ready + lv.planned;
        return (
          <section key={lv.id} className={`lvl ${lv.id === lvl.working ? 'lvl--current' : ''}`}>
            <header className="lvl__head">
              <span className="level__id">{lv.id}</span>
              <span className="lvl__name">{lv.name}</span>
              <span className="muted">{lv.done}/{total}</span>
            </header>
            <ProgressBar value={total ? lv.done / total : 0} label={`Avance ${lv.id}`} />
            {lv.finalExam && (
              lv.certified
                ? <p className="lvl__cert">🏅 Nivel certificado</p>
                : <Link to={`/examen/${lv.finalExam.id}`} className="btn btn--ghost btn--sm">Examen final {lv.id}</Link>
            )}
            <ul className="cando-list">
              {lv.canDo.map((c) => (
                <li key={c.unitId} className={c.done ? 'is-done' : c.planned ? 'is-planned' : ''}>
                  <span aria-hidden>{c.done ? '🏅' : c.planned ? '·' : '○'}</span> {c.text}
                  {c.planned && <span className="muted"> (próximamente)</span>}
                </li>
              ))}
            </ul>
          </section>
        );
      })}

      <h2>Historial</h2>
      {history.length === 0 && <p className="muted">Aquí verás cada lección, repaso y práctica que hagas.</p>}
      <ul className="history">
        {history.slice(0, 60).map((h) => (
          <li key={h.id}>
            <span className="history__type">{TYPE[h.type]}</span>
            <span className="history__title">{h.title}</span>
            <span className="muted">{h.total ? `${h.correct}/${h.total}` : '—'} · {Math.max(1, Math.round(h.durationSec / 60))} min · {formatDate(h.at)}</span>
          </li>
        ))}
      </ul>
    </Page>
  );
}
