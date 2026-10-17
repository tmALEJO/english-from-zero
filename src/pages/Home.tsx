import { Link } from 'react-router-dom';
import { useApp } from '../state';
import { currentLevel, levelProgress, nextLesson, lessonsDone } from '../engine/progress';
import { curriculum, route, units } from '../engine/content';
import { isDue } from '../engine/srs';
import { ProgressBar } from '../components/common';

function daysPracticedThisWeek(times: number[]): number {
  const weekAgo = Date.now() - 7 * 86400000;
  return new Set(times.filter((t) => t > weekAgo).map((t) => new Date(t).toDateString())).size;
}

export default function Home() {
  const { lessons, cards, history, settings } = useApp();
  const next = nextLesson(lessons, settings.explorerMode);
  const due = cards.filter((c) => isDue(c)).length;
  const lvl = currentLevel(lessons);
  const lp = levelProgress(lessons).find((l) => l.id === lvl.working)!;
  const levelInfo = curriculum.levels.find((l) => l.id === lvl.working)!;
  const lastWin = [...route].reverse().find((r) => units[r.id] && lessonsDone(r.id, lessons) === units[r.id].lessons.length);
  const days = daysPracticedThisWeek(history.map((h) => h.at));
  const isNew = lessons.length === 0;
  const total = lp.ready + lp.planned;

  return (
    <div className="page home">
      <header className="home__head">
        <p className="home__greet">{settings.learnerName ? `Hola, ${settings.learnerName}` : 'Hola'}</p>
        <h1 className="home__title">{isNew ? 'Empecemos desde cero.' : next ? 'Sigue donde te quedaste.' : 'Terminaste todo lo disponible.'}</h1>
      </header>

      {next && (
        <Link to={`/leccion/${next.lesson.id}`} className="next">
          <span className="next__emoji" aria-hidden>{next.unit.emoji}</span>
          <span className="next__body">
            <span className="next__unit">{next.unit.title}</span>
            <span className="next__lesson">{next.lesson.title}</span>
            <span className="next__meta">{next.lesson.newItems.length ? `${next.lesson.newItems.length} palabras nuevas` : 'Solo repaso y práctica'} · unos 8 minutos</span>
          </span>
          <span className="next__go">{isNew ? 'Empezar' : 'Continuar'}</span>
        </Link>
      )}

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
