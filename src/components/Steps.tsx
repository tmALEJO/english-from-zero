import { createContext, useContext, useEffect, useMemo, useState, type ReactNode } from 'react';
import type { Item, Step } from '../types';
import { EnglishText, Picture, SpeakButton, Spanish } from './common';
import { speak } from '../engine/speech';
import { sameSentence } from '../engine/text';
import { useApp } from '../state';
import { SpeakStep } from './SpeakStep';
import { DictationStep, RoleplayStep, WriteStep } from './ProductionSteps';

/** En exámenes no hay segundo intento: se muestra la respuesta y se sigue. */
export const ExamContext = createContext(false);

export interface StepResult { graded: boolean; correctFirstTry: boolean; attempts: number; skipped?: boolean }

interface Props { step: Step; onDone: (r: StepResult) => void }

// ─── Pieza común: barra de acción + retroalimentación amable ──

export type Phase = 'answering' | 'right' | 'wrong';

export function Feedback({ phase, correct, extra, onRetry, onContinue }: { phase: Phase; correct?: ReactNode; extra?: string; onRetry: () => void; onContinue: () => void }) {
  const exam = useContext(ExamContext);
  if (phase === 'answering') return null;
  if (phase === 'right') {
    return (
      <div className="feedback feedback--ok" role="status">
        <p className="feedback__title">¡Bien!</p>
        {extra && <p>{extra}</p>}
        <button type="button" className="btn btn--primary" onClick={onContinue} autoFocus>Continuar</button>
      </div>
    );
  }
  return (
    <div className="feedback feedback--fix" role="status">
      <p className="feedback__title">Casi. Así es:</p>
      {correct && <div className="feedback__answer">{correct}</div>}
      {extra && <p>{extra}</p>}
      <div className="feedback__actions">
        {!exam && <button type="button" className="btn btn--primary" onClick={onRetry} autoFocus>Intentar otra vez</button>}
        <button type="button" className={exam ? 'btn btn--primary' : 'btn btn--ghost'} onClick={onContinue} autoFocus={exam}>Continuar</button>
      </div>
    </div>
  );
}

/** Lógica compartida por todos los ejercicios de elegir una opción. */
function useChoice(correctIndex: number, onDone: Props['onDone']) {
  const [picked, setPicked] = useState<number | null>(null);
  const [phase, setPhase] = useState<Phase>('answering');
  const [attempts, setAttempts] = useState(0);
  const [wrong, setWrong] = useState<Set<number>>(new Set());
  const check = (i: number) => {
    if (phase !== 'answering') return;
    setPicked(i);
    const n = attempts + 1;
    setAttempts(n);
    if (i === correctIndex) setPhase('right');
    else { setPhase('wrong'); setWrong((w) => new Set(w).add(i)); }
  };
  return {
    picked, phase, wrong,
    check,
    retry: () => { setPhase('answering'); setPicked(null); },
    finish: () => onDone({ graded: true, correctFirstTry: attempts === 1 && phase === 'right', attempts }),
  };
}

function OptionGrid({ children }: { children: ReactNode }) {
  return <div className="options">{children}</div>;
}

function optClass(i: number, c: ReturnType<typeof useChoice>, correct: number) {
  let cls = 'option';
  if (c.wrong.has(i)) cls += ' option--wrong';
  if (c.phase !== 'answering' && i === correct) cls += ' option--right';
  if (c.picked === i) cls += ' option--picked';
  return cls;
}

/** Cómo se muestra una opción-imagen: emoji si todas lo tienen; si no, el español. */
function ItemFace({ item, allEmoji }: { item: Item; allEmoji: boolean }) {
  return allEmoji ? <Picture emoji={item.emoji} fallback={item.es} size="lg" /> : <span className="option__text">{item.es}</span>;
}

// ─── Pasos de INPUT (no se califican) ────────────────────────

function PresentStep({ step, onDone }: { step: Extract<Step, { kind: 'present' }>; onDone: Props['onDone'] }) {
  const [i, setI] = useState(0);
  const item = step.items[i];
  const last = i === step.items.length - 1;
  return (
    <div className="step step--present">
      <p className="step__kicker">Palabra nueva {step.items.length > 1 ? `${i + 1} de ${step.items.length}` : ''}</p>
      {step.note && i === 0 && <p className="step__note">{step.note}</p>}
      <div className="present-card" key={item.id}>
        <Picture emoji={item.emoji} fallback="🗨️" size="xl" />
        <p className="present-card__en"><EnglishText text={item.en} /></p>
        <SpeakButton text={item.en} auto big />
        {item.say && <p className="present-card__say">Suena como: <b>{item.say}</b></p>}
        <Spanish text={item.es} />
        {item.tip && <p className="present-card__tip">💡 {item.tip}</p>}
      </div>
      <div className="actions">
        <button type="button" className="btn btn--primary" onClick={() => (last ? onDone({ graded: false, correctFirstTry: true, attempts: 0 }) : setI(i + 1))}>
          {last ? 'Continuar' : 'Siguiente palabra'}
        </button>
      </div>
    </div>
  );
}

function DialogueStep({ step, onDone }: { step: Extract<Step, { kind: 'dialogue' }>; onDone: Props['onDone'] }) {
  const { settings } = useApp();
  const [active, setActive] = useState<number | null>(null);
  const playAll = async () => {
    for (let k = 0; k < step.lines.length; k++) {
      setActive(k);
      await speak(step.lines[k].en, { rate: settings.voiceRate, voiceName: settings.voiceName, speaker: step.lines[k].who });
      await new Promise((r) => setTimeout(r, 350));
    }
    setActive(null);
  };
  const speakers = [...new Set(step.lines.map((l) => l.who))];
  return (
    <div className="step">
      <p className="step__kicker">Escucha la conversación</p>
      <h2 className="step__title">{step.title}</h2>
      {step.scene && <p className="step__note">{step.scene}</p>}
      <button type="button" className="btn btn--ghost" onClick={playAll}>▶ Escuchar todo</button>
      <ol className="dialogue">
        {step.lines.map((l, k) => (
          <li key={k} className={`bubble ${speakers.indexOf(l.who) % 2 ? 'bubble--right' : ''} ${active === k ? 'is-active' : ''}`}>
            <span className="bubble__who">{l.who}</span>
            <p><EnglishText text={l.en} /> <SpeakButton text={l.en} speaker={l.who} /></p>
            <Spanish text={l.es} />
          </li>
        ))}
      </ol>
      <p className="hint">Toca cualquier palabra para ver qué significa.</p>
      <div className="actions">
        <button type="button" className="btn btn--primary" onClick={() => onDone({ graded: false, correctFirstTry: true, attempts: 0 })}>Continuar</button>
      </div>
    </div>
  );
}

function StoryStep({ step, onDone }: { step: Extract<Step, { kind: 'story' }>; onDone: Props['onDone'] }) {
  return (
    <div className="step">
      <p className="step__kicker">Historia corta</p>
      <h2 className="step__title">{step.emoji} {step.title}</h2>
      <div className="story">
        {step.paragraphs.map((p, k) => (
          <div key={k} className="story__p">
            <p><EnglishText text={p.en} /> <SpeakButton text={p.en} /></p>
            <Spanish text={p.es} />
          </div>
        ))}
      </div>
      <p className="hint">Lee con calma. Toca una palabra si no la conoces.</p>
      <div className="actions">
        <button type="button" className="btn btn--primary" onClick={() => onDone({ graded: false, correctFirstTry: true, attempts: 0 })}>Ya la leí</button>
      </div>
    </div>
  );
}

function TipStep({ step, onDone }: { step: Extract<Step, { kind: 'tip' }>; onDone: Props['onDone'] }) {
  return (
    <div className="step step--tip">
      <span className="pic pic--xl" aria-hidden>{step.emoji ?? '💡'}</span>
      <h2 className="step__title">{step.title}</h2>
      <p className="step__text">{step.text}</p>
      <div className="actions">
        <button type="button" className="btn btn--primary" onClick={() => onDone({ graded: false, correctFirstTry: true, attempts: 0 })}>Entendido</button>
      </div>
    </div>
  );
}

// ─── Pasos de PRÁCTICA (se califican) ────────────────────────

function ListenPick({ step, onDone }: { step: Extract<Step, { kind: 'listen-pick' }>; onDone: Props['onDone'] }) {
  const correct = step.options.findIndex((o) => o.id === step.target.id);
  const c = useChoice(correct, onDone);
  const allEmoji = step.options.every((o) => o.emoji);
  return (
    <div className="step">
      <p className="step__kicker">Escucha y elige</p>
      <div className="listen-hero"><SpeakButton text={step.target.en} auto big /></div>
      <OptionGrid>
        {step.options.map((o, i) => (
          <button key={o.id} type="button" className={optClass(i, c, correct)} disabled={c.wrong.has(i) && c.phase === 'answering'} onClick={() => c.check(i)} aria-label={o.es}>
            <ItemFace item={o} allEmoji={allEmoji} />
          </button>
        ))}
      </OptionGrid>
      <Feedback phase={c.phase} correct={<><b lang="en">{step.target.en}</b> = {step.target.es} <SpeakButton text={step.target.en} /></>} onRetry={c.retry} onContinue={c.finish} />
    </div>
  );
}

function ReadPick({ step, onDone }: { step: Extract<Step, { kind: 'read-pick' }>; onDone: Props['onDone'] }) {
  const correct = step.options.findIndex((o) => o.id === step.target.id);
  const c = useChoice(correct, onDone);
  const allEmoji = step.options.every((o) => o.emoji);
  return (
    <div className="step">
      <p className="step__kicker">Lee y elige</p>
      <p className="prompt-en" lang="en">{step.target.en}</p>
      <OptionGrid>
        {step.options.map((o, i) => (
          <button key={o.id} type="button" className={optClass(i, c, correct)} disabled={c.wrong.has(i) && c.phase === 'answering'} onClick={() => c.check(i)} aria-label={o.es}>
            <ItemFace item={o} allEmoji={allEmoji} />
          </button>
        ))}
      </OptionGrid>
      <Feedback phase={c.phase} correct={<><b lang="en">{step.target.en}</b> = {step.target.es} {step.target.emoji}</>} onRetry={c.retry} onContinue={c.finish} />
    </div>
  );
}

function PicturePick({ step, onDone }: { step: Extract<Step, { kind: 'picture-pick' }>; onDone: Props['onDone'] }) {
  const correct = step.options.findIndex((o) => o.id === step.target.id);
  const c = useChoice(correct, onDone);
  return (
    <div className="step">
      <p className="step__kicker">¿Cómo se dice en inglés?</p>
      <div className="picture-hero">
        <Picture emoji={step.target.emoji} fallback={step.target.es} size="xl" />
        {step.target.emoji && <span className="muted">{step.target.es}</span>}
      </div>
      <OptionGrid>
        {step.options.map((o, i) => (
          <button key={o.id} type="button" className={`${optClass(i, c, correct)} option--wide`} disabled={c.wrong.has(i) && c.phase === 'answering'} onClick={() => c.check(i)}>
            <span className="option__text" lang="en">{o.en}</span>
          </button>
        ))}
      </OptionGrid>
      <Feedback phase={c.phase} correct={<><b lang="en">{step.target.en}</b> <SpeakButton text={step.target.en} auto /></>} onRetry={c.retry} onContinue={c.finish} />
    </div>
  );
}

function MinimalPair({ step, onDone }: { step: Extract<Step, { kind: 'minimal-pair' }>; onDone: Props['onDone'] }) {
  const target = step.play === 'a' ? step.a : step.b;
  const correct = step.play === 'a' ? 0 : 1;
  const c = useChoice(correct, onDone);
  const opts = [{ w: step.a, h: step.aHint }, { w: step.b, h: step.bHint }];
  return (
    <div className="step">
      <p className="step__kicker">{step.title ?? '¿Cuál escuchaste?'}</p>
      <div className="listen-hero"><SpeakButton text={target} auto big /></div>
      <div className="options options--two">
        {opts.map((o, i) => (
          <button key={i} type="button" className={optClass(i, c, correct)} onClick={() => c.check(i)} disabled={c.wrong.has(i) && c.phase === 'answering'}>
            {o.h && <span className="pic pic--lg" aria-hidden>{o.h}</span>}
            <span className="option__text" lang="en">{o.w}</span>
          </button>
        ))}
      </div>
      {c.phase !== 'answering' && (
        <div className="compare">
          <span>Compara:</span>
          <span lang="en">{step.a}</span> <SpeakButton text={step.a} />
          <span lang="en">{step.b}</span> <SpeakButton text={step.b} />
        </div>
      )}
      <Feedback phase={c.phase} correct={<b lang="en">{target}</b>} onRetry={c.retry} onContinue={c.finish} />
    </div>
  );
}

function FillStep({ step, onDone }: { step: Extract<Step, { kind: 'fill' }>; onDone: Props['onDone'] }) {
  const c = useChoice(step.answer, onDone);
  const filled = c.phase !== 'answering' ? step.options[step.answer] : c.picked !== null ? step.options[c.picked] : '___';
  const [before, after] = step.en.split('___');
  return (
    <div className="step">
      <p className="step__kicker">Completa la frase</p>
      <p className="prompt-en" lang="en">
        {before}<span className={`blank ${c.phase === 'right' ? 'blank--ok' : ''}`}>{filled}</span>{after}
      </p>
      {step.es && <Spanish text={step.es} />}
      <div className="options options--chips">
        {step.options.map((o, i) => (
          <button key={o} type="button" className={`${optClass(i, c, step.answer)} option--chip`} disabled={c.wrong.has(i) && c.phase === 'answering'} onClick={() => c.check(i)} lang="en">
            {o}
          </button>
        ))}
      </div>
      <Feedback phase={c.phase} correct={<b lang="en">{step.en.replace('___', step.options[step.answer])}</b>} extra={step.explain} onRetry={c.retry} onContinue={c.finish} />
    </div>
  );
}

function QuestionStep({ step, onDone }: { step: Extract<Step, { kind: 'question' }>; onDone: Props['onDone'] }) {
  const c = useChoice(step.answer, onDone);
  return (
    <div className="step">
      <p className="step__kicker">Sobre “{step.context}”</p>
      <h2 className="step__title">{step.q}</h2>
      <div className="options options--list">
        {step.options.map((o, i) => (
          <button key={o} type="button" className={`${optClass(i, c, step.answer)} option--wide`} disabled={c.wrong.has(i) && c.phase === 'answering'} onClick={() => c.check(i)}>
            {o}
          </button>
        ))}
      </div>
      <Feedback phase={c.phase} correct={<b>{step.options[step.answer]}</b>} onRetry={c.retry} onContinue={c.finish} />
    </div>
  );
}

function BuildStep({ step, onDone }: { step: Extract<Step, { kind: 'build' }>; onDone: Props['onDone'] }) {
  const [chosen, setChosen] = useState<number[]>([]);
  const [phase, setPhase] = useState<Phase>('answering');
  const [attempts, setAttempts] = useState(0);
  const sentence = chosen.map((i) => step.tiles[i]).join(' ');
  const check = () => {
    setAttempts((a) => a + 1);
    setPhase(sameSentence(sentence, step.en) ? 'right' : 'wrong');
    if (sameSentence(sentence, step.en)) void speak(step.en);
  };
  return (
    <div className="step">
      <p className="step__kicker">Arma la frase en inglés</p>
      <h2 className="step__title">{step.es}</h2>
      <div className={`build-line ${phase === 'right' ? 'build-line--ok' : ''}`} aria-live="polite">
        {chosen.length === 0 && <span className="muted">Toca las palabras en orden</span>}
        {chosen.map((ti, k) => (
          <button key={k} type="button" className="tile tile--placed" lang="en" disabled={phase !== 'answering'} onClick={() => setChosen(chosen.filter((_, j) => j !== k))}>
            {step.tiles[ti]}
          </button>
        ))}
      </div>
      <div className="tiles">
        {step.tiles.map((t, i) => (
          <button key={i} type="button" className="tile" lang="en" disabled={chosen.includes(i) || phase !== 'answering'} onClick={() => setChosen([...chosen, i])}>
            {t}
          </button>
        ))}
      </div>
      {phase === 'answering' && (
        <div className="actions">
          <button type="button" className="btn btn--primary" disabled={!chosen.length} onClick={check}>Comprobar</button>
        </div>
      )}
      <Feedback
        phase={phase}
        correct={<><b lang="en">{step.en}</b> <SpeakButton text={step.en} auto /></>}
        onRetry={() => { setPhase('answering'); setChosen([]); }}
        onContinue={() => onDone({ graded: true, correctFirstTry: attempts === 1 && phase === 'right', attempts })}
      />
    </div>
  );
}

/** Gramática inductiva: ejemplos → notar → hipótesis → regla con nombre. */
function DiscoverStep({ step, onDone }: { step: Extract<Step, { kind: 'discover' }>; onDone: Props['onDone'] }) {
  const [stage, setStage] = useState<'examples' | 'question' | 'rule'>('examples');
  const [showMarks, setShowMarks] = useState(false);
  const c = useChoice(step.answer, () => undefined);
  const firstTry = useMemo(() => ({ v: true }), []);
  useEffect(() => { if (c.phase === 'wrong') firstTry.v = false; }, [c.phase, firstTry]);
  if (stage === 'examples') {
    return (
      <div className="step">
        <p className="step__kicker">Descubre el patrón</p>
        <h2 className="step__title">{step.intro}</h2>
        <ul className="examples">
          {step.examples.map((ex) => (
            <li key={ex.en}>
              <p><EnglishText text={ex.en} mark={showMarks ? ex.mark : []} /> <SpeakButton text={ex.en.replace('→', '.')} /></p>
              <Spanish text={ex.es} />
            </li>
          ))}
        </ul>
        <div className="actions">
          {!showMarks ? (
            <button type="button" className="btn btn--ghost" onClick={() => setShowMarks(true)}>Dame una pista</button>
          ) : null}
          <button type="button" className="btn btn--primary" onClick={() => { setShowMarks(true); setStage('question'); }}>Ya lo vi</button>
        </div>
      </div>
    );
  }
  if (stage === 'question') {
    return (
      <div className="step">
        <p className="step__kicker">¿Qué notaste?</p>
        <ul className="examples examples--compact">
          {step.examples.slice(0, 4).map((ex) => <li key={ex.en}><EnglishText text={ex.en} mark={ex.mark} /></li>)}
        </ul>
        <h2 className="step__title">{step.question}</h2>
        <div className="options options--list">
          {step.options.map((o, i) => (
            <button key={o} type="button" className={`${optClass(i, c, step.answer)} option--wide`} disabled={c.wrong.has(i) && c.phase === 'answering'} onClick={() => c.check(i)}>
              {o}
            </button>
          ))}
        </div>
        {c.phase === 'right' && (
          <div className="feedback feedback--ok"><p className="feedback__title">¡Exacto, lo descubriste tú!</p>
            <button type="button" className="btn btn--primary" onClick={() => setStage('rule')} autoFocus>Ver la regla</button></div>
        )}
        {c.phase === 'wrong' && (
          <div className="feedback feedback--fix"><p className="feedback__title">Mira otra vez las palabras marcadas.</p>
            <div className="feedback__actions">
              <button type="button" className="btn btn--primary" onClick={c.retry} autoFocus>Intentar otra vez</button>
              <button type="button" className="btn btn--ghost" onClick={() => setStage('rule')}>Ver la regla</button>
            </div></div>
        )}
      </div>
    );
  }
  return (
    <div className="step step--rule">
      <p className="step__kicker">Acabas de aprender</p>
      <h2 className="rule__topic">{step.topic}</h2>
      <p className="rule__text">{step.rule}</p>
      {step.ruleExamples?.map((ex) => (
        <p key={ex.en} className="rule__ex"><EnglishText text={ex.en} /> <SpeakButton text={ex.en} /> <span className="es">{ex.es}</span></p>
      ))}
      <div className="actions">
        <button type="button" className="btn btn--primary" onClick={() => onDone({ graded: true, correctFirstTry: firstTry.v, attempts: firstTry.v ? 1 : 2 })}>Practicar</button>
      </div>
    </div>
  );
}

export function StepView({ step, onDone }: Props) {
  switch (step.kind) {
    case 'present': return <PresentStep step={step} onDone={onDone} />;
    case 'dialogue': return <DialogueStep step={step} onDone={onDone} />;
    case 'story': return <StoryStep step={step} onDone={onDone} />;
    case 'tip': return <TipStep step={step} onDone={onDone} />;
    case 'listen-pick': return <ListenPick step={step} onDone={onDone} />;
    case 'read-pick': return <ReadPick step={step} onDone={onDone} />;
    case 'picture-pick': return <PicturePick step={step} onDone={onDone} />;
    case 'minimal-pair': return <MinimalPair step={step} onDone={onDone} />;
    case 'fill': return <FillStep step={step} onDone={onDone} />;
    case 'question': return <QuestionStep step={step} onDone={onDone} />;
    case 'build': return <BuildStep step={step} onDone={onDone} />;
    case 'discover': return <DiscoverStep step={step} onDone={onDone} />;
    case 'speak': return <SpeakStep step={step} onDone={onDone} />;
    case 'dictation': return <DictationStep step={step} onDone={onDone} />;
    case 'write': return <WriteStep step={step} onDone={onDone} />;
    case 'roleplay': return <RoleplayStep step={step} onDone={onDone} />;
  }
}
