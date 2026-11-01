from qk import mk, mkf, mko

UNIT = dict(
 id="u70",
 goals=[
  "membentuk **future continuous** dengan will be + V-ing",
  "membentuk **future perfect** dengan will have + V3",
  "memakai **by + waktu** dan **by the time** untuk future perfect",
  "membedakan future simple, continuous, dan perfect",
 ],
 lesson=[
  dict(t="intro", text="Dua tense masa depan yang lebih lanjut: **future continuous** (akan sedang berlangsung pada satu saat) dan **future perfect** (akan sudah selesai sebelum satu saat). Keduanya sangat berguna di kantor dan dalam rencana."),

  dict(t="grammar", title="1. Future continuous: will be + V-ing",
   table=[["Pola", "Rumus", "Contoh"],
          ["Positif", "will be + V-ing", "[[At nine tomorrow, I will be working.]]"],
          ["Negatif", "will not (won't) be + V-ing", "[[I won't be sleeping.]]"],
          ["Tanya", "Will + subjek + be + V-ing?", "[[Will you be working at nine?]]"]],
   examples=[dict(en="[[This time next week, I'll be lying on a beach.]]", id="Seminggu lagi pada jam ini, aku sedang berbaring di pantai."),
             dict(en="[[Don't call at seven. I'll be having dinner.]]", id="Jangan menelepon pukul tujuh. Aku sedang makan malam.")]),

  dict(t="grammar", title="2. Future perfect: will have + V3",
   table=[["Pola", "Rumus", "Contoh"],
          ["Positif", "will have + V3", "[[By Friday, I will have finished.]]"],
          ["Negatif", "will not (won't) have + V3", "[[I won't have finished.]]"],
          ["Tanya", "Will + subjek + have + V3?", "[[Will you have finished by Friday?]]"]],
   examples=[dict(en="[[By 2030, she will have graduated.]]", id="Pada tahun 2030, dia sudah lulus."),
             dict(en="[[By the time you arrive, I will have cooked dinner.]]", id="Pada saat kamu tiba, aku sudah memasak makan malam.")]),

  dict(t="grammar", title="3. Perbandingan tiga bentuk",
   table=[["Tense", "Artinya", "Contoh"],
          ["Future simple", "akan terjadi", "[[I will finish the report.]]"],
          ["Future continuous", "sedang berlangsung pada saat itu", "[[At five, I will be finishing the report.]]"],
          ["Future perfect", "sudah selesai sebelum saat itu", "[[By five, I will have finished the report.]]"]]),

  dict(t="grammar", title="4. Kata petunjuk",
   table=[["Tense", "Kata petunjuk", "Contoh"],
          ["Future continuous", "at + jam, this time tomorrow, all day", "[[This time tomorrow, I will be flying.]]"],
          ["Future perfect", "by + waktu, by the time, before", "[[By next year, I will have saved enough.]]"]]),

  dict(t="warn", title="by dan until",
   text="Gunakan **by** untuk batas waktu penyelesaian: [[I will have finished by five.]] Gunakan **until** untuk kegiatan yang berlanjut sampai batas: [[I will be working until five.]]"),
 ],

 practice=mk([
  ('Pilih bentuk yang benar: "At nine tomorrow, I ___ working."', "will be", "will have", "am", "would", "Pada satu saat → will be + V-ing."),
  ('Pilih bentuk yang benar: "By Friday, I ___ finished the report."', "will have", "will be", "would", "am", "By + waktu → will have + V3."),
  ('Pilih bentuk yang benar: "This time next week, I ___ lying on a beach."', "will be", "will have", "am", "have been", "will be + V-ing."),
  ('Pilih bentuk yang benar: "By 2030, she ___ graduated."', "will have", "will be", "has", "is", "will have + V3."),
  ('Pilih bentuk yang benar: "Don\'t call at seven. I ___ dinner."', "will be having", "will have", "have", "had", "Sedang berlangsung."),
  ('Pilih bentuk yang benar: "By the time you arrive, I ___ cooked."', "will have", "will be", "am", "was", "By the time → will have."),
  ('Pilih bentuk yang benar: "___ you be working at nine?"', "Will", "Do", "Are", "Did", "Will + you + be."),
  ('Pilih bentuk yang benar: "___ you have finished by Friday?"', "Will", "Do", "Did", "Are", "Will + you + have."),
  ('Pilih bentuk yang benar: "I ___ be sleeping at midnight."', "will", "have", "am", "was", "will be + V-ing."),
  ('Pilih bentuk yang benar: "I will have ___ by five." (finish)', "finished", "finish", "finishing", "finishes", "will have + V3."),
  ('Pilih bentuk yang benar: "I will be ___ at nine." (work)', "working", "worked", "work", "works", "will be + V-ing."),
  ('Pilih bentuk yang benar: "I ___ working until five."', "will be", "will have", "had been", "did", "until → berlangsung."),
  ('Pilih bentuk yang benar: "She ___ finished by five."', "will have", "will be", "has been", "is", "by five → will have + V3."),
  ('Pilih kalimat yang benar:', "By next year, I will have saved enough money.", "By next year, I will be saved enough money.", "By next year, I will save enough money already.", "By next year, I have saved will enough money.", "will have + V3."),
  ('Pilih kalimat yang SALAH:', "I will be finished by five.", "I will have finished by five.", "I will be finishing at five.", "I will finish at five.", "by five → will have + V3."),
  ('Pilih kalimat yang SALAH:', "At nine, I will have work.", "At nine, I will be working.", "By nine, I will have worked.", "At nine, I will work.", "will be + V-ing."),
 ]) + mkf([
  ("Besok pukul sembilan aku akan sedang bekerja.", "At nine tomorrow, I will ___ working. (be)", "be", "will be + V-ing."),
  ("Pada hari Jumat, aku sudah menyelesaikan laporan.", "By Friday, I will ___ finished the report. (have)", "have", "will have + V3."),
  ("Dia akan sudah lulus pada tahun 2030.", "By 2030, she will have ___. (graduate)", "graduated", "will have + V3."),
  ("Seminggu lagi aku sedang di pantai.", "This time next week, I will be ___ on a beach. (lie)", "lying", "will be + V-ing."),
  ("Apakah kamu akan sedang bekerja pukul sembilan?", "___ you be working at nine?", "Will", "Will you be?"),
  ("Aku akan bekerja sampai pukul lima.", "I will be working ___ five.", "until", "until."),
 ]) + mko([
  ("Pada hari Jumat aku sudah menyelesaikan laporan.", "By Friday I will have finished the report.", "will be finished", ""),
  ("Besok pukul sembilan aku sedang bekerja.", "At nine tomorrow I will be working.", "will have work", ""),
  ("Kapan kamu akan sudah selesai?", "When will you have finished?", "will be finish", ""),
 ]),

 quiz=mk([
  ('Rumus future continuous adalah...', "will be + V-ing", "will have + V3", "was + V-ing", "have been + V-ing", "will be + V-ing."),
  ('Rumus future perfect adalah...', "will have + V3", "will be + V-ing", "had + V3", "have + V3", "will have + V3."),
  ('Pilih bentuk yang benar: "By tomorrow noon, they ___ arrived."', "will have", "will be", "have been", "are", "by + waktu."),
  ('Pilih bentuk yang benar: "This time tomorrow, we ___ flying to Bali."', "will be", "will have", "are", "had", "this time tomorrow → continuous."),
  ('Pilih bentuk yang benar: "I will be ___ at five."', "working", "worked", "work", "works", "will be + V-ing."),
  ('Pilih kalimat yang SALAH:', "She will be graduated by 2030.", "She will have graduated by 2030.", "She will graduate in 2030.", "She will be studying in 2029.", "will have + V3."),
  ('Pilih kalimat yang benar:', "By the time I arrive, you will have left.", "By the time I will arrive, you will have left.", "By the time I arrive, you will be left.", "By the time I arrive, you have will left.", "by the time + present."),
  ('Pilih bentuk yang benar: "___ she have finished by noon?"', "Will", "Does", "Is", "Did", "Will + she + have."),
 ]) + mkf([
  ("Aku akan sedang tidur pukul dua belas.", "I will be ___ at midnight. (sleep)", "sleeping", "will be + V-ing."),
  ("Pada pukul lima aku sudah selesai.", "By five, I will have ___. (finish)", "finished", "will have + V3."),
  ("Mereka akan sudah tiba.", "They will ___ arrived.", "have", "will have + V3."),
 ]),
)
