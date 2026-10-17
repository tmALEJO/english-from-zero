import { GRADED } from '../src/types';
import 'fake-indexeddb/auto';
import { describe, expect, it } from 'vitest';
import { checkSpeech, sameSentence, levenshtein } from '../src/engine/text';
import { newCard, review, outcomeFrom } from '../src/engine/srs';
import { route, units, lookupWord, getItem } from '../src/engine/content';
import { expandLesson } from '../src/engine/steps';
import { unitStatuses, currentLevel, buildReview, nextLesson, testId, examRowId, UNIT_TEST_PASS } from '../src/engine/progress';
import { curriculum } from '../src/engine/content';
import { makeBackup, mergeBackup, toQrChunks, parseQrPart, fromQrParts } from '../src/engine/backup';
import { AppDB } from '../src/db/db';
import { completeLesson, exportBackup, importBackup } from '../src/db/actions';
import type { LessonRow } from '../src/types';

const DAY = 86400000;

describe('texto y voz', () => {
  it('acepta pequeñas diferencias de reconocimiento de voz', () => {
    expect(checkSpeech('Nice to meet you', ['nice to meet you']).ok).toBe(true);
    expect(checkSpeech("I'm from Colombia", ['I am from Colombia']).ok).toBe(true);
    const r = checkSpeech('How much is this?', ['how much is']);
    expect(r.ok).toBe(true);
    expect(r.missing).toEqual(['this']);
    expect(checkSpeech('The check, please', ['the chicken please']).ok).toBe(false);
  });
  it('compara frases armadas sin importar mayúsculas ni puntuación', () => {
    expect(sameSentence('my name is sam', 'My name is Sam')).toBe(true);
    expect(sameSentence("I'd like a coffee", 'I would like a coffee')).toBe(true);
    expect(levenshtein('ship', 'sheep')).toBe(2);
  });
});

describe('contenido', () => {
  it('todas las unidades listas tienen lecciones que se pueden expandir', () => {
    for (const r of route.filter((x) => x.status === 'ready')) {
      const u = units[r.id];
      expect(u, r.id).toBeDefined();
      for (const l of u.lessons) {
        const maxNew = u.level === 'B2' || u.level === 'C1' ? 5 : 4;
        expect(l.newItems.length, l.id).toBeLessThanOrEqual(maxNew);
        const steps = expandLesson(l, u);
        expect(steps.length, l.id).toBeGreaterThan(2);
        for (const s of steps) if ('options' in s && Array.isArray(s.options) && 'target' in s) {
          expect(s.options.some((o) => o.id === s.target.id)).toBe(true);
          expect(new Set(s.options.map((o) => o.id)).size).toBe(s.options.length);
        }
      }
    }
  });
  it('el diccionario encuentra formas conjugadas', () => {
    expect(lookupWord('works')?.en).toBe('work');
    expect(lookupWord('goes')?.en).toBe('go');
    expect(lookupWord('apples')?.en).toBe('apple');
    expect(lookupWord('the')?.es).toContain('el');
  });
});

describe('repetición espaciada', () => {
  it('los intervalos crecen cuando recuerdas y se reinician cuando olvidas', () => {
    let c = newCard('u01.hello', 'u01-saludos', new Date(0));
    c = review(c, 'good', undefined, new Date(0));
    const first = c.scheduled_days;
    c = review(c, 'good', undefined, new Date(c.due));
    expect(c.scheduled_days).toBeGreaterThan(first);
    const before = c.scheduled_days;
    c = review(c, 'again', undefined, new Date(c.due));
    expect(c.scheduled_days).toBeLessThan(before);
    expect(c.lapses).toBe(1);
  });
  it('traduce el desempeño en calificación', () => {
    expect(outcomeFrom(true, 1)).toBe('good');
    expect(outcomeFrom(false, 2)).toBe('hard');
    expect(outcomeFrom(false, 3)).toBe('again');
  });
  it('el repaso usa un modo distinto al último', () => {
    const card = { ...review(newCard('u02.nice', 'u02-presentarse'), 'good'), due: 0, lastMode: 'listen-pick' as const };
    const [p] = buildReview([card], 5);
    expect(p.mode).not.toBe('listen-pick');
  });
});

describe('progreso y niveles', () => {
  const row = (id: string, unitId: string): LessonRow => ({ lessonId: id, unitId, firstCompletedAt: 1, lastCompletedAt: 1, timesCompleted: 1, bestScore: 100 });
  // Terminar una unidad = todas las lecciones + la prueba aprobada.
  const done = (unitId: string): LessonRow[] => [
    ...units[unitId].lessons.map((l) => row(l.id, unitId)),
    { ...row(testId(unitId), unitId), bestScore: UNIT_TEST_PASS },
  ];
  const passExam = (examId: string): LessonRow => ({ lessonId: examRowId(examId), unitId: examId, firstCompletedAt: 1, lastCompletedAt: 1, timesCompleted: 1, bestScore: 100 });

  it('la ruta se desbloquea en orden', () => {
    const st = unitStatuses([]);
    expect(st['u00-sonidos']).toBe('available');
    expect(st['u01-saludos']).toBe('locked');
    const st2 = unitStatuses(done('u00-sonidos'));
    expect(st2['u00-sonidos']).toBe('done');
    expect(st2['u01-saludos']).toBe('available');
    expect(unitStatuses([], true)['u05-familia']).toBe('available');
  });
  it('sugiere la siguiente lección', () => {
    expect(nextLesson([])?.lesson.id).toBe('u00-l1');
    expect(nextLesson(done('u00-sonidos'))?.lesson.id).toBe('u01-l1');
  });
  it('A0 se alcanza al terminar todas sus unidades', () => {
    const a0 = [
      ...route.filter((r) => r.level === 'A0').flatMap((r) => done(r.id)),
      ...curriculum.exams.filter((e) => e.level === 'A0').map((e) => passExam(e.id)),
    ];
    expect(currentLevel([]).reached).toBeNull();
    expect(currentLevel(a0).reached).toBe('A0');
    expect(currentLevel(a0).working).toBe('A1');
  });
});

describe('exportar e importar', () => {
  const base = () => makeBackup({ cards: [], lessons: [], history: [], settings: {}, device: 'test' });

  it('combinar se queda con el repaso más reciente de cada palabra', () => {
    const old = { ...newCard('u01.hello', 'u01-saludos'), last_review: 1000, reps: 1 };
    const recent = { ...old, last_review: 5000, reps: 3 };
    const m = mergeBackup({ cards: [old], lessons: [], history: [] }, { ...base(), cards: [recent] });
    expect(m.cards[0].reps).toBe(3);
    const m2 = mergeBackup({ cards: [recent], lessons: [], history: [] }, { ...base(), cards: [old] });
    expect(m2.cards[0].reps).toBe(3);
  });

  it('el QR se divide en partes y se reconstruye en cualquier orden', () => {
    const cards = Object.keys(units).flatMap((u) => units[u].items.map((it) => ({ ...review(newCard(it.id, u), 'good'), lastMode: 'build' as const })));
    const b = { ...base(), cards };
    const chunks = toQrChunks(b);
    expect(chunks.length).toBeGreaterThan(1);
    const parts = chunks.map((c) => parseQrPart(c)!).reverse();
    const back = fromQrParts(parts);
    expect(back.cards.length).toBe(cards.length);
    expect(back.cards[0].itemId).toBe(cards[0].itemId);
    expect(Math.abs(back.cards[0].due - cards[0].due)).toBeLessThan(60001);
  });

  it('una lección terminada en el PC aparece en el celular tras importar', async () => {
    const pc = new AppDB('pc-test');
    const phone = new AppDB('phone-test');
    const u = units['u01-saludos'];
    await completeLesson(u, u.lessons[0], { type: 'lesson', refId: u.lessons[0].id, title: 't', correct: 5, total: 6, startedAt: Date.now() - 60000, results: [] }, pc);
    const backup = JSON.parse(JSON.stringify(await exportBackup(pc)));
    const stats = await importBackup(backup, 'merge', phone);
    expect(stats.lessonsAdded).toBe(1);
    expect(stats.cardsAdded).toBe(u.lessons[0].newItems.length);
    expect(await phone.cards.count()).toBe(4);
    expect(getItem('u01.hello').en).toBe('Hello');
    expect((await phone.cards.get('u01.hello'))!.due).toBeGreaterThan(Date.now() + DAY / 2);
  });
});

import { checkTyped } from '../src/engine/text';
import { buildUnitTest, buildExam } from '../src/engine/progress';
import { units as allUnits } from '../src/engine/content';
import { curriculum as curr } from '../src/engine/content';

describe('dictado y escritura', () => {
  it('acepta la respuesta correcta y marca errores', () => {
    expect(checkTyped('I am from Colombia', ['I am from Colombia']).ok).toBe(true);
    expect(checkTyped("I'm from Colombia", ['I am from Colombia']).ok).toBe(true); // contracción
    const r = checkTyped('I am from Colombai', ['I am from Colombia']);
    expect(r.ok).toBe(true); // typo de una letra en palabra larga se perdona
    expect(r.words.some((w) => w.status === 'typo')).toBe(true);
    const bad = checkTyped('I am from Peru', ['I am from Colombia']);
    expect(bad.ok).toBe(false);
    expect(bad.words.find((w) => w.word === 'colombia')?.status).toBe('wrong');
  });
});

describe('exámenes', () => {
  it('la prueba de unidad genera preguntas calificables', () => {
    const u = allUnits['u02-presentarse'];
    const steps = buildUnitTest(u, () => 0.5);
    expect(steps.length).toBeGreaterThan(5);
    expect(steps.every((s) => GRADED.includes(s.step.kind))).toBe(true);
  });
  it('cada examen del currículo se puede construir', () => {
    for (const e of curr.exams) {
      const steps = buildExam(e, () => 0.5);
      expect(steps.length, e.id).toBeGreaterThan(5);
      expect(steps.every((s) => GRADED.includes(s.step.kind)), e.id).toBe(true);
    }
  });
});
