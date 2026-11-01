// Service worker: aplikasi bisa dibuka tanpa internet setelah dikunjungi atau setelah "Simpan semua untuk offline".
const VERSION = 'v1';
const SHELL = `shell-${VERSION}`, DATA = `data-${VERSION}`;
const SHELL_FILES = ['./', 'index.html', 'app.js', 'style.css', 'manifest.webmanifest', 'icon-192.png'];

self.addEventListener('install', e => {
  e.waitUntil(caches.open(SHELL).then(c => c.addAll(SHELL_FILES)).then(() => self.skipWaiting()));
});
self.addEventListener('activate', e => {
  e.waitUntil(caches.keys().then(keys => Promise.all(keys.filter(k => ![SHELL, DATA].includes(k)).map(k => caches.delete(k)))).then(() => self.clients.claim()));
});
self.addEventListener('fetch', e => {
  const req = e.request;
  if (req.method !== 'GET') return;
  const url = new URL(req.url);
  if (url.origin !== location.origin) return;       // permintaan ke layanan lain (arti kata online) tidak disentuh
  if (url.pathname.includes('/data/')) {
    // data: tampilkan cache dulu, perbarui di latar belakang
    e.respondWith(caches.open(DATA).then(async c => {
      const hit = await c.match(req, { ignoreSearch: true });
      const net = fetch(req).then(r => { if (r.ok) c.put(req, r.clone()); return r; }).catch(() => hit);
      return hit || net;
    }));
    return;
  }
  // kode aplikasi: ambil versi terbaru dari jaringan, jatuh ke cache saat offline
  e.respondWith(fetch(req).then(r => { const cp = r.clone(); caches.open(SHELL).then(c => c.put(req, cp)); return r; }).catch(() => caches.match(req, { ignoreSearch: true }).then(h => h || caches.match('index.html'))));
});
