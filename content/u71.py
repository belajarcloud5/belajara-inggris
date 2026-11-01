from qk import mk, mkf, mko

UNIT = dict(
 id="u71",
 goals=[
  "memakai **when, while, before, after, as soon as, until** untuk menghubungkan kejadian",
  "memakai **present simple** setelah kata waktu saat membicarakan masa depan",
  "memakai **past simple** dan **past perfect** setelah kata waktu di masa lampau",
  "menyusun urutan kejadian dengan tense yang konsisten",
 ],
 lesson=[
  dict(t="intro", text="**Klausa waktu** (time clause) diawali kata seperti *when, while, before, after, as soon as, until*. Ada satu aturan penting: untuk masa depan, kata kerja setelah kata waktu memakai **present** (bukan will)."),

  dict(t="grammar", title="1. Masa depan: present setelah kata waktu",
   table=[["Salah", "Benar"],
          ["~~When I will arrive, I will call you.~~", "[[When I arrive, I will call you.]]"],
          ["~~I will wait until she will come.~~", "[[I will wait until she comes.]]"],
          ["~~After I will finish, I will rest.~~", "[[After I finish, I will rest.]]"]],
   examples=[dict(en="[[As soon as it stops raining, we will go out.]]", id="Begitu hujan berhenti, kita akan keluar.")]),

  dict(t="grammar", title="2. Masa lampau: urutan kejadian",
   table=[["Urutan", "Contoh"],
          ["berurutan, past simple semua", "[[When I arrived, she left.]] (aku tiba dulu, lalu dia pergi)"],
          ["yang lebih dulu, past perfect", "[[When I arrived, she had left.]] (dia sudah pergi sebelum aku tiba)"],
          ["dua kegiatan bersamaan", "[[While I was cooking, he was reading.]]"],
          ["kegiatan dipotong", "[[While I was cooking, the phone rang.]]"]]),

  dict(t="grammar", title="3. Arti kata penghubung",
   table=[["Kata", "Arti", "Contoh"],
          ["**when**", "ketika", "[[When I get home, I eat.]]"],
          ["**while**", "sementara", "[[While I eat, I watch TV.]]"],
          ["**before**", "sebelum", "[[Before I leave, I lock the door.]]"],
          ["**after**", "setelah", "[[After I eat, I wash the dishes.]]"],
          ["**as soon as**", "begitu", "[[As soon as I arrive, I'll call.]]"],
          ["**until**", "sampai", "[[Wait until I come.]]"]]),

  dict(t="grammar", title="4. Kebiasaan",
   text="Untuk kebiasaan, kedua klausa memakai present simple:",
   table=[["Contoh", "Artinya"],
          ["[[When it rains, I stay home.]]", "Setiap kali hujan, aku di rumah."],
          ["[[Before I sleep, I read a book.]]", "Sebelum tidur, aku selalu membaca."]]),

  dict(t="warn", title="Koma",
   text="Jika klausa waktu di awal kalimat, beri koma: [[When I arrive, I'll call.]] Jika di belakang, tanpa koma: [[I'll call when I arrive.]]"),
 ],

 practice=mk([
  ('Pilih bentuk yang benar: "When I ___ , I will call you."', "arrive", "will arrive", "arrived", "arriving", "Masa depan: present setelah when."),
  ('Pilih bentuk yang benar: "I will wait until she ___ ."', "comes", "will come", "came", "coming", "until + present."),
  ('Pilih bentuk yang benar: "After I ___ , I will rest."', "finish", "will finish", "finished", "finishing", "after + present."),
  ('Pilih bentuk yang benar: "As soon as it ___ raining, we will go out."', "stops", "will stop", "stopped", "stopping", "as soon as + present."),
  ('Pilih bentuk yang benar: "Before I ___ , I will lock the door."', "leave", "will leave", "left", "leaving", "before + present."),
  ('Pilih bentuk yang benar: "When I arrived, she ___ left." (dia pergi lebih dulu)', "had", "has", "have", "was", "Lebih dulu → had + V3."),
  ('Pilih bentuk yang benar: "When I arrived, she ___ ." (dia pergi setelah aku tiba)', "left", "had left", "has left", "leaves", "Berurutan → past simple."),
  ('Pilih bentuk yang benar: "While I ___ , the phone rang."', "was cooking", "cooked", "cook", "cooking", "while + continuous."),
  ('Pilih bentuk yang benar: "While I was cooking, he ___ reading."', "was", "is", "did", "has", "Dua kegiatan bersamaan."),
  ('Pilih bentuk yang benar: "When it rains, I ___ home." (kebiasaan)', "stay", "will stay", "stayed", "am staying", "Kebiasaan → simple."),
  ('Pilih bentuk yang benar: "After she ___ the work, she went home."', "finished", "finishes", "will finish", "finishing", "Masa lampau."),
  ('Pilih bentuk yang benar: "I\'ll call you when I ___ home."', "get", "will get", "got", "getting", "when + present."),
  ('Pilih kalimat yang benar:', "As soon as she arrives, I will tell her.", "As soon as she will arrive, I will tell her.", "As soon as she arrived, I will tell her.", "As soon as she arriving, I will tell her.", "present setelah as soon as."),
  ('Pilih kalimat yang SALAH:', "When I will arrive, I will call.", "When I arrive, I will call.", "I will call when I arrive.", "I will call as soon as I arrive.", "Jangan will setelah when."),
  ('Pilih kalimat yang SALAH:', "I will wait until he will come.", "I will wait until he comes.", "I waited until he came.", "I always wait until he comes.", "until + present."),
  ('Pilih kalimat yang SALAH:', "When I got home, I eat dinner.", "When I got home, I ate dinner.", "When I get home, I eat dinner.", "When I get home, I will eat dinner.", "Konsisten tense."),
 ]) + mkf([
  ("Ketika aku tiba, aku akan menelepon.", "When I ___, I will call. (arrive)", "arrive", "present setelah when."),
  ("Tunggulah sampai dia datang.", "Wait until she ___. (come)", "comes", "until + present."),
  ("Setelah aku makan, aku akan beristirahat.", "After I ___, I will rest. (eat)", "eat", "after + present."),
  ("Begitu hujan berhenti, kita pergi.", "As soon as it ___ raining, we will go. (stop)", "stops", "as soon as + present."),
  ("Ketika aku tiba, dia sudah pergi.", "When I arrived, she ___ left. (have)", "had", "had + V3."),
  ("Sementara aku memasak, telepon berdering.", "While I ___ cooking, the phone rang. (be)", "was", "was + V-ing."),
 ]) + mko([
  ("Begitu aku tiba, aku akan menelepon.", "As soon as I arrive, I will call.", "arrived will", ""),
  ("Ketika hujan, aku tinggal di rumah.", "When it rains, I stay home.", "rained rain", ""),
  ("Setelah dia pergi, aku makan.", "After she left, I ate.", "leave eat", ""),
 ]),

 quiz=mk([
  ('Pilih bentuk yang benar: "I\'ll tell her when she ___ ."', "arrives", "will arrive", "arrived", "arriving", "when + present."),
  ('Pilih bentuk yang benar: "Before we ___ , we will pack."', "leave", "will leave", "left", "leaving", "before + present."),
  ('Pilih bentuk yang benar: "When I called, she ___ left." (sudah pergi)', "had", "has", "have", "was", "had + V3."),
  ('Pilih bentuk yang benar: "While we ___ , it began to snow."', "were driving", "drove", "drive", "driving", "while + continuous."),
  ('Pilih bentuk yang benar: "Wait here until I ___ back."', "come", "will come", "came", "coming", "until + present."),
  ('Pilih kalimat yang SALAH:', "After I will eat, I wash.", "After I eat, I wash.", "After I ate, I washed.", "After I eat, I will wash.", "Jangan will setelah after."),
  ('Pilih kalimat yang benar:', "I will call you as soon as I get home.", "I will call you as soon as I will get home.", "I call you as soon as I will get home.", "I will call you as soon as I getting home.", "present setelah as soon as."),
  ('Pilih bentuk yang benar: "When I\'m tired, I ___ early." (kebiasaan)', "sleep", "will sleep", "slept", "am sleeping", "Kebiasaan → simple."),
 ]) + mkf([
  ("Begitu dia tiba, kami akan mulai.", "As soon as she ___, we will start. (arrive)", "arrives", "present."),
  ("Setelah aku selesai, aku pulang.", "After I ___, I go home. (finish)", "finish", "present."),
  ("Sebelum tidur, aku membaca.", "Before I ___, I read. (sleep)", "sleep", "present."),
 ]),
)
