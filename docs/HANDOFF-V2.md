# English from Zero — Documento de traspaso (para continuar en un chat nuevo)

> **Cómo usar este documento:** pégalo completo al inicio de un chat nuevo con un asistente (sin memoria del proyecto). Junto con el `README.md` y `docs/CONTENIDO.md` del repo, le da todo el contexto para seguir trabajando sin romper nada. Al final hay una lista de tareas para la **v2**, empezando por el **ejercicio de conjugación de verbos**.

---

## 0. Instrucción para el asistente que lea esto

Eres un equipo senior (arquitecto full-stack + diseñador instruccional de segundas lenguas + UX). Vas a continuar una app ya existente y funcionando, **no empezar de cero**. Antes de tocar nada:
1. Lee también el `README.md` y `docs/CONTENIDO.md` del proyecto.
2. Respeta la metodología y la arquitectura descritas aquí.
3. Todo debe ser **gratis y offline** (sin APIs de pago).
4. Cada cambio: compila contenido si aplica, corre `validate_content.py`, `npm test` y `npm run build` antes de dar algo por hecho.
5. El usuario trabaja en Windows con VS Code y sube a GitHub; las entregas se le pasan como archivos a reemplazar + comandos de git. Nunca le hagas crear un proyecto nuevo.

El usuario se llama TheBat (GitHub: THEBAT02468, repo `english-from-zero`). Habla español. Es desarrollador, entiende bien lo técnico, pero quiere pasos claros.

---

## 1. Qué es la app

Curso completo de inglés **de cero absoluto (A0) a avanzado (C1)** para hispanohablantes. Funciona como **web local en el PC** (se abre en el navegador) y como **APK de Android** (mismo código, empaquetado con Capacitor). 100% gratis, offline, sin cuentas ni servidores. El progreso vive en el dispositivo y se pasa entre PC y celular por archivo o QR.

**Estado actual (v0.5.0):** 107 unidades, ~1.002 lecciones, 19 exámenes, ~3.779 entradas de vocabulario (≈2.093 palabras sueltas + ≈1.686 frases/chunks), A0→C1. Imágenes OpenMoji incluidas. Audio Piper opcional (el usuario ya lo generó con `--scope items`).

### Metodología (no negociable)
- **Input comprensible primero:** escuchar y leer antes de producir; hablar es siempre opcional.
- **Carga cognitiva baja:** máximo 4 palabras nuevas por lección; el resto es reciclaje.
- **Repetición espaciada y variada:** cada ítem vuelve en días distintos y en modos distintos (escuchar, imagen, leer, armar, dictado) — algoritmo FSRS.
- **Gramática inductiva:** muchos ejemplos → el usuario descubre el patrón → recién al final aparece el nombre del tema.
- **Corrección amable:** muestra la forma correcta, deja reintentar, no bloquea.
- **Imagen y contexto antes que traducción:** el español está oculto hasta que se toca.
- **Hitos de competencia:** "Ya puedo pedir comida", niveles MCER A0→C1.

---

## 2. Stack técnico

- **UI:** React 19 + TypeScript + Vite 7. Una sola base para PC y Android.
- **Android:** Capacitor 7 (`android/` generado). APK compilado en GitHub Actions.
- **Base de datos local:** Dexie (IndexedDB). Progreso, historial, ajustes.
- **Repetición espaciada:** `ts-fsrs`.
- **QR:** `qrcode` (generar) + `html5-qrcode` (escanear) para exportar/importar progreso.
- **Imágenes:** OpenMoji (SVG) en `public/openmoji/`, con respaldo al emoji del sistema.
- **Voz:** audio pregenerado con **Piper** (opcional, en `public/audio/` + `manifest.json`); si no existe, usa la voz del sistema (Web Speech en PC, TTS nativo en Android).
- **Tipografía:** Atkinson Hyperlegible (legibilidad).

---

## 3. Estructura del proyecto

```
english-from-zero/
├── iniciar.bat / iniciar.sh        ← lanzador (doble clic en PC)
├── content/                        ← EL CONTENIDO
│   ├── src/*.py                    ← fuente compacta (se compila) — AQUÍ se escribe contenido nuevo
│   ├── units/*.json                ← unidades compiladas (NO editar a mano las generadas)
│   │                                 u00–u07 son hechas a mano (JSON) y se respetan tal cual
│   ├── curriculum.json             ← niveles, orden de unidades y exámenes (GENERADO)
│   ├── library.json                ← lecturas de la biblioteca (GENERADO desde src/library.py)
│   └── dictionary.json             ← palabras extra solo-diccionario (hecho a mano)
├── public/
│   ├── openmoji/*.svg              ← imágenes (generadas por scripts/build_images.py)
│   └── audio/                      ← MP3 de Piper + manifest.json (opcional, scripts/generate_audio.py)
├── scripts/                        ← Python
│   ├── build_content.py            ← compila content/src/*.py → JSON (npm run content:build)
│   ├── validate_content.py         ← valida el contenido
│   ├── build_images.py             ← copia SVG de OpenMoji según los emojis usados
│   ├── generate_audio.py           ← genera voz con Piper
│   └── crear_keystore.py           ← crea la clave de firma del APK (una vez)
├── src/
│   ├── types.ts                    ← tipos: Item, Activity, Step, etc.
│   ├── engine/                     ← lógica pura (probada en tests/)
│   │   ├── content.ts              ← carga unidades + diccionario
│   │   ├── steps.ts                ← convierte lecciones en ejercicios (Step[])
│   │   ├── srs.ts                  ← repetición espaciada (FSRS)
│   │   ├── progress.ts             ← desbloqueo, niveles, repaso, exámenes
│   │   ├── backup.ts               ← exportar/importar (archivo + QR)
│   │   ├── speech.ts               ← voz (Piper / navegador / Android)
│   │   └── text.ts                 ← normalización, checkSpeech, checkTyped
│   ├── db/                         ← Dexie + acciones (guardar lección, repaso, etc.)
│   ├── components/                 ← Steps.tsx (ejercicios), DictionaryDrawer, common.tsx (Emoji, etc.)
│   └── pages/                      ← Home, RoutePage, UnitPage, Session, ReviewHub, Library, Dictionary, Progress, Settings, Backup
├── tests/                          ← Vitest
├── android/                        ← Capacitor (generado)
└── .github/workflows/
    ├── build-apk.yml               ← compila el APK al crear un tag vX.Y.Z
    └── ci.yml                      ← pruebas en cada push
```

---

## 4. Cómo funciona el contenido (IMPORTANTE)

El contenido NO se escribe en JSON a mano. Se escribe **compacto** en `content/src/*.py` y el compilador `scripts/build_content.py` arma solo las lecciones, el reciclaje, los exámenes y la prueba de cada unidad.

### Formato de una unidad (en content/src/*.py)
```python
unit("u95-idioms-1", "C1", "Título", "🦉",
     "Ya puedo … (hito de competencia)",
     "Resumen corto de la unidad.",
     grammar=["Tema gramatical"],
     items="""
word | palabra en español | 🔤 | pronunciación-aproximada-opcional
to work | trabajar | 💼 | uérk
How much is this? | ¿Cuánto cuesta esto? | 🏷️
chicken (animal) | pollo (el animal) | 🐔      # el (paréntesis) distingue significado, no se lee
small (A1) | ...                                # (NIVEL) marca repaso de una palabra ya vista: se omite como nueva
""",
     extras=[ ... ])   # actividades especiales, ver abajo
```
- Cada ítem: `inglés | español | emoji | pronunciación?` (los dos últimos son opcionales).
- Las palabras deben ser **únicas** en toda la app; las repetidas se omiten con un aviso (se repasan desde su unidad original). Por eso al reforzar niveles altos conviene vocabulario poco común (idioms, colocaciones, phrasal verbs).
- El compilador agrupa en lecciones de ≤4 nuevas, agrega práctica variada y una lección final de repaso.

### Actividades especiales (extras / helpers disponibles)
- `D(topic, intro, examples, question, options, answer, rule, rule_examples="", fills="")` → gramática inductiva. `examples` y `rule_examples` usan `||` como separador (`inglés || español || palabras_a_resaltar`).
- `dialogue(title, scene, script)` → diálogo (`Quién: inglés || español`).
- `story(title, emoji, text, questions=())` → historia (`inglés || español` por línea) + preguntas `(pregunta, [opciones], índice_correcto)`.
- `roleplay(title, scene, script)` → conversación con opciones del usuario. Líneas con `+` = opción correcta, `-` = incorrecta (`+ inglés || español || por qué`).
- `tip(emoji, title, text)` → nota breve.
- `reading(id, level, title, emoji, kind, summary, text, questions)` → lectura de la biblioteca (`kind`: "story" | "dialogue" | "article").
- También: `writes="..."`, `dictations="..."`, `speak="..."` como parámetros de `unit()`.

### Recompilar
```
python scripts/build_content.py      # o: npm run content:build
python scripts/validate_content.py   # debe decir "Contenido OK"
```

---

## 5. Cómo funciona el motor (engine)

- **Tipos de ejercicio (Step)** en `types.ts`: present, listen-pick, read-pick, picture-pick, build, speak, minimal-pair, fill, dialogue, story, question, discover, tip, **dictation**, **write**, **roleplay**, checkpoint. Los que se califican están en `GRADED`.
- `steps.ts` convierte una lección (datos) en `Step[]`, genera distractores, y arma ejercicios automáticos (`auto`) con modos variados.
- `srs.ts` usa FSRS: cada palabra vuelve justo antes de olvidarse; `nextMode` elige un modo distinto al anterior.
- `progress.ts`: desbloqueo de unidades en orden, niveles MCER, repaso del día, "mis difíciles", práctica libre, exámenes (control cada 6 unidades + final por nivel, con nota para aprobar).
- `text.ts`: `checkSpeech` (inteligibilidad al hablar, tolerante), `checkTyped` (corrige dictado/escritura ignorando mayúsculas/tildes, acepta contracciones, perdona 1 letra en palabras largas).

Para **agregar un tipo de ejercicio nuevo** hay que tocar: `types.ts` (Step + Activity + GRADED), `steps.ts` (generarlo), `components/Steps.tsx` (componente + en el switch de `StepView`), y si viene del contenido, el compilador `build_content.py`. Agregar tests en `tests/engine.test.ts`.

---

## 6. Correr y desplegar

### En el PC
```
npm install          # primera vez
npm run start        # abre la web en el navegador
npm test             # pruebas (Vitest)
npm run build        # compila a dist/
```
O doble clic en `iniciar.bat`.

### Imágenes (si se agregan emojis nuevos)
```
npm i -D openmoji
python scripts/build_images.py
```

### Audio Piper (opcional)
```
pip install piper-tts            # + ffmpeg para MP3 livianos
python scripts/generate_audio.py --scope items   # o sin flag para todo (pesa más)
```

### Subir a GitHub y compilar el APK (flujo que usa el usuario)
El APK se compila **solo** en GitHub Actions al crear una etiqueta de versión.
```
git add .
git commit -m "mensaje"
git push
git tag v0.6.0          # SUBIR LA VERSIÓN cada entrega (v0.5.0 es la actual)
git push origin v0.6.0
```
Luego: pestaña **Actions** → "Compilar APK" en verde → el APK queda en **Releases**. Se instala encima del anterior **sin perder progreso** porque está firmado con la misma clave.

**Firma del APK (ya configurada):** hay una clave (`release.p12`, NO está en el repo, está en `.gitignore`) y dos secretos en GitHub: `KEYSTORE_BASE64` y `KEYSTORE_PASSWORD`. Se crearon con `scripts/crear_keystore.py`. No hay que volver a hacerlo salvo que se pierda la clave (si se pierde, el APK nuevo ya no se instala encima y toca desinstalar).

**Reglas al desplegar:** solo tocar lo necesario; `public/audio` y `release.p12` no van en las entregas (el usuario los conserva local). Confirmar con `git status` que solo cambió lo esperado.

---

## 7. Limitaciones conocidas (lo que falta)

1. **No hay conversación libre para hablar.** Hoy hay pronunciación guiada (micrófono + `checkSpeech`) y roleplay con opciones, pero no una IA que responda. Es la limitación más grande.
2. **No hay drill de conjugación verbo por verbo.** Se enseña la REGLA de cada tiempo (-ed, -s, -ing, irregulares) y el usuario la aplica, pero no se practica cada verbo en todas sus formas. → **Primera tarea de la v2, ver abajo.**
3. **Vocabulario de palabras sueltas** en B2/C1 por debajo del máximo del MCER (se compensa con muchas frases/chunks). Se amplía agregando vocabulario poco común en `content/src/`.
4. **Pocas frases de ejemplo por palabra.** No se garantiza que cada palabra aparezca en 3 frases en tiempos distintos.

---

## 8. Hoja de ruta v2 (en orden sugerido)

### TAREA 1 (prioritaria): Ejercicio de conjugación de verbos
**Objetivo:** que el usuario practique cada verbo en sus formas/tiempos: base, 3ª persona (-s), pasado (-ed o irregular), gerundio (-ing), y opcionalmente futuro (will + base) y present perfect (have + participio).

**Enfoque sugerido (gratis, encaja con lo que existe):**
- **Datos:** la mayoría de las formas regulares se pueden **generar por reglas** (añadir -s/-es, -ed/-d, -ing, con reglas de ortografía: study→studies, stop→stopped, make→making). Para los **irregulares** hace falta una tablita (base, pasado, participio): go/went/gone, etc. Se puede poner en un `content/irregulars.json` o como campo en los ítems (el formato de ítems ya soporta `forms` y etiquetas `past`/`participle` con paréntesis).
- **Motor:** una función `conjugate(verb, tense)` en `engine/` que aplique las reglas regulares y consulte la tabla de irregulares. Con tests en `tests/`.
- **Nuevo tipo de ejercicio** `conjugate`: muestra el verbo base + un tiempo pedido ("pon *work* en pasado") y el usuario **escribe** la forma (reutilizar `checkTyped`) o **elige** entre opciones. Agregarlo a `types.ts` (Step + GRADED), `steps.ts`, `components/Steps.tsx`, y que el compilador pueda inyectarlo en las lecciones de verbos (o generar una "práctica de conjugación" por unidad).
- **UX:** una habilidad por actividad; corrección amable; mostrar la forma correcta y la regla breve si falla.
- **Opcional:** un modo de repaso "Conjugación" en la pestaña Repaso, y detectar verbos entre los ítems existentes para practicarlos.

### TAREA 2: Más frases de ejemplo por palabra / en varios tiempos
Hacer que el motor (o el contenido) presente cada palabra clave en 2–3 frases en contextos y tiempos distintos (get it / got it / getting it). Puede ser un campo de ejemplos más rico o generación automática de frases de práctica variando el tiempo.

### TAREA 3: Conversación libre (hablar de verdad)
Solo en el PC y gratis: integrar un modelo local con **Ollama** (p. ej. Llama o similar) para una práctica de conversación guiada por nivel. En Android no aplica (no hay IA local viable). Dejar claro que esto NO rompe el "todo offline/gratis" si se corre en el PC del usuario.

### TAREA 4: Ampliar vocabulario B2/C1
Agregar unidades en `content/src/` con vocabulario menos común (usar listas libres como NGSL y frases de Tatoeba como guía). Recordar que las palabras repetidas se omiten; priorizar lo que aún no existe.

### TAREA 5 (ideas sueltas)
- Exportar el progreso también a la nube opcional (sigue siendo gratis con límites).
- Estadísticas más ricas (racha, dominio por tema).
- Modo "examen de ubicación" al inicio para saltar niveles.

---

## 9. Checklist antes de entregar cualquier cambio
- [ ] `python scripts/build_content.py` sin ERROR (si tocaste contenido).
- [ ] `python scripts/validate_content.py` → "Contenido OK".
- [ ] `npx tsc -b` sin errores.
- [ ] `npm test` en verde.
- [ ] `npm run build` compila.
- [ ] Si agregaste emojis nuevos: `python scripts/build_images.py`.
- [ ] Entregar archivos a reemplazar + comandos de git + subir versión (nuevo tag).
- [ ] Recordar: nada de APIs de pago; respetar la metodología; no romper el flujo de despliegue.

---

*Versión de partida: v0.5.0. Autor del proyecto: Santiago David López Villota (TheBat / THEBAT02468). Licencia MIT.*
