from qk import mk, mkf, mko

UNIT = dict(
 id="u74",
 goals=[
  "menjaga **konsistensi tense** dalam cerita, email, dan laporan",
  "memakai tense yang tepat untuk **narasi**, **berita**, dan **laporan data**",
  "mengubah tense pada **ujaran tidak langsung** (reported speech)",
  "menghubungkan tense dengan **kalimat bersyarat**",
 ],
 lesson=[
  dict(t="intro", text="Sampai sini kamu sudah mengenal tiap tense. Sekarang kita lihat bagaimana tense bekerja **bersama-sama** di teks nyata: cerita, laporan, ujaran tidak langsung, dan kalimat bersyarat. Aturan utamanya: **pilih satu 'waktu utama' lalu jaga konsistensinya**."),

  dict(t="grammar", title="1. Konsistensi dalam teks",
   table=[["Jenis teks", "Waktu utama", "Contoh"],
          ["Cerita masa lalu", "past simple (+ continuous, perfect)", "[[Yesterday I woke up late. It was raining, so I took a taxi.]]"],
          ["Kebiasaan dan fakta", "present simple", "[[I wake up at six. I take a bus.]]"],
          ["Rencana", "future / be going to", "[[Tomorrow I will wake up early.]]"],
          ["Berita", "past simple + present perfect", "[[A fire has destroyed a market. Police said it started at nine.]]"],
          ["Laporan data", "past simple (data) + present (kesimpulan)", "[[Sales rose by 10%. This shows that demand is growing.]]"]]),

  dict(t="grammar", title="2. Berpindah tense dengan alasan",
   text="Tense boleh berpindah jika waktunya memang berpindah:",
   table=[["Perpindahan", "Contoh"],
          ["past → present (fakta umum)", "[[She told me that water boils at 100 degrees.]]"],
          ["past → past perfect (lebih dulu)", "[[I was tired because I had slept badly.]]"],
          ["past → future-in-past", "[[He said he would call.]]"],
          ["present → present perfect (hasil)", "[[I live in Bali. I have lived here for years.]]"]]),

  dict(t="grammar", title="3. Reported speech: mundur satu langkah",
   table=[["Ucapan langsung", "Ujaran tidak langsung"],
          ["present simple → \"I am tired.\"", "past simple → [[She said she was tired.]]"],
          ["present continuous → \"I am working.\"", "past continuous → [[He said he was working.]]"],
          ["past simple → \"I went.\"", "past perfect → [[She said she had gone.]]"],
          ["present perfect → \"I have finished.\"", "past perfect → [[He said he had finished.]]"],
          ["will → \"I will call.\"", "would → [[She said she would call.]]"]]),

  dict(t="grammar", title="4. Tense dan conditional",
   table=[["Jenis", "Rumus", "Contoh"],
          ["zero", "if + present, present", "[[If you heat ice, it melts.]]"],
          ["type 1", "if + present, will + V1", "[[If it rains, I will stay.]]"],
          ["type 2", "if + past, would + V1", "[[If I were rich, I would travel.]]"],
          ["type 3", "if + past perfect, would have + V3", "[[If I had known, I would have come.]]"]]),

  dict(t="tip", title="Cek konsistensi saat menulis",
   text="Setelah menulis satu paragraf, baca ulang hanya **kata kerjanya**. Apakah semuanya mengikuti waktu utama? Jika ada yang berbeda, pastikan perpindahannya punya alasan."),
 ],

 practice=mk([
  ('Pilih paragraf yang konsisten:', "Yesterday I woke up late. It was raining, so I took a taxi.", "Yesterday I wake up late. It rains, so I took a taxi.", "Yesterday I woke up late. It is raining, so I take a taxi.", "Yesterday I wake up late. It was raining, so I take a taxi.", "Past semua."),
  ('Pilih tense yang tepat (cerita): "Last night, I ___ home and cooked dinner."', "went", "go", "have gone", "will go", "Cerita lampau."),
  ('Pilih tense yang tepat (kebiasaan): "Every morning, I ___ at six."', "wake up", "woke up", "will wake up", "had woken up", "Kebiasaan."),
  ('Pilih bentuk yang benar (berita): "A fire ___ a market this morning."', "has destroyed", "destroys", "will destroy", "was destroy", "Berita: perfect untuk kejadian baru."),
  ('Pilih bentuk yang benar (laporan): "Sales ___ by 10% last month."', "rose", "rise", "will rise", "have rised", "last month → past simple."),
  ('Ubah ke ujaran tidak langsung: "I am tired," she said. → She said she ___ tired.', "was", "is", "were", "will be", "Present → past."),
  ('Ubah: "I went home," he said. → He said he ___ gone home.', "had", "has", "have", "was", "Past → past perfect."),
  ('Ubah: "I will call you," she said. → She said she ___ call me.', "would", "will", "can", "does", "will → would."),
  ('Ubah: "I have finished," he said. → He said he ___ finished.', "had", "has", "have", "was", "Present perfect → past perfect."),
  ('Ubah: "I am working," she said. → She said she ___ working.', "was", "is", "were", "has been", "Present continuous → past continuous."),
  ('Pilih bentuk yang benar (type 1): "If it rains, I ___ stay home."', "will", "would", "did", "am", "Type 1."),
  ('Pilih bentuk yang benar (type 2): "If I were rich, I ___ travel."', "would", "will", "did", "am", "Type 2."),
  ('Pilih bentuk yang benar (type 3): "If I had known, I ___ come."', "would have", "will have", "did", "had", "Type 3."),
  ('Pilih kalimat yang SALAH:', "Yesterday I wake up late and took a taxi.", "Yesterday I woke up late and took a taxi.", "I wake up late and take a taxi.", "I woke up late and took a taxi.", "Konsisten."),
  ('Pilih kalimat yang SALAH:', "She said she will call me.", "She said she would call me.", "She said she was ready.", "She said she had left.", "will → would."),
  ('Pilih kalimat yang SALAH:', "If it will rain, I will stay.", "If it rains, I will stay.", "If it rained, I would stay.", "If it had rained, I would have stayed.", "Jangan will di if."),
 ]) + mkf([
  ("Kemarin aku bangun kesiangan.", "Yesterday I ___ up late. (wake)", "woke", "past simple."),
  ("Dia bilang dia lelah.", "She said she ___ tired. (be)", "was", "Present → past."),
  ("Dia bilang dia akan menelepon.", "She said she ___ call me.", "would", "will → would."),
  ("Dia bilang dia sudah selesai.", "He said he ___ finished. (have)", "had", "perfect → past perfect."),
  ("Kalau hujan, aku akan tinggal di rumah.", "If it rains, I ___ stay home.", "will/'ll", "Type 1."),
  ("Seandainya aku tahu, aku sudah datang.", "If I had known, I would ___ come.", "have", "Type 3."),
 ]) + mko([
  ("Kemarin aku bangun kesiangan dan naik taksi.", "Yesterday I woke up late and took a taxi.", "wake take", ""),
  ("Dia bilang dia akan menelepon.", "She said she would call me.", "will called", ""),
  ("Kalau hujan, aku akan tinggal di rumah.", "If it rains, I will stay home.", "would rain", ""),
 ]),

 quiz=mk([
  ('Pilih paragraf yang konsisten:', "I woke up at six. I took a bath and ate breakfast.", "I woke up at six. I take a bath and ate breakfast.", "I wake up at six. I took a bath and eat breakfast.", "I wake up at six. I took a bath and eaten breakfast.", "Past semua."),
  ('Ubah: "We are late," they said. → They said they ___ late.', "were", "are", "was", "will be", "Present → past."),
  ('Ubah: "I can swim," she said. → She said she ___ swim.', "could", "can", "will", "must", "can → could."),
  ('Pilih bentuk yang benar (berita): "The police ___ that two people were hurt."', "said", "say", "will say", "have say", "Berita: past simple."),
  ('Pilih bentuk yang benar (type 2): "If I had more time, I ___ help you."', "would", "will", "did", "am", "Type 2."),
  ('Pilih kalimat yang SALAH:', "He said he has finished.", "He said he had finished.", "He said he was tired.", "He said he would come.", "has → had."),
  ('Pilih kalimat yang SALAH:', "If I would be rich, I would travel.", "If I were rich, I would travel.", "If I had money, I would travel.", "If I had been rich, I would have traveled.", "Jangan would di klausa if."),
  ('Pilih kalimat yang benar:', "She told me that water boils at 100 degrees.", "She told me that water boiled at 100 degree.", "She told me that water boiling at 100 degrees.", "She told me that water has boil.", "Fakta umum boleh tetap present."),
 ]) + mkf([
  ("Kemarin dia pergi ke pasar.", "Yesterday she ___ to the market. (go)", "went", "past."),
  ("Dia bilang dia bisa berenang.", "She said she ___ swim.", "could", "can → could."),
  ("Kalau aku kaya, aku akan bepergian.", "If I were rich, I ___ travel.", "would", "Type 2."),
 ]),
)
