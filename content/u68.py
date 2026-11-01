from qk import mk, mkf, mko

UNIT = dict(
 id="u68",
 goals=[
  "membentuk **past perfect** dengan had + V3",
  "menyusun dua kejadian lampau: yang **lebih dulu** dan yang **kemudian**",
  "memakai **before, after, by the time, already, when** dengan past perfect",
  "membedakan past perfect dari past simple dan present perfect",
 ],
 lesson=[
  dict(t="intro", text="**Past perfect** dipakai saat dua kejadian di masa lampau terjadi berurutan. Kejadian yang **lebih dulu** memakai **had + V3**, kejadian yang **kemudian** memakai **past simple**. Bayangkan: ada masa lalu di dalam masa lalu."),

  dict(t="grammar", title="1. Rumus",
   table=[["Pola", "Rumus", "Contoh"],
          ["Positif", "had + V3", "[[I had finished.]]"],
          ["Negatif", "had not (hadn't) + V3", "[[I hadn't finished.]]"],
          ["Tanya", "Had + subjek + V3?", "[[Had you finished?]]"]],
   examples=[dict(en="[[When I arrived, the film had started.]]", id="Ketika aku tiba, filmnya sudah mulai. (mulai lebih dulu, tiba kemudian)")]),

  dict(t="grammar", title="2. Dua kejadian lampau",
   table=[["Urutan", "Tense", "Contoh"],
          ["lebih dulu", "had + V3", "[[She had left]]"],
          ["kemudian", "past simple", "[[when I called.]]"]],
   examples=[dict(en="[[She had left when I called.]]", id="Dia sudah pergi ketika aku menelepon."),
             dict(en="[[I called, and she left.]]", id="Aku menelepon, lalu dia pergi. (urutan biasa, past simple semua)")]),

  dict(t="grammar", title="3. Kata penghubung",
   table=[["Kata", "Contoh"],
          ["**before**", "[[She had left before I called.]]"],
          ["**after**", "[[After she had left, I called.]] / [[After she left, I called.]]"],
          ["**by the time**", "[[By the time I arrived, the film had started.]]"],
          ["**already / just**", "[[The film had already started.]]"],
          ["**when**", "[[When I got there, they had gone.]]"]]),

  dict(t="grammar", title="4. Past perfect dalam cerita dan alasan",
   table=[["Contoh", "Fungsi"],
          ["[[He was late because he had missed the bus.]]", "alasan sebelum kejadian"],
          ["[[She was sad. She had lost her phone.]]", "penyebab yang terjadi lebih dulu"],
          ["[[I didn't go because I had already seen the film.]]", "alasan yang sudah terjadi"]]),

  dict(t="warn", title="Jangan berlebihan",
   text="Jika urutannya sudah jelas dari **before/after**, past simple boleh dipakai: [[After she left, I called.]] Dan past perfect tidak dipakai untuk kejadian tunggal: bukan ~~I had visited Bali last year~~."),
 ],

 practice=mk([
  ('Pilih bentuk yang benar: "When I arrived, the film ___ started."', "had", "has", "was", "did", "Lebih dulu → had + V3."),
  ('Pilih bentuk yang benar: "She ___ left when I called."', "had", "has", "have", "was", "had + V3."),
  ('Pilih bentuk yang benar: "He was late because he ___ missed the bus."', "had", "has", "have", "is", "Sebab yang lebih dulu."),
  ('Pilih bentuk yang benar: "I ___ eaten before she came."', "had", "have", "has", "am", "Sebelum kejadian lampau."),
  ('Pilih bentuk yang benar: "By the time we arrived, they ___ gone."', "had", "have", "has", "were", "By the time → had + V3."),
  ('Pilih bentuk yang benar: "After she ___ finished, she went home."', "had", "has", "have", "is", "after + had."),
  ('Pilih bentuk yang benar: "I didn\'t go because I ___ seen the film."', "had already", "have already", "already was", "did already", "had already."),
  ('Pilih bentuk yang benar: "She ___ lost her phone, so she was sad."', "had", "has", "have", "did", "Penyebab lebih dulu."),
  ('Pilih bentuk yang benar: "When I got there, they ___ left." (tidak)', "hadn\'t", "haven\'t", "didn\'t", "weren\'t", "hadn't + V3."),
  ('Pilih bentuk yang benar: "___ you finished when I called?"', "Had", "Have", "Did", "Were", "Had + subjek + V3."),
  ('Pilih bentuk yang benar: "I ___ breakfast before I left home."', "had eaten", "have eaten", "was eating", "eat", "Sebelum kejadian lampau."),
  ('Pilih bentuk yang benar: "She ___ Japanese before she moved to Tokyo."', "had studied", "has studied", "studies", "is studying", "Lebih dulu → had + V3."),
  ('Pilih kalimat yang benar:', "When I arrived, she had left.", "When I arrived, she has left.", "When I arrived, she leaved.", "When I arrived, she had leave.", "had + V3."),
  ('Pilih kalimat yang SALAH:', "I had visited Bali last year.", "I visited Bali last year.", "I had visited Bali before I moved.", "I had never been there.", "Kejadian tunggal → past simple."),
  ('Pilih kalimat yang SALAH:', "She had went home.", "She had gone home.", "She went home.", "She had left.", "V3 dari go adalah gone."),
  ('Pilih kalimat yang SALAH:', "When I called, she has left.", "When I called, she had left.", "When I called, she left.", "When I called, she was leaving.", "has → had (masa lampau)."),
 ]) + mkf([
  ("Ketika aku tiba, filmnya sudah mulai.", "When I arrived, the film ___ started. (have)", "had", "had + V3."),
  ("Dia sudah pergi ketika aku menelepon.", "She ___ left when I called. (have)", "had", "had + V3."),
  ("Dia terlambat karena ketinggalan bus.", "He was late because he ___ missed the bus.", "had", "sebab lebih dulu."),
  ("Sebelum dia datang, aku sudah makan.", "I ___ eaten before she came.", "had", "had + V3."),
  ("Pada saat kami tiba, mereka sudah pergi.", "By the time we arrived, they had ___. (go)", "gone", "V3 dari go."),
  ("Aku tidak pergi karena sudah menonton film itu.", "I didn't go because I had ___ seen the film.", "already", "had already + V3."),
 ]) + mko([
  ("Ketika aku tiba, dia sudah pergi.", "When I arrived, she had left.", "has left", ""),
  ("Dia terlambat karena ketinggalan bus.", "He was late because he had missed the bus.", "has missed", ""),
  ("Sebelum pergi, aku sudah makan.", "I had eaten before I left.", "have eaten", ""),
 ]),

 quiz=mk([
  ('Rumus past perfect adalah...', "had + V3", "have + V3", "was + V-ing", "will have + V3", "had + V3."),
  ('Pilih bentuk yang benar: "When she came, I ___ already eaten."', "had", "have", "has", "did", "Lebih dulu → had."),
  ('Pilih bentuk yang benar: "He ___ never seen the sea before that day."', "had", "has", "have", "was", "Sebelum satu hari di masa lampau."),
  ('Pilih bentuk yang benar: "By the time I got home, my parents ___ gone to bed."', "had", "have", "has", "are", "By the time → had."),
  ('Pilih kalimat yang SALAH:', "I had finished yesterday.", "I finished yesterday.", "I had finished before she came.", "I hadn't finished.", "Tanpa kejadian lain → past simple."),
  ('Pilih kalimat yang benar:', "She was tired because she had worked all day.", "She was tired because she has worked all day.", "She is tired because she had worked.", "She tired because had worked.", "Penyebab lebih dulu."),
  ('Pilih kalimat yang SALAH:', "He had saw it before.", "He had seen it before.", "He saw it yesterday.", "He hadn't seen it.", "V3: seen."),
  ('Pilih bentuk yang benar: "I called her, and she ___ left." (sudah pergi)', "had", "has", "have", "was", "Sudah pergi lebih dulu."),
 ]) + mkf([
  ("Dia sudah makan sebelum aku datang.", "She had ___ before I came. (eat)", "eaten", "V3 dari eat."),
  ("Kami sudah tiba ketika hujan mulai.", "We ___ arrived when the rain started. (have)", "had", "had + V3."),
  ("Mereka belum pergi ketika aku menelepon.", "They ___ left when I called. (not)", "hadn't/had not", "had not + V3."),
 ]),
)
