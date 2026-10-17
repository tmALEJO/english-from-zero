import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';

// base: './' hace que el build funcione tanto en el navegador como dentro del APK (Capacitor).
export default defineConfig({
  plugins: [react()],
  base: './',
  server: { port: 5173, strictPort: false, host: 'localhost' },
  build: { outDir: 'dist', chunkSizeWarningLimit: 1500 },
  test: { environment: 'node', include: ['tests/**/*.test.ts'] },
} as never);
