# Cómo agregar contenido

Todo el contenido son archivos JSON en `content/`. Para agregar una unidad no hay que tocar código.

## 1. Crear la unidad

1. Copia una unidad parecida de `content/units/` (por ejemplo `u07-mi-dia.json`).
2. Renómbrala con el id de `curriculum.json`, por ejemplo `u08-preguntas.json`. **El campo `id` del archivo debe ser igual al nombre.**
3. En `content/curriculum.json` cambia esa unidad de `"status": "planned"` a `"status": "ready"`.
4. Revisa: `python scripts/validate_content.py` y luego `npm run dev`.

## 2. Partes de una unidad

```jsonc
{
  "id": "u08-preguntas",
  "level": "A1",
  "title": "Haciendo preguntas",
  "emoji": "❓",
  "canDo": "Ya puedo hacer preguntas sobre la rutina de otros",   // el logro que se celebra
  "summary": "Texto corto que aparece arriba de la unidad.",
  "grammar": ["Do / Does"],
  "items": [ /* palabras y frases que se aprenden y repasan */ ],
  "lessons": [ /* lecciones */ ]
}
```

### Ítems

```jsonc
{
  "id": "u08.doyou",            // único en toda la app: <unidad>.<nombre>
  "en": "Do you work?",
  "es": "¿Trabajas?",
  "kind": "chunk",              // word | chunk (frase hecha) | sound
  "emoji": "💼",                // la "imagen". Ayuda a no depender de la traducción
  "say": "du iu uérk",          // pronunciación aproximada para hispanohablantes
  "tip": "Consejo corto.",
  "forms": ["do"],              // formas que también abren esta entrada en el diccionario
  "examples": [{ "en": "...", "es": "..." }]
}
```

### Lecciones

```jsonc
{
  "id": "u08-l1",
  "title": "¿Trabajas?",
  "focus": "listening",         // listening | reading | pronunciation | grammar | speaking | vocabulary
  "newItems": ["u08.doyou"],    // MÁXIMO 4. Entran al repaso espaciado al terminar la lección
  "activities": [ ... ]
}
```

## 3. Tipos de actividad

| type | Para qué | Campos |
|---|---|---|
| `present` | Presentar ítems nuevos (imagen + audio + pronunciación) | `items`, `note?` |
| `auto` | El motor genera ejercicios variados de esos ítems | `items`, `modes` (`listen-pick`, `read-pick`, `picture-pick`, `build`, `speak`), `count?` |
| `dialogue` | Conversación para escuchar (input) | `title`, `scene?`, `lines[{who,en,es}]` |
| `story` | Historia corta con palabras tocables + preguntas | `title`, `emoji?`, `paragraphs[{en,es}]`, `questions?[{q,options,answer}]` |
| `discover` | **Gramática inductiva**: ejemplos → pregunta → regla | `topic`, `intro`, `examples[{en,es,mark?}]`, `question`, `options`, `answer`, `rule`, `ruleExamples?` |
| `fill` | Completar el hueco `___` | `en`, `es?`, `options`, `answer`, `explain?` |
| `build` | Ordenar fichas para armar la frase | `en`, `es`, `distractors?` |
| `minimal-pair` | Distinguir sonidos parecidos | `title?`, `pairs[{a,b,aHint?,bHint?,play:'a'|'b'}]` |
| `speak` | Hablar (siempre opcional) | `en`, `es`, `note?` |
| `tip` | Nota breve | `title`, `text`, `emoji?` |

## 4. Reglas de diseño (las mismas de la app)

- **Input antes que producción**: dentro de una unidad, primero `present`/`dialogue`/`story`, luego ejercicios, y `speak` al final.
- **Gramática**: nunca empieces por la regla. Usa `discover` con 4–7 ejemplos marcados (`mark`) y deja que el nombre técnico (`topic`) aparezca solo al final.
- **Recicla**: en `auto` y en historias usa ítems de unidades anteriores. Solo `newItems` cuenta como nuevo.
- **Una habilidad por actividad**: si la actividad es de pronunciación, no corrijas gramática ahí.
- **Diccionario**: toda palabra de historias, diálogos y ejemplos debería poder tocarse. El validador avisa qué palabras faltan; agrégalas en `content/dictionary.json` o como `forms` de un ítem.

Después de agregar contenido, si usas audio Piper: `python scripts/generate_audio.py`.
