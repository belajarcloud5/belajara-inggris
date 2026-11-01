import random
from ub import *
import u168, u169, u170, u171, u172, u173
UNIT = mkunit("u174",
 ["mengulang **semua unit menulis**: kalimat, deskripsi, cerita, esai, ringkasan, pesan",
  "mengerjakan latihan **campuran** berbagai tipe soal",
  "menemukan unit yang perlu diulang",
  "menyusun **rencana menulis mingguan**"],
 [intro("Unit ini mengulang seluruh level **Menulis Lanjutan**. Kerjakan latihan dan kuis, lalu ulangi unit yang masih sulit."),
  gram("Peta ringkas",
   table=[["Unit", "Isi utama", "Contoh"],
          ["168 Menggabungkan kalimat", "and, but, so, because, although, who, which", "[[Although it rained, we went out.]]"],
          ["169 Deskripsi", "detail spesifik, lima indra, urutan sifat", "[[a lovely small old wooden box]]"],
          ["170 Cerita", "awal, masalah, penyelesaian, penanda waktu", "[[Suddenly, the lights went out.]]"],
          ["171 Esai opini", "thesis, alasan, contoh, kesimpulan", "[[In conclusion, ...]]"],
          ["172 Ringkas dan parafrase", "ganti kata dan struktur, jaga makna", "[[buy → purchase]]"],
          ["173 Pesan singkat", "siapa, apa, kapan, di mana, sopan", "[[Could you please send me ...?]]"]]),
  tip("Rencana mingguan", text="Senin: satu paragraf deskripsi. Rabu: ringkas satu artikel. Jumat: tulis pesan resmi. Minggu: satu cerita pendek."),
  summary(["Variasi kalimat dengan penghubung.", "Detail spesifik dalam deskripsi.", "Cerita: awal, masalah, akhir.", "Esai: thesis, alasan, contoh, kesimpulan.", "Parafrase: kata dan struktur berbeda.", "Pesan: jelas, sopan, lengkap."])],
 [], [])
rng = random.Random(174)
P, Q = [], []
for u in (u168, u169, u170, u171, u172, u173):
    P += rng.sample(u.UNIT["practice"], 7)
    Q += rng.sample(u.UNIT["quiz"], 2)
UNIT["practice"] = P
UNIT["quiz"] = Q
