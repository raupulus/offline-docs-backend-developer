/* Service Worker desmantelado: desregistra y vacía toda la caché del navegador */
self.addEventListener('install', function (event) {
  self.skipWaiting();
});

self.addEventListener('activate', function (event) {
  event.waitUntil(
    caches.keys().then(function (keys) {
      return Promise.all(
        keys.map(function (k) {
          return caches.delete(k);
        })
      );
    }).then(function () {
      return self.registration.unregister();
    }).then(function () {
      return self.clients.claim();
    })
  );
});

self.addEventListener('fetch', function () {
  // No interceptar nada: petición directa a red
  return;
});

