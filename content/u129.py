import random
from ub import *
import u122, u123, u124, u125, u126, u127, u128
UNIT = mkunit("u129",
 ["mengulang **bandara, hotel, restoran, transportasi, belanja, darurat, dan obrolan ringan**",
  "berlatih **percakapan** singkat yang sering terjadi saat bepergian",
  "mendengar dan menulis **kalimat bepergian**",
  "memilih unit yang perlu diulang"],
 [intro("Unit ini mengulang seluruh level **Inggris untuk Bepergian**. Kerjakan latihan dan kuis, lalu ulangi unit yang masih terasa sulit."),
  gram("Ringkasan pola penting",
   table=[["Tujuan", "Pola", "Contoh"],
          ["Memesan / meminta", "[[I'd like ...]] / [[Could I have ...?]]", "[[Could I have the bill, please?]]"],
          ["Bertanya ada atau tidak", "[[Is there ...?]] / [[Do you have ...?]]", "[[Is there a pharmacy near here?]]"],
          ["Bertanya harga / cara", "[[How much is ...?]] / [[How do I get to ...?]]", "[[How do I get to the station?]]"],
          ["Melaporkan masalah", "[[The ... is broken.]] / [[I have lost ...]]", "[[The shower is broken.]]"],
          ["Berkenalan", "[[Nice to meet you.]] / [[Where are you from?]]", "[[I'm from Indonesia. And you?]]"]]),
  tip("Kalimat pendek lebih aman", text="Saat gugup, pakai kalimat pendek dan jelas: *One ticket, please.* *I need help.* Lawan bicara menghargai kejelasan lebih daripada kerumitan."),
  summary(["Pola sopan: I'd like ..., Could I have ...?", "Tanya: Is there ...? How much ...? How do I get to ...?", "Masalah: The ... is broken. I have lost ...", "Berkenalan: Nice to meet you. Where are you from?"])],
 [], [])
rng = random.Random(129)
P, Q = [], []
for u in (u122, u123, u124, u125, u126, u127, u128):
    P += rng.sample([q for q in u.UNIT["practice"] if q["type"] in ("mcq", "listen")], 5)
    P += rng.sample([q for q in u.UNIT["practice"] if q["type"] == "reply"], 2)
    Q += rng.sample(u.UNIT["quiz"], 2)
P += dictate([("Could I have the bill, please?", "Boleh minta tagihannya?"), ("I would like a window seat, please.", "Saya mau kursi dekat jendela."),
              ("How do I get to the station?", "Bagaimana cara ke stasiun?"), ("I have lost my passport.", "Paspor saya hilang."),
              ("Nice to meet you, I'm Rani.", "Senang bertemu denganmu, aku Rani.")])
UNIT["practice"] = P
UNIT["quiz"] = Q
