import { Link } from 'react-router-dom';
import { useApp } from '../state';
import { route, units, itemsById } from '../engine/content';
import { hardItems } from '../engine/progress';
import { isDue } from '../engine/srs';
import { Emoji, Page } from '../components/common';

export default function ReviewHub() {
  const { cards } = useApp();
  const due = cards.filter((c) => isDue(c));
  const hard = hardItems(cards);
  const byUnit = route
    .filter((r) => units[r.id])
    .map((r) => ({ ref: r, ids: cards.filter((c) => c.unitId === r.id).map((c) => c.itemId) }))
    .filter((x) => x.ids.length);

  const link = (ids: string[], title: string) => `/practicar?items=${ids.join(',')}&title=${encodeURIComponent(title)}`;

  return (
    <Page title="Repaso y práctica" intro="El repaso del día te muestra cada palabra justo antes de que la olvides. La práctica libre es para reforzar lo que tú quieras.">
      <section className="review-today">
        {due.length ? (
          <>
            <p className="review-today__n">{due.length}</p>
            <p>{due.length === 1 ? 'palabra lista para repasar' : 'palabras listas para repasar'}</p>
            <Link to="/repasar" className="btn btn--primary">Repasar ahora</Link>
          </>
        ) : (
          <p>{cards.length ? 'Tu repaso de hoy está al día. Vuelve mañana o practica libre abajo.' : 'Cuando termines tu primera lección, aquí aparecerán tus repasos.'}</p>
        )}
      </section>

      {hard.length > 0 && (
        <section>
          <h2>Mis difíciles</h2>
          <p className="muted">Las que más se te han olvidado: {hard.slice(0, 6).map((id) => itemsById[id]?.en).join(', ')}{hard.length > 6 ? '…' : ''}</p>
          <Link to={link(hard.slice(0, 12), 'Mis difíciles')} className="btn btn--ghost">Practicar mis difíciles</Link>
        </section>
      )}

      {byUnit.length > 0 && (
        <section>
          <h2>Practicar por tema</h2>
          <ul className="topics">
            {byUnit.map(({ ref, ids }) => (
              <li key={ref.id}>
                <Link to={link(ids, ref.title)} className="topic">
                  <Emoji e={ref.emoji} className="topic__emoji" />
                  <span>{ref.title}</span>
                  <span className="muted">{ids.length} palabras</span>
                </Link>
              </li>
            ))}
          </ul>
        </section>
      )}
    </Page>
  );
}
