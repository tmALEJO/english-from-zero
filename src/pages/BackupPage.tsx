import { useEffect, useRef, useState } from 'react';
import { Link } from 'react-router-dom';
import QRCode from 'qrcode';
import { exportBackup, importBackup } from '../db/actions';
import { fromQrParts, parseBackup, parseQrPart, toQrChunks, type Backup, type QrPart } from '../engine/backup';
import { readFileAsText, saveTextFile } from '../engine/files';
import { Page } from '../components/common';

type Mode = 'merge' | 'replace';

export default function BackupPage() {
  const [msg, setMsg] = useState<{ ok: boolean; text: string } | null>(null);
  const [mode, setMode] = useState<Mode>('merge');
  const [qr, setQr] = useState<string[] | null>(null);
  const [scanning, setScanning] = useState(false);
  const fileRef = useRef<HTMLInputElement>(null);

  const doImport = async (b: Backup) => {
    const s = await importBackup(b, mode);
    setMsg({ ok: true, text: `Listo. Se importó la copia de ${b.device} (${new Date(b.exportedAt).toLocaleString('es-CO')}): ${s.cardsAdded} palabras nuevas, ${s.cardsUpdated} actualizadas y ${s.lessonsAdded} lecciones.` });
  };

  const exportFile = async () => {
    const b = await exportBackup();
    const name = `english-progreso-${new Date().toISOString().slice(0, 10)}.json`;
    setMsg({ ok: true, text: await saveTextFile(name, JSON.stringify(b, null, 1)) });
  };

  const importFile = async (f: File) => {
    try { await doImport(parseBackup(JSON.parse(await readFileAsText(f)))); }
    catch (e) { setMsg({ ok: false, text: e instanceof SyntaxError ? 'El archivo no es un JSON válido.' : (e as Error).message }); }
  };

  return (
    <Page title="Exportar e importar progreso" intro="Lleva tu avance del PC al celular y al revés. Exporta en un dispositivo e importa en el otro." actions={<Link to="/progreso" className="btn btn--ghost btn--sm">Volver</Link>}>
      {msg && <p className={`notice ${msg.ok ? '' : 'notice--fix'}`} role="status">{msg.text}</p>}

      <section className="backup">
        <h2>Exportar</h2>
        <div className="row-gap">
          <button type="button" className="btn btn--primary" onClick={exportFile}>Guardar archivo .json</button>
          <button type="button" className="btn btn--ghost" onClick={async () => setQr(toQrChunks(await exportBackup()))}>Mostrar código QR</button>
        </div>
        <p className="muted">El archivo lleva todo, incluido el historial completo. El QR lleva tu progreso y las últimas 30 sesiones del historial.</p>
        {qr && <QrCarousel chunks={qr} onClose={() => setQr(null)} />}
      </section>

      <section className="backup">
        <h2>Importar</h2>
        <fieldset className="field">
          <legend>¿Qué hago con lo que ya hay en este dispositivo?</legend>
          <label className="check"><input type="radio" checked={mode === 'merge'} onChange={() => setMode('merge')} /> Combinar (recomendado): se queda con lo más reciente de cada palabra y no pierde nada</label>
          <label className="check"><input type="radio" checked={mode === 'replace'} onChange={() => setMode('replace')} /> Reemplazar: borra lo de aquí y deja solo la copia</label>
        </fieldset>
        <div className="row-gap">
          <button type="button" className="btn btn--primary" onClick={() => fileRef.current?.click()}>Elegir archivo .json</button>
          <button type="button" className="btn btn--ghost" onClick={() => setScanning(true)}>Escanear código QR</button>
        </div>
        <input ref={fileRef} type="file" accept="application/json,.json" hidden onChange={(e) => { const f = e.target.files?.[0]; if (f) void importFile(f); e.target.value = ''; }} />
        {scanning && (
          <QrScanner
            onClose={() => setScanning(false)}
            onDone={async (b) => { setScanning(false); await doImport(b); }}
            onError={(t) => setMsg({ ok: false, text: t })}
          />
        )}
      </section>
    </Page>
  );
}

/** Muestra las partes del QR una tras otra. El otro dispositivo las va juntando. */
function QrCarousel({ chunks, onClose }: { chunks: string[]; onClose: () => void }) {
  const [i, setI] = useState(0);
  const [img, setImg] = useState('');
  const [auto, setAuto] = useState(chunks.length > 1);
  useEffect(() => {
    QRCode.toDataURL(chunks[i], { errorCorrectionLevel: 'M', margin: 2, width: 360 }).then(setImg);
  }, [chunks, i]);
  useEffect(() => {
    if (!auto) return;
    const t = setInterval(() => setI((x) => (x + 1) % chunks.length), 1800);
    return () => clearInterval(t);
  }, [auto, chunks.length]);
  return (
    <div className="qr">
      {img && <img src={img} alt={`Código QR ${i + 1} de ${chunks.length}`} width={300} height={300} />}
      <p><b>Código {i + 1} de {chunks.length}</b></p>
      {chunks.length > 1 && <p className="muted">Los códigos cambian solos. Apunta la cámara del otro dispositivo hasta que diga que los tiene todos.</p>}
      <div className="row-gap">
        {chunks.length > 1 && <button type="button" className="btn btn--ghost btn--sm" onClick={() => setAuto(!auto)}>{auto ? 'Pausar' : 'Pasar solos'}</button>}
        {chunks.length > 1 && !auto && <button type="button" className="btn btn--ghost btn--sm" onClick={() => setI((i + 1) % chunks.length)}>Siguiente</button>}
        <button type="button" className="btn btn--ghost btn--sm" onClick={onClose}>Cerrar</button>
      </div>
    </div>
  );
}

function QrScanner({ onDone, onClose, onError }: { onDone: (b: Backup) => void; onClose: () => void; onError: (t: string) => void }) {
  const [parts, setParts] = useState<Map<number, QrPart>>(new Map());
  const [total, setTotal] = useState(0);
  const idRef = useRef<string | null>(null);
  const finished = useRef(false);

  useEffect(() => {
    let scanner: { stop: () => Promise<void>; clear: () => void } | null = null;
    let alive = true;
    (async () => {
      const { Html5Qrcode } = await import('html5-qrcode');
      if (!alive) return;
      const s = new Html5Qrcode('qr-reader');
      scanner = s as never;
      try {
        await s.start(
          { facingMode: 'environment' },
          { fps: 10, qrbox: 260 },
          (text) => {
            if (finished.current) return;
            const p = parseQrPart(text);
            if (!p) return;
            if (idRef.current && idRef.current !== p.id) return; // ignora códigos de otra exportación
            idRef.current = p.id;
            setTotal(p.total);
            setParts((prev) => {
              if (prev.has(p.index)) return prev;
              const next = new Map(prev).set(p.index, p);
              if (next.size === p.total && !finished.current) {
                finished.current = true;
                try { onDone(fromQrParts([...next.values()])); } catch (e) { onError((e as Error).message); }
              }
              return next;
            });
          },
          () => undefined,
        );
      } catch {
        onError('No pude abrir la cámara. Revisa el permiso de cámara o usa la opción de archivo.');
        onClose();
      }
    })();
    return () => {
      alive = false;
      scanner?.stop().then(() => scanner?.clear()).catch(() => undefined);
    };
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, []);

  return (
    <div className="qr">
      <div id="qr-reader" className="qr__reader" />
      <p>{total ? `Leídos ${parts.size} de ${total} códigos` : 'Apunta al código QR del otro dispositivo'}</p>
      <button type="button" className="btn btn--ghost btn--sm" onClick={onClose}>Cancelar</button>
    </div>
  );
}
