import { useMemo, useRef, useState, type ReactNode } from 'react';
import { Link, useLocation, useNavigate, useParams, useSearchParams } from 'react-router-dom';
import type { AutoMode, Step } from '../types';
import { useApp } from '../state';
import { StepView, type StepResult } from '../components/Steps';
import { ExamContext } from '../components/Steps';
import { ProgressBar } from '../components/common';
import { findLesson, getItem, itemsById, units } from '../engine/content';
import { expandLesson } from '../engine/steps';
import { buildPractice, buildReview, buildWarmup, buildUnitTest, buildExam, findExam, isUnitDone, nextLesson, testId, examRowId, UNIT_TEST_PASS, type PlannedStep } from '../engine/progress';
import { outcomeFrom } from '../engine/srs';
import { completeLesson, completePractice, completeReview, completeAssessment, type ItemResult, type SessionSummary } from '../db/actions';
import { stopSpeaking } from '../engine/speech';

function stepItemId(s: Step): string | undefined {
  if ('target' in s) return s.target.id;
  if ((s.kind === 'build' || s.kind === 'speak') && s.itemId) return s.itemId;
  return undefined;
}

interface QueueEntry extends PlannedStep { key: number; retry?: boolean; section?: string }

interface PlayerProps {
  title: string;
  planned: QueueEntry[];
  exam?: boolean;
  onFinish: (s: Omit<SessionSummary, 'type' | 'refId' | 'title'>) => Promise<ReactNode>;
}

/** Reproductor común para lecciones, repasos y práctica libre. */
function Player({ title, planned, exam = false, onFinish }: PlayerProps) {
  const { openDict } = useApp();
  const navigate = useNavigate();
  const [queue, setQueue] = useState<QueueEntry[]>(planned);
  const [pos, setPos] = useState(0);
  const [end, setEnd] = useState<ReactNode | null>(null);
  const results = useRef<ItemResult[]>([]);
  const score = useRef({ correct: 0, total: 0 });
  const startedAt = useRef(Date.now());
  const nextKey = useRef(10000);

  const current = queue[pos];

  const handleDone = async (r: StepResult) => {
    const e = queue[pos];
    let q = queue;
    if (r.graded && !e.retry) {
      score.current.total++;
      if (r.correctFirstTry) score.current.correct++;
    }
    const itemId = e.itemId ?? stepItemId(e.step);
    if (r.graded && itemId && !e.retry) {
      results.current.push({ itemId, outcome: outcomeFrom(r.correctFirstTry, r.attempts), mode: e.mode as AutoMode | undefined });
    }
    // Si fallaste, el ejercicio vuelve al final de la sesión (una sola vez), en otro momento.
    if (r.graded && !r.correctFirstTry && !e.retry && e.step.kind !== 'discover' && !exam) {
      q = [...queue, { ...e, key: nextKey.current++, retry: true, section: 'Otra oportunidad' }];
      setQueue(q);
    }
    if (pos + 1 >= q.length) {
      stopSpeaking();
      const node = await onFinish({ ...score.current, startedAt: startedAt.current, results: results.current });
      setEnd(node);
    } else setPos(pos + 1);
  };

  const exit = () => {
    stopSpeaking();
    if (pos === 0 || confirm('¿Salir de la sesión? Lo que llevas no se guardará.')) navigate(-1);
  };

  if (end) return <div className="session session--end">{end}</div>;
  if (!current) return <div className="session"><p>No hay nada que practicar aquí.</p><Link to="/" className="btn btn--primary">Volver</Link></div>;

  return (
    <div className="session">
      <header className="session__top">
        <button type="button" className="icon-btn" onClick={exit} aria-label="Salir">✕</button>
        <div className="session__title">
          <span>{current.section ?? title}</span>
          <ProgressBar value={pos / queue.length} label="Avance de la sesión" />
        </div>
        <button type="button" className="icon-btn" onClick={() => openDict()} aria-label="Abrir diccionario" title="Diccionario">📖</button>
      </header>
      <div className="session__body" key={current.key}>
        <ExamContext.Provider value={exam}>
          <StepView step={current.step} onDone={handleDone} />
        </ExamContext.Provider>
      </div>
    </div>
  );
}

function filterSpeaking(steps: QueueEntry[], enabled: boolean) {
  return enabled ? steps : steps.filter((s) => s.step.kind !== 'speak');
}

let keySeq = 0;
const toEntries = (ps: PlannedStep[], section?: string): QueueEntry[] => ps.map((p) => ({ ...p, key: keySeq++, section }));

// ─── Lección ─────────────────────────────────────────────────

function LessonInner() {
  const { lessonId = '' } = useParams();
  const { cards, lessons, settings } = useApp();
  const found = findLesson(lessonId);
  // La sesión se arma UNA vez al entrar, aunque los datos cambien mientras juegas.
  const [planned] = useState<QueueEntry[]>(() => {
    if (!found) return [];
    const warm = buildWarmup(cards, found.unit.id, settings.warmupSize);
    const main = expandLesson(found.lesson, found.unit).map((step) => ({ step }));
    const warmEntries = warm.length
      ? [{ step: { kind: 'tip', emoji: '🔁', title: 'Calentamiento', text: 'Antes de empezar, un repaso rápido de lo que ya sabes. Así no se te olvida.' } as Step }, ...warm]
      : [];
    return filterSpeaking([...toEntries(warmEntries, 'Calentamiento'), ...toEntries(main)], settings.speakingEnabled);
  });
  const [wasUnitDone] = useState(() => (found ? isUnitDone(found.unit.id, lessons) : false));
  if (!found) return <div className="session"><p>Esa lección no existe.</p><Link to="/ruta" className="btn btn--primary">Ver la ruta</Link></div>;
  const { unit, lesson, index } = found;

  return (
    <Player
      title={`${unit.title} · ${lesson.title}`}
      planned={planned}
      onFinish={async (s) => {
        await completeLesson(unit, lesson, { ...s, type: 'lesson', refId: lesson.id, title: `${unit.title}: ${lesson.title}` });
        const doneNow = [...lessons.filter((l) => l.lessonId !== lesson.id), { lessonId: lesson.id, unitId: unit.id, firstCompletedAt: 0, lastCompletedAt: 0, timesCompleted: 1, bestScore: 0 }];
        const unitCompleted = !wasUnitDone && isUnitDone(unit.id, doneNow);
        const next = nextLesson(doneNow, settings.explorerMode);
        const sameUnitNext = unit.lessons[index + 1];
        return (
          <EndScreen
            title="Lección terminada"
            correct={s.correct}
            total={s.total}
            milestone={unitCompleted ? unit.canDo : undefined}
            learned={lesson.newItems.map((id) => getItem(id))}
            next={sameUnitNext ? { to: `/leccion/${sameUnitNext.id}`, label: `Siguiente: ${sameUnitNext.title}` } : next ? { to: `/leccion/${next.lesson.id}`, label: `Siguiente: ${next.unit.title}` } : undefined}
            repeat={`/leccion/${lesson.id}`}
            back={`/unidad/${unit.id}`}
          />
        );
      }}
    />
  );
}

// ─── Repaso espaciado ───────────────────────────────────────

function ReviewInner() {
  const { cards, settings } = useApp();
  const [planned] = useState(() => toEntries(buildReview(cards, settings.reviewSize)));
  return (
    <Player
      title="Repaso del día"
      planned={planned}
      onFinish={async (s) => {
        await completeReview({ ...s, type: 'review', refId: 'srs', title: 'Repaso del día' });
        return <EndScreen title="Repaso hecho" correct={s.correct} total={s.total} note="Cada palabra volverá cuando estés a punto de olvidarla: mañana, en unos días o en semanas." back="/repaso" />;
      }}
    />
  );
}

// ─── Práctica libre (unidad, tema, palabra, difíciles) ───────

function PracticeInner() {
  const [params] = useSearchParams();
  const ids = useMemo(() => (params.get('items') ?? '').split(',').filter((id) => itemsById[id]), [params]);
  const title = params.get('title') ?? 'Práctica libre';
  const [planned] = useState(() => toEntries(buildPractice(ids, ids.length <= 2 ? 4 : 2)));
  return (
    <Player
      title={title}
      planned={planned}
      onFinish={async (s) => {
        await completePractice({ ...s, type: 'practice', refId: params.get('items') ?? '', title });
        return <EndScreen title="Práctica terminada" correct={s.correct} total={s.total} note="La práctica libre no cambia tu calendario de repaso: puedes practicar todo lo que quieras." repeat={`/practicar?${params.toString()}`} back="/repaso" />;
      }}
    />
  );
}

// ─── Pantalla final ─────────────────────────────────────────

function EndScreen(p: {
  title: string; correct: number; total: number; milestone?: string; note?: string;
  learned?: { id: string; en: string; es: string; emoji?: string }[];
  next?: { to: string; label: string }; repeat?: string; back: string;
}) {
  const pct = p.total ? Math.round((p.correct / p.total) * 100) : 100;
  return (
    <div className="end">
      {p.milestone && (
        <section className="milestone" aria-live="polite">
          <span className="milestone__badge" aria-hidden>🏅</span>
          <p className="milestone__label">Nuevo logro</p>
          <h1 className="milestone__text">{p.milestone}</h1>
        </section>
      )}
      <h2>{p.title}</h2>
      {p.total > 0 && <p className="end__score">{p.correct} de {p.total} a la primera <span className="muted">({pct}%)</span></p>}
      {p.total > 0 && pct < 60 && <p className="muted">Es normal fallar al principio. Repetir la lección ayuda mucho.</p>}
      {p.learned && p.learned.length > 0 && (
        <>
          <h3>Aprendiste</h3>
          <ul className="learned">
            {p.learned.map((it) => <li key={it.id}><span aria-hidden>{it.emoji}</span> <b lang="en">{it.en}</b> <span className="muted">{it.es}</span></li>)}
          </ul>
          <p className="muted">Volverán en tu repaso en unos días, en otros contextos.</p>
        </>
      )}
      {p.note && <p className="muted">{p.note}</p>}
      <div className="end__actions">
        {p.next && <Link className="btn btn--primary" to={p.next.to} replace>{p.next.label}</Link>}
        {p.repeat && <Link className="btn btn--ghost" to={p.repeat} replace>Repetir</Link>}
        <Link className="btn btn--ghost" to={p.back} replace>Volver</Link>
      </div>
    </div>
  );
}

// ─── Prueba de unidad ───────────────────────────────────────

function UnitTestInner() {
  const { unitId = '' } = useParams();
  const { settings } = useApp();
  const unit = units[unitId];
  const [planned] = useState(() => (unit ? toEntries(buildUnitTest(unit)) : []));
  if (!unit) return <div className="session"><p>Unidad no encontrada.</p><Link to="/ruta" className="btn btn--primary">Ruta</Link></div>;
  return (
    <Player
      title={`Prueba: ${unit.title}`}
      planned={planned}
      exam
      onFinish={async (s) => {
        const score = await completeAssessment(testId(unit.id), unit.id, { ...s, type: 'test', refId: testId(unit.id), title: `Prueba: ${unit.title}` });
        const passed = score >= UNIT_TEST_PASS;
        const next = nextLesson([], settings.explorerMode);
        return (
          <EndScreen
            title={passed ? '¡Prueba aprobada!' : 'Prueba no aprobada'}
            correct={s.correct}
            total={s.total}
            milestone={passed ? unit.canDo : undefined}
            note={passed ? 'Unidad completada. Esta palabra entra firme a tu repaso.' : `Necesitas ${UNIT_TEST_PASS}% para aprobar. Repasa la unidad y vuelve a intentarlo: ¡no pierdes nada!`}
            next={passed && next ? { to: `/leccion/${next.lesson.id}`, label: `Siguiente: ${next.unit.title}` } : undefined}
            repeat={passed ? undefined : `/prueba/${unit.id}`}
            back={`/unidad/${unit.id}`}
          />
        );
      }}
    />
  );
}

// ─── Examen de control / final ──────────────────────────────

function ExamInner() {
  const { examId = '' } = useParams();
  const exam = findExam(examId);
  const [planned] = useState(() => (exam ? toEntries(buildExam(exam)) : []));
  if (!exam) return <div className="session"><p>Examen no encontrado.</p><Link to="/ruta" className="btn btn--primary">Ruta</Link></div>;
  return (
    <Player
      title={exam.title}
      planned={planned}
      exam
      onFinish={async (s) => {
        const score = await completeAssessment(examRowId(exam.id), exam.id, { ...s, type: 'exam', refId: exam.id, title: exam.title });
        const passed = score >= exam.passPct;
        return (
          <EndScreen
            title={passed ? (exam.kind === 'final' ? `¡Nivel ${exam.level} aprobado!` : '¡Examen aprobado!') : 'Examen no aprobado'}
            correct={s.correct}
            total={s.total}
            milestone={passed && exam.kind === 'final' ? `Alcanzaste el nivel ${exam.level}` : undefined}
            note={passed ? (exam.kind === 'final' ? '¡Felicitaciones! Has certificado este nivel completo.' : 'Puedes seguir avanzando en la ruta.') : `Necesitas ${exam.passPct}%. Repasa las unidades de este bloque y vuelve a intentarlo.`}
            repeat={passed ? undefined : `/examen/${exam.id}`}
            back="/ruta"
          />
        );
      }}
    />
  );
}

// Cada visita (incluido "Repetir") arma una sesión nueva: la clave de la ruta reinicia el componente.
function useSessionKey() {
  const l = useLocation();
  return `${l.pathname}${l.search}#${l.key}`;
}
export function LessonSession() { return <LessonInner key={useSessionKey()} />; }
export function ReviewSession() { return <ReviewInner key={useSessionKey()} />; }
export function PracticeSession() { return <PracticeInner key={useSessionKey()} />; }
export function UnitTestSession() { return <UnitTestInner key={useSessionKey()} />; }
export function ExamSession() { return <ExamInner key={useSessionKey()} />; }
