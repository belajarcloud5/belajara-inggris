# Let's Learn English! (SMP)

Web belajar bahasa Inggris interaktif untuk SMP: Kelas 7, 8 (masing-masing 9 unit), dan 9 (8 unit) sudah lengkap. Setiap unit masing-masing berisi **Belajar**, **Latihan** (16 soal), dan **Kuis** (10 soal, bintang 1-3).

## Menjalankan
```bash
docker compose up -d        # buka http://localhost:8085
```
Kemajuan dan bintang tersimpan di browser (localStorage). Suara memakai suara bawaan browser.

## Mengubah atau menambah isi
Isi ada di `content/uNN.py` (daftar unit di `content/units.py`, pembuat soal di `content/helpers.py`).
Setelah mengubah, jalankan:
```bash
python3 build.py            # validasi soal dan menulis site/data/*.json
```
Tidak perlu restart container; cukup muat ulang halaman.

Jenis soal: `mcq` (pilihan ganda), `listen` (dengar lalu pilih), `fill` (isian), `order` (susun kalimat), `match` (pasangkan).
Format teks: `**tebal**`, `*miring*`, `~~coret~~`, dan `[[kata Inggris]]` (bisa diklik untuk didengar).

## Unit Kelas 7
1 Hello! · 2 My Family and Friends · 3 Numbers, Time, and Dates · 4 My Daily Activities · 5 My School · 6 Describing People and Things · 7 Hobbies and Abilities · 8 Food and Drinks · 9 Places and Directions

## Unit Kelas 8
1 What Did You Do? (simple past) · 2 What Are You Doing? (present continuous) · 3 Comparing Things · 4 Future Plans (will, be going to) · 5 How to Make It (procedure text) · 6 Describing Places and Animals · 7 Announcements and Invitations · 8 Rules and Advice (modals) · 9 Health, Letters, and Emails

## Unit Kelas 9
1 Once Upon a Time (narrative, past continuous) · 2 Report Text · 3 Made in Indonesia (passive voice) · 4 If ..., Then ... (conditional 1) · 5 Have You Ever ...? (present perfect) · 6 Giving Opinions · 7 Short Presentations · 8 Exam Review (rangkuman dan latihan campuran)
