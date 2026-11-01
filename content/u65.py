from qk import mk, mkf, mko

UNIT = dict(
 id="u65",
 goals=[
  "membentuk **present perfect** dengan have/has + V3",
  "memakainya untuk **pengalaman**, **hasil sekarang**, dan **kegiatan yang berlanjut**",
  "memakai **for, since, already, yet, just, ever, never** dengan benar",
  "menghafal bentuk **V3** kata kerja yang sering dipakai",
 ],
 lesson=[
  dict(t="intro", text="**Present perfect** menghubungkan masa lalu dengan sekarang. Kita tidak peduli **kapan persisnya** sesuatu terjadi, tetapi **hubungannya dengan saat ini**: pengalaman, hasil yang masih terasa, atau keadaan yang berlanjut."),

  dict(t="grammar", title="1. Rumus",
   table=[["Pola", "Rumus", "Contoh"],
          ["Positif", "have/has + V3", "[[I have finished.]] / [[She has finished.]]"],
          ["Negatif", "have/has + not + V3", "[[I haven't finished.]] / [[She hasn't finished.]]"],
          ["Tanya", "Have/Has + subjek + V3?", "[[Have you finished?]] / [[Has she finished?]]"]]),

  dict(t="grammar", title="2. Tiga pemakaian utama",
   table=[["Pemakaian", "Contoh", "Artinya"],
          ["**Pengalaman**", "[[I have visited Bali twice.]]", "Pernah (kapan tidak penting)"],
          ["**Hasil sekarang**", "[[I have lost my keys.]]", "Kuncinya hilang (dan masih hilang)"],
          ["**Berlanjut**", "[[I have lived here for five years.]]", "Masih tinggal sampai sekarang"]]),

  dict(t="grammar", title="3. for dan since",
   table=[["Kata", "Diikuti", "Contoh"],
          ["**for**", "lama waktu (durasi)", "[[for two hours]] / [[for five years]]"],
          ["**since**", "titik awal waktu", "[[since 2015]] / [[since Monday]]"]],
   examples=[dict(en="[[I have known her for ten years.]] / [[I have known her since 2015.]]", id="Aku sudah mengenalnya selama sepuluh tahun. / sejak 2015.")]),

  dict(t="grammar", title="4. already, yet, just, ever, never",
   table=[["Kata", "Posisi", "Contoh"],
          ["**already**", "di tengah (kalimat positif)", "[[I have already eaten.]]"],
          ["**yet**", "di akhir (negatif dan tanya)", "[[I haven't eaten yet.]] / [[Have you eaten yet?]]"],
          ["**just**", "di tengah, baru saja", "[[I have just arrived.]]"],
          ["**ever**", "di tanya, pernah", "[[Have you ever been to Japan?]]"],
          ["**never**", "di tengah, tidak pernah", "[[I have never been to Japan.]]"]]),

  dict(t="grammar", title="5. Bentuk V3 yang sering dipakai",
   table=[["V1", "V2", "V3"],
          ["go", "went", "**gone**"], ["see", "saw", "**seen**"], ["eat", "ate", "**eaten**"],
          ["write", "wrote", "**written**"], ["take", "took", "**taken**"], ["do", "did", "**done**"],
          ["be", "was/were", "**been**"], ["have", "had", "**had**"], ["finish", "finished", "**finished**"]]),

  dict(t="warn", title="Jangan dengan waktu yang jelas",
   text="Present perfect tidak dipakai dengan waktu yang jelas: bukan ~~I have seen her yesterday~~, tetapi [[I saw her yesterday.]] Ini dibahas lebih dalam di unit 66."),
 ],

 practice=mk([
  ('Pilih bentuk yang benar: "I ___ finished my homework."', "have", "has", "had been", "am", "I + have."),
  ('Pilih bentuk yang benar: "She ___ lost her keys."', "has", "have", "is", "was been", "she + has."),
  ('Pilih bentuk yang benar: "They have ___ to Bali twice."', "been", "be", "being", "was", "have been to."),
  ('Pilih bentuk yang benar: "I have ___ this movie."', "seen", "saw", "see", "seeing", "V3 dari see."),
  ('Pilih bentuk yang benar: "He has ___ breakfast already."', "eaten", "ate", "eat", "eating", "V3 dari eat."),
  ('Pilih bentuk yang benar: "We have lived here ___ ten years."', "for", "since", "from", "during", "for + durasi."),
  ('Pilih bentuk yang benar: "We have lived here ___ 2015."', "since", "for", "from", "ago", "since + titik awal."),
  ('Pilih bentuk yang benar: "I haven\'t finished ___."', "yet", "already", "just", "ever", "yet di akhir negatif."),
  ('Pilih bentuk yang benar: "She has ___ arrived."', "just", "yet", "since", "for", "just = baru saja."),
  ('Pilih bentuk yang benar: "Have you ___ been to Japan?"', "ever", "never", "already", "yet", "ever dalam tanya."),
  ('Pilih bentuk yang benar: "I have ___ been to Japan."', "never", "ever", "yet", "since", "never = belum pernah."),
  ('Pilih bentuk yang benar: "___ she finished her work?"', "Has", "Have", "Did", "Is", "Has + she."),
  ('Pilih bentuk yang benar: "He ___ written three books."', "has", "have", "had been", "is", "he + has."),
  ('Pilih kalimat yang benar:', "I have already eaten.", "I already have ate.", "I have eaten already yesterday.", "I am already eaten.", "have + already + V3."),
  ('Pilih kalimat yang SALAH:', "She has went home.", "She has gone home.", "She went home.", "She hasn't gone home.", "V3 dari go adalah gone."),
  ('Pilih kalimat yang SALAH:', "I have seen her yesterday.", "I saw her yesterday.", "I have seen her.", "I have never seen her.", "yesterday → past simple."),
  ('Pilih kalimat yang SALAH:', "He have finished.", "He has finished.", "They have finished.", "I have finished.", "he → has."),
 ]) + mkf([
  ("Aku sudah menyelesaikan PR-ku.", "I ___ finished my homework. (have)", "have", "have + V3."),
  ("Dia sudah pergi ke Bali dua kali.", "She has ___ to Bali twice. (be)", "been", "V3 dari be."),
  ("Kami tinggal di sini sejak 2015.", "We have lived here ___ 2015.", "since", "since + titik awal."),
  ("Kami tinggal di sini selama lima tahun.", "We have lived here ___ five years.", "for", "for + durasi."),
  ("Aku belum makan.", "I haven't eaten ___.", "yet", "yet di akhir."),
  ("Dia baru saja tiba.", "She has ___ arrived.", "just", "just."),
 ]) + mko([
  ("Aku sudah mengerjakan PR-ku.", "I have done my homework.", "did does", ""),
  ("Dia belum pernah ke Jepang.", "She has never been to Japan.", "ever yet", ""),
  ("Pernahkah kamu makan sushi?", "Have you ever eaten sushi?", "ate eat", ""),
 ]),

 quiz=mk([
  ('Rumus present perfect adalah...', "have/has + V3", "was/were + V-ing", "had + V3", "will + V1", "have/has + V3."),
  ('"I have visited Bali twice." menekankan...', "pengalaman", "kebiasaan", "rencana", "kejadian kemarin", "pengalaman."),
  ('Pilih bentuk yang benar: "He ___ never eaten durian."', "has", "have", "is", "was", "he → has."),
  ('Pilih bentuk yang benar: "We have known her ___ 2010."', "since", "for", "ago", "during", "since + titik awal."),
  ('Pilih bentuk yang benar: "I have waited ___ two hours."', "for", "since", "from", "ago", "for + durasi."),
  ('Pilih bentuk yang benar: "Has the bus arrived ___?"', "yet", "already", "just", "since", "yet di tanya."),
  ('Pilih kalimat yang SALAH:', "I have ate lunch.", "I have eaten lunch.", "I ate lunch.", "I haven't eaten lunch.", "V3: eaten."),
  ('Pilih kalimat yang benar:', "Have you ever tried sushi?", "Did you ever tried sushi?", "Have you ever try sushi?", "Do you ever tried sushi?", "Have + ever + V3."),
 ]) + mkf([
  ("Dia sudah menulis surat itu.", "She has ___ the letter. (write)", "written", "V3 dari write."),
  ("Aku belum pernah ke sana.", "I have ___ been there.", "never", "never."),
  ("Mereka sudah pergi.", "They have ___. (go)", "gone", "V3 dari go."),
 ]),
)
