# Let's Learn English!

Web belajar bahasa Inggris interaktif dari SMP sampai dunia kerja. Ada **61 unit** yang dibagi menjadi tujuh level: Kelas 7, 8, 9, 10, 11, 12, dan **Pekerja / Formal**. Beranda berupa kartu level; klik satu kartu untuk melihat unit-unitnya. Setiap unit berisi **Belajar**, **Latihan** (16 soal acak), dan **Kuis** (10 soal acak, bintang 1-3).

Situs: https://belajarcloud5.github.io/belajara-inggris/

## Menjalankan
```bash
docker compose up -d        # buka http://localhost:8085
```
Kemajuan dan bintang tersimpan di browser (localStorage). Suara memakai suara bawaan browser.

## Mengubah atau menambah isi
Isi ada di `content/uNN.py` (daftar unit dan level di `content/units.py`, pembuat soal di `content/helpers.py`).
Setelah mengubah, jalankan:
```bash
python3 build.py            # validasi soal dan menulis site/data/*.json
```
Tidak perlu restart container; cukup muat ulang halaman.

Jenis soal: `mcq` (pilihan ganda), `listen` (dengar lalu pilih), `fill` (isian), `order` (susun kalimat), `match` (pasangkan).
Format teks: `**tebal**`, `*miring*`, `~~coret~~`, dan `[[kata Inggris]]` (bisa diklik untuk didengar).

Menambah level baru: tambahkan unit dengan `kelas="nama-level"` di `content/units.py`, lalu daftarkan levelnya di `LEVELS` dalam `site/app.js`. Unit yang file isinya belum ada tampil sebagai "segera hadir".

## Level dan unit

**Kelas 7 (9 unit)**
1 Hello! · 2 My Family and Friends · 3 Numbers, Time, and Dates · 4 My Daily Activities · 5 My School · 6 Describing People and Things · 7 Hobbies and Abilities · 8 Food and Drinks · 9 Places and Directions

**Kelas 8 (9 unit)**
1 What Did You Do? (simple past) · 2 What Are You Doing? (present continuous) · 3 Comparing Things · 4 Future Plans (will, be going to) · 5 How to Make It (procedure text) · 6 Describing Places and Animals · 7 Announcements and Invitations · 8 Rules and Advice (modals) · 9 Health, Letters, and Emails

**Kelas 9 (8 unit)**
1 Once Upon a Time (narrative, past continuous) · 2 Report Text · 3 Made in Indonesia (passive voice) · 4 If ..., Then ... (conditional 1) · 5 Have You Ever ...? (present perfect) · 6 Giving Opinions · 7 Short Presentations · 8 Exam Review

**Kelas 10 (8 unit)**
1 Getting to Know Each Other · 2 Descriptive Text · 3 Recount Text · 4 Procedure Text · 5 Narrative Text · 6 Announcements and Invitations · 7 Reading Short Texts · 8 Review Kelas 10

**Kelas 11 (7 unit)**
1 Giving Opinions and Arguing · 2 Analytical Exposition · 3 Hortatory Exposition · 4 Explanation Text · 5 News Item · 6 Application Letter and CV · 7 Review Kelas 11

**Kelas 12 (6 unit)**
1 Conditional Sentences · 2 Passive Voice and Reported Speech · 3 Job Interview · 4 Reading for Exams · 5 Grammar for Exams · 6 Final Review

**Pekerja / Formal (14 unit)**
1 Workplace Introductions and Small Talk · 2 Office Life and Job Roles · 3 Polite Requests and Offers · 4 Professional Emails · 5 Phone Calls and Voicemail · 6 Scheduling and Appointments · 7 Meetings · 8 Reports and Data · 9 Presentations · 10 Customer Service and Complaints · 11 Problem Solving and Status Updates · 12 Feedback and Career Growth · 13 Business Travel · 14 Review Level Pekerja

Topik dan susunan unit adalah rancangan sendiri, bukan kurikulum resmi. Soal dibuat sendiri dan belum ditinjau guru.

## Bank soal
Setiap unit punya bank soal yang lebih besar dari yang ditampilkan: tiap sesi Latihan mengambil 16 soal acak dan tiap Kuis 10 soal acak, jadi mengulang selalu memberi soal berbeda. Total bank saat ini: 4094 soal latihan dan 2329 soal kuis (6423 soal).

Soal dasar ada di `content/uNN.py` dan soal tambahan di `content/uNN_extra.py`. Unit Kelas 7-9 punya tiga ronde tambahan: `content/uNN_more.py` (soal bacaan, mencari kalimat salah, melengkapi dialog, terjemahan), `content/uNN_plus.py` (situasi, ejaan, kata tanya, melengkapi kalimat), dan `content/uNN_ext.py` (benar/salah dari teks, memperbaiki kesalahan, sinonim dan antonim, bunyi mirip). Duplikat persis dibuang otomatis oleh `build.py`.
