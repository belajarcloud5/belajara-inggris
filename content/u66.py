from qk import mk, mkf, mko

UNIT = dict(
 id="u66",
 goals=[
  "membedakan **present perfect** dan **past simple**",
  "memilih tense dari **kata petunjuk waktu**: yesterday, ago, last, in 2020 vs ever, never, already, yet, just",
  "mengenali apakah **waktunya disebut atau tidak**",
  "memakai pertanyaan **When ... ?** dengan past simple",
 ],
 lesson=[
  dict(t="intro", text="Ini pasangan tense yang paling sering membingungkan. Aturan emasnya sederhana: **kalau waktunya jelas disebut (yesterday, last week, in 2020), pakai past simple. Kalau waktunya tidak disebut dan yang penting adalah hubungan dengan sekarang, pakai present perfect.**"),

  dict(t="grammar", title="1. Perbedaan inti",
   table=[["", "Past simple", "Present perfect"],
          ["**Waktu**", "jelas dan selesai", "tidak disebut / sampai sekarang"],
          ["**Rumus**", "V2", "have/has + V3"],
          ["**Contoh**", "[[I visited Bali in 2020.]]", "[[I have visited Bali.]]"],
          ["**Fokus**", "kapan kejadiannya", "hubungan dengan sekarang"]],
   examples=[dict(en="[[I lost my keys yesterday.]] / [[I have lost my keys.]]", id="Kemarin aku menghilangkan kunci. / Kunciku hilang (dan masih belum ketemu).")]),

  dict(t="grammar", title="2. Kata petunjuk",
   table=[["Past simple", "Present perfect"],
          ["yesterday, last week/year, ago", "ever, never, already, yet, just"],
          ["in 2020, on Monday, at six", "for, since, so far, recently"],
          ["When did you ...?", "Have you ever ...?"]]),

  dict(t="grammar", title="3. Pertanyaan: When atau Have you ever?",
   table=[["Pertanyaan", "Tense", "Contoh"],
          ["**Have you ever ...?**", "present perfect (pengalaman)", "[[Have you ever visited Bali?]]"],
          ["**When did you ...?**", "past simple (waktunya)", "[[When did you visit Bali?]] — [[I visited it in 2020.]]"]],
   examples=[dict(en="[[Have you seen this film?]] — [[Yes, I saw it last week.]]", id="Kamu sudah menonton film ini? — Ya, aku menontonnya minggu lalu. (beralih ke past simple saat waktunya disebut)")]),

  dict(t="grammar", title="4. Keadaan yang sudah berakhir atau masih berlanjut",
   table=[["Contoh", "Artinya"],
          ["[[I lived in Bandung for five years.]]", "Dulu tinggal, sekarang sudah tidak."],
          ["[[I have lived in Bandung for five years.]]", "Masih tinggal sampai sekarang."]]),

  dict(t="warn", title="Jangan dengan waktu yang jelas",
   text="Salah: ~~I have visited Bali in 2020~~ dan ~~She has left two days ago~~. Benar: [[I visited Bali in 2020.]] dan [[She left two days ago.]]"),
 ],

 practice=mk([
  ('Pilih bentuk yang benar: "I ___ Bali in 2020."', "visited", "have visited", "visit", "am visiting", "in 2020 → past simple."),
  ('Pilih bentuk yang benar: "I ___ Bali twice."', "have visited", "visited", "visit", "was visiting", "Pengalaman tanpa waktu → present perfect."),
  ('Pilih bentuk yang benar: "She ___ two days ago."', "left", "has left", "leaves", "is leaving", "ago → past simple."),
  ('Pilih bentuk yang benar: "He ___ already left."', "has", "had been", "did", "was", "already → present perfect."),
  ('Pilih bentuk yang benar: "When ___ you see him?"', "did", "have", "do", "are", "When + did."),
  ('Pilih bentuk yang benar: "___ you ever seen a whale?"', "Have", "Did", "Do", "Are", "Have you ever ...?"),
  ('Pilih bentuk yang benar: "I ___ my keys yesterday."', "lost", "have lost", "lose", "am losing", "yesterday → past simple."),
  ('Pilih bentuk yang benar: "I ___ my keys. Can you help me look?" (masih hilang)', "have lost", "lost", "was losing", "lose", "Hasil sekarang."),
  ('Pilih bentuk yang benar: "We ___ here since 2015."', "have lived", "lived", "live", "were living", "since → present perfect."),
  ('Pilih bentuk yang benar: "We ___ in Jakarta for five years, but now we live in Bali."', "lived", "have lived", "live", "are living", "Sudah berakhir → past simple."),
  ('Pilih bentuk yang benar: "She ___ finished yet."', "hasn\'t", "didn\'t", "wasn\'t", "doesn\'t", "yet → present perfect."),
  ('Pilih bentuk yang benar: "Last night I ___ a good movie."', "watched", "have watched", "watch", "am watching", "last night → past simple."),
  ('Pilih bentuk yang benar: "Have you finished? — Yes, I ___ it an hour ago."', "finished", "have finished", "finish", "was finishing", "ago → past simple."),
  ('Pilih kalimat yang SALAH:', "I have seen her yesterday.", "I saw her yesterday.", "I have seen her before.", "I haven't seen her.", "yesterday → past simple."),
  ('Pilih kalimat yang SALAH:', "When have you arrived?", "When did you arrive?", "Have you arrived?", "Did you arrive early?", "When + did."),
  ('Pilih kalimat yang SALAH:', "She has gone to Bali last week.", "She went to Bali last week.", "She has gone to Bali.", "She has never gone to Bali.", "last week → past simple."),
 ]) + mkf([
  ("Aku mengunjungi Bali pada tahun 2020.", "I ___ Bali in 2020. (visit)", "visited", "past simple."),
  ("Aku pernah mengunjungi Bali dua kali.", "I ___ visited Bali twice. (have)", "have", "present perfect."),
  ("Dia pergi dua hari yang lalu.", "She ___ two days ago. (leave)", "left", "ago → past simple."),
  ("Kapan kamu bertemu dia?", "When ___ you meet him?", "did", "When + did."),
  ("Pernahkah kamu melihat paus?", "___ you ever seen a whale?", "Have", "Have you ever?"),
  ("Dia belum selesai.", "She hasn't finished ___.", "yet", "yet."),
 ]) + mko([
  ("Aku melihatnya kemarin.", "I saw her yesterday.", "have seen", ""),
  ("Kapan kamu tiba di sini?", "When did you arrive here?", "have arrive", ""),
  ("Dia sudah tinggal di sini lima tahun.", "She has lived here for five years.", "lived live", ""),
 ]),

 quiz=mk([
  ('Pilih bentuk yang benar: "I ___ him last week."', "met", "have met", "meet", "am meeting", "last week → past simple."),
  ('Pilih bentuk yang benar: "I ___ him before."', "have met", "met", "meet", "was meeting", "before tanpa waktu jelas."),
  ('Pilih bentuk yang benar: "She ___ in 2018."', "graduated", "has graduated", "graduates", "is graduating", "in 2018 → past simple."),
  ('Pilih bentuk yang benar: "They ___ lunch already."', "have had", "had been", "did have", "were having", "already → present perfect."),
  ('Pilih bentuk yang benar: "When ___ the film start?"', "did", "has", "have", "do", "When + did."),
  ('Pilih kalimat yang SALAH:', "I have bought it last month.", "I bought it last month.", "I have bought it.", "I haven't bought it.", "last month → past simple."),
  ('Pilih kalimat yang SALAH:', "Did you ever been to Japan?", "Have you ever been to Japan?", "Did you go to Japan?", "Have you been to Japan?", "Have you ever been."),
  ('Pilih kalimat yang benar:', "I lived in Bandung for five years, but now I live in Bali.", "I have lived in Bandung for five years, but now I live in Bali.", "I live in Bandung for five years but now Bali.", "I living in Bandung for five years.", "Sudah berakhir → past simple."),
 ]) + mkf([
  ("Kemarin aku menghilangkan kunciku.", "I ___ my keys yesterday. (lose)", "lost", "past simple."),
  ("Dia sudah pergi.", "She ___ gone.", "has", "present perfect."),
  ("Kamu pernah ke Jepang?", "___ you ever been to Japan?", "Have", "Have you ever."),
 ]),
)
