import { defineConfig } from 'vite';

export default defineConfig({
  root: '.',       // root ist das aktuelle Verzeichnis
  server: {
    host: '0.0.0.0',
    port: 5173
  }
});