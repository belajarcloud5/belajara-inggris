(() => {
'use strict';

// ---------- util ----------
const $ = (s, el = document) => el.querySelector(s);
const app = $('#app');
const esc = s => String(s).replace(/[&<>"']/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]));
// **tebal**, *miring*, ~~coret~~ dan [[kata Inggris yang bisa diklik untuk didengar]]
const fmt = s => esc(s)
  .replace(/\*\*(.+?)\*\*/g, '<b>$1</b>')
  .replace(/~~(.+?)~~/g, '<s>$1</s>')
  .replace(/\*([^*\n]+?)\*/g, '<i>$1</i>')
  .replace(/\[\[(.+?)\]\]/g, (m, a) => `<span class="en" role="button" tabindex="0" data-say="${a}">${a}</span>`);
const shuffle = a => { a = a.slice(); for (let i = a.length - 1; i > 0; i--) { const j = Math.floor(Math.random() * (i + 1)); [a[i], a[j]] = [a[j], a[i]]; } return a; };
const norm = s => String(s).toLowerCase().replace(/[’‘`]/g, "'").replace(/[.,!?;:]/g, '').replace(/\s+/g, ' ').trim();
// dikte: bentuk singkat dan lengkap dianggap sama (I'm = I am, don't = do not)
const expand = s => norm(s).replace(/\bcan't\b/g, 'cannot').replace(/\bwon't\b/g, 'will not').replace(/n't\b/g, ' not').replace(/'m\b/g, ' am').replace(/'re\b/g, ' are').replace(/'ll\b/g, ' will').replace(/'ve\b/g, ' have').replace(/\bcan not\b/g, 'cannot').replace(/-/g, ' ').replace(/\s+/g, ' ').trim();
const stripTags = s => String(s).replace(/\[\[|\]\]|\*\*/g, '');

// ---------- suara (bawaan browser; bisa dipilih, disimpan) ----------
const hasTTS = 'speechSynthesis' in window;
const VKEY = 'english7.voice';
const vset = { name: '', rate: 0.85, pitch: 1 };
try { Object.assign(vset, JSON.parse(localStorage.getItem(VKEY)) || {}); } catch (e) { /* diabaikan */ }
const saveVoice = () => { try { localStorage.setItem(VKEY, JSON.stringify(vset)); } catch (e) { /* diabaikan */ } };
const FEMALE = /(zira|samantha|jenny|aria|susan|hazel|female|woman|karen|victoria|moira|tessa|fiona|libby|sonia|joanna|salli|ivy|kendra|kimberly|emma|amy|allison|ava|nicky|serena|kate|sara|google us english)/i;
const MALE = /(david|mark|george|james|daniel|(?<!fe)male|fred|alex|ryan|guy|brian|thomas|oliver|rishi|junior|eric|christopher)/i;
const enVoices = () => hasTTS ? speechSynthesis.getVoices().filter(v => /^en/i.test(v.lang)) : [];
function scoreVoice(v) {
  let sc = 0;
  if (FEMALE.test(v.name)) sc += 10;
  if (MALE.test(v.name)) sc -= 10;
  if (/^en[-_]US/i.test(v.lang)) sc += 3;
  if (/natural|online/i.test(v.name)) sc += 2;
  return sc;
}
function currentVoice() {
  const vs = enVoices();
  if (!vs.length) return null;
  if (vset.name) { const f = vs.find(v => v.name === vset.name); if (f) return f; }
  return vs.slice().sort((a, b) => scoreVoice(b) - scoreVoice(a))[0];   // utamakan suara perempuan bila ada
}
// jenis kelamin pembicara dialog -> suara perempuan / laki-laki
const GENDER = { dina: 'f', rani: 'f', mother: 'f', budi: 'm', tom: 'm', 'mr. adi': 'm', 'ms. sari': 'f', ani: 'f', siti: 'f', maya: 'f', rina: 'f', lisa: 'f', anna: 'f', sarah: 'f', dewi: 'f', tika: 'f', salma: 'f', laura: 'f', 'mrs. hartono': 'f', 'ms. lestari': 'f', arif: 'm', kevin: 'm', rizal: 'm', anton: 'm', andi: 'm', doni: 'm', dika: 'm', ryan: 'm', ben: 'm', sam: 'm', father: 'm', 'mr. hadi': 'm', 'dr. wijaya': 'm', ali: 'm', anita: 'f', ana: 'f', wulan: 'f', sinta: 'f', daniel: 'm', grandpa: 'm', grandfather: 'm', dad: 'm', mom: 'f', grandma: 'f', grandmother: 'f' };
const genderOf = name => GENDER[String(name).toLowerCase()] || '';
function maleVoice() {
  const vs = enVoices().filter(v => MALE.test(v.name) && !FEMALE.test(v.name));
  return vs.sort((a, b) => scoreVoice(a) - scoreVoice(b) || (/^en[-_]US/i.test(b.lang) - /^en[-_]US/i.test(a.lang)))[0] || null;
}
function femaleVoice() {
  const vs = enVoices().filter(v => FEMALE.test(v.name) && !MALE.test(v.name));
  return vs.sort((a, b) => scoreVoice(b) - scoreVoice(a))[0] || null;
}
function speakSlow(text) { const r = vset.rate; vset.rate = Math.max(0.5, r * 0.6); speak(text); vset.rate = r; }
// membuat ucapan dengan suara sesuai jenis kelamin: 'f' perempuan, 'm' laki-laki, '' suara bawaan (diutamakan perempuan)
function makeUtter(text, gender) {
  const u = new SpeechSynthesisUtterance(text);
  u.lang = 'en-US'; u.rate = vset.rate; u.pitch = vset.pitch;
  let v = currentVoice();
  if (gender === 'm') {
    const m = maleVoice();
    if (m) { v = m; u.pitch = 1; } else u.pitch = 0.7;          // tidak ada suara laki-laki: turunkan nada
  } else if (gender === 'f' && !(v && FEMALE.test(v.name) && !MALE.test(v.name))) {   // suara pilihan sudah perempuan: biarkan
    const f = femaleVoice();
    if (f) { v = f; u.pitch = vset.pitch; }
    else if (v && MALE.test(v.name) && !FEMALE.test(v.name)) u.pitch = Math.max(vset.pitch, 1.5);   // hanya ada suara laki-laki: naikkan nada
  }
  if (v) { u.voice = v; u.lang = v.lang; }
  return u;
}
function speak(text, gender) {
  if (!hasTTS) return;
  speechSynthesis.cancel();
  speechSynthesis.speak(makeUtter(text, gender));
}
// bacaan berdialog: tiap pembicara ("Dina: ...", "Tom: ...") dibacakan dengan suara sesuai namanya
const ROLES = new Set(['agent', 'audience', 'caller', 'chair', 'colleague', 'customer', 'doctor', 'guest', 'hr', 'interviewer', 'manager', 'officer', 'receptionist', 'reporter', 'seller', 'staff', 'student', 'teacher', 'tourist', 'waiter', 'visitor', 'witness']);
function parseSpeakers(text) {
  const re = /(^|[\s"])((?:Mr|Ms|Mrs|Dr)\.\s[A-Z][a-z]+|[A-Z][A-Za-z]+): /g, marks = [];
  let m;
  while ((m = re.exec(text))) {
    const name = m[2], key = name.toLowerCase();
    if (GENDER[key] || ROLES.has(key)) marks.push({ name, at: m.index + m[1].length, from: m.index + m[0].length });
  }
  const segs = [];
  if (!marks.length) {   // narasi orang pertama: "My name is Arif" -> suara laki-laki
    let g = '';
    for (const me of text.matchAll(/\b(?:my name is|i am|i'm|this is)\s+([a-z]+)/gi)) { g = genderOf(me[1]); if (g) break; }
    return [{ who: '', g, text }];
  }
  if (marks[0].at > 0 && text.slice(0, marks[0].at).trim()) segs.push({ who: '', g: '', text: text.slice(0, marks[0].at).trim() });
  marks.forEach((k, i) => segs.push({ who: k.name, g: genderOf(k.name), text: text.slice(k.from, i + 1 < marks.length ? marks[i + 1].at : undefined).trim() }));
  // peran tanpa jenis kelamin (Tourist, Customer, ...) diberi suara berlawanan dengan lawan bicara yang jenis kelaminnya diketahui
  const known = segs.find(x => x.g);
  const given = {};
  segs.forEach(x => {
    if (x.g || !x.who) return;
    if (!(x.who in given)) given[x.who] = known ? (known.g === 'f' ? 'm' : 'f') : (Object.keys(given).length % 2 ? 'm' : 'f');
    x.g = given[x.who];
  });
  return segs.filter(x => x.text);
}
function speakSeq(segs) {
  if (!hasTTS) return;
  speechSynthesis.cancel();
  segs.forEach(x => speechSynthesis.speak(makeUtter(x.text, x.g)));
}
function initVoicePanel() {
  const btn = $('#vbtn'), wrap = $('#vpanel'), panel = $('#vbody');
  if (!btn || !wrap || !panel) return;
  function render() {
    if (!hasTTS) {
      panel.innerHTML = `<h4>🔊 Suara</h4><p><b>Browser ini tidak mendukung suara bawaan.</b> Tombol 🔊 tidak akan berbunyi di sini.</p>
        <p class="hint">Coba buka situs ini di browser lain di perangkat ini (Chrome, Puffin TV Browser, atau Microsoft Edge). Atau pakai HP/laptop untuk bagian yang butuh suara.</p>`;
      return;
    }
    const vs = enVoices(), cur = currentVoice();
    const sel = vs.length
      ? `<label>Pilih suara<select id="vsel">${vs.map(v => `<option value="${esc(v.name)}" ${cur && cur.name === v.name ? 'selected' : ''}>${esc(v.name)} (${esc(v.lang)})</option>`).join('')}</select></label>`
      : '<p class="hint">Belum ada suara bahasa Inggris di perangkat ini. Pasang suara bahasa Inggris di pengaturan sistem, atau coba browser lain (misalnya Microsoft Edge).</p>';
    panel.innerHTML = `<h4>🔊 Suara</h4><p class="hint" id="vstat">Suara bahasa Inggris terdeteksi: <b>${vs.length}</b></p>${sel}
      <label>Kecepatan: <b id="vrv">${vset.rate}</b><input id="vrate" type="range" min="0.5" max="1.2" step="0.05" value="${vset.rate}"></label>
      <label>Nada: <b id="vpv">${vset.pitch}</b><input id="vpitch" type="range" min="0.8" max="1.8" step="0.05" value="${vset.pitch}"></label>
      <div class="row"><button class="btn small" id="vtest">🔊 Tes suara</button><button class="btn ghost small" id="vreset">Atur ulang</button></div>
      <p class="hint">Mau suara perempuan? Pilih suara yang namanya perempuan (mis. Zira, Aria, Jenny, Samantha, atau "Google US English"). Kalau hanya ada suara laki-laki, naikkan <b>Nada</b> ke 1.4 sampai 1.6 supaya terdengar lebih tinggi. Di Microsoft Edge ada banyak suara perempuan yang natural.</p>`;
    const sv = $('#vsel', panel);
    if (sv) sv.addEventListener('change', () => { vset.name = sv.value; saveVoice(); speak('Hello! Nice to meet you.'); });
    $('#vrate', panel).addEventListener('input', e => { vset.rate = +e.target.value; $('#vrv', panel).textContent = vset.rate; saveVoice(); });
    $('#vpitch', panel).addEventListener('input', e => { vset.pitch = +e.target.value; $('#vpv', panel).textContent = vset.pitch; saveVoice(); });
    $('#vtest', panel).addEventListener('click', () => {
      const st = $('#vstat', panel); st.textContent = 'Memutar…';
      const u = new SpeechSynthesisUtterance('Hello! My name is Rani. Nice to meet you.');
      u.lang = 'en-US'; u.rate = vset.rate; u.pitch = vset.pitch;
      const v = currentVoice(); if (v) { u.voice = v; u.lang = v.lang; }
      u.onstart = () => { st.textContent = 'Suara berjalan ✅. Kalau tidak terdengar, naikkan volume TV.'; };
      u.onerror = e => { st.textContent = 'Gagal memutar suara (' + (e.error || 'tidak diketahui') + '). Pasang suara bahasa Inggris di pengaturan TV.'; };
      speechSynthesis.cancel(); speechSynthesis.speak(u);
      setTimeout(() => { if (st.textContent === 'Memutar…') st.textContent = 'Tidak ada respons dari mesin suara browser ini ❌'; }, 3000);
    });
    $('#vreset', panel).addEventListener('click', () => { vset.name = ''; vset.rate = 0.85; vset.pitch = 1; saveVoice(); render(); });
  }
  btn.addEventListener('click', () => { wrap.hidden = !wrap.hidden; if (!wrap.hidden) render(); });
  if (hasTTS) speechSynthesis.onvoiceschanged = () => { if (!wrap.hidden) render(); };
}
document.addEventListener('click', e => {
  const el = e.target.closest('[data-say]');
  if (el) speak(el.dataset.say, el.dataset.g);
});
document.addEventListener('keydown', e => {
  if ((e.key === 'Enter' || e.key === ' ') && e.target.matches('.en[data-say]')) { e.preventDefault(); speak(e.target.dataset.say, e.target.dataset.g); }
});

initVoicePanel();

// ---------- tema terang / gelap ----------
// Awalnya mengikuti pengaturan perangkat; setelah tombol ditekan, pilihan disimpan di browser.
(function initTheme() {
  const btn = $('#tbtn'); if (!btn) return;
  const root = document.documentElement, TKEY = 'english7.theme';
  const mq = window.matchMedia ? matchMedia('(prefers-color-scheme: dark)') : null;
  const isDark = () => root.getAttribute('data-theme') === 'dark' || (!root.getAttribute('data-theme') && !!(mq && mq.matches));
  const paint = () => {
    const d = isDark();
    btn.textContent = d ? '☀️ Terang' : '🌙 Gelap';
    btn.setAttribute('aria-pressed', d ? 'true' : 'false');
    btn.title = d ? 'Sekarang mode gelap. Klik untuk mode terang.' : 'Sekarang mode terang. Klik untuk mode gelap.';
  };
  btn.addEventListener('click', () => {
    const next = isDark() ? 'light' : 'dark';
    root.setAttribute('data-theme', next);
    try { localStorage.setItem(TKEY, next); } catch (e) { /* diabaikan */ }
    paint();
  });
  if (mq && mq.addEventListener) mq.addEventListener('change', paint);   // pengaturan perangkat berubah dan belum ada pilihan sendiri
  paint();
})();

// ---------- kemajuan (tersimpan di browser) ----------
const KEY = 'english7.v1';
function loadProg() { try { return JSON.parse(localStorage.getItem(KEY)) || {}; } catch (e) { return {}; } }
let prog = loadProg();
prog.units = prog.units || {};
prog.wrong = prog.wrong || {};   // kunci soal -> id unit, untuk fitur 'Ulangi yang salah'
function saveProg() { try { localStorage.setItem(KEY, JSON.stringify(prog)); } catch (e) { /* diabaikan */ } }
const U = id => (prog.units[id] = prog.units[id] || { learned: false, practice: 0, quiz: 0, stars: 0 });
const starsFor = pct => pct >= 90 ? 3 : pct >= 70 ? 2 : pct >= 50 ? 1 : 0;
const starHtml = n => `<span class="stars" aria-label="${n} dari 3 bintang">${[1, 2, 3].map(i => `<span class="${i <= n ? 'on' : ''}">★</span>`).join('')}</span>`;
function totalStars() { return Object.values(prog.units).reduce((a, u) => a + (u.stars || 0), 0); }

// ---------- data ----------
const cache = {};
async function getJSON(path) {
  if (!cache[path]) {
    const r = await fetch(path, { cache: 'no-cache' });
    if (!r.ok) throw new Error(path + ' ' + r.status);
    cache[path] = await r.json();
  }
  return cache[path];
}

// ---------- router ----------
window.addEventListener('hashchange', route);
route();
async function route() {
  const [, page, id, tab, idx] = location.hash.slice(1).split('/');
  window.scrollTo(0, 0);
  try {
    const index = await getJSON('data/index.json');
    $('#total').textContent = `⭐ ${totalStars()} / ${index.filter(u => u.ready).length * 3}`;
    if (page === 'kelas') return renderKelas(index, id);
    if (page === 'kamus') return renderKamus(await getJSON('data/kamus.json'));
    if (page === 'ulang') return renderRetry(index);
    if (page === 'kartu') return renderKartu();
    if (page === 'tes') return renderTes(index);
    if (page === 'bicara') return renderBicara();
    if (page === 'statistik') return renderStat(index);
    if (page === 'ujian') return renderUjian(index, id);
    if (page === 'unit' && id) {
      const meta = index.find(u => u.id === id && u.ready);
      if (meta) return renderUnit(await getJSON(`data/${id}.json`), tab || 'learn', index, idx);
    }
    renderHome(index);
  } catch (e) {
    app.innerHTML = `<div class="card"><b>Oops!</b> Halaman tidak bisa dimuat. Coba muat ulang.<br><small>${esc(e.message)}</small></div>`;
  }
}

const kelasName = k => k === 'kerja' ? 'Level Pekerja' : k === 'tenses' ? 'Modul Tenses' : k === 'ielts' ? 'Persiapan IELTS' : k === 'pron' ? 'Modul Pelafalan' : k === 'kosa' ? 'Kosakata dan Menulis' : k === 'toeic' ? 'Persiapan TOEIC' : k === 'travel' ? 'Inggris untuk Bepergian' : k === 'skill' ? 'Latihan Keterampilan' : k === 'listen' ? 'Listening Bertahap' : k === 'reader' ? 'Cerita Bertingkat' : k === 'toefl' ? 'Persiapan TOEFL ITP' : k === 'write' ? 'Menulis Lanjutan' : k === 'talk' ? 'Percakapan Interaktif' : k === 'theme' ? 'Tema Mingguan' : `Kelas ${k}`;

// ---------- beranda ----------
function unitCard(u) {
  if (!u.ready) return `<div class="ucard soon"><span class="no">UNIT ${u.no}</span><span class="em">${u.emoji}</span><span class="t">${esc(u.title)}</span><span class="j">${esc(u.judul)}</span><span class="badge">Segera hadir 🔒</span></div>`;
  const p = U(u.id);
  const badge = p.quiz >= 50 ? `<span class="badge done">Selesai ✔ ${p.quiz}%</span>` : p.learned ? `<span class="badge">Sedang belajar</span>` : `<span class="badge">Mulai di sini</span>`;
  return `<a class="ucard" href="#/unit/${u.id}/learn"><span class="no">UNIT ${u.no}</span><span class="em">${u.emoji}</span><span class="t">${esc(u.title)}</span><span class="j">${esc(u.judul)}</span><span class="j">${esc(u.ringkas)}</span>${starHtml(p.stars || 0)}${badge}</a>`;
}

// Level di dashboard. Kelas 7-12 diambil dari index.json; level 'kerja' aktif otomatis
// begitu ada unit dengan kelas: "kerja" di index.json.
const LEVELS = [
  ...[7, 8, 9, 10, 11, 12].map(k => ({ key: String(k), title: `Kelas ${k}`, emoji: ['🎒', '📘', '🧭', '🚀', '🎯', '🎓'][k - 7], sub: k <= 9 ? 'SMP' : 'SMA', desc: ['Sapaan, keluarga, angka dan jam, hobi, makanan, dan arah', 'Lampau, sedang terjadi, perbandingan, rencana, dan surat', 'Narrative, report, passive, conditional, dan persiapan ujian', 'Perkenalan, teks deskriptif, recount, prosedur, dan narasi', 'Eksposisi, berita, surat lamaran, dan CV', 'Pengandaian, pasif, wawancara kerja, dan persiapan ujian'][k - 7] })),
  { key: 'tenses', title: 'Modul Tenses', emoji: '⏱️', sub: 'SEMUA LEVEL', desc: 'Paham 12 tense dari nol: rumus, garis waktu, kontras, dan tes akhir' },
  { key: 'pron', title: 'Modul Pelafalan', emoji: '🔊', sub: 'SEMUA LEVEL', desc: 'Bunyi vokal dan konsonan, tekanan kata dan kalimat, intonasi, dan ejaan yang menipu' },
  { key: 'kosa', title: 'Kosakata dan Menulis', emoji: '📚', sub: 'SEMUA LEVEL', desc: 'Kata yang sering tertukar, pembentukan kata, kosakata per tema, dan menulis terpandu' },
  { key: 'travel', title: 'Inggris untuk Bepergian', emoji: '✈️', sub: 'SEMUA LEVEL', desc: 'Bandara, hotel, restoran, transportasi, belanja, darurat, dan obrolan ringan' },
  { key: 'skill', title: 'Latihan Keterampilan', emoji: '🧩', sub: 'SEMUA LEVEL', desc: 'Urutkan paragraf dan dialog, temukan kesalahan, definisi kata, dan dengar lalu isi' },
  { key: 'listen', title: 'Listening Bertahap', emoji: '🎧', sub: 'SEMUA LEVEL', desc: 'Delapan tahap mendengarkan, dari sapaan sampai kuliah dan diskusi' },
  { key: 'reader', title: 'Cerita Bertingkat', emoji: '📚', sub: 'SEMUA LEVEL', desc: 'Delapan tahap cerita dan artikel pendek, makin lama makin panjang' },
  { key: 'write', title: 'Menulis Lanjutan', emoji: '✍️', sub: 'SEMUA LEVEL', desc: 'Gabungkan kalimat, deskripsi, cerita, esai opini, ringkasan, dan pesan singkat' },
  { key: 'talk', title: 'Percakapan Interaktif', emoji: '🗨️', sub: 'SEMUA LEVEL', desc: 'Balas percakapan dalam bahasa Inggris: kenalan, rumah, sekolah, kerja, dan layanan' },
  { key: 'theme', title: 'Tema Mingguan', emoji: '📅', sub: 'SEMUA LEVEL', desc: 'Satu tema tiap minggu: kosakata, bacaan, dan latihan terpadu' },
  { key: 'ielts', title: 'Persiapan IELTS', emoji: '🌍', sub: 'UJIAN', desc: 'Strategi, reading, listening, kosakata akademik, writing, dan speaking' },
  { key: 'toefl', title: 'Persiapan TOEFL ITP', emoji: '🎓', sub: 'UJIAN KAMPUS', desc: 'Listening, Structure, Written Expression, dan Reading ala TOEFL ITP' },
  { key: 'toeic', title: 'Persiapan TOEIC', emoji: '🏢', sub: 'UJIAN KERJA', desc: 'Format TOEIC, listening, tata bahasa, kosakata bisnis, dan membaca teks kantor' },
  { key: 'kerja', title: 'Pekerja / Formal', emoji: '💼', sub: 'DEWASA', desc: 'Bahasa Inggris untuk kantor, email, rapat, dan wawancara' },
];

function levelStat(index, key) {
  const us = index.filter(u => String(u.kelas) === key), r = us.filter(u => u.ready);
  const stars = r.reduce((a, u) => a + (U(u.id).stars || 0), 0);
  const done = r.filter(u => U(u.id).quiz >= 50).length;
  return { us, ready: r.length, stars, max: r.length * 3, done };
}

function levelCard(index, lv) {
  const st = levelStat(index, lv.key);
  const head = `<span class="lsub">${lv.sub}</span><span class="em">${lv.emoji}</span><span class="t">${esc(lv.title)}</span><span class="j">${esc(lv.desc)}</span>`;
  if (!st.ready) return `<div class="ucard lcard soon">${head}<span class="badge">Segera hadir 🔒</span></div>`;
  const pct = Math.round(100 * st.stars / st.max);
  const last = String(prog.kelas) === lv.key ? '<span class="badge last">Terakhir dibuka</span>' : '';
  return `<a class="ucard lcard" href="#/kelas/${lv.key}" aria-label="${esc(lv.title)}: ${st.done} dari ${st.ready} unit selesai">${head}
    <span class="lprog"><i style="width:${pct}%"></i></span>
    <span class="j">${st.done}/${st.ready} unit selesai · ⭐ ${st.stars}/${st.max}</span>${last}</a>`;
}

function renderHome(index) {
  const ready = index.filter(u => u.ready);
  const got = totalStars(), max = ready.length * 3 || 1;
  app.innerHTML = `
    <section class="hero">
      <h1>Hi! Ayo belajar bahasa Inggris 🎉</h1>
      <p>Pilih levelmu, lalu pilih unit. Setiap unit punya <b>Belajar</b>, <b>Latihan</b>, dan <b>Kuis</b>. Kumpulkan bintang ⭐ sebanyak mungkin!</p>
      <div class="bar" role="progressbar" aria-valuemin="0" aria-valuemax="${max}" aria-valuenow="${got}"><i style="width:${Math.round(100 * got / max)}%"></i></div>
    </section>${dailyCard()}${toolsRow()}${wrongCount() ? `<div class="card retry"><b>🔁 ${wrongCount()} soal perlu diulang</b> <a class="btn small" href="#/ulang">Ulangi yang salah</a></div>` : ''}
    <h2 class="sec">Pilih level</h2>
    <div class="grid lgrid">${LEVELS.map(lv => levelCard(index, lv)).join('')}</div>`;
  bindHome(index);
}

function renderKelas(index, key) {
  const lv = LEVELS.find(l => l.key === key);
  const st = lv && levelStat(index, key);
  if (!lv || !st.ready) return renderHome(index);
  if (String(prog.kelas) !== key) { prog.kelas = key; saveProg(); }
  const i = LEVELS.findIndex(l => l.key === key);
  const nb = (l, txt) => l && levelStat(index, l.key).ready ? `<a class="btn ghost small" href="#/kelas/${l.key}">${txt}</a>` : '<span></span>';
  app.innerHTML = `
    <a class="crumb" href="#/">← Semua level</a>
    <h1>${lv.emoji} ${esc(lv.title)}</h1>
    <p class="lead">${lv.sub} · ${st.done}/${st.ready} unit selesai · ⭐ ${st.stars}/${st.max}</p>
    <div class="row"><a class="btn ghost small" href="#/ujian/${key}">📝 Mode ujian${(prog.exam || {})[key] ? ` (terbaik ${prog.exam[key].best}%)` : ''}</a></div>
    <section class="kelas"><div class="grid">${st.us.map(unitCard).join('')}</div></section>
    <div class="row lnav">${nb(LEVELS[i - 1], '← ' + (LEVELS[i - 1] || {}).title)}${nb(LEVELS[i + 1], (LEVELS[i + 1] || {}).title + ' →')}</div>`;
}

// ---------- kamus ----------
function renderKamus(words) {
  app.innerHTML = `<a class="crumb" href="#/">← Beranda</a><h1>📖 Kamus Kecil</h1>
    <p class="lead">${words.length} kata dari semua unit. Klik kata untuk mendengarnya.</p>
    <div class="row"><input class="blank" id="kq" type="search" placeholder="Cari kata Inggris atau artinya…" aria-label="Cari kata"></div>
    <div id="klist"></div>`;
  const list = $('#klist'), q = $('#kq');
  function draw() {
    const t = norm(q.value);
    const hit = t ? words.filter(w => norm(w.en).includes(t) || norm(w.id).includes(t)) : words;
    list.innerHTML = hit.length
      ? `<div class="vgrid">${hit.map(w => `<button class="vcard" data-say="${esc(stripTags(w.en))}"><span class="v-en">${esc(w.en)}</span><span class="v-id">${esc(w.id)}</span>${w.ex ? `<span class="v-ex">${esc(w.ex)}</span>` : ''}<span class="v-ex">Unit ${w.no} · ${kelasName(w.kelas)}</span></button>`).join('')}</div>`
      : '<p class="hint">Kata tidak ditemukan.</p>';
  }
  q.addEventListener('input', draw);
  draw();
}

// ---------- ulangi yang salah ----------
const wrongCount = () => Object.keys(prog.wrong).length;
async function renderRetry() {
  const ids = [...new Set(Object.values(prog.wrong))].filter(id => id !== 'ulang');   // 'ulang' = sisa data dari bug lama
  for (const k of Object.keys(prog.wrong)) if (prog.wrong[k] === 'ulang') delete prog.wrong[k];
  const pool = [];
  for (const id of ids) {
    const d = await getJSON(`data/${id}.json`);
    for (const q of d.practice.concat(d.quiz)) if (q.k && prog.wrong[q.k] === id) pool.push({ ...q, unit: id });
  }
  const seen = new Set(), qs = pool.filter(q => !seen.has(q.k) && seen.add(q.k));
  const live = new Set(qs.map(q => q.k));
  for (const k of Object.keys(prog.wrong)) if (!live.has(k)) delete prog.wrong[k];   // soal yang sudah tidak ada
  saveProg();
  if (!qs.length) {
    app.innerHTML = `<a class="crumb" href="#/">← Beranda</a><div class="card result"><div class="big">🌟</div><h2>Tidak ada soal yang perlu diulang</h2><p>Semua jawabanmu sudah benar. Lanjutkan belajar ya!</p></div>`;
    return;
  }
  app.innerHTML = `<a class="crumb" href="#/">← Beranda</a><h1>🔁 Ulangi yang salah</h1><p class="lead">${qs.length} soal yang pernah salah. Jawab benar untuk menghapusnya dari daftar.</p><div id="pane"></div>`;
  runner($('#pane'), { id: 'ulang', practice: qs, quiz: [] }, 'practice');
}

// ---------- unit ----------
function renderUnit(d, tab, index, idx) {
  const tabs = [['learn', '📖 Belajar'], ['practice', '✏️ Latihan'], ['quiz', '🏆 Kuis']];
  if (d.read && d.read.length) tabs.splice(2, 0, ['read', '📚 Bacaan']);
  app.innerHTML = `
    <a class="crumb" href="#/kelas/${d.kelas}">← ${kelasName(d.kelas)}</a>
    <h1>${d.emoji} Unit ${d.no}: ${esc(d.title)}</h1>
    <p class="lead">${kelasName(d.kelas)} · ${esc(d.judul)}</p>
    <nav class="tabs">${tabs.map(([k, l]) => `<a class="${tab === k ? 'on' : ''}" href="#/unit/${d.id}/${k}">${l}</a>`).join('')}</nav>
    <div id="pane"></div>`;
  const pane = $('#pane');
  if (tab === 'practice') return runner(pane, d, 'practice');
  if (tab === 'quiz') return runner(pane, d, 'quiz');
  if (tab === 'read' && d.read && d.read.length) return renderRead(pane, d, idx);
  renderLesson(pane, d);
}

function renderLesson(pane, d) {
  const p = U(d.id); if (!p.learned) { p.learned = true; saveProg(); }
  const goals = `<div class="card"><b>Setelah unit ini kamu bisa:</b><ul class="goals">${d.goals.map(g => `<li>${fmt(g)}</li>`).join('')}</ul></div>`;
  pane.innerHTML = goals + d.lesson.map(blockHtml).join('') +
    `<div class="nextrow"><a class="btn" href="#/unit/${d.id}/practice">Mulai Latihan →</a></div>`;
  pane.querySelectorAll('.dialog .toggle').forEach(b => b.addEventListener('click', () => {
    const dl = b.closest('.dialog'); dl.classList.toggle('show');
    b.textContent = dl.classList.contains('show') ? 'Sembunyikan terjemahan' : 'Tampilkan terjemahan';
  }));
}

function blockHtml(b) {
  switch (b.t) {
    case 'intro': return `<div class="card">${fmt(b.text)}</div>`;
    case 'h': return `<h2>${esc(b.text)}</h2>`;
    case 'p': return `<p>${fmt(b.text)}</p>`;
    case 'tip': case 'warn':
      return `<div class="callout ${b.t}"><b class="h">${b.t === 'tip' ? '💡 Tips' : '⚠️ Awas!'}${b.title ? ': ' + esc(b.title) : ''}</b>${fmt(b.text)}</div>`;
    case 'vocab':
      return `<h2>${esc(b.title)}</h2><div class="vgrid">${b.items.map(i =>
        `<button class="vcard" data-say="${esc(stripTags(i.en))}"><span class="v-en">${esc(i.en)}</span><span class="v-id">${esc(i.id)}</span>${i.ex ? `<span class="v-ex">${esc(i.ex)}</span>` : ''}</button>`).join('')}</div>`;
    case 'dialog': {
      const names = [...new Set(b.lines.map(l => l.who))];
      return `<div class="card dialog"><div class="dhead"><h3 style="margin:0">${esc(b.title)}</h3><button class="btn ghost small toggle">Tampilkan terjemahan</button></div>${b.lines.map(l => {
        const right = names.indexOf(l.who) % 2 === 1;
        return `<div class="bubble ${right ? 'r' : ''}"><div class="avatar">${esc(l.who[0])}</div><div class="msg" data-say="${esc(l.en)}" data-g="${genderOf(l.who)}"><div class="who">${esc(l.who)}</div><div class="e">${esc(l.en)}</div><div class="tr">${esc(l.id)}</div></div></div>`;
      }).join('')}</div>`;
    }
    case 'grammar': {
      let h = `<h2>${esc(b.title)}</h2><div class="card">`;
      if (b.text) h += b.text.split('\n').map(x => `<p>${fmt(x)}</p>`).join('');
      if (b.table) h += `<div class="tw"><table><thead><tr>${b.table[0].map(c => `<th>${fmt(c)}</th>`).join('')}</tr></thead><tbody>${b.table.slice(1).map(r => `<tr>${r.map(c => `<td>${fmt(c)}</td>`).join('')}</tr>`).join('')}</tbody></table></div>`;
      if (b.examples) h += b.examples.map(e => `<div class="ex">${fmt(e.en)}<small>${esc(e.id)}</small></div>`).join('');
      return h + '</div>';
    }
    case 'alphabet':
      return `<h2>${esc(b.title)}</h2><div class="alpha">${b.letters.map(([l, r]) => `<button data-say="${esc(l)}"><b>${esc(l)}</b><small>${esc(r)}</small></button>`).join('')}</div>`;
    case 'summary':
      return `<h2>${esc(b.title || 'Rangkuman')}</h2><div class="card"><ul class="goals">${b.items.map(i => `<li>${fmt(i)}</li>`).join('')}</ul></div>`;
    default: return '';
  }
}

// ---------- pelatihan dan kuis ----------
function runner(pane, d, mode) {
  const isQuiz = mode === 'quiz';
  const src = isQuiz ? d.quiz : d.practice;
  const retry = d.id === 'ulang';
  const N = retry ? 10 : isQuiz ? 50 : 50;                       // jumlah soal tiap sesi, diambil acak dari bank soal
  // soal yang diturunkan dari satu soal (pilihan ganda dan isian) berbagi `g`; ambil salah satu saja per sesi
  const pick = () => { const seen = new Set(); return shuffle(src).filter(q => !q.g || (!seen.has(q.g) && seen.add(q.g))).slice(0, N); };
  let qs = pick();
  let i = 0, score = 0, wrong = [];

  function show() {
    closeWordPop();
    if (i >= qs.length) return finish();
    const q = qs[i];
    pane.innerHTML = `
      <div class="qhead"><span class="qno">${isQuiz ? '🏆 Kuis' : '✏️ Latihan'} ${i + 1}/${qs.length}</span><div class="pbar"><i style="width:${Math.round(100 * i / qs.length)}%"></i></div></div>
      <div class="card"><div id="qbox"></div><div id="fb"></div></div>`;
    renderQ(q, $('#qbox'), (ok, shown) => {
      if (ok) score++; else wrong.push({ q, shown });
      bumpDaily();
      if (q.k) { if (ok) delete prog.wrong[q.k]; else prog.wrong[q.k] = q.unit || d.id; saveProg(); }
      const last = i === qs.length - 1;
      $('#fb').innerHTML = `<div class="fb ${ok ? 'ok' : 'bad'}"><b class="h">${ok ? '✅ Benar! Hebat!' : '❌ Belum tepat'}</b>${ok ? '' : `<div>Jawaban yang benar: <b>${esc(correctText(q))}</b></div>`}<div>${fmt(q.exp)}</div></div>
        <div class="nextrow"><button class="btn" id="next">${last ? 'Lihat hasil' : 'Lanjut →'}</button></div>`;
      const nb = $('#next'); nb.focus();
      nb.addEventListener('click', () => { i++; show(); });
    });
  }

  function finish() {
    const pct = Math.round(100 * score / qs.length);
    const p = retry ? {} : U(d.id);
    let extra = '';
    if (retry) {
      extra = `<p>${pct >= 70 ? 'Hebat! Soal yang benar sudah dihapus dari daftar ulangan 🎉' : 'Terus coba, soal yang masih salah akan muncul lagi 💪'}</p>`;
    } else if (isQuiz) {
      const st = starsFor(pct);
      p.quiz = Math.max(p.quiz || 0, pct); p.stars = Math.max(p.stars || 0, starsFor(p.quiz));
      saveProg();
      extra = `<div class="stars">${[1, 2, 3].map(n => `<span class="${n <= st ? 'on' : ''}">★</span>`).join('')}</div>
        <p>${st === 3 ? 'Luar biasa! Kamu menguasai unit ini! 🎉' : st === 2 ? 'Bagus sekali! Sedikit lagi sempurna 👍' : st === 1 ? 'Lumayan! Baca lagi bagian Belajar, lalu coba lagi 💪' : 'Jangan menyerah! Baca lagi bagian Belajar, lalu coba lagi 💪'}</p>`;
    } else {
      p.practice = Math.max(p.practice || 0, pct); saveProg();
      extra = `<p>${pct >= 70 ? 'Mantap! Kamu siap mencoba kuis 🏆' : 'Ulangi latihan sampai terasa mudah, lalu coba kuis ya 😊'}</p>`;
    }
    const review = wrong.length ? `<h3>Yang perlu diulang:</h3><ol class="review">${wrong.map(w => `<li>${fmt(w.q.q || w.q.say || '')}<br>Jawaban benar: <b>${esc(correctText(w.q))}</b></li>`).join('')}</ol>` : '';
    pane.innerHTML = `<div class="card result"><div class="big">${pct >= 70 ? '🎉' : '💪'}</div><h2>${score} dari ${qs.length} benar (${pct}%)</h2>${extra}
      <div class="row" style="justify-content:center;margin-top:12px">
        ${retry ? '' : `<a class="btn ghost" href="#/unit/${d.id}/learn">📖 Baca lagi</a>`}
        <button class="btn" id="again">🔁 Ulangi</button>
        ${retry ? '' : `<a class="btn" href="#/unit/${d.id}/${isQuiz ? 'practice' : 'quiz'}">${isQuiz ? '✏️ Latihan' : '🏆 Ke kuis'}</a>`}
        <a class="btn ghost" href="#/">🏠 Beranda</a></div></div>${review ? `<div class="card review">${review}</div>` : ''}`;
    $('#again').addEventListener('click', () => { if (retry) return renderRetry(); qs = pick(); i = 0; score = 0; wrong = []; show(); });
    // perbarui lencana total
    getJSON('data/index.json').then(ix => { $('#total').textContent = `⭐ ${totalStars()} / ${ix.filter(u => u.ready).length * 3}`; });
  }
  show();
}

// ---------- bacaan: teks pendek + beberapa pertanyaan ----------
// ---------- popup kata di bacaan ----------
// Klik atau blok kata/frasa di teks bacaan: muncul kartu berisi cara baca (IPA + ejaan Indonesia), suara, arti, dan definisi Inggris.
const WORD_SPLIT = /([A-Za-z]+(?:'[A-Za-z]+)*)/;
const wrapWords = line => line.split(WORD_SPLIT).map((t, i) => i % 2 ? `<span class="w" data-w="${esc(t)}">${esc(t)}</span>` : esc(t)).join('');
const WORDS_KEY = 'english7.words';
let wordsOnline = {};
try { wordsOnline = JSON.parse(localStorage.getItem(WORDS_KEY) || '{}'); } catch (e) { wordsOnline = {}; }
function saveWordsOnline() { try { localStorage.setItem(WORDS_KEY, JSON.stringify(wordsOnline)); } catch (e) { /* penyimpanan penuh: abaikan */ } }
function lemmaCandidates(w) {
  const c = [], add = x => { if (x.length > 1 && !c.includes(x)) c.push(x); };
  add(w);
  if (w.endsWith("'s")) add(w.slice(0, -2));
  if (w.endsWith('ies')) add(w.slice(0, -3) + 'y');
  if (w.endsWith('es')) add(w.slice(0, -2));
  if (w.endsWith('s')) add(w.slice(0, -1));
  if (w.endsWith('ed')) { add(w.slice(0, -2)); add(w.slice(0, -1)); if (/(.)\1ed$/.test(w)) add(w.slice(0, -3)); if (w.endsWith('ied')) add(w.slice(0, -3) + 'y'); }
  if (w.endsWith('ing')) { add(w.slice(0, -3)); add(w.slice(0, -3) + 'e'); if (/(.)\1ing$/.test(w)) add(w.slice(0, -4)); }
  if (w.endsWith('ly')) add(w.slice(0, -2));
  return c;
}
let kamusMap = null;
async function localWord(raw) {
  const w = raw.toLowerCase();
  let kata = {}, kam = [];
  try { kata = await getJSON('data/kata.json'); } catch (e) { /* tanpa data lokal */ }
  if (!kamusMap) {
    try { kam = await getJSON('data/kamus.json'); } catch (e) { /* tanpa kamus */ }
    kamusMap = {};
    kam.forEach(k => { const key = k.en.toLowerCase().replace(/^(a|an|the|to)\s+/, ''); if (!(key in kamusMap)) kamusMap[key] = k.id; });
  }
  const own = kata[w] || ['', '', ''];
  const info = { ipa: own[0], say: own[1], mean: own[2], from: '' };
  if (!info.mean && kamusMap[w]) info.mean = kamusMap[w];
  if (!info.mean) {
    for (const l of lemmaCandidates(w).slice(1)) {
      const m = (kata[l] && kata[l][2]) || kamusMap[l];
      if (m) { info.mean = m; info.from = l; break; }
    }
  }
  if (!info.ipa) for (const l of lemmaCandidates(w).slice(1)) if (kata[l] && kata[l][0]) { info.ipa = kata[l][0]; info.say = kata[l][1]; break; }
  return info;
}
async function onlineWord(raw, needMean) {
  const key = raw.toLowerCase();
  const hit = wordsOnline[key] || {};
  const out = { mean: hit.mean || '', pos: hit.pos || '', def: hit.def || '', ipa: hit.ipa || '' };
  const ft = (url) => Promise.race([fetch(url).then(r => r.ok ? r.json() : null), new Promise(res => setTimeout(() => res(null), 6000))]).catch(() => null);
  const jobs = [];
  if (!hit.done && !/\s/.test(key)) {
    jobs.push((async () => {
      for (const l of lemmaCandidates(key).slice(0, 3)) {
        const d = await ft('https://api.dictionaryapi.dev/api/v2/entries/en/' + encodeURIComponent(l));
        if (Array.isArray(d) && d.length) {
          const e = d[0], m = (e.meanings || [])[0];
          out.ipa = out.ipa || e.phonetic || ((e.phonetics || []).find(p => p.text) || {}).text || '';
          if (m && m.definitions && m.definitions[0]) { out.pos = m.partOfSpeech || ''; out.def = m.definitions[0].definition || ''; }
          break;
        }
      }
    })());
  }
  if (needMean && !out.mean) {
    jobs.push((async () => {
      const d = await ft('https://api.mymemory.translated.net/get?langpair=en|id&q=' + encodeURIComponent(raw));
      const t = d && d.responseData && d.responseData.translatedText;
      if (t && t.toLowerCase() !== key && !/MYMEMORY|INVALID/i.test(t)) out.mean = t;
    })());
  }
  await Promise.all(jobs);
  if (out.mean || out.def) { wordsOnline[key] = { ...out, done: true }; saveWordsOnline(); }
  return out;
}
let wpopEl = null, wpopToken = 0, wpopMark = null;
function closeWordPop() {
  wpopToken++;
  if (wpopEl) { wpopEl.remove(); wpopEl = null; }
  if (wpopMark) { wpopMark.classList.remove('on'); wpopMark = null; }
}
async function showWordPop(text, rect, mark) {
  closeWordPop();
  const token = wpopToken;
  const phrase = /\s/.test(text);
  if (mark) { mark.classList.add('on'); wpopMark = mark; }
  const el = wpopEl = document.createElement('div');
  el.className = 'wpop'; el.setAttribute('role', 'dialog');
  document.body.appendChild(el);
  const local = phrase ? { ipa: '', say: '', mean: '', from: '' } : await localWord(text);
  if (token !== wpopToken) return;
  const draw = (on) => {
    if (token !== wpopToken) return;
    const mean = local.mean || (on && on.mean) || '';
    const ipa = local.ipa || (on && on.ipa) || '';
    el.innerHTML = `<div class="wp-head"><b class="wp-word">${esc(text)}</b><button class="wp-x" aria-label="Tutup">×</button></div>
      ${ipa || local.say ? `<div class="wp-ipa">${ipa ? `<span>${esc(ipa)}</span>` : ''}${local.say ? `<span class="wp-say" title="Huruf besar = bagian yang ditekan. Ini hanya perkiraan; dengarkan suaranya.">dibaca: <b>${esc(local.say)}</b></span>` : ''}</div>` : ''}
      ${hasTTS ? `<div class="wp-btns"><button class="btn small" data-a="s">🔊 Dengarkan</button> <button class="btn ghost small" data-a="sl">🐢 Pelan</button></div>` : '<div class="hint">Suara tidak tersedia di perangkat ini.</div>'}
      <div class="wp-mean">${mean ? `<b>Arti:</b> ${esc(mean)}${local.from ? ` <small class="hint">(bentuk dari ${esc(local.from)})</small>` : ''}` : (on ? '<small class="hint">Arti belum ditemukan. Coba blok seluruh frasanya, atau periksa sambungan internet.</small>' : '<small class="hint">Mencari arti…</small>')}</div>
      ${on && on.def ? `<div class="wp-def"><small>${esc(on.pos)}${on.pos ? ' · ' : ''}${esc(on.def)}</small></div>` : ''}`;
    $('.wp-x', el).addEventListener('click', closeWordPop);
    const b1 = $('[data-a=s]', el), b2 = $('[data-a=sl]', el);
    if (b1) b1.addEventListener('click', () => speak(text));
    if (b2) b2.addEventListener('click', () => speakSlow(text));
    place(el, rect);
  };
  draw(null);
  if (hasTTS) speak(text);
  const on = await onlineWord(text, !local.mean);
  draw(on);
}
function place(el, rect) {
  const pad = 8, w = el.offsetWidth, h = el.offsetHeight;
  let left = Math.min(Math.max(pad, rect.left + rect.width / 2 - w / 2), window.innerWidth - w - pad);
  let top = rect.bottom + pad;
  if (top + h > window.innerHeight - pad) top = Math.max(pad, rect.top - h - pad);
  el.style.left = left + 'px'; el.style.top = top + 'px';
}
let wordPopUnbind = null;
function bindWordPop(box) {
  if (wordPopUnbind) wordPopUnbind();
  let selTimer = 0;
  const inBox = n => n && box.contains(n.nodeType === 3 ? n.parentNode : n);
  box.addEventListener('click', e => {
    const sel = String(window.getSelection()).trim();
    if (sel) return;                                   // ada blok teks: ditangani selectionchange
    const w = e.target.closest && e.target.closest('.w');
    if (w) { e.stopPropagation(); showWordPop(w.dataset.w, w.getBoundingClientRect(), w); }
  });
  const onSel = () => {
    clearTimeout(selTimer);
    selTimer = setTimeout(() => {
      const s = window.getSelection();
      const t = String(s).replace(/\s+/g, ' ').trim();
      if (!t || !s.rangeCount || !inBox(s.anchorNode) || !inBox(s.focusNode)) return;
      if (!/[A-Za-z]/.test(t) || t.split(' ').length > 6 || t.length > 60) return;
      showWordPop(t.replace(/^[^A-Za-z]+|[^A-Za-z.!?']+$/g, ''), s.getRangeAt(0).getBoundingClientRect(), null);
    }, 450);
  };
  document.addEventListener('selectionchange', onSel);
  wordPopUnbind = () => { clearTimeout(selTimer); document.removeEventListener('selectionchange', onSel); wordPopUnbind = null; };
}
document.addEventListener('click', e => { if (wpopEl && !wpopEl.contains(e.target) && !(e.target.closest && e.target.closest('.w'))) closeWordPop(); });
document.addEventListener('keydown', e => { if (e.key === 'Escape') closeWordPop(); });
window.addEventListener('scroll', () => closeWordPop(), true);
window.addEventListener('resize', closeWordPop);
window.addEventListener('hashchange', closeWordPop);

function renderRead(pane, d, idx) {
  const rs = (U(d.id).reads = U(d.id).reads || {});
  const n = +idx;
  if (!(n >= 0 && n < d.read.length)) {
    pane.innerHTML = `<p class="lead">Baca teks pendek, lalu jawab pertanyaannya. Klik 🔊 untuk mendengarkan, dan buka terjemahan bila perlu.</p>
      <div class="grid">${d.read.map((p, i) => `<a class="ucard" href="#/unit/${d.id}/read/${i}"><span class="no">BACAAN ${i + 1}</span><span class="t">${esc(p.title)}</span>${p.focus ? `<span class="j">🕐 Fokus: ${esc(p.focus)}</span>` : ''}<span class="j">${p.qs.length} pertanyaan${p.qs.some(q => q.type !== 'mcq') ? ' · beragam' : ''}</span><span class="badge ${rs[i] >= 70 ? 'done' : ''}">${rs[i] == null ? 'Belum dicoba' : 'Terbaik ' + rs[i] + '%'}</span></a>`).join('')}</div>`;
    return;
  }
  const ps = d.read[n];
  const qs = shuffle(ps.qs);
  let i = 0, score = 0, wrong = [];
  const textHtml = `<div class="card passage"><div class="dhead"><div><h3 style="margin:0">${esc(ps.title)}</h3>${ps.focus ? `<small class="hint">🕐 Fokus tenses: ${esc(ps.focus)}</small>` : ''}</div><span><button class="btn ghost small" id="ttsp">🔊 Dengarkan</button> <button class="btn ghost small" id="trtog">Tampilkan terjemahan</button></span></div>
    <small class="hint">💡 Klik atau blok kata yang belum kamu mengerti untuk melihat arti, cara baca, dan suaranya.</small><div class="ptext">${ps.text.split('\n').map(x => { const m = x.match(/^([A-Z][A-Za-z.' ]{0,24}:) (.*)$/); return m ? `<p><b class="spk">${esc(m[1])}</b> ${wrapWords(m[2])}</p>` : `<p>${wrapWords(x)}</p>`; }).join('')}</div><div class="tr-box" id="trbox" hidden>${ps.id.split('\n').map(x => { const m = x.match(/^([A-Z][A-Za-z.' ]{0,24}:) (.*)$/); return m ? `<p><b class="spk">${esc(m[1])}</b> ${esc(m[2])}</p>` : `<p>${esc(x)}</p>`; }).join('')}</div></div>`;
  function show() {
    if (i >= qs.length) return finish();
    const q = qs[i];
    pane.innerHTML = `<a class="crumb" href="#/unit/${d.id}/read">← Semua bacaan</a>${textHtml}
      <div class="qhead"><span class="qno">📚 Pertanyaan ${i + 1}/${qs.length}</span><div class="pbar"><i style="width:${Math.round(100 * i / qs.length)}%"></i></div></div>
      <div class="card"><div id="qbox"></div><div id="fb"></div></div>`;
    $('#ttsp').addEventListener('click', () => speakSeq(parseSpeakers(ps.text.replace(/\n+/g, ' '))));
    bindWordPop($('.ptext', pane));
    $('#trtog').addEventListener('click', e => { const b = $('#trbox'); b.hidden = !b.hidden; e.target.textContent = b.hidden ? 'Tampilkan terjemahan' : 'Sembunyikan terjemahan'; });
    renderQ(q, $('#qbox'), ok => {
      if (ok) score++; else wrong.push(q);
      const last = i === qs.length - 1;
      $('#fb').innerHTML = `<div class="fb ${ok ? 'ok' : 'bad'}"><b class="h">${ok ? '✅ Benar! Hebat!' : '❌ Belum tepat'}</b>${ok ? '' : `<div>Jawaban yang benar: <b>${esc(correctText(q))}</b></div>`}<div>${fmt(q.exp)}</div></div>
        <div class="nextrow"><button class="btn" id="next">${last ? 'Lihat hasil' : 'Lanjut →'}</button></div>`;
      const nb = $('#next'); nb.focus(); nb.addEventListener('click', () => { i++; show(); });
    });
  }
  function finish() {
    const pct = Math.round(100 * score / qs.length);
    rs[n] = Math.max(rs[n] == null ? 0 : rs[n], pct); saveProg();
    const nxt = n + 1 < d.read.length ? `<a class="btn" href="#/unit/${d.id}/read/${n + 1}">Bacaan berikutnya →</a>` : '';
    pane.innerHTML = `<div class="card result"><div class="big">${pct >= 70 ? '🎉' : '💪'}</div><h2>${score} dari ${qs.length} benar (${pct}%)</h2>
      <p>${pct >= 70 ? 'Mantap! Kamu memahami bacaan ini 👍' : 'Baca teksnya sekali lagi, lalu coba lagi 💪'}</p>
      <div class="row" style="justify-content:center;margin-top:12px"><button class="btn ghost" id="again">🔁 Ulangi</button>${nxt}<a class="btn ghost" href="#/unit/${d.id}/read">📚 Semua bacaan</a></div></div>
      ${wrong.length ? `<div class="card review"><h3>Yang perlu diulang:</h3><ol class="review">${wrong.map(q => `<li>${fmt(q.q)}<br>Jawaban benar: <b>${esc(correctText(q))}</b></li>`).join('')}</ol></div>` : ''}`;
    $('#again').addEventListener('click', () => renderRead(pane, d, String(n)));
  }
  show();
}

function correctText(q) {
  switch (q.type) {
    case 'mcq': case 'listen': return q.options[q.answer];
    case 'fill': return q.answers[0];
    case 'order': return q.answer;
    case 'dictate': return q.answer;
    case 'reply': return q.answers.slice(0, 3).join('  /  ');
    case 'match': return q.pairs.map(([a, b]) => `${a} = ${b}`).join(' · ');
    case 'seq': return q.items.join(' ');
    case 'spot': return q.items[q.answer];
    case 'cloze': return q.answers.map(a => a[0]).join(', ');
  }
  return '';
}

function renderQ(q, box, done) {
  const finish = (() => { let used = false; return (ok, shown) => { if (!used) { used = true; done(ok, shown); } }; })();
  if (q.type === 'mcq' || q.type === 'listen') return qMcq(q, box, finish);
  if (q.type === 'fill') return qFill(q, box, finish);
  if (q.type === 'order') return qOrder(q, box, finish);
  if (q.type === 'match') return qMatch(q, box, finish);
  if (q.type === 'dictate') return qDictate(q, box, finish);
  if (q.type === 'reply') return qReply(q, box, finish);
  if (q.type === 'seq') return qSeq(q, box, finish);
  if (q.type === 'spot') return qSpot(q, box, finish);
  if (q.type === 'cloze') return qCloze(q, box, finish);
}

function qMcq(q, box, finish) {
  const opts = shuffle(q.options.map((t, idx) => ({ t, idx })));
  const play = q.type === 'listen' ? `<button class="btn play" data-say="${esc(q.say)}">🔊 Dengarkan</button> ` : '';
  box.innerHTML = `<div class="qtext">${fmt(q.q)}</div>${play}<div class="opts">${opts.map(o => `<button class="opt" data-i="${o.idx}">${esc(o.t)}</button>`).join('')}</div>`;
  if (q.type === 'listen') setTimeout(() => speak(q.say), 250);
  box.querySelectorAll('.opt').forEach(b => b.addEventListener('click', () => {
    const idx = +b.dataset.i, ok = idx === q.answer;
    box.querySelectorAll('.opt').forEach(x => { x.disabled = true; if (+x.dataset.i === q.answer) x.classList.add('ok'); });
    if (!ok) b.classList.add('bad');
    finish(ok, q.options[idx]);
  }));
}

function qFill(q, box, finish) {
  const sent = esc(q.q).replace('___', '<u>&nbsp;&nbsp;&nbsp;&nbsp;</u>');
  box.innerHTML = `<div class="qtext">${q.id ? esc(q.id) : 'Lengkapi kalimat berikut:'}</div><div class="sent">${sent}</div>
    <div class="row"><input class="blank" type="text" autocomplete="off" autocapitalize="off" spellcheck="false" aria-label="Jawabanmu" placeholder="Ketik jawabanmu…"><button class="btn" id="chk">Cek</button></div>${q.hint ? `<div class="hint">💡 Petunjuk: ${esc(q.hint)}</div>` : ''}`;
  const inp = $('input', box), btn = $('#chk', box);
  inp.focus();
  const check = () => {
    const v = inp.value; if (!norm(v)) { inp.focus(); return; }
    const ok = q.answers.some(a => norm(a) === norm(v));
    inp.disabled = true; btn.disabled = true; inp.classList.add(ok ? 'ok' : 'bad');
    finish(ok, v);
  };
  btn.addEventListener('click', check);
  inp.addEventListener('keydown', e => { if (e.key === 'Enter') check(); });
}

// jarak edit antar kata, untuk memaafkan salah ketik kecil
function lev(a, b) {
  const m = a.length, n = b.length; let prev = Array.from({ length: n + 1 }, (_, j) => j);
  for (let i = 1; i <= m; i++) { const cur = [i]; for (let j = 1; j <= n; j++) cur[j] = Math.min(prev[j] + 1, cur[j - 1] + 1, prev[j - 1] + (a[i - 1] === b[j - 1] ? 0 : 1)); prev = cur; }
  return prev[n];
}
// balasan benar bila (1) hampir sama dengan salah satu jawaban contoh, atau (2) kalimat lengkap yang memuat kata kunci tiap kelompok
function gradeReply(v, q) {
  const e = expand(v);
  if (q.answers.some(a => { const x = expand(a); return e === x || lev(e, x) <= Math.max(1, Math.floor(x.length * 0.08)); })) return true;
  if (!q.keys) return false;
  const padded = ' ' + e + ' ';
  const wantsNeg = q.keys.some(g => g.some(w => /^(not|cannot|never|no)$/.test(w)));
  if (!wantsNeg && /\b(not|never|no|cannot)\b/.test(e)) return false;   // "I am not fine" bukan balasan untuk 'baik-baik saja'
  return e.split(' ').length >= (q.min || 3) && q.keys.every(g => g.some(w => padded.includes(' ' + w + ' ')));
}
function qReply(q, box, finish) {
  const bub = ([who, text], i) => {
    const mine = who === 'You';
    return `<div class="bubble ${mine ? 'r' : ''}"><div class="avatar">${esc(who[0])}</div><div class="msg" data-say="${esc(text)}" data-g="${genderOf(who)}"><div class="who">${esc(who)}</div><div class="e">${esc(text)}</div></div></div>`;
  };
  box.innerHTML = `<div class="qtext">💬 ${esc(q.scene)}</div><div class="dialog-q">${q.turns.map(bub).join('')}</div>
    <div class="hint">Balas dengan bahasa Inggris: <b>${esc(q.id)}</b></div>
    <div class="row"><input class="blank reply" type="text" autocomplete="off" autocapitalize="off" spellcheck="false" aria-label="Balasanmu" placeholder="Ketik balasanmu…"><button class="btn" id="chk">Cek</button></div>
    <div class="hint">Tulis kalimat lengkap. Banyak balasan bisa benar; contoh jawaban muncul setelah kamu mengecek.</div>`;
  const inp = $('input', box), btn = $('#chk', box);
  const last = q.turns[q.turns.length - 1];
  if (hasTTS) setTimeout(() => speak(last[1], genderOf(last[0])), 250);
  inp.focus();
  const check = () => {
    const v = inp.value; if (!norm(v)) { inp.focus(); return; }
    const ok = gradeReply(v, q);
    inp.disabled = true; btn.disabled = true; inp.classList.add(ok ? 'ok' : 'bad');
    finish(ok, v);
  };
  btn.addEventListener('click', check);
  inp.addEventListener('keydown', e => { if (e.key === 'Enter') check(); });
}

function qDictate(q, box, finish) {
  const nW = q.answer.split(/\s+/).length;
  box.innerHTML = `<div class="qtext">${esc(q.q)}</div>
    ${hasTTS ? `<div class="row"><button class="btn play" data-say="${esc(q.say)}" id="dplay">🔊 Dengarkan</button><button class="btn ghost" id="dslow">🐢 Pelan</button></div>`
      : `<div class="hint">Browser ini tidak mendukung suara, jadi kalimatnya ditampilkan untuk disalin: <b>${esc(q.say)}</b></div>`}
    <div class="row"><input class="blank dict" type="text" autocomplete="off" autocapitalize="off" spellcheck="false" aria-label="Kalimat yang kamu dengar" placeholder="Ketik kalimatnya…"><button class="btn" id="chk">Cek</button></div>
    <div class="hint">💡 Jumlah kata: ${nW}. Tanda baca dan huruf besar tidak dinilai.</div>`;
  const inp = $('input', box), btn = $('#chk', box);
  $('#dslow', box) && $('#dslow', box).addEventListener('click', () => speakSlow(q.say));
  if (hasTTS) setTimeout(() => speak(q.say), 250);
  inp.focus();
  const check = () => {
    const v = inp.value; if (!norm(v)) { inp.focus(); return; }
    const ok = expand(v) === expand(q.answer);
    inp.disabled = true; btn.disabled = true; inp.classList.add(ok ? 'ok' : 'bad');
    finish(ok, v);
  };
  btn.addEventListener('click', check);
  inp.addEventListener('keydown', e => { if (e.key === 'Enter') check(); });
}

function qOrder(q, box, finish) {
  const words = q.answer.split(/\s+/).concat(q.extra || []);
  let bank = shuffle(words.map((w, i) => ({ w, i, used: false }))), ans = [];
  box.innerHTML = `<div class="qtext">${fmt(q.q)}</div><div class="chips ans" id="ans" aria-label="Kalimatmu"></div><div class="chips" id="bank"></div>
    <div class="row"><button class="btn" id="chk" disabled>Cek</button><button class="btn ghost" id="clr">Hapus semua</button></div>`;
  const aEl = $('#ans', box), bEl = $('#bank', box), chk = $('#chk', box), clr = $('#clr', box);
  let locked = false;
  function draw() {
    aEl.innerHTML = ans.map(x => `<button class="chip" data-i="${x.i}">${esc(x.w)}</button>`).join('');
    bEl.innerHTML = bank.map(x => `<button class="chip" data-i="${x.i}" ${x.used ? 'disabled' : ''}>${esc(x.w)}</button>`).join('');
    chk.disabled = locked || ans.length === 0;
    aEl.querySelectorAll('.chip').forEach(c => c.addEventListener('click', () => {
      if (locked) return; const k = ans.findIndex(x => x.i === +c.dataset.i); const [x] = ans.splice(k, 1); bank.find(b => b.i === x.i).used = false; draw();
    }));
    bEl.querySelectorAll('.chip').forEach(c => c.addEventListener('click', () => {
      if (locked) return; const x = bank.find(b => b.i === +c.dataset.i); if (x.used) return; x.used = true; ans.push(x); draw();
    }));
  }
  clr.addEventListener('click', () => { if (locked) return; ans = []; bank.forEach(b => b.used = false); draw(); });
  chk.addEventListener('click', () => {
    locked = true; const text = ans.map(x => x.w).join(' ');
    const ok = [q.answer].concat(q.alts || []).some(x => norm(text) === norm(x));
    aEl.style.borderColor = ok ? 'var(--ok)' : 'var(--bad)'; draw(); clr.disabled = true; finish(ok, text);
  });
  draw();
}

// urutkan kalimat menjadi paragraf atau dialog yang runtut
function qSeq(q, box, finish) {
  let order = q.items.map((t, i) => ({ t, i }));
  let bank = shuffle(order);
  for (let n = 0; n < 8 && bank.length > 1 && bank.every((x, k) => x.i === k); n++) bank = shuffle(order);
  bank = bank.map(x => ({ ...x, used: false }));
  let ans = [], locked = false;
  box.innerHTML = `<div class="qtext">${fmt(q.q)}</div><ol class="seqans" id="sans" aria-label="Urutanmu"></ol><div class="seqbank" id="sbank"></div>
    <div class="row"><button class="btn" id="chk" disabled>Cek urutan</button><button class="btn ghost" id="clr">Hapus semua</button></div>`;
  const aEl = $('#sans', box), bEl = $('#sbank', box), chk = $('#chk', box), clr = $('#clr', box);
  function draw() {
    aEl.innerHTML = ans.map(x => `<li><button class="sq" data-i="${x.i}">${esc(x.t)}</button></li>`).join('');
    bEl.innerHTML = bank.map(x => `<button class="sq" data-i="${x.i}" ${x.used ? 'disabled' : ''}>${esc(x.t)}</button>`).join('');
    chk.disabled = locked || ans.length !== bank.length;
    aEl.querySelectorAll('.sq').forEach(c => c.addEventListener('click', () => {
      if (locked) return; const k = ans.findIndex(x => x.i === +c.dataset.i); const [x] = ans.splice(k, 1); bank.find(b => b.i === x.i).used = false; draw();
    }));
    bEl.querySelectorAll('.sq').forEach(c => c.addEventListener('click', () => {
      if (locked) return; const x = bank.find(b => b.i === +c.dataset.i); if (x.used) return; x.used = true; ans.push(x); draw();
    }));
  }
  clr.addEventListener('click', () => { if (locked) return; ans = []; bank.forEach(b => b.used = false); draw(); });
  chk.addEventListener('click', () => {
    locked = true; const ok = ans.every((x, k) => x.i === k);
    aEl.classList.add(ok ? 'okbox' : 'badbox'); draw(); clr.disabled = true; finish(ok, ans.map(x => x.t).join(' '));
  });
  draw();
}

// temukan kalimat yang salah
function qSpot(q, box, finish) {
  box.innerHTML = `<div class="qtext">${fmt(q.q)}</div><div class="spot">${q.items.map((t, i) => `<button class="sp" data-i="${i}">${esc(t)}</button>`).join('')}</div>`;
  box.querySelectorAll('.sp').forEach(b => b.addEventListener('click', () => {
    const idx = +b.dataset.i, ok = idx === q.answer;
    box.querySelectorAll('.sp').forEach(x => { x.disabled = true; if (+x.dataset.i === q.answer) x.classList.add('ok'); });
    if (!ok) b.classList.add('bad');
    finish(ok, q.items[idx]);
  }));
}

// dengarkan lalu isi kata yang hilang
function qCloze(q, box, finish) {
  const parts = q.text.split('___');
  const inputs = parts.slice(0, -1).map((p, i) => `${esc(p)}<input class="blank cz" type="text" autocomplete="off" autocapitalize="off" spellcheck="false" aria-label="Kata ke-${i + 1}" size="${Math.max(4, Math.max(...q.answers[i].map(a => a.length)) + 1)}">`).join('') + esc(parts[parts.length - 1]);
  box.innerHTML = `<div class="qtext">${fmt(q.q)}</div>
    ${hasTTS ? `<div class="row"><button class="btn play" id="cplay" type="button">🔊 Dengarkan</button><button class="btn ghost" id="cslow" type="button">🐢 Pelan</button></div>` : `<div class="hint">Browser ini tidak mendukung suara, jadi teksnya ditampilkan: <b>${esc(q.say)}</b></div>`}
    <div class="cloze">${inputs}</div><div class="row"><button class="btn" id="chk" type="button">Cek</button></div>`;
  const ins = [...box.querySelectorAll('input.cz')], btn = $('#chk', box);
  const pl = $('#cplay', box); if (pl) pl.addEventListener('click', () => speak(q.say));
  const sl = $('#cslow', box); if (sl) sl.addEventListener('click', () => speakSlow(q.say));
  if (hasTTS) setTimeout(() => speak(q.say), 250);
  if (ins[0]) ins[0].focus();
  const check = () => {
    if (ins.every(i => !norm(i.value))) { ins[0].focus(); return; }
    let all = true;
    ins.forEach((inp, k) => { const ok = q.answers[k].some(a => expand(inp.value) === expand(a)); if (!ok) all = false; inp.classList.add(ok ? 'ok' : 'bad'); inp.disabled = true; });
    btn.disabled = true; finish(all, ins.map(i => i.value).join(', '));
  };
  btn.addEventListener('click', check);
  ins.forEach(i => i.addEventListener('keydown', e => { if (e.key === 'Enter') check(); }));
}

function qMatch(q, box, finish) {
  const left = q.pairs.map(p => p[0]), right = shuffle(q.pairs.map(p => p[1]));
  const ansOf = Object.fromEntries(q.pairs);
  box.innerHTML = `<div class="qtext">${fmt(q.q)}</div><div class="mgrid"><div class="opts" id="L">${left.map(l => `<button class="opt" data-v="${esc(l)}">${esc(l)}</button>`).join('')}</div><div class="opts" id="R">${right.map(r => `<button class="opt" data-v="${esc(r)}">${esc(r)}</button>`).join('')}</div></div><div class="hint">Klik satu di kiri, lalu pasangannya di kanan.</div>`;
  let sel = null, mistakes = 0, matched = 0;
  const L = $('#L', box), R = $('#R', box);
  L.querySelectorAll('.opt').forEach(b => b.addEventListener('click', () => {
    if (b.classList.contains('ok')) return;
    L.querySelectorAll('.opt').forEach(x => x.classList.remove('sel')); b.classList.add('sel'); sel = b;
    if (/^[A-Za-z]/.test(b.dataset.v) && b.dataset.v.length < 40) speak(b.dataset.v);
  }));
  R.querySelectorAll('.opt').forEach(b => b.addEventListener('click', () => {
    if (!sel || b.classList.contains('ok')) return;
    if (ansOf[sel.dataset.v] === b.dataset.v) {
      sel.classList.remove('sel'); sel.classList.add('ok'); b.classList.add('ok'); sel.disabled = true; b.disabled = true; sel = null; matched++;
      if (matched === left.length) finish(mistakes === 0, mistakes ? `${mistakes} kesalahan` : 'semua benar');
    } else {
      mistakes++; b.classList.add('shake'); setTimeout(() => b.classList.remove('shake'), 400);
    }
  }));
}

// ---------- target harian dan rangkaian hari ----------
const dayStr = d => d.toLocaleDateString('sv-SE');
const todayStr = () => dayStr(new Date());
const yesterdayStr = () => { const d = new Date(); d.setDate(d.getDate() - 1); return dayStr(d); };
const goalN = () => [10, 20, 30, 50].includes(prog.goal) ? prog.goal : 10;
function dailyCount() { return prog.daily && prog.daily.date === todayStr() ? prog.daily.count : 0; }
function streakN() { const st = prog.streak; return st && (st.last === todayStr() || st.last === yesterdayStr()) ? st.n : 0; }
function bumpDaily() {
  const t = todayStr();
  if (!prog.daily || prog.daily.date !== t) prog.daily = { date: t, count: 0 };
  prog.daily.count++;
  const hist = prog.hist = prog.hist || {};
  hist[t] = (hist[t] || 0) + 1;
  const keys = Object.keys(hist).sort();
  while (keys.length > 120) delete hist[keys.shift()];
  const st = prog.streak = prog.streak || { last: '', n: 0 };
  if (st.last !== t) { st.n = st.last === yesterdayStr() ? st.n + 1 : 1; st.last = t; }
  saveProg();
}
function dailyCard() {
  const c = dailyCount(), g = goalN(), pct = Math.min(100, Math.round(100 * c / g)), n = streakN();
  return `<div class="card daily"><div class="dtop"><b>🎯 Target hari ini: ${c}/${g} soal</b><span class="streak" title="Hari belajar berturut-turut">🔥 ${n} hari</span></div>
    <div class="bar" role="progressbar" aria-valuemin="0" aria-valuemax="${g}" aria-valuenow="${Math.min(c, g)}"><i style="width:${pct}%"></i></div>
    <div class="dbot"><small class="hint">${c >= g ? 'Target tercapai, hebat! 🎉' : 'Jawab soal di mana saja untuk menambah.'}</small>
    <label class="gl">Target <select id="goalsel" aria-label="Target soal per hari">${[10, 20, 30, 50].map(v => `<option value="${v}"${v === g ? ' selected' : ''}>${v}</option>`).join('')}</select></label></div></div>`;
}

// ---------- alat belajar di beranda ----------
function srsDueCount() { const now = Date.now(); return Object.values(prog.srs || {}).filter(c => c.due <= now).length; }
function toolsRow() {
  const due = srsDueCount();
  return `<div class="tools">
    <a class="btn ghost" href="#/kartu">🧠 Kartu hafalan${due ? ` <span class="pill">${due}</span>` : ''}</a>
    <a class="btn ghost" href="#/tes">🎯 Tes penempatan</a>
    <a class="btn ghost" href="#/bicara">🎤 Latihan berbicara</a>
    <a class="btn ghost" href="#/statistik">📊 Statistik dan cadangan</a>
    <button class="btn ghost" id="offbtn" type="button">📴 Simpan untuk offline</button></div><div id="offmsg" class="hint"></div>`;
}
function bindHome(index) {
  const gs = $('#goalsel');
  if (gs) gs.addEventListener('change', () => { prog.goal = +gs.value; saveProg(); renderHome(index); });
  const ob = $('#offbtn');
  if (ob) ob.addEventListener('click', () => saveOffline(index, ob));
}
async function saveOffline(index, btn) {
  const msg = $('#offmsg');
  if (!('serviceWorker' in navigator) || !navigator.serviceWorker.controller) {
    msg.textContent = 'Fitur ini aktif setelah halaman dimuat ulang sekali (dan harus lewat https). Muat ulang, lalu coba lagi.';
    return;
  }
  btn.disabled = true;
  const files = ['data/index.json', 'data/kamus.json', 'data/kata.json', 'data/bicara.json', 'data/placement.json', ...index.filter(u => u.ready).map(u => `data/${u.id}.json`)];
  let n = 0, fail = 0;
  for (let i = 0; i < files.length; i += 6) {
    await Promise.all(files.slice(i, i + 6).map(f => fetch(f).then(r => { if (!r.ok) throw 0; return r.blob(); }).then(() => n++).catch(() => fail++)));
    msg.textContent = `Menyimpan… ${n}/${files.length}`;
  }
  msg.textContent = fail ? `Tersimpan ${n} dari ${files.length} berkas. Coba lagi bila internet stabil.` : `Selesai! ${n} berkas tersimpan. Aplikasi bisa dibuka tanpa internet.`;
  btn.disabled = false;
}
if ('serviceWorker' in navigator && location.protocol.startsWith('http')) navigator.serviceWorker.register('sw.js').catch(() => { /* diabaikan */ });

// ---------- kartu hafalan (pengulangan berjarak) ----------
const SRS_DAYS = [0, 1, 3, 7, 16, 35, 90];
async function renderKartu() {
  const words = await getJSON('data/kamus.json');
  prog.srs = prog.srs || {};
  const now = Date.now(), day = 86400000;
  const known = new Set(Object.entries(prog.units).filter(([, u]) => u.learned || u.practice || u.quiz).map(([id]) => id));
  const pool = words.filter(w => known.size ? known.has(w.u) : w.kelas === 7 || w.kelas === '7');
  const byKey = new Map(words.map(w => [w.en, w]));
  const dueW = Object.entries(prog.srs).filter(([en, c]) => c.due <= now && byKey.has(en)).sort((a, b) => a[1].due - b[1].due).slice(0, 25).map(([en]) => byKey.get(en));
  const fresh = pool.filter(w => !prog.srs[w.en]).slice(0, 8);
  const queue = [...dueW, ...fresh];
  app.innerHTML = `<a class="crumb" href="#/">← Beranda</a><h1>🧠 Kartu hafalan</h1>
    <p class="lead">Kata yang kamu lupakan muncul lebih sering; kata yang kamu ingat muncul makin jarang. Kata baru diambil dari unit yang sudah kamu buka.</p><div id="kpane"></div>`;
  const pane = $('#kpane');
  if (!queue.length) {
    pane.innerHTML = `<div class="card result"><div class="big">🌟</div><h2>Tidak ada kartu untuk hari ini</h2><p>${Object.keys(prog.srs).length ? 'Semua kartu sudah diulang. Kembali lagi besok!' : 'Buka dan pelajari satu unit dulu, lalu kembali ke sini.'}</p><a class="btn" href="#/">🏠 Beranda</a></div>`;
    return;
  }
  let i = 0, done = 0; const total = queue.length; const redo = new Map();
  function card() {
    if (i >= queue.length) return fin();
    const w = queue[i];
    pane.innerHTML = `<div class="qhead"><span class="qno">Kartu ${Math.min(done + 1, total)}/${total}</span><div class="pbar"><i style="width:${Math.round(100 * done / total)}%"></i></div></div>
      <div class="card flash"><div class="fen">${esc(w.en)}</div><button class="btn ghost small" id="fsay" type="button">🔊 Dengar</button>
      <div id="fback" hidden><div class="fid">${esc(w.id)}</div>${w.ex ? `<div class="fex">${esc(w.ex)}</div>` : ''}</div>
      <div class="nextrow"><button class="btn" id="fshow" type="button">Lihat arti</button></div>
      <div class="rate" id="frate" hidden><button class="btn bad" data-r="0" type="button">😵 Lupa</button><button class="btn ghost" data-r="1" type="button">🤔 Sulit</button><button class="btn" data-r="2" type="button">😄 Ingat</button></div></div>`;
    speak(w.en);
    $('#fsay').addEventListener('click', () => speak(w.en));
    $('#fshow').addEventListener('click', () => { $('#fback').hidden = false; $('#frate').hidden = false; $('#fshow').parentNode.hidden = true; });
    pane.querySelectorAll('[data-r]').forEach(b => b.addEventListener('click', () => rate(w, +b.dataset.r)));
  }
  function rate(w, r) {
    const c = prog.srs[w.en] || { box: 0, due: 0 };
    if (r === 0) { c.box = 0; c.due = Date.now() + 10 * 60000; const t = (redo.get(w.en) || 0) + 1; redo.set(w.en, t); if (t <= 2) queue.push(w); else done++; }
    else if (r === 1) { c.box = Math.max(1, c.box); c.due = Date.now() + day; done++; }
    else { c.box = Math.min(c.box + 1, SRS_DAYS.length - 1); c.due = Date.now() + Math.max(1, SRS_DAYS[c.box]) * day; done++; }
    prog.srs[w.en] = c;
    bumpDaily(); i++; card();
  }
  function fin() {
    pane.innerHTML = `<div class="card result"><div class="big">🎉</div><h2>Sesi selesai!</h2><p>${total} kartu sudah diulang. Kata yang sulit akan muncul lagi lebih cepat.</p>
      <div class="row" style="justify-content:center"><a class="btn" href="#/kartu">➕ Sesi lagi</a><a class="btn ghost" href="#/">🏠 Beranda</a></div></div>`;
  }
  card();
}

// ---------- tes penempatan ----------
const BAND_INFO = [
  ['', ''],
  ['Kelas 7', 'kelas/7'], ['Kelas 8', 'kelas/8'], ['Kelas 9', 'kelas/9'], ['Kelas 10', 'kelas/10'], ['Kelas 11', 'kelas/11'], ['Kelas 12', 'kelas/12'],
];
async function renderTes() {
  const qs = await getJSON('data/placement.json');
  app.innerHTML = `<a class="crumb" href="#/">← Beranda</a><h1>🎯 Tes penempatan</h1>
    <p class="lead">24 soal pilihan ganda dari mudah ke sulit. Tidak memengaruhi bintang. Hasilnya menyarankan level untuk mulai belajar.</p><div id="tpane"></div>`;
  const pane = $('#tpane');
  let i = 0; const got = {};
  function show() {
    if (i >= qs.length) return result();
    const q = qs[i];
    pane.innerHTML = `<div class="qhead"><span class="qno">Soal ${i + 1}/${qs.length}</span><div class="pbar"><i style="width:${Math.round(100 * i / qs.length)}%"></i></div></div><div class="card"><div id="qbox"></div><div id="fb"></div></div>`;
    qMcq({ ...q, type: 'mcq' }, $('#qbox'), ok => {
      got[q.band] = (got[q.band] || 0) + (ok ? 1 : 0);
      bumpDaily();
      $('#fb').innerHTML = `<div class="fb ${ok ? 'ok' : 'bad'}"><b class="h">${ok ? '✅ Benar' : '❌ Belum tepat'}</b>${ok ? '' : `<div>Jawaban benar: <b>${esc(q.options[0])}</b></div>`}<div>${fmt(q.exp)}</div></div>
        <div class="nextrow"><button class="btn" id="next">${i === qs.length - 1 ? 'Lihat hasil' : 'Lanjut →'}</button></div>`;
      const nb = $('#next'); nb.focus(); nb.addEventListener('click', () => { i++; show(); });
    });
  }
  function result() {
    let level = 7;
    for (let b = 1; b <= 6; b++) { if ((got[b] || 0) >= 3) level = b + 1; else break; }
    const total = Object.values(got).reduce((a, v) => a + v, 0);
    const adv = level >= 7;
    const rec = adv ? `Kamu sudah kuat! Coba <a href="#/kelas/ielts">Persiapan IELTS</a>, <a href="#/kelas/toeic">Persiapan TOEIC</a>, atau level <a href="#/kelas/kerja">Pekerja</a>.`
      : `Mulai dari <a href="#/${BAND_INFO[level][1]}"><b>${BAND_INFO[level][0]}</b></a>. ${level > 1 ? `Tingkat sebelumnya sudah kamu kuasai.` : 'Mulai dari dasar supaya fondasinya kuat.'}`;
    pane.innerHTML = `<div class="card result"><div class="big">🎯</div><h2>Skor ${total} dari ${qs.length}</h2><p>${rec}</p>
      <p class="hint">Jika banyak salah di tenses, buka <a href="#/kelas/tenses">Modul Tenses</a>. Jika sulit memahami ucapan, coba <a href="#/kelas/pron">Modul Pelafalan</a>.</p>
      <div class="row" style="justify-content:center"><a class="btn" href="#/tes">🔁 Ulangi tes</a><a class="btn ghost" href="#/">🏠 Beranda</a></div></div>`;
  }
  show();
}

// ---------- latihan berbicara (pengenalan suara) ----------
const SR = window.SpeechRecognition || window.webkitSpeechRecognition;
async function renderBicara() {
  const all = await getJSON('data/bicara.json');
  app.innerHTML = `<a class="crumb" href="#/">← Beranda</a><h1>🎤 Latihan berbicara</h1>
    <p class="lead">Dengarkan kalimat, lalu ucapkan. Aplikasi mencocokkan kata-kata yang terdengar. Butuh Chrome (HP atau laptop), izin mikrofon, dan internet.</p>${SR ? '' : '<div class="card"><b>Browser ini belum mendukung pengenalan suara.</b> Coba buka di Chrome. Sementara itu kamu tetap bisa mendengar contoh kalimat di bawah.</div>'}<div id="bpane"></div>`;
  const pane = $('#bpane');
  const qs = shuffle(all).slice(0, 10);
  let i = 0, okN = 0;
  const words = t => norm(t).split(' ').filter(Boolean);
  function grade(target, heard) {
    const tw = words(expand(target)), hw = words(expand(heard)), pool = hw.slice();
    const hit = tw.map(w => { const k = pool.indexOf(w); if (k >= 0) { pool.splice(k, 1); return true; } return false; });
    return { hit, tw, pct: Math.round(100 * hit.filter(Boolean).length / tw.length) };
  }
  function show() {
    if (i >= qs.length) {
      pane.innerHTML = `<div class="card result"><div class="big">🎤</div><h2>${okN} dari ${qs.length} kalimat tepat</h2><div class="row" style="justify-content:center"><a class="btn" href="#/bicara">🔁 Sesi baru</a><a class="btn ghost" href="#/">🏠 Beranda</a></div></div>`;
      return;
    }
    const q = qs[i];
    pane.innerHTML = `<div class="qhead"><span class="qno">Kalimat ${i + 1}/${qs.length}</span><div class="pbar"><i style="width:${Math.round(100 * i / qs.length)}%"></i></div></div>
      <div class="card"><div class="qtext">${esc(q.s)}</div><div class="hint">${esc(q.id)}</div>
      <div class="row"><button class="btn ghost" id="bsay" type="button">🔊 Dengar</button><button class="btn ghost small" id="bslow" type="button">🐢 Pelan</button>${SR ? '<button class="btn" id="bmic" type="button">🎤 Ucapkan</button>' : ''}</div>
      <div id="bres"></div><div class="nextrow"><button class="btn ghost" id="bnext" type="button">${i === qs.length - 1 ? 'Selesai' : 'Lewati / Lanjut →'}</button></div></div>`;
    $('#bsay').addEventListener('click', () => speak(q.s));
    $('#bslow').addEventListener('click', () => speakSlow(q.s));
    $('#bnext').addEventListener('click', () => { i++; show(); });
    speak(q.s);
    const mic = $('#bmic');
    if (mic) mic.addEventListener('click', () => listen(q, mic));
  }
  function listen(q, mic) {
    const rec = new SR(); rec.lang = 'en-US'; rec.interimResults = false; rec.maxAlternatives = 3;
    const res = $('#bres'); mic.disabled = true; res.innerHTML = '<p class="hint">🎙️ Mendengarkan… ucapkan kalimatnya.</p>';
    rec.onresult = ev => {
      const alts = [...ev.results[0]].map(a => a.transcript);
      const best = alts.map(a => ({ a, g: grade(q.s, a) })).sort((x, y) => y.g.pct - x.g.pct)[0];
      const ok = best.g.pct >= 80;
      if (ok) okN++;
      bumpDaily();
      res.innerHTML = `<div class="fb ${ok ? 'ok' : 'bad'}"><b class="h">${ok ? '✅ Bagus!' : '🔁 Coba lagi'} ${best.g.pct}%</b>
        <div>Terdengar: <i>${esc(best.a)}</i></div>
        <div>Kalimat: ${best.g.tw.map((w, k) => `<span class="${best.g.hit[k] ? 'hit' : 'miss'}">${esc(w)}</span>`).join(' ')}</div></div>`;
      mic.disabled = false;
    };
    rec.onerror = ev => { res.innerHTML = `<p class="hint">${ev.error === 'not-allowed' ? 'Izin mikrofon ditolak. Aktifkan izin mikrofon di browser.' : ev.error === 'no-speech' ? 'Suaramu tidak terdengar. Coba lagi lebih dekat ke mikrofon.' : ev.error === 'network' ? 'Pengenalan suara butuh internet.' : 'Gagal mendengarkan. Coba lagi.'}</p>`; mic.disabled = false; };
    rec.onend = () => { mic.disabled = false; };
    try { rec.start(); } catch (e) { mic.disabled = false; }
  }
  show();
}


// ---------- statistik, cadangan, dan mode ujian ----------
function exportProg() {
  const blob = new Blob([JSON.stringify({ app: 'belajar-inggris', v: 1, at: new Date().toISOString(), prog })], { type: 'application/json' });
  const a = document.createElement('a');
  a.href = URL.createObjectURL(blob); a.download = 'kemajuan-belajar-inggris.json';
  document.body.appendChild(a); a.click(); a.remove();
  setTimeout(() => URL.revokeObjectURL(a.href), 1000);
}
function mergeProg(inc) {
  let n = 0;
  for (const [id, u] of Object.entries(inc.units || {})) {
    const m = U(id);
    for (const k of ['practice', 'quiz', 'stars']) if ((u[k] || 0) > (m[k] || 0)) { m[k] = u[k]; n++; }
    if (u.learned && !m.learned) { m.learned = true; n++; }
    if (u.reads) m.reads = { ...u.reads, ...(m.reads || {}) };
  }
  for (const [k, v] of Object.entries(inc.wrong || {})) if (!(k in prog.wrong)) prog.wrong[k] = v;
  prog.srs = prog.srs || {};
  for (const [en, c] of Object.entries(inc.srs || {})) if (!prog.srs[en] || (c.box || 0) > (prog.srs[en].box || 0)) { prog.srs[en] = c; n++; }
  prog.hist = prog.hist || {};
  for (const [d, c] of Object.entries(inc.hist || {})) prog.hist[d] = Math.max(prog.hist[d] || 0, c);
  prog.exam = prog.exam || {};
  for (const [k, e] of Object.entries(inc.exam || {})) if (!prog.exam[k] || e.best > prog.exam[k].best) prog.exam[k] = e;
  if (inc.streak && (!prog.streak || String(inc.streak.last) > String(prog.streak.last))) prog.streak = inc.streak;
  saveProg();
  return n;
}
function renderStat(index) {
  const hist = prog.hist || {};
  const days = [];
  for (let i = 13; i >= 0; i--) { const d = new Date(); d.setDate(d.getDate() - i); const k = dayStr(d); days.push([k, hist[k] || 0]); }
  const max = Math.max(10, ...days.map(x => x[1]));
  const total = Object.values(hist).reduce((a, v) => a + v, 0);
  const lv = LEVELS.map(l => ({ l, st: levelStat(index, l.key) })).filter(x => x.st.ready);
  const wr = {};
  for (const id of Object.values(prog.wrong)) if (id !== 'ulang') wr[id] = (wr[id] || 0) + 1;
  const byId = Object.fromEntries(index.map(u => [u.id, u]));
  const wrongTop = Object.entries(wr).sort((a, b) => b[1] - a[1]).slice(0, 5).filter(([id]) => byId[id]);
  const weak = Object.entries(prog.units).filter(([id, u]) => byId[id] && u.quiz > 0 && u.quiz < 70).sort((a, b) => a[1].quiz - b[1].quiz).slice(0, 5);
  const srs = Object.values(prog.srs || {}), now = Date.now();
  const exams = Object.entries(prog.exam || {});
  app.innerHTML = `<a class="crumb" href="#/">← Beranda</a><h1>📊 Statistik</h1>
    <div class="grid stats"><div class="card sbox"><b>${total}</b><span>soal dijawab</span></div><div class="card sbox"><b>${Object.keys(hist).length}</b><span>hari belajar</span></div>
      <div class="card sbox"><b>${streakN()}</b><span>hari berturut-turut</span></div><div class="card sbox"><b>${totalStars()}</b><span>bintang</span></div></div>
    <h2 class="sec">14 hari terakhir</h2>
    <div class="card"><div class="chart" role="img" aria-label="Jumlah soal per hari selama 14 hari">${days.map(([k, c]) => `<div class="cb" title="${k}: ${c} soal"><i style="height:${Math.round(100 * c / max)}%"></i><small>${k.slice(8)}</small></div>`).join('')}</div></div>
    <h2 class="sec">Kemajuan per level</h2>
    <div class="card">${lv.map(({ l, st }) => `<div class="lrow"><a href="#/kelas/${l.key}">${l.emoji} ${esc(l.title)}</a><div class="bar"><i style="width:${Math.round(100 * st.stars / st.max)}%"></i></div><small>${st.done}/${st.ready} unit</small></div>`).join('')}</div>
    <h2 class="sec">Perlu diulang</h2>
    <div class="card">${wrongTop.length ? `<p class="hint">Unit dengan soal salah terbanyak:</p><ul class="slist">${wrongTop.map(([id, n]) => `<li><a href="#/unit/${id}/practice">Unit ${byId[id].no} ${esc(byId[id].title)}</a> <small>(${n} soal)</small></li>`).join('')}</ul>` : '<p class="hint">Belum ada soal yang salah. Bagus!</p>'}
      ${weak.length ? `<p class="hint">Kuis dengan nilai rendah:</p><ul class="slist">${weak.map(([id, u]) => `<li><a href="#/unit/${id}/learn">Unit ${byId[id].no} ${esc(byId[id].title)}</a> <small>(${u.quiz}%)</small></li>`).join('')}</ul>` : ''}</div>
    <h2 class="sec">Kartu hafalan</h2>
    <div class="card"><p>${srs.length} kartu dipelajari · ${srs.filter(c => c.due <= now).length} siap diulang · ${srs.filter(c => (c.box || 0) >= 3).length} sudah kuat.</p><a class="btn ghost small" href="#/kartu">🧠 Buka kartu hafalan</a></div>
    ${exams.length ? `<h2 class="sec">Hasil mode ujian</h2><div class="card"><ul class="slist">${exams.map(([k, e]) => `<li>${esc(kelasName(isNaN(+k) ? k : +k))}: terbaik <b>${e.best}%</b> · terakhir ${e.last}%</li>`).join('')}</ul></div>` : ''}
    <h2 class="sec">Cadangkan atau pindahkan kemajuan</h2>
    <div class="card"><p class="hint">Kemajuan hanya tersimpan di browser ini. Unduh cadangan untuk dipindahkan ke HP atau laptop lain, lalu pulihkan di sana. Memulihkan akan <b>menggabungkan</b> (nilai tertinggi dipertahankan), tidak menghapus apa pun.</p>
      <div class="row"><button class="btn" id="exp" type="button">⬇️ Unduh cadangan</button><label class="btn ghost" for="imp">⬆️ Pulihkan dari berkas</label><input id="imp" type="file" accept="application/json,.json" hidden></div><div id="impmsg" class="hint"></div></div>`;
  $('#exp').addEventListener('click', exportProg);
  $('#imp').addEventListener('change', ev => {
    const f = ev.target.files && ev.target.files[0]; if (!f) return;
    const r = new FileReader();
    r.onload = () => {
      try {
        const d = JSON.parse(r.result);
        if (!d || d.app !== 'belajar-inggris' || !d.prog || typeof d.prog.units !== 'object') throw new Error('format');
        const n = mergeProg(d.prog);
        $('#impmsg').textContent = `Berhasil digabungkan (${n} perubahan).`;
        setTimeout(() => renderStat(index), 900);
      } catch (e) { $('#impmsg').textContent = 'Berkas tidak dikenali. Pakai berkas cadangan dari aplikasi ini.'; }
    };
    r.readAsText(f);
  });
}

async function renderUjian(index, key) {
  const lv = LEVELS.find(l => l.key === key);
  const units = index.filter(u => String(u.kelas) === key && u.ready);
  if (!lv || !units.length) return renderHome(index);
  const N = ['ielts', 'toeic', 'toefl'].includes(key) ? 40 : 30, MIN = N;
  app.innerHTML = `<a class="crumb" href="#/kelas/${key}">← ${esc(lv.title)}</a><h1>📝 Mode ujian: ${esc(lv.title)}</h1>
    <div class="card"><p>${N} soal acak dari seluruh unit level ini, waktu <b>${MIN} menit</b>. Tidak ada penjelasan sampai ujian selesai, dan setiap soal dijawab satu kali.</p>
      <ul class="slist"><li>Soal dengar hanya diputar bila perangkatmu mendukung suara.</li><li>Soal yang salah masuk ke daftar <b>Ulangi yang salah</b>.</li>${(prog.exam || {})[key] ? `<li>Nilai terbaikmu: <b>${prog.exam[key].best}%</b></li>` : ''}</ul>
      <div class="row"><button class="btn" id="go" type="button">▶️ Mulai ujian</button></div></div><div id="epane"></div>`;
  $('#go').addEventListener('click', async () => {
    const pane = $('#epane'); $('#go').disabled = true;
    pane.innerHTML = '<p class="loading">Menyiapkan soal…</p>';
    const data = await Promise.all(units.map(u => getJSON(`data/${u.id}.json`)));
    const okType = q => !['dictate', 'reply'].includes(q.type) && (hasTTS || !['listen', 'cloze'].includes(q.type));
    let pool = [];
    data.forEach(d => { const seen = new Set(); shuffle(d.practice.concat(d.quiz).filter(okType)).forEach(q => { if (q.k && seen.has(q.k)) return; if (q.k) seen.add(q.k); pool.push({ ...q, unit: d.id }); }); });
    const per = Math.max(2, Math.ceil(N / units.length) + 1), cnt = {};
    const qs = shuffle(pool).filter(q => (cnt[q.unit] = (cnt[q.unit] || 0) + 1) <= per).slice(0, N);
    if (qs.length < 5) { pane.innerHTML = '<p class="hint">Soal belum cukup.</p>'; return; }
    runExam(pane, key, lv, qs, MIN, index);
  });
}

function runExam(pane, key, lv, qs, minutes, index) {
  let i = 0, score = 0, left = minutes * 60, over = false;
  const res = [], t0 = Date.now();
  const mmss = s => `${Math.floor(s / 60)}:${String(s % 60).padStart(2, '0')}`;
  const timer = setInterval(() => {
    if (!document.body.contains(pane) || location.hash.indexOf('#/ujian/') !== 0) { clearInterval(timer); return; }
    left--; const el = $('#etime'); if (el) el.textContent = mmss(Math.max(0, left));
    if (left <= 0) { clearInterval(timer); over = true; finish(); }
  }, 1000);
  function show() {
    if (over) return;
    if (i >= qs.length) { clearInterval(timer); return finish(); }
    closeWordPop();
    const q = qs[i];
    pane.innerHTML = `<div class="qhead"><span class="qno">📝 ${i + 1}/${qs.length}</span><div class="pbar"><i style="width:${Math.round(100 * i / qs.length)}%"></i></div><span class="etime" id="etime" aria-label="Sisa waktu">${mmss(left)}</span></div>
      <div class="card exam"><div id="qbox"></div></div>`;
    renderQ(q, $('#qbox'), (ok, shown) => {
      if (over) return;
      res.push({ q, ok, shown }); if (ok) score++; bumpDaily();
      if (q.k) { if (ok) delete prog.wrong[q.k]; else prog.wrong[q.k] = q.unit; saveProg(); }
      setTimeout(() => { i++; show(); }, 450);
    });
  }
  function finish() {
    over = true;
    const total = qs.length, pct = Math.round(100 * score / total);
    const used = Math.min(minutes * 60, Math.round((Date.now() - t0) / 1000));
    const ex = prog.exam = prog.exam || {}; const prev = ex[key] ? ex[key].best : 0;
    ex[key] = { best: Math.max(prev, pct), last: pct, date: todayStr() }; saveProg();
    const byU = {}; res.forEach(r => { const b = byU[r.q.unit] = byU[r.q.unit] || [0, 0]; b[1]++; if (r.ok) b[0]++; });
    const ids = Object.fromEntries(index.map(u => [u.id, u]));
    const unanswered = total - res.length;
    pane.innerHTML = `<div class="card result"><div class="big">${pct >= 70 ? '🎉' : '💪'}</div><h2>${score} dari ${total} benar (${pct}%)</h2>
      <p>Waktu: ${mmss(used)} dari ${mmss(minutes * 60)}${unanswered ? ` · ${unanswered} soal belum sempat dijawab` : ''}${pct > prev ? ' · nilai terbaik baru! ⭐' : ''}</p>
      <div class="row" style="justify-content:center"><a class="btn" href="#/ujian/${key}">🔁 Ujian lagi</a><a class="btn ghost" href="#/kelas/${key}">← ${esc(lv.title)}</a></div></div>
      <div class="card"><h3>Hasil per unit</h3><ul class="slist">${Object.entries(byU).map(([id, [a, b]]) => `<li><a href="#/unit/${id}/learn">Unit ${ids[id] ? ids[id].no : ''} ${ids[id] ? esc(ids[id].title) : id}</a> <small>${a}/${b}</small></li>`).join('')}</ul></div>
      ${res.some(r => !r.ok) ? `<div class="card review"><h3>Pembahasan soal yang salah:</h3><ol class="review">${res.filter(r => !r.ok).map(r => `<li>${fmt(r.q.q || r.q.say || '')}<br>Jawaban benar: <b>${esc(correctText(r.q))}</b><br><small>${fmt(r.q.exp)}</small></li>`).join('')}</ol></div>` : ''}`;
  }
  show();
}

})();

// ---------- tombol kembali ke atas ----------
(() => {
  const b = document.getElementById('totop');
  if (!b) return;
  let anim = 0;
  const upd = () => b.classList.toggle('show', window.scrollY > 400);
  window.addEventListener('scroll', upd, { passive: true });
  const stop = () => { cancelAnimationFrame(anim); anim = 0; b.classList.remove('going'); };
  ['wheel', 'touchstart', 'keydown'].forEach(ev => window.addEventListener(ev, () => anim && stop(), { passive: true }));
  b.addEventListener('click', () => {
    stop();
    const from = window.scrollY;
    if (from <= 0) return;
    const dur = Math.min(900, 350 + from / 6);               // makin jauh makin lama, maksimal 0,9 detik
    const t0 = performance.now();
    const ease = t => 1 - Math.pow(1 - t, 3);                // melambat di akhir
    b.classList.add('going');
    const step = now => {
      const t = Math.min(1, (now - t0) / dur);
      window.scrollTo(0, from * (1 - ease(t)));
      if (t < 1) anim = requestAnimationFrame(step); else stop();
    };
    anim = requestAnimationFrame(step);
  });
  upd();
})();

