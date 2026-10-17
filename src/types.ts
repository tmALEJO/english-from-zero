// ─────────────────────────────────────────────────────────────
// Esquema del contenido. Las lecciones son DATOS (JSON en /content),
// así se agregan unidades nuevas sin tocar el código.
// ─────────────────────────────────────────────────────────────

export type LevelId = 'A0' | 'A1' | 'A2' | 'B1' | 'B2' | 'C1';

/** Una palabra, frase hecha (chunk) o sonido que se aprende y se repasa. */
export interface Item {
  id: string;
  en: string;
  es: string;
  kind: 'word' | 'chunk' | 'sound';
  emoji?: string;
  /** Pronunciación aproximada para hispanohablantes, p. ej. "jé-lou". */
  say?: string;
  /** Consejo corto de pronunciación o uso. */
  tip?: string;
  /** Formas que deben llevar a esta entrada en el diccionario (works, worked…). */
  forms?: string[];
  examples?: { en: string; es: string }[];
  tags?: string[];
}

export type Focus = 'listening' | 'reading' | 'pronunciation' | 'grammar' | 'speaking' | 'vocabulary';

/** Modos de práctica que el motor sabe generar automáticamente a partir de un ítem. */
export type AutoMode = 'listen-pick' | 'read-pick' | 'picture-pick' | 'build' | 'speak' | 'dictation';

export type Activity =
  | { type: 'present'; items: string[]; note?: string }
  | { type: 'auto'; items: string[]; modes: AutoMode[]; count?: number }
  | { type: 'minimal-pair'; title?: string; pairs: { a: string; b: string; aHint?: string; bHint?: string; play: 'a' | 'b' }[] }
  | { type: 'build'; en: string; es: string; distractors?: string[] }
  | { type: 'fill'; en: string; es?: string; options: string[]; answer: number; explain?: string }
  | { type: 'dialogue'; title: string; scene?: string; lines: { who: string; en: string; es: string }[] }
  | {
      type: 'story';
      title: string;
      emoji?: string;
      paragraphs: { en: string; es: string }[];
      questions?: { q: string; options: string[]; answer: number }[];
    }
  | {
      type: 'discover';
      /** Nombre técnico del tema; se revela al final, nunca al principio. */
      topic: string;
      intro: string;
      examples: { en: string; es: string; mark?: string[] }[];
      question: string;
      options: string[];
      answer: number;
      rule: string;
      ruleExamples?: { en: string; es: string }[];
    }
  | { type: 'speak'; en: string; es: string; note?: string }
  | { type: 'tip'; title: string; text: string; emoji?: string }
  /** Dictado: escuchas y escribes. Entrena oído y ortografía a la vez. */
  | { type: 'dictation'; en: string; es?: string }
  /** Escritura guiada: ves la idea en español y la escribes en inglés. */
  | { type: 'write'; es: string; en: string; accept?: string[]; hint?: string }
  /** Juego de rol: una conversación donde tú eliges (o dices) tu respuesta. */
  | { type: 'roleplay'; title: string; scene?: string; turns: RoleTurn[] };

export type RoleTurn =
  | { who: string; en: string; es: string }
  | { you: true; options: { en: string; es: string; ok: boolean; why?: string }[] };

export interface Lesson {
  id: string;
  title: string;
  focus: Focus;
  /** Ítems nuevos que introduce (máximo recomendado: 4). */
  newItems: string[];
  activities: Activity[];
}

export interface Unit {
  id: string;
  level: LevelId;
  title: string;
  emoji: string;
  /** Hito de competencia que se celebra al terminar: "Ya puedo…". */
  canDo: string;
  summary: string;
  /** Tema gramatical que se trabaja (aparece como etiqueta, no como clase abstracta). */
  grammar?: string[];
  items: Item[];
  lessons: Lesson[];
}

export interface CurriculumUnitRef {
  id: string;
  level: LevelId;
  title: string;
  emoji: string;
  canDo: string;
  grammar?: string[];
  /** 'ready' = contenido disponible; 'planned' = aparece en la ruta como "próximamente". */
  status: 'ready' | 'planned';
}

export interface LevelInfo {
  id: LevelId;
  name: string;
  description: string;
}

/** Examen: de control (cada bloque de unidades) o final de nivel (certifica el nivel). */
export interface ExamRef {
  id: string;
  level: LevelId;
  kind: 'checkpoint' | 'final';
  title: string;
  /** El examen aparece en la ruta justo después de esta unidad. */
  afterUnit: string;
  /** Unidades que evalúa. */
  units: string[];
  questions: number;
  passPct: number;
}

export interface Curriculum {
  levels: LevelInfo[];
  units: CurriculumUnitRef[];
  exams: ExamRef[];
}

/** Lectura de la Biblioteca: texto largo graduado, para leer, escuchar, hacer shadowing y dictado. */
export interface Reading {
  id: string;
  level: LevelId;
  title: string;
  emoji: string;
  kind: 'story' | 'dialogue' | 'article' | 'real-speech';
  summary: string;
  sentences: { en: string; es: string; who?: string }[];
  questions?: { q: string; options: string[]; answer: number }[];
}

/** Entrada extra del diccionario (palabras que aparecen en historias pero no son ítems de unidad). */
export interface DictEntry {
  en: string;
  es: string;
  emoji?: string;
  say?: string;
  forms?: string[];
  note?: string;
}

// ─────────────────────────────────────────────────────────────
// Actividades ya "resueltas" que la pantalla de lección reproduce.
// ─────────────────────────────────────────────────────────────

export type Step =
  | { kind: 'present'; items: Item[]; note?: string }
  | { kind: 'listen-pick'; target: Item; options: Item[] }
  | { kind: 'read-pick'; target: Item; options: Item[] }
  | { kind: 'picture-pick'; target: Item; options: Item[] }
  | { kind: 'build'; en: string; es: string; tiles: string[]; itemId?: string }
  | { kind: 'speak'; en: string; es: string; note?: string; itemId?: string }
  | { kind: 'minimal-pair'; title?: string; a: string; b: string; aHint?: string; bHint?: string; play: 'a' | 'b' }
  | { kind: 'fill'; en: string; es?: string; options: string[]; answer: number; explain?: string }
  | { kind: 'dialogue'; title: string; scene?: string; lines: { who: string; en: string; es: string }[] }
  | { kind: 'story'; title: string; emoji?: string; paragraphs: { en: string; es: string }[] }
  | { kind: 'question'; q: string; options: string[]; answer: number; context: string }
  | {
      kind: 'discover';
      topic: string;
      intro: string;
      examples: { en: string; es: string; mark?: string[] }[];
      question: string;
      options: string[];
      answer: number;
      rule: string;
      ruleExamples?: { en: string; es: string }[];
    }
  | { kind: 'tip'; title: string; text: string; emoji?: string }
  | { kind: 'dictation'; en: string; es?: string; itemId?: string }
  | { kind: 'write'; es: string; en: string; accept?: string[]; hint?: string }
  | { kind: 'roleplay'; title: string; scene?: string; turns: RoleTurn[] };

/** Pasos que se califican (los demás son input: se leen/escuchan y se continúa). */
export const GRADED: Step['kind'][] = ['listen-pick', 'read-pick', 'picture-pick', 'build', 'minimal-pair', 'fill', 'question', 'discover', 'dictation', 'write', 'roleplay'];

// ─────────────────────────────────────────────────────────────
// Datos del usuario (IndexedDB)
// ─────────────────────────────────────────────────────────────

export interface CardRow {
  itemId: string;
  unitId: string;
  due: number;
  stability: number;
  difficulty: number;
  elapsed_days: number;
  scheduled_days: number;
  learning_steps: number;
  reps: number;
  lapses: number;
  state: number;
  last_review: number | null;
  /** Último modo usado: el siguiente repaso usa otro distinto (repetición variada). */
  lastMode?: AutoMode;
}

export interface LessonRow {
  lessonId: string;
  unitId: string;
  firstCompletedAt: number;
  lastCompletedAt: number;
  timesCompleted: number;
  bestScore: number;
}

export interface HistoryRow {
  id: string;
  at: number;
  type: 'lesson' | 'review' | 'practice' | 'test' | 'exam' | 'reading';
  refId: string;
  title: string;
  correct: number;
  total: number;
  durationSec: number;
  newItems: number;
}

export interface Settings {
  voiceRate: number;
  voiceName: string;
  showSpanish: 'tap' | 'always';
  speakingEnabled: boolean;
  explorerMode: boolean;
  reviewSize: number;
  warmupSize: number;
  learnerName: string;
  /** Velocidad natural para escucha avanzada (Biblioteca y niveles B1+). */
  naturalSpeed: boolean;
  /** Usar voces distintas (y acentos) para cada personaje. */
  multiVoice: boolean;
  /** IA local opcional (Ollama) para conversar. */
  aiUrl: string;
  aiModel: string;
}

export const DEFAULT_SETTINGS: Settings = {
  voiceRate: 0.85,
  voiceName: '',
  showSpanish: 'tap',
  speakingEnabled: true,
  explorerMode: false,
  reviewSize: 15,
  warmupSize: 3,
  learnerName: '',
  naturalSpeed: false,
  multiVoice: true,
  aiUrl: 'http://localhost:11434',
  aiModel: 'llama3.2:3b',
};
