import random
from ub import *
import u100, u101, u102, u103, u104, u105, u106, u107, u108, u109, u110, u111, u112
UNIT = mkunit("u113",
 ["mengulang **kata tertukar, awalan, akhiran, dan kosakata tema**",
  "mengulang **tanda baca, paragraf, dan email**",
  "mengerjakan latihan **campuran** dari semua unit kosakata dan menulis",
  "menemukan bagian yang perlu diulang"],
 [intro("Unit ini mengulang seluruh level Kosakata dan Menulis. Kerjakan latihan dan kuis, lalu ulangi unit yang masih sulit."),
  gram("Peta ringkas",
   table=[["Unit", "Isi utama", "Contoh"],
          ["100–101 Kata tertukar", "its/it's, there/their, make/do, affect/effect", "[[its]] – [[it's]], [[make]] – [[do]]"],
          ["102–103 Pembentukan kata", "awalan dan akhiran", "[[unhappy]], [[teacher]], [[careful]]"],
          ["104–109 Kosakata tema", "rumah, tubuh, pakaian, kota, pekerjaan, hobi", "[[kitchen]], [[fever]], [[size]], [[station]], [[mechanic]], [[chess]]"],
          ["110 Tanda baca", "kapital, koma, apostrof", "[[Rani's bag]], [[However,]]"],
          ["111 Paragraf", "topik, pendukung, penutup", "[[First]], [[That is why]]"],
          ["112 Email", "salam, isi, penutup", "[[Dear Mr. Adi,]], [[Yours sincerely]]"]]),
  tip("Rutinitas mingguan", text="Pilih satu tema kosakata per minggu, tulis satu paragraf pendek tentangnya, lalu kirim email kepada dirimu sendiri memakai kata baru."),
  summary(["Kata tertukar: pelajari berpasangan.", "Awalan dan akhiran memperbanyak kosakata.", "Kosakata tema + pola kalimat.", "Tanda baca, paragraf, dan email."])],
 [], [])
rng = random.Random(113)
P, Q = [], []
for u in (u100, u101, u102, u103, u110, u111, u112):
    pr = [q for q in u.UNIT["practice"] if q["type"] in ("mcq", "fill")]
    P += rng.sample(pr, 7)
    Q += rng.sample(u.UNIT["quiz"], 1)
for u in (u104, u105, u106, u107, u108, u109):
    pr = [q for q in u.UNIT["practice"] if q["type"] in ("mcq", "listen")]
    P += rng.sample(pr, 5)
    Q += rng.sample(u.UNIT["quiz"], 1)
P += dictate([("It is impossible to unlock the unfair rule.", "Mustahil membuka aturan yang tidak adil itu."), ("Rani's mother is a busy nurse at a hospital.", "Ibu Rani adalah perawat sibuk di rumah sakit."),
              ("When it rains, we stay at home and watch a film.", "Kalau hujan, kami di rumah dan menonton film."), ("Dear Mr. Adi, I am writing to ask about the course.", "Yth. Pak Adi, saya menulis untuk menanyakan kursus.")])
Q += mk([
 ('Pilih yang benar: "The cat licked ___ paw."', 'its', "it's", 'it', 'is', 'Milik kucing.'),
 ('Pilih awalan yang tepat untuk "tidak setuju": ___agree', 'dis', 'un', 'im', 'mis', 'Dis- = tidak.'),
])
UNIT["practice"] = P
UNIT["quiz"] = Q
