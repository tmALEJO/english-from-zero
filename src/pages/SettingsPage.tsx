import { useEffect, useState } from 'react';
import { Link } from 'react-router-dom';
import { useApp } from '../state';
import { listVoices, speak } from '../engine/speech';
import { resetAll } from '../db/actions';
import { Page } from '../components/common';

export default function SettingsPage() {
  const { settings, updateSettings } = useApp();
  const [voices, setVoices] = useState<{ name: string; lang: string }[]>([]);
  useEffect(() => { listVoices().then(setVoices).catch(() => setVoices([])); }, []);

  return (
    <Page title="Ajustes" actions={<Link to="/progreso" className="btn btn--ghost btn--sm">Volver</Link>}>
      <form className="settings" onSubmit={(e) => e.preventDefault()}>
        <label className="field">
          <span>Tu nombre (opcional)</span>
          <input className="input" value={settings.learnerName} onChange={(e) => updateSettings({ learnerName: e.target.value })} />
        </label>

        <fieldset className="field">
          <legend>Traducción al español</legend>
          <label className="check"><input type="radio" checked={settings.showSpanish === 'tap'} onChange={() => updateSettings({ showSpanish: 'tap' })} /> Oculta hasta que la toque (recomendado)</label>
          <label className="check"><input type="radio" checked={settings.showSpanish === 'always'} onChange={() => updateSettings({ showSpanish: 'always' })} /> Siempre visible</label>
          <p className="muted">Ocultarla te obliga a entender por la imagen y el contexto primero, que es como mejor se aprende.</p>
        </fieldset>

        <label className="field">
          <span>Velocidad de la voz: {settings.voiceRate.toFixed(2)}</span>
          <input type="range" min={0.5} max={1.1} step={0.05} value={settings.voiceRate} onChange={(e) => updateSettings({ voiceRate: Number(e.target.value) })} />
        </label>

        {voices.length > 0 && (
          <label className="field">
            <span>Voz en inglés</span>
            <select className="input" value={settings.voiceName} onChange={(e) => updateSettings({ voiceName: e.target.value })}>
              <option value="">Automática</option>
              {voices.map((v) => <option key={v.name} value={v.name}>{v.name} ({v.lang})</option>)}
            </select>
            <button type="button" className="btn btn--ghost btn--sm" onClick={() => speak('Hello! Nice to meet you.', { rate: settings.voiceRate, voiceName: settings.voiceName })}>Probar voz</button>
          </label>
        )}

        <label className="check">
          <input type="checkbox" checked={settings.speakingEnabled} onChange={(e) => updateSettings({ speakingEnabled: e.target.checked })} />
          Incluir ejercicios de hablar (siempre son opcionales)
        </label>

        <label className="field">
          <span>Tarjetas por repaso: {settings.reviewSize}</span>
          <input type="range" min={5} max={40} step={5} value={settings.reviewSize} onChange={(e) => updateSettings({ reviewSize: Number(e.target.value) })} />
        </label>

        <label className="field">
          <span>Calentamiento al inicio de cada lección: {settings.warmupSize} ejercicios</span>
          <input type="range" min={0} max={6} step={1} value={settings.warmupSize} onChange={(e) => updateSettings({ warmupSize: Number(e.target.value) })} />
        </label>

        <label className="check">
          <input type="checkbox" checked={settings.explorerMode} onChange={(e) => updateSettings({ explorerMode: e.target.checked })} />
          Modo explorador: abrir todas las unidades sin seguir el orden
        </label>

        <div className="danger">
          <h2>Borrar todo</h2>
          <p className="muted">Elimina tu progreso de este dispositivo. Exporta una copia antes si quieres conservarlo.</p>
          <button
            type="button"
            className="btn btn--danger"
            onClick={async () => {
              if (confirm('¿Borrar todo tu progreso de este dispositivo? No se puede deshacer.')) { await resetAll(); location.hash = '#/'; }
            }}
          >
            Borrar mi progreso
          </button>
        </div>
      </form>
    </Page>
  );
}
