from qk import mk, mkf, mko

UNIT = dict(
 id="u64",
 goals=[
  "memakai **past simple** untuk kejadian yang sudah selesai di masa lampau",
  "memakai **past continuous** untuk kejadian yang sedang berlangsung pada satu saat di masa lampau",
  "memakai **when** dan **while** untuk menggabungkan dua kejadian",
  "membedakan kejadian latar (background) dan kejadian pendek yang memotong",
 ],
 lesson=[
  dict(t="intro", text="Saat bercerita tentang masa lalu, kita memakai dua tense utama. **Past simple** untuk kejadian yang selesai (*I called her.*). **Past continuous** untuk kejadian yang **sedang berlangsung** pada satu saat (*I was cooking when she called.*)."),

  dict(t="grammar", title="1. Past simple",
   table=[["Pola", "Rumus", "Contoh"],
          ["Positif", "V2 (beraturan: -ed; tidak beraturan: berubah)", "[[I visited Bali.]] / [[I went to Bali.]]"],
          ["Negatif", "did not + V1", "[[I didn't visit Bali.]]"],
          ["Tanya", "Did + subjek + V1?", "[[Did you visit Bali?]]"]],
   examples=[dict(en="[[She arrived at six and ate dinner.]]", id="Dia tiba pukul enam dan makan malam. (urutan kejadian selesai)")]),

  dict(t="grammar", title="2. Past continuous",
   table=[["Pola", "Rumus", "Contoh"],
          ["Positif", "was/were + V-ing", "[[I was cooking.]] / [[They were playing.]]"],
          ["Negatif", "was/were + not + V-ing", "[[I wasn't sleeping.]]"],
          ["Tanya", "Was/Were + subjek + V-ing?", "[[Were you sleeping?]]"]],
   examples=[dict(en="[[At eight last night, I was watching TV.]]", id="Pukul delapan tadi malam, aku sedang menonton TV.")]),

  dict(t="grammar", title="3. when dan while",
   table=[["Kata", "Dipakai dengan", "Contoh"],
          ["**while**", "past continuous (kegiatan panjang)", "[[While I was cooking, the phone rang.]]"],
          ["**when**", "past simple (kejadian pendek)", "[[I was cooking when the phone rang.]]"],
          ["**while ... while**", "dua kegiatan bersamaan", "[[While I was cooking, he was reading.]]"]],
   examples=[dict(en="[[I was walking home when it started to rain.]]", id="Aku sedang berjalan pulang ketika hujan mulai turun. (berjalan = latar; hujan = memotong)")]),

  dict(t="tip", title="Kejadian latar dan kejadian memotong",
   text="Bayangkan film. **Past continuous** adalah latar belakang yang berjalan (*was walking*). **Past simple** adalah kejadian pendek yang memotong (*started to rain*). Tanya: mana yang panjang dan mana yang pendek?"),
  dict(t="warn", title="Kata kerja keadaan tetap past simple",
   text="Katakan [[I knew the answer.]], bukan ~~I was knowing the answer~~. Dan untuk urutan kejadian selesai, pakai past simple semua: [[She came in, sat down, and opened her book.]]"),
 ],

 practice=mk([
  ('Pilih bentuk yang benar: "I ___ Bali last year."', "visited", "was visiting", "visit", "have visit", "last year → past simple."),
  ('Pilih bentuk yang benar: "At eight last night, I ___ TV."', "was watching", "watched", "watch", "am watching", "Pada satu saat lampau → continuous."),
  ('Pilih bentuk yang benar: "She ___ dinner and then went to bed."', "ate", "was eating", "eats", "eating", "Urutan selesai → past simple."),
  ('Pilih bentuk yang benar: "While I ___ , the phone rang."', "was cooking", "cooked", "cook", "am cooking", "while + continuous."),
  ('Pilih bentuk yang benar: "I was cooking when the phone ___."', "rang", "was ringing", "rings", "ring", "Kejadian pendek → past simple."),
  ('Pilih bentuk yang benar: "They ___ football when it started to rain."', "were playing", "played", "play", "are playing", "Latar → continuous."),
  ('Pilih bentuk yang benar: "He ___ the door and walked in."', "opened", "was opening", "opens", "open", "Urutan selesai → past simple."),
  ('Pilih bentuk yang benar: "What ___ you doing at nine?"', "were", "did", "are", "was", "were + V-ing."),
  ('Pilih bentuk yang benar: "___ you see the match yesterday?"', "Did", "Were", "Do", "Was", "Tanya past simple → Did."),
  ('Pilih bentuk yang benar: "I ___ know the answer yesterday."', "didn't", "wasn't", "don't", "haven't", "didn't + V1."),
  ('Pilih bentuk yang benar: "I ___ the answer." (tahu, kemarin)', "knew", "was knowing", "know", "am knowing", "know = stative."),
  ('Pilih bentuk yang benar: "While she ___ , he was reading."', "was cooking", "cooked", "cooks", "cook", "Dua kegiatan bersamaan."),
  ('Pilih kalimat yang benar:', "I was walking home when it started to rain.", "I walked home when it was starting to rain.", "I was walk home when it started to rain.", "I walking home when it started to rain.", "Latar continuous, memotong simple."),
  ('Pilih kalimat yang SALAH:', "I was knowing the answer.", "I knew the answer.", "I was thinking about it.", "I didn't know.", "know tidak continuous."),
  ('Pilih kalimat yang SALAH:', "She was came in and sat down.", "She came in and sat down.", "She was sitting down when I came.", "She didn't sit.", "came, bukan was came."),
  ('Pilih kalimat yang SALAH:', "Did you went to school?", "Did you go to school?", "Did you walk?", "Were you walking?", "Did + V1."),
 ]) + mkf([
  ("Aku mengunjungi Bali tahun lalu.", "I ___ Bali last year. (visit)", "visited", "past simple."),
  ("Aku sedang memasak ketika telepon berdering.", "I ___ cooking when the phone rang. (be)", "was", "was + V-ing."),
  ("Mereka sedang bermain bola ketika hujan turun.", "They ___ playing football when it rained. (be)", "were", "were + V-ing."),
  ("Apakah kamu pergi ke sekolah kemarin?", "___ you go to school yesterday?", "Did", "Did + subjek + V1."),
  ("Aku tidak melihat dia.", "I ___ see him.", "didn't/did not", "did not + V1."),
  ("Ketika aku tiba, dia sedang tidur.", "When I arrived, she ___ sleeping. (be)", "was", "was + V-ing."),
 ]) + mko([
  ("Aku sedang membaca ketika dia masuk.", "I was reading when she came in.", "read reading", ""),
  ("Kami makan malam lalu menonton TV.", "We ate dinner and then watched TV.", "were eating", ""),
  ("Pukul delapan tadi malam aku sedang tidur.", "At eight last night I was sleeping.", "slept sleep", ""),
 ]),

 quiz=mk([
  ('Pilih bentuk yang benar: "I ___ my keys yesterday."', "lost", "was losing", "lose", "have lose", "Kejadian selesai."),
  ('Pilih bentuk yang benar: "It ___ when I left home."', "was raining", "rained", "rains", "rain", "Latar saat pergi."),
  ('Pilih bentuk yang benar: "She was crying when I ___ in."', "came", "was coming", "come", "coming", "Kejadian pendek."),
  ('Pilih bentuk yang benar: "While we ___ , it began to snow."', "were driving", "drove", "drive", "driving", "while + continuous."),
  ('Pilih bentuk yang benar: "Where ___ you yesterday evening?"', "were", "did", "do", "are", "were + subjek."),
  ('Pilih kalimat yang SALAH:', "I was seeing him yesterday.", "I saw him yesterday.", "I was walking when I saw him.", "I didn't see him.", "see = tindakan selesai, past simple."),
  ('Pilih kalimat yang SALAH:', "He didn't came.", "He didn't come.", "He wasn't coming.", "He came late.", "didn't + V1."),
  ('Pilih kalimat yang benar:', "While I was studying, she was cooking.", "While I studied, she was cook.", "While I was studying, she cooked.", "While I study, she was cooking.", "Dua kegiatan bersamaan."),
 ]) + mkf([
  ("Dia sedang tidur pukul sepuluh.", "She ___ sleeping at ten. (be)", "was", "was + V-ing."),
  ("Kami pergi ke pantai kemarin.", "We ___ to the beach yesterday. (go)", "went", "V2 dari go."),
  ("Kamu sedang apa ketika aku menelepon?", "What ___ you doing when I called?", "were", "were + V-ing."),
 ]),
)
