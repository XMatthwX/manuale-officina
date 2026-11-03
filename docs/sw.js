/* Service worker: l'app funziona anche senza internet e si aggiorna da sola quando c'è rete. */
const VERSION = "cf037649c0";
const SHELL_CACHE = "coppie-shell-" + VERSION;
const FONT_CACHE = "coppie-fonts";
const SHELL = ["./", "index.html", "seed.js", "manifest.webmanifest", "icon-192.png", "icon-512.png", "apple-touch-icon.png"];

self.addEventListener("install", e => {
  e.waitUntil(caches.open(SHELL_CACHE).then(c => c.addAll(SHELL)).then(() => self.skipWaiting()));
});
self.addEventListener("activate", e => {
  e.waitUntil(caches.keys()
    .then(keys => Promise.all(keys.filter(k => k.startsWith("coppie-shell-") && k !== SHELL_CACHE).map(k => caches.delete(k))))
    .then(() => self.clients.claim()));
});
const timeout = (ms) => new Promise((_, rej) => setTimeout(() => rej(new Error("timeout")), ms));
self.addEventListener("fetch", e => {
  const req = e.request;
  if (req.method !== "GET") return;
  const url = new URL(req.url);
  if (url.origin === self.location.origin) {
    /* prima la rete (versione nuova), se è lenta o assente la copia salvata */
    e.respondWith((async () => {
      const cache = await caches.open(SHELL_CACHE);
      try {
        const res = await Promise.race([fetch(req), timeout(3500)]);
        if (res && res.ok) cache.put(req, res.clone());
        return res;
      } catch (err) {
        return (await cache.match(req, { ignoreSearch: true })) || (await cache.match("index.html")) || Response.error();
      }
    })());
  } else if (/fonts\.(googleapis|gstatic)\.com$/.test(url.hostname)) {
    e.respondWith(caches.open(FONT_CACHE).then(c => c.match(req).then(hit => hit || fetch(req).then(res => { c.put(req, res.clone()); return res; }))));
  }
});
