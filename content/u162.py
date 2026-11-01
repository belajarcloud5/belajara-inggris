import random
from ub import *
import u157, u158, u159, u160
UNIT = mkunit("u162",
 ["mengerjakan **tes mini** bergaya TOEFL ITP",
  "menguji **Listening, Structure, Written Expression, dan Reading** sekaligus",
  "melatih **ketepatan waktu** (sekitar 30–40 detik per soal)",
  "mengetahui bagian yang perlu diperkuat"],
 [intro("Ini tes mini campuran dari unit TOEFL sebelumnya. Kerjakan tanpa membuka materi, lalu cek hasilnya. Untuk simulasi waktu, pakai **Mode ujian** di halaman level TOEFL."),
  gram("Peta tes mini",
   table=[["Bagian", "Jumlah soal di sini", "Waktu yang disarankan"],
          ["Listening", "8", "sekitar 5 menit"],
          ["Structure", "8", "sekitar 4 menit"],
          ["Written Expression", "8", "sekitar 4 menit"],
          ["Reading", "8", "sekitar 8 menit"]]),
  tip("Evaluasi setelah tes", text="Catat bagian dengan skor terendah dan ulangi unit yang bersangkutan: u157 (Listening), u158 (Structure), u159 (Written Expression), u160 (Reading)."),
  summary(["Kerjakan cepat tanpa membuka materi.", "Evaluasi: bagian mana yang terendah?", "Gunakan Mode ujian untuk simulasi waktu."])],
 [], [])
rng = random.Random(162)
P = []
P += rng.sample([q for q in u157.UNIT["practice"] if q["type"] == "listen"], 8)
P += rng.sample([q for q in u158.UNIT["practice"]], 8)
P += rng.sample([q for q in u159.UNIT["practice"]], 8)
P += rng.sample([q for q in u160.UNIT["practice"]], 8)
Q = rng.sample(u158.UNIT["quiz"], 3) + rng.sample(u159.UNIT["quiz"], 3) + rng.sample(u160.UNIT["quiz"], 2)
UNIT["practice"] = P
UNIT["quiz"] = Q
