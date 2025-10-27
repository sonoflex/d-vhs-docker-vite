import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

export default defineConfig({
  plugins: [vue()],
  root: '/app',                // Root der App im Container
  publicDir: '/app/public',    // Damit index.html und Assets gefunden werden
  server: {
    host: '0.0.0.0',           // Lauschen auf allen Interfaces
    port: 5173,
  }
})