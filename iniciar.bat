@echo off
chcp 65001 >nul
title English from Zero
cd /d "%~dp0"

echo.
echo  ==========================================
echo    English from Zero - iniciando...
echo  ==========================================
echo.

where node >nul 2>nul
if errorlevel 1 (
  echo  [!] No encontre Node.js en este PC.
  echo      1. Instala la version LTS desde https://nodejs.org
  echo      2. Cierra esta ventana y vuelve a dar doble clic en iniciar.bat
  start https://nodejs.org/es/download
  pause
  exit /b 1
)

if not exist "node_modules\" (
  echo  Primera vez: instalando dependencias. Tarda 1-3 minutos...
  call npm install
  if errorlevel 1 (
    echo  [!] La instalacion fallo. Revisa tu conexion a internet y vuelve a intentarlo.
    pause
    exit /b 1
  )
)

echo  Abriendo la app en tu navegador...
echo  Para cerrarla, cierra esta ventana.
echo.
call npm run start
pause
