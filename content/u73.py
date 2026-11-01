from qk import mk, mkf, mko

UNIT = dict(
 id="u73",
 goals=[
  "memilih tense yang tepat dari **tense masa lampau**: past simple, continuous, perfect, perfect continuous",
  "membedakan **past simple** dari **present perfect** di cerita",
  "menyusun **urutan kejadian** dengan tense yang konsisten",
  "mengecek diri dengan **latihan campuran** masa lampau",
 ],
 lesson=[
  dict(t="intro", text="Sekarang latihan kontras untuk masa lampau. Tiga pertanyaan penuntun: (1) apakah **waktunya disebut**? (2) apakah kejadiannya **selesai atau sedang berlangsung**? (3) apakah ada kejadian lain yang **lebih dulu**?"),

  dict(t="grammar", title="1. Peta keputusan masa lampau",
   table=[["Ciri kalimat", "Tense", "Contoh"],
          ["kejadian selesai, waktu jelas", "past simple", "[[I met her yesterday.]]"],
          ["sedang berlangsung pada satu saat lampau", "past continuous", "[[I was walking when it rained.]]"],
          ["terjadi lebih dulu daripada kejadian lampau lain", "past perfect", "[[She had left when I arrived.]]"],
          ["kegiatan panjang sebelum kejadian lampau", "past perfect continuous", "[[I had been waiting for an hour when she came.]]"],
          ["tanpa waktu, ada hubungan sekarang", "present perfect", "[[I have met her.]]"]]),

  dict(t="grammar", title="2. Past perfect continuous",
   table=[["Pola", "Rumus", "Contoh"],
          ["Positif", "had been + V-ing", "[[I had been waiting for an hour.]]"],
          ["Negatif", "hadn't been + V-ing", "[[I hadn't been sleeping.]]"],
          ["Tanya", "Had + subjek + been + V-ing?", "[[Had you been waiting long?]]"]],
   examples=[dict(en="[[She was tired because she had been working all day.]]", id="Dia lelah karena sudah bekerja sepanjang hari.")]),

  dict(t="grammar", title="3. Cerita dalam empat lapisan",
   table=[["Lapisan", "Tense", "Contoh"],
          ["Latar", "past continuous", "[[It was raining.]]"],
          ["Kejadian utama", "past simple", "[[A man knocked on the door.]]"],
          ["Yang terjadi sebelumnya", "past perfect", "[[He had lost his way.]]"],
          ["Lama sebelumnya", "past perfect continuous", "[[He had been walking for hours.]]"]]),

  dict(t="warn", title="Past simple atau present perfect?",
   text="Dalam cerita masa lalu yang waktunya jelas, pakai past simple. Present perfect hanya untuk hubungan dengan sekarang. Jangan campur: bukan ~~Yesterday I have gone~~."),
 ],

 practice=mk([
  ('Pilih bentuk yang benar: "I ___ her yesterday."', "met", "have met", "was meeting", "meet", "yesterday → past simple."),
  ('Pilih bentuk yang benar: "I ___ home when it began to rain."', "was walking", "walked", "have walked", "walk", "Latar → continuous."),
  ('Pilih bentuk yang benar: "When I arrived, she ___ already left."', "had", "has", "have", "was", "Lebih dulu → had + V3."),
  ('Pilih bentuk yang benar: "She was tired because she ___ working all day."', "had been", "has been", "was", "is", "had been + V-ing."),
  ('Pilih bentuk yang benar: "I ___ for an hour when she finally came."', "had been waiting", "waited", "was wait", "have waited", "Lama sebelum kejadian."),
  ('Pilih bentuk yang benar: "It was dark. The rain ___ hard."', "was falling", "fell", "falls", "has fallen", "Latar."),
  ('Pilih bentuk yang benar: "Suddenly, a man ___ on the door."', "knocked", "was knocking", "had knocked", "knocks", "Kejadian utama."),
  ('Pilih bentuk yang benar: "He was wet because he ___ in the rain."', "had been walking", "walked", "walks", "is walking", "Penyebab lebih dulu."),
  ('Pilih bentuk yang benar: "___ you been waiting long when the bus came?"', "Had", "Have", "Did", "Were", "Had you been."),
  ('Pilih bentuk yang benar: "I ___ the film before, so I didn\'t go."', "had seen", "have seen", "saw", "was seeing", "Lebih dulu."),
  ('Pilih bentuk yang benar: "Last year I ___ to Japan."', "went", "have gone", "had gone", "was go", "last year → past simple."),
  ('Pilih bentuk yang benar: "I ___ never been to Japan before that trip."', "had", "have", "was", "did", "Sebelum kejadian lampau."),
  ('Pilih kalimat yang benar:', "While I was cooking, the phone rang.", "While I cooked, the phone was ringing.", "While I cook, the phone rang.", "While I had cooked, the phone rang.", "Latar vs memotong."),
  ('Pilih kalimat yang SALAH:', "Yesterday I have gone to the market.", "Yesterday I went to the market.", "I have gone to the market.", "I had gone before she came.", "yesterday → past simple."),
  ('Pilih kalimat yang SALAH:', "She had been came late.", "She had come late.", "She came late.", "She had been working.", "had come atau had been working."),
  ('Pilih kalimat yang SALAH:', "When I arrived, she has left.", "When I arrived, she had left.", "When I arrived, she left.", "When I arrived, she was leaving.", "has → had."),
 ]) + mkf([
  ("Aku bertemu dia kemarin.", "I ___ her yesterday. (meet)", "met", "past simple."),
  ("Aku sedang berjalan ketika hujan turun.", "I ___ walking when it rained. (be)", "was", "past continuous."),
  ("Ketika aku tiba, dia sudah pergi.", "When I arrived, she ___ left. (have)", "had", "past perfect."),
  ("Dia lelah karena sudah bekerja sepanjang hari.", "She was tired because she had ___ working all day. (be)", "been", "had been + V-ing."),
  ("Aku sudah menunggu selama satu jam ketika dia datang.", "I had been ___ for an hour. (wait)", "waiting", "had been + V-ing."),
  ("Tahun lalu aku pergi ke Jepang.", "Last year I ___ to Japan. (go)", "went", "past simple."),
 ]) + mko([
  ("Ketika aku tiba, filmnya sudah mulai.", "When I arrived, the film had started.", "has started", ""),
  ("Aku sedang menonton TV ketika dia menelepon.", "I was watching TV when she called.", "watched call", ""),
  ("Dia lelah karena sudah bekerja sepanjang hari.", "She was tired because she had been working all day.", "has worked", ""),
 ]),

 quiz=mk([
  ('Pilih bentuk yang benar: "He ___ the door and walked in."', "opened", "was opening", "had been opening", "opens", "Urutan kejadian selesai."),
  ('Pilih bentuk yang benar: "At nine last night, we ___ dinner."', "were having", "had", "have had", "had had to", "Pada satu saat."),
  ('Pilih bentuk yang benar: "By the time we arrived, they ___ gone."', "had", "have", "were", "did", "had + V3."),
  ('Pilih bentuk yang benar: "She ___ for hours when he called."', "had been studying", "studied", "studies", "is studying", "Lama sebelumnya."),
  ('Pilih bentuk yang benar: "While I ___ , she was reading."', "was cooking", "cooked", "cook", "had cooked", "Dua kegiatan bersamaan."),
  ('Pilih kalimat yang SALAH:', "I was knowing the answer.", "I knew the answer.", "I was thinking about it.", "I had known it.", "know tidak continuous."),
  ('Pilih kalimat yang SALAH:', "He had saw it already.", "He had seen it already.", "He saw it yesterday.", "He hadn't seen it.", "V3: seen."),
  ('Pilih kalimat yang benar:', "She was sad because she had lost her phone.", "She was sad because she has lost her phone.", "She sad because lost her phone.", "She is sad because she had lost.", "Penyebab lebih dulu."),
 ]) + mkf([
  ("Dia pergi kemarin.", "She ___ yesterday. (leave)", "left", "past simple."),
  ("Mereka sedang tidur pukul sepuluh.", "They ___ sleeping at ten. (be)", "were", "past continuous."),
  ("Aku sudah makan sebelum dia datang.", "I ___ eaten before she came. (have)", "had", "past perfect."),
 ]),
)
