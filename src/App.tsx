import { HashRouter, NavLink, Route, Routes, useLocation } from 'react-router-dom';
import { AppProvider, useApp } from './state';
import { DictionaryDrawer } from './components/DictionaryDrawer';
import Home from './pages/Home';
import RoutePage from './pages/RoutePage';
import UnitPage from './pages/UnitPage';
import { LessonSession, PracticeSession, ReviewSession, UnitTestSession, ExamSession } from './pages/Session';
import ReviewHub from './pages/ReviewHub';
import Library from './pages/Library';
import DictionaryPage from './pages/DictionaryPage';
import ProgressPage from './pages/ProgressPage';
import SettingsPage from './pages/SettingsPage';
import BackupPage from './pages/BackupPage';
import { isDue } from './engine/srs';

const NAV = [
  { to: '/', label: 'Hoy', icon: '☀️' },
  { to: '/ruta', label: 'Ruta', icon: '🧭' },
  { to: '/repaso', label: 'Repaso', icon: '🔁' },
  { to: '/biblioteca', label: 'Biblioteca', icon: '📚' },
  { to: '/diccionario', label: 'Diccionario', icon: '📖' },
  { to: '/progreso', label: 'Progreso', icon: '📈' },
];

function Shell() {
  const { ready, cards } = useApp();
  const loc = useLocation();
  const inSession = /^\/(leccion|repasar|practicar|prueba|examen)/.test(loc.pathname);
  const due = cards.filter((c) => isDue(c)).length;

  if (!ready) return <div className="boot">Cargando…</div>;

  return (
    <div className={inSession ? 'shell shell--session' : 'shell'}>
      {!inSession && (
        <nav className="nav" aria-label="Secciones">
          <div className="nav__brand">
            <img src="./icon.svg" alt="" width={32} height={32} />
            <span>English from Zero</span>
          </div>
          {NAV.map((n) => (
            <NavLink key={n.to} to={n.to} end={n.to === '/'} className="nav__link">
              <span className="nav__icon" aria-hidden>{n.icon}</span>
              <span className="nav__label">{n.label}</span>
              {n.to === '/repaso' && due > 0 && <span className="nav__badge" aria-label={`${due} pendientes`}>{due}</span>}
            </NavLink>
          ))}
        </nav>
      )}
      <main className="main">
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/ruta" element={<RoutePage />} />
          <Route path="/unidad/:unitId" element={<UnitPage />} />
          <Route path="/leccion/:lessonId" element={<LessonSession />} />
          <Route path="/repasar" element={<ReviewSession />} />
          <Route path="/prueba/:unitId" element={<UnitTestSession />} />
          <Route path="/examen/:examId" element={<ExamSession />} />
          <Route path="/biblioteca" element={<Library />} />
          <Route path="/practicar" element={<PracticeSession />} />
          <Route path="/repaso" element={<ReviewHub />} />
          <Route path="/diccionario" element={<DictionaryPage />} />
          <Route path="/progreso" element={<ProgressPage />} />
          <Route path="/ajustes" element={<SettingsPage />} />
          <Route path="/copia" element={<BackupPage />} />
        </Routes>
      </main>
      <DictionaryDrawer />
    </div>
  );
}

export default function App() {
  return (
    <AppProvider>
      <HashRouter>
        <Shell />
      </HashRouter>
    </AppProvider>
  );
}
