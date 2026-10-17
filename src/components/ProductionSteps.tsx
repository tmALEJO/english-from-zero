import { useContext, useEffect, useRef, useState } from 'react';
import type { Step } from '../types';
import type { StepResult } from './Steps';
import { ExamContext, Feedback, type Phase } from './Steps';
import { EnglishText, SpeakButton, Spanish } from './common';
import { checkTyped, type TypedCheck } from '../engine/text';
import { canListen, listen, speak } from '../engine/speech';
import { checkSpeech } from '../engine/text';
import { useApp } from '../state';

type Done = (r: StepResult) => void;

/** Muestra palabra por palabra qué estuvo bien, qué tuvo un error pequeño y qué faltó. */
function Corrections({ check }: { check: TypedCheck }) {
  return (
    <p className="corrections" lang="en">
      {check.words.map((w, i) => (
        <span key={i} className={`corr corr--${w.status}`}>{w.word}</span>
      ))}
    </p>
  );
}

function useTyped(answers: string[], onDone: Done) {
  const [value, setValue] = useState('');
  const [phase, setPhase] = useState<Phase>('answering');
  const [check, setCheck] = useState<TypedCheck | null>(null);
  const [attempts, setAttempts] = useState(0);
  const submit = () => {
    if (!value.trim()) return;
    const c = checkTyped(value, answers);
    setCheck(c);
    setAttempts((a) => a + 1);
    setPhase(c.ok ? 'right' : 'wrong');
  };
  return {
    value, setValue, phase, check, submit,
    retry: () => { setPhase('answering'); setValue(''); },
    finish: () => onDone({ graded: true, correctFirstTry: attempts === 1 && phase === 'right', attempts }),
  };
}

/** Dictado: escucha (las veces que quieras) y escribe exactamente lo que oíste. */
export function DictationStep({ step, onDone }: { step: Extract<Step, { kind: 'dictation' }>; onDone: Done }) {
  const t = useTyped([step.en], onDone);
  const inputRef = useRef<HTMLInputElement>(null);
  const hasTypo = t.check?.words.some((w) => w.status === 'typo');
  return (
    <div className="step">
      <p className="step__kicker">Dictado: escucha y escribe</p>
      <div className="listen-hero"><SpeakButton text={step.en} auto big /></div>
      <form onSubmit={(e) => { e.preventDefault(); t.submit(); }} className="typed">
        <input
          ref={inputRef}
          className="input input--big"
          lang="en"
          autoCapitalize="off"
          autoCorrect="off"
          spellCheck={false}
          autoComplete="off"
          placeholder="Escribe en inglés lo que escuchaste"
          value={t.value}
          disabled={t.phase !== 'answering'}
          onChange={(e) => t.setValue(e.target.value)}
          autoFocus
        />
        {t.phase === 'answering' && (
          <div className="actions">
            <button type="submit" className="btn btn--primary" disabled={!t.value.trim()}>Comprobar</button>
          </div>
        )}
      </form>
      {t.check && t.phase !== 'answering' && <Corrections check={t.check} />}
      <Feedback
        phase={t.phase}
        correct={<><b lang="en">{step.en}</b>{step.es && <span className="es">{step.es}</span>}</>}
        extra={t.phase === 'right' && hasTypo ? 'Casi perfecto: revisa las letras marcadas en amarillo.' : undefined}
        onRetry={() => { t.retry(); setTimeout(() => inputRef.current?.focus(), 0); }}
        onContinue={t.finish}
      />
    </div>
  );
}

/** Escritura guiada: la idea en español, tú la escribes en inglés. */
export function WriteStep({ step, onDone }: { step: Extract<Step, { kind: 'write' }>; onDone: Done }) {
  const t = useTyped([step.en, ...(step.accept ?? [])], onDone);
  const [showHint, setShowHint] = useState(false);
  return (
    <div className="step">
      <p className="step__kicker">Escribe en inglés</p>
      <h2 className="step__title">{step.es}</h2>
      {step.hint && (showHint ? <p className="step__note">💡 {step.hint}</p> : <button type="button" className="btn btn--ghost btn--sm self-start" onClick={() => setShowHint(true)}>Ver pista</button>)}
      <form onSubmit={(e) => { e.preventDefault(); t.submit(); }} className="typed">
        <textarea
          className="input input--big"
          lang="en"
          rows={2}
          autoCapitalize="sentences"
          spellCheck={false}
          placeholder="Tu frase en inglés"
          value={t.value}
          disabled={t.phase !== 'answering'}
          onChange={(e) => t.setValue(e.target.value)}
          onKeyDown={(e) => { if (e.key === 'Enter' && !e.shiftKey) { e.preventDefault(); t.submit(); } }}
          autoFocus
        />
        {t.phase === 'answering' && (
          <div className="actions">
            <button type="submit" className="btn btn--primary" disabled={!t.value.trim()}>Comprobar</button>
          </div>
        )}
      </form>
      {t.check && t.phase !== 'answering' && <Corrections check={t.check} />}
      <Feedback
        phase={t.phase}
        correct={<><b lang="en">{step.en}</b> <SpeakButton text={step.en} /></>}
        extra={step.accept?.length ? `También vale: ${step.accept.join(' / ')}` : undefined}
        onRetry={t.retry}
        onContinue={t.finish}
      />
    </div>
  );
}

/**
 * Juego de rol: escuchas a la otra persona y, en tu turno, eliges o DICES la respuesta adecuada.
 * Se califica si elegiste lo apropiado para la situación (no solo lo gramatical).
 */
export function RoleplayStep({ step, onDone }: { step: Extract<Step, { kind: 'roleplay' }>; onDone: Done }) {
  const { settings } = useApp();
  const exam = useContext(ExamContext);
  const [turn, setTurn] = useState(0);
  const [log, setLog] = useState<{ who: string; en: string; es: string; mine?: boolean }[]>([]);
  const [picked, setPicked] = useState<number | null>(null);
  const [mistakes, setMistakes] = useState(0);
  const [listening, setListening] = useState(false);
  const [micMsg, setMicMsg] = useState('');
  const [micOk, setMicOk] = useState<boolean | null>(null);

  const advance = async (from: number, logNow: typeof log) => {
    let i = from;
    const out = [...logNow];
    while (i < step.turns.length) {
      const t = step.turns[i];
      if ('you' in t) break;
      out.push({ who: t.who, en: t.en, es: t.es });
      setLog([...out]);
      await speak(t.en, { rate: settings.voiceRate, voiceName: settings.voiceName, speaker: t.who });
      i++;
    }
    setTurn(i);
  };

  // Arranca la conversación una sola vez (el ref evita el doble arranque del modo estricto).
  const started = useRef(false);
  useEffect(() => {
    if (started.current) return;
    started.current = true;
    void advance(0, []);
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, []);

  const current = step.turns[turn];
  const done = turn >= step.turns.length;

  const choose = (k: number) => {
    if (!current || !('you' in current) || picked !== null) return;
    setPicked(k);
    if (!current.options[k].ok) setMistakes((m) => m + 1);
  };

  const confirm = () => {
    if (!current || !('you' in current) || picked === null) return;
    const opt = current.options[picked];
    if (!opt.ok && !exam) { setPicked(null); return; } // otra oportunidad
    const best = current.options.find((o) => o.ok)!;
    const said = opt.ok ? opt : best;
    const next = [...log, { who: 'Tú', en: said.en, es: said.es, mine: true }];
    setLog(next);
    setPicked(null);
    setMicMsg('');
    setMicOk(null);
    void speak(said.en, { rate: settings.voiceRate, voiceName: settings.voiceName, speaker: 'Tú' }).then(() => advance(turn + 1, next));
  };

  const sayIt = async () => {
    if (!current || !('you' in current)) return;
    setListening(true);
    setMicMsg('');
    try {
      const heard = await listen();
      const scores = current.options.map((o) => checkSpeech(o.en, heard));
      const bestIdx = scores.reduce((b, s, i) => (s.score > scores[b].score ? i : b), 0);
      if (scores[bestIdx].score < 0.5) { setMicMsg(`Escuché "${heard[0] ?? ''}". Inténtalo otra vez o toca una opción.`); setMicOk(false); }
      else { setMicMsg(`Escuché: "${scores[bestIdx].heard}"`); setMicOk(true); choose(bestIdx); }
    } catch (e) { setMicMsg((e as Error).message); setMicOk(false); }
    setListening(false);
  };

  const [canMic, setCanMic] = useState(false);
  useEffect(() => { if (settings.speakingEnabled) void canListen().then(setCanMic); }, [settings.speakingEnabled]);

  return (
    <div className="step">
      <p className="step__kicker">Juego de rol</p>
      <h2 className="step__title">{step.title}</h2>
      {step.scene && <p className="step__note">{step.scene}</p>}
      <ol className="dialogue">
        {log.map((l, k) => (
          <li key={k} className={`bubble ${l.mine ? 'bubble--right bubble--me' : ''}`}>
            <span className="bubble__who">{l.who}</span>
            <p><EnglishText text={l.en} /> <SpeakButton text={l.en} /></p>
            <Spanish text={l.es} />
          </li>
        ))}
      </ol>

      {current && 'you' in current && (
        <div className="your-turn">
          <p className="your-turn__label">Tu turno. ¿Qué dices?</p>
          <div className="options options--list">
            {current.options.map((o, k) => {
              const cls = picked === k ? (o.ok ? 'option option--wide option--right' : 'option option--wide option--wrong') : 'option option--wide';
              return (
                <button key={k} type="button" className={cls} onClick={() => choose(k)} disabled={picked !== null && picked !== k}>
                  <span lang="en">{o.en}</span>
                </button>
              );
            })}
          </div>
          {canMic && picked === null && (
            <button type="button" className={`btn btn--ghost ${listening ? 'is-listening' : ''}`} onClick={sayIt} disabled={listening}>
              🎙️ {listening ? 'Te escucho…' : 'Decirlo en voz alta (opcional)'}
            </button>
          )}
          {micMsg && <p className={`notice ${micOk === false ? 'notice--fix' : ''}`}>{micMsg}</p>}
          {picked !== null && (
            <div className={`feedback ${current.options[picked].ok ? 'feedback--ok' : 'feedback--fix'}`}>
              <p className="feedback__title">{current.options[picked].ok ? '¡Buena respuesta!' : 'Mejor no…'}</p>
              {current.options[picked].why && <p>{current.options[picked].why}</p>}
              <p className="es">{current.options[picked].es}</p>
              <div className="feedback__actions">
                <button type="button" className="btn btn--primary" onClick={confirm} autoFocus>
                  {current.options[picked].ok || exam ? 'Continuar' : 'Elegir otra'}
                </button>
              </div>
            </div>
          )}
        </div>
      )}

      {done && (
        <div className="actions">
          <button type="button" className="btn btn--primary" onClick={() => onDone({ graded: true, correctFirstTry: mistakes === 0, attempts: mistakes + 1 })}>
            Terminar conversación
          </button>
        </div>
      )}
    </div>
  );
}
