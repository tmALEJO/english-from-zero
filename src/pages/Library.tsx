import { useMemo, useState } from 'react';
import { useApp } from '../state';
import library from '../../content/library.json';
import type { Reading } from '../types';
import { LEVEL_ORDER, curriculum } from '../engine/content';
import { currentLevel } from '../engine/progress';
import { Emoji, EnglishText, Page, Spanish, SpeakButton } from '../components/common';
import { speak, stopSpeaking } from '../engine/speech';

const readings = library as Reading[];
const KIND: Record<Reading['kind'], string> = { story: '📖 Historia', dialogue: '💬 Diálogo', article: '📰 Artículo', 'real-speech': '🎧 Habla real' };

export default function Library() {
  const { lessons } = useApp();
  const working = currentLevel(lessons).working;
  const [open, setOpen] = useState<Reading | null>(null);
  const [level, setLevel] = useState<string>('all');

  const list = useMemo(
    () => readings.filter((r) => level === 'all' || r.level === level).sort((a, b) => LEVEL_ORDER.indexOf(a.level) - LEVEL_ORDER.indexOf(b.level)),
    [level],
  );

  if (open) return <ReadingView reading={open} onClose={() => setOpen(null)} />;

  return (
    <Page
      title="Biblioteca"
      intro="Lee y escucha historias, diálogos y artículos de tu nivel. Mientras más leas y escuches, más rápido avanzas. Toca cualquier palabra para ver su significado."
    >
      <div className="chips">
        <button type="button" className={`chip ${level === 'all' ? 'is-active' : ''}`} onClick={() => setLevel('all')}>Todos</button>
        {curriculum.levels.map((lv) => (
          <button key={lv.id} type="button" className={`chip ${level === lv.id ? 'is-active' : ''}`} onClick={() => setLevel(lv.id)}>
            {lv.id}{lv.id === working ? ' · tu nivel' : ''}
          </button>
        ))}
      </div>
      <ul className="readings">
        {list.map((r) => (
          <li key={r.id}>
            <button type="button" className="reading-card" onClick={() => setOpen(r)}>
              <Emoji e={r.emoji} className="reading-card__emoji" />
              <span className="reading-card__body">
                <span className="reading-card__title">{r.title}</span>
                <span className="muted">{KIND[r.kind]} · {r.sentences.length} frases</span>
                <span className="reading-card__summary">{r.summary}</span>
              </span>
              <span className="reading-card__level">{r.level}</span>
            </button>
          </li>
        ))}
      </ul>
    </Page>
  );
}

type Mode = 'read' | 'listen' | 'shadow';

function ReadingView({ reading, onClose }: { reading: Reading; onClose: () => void }) {
  const { settings } = useApp();
  const [mode, setMode] = useState<Mode>('read');
  const [active, setActive] = useState<number | null>(null);
  const [playing, setPlaying] = useState(false);
  const [showQuestions, setShowQuestions] = useState(false);

  const playAll = async () => {
    setPlaying(true);
    for (let i = 0; i < reading.sentences.length; i++) {
      setActive(i);
      const s = reading.sentences[i];
      await speak(s.en, { rate: settings.voiceRate, voiceName: settings.voiceName, speaker: s.who, natural: true });
      if (mode === 'shadow') await new Promise((r) => setTimeout(r, 1200)); // pausa para repetir
      else await new Promise((r) => setTimeout(r, 250));
    }
    setActive(null);
    setPlaying(false);
  };

  const stop = () => { stopSpeaking(); setPlaying(false); setActive(null); };

  return (
    <div className="page reading-view">
      <header className="page__head">
        <div>
          <h1><Emoji e={reading.emoji} className="h-emoji" /> {reading.title}</h1>
          <p className="muted">{KIND[reading.kind]} · nivel {reading.level}</p>
        </div>
        <button type="button" className="btn btn--ghost btn--sm" onClick={() => { stop(); onClose(); }}>Cerrar</button>
      </header>

      <div className="chips">
        {(['read', 'listen', 'shadow'] as Mode[]).map((m) => (
          <button key={m} type="button" className={`chip ${mode === m ? 'is-active' : ''}`} onClick={() => { stop(); setMode(m); }}>
            {m === 'read' ? '📖 Leer' : m === 'listen' ? '🎧 Escuchar' : '🗣️ Shadowing'}
          </button>
        ))}
      </div>
      {mode === 'shadow' && <p className="hint">Shadowing: escucha cada frase y repítela en voz alta en la pausa, imitando el ritmo. Es el mejor ejercicio para la pronunciación.</p>}

      <div className="row-gap reading-controls">
        {!playing ? (
          <button type="button" className="btn btn--primary" onClick={playAll}>▶ {mode === 'shadow' ? 'Escuchar y repetir' : 'Escuchar todo'}</button>
        ) : (
          <button type="button" className="btn btn--ghost" onClick={stop}>⏹ Detener</button>
        )}
      </div>

      <div className="reading-text">
        {reading.sentences.map((s, i) => (
          <div key={i} className={`reading-line ${active === i ? 'is-active' : ''} ${s.who ? 'reading-line--dialogue' : ''}`}>
            {s.who && <span className="bubble__who">{s.who}</span>}
            <p>
              <EnglishText text={s.en} /> <SpeakButton text={s.en} speaker={s.who} natural />
            </p>
            {mode === 'read' && <Spanish text={s.es} />}
          </div>
        ))}
      </div>

      {reading.questions && reading.questions.length > 0 && (
        <section className="reading-quiz">
          {!showQuestions ? (
            <button type="button" className="btn btn--ghost" onClick={() => setShowQuestions(true)}>¿Entendiste? Responde unas preguntas</button>
          ) : (
            <Comprehension reading={reading} />
          )}
        </section>
      )}
    </div>
  );
}

function Comprehension({ reading }: { reading: Reading }) {
  const [picked, setPicked] = useState<Record<number, number>>({});
  return (
    <div className="comprehension">
      <h2>Comprensión</h2>
      {reading.questions!.map((q, qi) => (
        <div key={qi} className="step">
          <p className="step__title">{q.q}</p>
          <div className="options options--list">
            {q.options.map((o, oi) => {
              const chosen = picked[qi];
              const cls = chosen === undefined ? 'option option--wide'
                : oi === q.answer ? 'option option--wide option--right'
                : chosen === oi ? 'option option--wide option--wrong' : 'option option--wide';
              return (
                <button key={oi} type="button" className={cls} disabled={chosen !== undefined} onClick={() => setPicked((p) => ({ ...p, [qi]: oi }))}>
                  {o}
                </button>
              );
            })}
          </div>
        </div>
      ))}
    </div>
  );
}
