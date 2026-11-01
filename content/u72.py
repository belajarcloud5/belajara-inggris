from qk import mk, mkf, mko

UNIT = dict(
 id="u72",
 goals=[
  "memilih tense yang tepat dari **empat present tense**: simple, continuous, perfect, perfect continuous",
  "mengenali **kata petunjuk** yang membedakan keempat tense",
  "menentukan tense dari **konteks** dan **maksud** pembicara",
  "mengecek diri dengan **latihan campuran** present",
 ],
 lesson=[
  dict(t="intro", text="Unit ini adalah **latihan kontras**. Kamu sudah mempelajari keempat present tense. Sekarang kamu menguji kemampuan memilih. Gunakan **peta pertanyaan** di bawah setiap kali ragu."),

  dict(t="grammar", title="1. Peta keputusan empat present tense",
   table=[["Ciri kalimat", "Tense", "Contoh"],
          ["kebiasaan, fakta, jadwal", "present simple", "[[I work in a bank.]]"],
          ["sedang terjadi sekarang", "present continuous", "[[I am working now.]]"],
          ["pengalaman, hasil, belum/sudah, tanpa waktu jelas", "present perfect", "[[I have worked here.]]"],
          ["kegiatan sampai sekarang + lama", "present perfect continuous", "[[I have been working for two hours.]]"]]),

  dict(t="grammar", title="2. Kata petunjuk",
   table=[["Tense", "Petunjuk"],
          ["present simple", "always, usually, every day, on Mondays"],
          ["present continuous", "now, at the moment, Look!, these days"],
          ["present perfect", "already, yet, just, ever, never, so far"],
          ["present perfect continuous", "for + durasi, since + titik awal, all day, lately"]]),

  dict(t="grammar", title="3. Pasangan yang sering tertukar",
   table=[["Pasangan", "Contoh"],
          ["simple vs continuous", "[[I live in Jakarta.]] (tetap) vs [[I am living in Jakarta this year.]] (sementara)"],
          ["simple vs perfect", "[[I know her.]] (sekarang) vs [[I have known her for years.]] (sejak lama)"],
          ["perfect vs perfect continuous", "[[I have read the book.]] (selesai) vs [[I have been reading the book.]] (kegiatan)"]]),

  dict(t="tip", title="Cek dua kali",
   text="Setelah memilih tense, cek: (1) apakah ada **kata petunjuk**? (2) apakah kata kerjanya **kata kerja keadaan** (know, like, want)? Kata kerja keadaan tidak dipakai dalam continuous."),
 ],

 practice=mk([
  ('Pilih bentuk yang benar: "I ___ in a bank." (pekerjaan tetap)', "work", "am working", "have worked", "have been working", "Fakta tetap → simple."),
  ('Pilih bentuk yang benar: "Be quiet! The baby ___ ."', "is sleeping", "sleeps", "has slept", "has been sleep", "Sekarang → continuous."),
  ('Pilih bentuk yang benar: "I ___ here for five years."', "have worked", "work", "am working", "works", "for + durasi → perfect."),
  ('Pilih bentuk yang benar: "She ___ for three hours and she is still tired."', "has been studying", "studies", "is study", "studied", "Durasi + masih → perfect continuous."),
  ('Pilih bentuk yang benar: "I ___ my homework. Now I can play."', "have finished", "finish", "am finishing", "was finishing", "Hasil sekarang → perfect."),
  ('Pilih bentuk yang benar: "He ___ the answer." (tahu)', "knows", "is knowing", "has been knowing", "know", "stative → simple."),
  ('Pilih bentuk yang benar: "They ___ football every Sunday."', "play", "are playing", "have played", "has played", "every Sunday → simple."),
  ('Pilih bentuk yang benar: "Look! They ___ football."', "are playing", "play", "have played", "has played", "Look! → continuous."),
  ('Pilih bentuk yang benar: "I ___ never ___ sushi."', "have / eaten", "am / eating", "was / eat", "did / ate", "never → perfect."),
  ('Pilih bentuk yang benar: "It ___ since morning."', "has been raining", "rains", "is rain", "rained", "since morning → perfect continuous."),
  ('Pilih bentuk yang benar: "She ___ here since 2015."', "has lived", "lives", "is living", "live", "since → perfect."),
  ('Pilih bentuk yang benar: "How long ___ you been waiting?"', "have", "are", "do", "did", "have you been."),
  ('Pilih bentuk yang benar: "I ___ three emails this morning." (jumlah)', "have written", "have been writing", "am writing", "write", "Jumlah → perfect."),
  ('Pilih bentuk yang benar: "She is tired because she ___ all day." (kegiatan)', "has been working", "works", "is work", "worked", "Kegiatan + hasil."),
  ('Pilih kalimat yang SALAH:', "I am knowing her.", "I know her.", "I have known her.", "I have been working.", "know tidak continuous."),
  ('Pilih kalimat yang SALAH:', "She has worked here since five years.", "She has worked here for five years.", "She has worked here since 2020.", "She works here.", "for + durasi."),
 ]) + mkf([
  ("Aku bekerja di bank.", "I ___ in a bank. (work)", "work", "simple."),
  ("Lihat! Dia sedang menari.", "Look! She ___ dancing. (be)", "is", "continuous."),
  ("Aku sudah selesai.", "I ___ finished. (have)", "have", "perfect."),
  ("Dia sudah menunggu selama dua jam.", "She has been ___ for two hours. (wait)", "waiting", "perfect continuous."),
  ("Mereka tinggal di sini sejak 2018.", "They have lived here ___ 2018.", "since", "since."),
  ("Aku tahu jawabannya.", "I ___ the answer. (know)", "know", "stative."),
 ]) + mko([
  ("Aku sudah menunggu selama satu jam.", "I have been waiting for an hour.", "wait waited", ""),
  ("Dia bekerja di rumah sakit.", "She works in a hospital.", "working work", ""),
  ("Kami sudah menyelesaikan proyek itu.", "We have finished the project.", "finish finishes", ""),
 ]),

 quiz=mk([
  ('Pilih bentuk yang benar: "Water ___ at 100 degrees."', "boils", "is boiling", "has boiled", "boiled", "Fakta."),
  ('Pilih bentuk yang benar: "I ___ for the bus right now."', "am waiting", "wait", "have waited", "waited", "right now."),
  ('Pilih bentuk yang benar: "He ___ in Paris since 2020."', "has lived", "lives", "lived", "is living", "since."),
  ('Pilih bentuk yang benar: "We ___ English for two years."', "have been learning", "learn", "learned", "are learn", "for + durasi."),
  ('Pilih bentuk yang benar: "She ___ her keys. She can\'t get in."', "has lost", "loses", "is losing", "was losing", "Hasil sekarang."),
  ('Pilih kalimat yang SALAH:', "She is liking music.", "She likes music.", "She has liked music.", "She is listening now.", "like = stative."),
  ('Pilih kalimat yang SALAH:', "I have seen him yesterday.", "I saw him yesterday.", "I have seen him.", "I have never seen him.", "yesterday → past simple."),
  ('Pilih kalimat yang benar:', "I have been studying since noon.", "I am studying since noon.", "I study since noon.", "I has been studying since noon.", "since + perfect continuous."),
 ]) + mkf([
  ("Dia tinggal di Bali sekarang.", "She ___ in Bali now. (live)", "lives", "simple."),
  ("Hujan sedang turun.", "It ___ raining. (be)", "is", "continuous."),
  ("Mereka sudah makan.", "They ___ eaten. (have)", "have", "perfect."),
 ]),
)
