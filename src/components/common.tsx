import { useEffect, useState, type ReactNode } from 'react';
import { speak } from '../engine/speech';
import { lookupWord } from '../engine/content';
import { useApp } from '../state';

/** Botón de audio. El segundo botón (tortuga) repite más lento. */
export function SpeakButton({ text, auto = false, big = false, label, speaker, natural }: { text: string; auto?: boolean; big?: boolean; label?: string; speaker?: string; natural?: boolean }) {
  const { settings } = useApp();
  const [playing, setPlaying] = useState(false);
  const play = async (rate: number) => {
    setPlaying(true);
    await speak(text, { rate, voiceName: settings.voiceName, speaker, natural });
    setPlaying(false);
  };
  useEffect(() => {
    if (auto) void play(settings.voiceRate);
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [text, auto]);
  return (
    <span className="speak">
      <button
        type="button"
        className={`speak__btn ${big ? 'speak__btn--big' : ''} ${playing ? 'is-playing' : ''}`}
        onClick={() => play(settings.voiceRate)}
        aria-label={label ?? `Escuchar: ${text}`}
      >
        🔊
      </button>
      <button type="button" className="speak__slow" onClick={() => play(Math.max(0.5, settings.voiceRate - 0.3))} aria-label="Escuchar más lento" title="Más lento">
        🐢
      </button>
    </span>
  );
}

/** Texto en inglés donde cada palabra se puede tocar para ver su significado. */
export function EnglishText({ text, mark = [], className = '' }: { text: string; mark?: string[]; className?: string }) {
  const { openDict } = useApp();
  const marks = new Set(mark.map((m) => m.toLowerCase()));
  const parts = text.split(/(\s+)/);
  return (
    <span className={`en ${className}`} lang="en">
      {parts.map((p, i) => {
        if (/^\s+$/.test(p)) return p;
        const m = /^([^A-Za-z']*)([A-Za-z'’]+)([^A-Za-z']*)$/.exec(p);
        if (!m) return <span key={i}>{p}</span>;
        const [, pre, word, post] = m;
        const entry = lookupWord(word);
        const isMark = marks.has(word.toLowerCase());
        return (
          <span key={i}>
            {pre}
            {entry ? (
              <button type="button" className={`word ${isMark ? 'word--mark' : ''}`} onClick={() => openDict({ entry })}>
                {word}
              </button>
            ) : (
              <span className={isMark ? 'word--mark' : ''}>{word}</span>
            )}
            {post}
          </span>
        );
      })}
    </span>
  );
}

/** Traducción en español: oculta hasta que la tocas (o siempre visible, según Ajustes). */
export function Spanish({ text, forceShow = false }: { text: string; forceShow?: boolean }) {
  const { settings } = useApp();
  const [shown, setShown] = useState(settings.showSpanish === 'always' || forceShow);
  useEffect(() => setShown(settings.showSpanish === 'always' || forceShow), [text, settings.showSpanish, forceShow]);
  if (shown) return <span className="es">{text}</span>;
  return (
    <button type="button" className="es es--hidden" onClick={() => setShown(true)}>
      Ver en español
    </button>
  );
}

export function ProgressBar({ value, label }: { value: number; label?: string }) {
  const pct = Math.round(Math.max(0, Math.min(1, value)) * 100);
  return (
    <div className="bar" role="progressbar" aria-valuenow={pct} aria-valuemin={0} aria-valuemax={100} aria-label={label}>
      <div className="bar__fill" style={{ width: `${pct}%` }} />
    </div>
  );
}

export function Page({ title, intro, children, actions }: { title: ReactNode; intro?: ReactNode; children: ReactNode; actions?: ReactNode }) {
  return (
    <div className="page">
      <header className="page__head">
        <div>
          <h1>{title}</h1>
          {intro && <p className="page__intro">{intro}</p>}
        </div>
        {actions}
      </header>
      {children}
    </div>
  );
}

/** Nombre del archivo OpenMoji para un emoji: puntos de código en hex, sin el selector FE0F. */
export function openmojiKey(e: string): string {
  return [...e]
    .filter((c) => c !== '️')
    .map((c) => c.codePointAt(0)!.toString(16).toUpperCase().padStart(4, '0'))
    .join('-');
}

/**
 * Ilustración de un emoji usando OpenMoji (imágenes libres, iguales en PC y Android).
 * Si no existe el SVG, cae al emoji del sistema, así nunca se rompe.
 */
export function Emoji({ e, className = '', label }: { e: string; className?: string; label?: string }) {
  const [failed, setFailed] = useState(false);
  const key = openmojiKey(e);
  if (failed || !key) return <span className={className} role={label ? 'img' : undefined} aria-label={label} aria-hidden={!label}>{e}</span>;
  return (
    <img
      className={`omoji ${className}`}
      src={`./openmoji/${key}.svg`}
      alt={label ?? ''}
      aria-hidden={!label}
      draggable={false}
      loading="lazy"
      onError={() => setFailed(true)}
    />
  );
}

export function Picture({ emoji, fallback, size = 'md' }: { emoji?: string; fallback: string; size?: 'sm' | 'md' | 'lg' | 'xl' }) {
  if (emoji) return <Emoji e={emoji} className={`pic pic--${size}`} />;
  return <span className={`pic pic--text pic--${size}`}>{fallback}</span>;
}

export function formatDate(ms: number): string {
  return new Date(ms).toLocaleDateString('es-CO', { day: 'numeric', month: 'short', hour: '2-digit', minute: '2-digit' });
}
