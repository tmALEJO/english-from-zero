import { Link } from 'react-router-dom';
import { useApp } from '../state';
import { currentLevel, levelProgress, nextStep, isUnitDone } from '../engine/progress';
import { curriculum, route, units } from '../engine/content';
import { isDue } from '../engine/srs';
import { Emoji, ProgressBar } from '../components/common';

function daysPracticedThisWeek(times: number[]): number {
  const weekAgo = Date.now() - 7 * 86400000;
  return new Set(times.filter((t) => t > weekAgo).map((t) => new Date(t).toDateString())).size;
}

export default function Home() {
  const { lessons, cards, history, settings } = useApp();
  const next = nextStep(lessons, settings.explorerMode);
  const due = cards.filter((c) => isDue(c)).length;
  const lvl = currentLevel(lessons);
  const lp = levelProgress(lessons).find((l) => l.id === lvl.working)!;
  const levelInfo = curriculum.levels.find((l) => l.id === lvl.working)!;
  const lastWin = [...route].reverse().find((r) => units[r.id] && isUnitDone(r.id, lessons));
  const days = daysPracticedThisWeek(history.map((h) => h.at));
  const isNew = lessons.length === 0;
  const total = lp.ready + lp.planned;

  return (
    <div className="page home">
      <header className="home__head">
        <p className="home__greet">{settings.learnerName ? `Hola, ${settings.learnerName}` : 'Hola'}</p>
        <h1 className="home__title">{isNew ? 'Empecemos desde cero.' : next ? 'Sigue donde te quedaste.' : 'Terminaste todo lo disponible.'}</h1>
      </header>

      {next && (() => {
        const to = next.kind === 'lesson' ? `/leccion/${next.lesson.id}` : next.kind === 'test' ? `/prueba/${next.unit.id}` : `/examen/${next.exam.id}`;
        const emoji = next.kind === 'exam' ? '📝' : next.kind === 'test' ? '🏁' : next.unit.emoji;
        const kicker = next.kind === 'exam' ? 'Examen' : next.kind === 'test' ? next.unit.title : next.unit.title;
        const title = next.kind === 'exam' ? next.exam.title : next.kind === 'test' ? 'Prueba de la unidad' : next.lesson.title;
        const meta = next.kind === 'exam' ? `${next.exam.questions} preguntas` : next.kind === 'test' ? 'Demuestra lo aprendido' : next.lesson.newItems.length ? `${next.lesson.newItems.length} palabras nuevas · unos 8 minutos` : 'Repaso y práctica · unos 8 minutos';
        return (
          <Link to={to} className="next">
            <Emoji e={emoji} className="next__emoji" />
            <span className="next__body">
              <span className="next__unit">{kicker}</span>
              <span className="next__lesson">{title}</span>
              <span className="next__meta">{meta}</span>
            </span>
            <span className="next__go">{isNew ? 'Empezar' : 'Continuar'}</span>
          </Link>
        );
      })()}

      <div className="home__grid">
        <Link to={due ? '/repasar' : '/repaso'} className="tile-card">
          <span className="tile-card__big">{due}</span>
          <span>{due === 1 ? 'palabra para repasar hoy' : 'palabras para repasar hoy'}</span>
          {due === 0 && <span className="muted">Nada pendiente. Puedes practicar libre.</span>}
        </Link>
        <Link to="/progreso" className="tile-card">
          <span className="tile-card__level">{lvl.working}</span>
          <span>{levelInfo.name}</span>
          <ProgressBar value={total ? lp.done / total : 0} label={`Avance en ${lvl.working}`} />
          <span className="muted">{lp.done} de {total} temas del nivel</span>
        </Link>
      </div>

      {lastWin && (
        <p className="home__win">🏅 <b>{lastWin.canDo}.</b></p>
      )}
      {days > 0 && <p className="muted">Practicaste {days} {days === 1 ? 'día' : 'días'} esta semana.</p>}
      {isNew && (
        <section className="home__how">
          <h2>Cómo funciona</h2>
          <p>Primero escuchas y lees; hablar llega después, cuando tú quieras. Cada lección trae máximo 4 palabras nuevas y el resto es repaso. Las palabras vuelven en días distintos y en otros contextos para que no se te olviden.</p>
        </section>
      )}
    </div>
  );
}
