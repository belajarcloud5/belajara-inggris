from qk import mk, mkf, mko

UNIT = dict(
 id="u67",
 goals=[
  "membentuk **present perfect continuous** dengan have/has been + V-ing",
  "menjelaskan **lama kegiatan** yang masih berlangsung atau baru selesai",
  "membedakannya dengan **present perfect**",
  "memakai **for, since, all day, lately** dengan tepat",
 ],
 lesson=[
  dict(t="intro", text="**Present perfect continuous** menekankan **kegiatan** dan **berapa lama** kegiatan itu berlangsung. Cocok untuk menjelaskan sesuatu yang masih berlangsung, atau yang baru saja berhenti dan hasilnya terlihat."),

  dict(t="grammar", title="1. Rumus",
   table=[["Pola", "Rumus", "Contoh"],
          ["Positif", "have/has been + V-ing", "[[I have been waiting.]] / [[She has been waiting.]]"],
          ["Negatif", "have/has not been + V-ing", "[[I haven't been sleeping.]]"],
          ["Tanya", "Have/Has + subjek + been + V-ing?", "[[Have you been waiting long?]]"]]),

  dict(t="grammar", title="2. Dua pemakaian",
   table=[["Pemakaian", "Contoh", "Artinya"],
          ["**Masih berlangsung**", "[[I have been studying for two hours.]]", "Aku sudah belajar dua jam (dan masih)."],
          ["**Baru selesai, ada hasil**", "[[I am tired. I have been running.]]", "Aku lelah karena baru saja berlari."]],
   examples=[dict(en="[[It has been raining since morning.]]", id="Hujan turun sejak pagi.")]),

  dict(t="grammar", title="3. Bedanya dengan present perfect",
   table=[["Present perfect", "Present perfect continuous"],
          ["[[I have read this book.]] (selesai)", "[[I have been reading this book.]] (kegiatan, mungkin belum selesai)"],
          ["[[She has painted the room.]] (hasil)", "[[She has been painting the room.]] (kegiatan, ada cat di bajunya)"],
          ["jumlah: [[I have written three emails.]]", "durasi: [[I have been writing for an hour.]]"]]),

  dict(t="warn", title="Kata kerja keadaan tidak dipakai",
   text="Seperti continuous lainnya, kata kerja keadaan tidak dipakai: katakan [[I have known her for ten years.]], bukan ~~I have been knowing her~~. Dan untuk jumlah, pakai present perfect: [[I have written three emails.]]"),
 ],

 practice=mk([
  ('Pilih bentuk yang benar: "I ___ waiting for an hour."', "have been", "has been", "am", "was been", "I + have been."),
  ('Pilih bentuk yang benar: "She ___ studying since morning."', "has been", "have been", "is", "was", "she + has been."),
  ('Pilih bentuk yang benar: "It has been ___ all day."', "raining", "rained", "rain", "rains", "been + V-ing."),
  ('Pilih bentuk yang benar: "They have been ___ for two hours."', "playing", "played", "play", "plays", "been + V-ing."),
  ('Pilih bentuk yang benar: "How long ___ you been waiting?"', "have", "has", "did", "are", "have you been."),
  ('Pilih bentuk yang benar: "He ___ been working here since 2020."', "has", "have", "is", "had", "he → has."),
  ('Pilih bentuk yang benar: "I\'m tired. I ___ running."', "have been", "was", "am been", "has been", "Baru selesai, ada hasil."),
  ('Pilih bentuk yang benar: "I ___ three emails today." (jumlah)', "have written", "have been writing", "am writing", "wrote been", "Jumlah → present perfect."),
  ('Pilih bentuk yang benar: "I ___ for an hour." (durasi)', "have been writing", "have written", "wrote", "am write", "Durasi → perfect continuous."),
  ('Pilih bentuk yang benar: "I ___ her for ten years."', "have known", "have been knowing", "am knowing", "knowing", "know = stative."),
  ('Pilih bentuk yang benar: "We ___ learning English for three years."', "have been", "has been", "are", "did", "we + have been."),
  ('Pilih bentuk yang benar: "She is covered in paint. She ___ the room."', "has been painting", "paints", "will paint", "painted been", "Hasil terlihat."),
  ('Pilih kalimat yang benar:', "I have been waiting for an hour.", "I have waiting for an hour.", "I am been waiting for an hour.", "I has been waiting for an hour.", "have been + V-ing."),
  ('Pilih kalimat yang SALAH:', "She has been knowing him for years.", "She has known him for years.", "She has been working for years.", "She has been waiting.", "know tidak continuous."),
  ('Pilih kalimat yang SALAH:', "He have been sleeping.", "He has been sleeping.", "They have been sleeping.", "I have been sleeping.", "he → has been."),
 ]) + mkf([
  ("Aku sudah menunggu selama satu jam.", "I ___ been waiting for an hour. (have)", "have", "have been + V-ing."),
  ("Dia sudah belajar sejak pagi.", "She has been ___ since morning. (study)", "studying", "been + V-ing."),
  ("Hujan turun sejak pagi.", "It has been ___ since morning. (rain)", "raining", "been + V-ing."),
  ("Sudah berapa lama kamu menunggu?", "How long ___ you been waiting?", "have", "have you been."),
  ("Mereka sudah bermain selama dua jam.", "They have been playing ___ two hours.", "for", "for + durasi."),
  ("Dia sudah bekerja di sini sejak 2020.", "He has been working here ___ 2020.", "since", "since + titik awal."),
 ]) + mko([
  ("Aku sudah belajar selama dua jam.", "I have been studying for two hours.", "study studied", ""),
  ("Hujan turun sejak pagi.", "It has been raining since morning.", "rained rain", ""),
  ("Sudah berapa lama kamu bekerja di sini?", "How long have you been working here?", "has work", ""),
 ]),

 quiz=mk([
  ('Rumus present perfect continuous adalah...', "have/has been + V-ing", "have/has + V3", "was/were + V-ing", "had been + V-ing", "have/has been + V-ing."),
  ('Pilih bentuk yang benar: "He ___ playing since noon."', "has been", "have been", "is", "was", "he → has been."),
  ('Pilih bentuk yang benar: "I have been learning English ___ three years."', "for", "since", "from", "ago", "for + durasi."),
  ('Pilih bentuk yang benar: "She has been working here ___ 2019."', "since", "for", "ago", "during", "since + titik awal."),
  ('Pilih bentuk yang benar: "How long ___ they been living here?"', "have", "has", "did", "are", "have they been."),
  ('Pilih kalimat yang SALAH:', "I have been knowing him for years.", "I have known him for years.", "I have been working for years.", "I have waited.", "know tidak continuous."),
  ('Pilih kalimat yang benar:', "I have been cooking all morning.", "I am been cooking all morning.", "I has been cooking all morning.", "I have cooked been all morning.", "have been + V-ing."),
  ('Pilih bentuk yang benar: "I ___ four emails this morning." (jumlah)', "have written", "have been writing", "am writing", "write been", "Jumlah → present perfect."),
 ]) + mkf([
  ("Dia sudah menunggu selama satu jam.", "She has been ___ for an hour. (wait)", "waiting", "been + V-ing."),
  ("Kami sudah belajar sejak pagi.", "We have been ___ since morning. (study)", "studying", "been + V-ing."),
  ("Aku sudah tinggal di sini selama lima tahun.", "I have been ___ here for five years. (live)", "living", "been + V-ing."),
 ]),
)
