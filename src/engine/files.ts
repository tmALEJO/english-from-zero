import { Directory, Encoding, Filesystem } from '@capacitor/filesystem';
import { Share } from '@capacitor/share';
import { isNative } from './speech';

/** Guarda un archivo de texto: descarga en el PC, menú "Compartir" en Android (Drive, WhatsApp, Archivos…). */
export async function saveTextFile(filename: string, content: string): Promise<string> {
  if (isNative) {
    const res = await Filesystem.writeFile({ path: filename, data: content, directory: Directory.Cache, encoding: Encoding.UTF8 });
    await Share.share({ title: 'Progreso de English from Zero', files: [res.uri], dialogTitle: 'Guardar o enviar tu progreso' });
    return 'Elige dónde guardar o a quién enviar el archivo.';
  }
  const blob = new Blob([content], { type: 'application/json' });
  const url = URL.createObjectURL(blob);
  const a = document.createElement('a');
  a.href = url;
  a.download = filename;
  document.body.appendChild(a);
  a.click();
  a.remove();
  setTimeout(() => URL.revokeObjectURL(url), 2000);
  return `Se descargó ${filename}. Búscalo en tu carpeta de Descargas.`;
}

export function readFileAsText(file: File): Promise<string> {
  return new Promise((resolve, reject) => {
    const r = new FileReader();
    r.onload = () => resolve(String(r.result));
    r.onerror = () => reject(new Error('No se pudo leer el archivo.'));
    r.readAsText(file);
  });
}
