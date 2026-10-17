import { useEffect, useState } from 'react';
import type { Step } from '../types';
import type { StepResult } from './Steps';
import { EnglishText, SpeakButton, Spanish } from './common';
import { canListen, listen } from '../engine/speech';
import { checkSpeech, type SpeechCheck } from '../engine/text';

/**
 * Producción oral guiada y SIEMPRE opcional.
 * Mide si se te entiende (no el acento). Si algo falla: muestra qué se escuchó,
 * qué palabra faltó, te deja escuchar el modelo y repetir. Nunca bloquea.
 */
export function SpeakStep({ step, onDone }: { step: Extract<Step, { kind: 'speak' }>; onDone: (r: StepResult) => void }) {
  const [available, setAvailable] = useState<boolean | null>(null);
  const [state, setState] = useState<'idle' | 'listening' | 'result' | 'error'>('idle');
  const [result, setResult] = useState<SpeechCheck | null>(null);
  const [error, setError] = useState('');
  const [tries, setTries] = useState(0);

  useEffect(() => { canListen().then(setAvailable); }, []);

  const record = async () => {
    setState('listening');
    setError('');
    try {
      const heard = await listen();
      if (!heard.length) throw new Error('No escuché nada. Acércate al micrófono e inténtalo de nuevo.');
      setResult(checkSpeech(step.en, heard));
      setTries((t) => t + 1);
      setState('result');
    } catch (e) {
      setError((e as Error).message);
      setState('error');
    }
  };

  const skip = () => onDone({ graded: false, correctFirstTry: true, attempts: 0, skipped: true });
  const finish = () => onDone({ graded: false, correctFirstTry: Boolean(result?.ok), attempts: tries });

  return (
    <div className="step step--speak">
      <p className="step__kicker">Habla (opcional)</p>
      <p className="prompt-en"><EnglishText text={step.en} /></p>
      <SpeakButton text={step.en} big />
      <Spanish text={step.es} />
      {step.note && <p className="step__note">{step.note}</p>}

      {available === false && (
        <p className="notice">El reconocimiento de voz no está disponible aquí. En el PC usa Chrome o Edge; en Android, revisa que tengas la app de Google. Puedes repetir en voz alta igual y continuar.</p>
      )}

      {available && state !== 'result' && (
        <button type="button" className={`mic ${state === 'listening' ? 'is-listening' : ''}`} onClick={record} disabled={state === 'listening'}>
          <span aria-hidden>🎙️</span>
          {state === 'listening' ? 'Te escucho…' : 'Toca y habla'}
        </button>
      )}

      {state === 'error' && <p className="notice notice--fix">{error}</p>}

      {state === 'result' && result && (
        <div className={`feedback ${result.ok ? 'feedback--ok' : 'feedback--fix'}`} role="status">
          <p className="feedback__title">{result.ok ? '¡Se te entendió!' : 'Se entendió una parte'}</p>
          <p>Escuché: <i lang="en">“{result.heard}”</i></p>
          {!result.ok && result.missing.length > 0 && (
            <p>Faltó que se entendiera: {result.missing.map((w) => <b key={w} lang="en" className="missing">{w} </b>)}. Escucha el modelo y repite despacio.</p>
          )}
          <div className="feedback__actions">
            {!result.ok && <button type="button" className="btn btn--primary" onClick={() => setState('idle')}>Repetir</button>}
            <button type="button" className={result.ok ? 'btn btn--primary' : 'btn btn--ghost'} onClick={finish} autoFocus={result.ok}>Continuar</button>
          </div>
        </div>
      )}

      {state !== 'result' && (
        <div className="actions">
          <button type="button" className="btn btn--ghost" onClick={skip}>Ahora no</button>
          {tries > 0 && <button type="button" className="btn btn--ghost" onClick={finish}>Continuar</button>}
        </div>
      )}
    </div>
  );
}
