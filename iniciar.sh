#!/usr/bin/env bash
# English from Zero - lanzador para Linux / macOS
cd "$(dirname "$0")"

if ! command -v node >/dev/null 2>&1; then
  echo "[!] No encontré Node.js. Instala la versión LTS desde https://nodejs.org y vuelve a ejecutar ./iniciar.sh"
  exit 1
fi

if [ ! -d node_modules ]; then
  echo "Primera vez: instalando dependencias (1-3 minutos)..."
  npm install || { echo "[!] La instalación falló."; exit 1; }
fi

echo "Abriendo la app en tu navegador... (Ctrl+C para cerrar)"
npm run start
