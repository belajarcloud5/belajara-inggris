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
const GENDER = { dina: 'f', rani: 'f', mother: 'f', budi: 'm', tom: 'm', 'mr. adi': 'm', 'ms. sari': 'f' };
const genderOf = name => GENDER[String(name).toLowerCase()] || '';
function maleVoice() {
  const vs = enVoices().filter(v => MALE.test(v.name) && !FEMALE.test(v.name));
  return vs.sort((a, b) => scoreVoice(a) - scoreVoice(b) || (/^en[-_]US/i.test(b.lang) - /^en[-_]US/i.test(a.lang)))[0] || null;
}
function speak(text, gender) {
  if (!hasTTS) return;
  speechSynthesis.cancel();
  const u = new SpeechSynthesisUtterance(text);
  u.lang = 'en-US'; u.rate = vset.rate; u.pitch = vset.pitch;
  let v = currentVoice();
  if (gender === 'm') {
    const m = maleVoice();
    if (m) { v = m; u.pitch = 1; } else u.pitch = 0.7;          // tidak ada suara laki-laki: turunkan nada
  } else if (gender === 'f' && v && MALE.test(v.name) && !FEMALE.test(v.name)) u.pitch = Math.max(vset.pitch, 1.5);
  if (v) { u.voice = v; u.lang = v.lang; }
  speechSynthesis.speak(u);
}
function initVoicePanel() {
  const btn = $('#vbtn'), panel = $('#vpanel');
  if (!btn || !panel) return;
  function render() {
    if (!hasTTS) {
      panel.innerHTML = `<h3>🔊 Pengaturan suara</h3><p><b>Browser ini tidak mendukung suara bawaan.</b> Tombol 🔊 tidak akan berbunyi di sini.</p>
        <p class="hint">Coba buka situs ini di browser lain di perangkat ini (Chrome, Puffin TV Browser, atau Microsoft Edge). Atau pakai HP/laptop untuk bagian yang butuh suara.</p>`;
      return;
    }
    const vs = enVoices(), cur = currentVoice();
    const sel = vs.length
      ? `<label>Pilih suara<select id="vsel">${vs.map(v => `<option value="${esc(v.name)}" ${cur && cur.name === v.name ? 'selected' : ''}>${esc(v.name)} (${esc(v.lang)})</option>`).join('')}</select></label>`
      : '<p class="hint">Belum ada suara bahasa Inggris di perangkat ini. Pasang suara bahasa Inggris di pengaturan sistem, atau coba browser lain (misalnya Microsoft Edge).</p>';
    panel.innerHTML = `<h3>🔊 Pengaturan suara</h3><p class="hint" id="vstat">Suara bahasa Inggris terdeteksi: <b>${vs.length}</b></p>${sel}
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
  btn.addEventListener('click', () => { panel.hidden = !panel.hidden; if (!panel.hidden) render(); });
  if (hasTTS) speechSynthesis.onvoiceschanged = () => { if (!panel.hidden) render(); };
}
document.addEventListener('click', e => {
  const el = e.target.closest('[data-say]');
  if (el) speak(el.dataset.say, el.dataset.g);
});
document.addEventListener('keydown', e => {
  if ((e.key === 'Enter' || e.key === ' ') && e.target.matches('.en[data-say]')) { e.preventDefault(); speak(e.target.dataset.say, e.target.dataset.g); }
});

initVoicePanel();

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
  const [, page, id, tab] = location.hash.slice(1).split('/');
  window.scrollTo(0, 0);
  try {
    const index = await getJSON('data/index.json');
    $('#total').textContent = `⭐ ${totalStars()} / ${index.filter(u => u.ready).length * 3}`;
    if (page === 'kelas') return renderKelas(index, id);
    if (page === 'kamus') return renderKamus(await getJSON('data/kamus.json'));
    if (page === 'ulang') return renderRetry(index);
    if (page === 'unit' && id) {
      const meta = index.find(u => u.id === id && u.ready);
      if (meta) return renderUnit(await getJSON(`data/${id}.json`), tab || 'learn', index);
    }
    renderHome(index);
  } catch (e) {
    app.innerHTML = `<div class="card"><b>Oops!</b> Halaman tidak bisa dimuat. Coba muat ulang.<br><small>${esc(e.message)}</small></div>`;
  }
}

const kelasName = k => k === 'kerja' ? 'Level Pekerja' : `Kelas ${k}`;

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
    </section>${wrongCount() ? `<div class="card retry"><b>🔁 ${wrongCount()} soal perlu diulang</b> <a class="btn small" href="#/ulang">Ulangi yang salah</a></div>` : ''}
    <h2 class="sec">Pilih level</h2>
    <div class="grid lgrid">${LEVELS.map(lv => levelCard(index, lv)).join('')}</div>`;
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
  const ids = [...new Set(Object.values(prog.wrong))];
  const pool = [];
  for (const id of ids) {
    const d = await getJSON(`data/${id}.json`);
    for (const q of d.practice.concat(d.quiz)) if (q.k && prog.wrong[q.k]) pool.push(q);
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
function renderUnit(d, tab, index) {
  const tabs = [['learn', '📖 Belajar'], ['practice', '✏️ Latihan'], ['quiz', '🏆 Kuis']];
  app.innerHTML = `
    <a class="crumb" href="#/kelas/${d.kelas}">← ${kelasName(d.kelas)}</a>
    <h1>${d.emoji} Unit ${d.no}: ${esc(d.title)}</h1>
    <p class="lead">${kelasName(d.kelas)} · ${esc(d.judul)}</p>
    <nav class="tabs">${tabs.map(([k, l]) => `<a class="${tab === k ? 'on' : ''}" href="#/unit/${d.id}/${k}">${l}</a>`).join('')}</nav>
    <div id="pane"></div>`;
  const pane = $('#pane');
  if (tab === 'practice') return runner(pane, d, 'practice');
  if (tab === 'quiz') return runner(pane, d, 'quiz');
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
  const N = retry ? 10 : isQuiz ? 20 : 50;                       // jumlah soal tiap sesi, diambil acak dari bank soal
  const pick = () => shuffle(src).slice(0, Math.min(N, src.length));
  let qs = pick();
  let i = 0, score = 0, wrong = [];

  function show() {
    if (i >= qs.length) return finish();
    const q = qs[i];
    pane.innerHTML = `
      <div class="qhead"><span class="qno">${isQuiz ? '🏆 Kuis' : '✏️ Latihan'} ${i + 1}/${qs.length}</span><div class="pbar"><i style="width:${Math.round(100 * i / qs.length)}%"></i></div></div>
      <div class="card"><div id="qbox"></div><div id="fb"></div></div>`;
    renderQ(q, $('#qbox'), (ok, shown) => {
      if (ok) score++; else wrong.push({ q, shown });
      if (q.k) { if (ok) delete prog.wrong[q.k]; else prog.wrong[q.k] = d.id; saveProg(); }
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

function correctText(q) {
  switch (q.type) {
    case 'mcq': case 'listen': return q.options[q.answer];
    case 'fill': return q.answers[0];
    case 'order': return q.answer;
    case 'match': return q.pairs.map(([a, b]) => `${a} = ${b}`).join(' · ');
  }
  return '';
}

function renderQ(q, box, done) {
  const finish = (() => { let used = false; return (ok, shown) => { if (!used) { used = true; done(ok, shown); } }; })();
  if (q.type === 'mcq' || q.type === 'listen') return qMcq(q, box, finish);
  if (q.type === 'fill') return qFill(q, box, finish);
  if (q.type === 'order') return qOrder(q, box, finish);
  if (q.type === 'match') return qMatch(q, box, finish);
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
    const ok = norm(text) === norm(q.answer);
    aEl.style.borderColor = ok ? 'var(--ok)' : 'var(--bad)'; draw(); clr.disabled = true; finish(ok, text);
  });
  draw();
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
})();
