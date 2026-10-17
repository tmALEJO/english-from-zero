# English from Zero 🇬🇧

App para aprender inglés **desde cero absoluto** (para hispanohablantes), paso a paso y basada en la ciencia de la adquisición de lenguas. Funciona **en el PC** (se abre en tu navegador, todo local) y **en Android** (APK que descargas desde GitHub Releases).

**100 % gratis y offline**: no usa APIs de pago, ni cuentas, ni servidores. Tu progreso vive en tu dispositivo y lo pasas entre PC y celular con un archivo o un código QR.

---

## Cómo enseña

| Principio | Cómo lo aplica la app |
|---|---|
| **Input comprensible primero** | Cada tema empieza escuchando y leyendo (diálogos, historias cortas). Hablar llega después y **siempre es opcional** ("Ahora no"). |
| **Carga cognitiva baja** | Máximo **4 palabras o frases nuevas por lección**. El resto es reciclaje: calentamiento con repaso al inicio de cada lección. |
| **Repetición espaciada y variada** | Algoritmo **FSRS**: cada palabra vuelve justo antes de que la olvides (≈ 3 días → 2 semanas → 2 meses…), y **cada vez en un ejercicio distinto** (escuchar, leer, imagen, armar frase). |
| **Gramática inductiva** | Nada de tablas al principio. Ves muchos ejemplos (*I work / she works*), descubres el patrón respondiendo una pregunta, y **solo al final** aparece el nombre: "Acabas de aprender: Presente simple". |
| **Corrección amable** | Si fallas: te muestra la forma correcta, te deja intentar otra vez y el ejercicio vuelve al final de la sesión. Nunca te bloquea. |
| **Imagen y contexto antes que traducción** | Imágenes (emoji) y audio primero. El español está **oculto hasta que lo tocas** (se puede cambiar en Ajustes). |
| **Logros de competencia** | En vez de monedas: "🏅 Ya puedo pedir comida en un restaurante". Tu nivel se mide en MCER: A0 → A1 → A2 → B1 → B2 → C1. |
| **Sin fricción** | Diccionario integrado (toca cualquier palabra de una historia o ábrelo con 📖 en plena lección), repaso, práctica libre e historial en la misma app. |

**Pronunciación pensada para hispanohablantes**: pares mínimos (*ship/sheep*, *boat/vote*, *three/tree*, *they/day*), la "S sin E" (*school*, no *eschool*) y una guía "suena como" en cada palabra.

### Qué incluye hoy

- **Ruta completa A0 → C1** con 39 temas y su hito "Ya puedo…".
- **8 unidades con contenido completo** (30 lecciones, 116 palabras y frases): Sonidos del inglés · Hola y adiós · Me presento (*to be*) · Números y precios · Colores y cosas (*a/an*, adjetivo antes del sustantivo) · Mi familia (*to be* completo, *his/her*) · En el restaurante (*I'd like…*) · Mi día (**presente simple**).
- El resto de la ruta aparece como "Próximamente": se agrega contenido sin tocar código (ver [docs/CONTENIDO.md](docs/CONTENIDO.md)).

### Funciones

- **Hoy**: la siguiente lección sugerida, tus repasos pendientes y tu nivel.
- **Ruta**: unidades en orden; se desbloquean al terminar la anterior. Las terminadas **siempre se pueden repetir**. (Ajustes → *Modo explorador* abre todo.)
- **Repaso**: repaso del día (espaciado), **Mis difíciles**, y **práctica libre por tema o por palabra** (no altera tu calendario).
- **Diccionario**: búsqueda en inglés o español, audio, pronunciación aproximada, ejemplos, cuándo vuelve cada palabra y botón "Practicar esta palabra".
- **Progreso**: nivel MCER, logros "Ya puedo…", estadísticas e **historial** de cada sesión.
- **Exportar / importar**: archivo `.json` o **códigos QR** (se divide en varios si hace falta). Al importar puedes **combinar** (se queda con lo más reciente de cada palabra, no pierde nada) o **reemplazar**.
- Voz en inglés (normal y 🐢 lenta) y reconocimiento de voz para los ejercicios opcionales de hablar.
- Modo oscuro automático, funciona con teclado y respeta "reducir movimiento".

---

## 1. Usarla en el PC (Windows)

### Lo que necesitas instalar (una sola vez)

1. **Node.js LTS** → https://nodejs.org (siguiente, siguiente, finalizar).
2. **Git** → https://git-scm.com (para clonar y subir a GitHub).
3. **Visual Studio Code** → https://code.visualstudio.com
4. *(Opcional)* **Python 3** → https://python.org (solo para validar contenido, generar audio o crear la clave del APK).
5. Navegador **Google Chrome** o **Microsoft Edge** (el reconocimiento de voz no funciona en Firefox).

### Arrancar

**Doble clic en `iniciar.bat`.**

La primera vez instala las dependencias (1–3 minutos, necesita internet). Luego abre la app en tu navegador en `http://localhost:5173`. Las siguientes veces abre en segundos. Para cerrarla, cierra la ventana negra.

> En Linux/macOS: `./iniciar.sh`.

### Desde VS Code (si vas a programar)

```bash
npm install        # dependencias (solo la primera vez)
npm run dev        # servidor local con recarga automática
npm test           # pruebas del motor (repaso, niveles, exportar/importar)
npm run build      # compila a la carpeta dist/
python scripts/validate_content.py   # revisa el contenido
```

---

## 2. Usarla en Android (APK desde GitHub Releases)

No necesitas Android Studio: **GitHub compila el APK por ti**, gratis.

### Subir el proyecto a GitHub (una sola vez)

1. Crea un repositorio vacío en GitHub, por ejemplo `english-from-zero`.
2. En la carpeta del proyecto (terminal de VS Code):
   ```bash
   git init
   git add .
   git commit -m "Primera versión"
   git branch -M main
   git remote add origin https://github.com/THEBAT02468/english-from-zero.git
   git push -u origin main
   ```

### Firmar el APK (una sola vez, muy recomendado)

Android solo instala una actualización encima de la anterior si ambas tienen **la misma firma**. Sin esto, para actualizar tendrías que desinstalar y perderías el progreso (salvo que lo exportes antes).

```bash
pip install cryptography
python scripts/crear_keystore.py
```

Te muestra dos valores. En GitHub ve a **Settings → Secrets and variables → Actions → New repository secret** y crea:

| Nombre | Valor |
|---|---|
| `KEYSTORE_BASE64` | todo el contenido de `keystore-base64.txt` |
| `KEYSTORE_PASSWORD` | la contraseña que mostró el script |

Guarda `release.p12` y la contraseña en un lugar seguro y borra `keystore-base64.txt`. Ninguno de los dos se sube a GitHub (están en `.gitignore`).

### Publicar una versión

```bash
git tag v0.1.0
git push origin v0.1.0
```

En la pestaña **Actions** verás "Compilar APK" (tarda unos 5–8 minutos). Al terminar, el APK aparece en **Releases** del repositorio.

> También puedes lanzarlo a mano: **Actions → Compilar APK → Run workflow**. En ese caso el APK queda en *Artifacts* de esa ejecución.

### Instalar en el celular

1. Abre la página de **Releases** desde el celular y descarga `english-from-zero-v0.1.0.apk`.
2. Ábrelo. Si Android lo pide, permite **"Instalar apps desconocidas"** para tu navegador o gestor de archivos.
3. Para actualizar: publica una etiqueta nueva (`v0.2.0`) e instala el APK nuevo encima. Tu progreso se conserva.

La primera vez que hagas un ejercicio de hablar, Android pedirá permiso de micrófono; para escanear el QR, permiso de cámara.

---

## 3. Pasar el progreso entre PC y celular

**Progreso → Exportar / importar**

- **Archivo**: en el PC se descarga un `.json`; en Android se abre el menú *Compartir* (Drive, WhatsApp, Archivos…). En el otro dispositivo, *Elegir archivo .json*.
- **QR**: pulsa *Mostrar código QR* en un dispositivo y *Escanear código QR* en el otro. Si el progreso es grande, se muestran varios códigos que cambian solos; el escáner los junta.
- **Combinar** (recomendado) une ambos lados quedándose con lo más reciente de cada palabra. **Reemplazar** deja solo lo de la copia.

---

## 4. Audio de alta calidad (opcional)

Sin hacer nada, la app usa la voz del sistema (Chrome/Edge en el PC, el motor de voz de Android en el celular). Para que todo suene con una **voz natural e igual en todos los dispositivos**, genera el audio offline con [Piper](https://github.com/rhasspy/piper) (gratis, open source). Corre esto **en tu PC** (la primera vez baja la voz, ~60 MB, necesita internet):

```bash
pip install piper-tts
python scripts/generate_audio.py            # todo el contenido
# o, para un audio más liviano (solo vocabulario):
python scripts/generate_audio.py --scope items
```

Crea `public/audio/` con un archivo por frase y un `manifest.json` que la app detecta sola. Instala **ffmpeg** para que los guarde en MP3 (mucho más livianos que WAV). Vuelve a ejecutarlo cuando agregues contenido.

**Decisión de tamaño.** El audio se suma al APK: `--scope all` puede pesar ~80–150 MB; `--scope items` cubre todas las palabras del vocabulario y queda mucho más liviano (el resto usa la voz del sistema). Si **no** quieres audio dentro del APK, agrega `public/audio/` a `.gitignore` antes del commit: la app seguirá hablando con la voz del sistema.

Después de generarlo: `git add public/audio`, commit, push y una etiqueta nueva (`v0.4.0`) para que el APK lo incluya.

---

## Estructura del proyecto

```
english-from-zero/
├── iniciar.bat / iniciar.sh     ← doble clic y listo
├── content/                     ← EL CONTENIDO (datos, no código)
│   ├── curriculum.json          ← niveles A0–C1 y orden de las 39 unidades
│   ├── dictionary.json          ← palabras extra del diccionario
│   └── units/*.json             ← una unidad por archivo (ítems + lecciones)
├── src/
│   ├── engine/                  ← lógica pura, probada en tests/
│   │   ├── content.ts           ← carga unidades y arma el diccionario
│   │   ├── steps.ts             ← convierte lecciones en ejercicios
│   │   ├── srs.ts               ← repetición espaciada (FSRS)
│   │   ├── progress.ts          ← desbloqueo, niveles, repaso, práctica
│   │   ├── backup.ts            ← exportar / importar / QR
│   │   ├── speech.ts            ← voz (Piper, navegador o Android)
│   │   └── text.ts              ← comparación de pronunciación
│   ├── db/                      ← IndexedDB (Dexie): progreso e historial
│   ├── components/              ← ejercicios, diccionario lateral…
│   └── pages/                   ← Hoy, Ruta, Unidad, Sesión, Repaso…
├── scripts/                     ← Python: validar contenido, audio, clave del APK
├── android/                     ← proyecto Android generado por Capacitor
├── tests/                       ← pruebas (Vitest)
└── .github/workflows/           ← pruebas + compilación del APK
```

**Tecnologías**: React 19 + TypeScript + Vite · Capacitor 7 (Android) · Dexie (IndexedDB) · ts-fsrs · qrcode / html5-qrcode · Piper TTS (opcional) · Atkinson Hyperlegible (tipografía diseñada para legibilidad).

## Preguntas frecuentes

**"No escucho la voz."** En el PC usa Chrome o Edge y revisa que el volumen de la pestaña no esté silenciado. En Android, revisa en *Ajustes del sistema → Texto a voz* que haya un motor instalado (Google).

**"El micrófono no funciona en el PC."** El reconocimiento de voz de Chrome necesita internet y permiso de micrófono (candado junto a la dirección). Los ejercicios de hablar son opcionales: puedes pulsar "Ahora no".

**"¿Se borra mi progreso si cierro la app?"** No. Se guarda en el navegador (o en la app Android). Se borra solo si limpias los datos del navegador, desinstalas la app o usas *Ajustes → Borrar mi progreso*. Exporta una copia de vez en cuando.

**"Quiero agregar más lecciones."** Lee [docs/CONTENIDO.md](docs/CONTENIDO.md).

## Licencia

MIT © Santiago David López Villota ([@THEBAT02468](https://github.com/THEBAT02468))
