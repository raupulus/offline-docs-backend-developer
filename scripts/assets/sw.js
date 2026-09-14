/* ═══════════════════════════════════════════════════════════════════
   Service Worker — Documentación offline
   Estrategia de caché progresiva (PWA 100% estática y sin dependencias)
   ═══════════════════════════════════════════════════════════════════ */

const CACHE_NAME = 'docs-offline-v1';

// Recursos esenciales precacheados durante la instalación
const CORE_ASSETS = [
  './',
  './index.html',
  './licenses.html',
  './legal.html',
  './manifest.json',
  './_assets/style.css',
  './_assets/code.css',
  './_assets/app.js',
  './_assets/icon.svg'
];

self.addEventListener('install', (event) => {
  event.waitUntil(
    caches.open(CACHE_NAME).then((cache) => {
      // Usar individualmente para que si alguno falla no aborte todo el precache
      return Promise.allSettled(
        CORE_ASSETS.map((url) => cache.add(url).catch((err) => console.warn('SW pre-cache skip:', url, err)))
      );
    }).then(() => self.skipWaiting())
  );
});

self.addEventListener('activate', (event) => {
  event.waitUntil(
    caches.keys().then((keys) => {
      return Promise.all(
        keys.map((key) => {
          if (key !== CACHE_NAME) {
            return caches.delete(key);
          }
        })
      );
    }).then(() => self.clients.claim())
  );
});

self.addEventListener('fetch', (event) => {
  const request = event.request;

  // Solo gestionar peticiones GET del mismo origen
  if (request.method !== 'GET') return;
  const url = new URL(request.url);
  if (url.origin !== self.location.origin) return;

  // 1. Assets estáticos (_assets/): Cache First con fallback a red
  if (url.pathname.includes('/_assets/')) {
    event.respondWith(
      caches.match(request).then((cachedResponse) => {
        if (cachedResponse) return cachedResponse;
        return fetch(request).then((networkResponse) => {
          if (networkResponse && networkResponse.status === 200) {
            const clone = networkResponse.clone();
            caches.open(CACHE_NAME).then((cache) => cache.put(request, clone));
          }
          return networkResponse;
        });
      })
    );
    return;
  }

  // 2. Páginas HTML e índices de búsqueda: Network First con fallback a caché
  event.respondWith(
    fetch(request)
      .then((networkResponse) => {
        if (networkResponse && networkResponse.status === 200) {
          const clone = networkResponse.clone();
          caches.open(CACHE_NAME).then((cache) => cache.put(request, clone));
        }
        return networkResponse;
      })
      .catch(() => {
        return caches.match(request).then((cachedResponse) => {
          if (cachedResponse) return cachedResponse;
          // Fallback a portada si es navegación y no se encuentra en caché
          if (request.mode === 'navigate') {
            return caches.match('./index.html') || caches.match('/');
          }
          return new Response('Sin conexión', { status: 503, statusText: 'Offline' });
        });
      })
  );
});
