const CACHE_VERSION = "esperanto-mobile-pwa-2026-05-11-3";
const APP_CACHE = `${CACHE_VERSION}:app`;
const RUNTIME_CACHE = `${CACHE_VERSION}:runtime`;

const APP_SHELL = [
  "./mobile_app/index.html",
  "./mobile_app/styles.css",
  "./mobile_app/app.js",
  "./mobile_app/manifest.webmanifest",
  "./mobile_app/icon.svg",
  "./mobile_app/data/vocab.json",
  "./mobile_app/data/sentences.json",
];

self.addEventListener("install", (event) => {
  event.waitUntil(
    caches.open(APP_CACHE)
      .then((cache) => cache.addAll(APP_SHELL))
      .then(() => self.skipWaiting()),
  );
});

self.addEventListener("activate", (event) => {
  event.waitUntil(
    caches.keys()
      .then((keys) => Promise.all(
        keys
          .filter((key) => !key.startsWith(CACHE_VERSION))
          .map((key) => caches.delete(key)),
      ))
      .then(() => self.clients.claim()),
  );
});

self.addEventListener("fetch", (event) => {
  const { request } = event;
  if (request.method !== "GET") {
    return;
  }
  const url = new URL(request.url);
  if (url.origin !== self.location.origin) {
    return;
  }

  if (url.pathname.endsWith("/vocab.json") || url.pathname.endsWith("/sentences.json")) {
    event.respondWith(networkFirst(request));
    return;
  }

  if (url.pathname.endsWith(".wav") || url.pathname.endsWith(".mp3") || url.pathname.endsWith(".ogg")) {
    event.respondWith(cacheFirst(request, RUNTIME_CACHE));
    return;
  }

  if (url.pathname.includes("/mobile_app/") || url.pathname.endsWith("/mobile-sw.js")) {
    event.respondWith(cacheFirst(request, APP_CACHE));
  }
});

async function cacheFirst(request, cacheName) {
  const cached = await caches.match(request);
  if (cached) {
    return cached;
  }
  const response = await fetch(request);
  if (response.ok) {
    const cache = await caches.open(cacheName);
    cache.put(request, response.clone());
  }
  return response;
}

async function networkFirst(request) {
  const cache = await caches.open(APP_CACHE);
  try {
    const response = await fetch(request);
    if (response.ok) {
      cache.put(request, response.clone());
    }
    return response;
  } catch (error) {
    const cached = await cache.match(request);
    if (cached) {
      return cached;
    }
    throw error;
  }
}
