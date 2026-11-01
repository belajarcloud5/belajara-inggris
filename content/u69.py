from qk import mk, mkf, mko

UNIT = dict(
 id="u69",
 goals=[
  "membedakan **will** dan **be going to** untuk masa depan",
  "memakai **present continuous** untuk rencana yang sudah diatur",
  "memakai **present simple** untuk jadwal tetap",
  "memilih bentuk masa depan yang tepat: keputusan, rencana, prediksi, atau jadwal",
 ],
 lesson=[
  dict(t="intro", text="Bahasa Inggris tidak punya satu bentuk tunggal untuk masa depan. Ada beberapa pilihan, dan **pilihannya tergantung maksud pembicara**: baru memutuskan, sudah merencanakan, memprediksi, atau menyebut jadwal."),

  dict(t="grammar", title="1. Ringkasan empat bentuk",
   table=[["Bentuk", "Dipakai untuk", "Contoh"],
          ["**will + V1**", "keputusan saat bicara, janji, prediksi", "[[It's cold. I'll close the window.]]"],
          ["**be going to + V1**", "rencana yang sudah dipikirkan, prediksi dengan bukti", "[[I'm going to study tonight.]] / [[Look at the clouds! It's going to rain.]]"],
          ["**present continuous**", "rencana yang sudah diatur (ada waktu dan orang)", "[[I'm meeting Rani at six.]]"],
          ["**present simple**", "jadwal tetap", "[[The train leaves at nine.]]"]]),

  dict(t="grammar", title="2. will: keputusan, janji, prediksi",
   table=[["Fungsi", "Contoh"],
          ["keputusan saat bicara", "[[The phone is ringing. I'll answer it.]]"],
          ["janji", "[[I will help you tomorrow.]]"],
          ["prediksi (pendapat)", "[[I think it will rain.]]"],
          ["tawaran", "[[I'll carry your bag.]]"]]),

  dict(t="grammar", title="3. be going to: rencana dan bukti",
   table=[["Fungsi", "Contoh"],
          ["rencana yang sudah ada", "[[We're going to visit Bali next month.]]"],
          ["prediksi dengan bukti", "[[Look! He's going to fall.]]"],
          ["negatif", "[[I'm not going to quit.]]"],
          ["tanya", "[[Are you going to come?]]"]]),

  dict(t="grammar", title="4. Beda will dan be going to",
   table=[["Situasi", "Pilihan"],
          ["Telepon berbunyi, kamu langsung mengangkat", "[[I'll get it.]] (will, keputusan spontan)"],
          ["Kamu sudah memutuskan kemarin untuk belajar", "[[I'm going to study tonight.]] (be going to, rencana)"],
          ["Langit mendung", "[[It's going to rain.]] (be going to, ada bukti)"],
          ["Pendapat umum tentang masa depan", "[[I think it will rain tomorrow.]] (will, opini)"]]),

  dict(t="grammar", title="5. Present continuous dan present simple untuk masa depan",
   table=[["Contoh", "Maknanya"],
          ["[[I'm meeting Rani at six.]]", "Rencana yang sudah diatur."],
          ["[[We're flying to Bali on Friday.]]", "Tiket sudah dibeli."],
          ["[[The meeting starts at ten.]]", "Jadwal tetap."],
          ["[[The shop closes at nine.]]", "Jadwal tetap."]]),

  dict(t="warn", title="Jebakan umum",
   text="Jangan pakai will setelah **if/when** untuk masa depan: [[If it rains, I will stay home.]], bukan ~~If it will rain~~. Dan jangan campur: bukan ~~I will going to~~."),
 ],

 practice=mk([
  ('Pilih bentuk yang benar (keputusan spontan): "The phone is ringing. I ___ answer it."', "will", "am going to", "would", "am answering", "Keputusan spontan → will."),
  ('Pilih bentuk yang benar (rencana): "I ___ study tonight. I decided this morning."', "am going to", "will", "would", "study", "Rencana → be going to."),
  ('Pilih bentuk yang benar (bukti): "Look at those clouds! It ___ rain."', "is going to", "will", "would", "rains", "Ada bukti → be going to."),
  ('Pilih bentuk yang benar (jadwal): "The train ___ at nine."', "leaves", "will leaving", "is going leave", "leaving", "Jadwal tetap → simple."),
  ('Pilih bentuk yang benar (rencana diatur): "I ___ Rani at six."', "am meeting", "meet", "will meeting", "meets", "Rencana diatur → continuous."),
  ('Pilih bentuk yang benar (janji): "I ___ help you tomorrow."', "will", "am helping", "helped", "have help", "Janji → will."),
  ('Pilih bentuk yang benar (tawaran): "I ___ carry your bag."', "will", "am going", "carried", "carrying", "Tawaran → will."),
  ('Pilih bentuk yang benar: "We ___ to Bali next month. We have the tickets."', "are flying", "will flying", "fly", "flew", "Rencana diatur."),
  ('Pilih bentuk yang benar: "I think it ___ rain tomorrow."', "will", "is going", "rains", "rained", "Opini → will."),
  ('Pilih bentuk yang benar: "The shop ___ at nine tonight."', "closes", "is closing down at", "will close down", "closing", "Jadwal tetap."),
  ('Pilih bentuk yang benar: "If it ___ tomorrow, I\'ll stay home."', "rains", "will rain", "rain", "rained", "if + present."),
  ('Pilih bentuk yang benar: "___ you going to come to the party?"', "Are", "Do", "Will", "Is", "Are you going to?"),
  ('Pilih bentuk yang benar: "She isn\'t going ___ quit."', "to", "for", "in", "at", "going to + V1."),
  ('Pilih kalimat yang benar:', "I'll call you tomorrow.", "I'll calling you tomorrow.", "I will to call you tomorrow.", "I'll called you tomorrow.", "will + V1."),
  ('Pilih kalimat yang SALAH:', "If it will rain, I stay home.", "If it rains, I will stay home.", "I think it will rain.", "It is going to rain.", "if + present."),
  ('Pilih kalimat yang SALAH:', "I will going to study.", "I am going to study.", "I will study.", "I am studying.", "Jangan campur will dan going to."),
 ]) + mkf([
  ("Aku akan mengangkat telepon itu. (spontan)", "The phone is ringing. I ___ get it.", "will/'ll", "Spontan → will."),
  ("Aku berencana belajar malam ini.", "I am ___ to study tonight.", "going", "be going to."),
  ("Lihat! Akan hujan.", "Look! It is going ___ rain.", "to", "going to + V1."),
  ("Kereta berangkat pukul sembilan.", "The train ___ at nine. (leave)", "leaves", "jadwal → simple."),
  ("Aku akan bertemu Rani pukul enam. (sudah diatur)", "I am ___ Rani at six. (meet)", "meeting", "present continuous."),
  ("Apakah kamu akan datang?", "___ you going to come?", "Are", "Are you going to?"),
 ]) + mko([
  ("Aku akan membantumu besok.", "I will help you tomorrow.", "am helping helps", ""),
  ("Kami akan mengunjungi Bali bulan depan.", "We are going to visit Bali next month.", "will visiting", ""),
  ("Rapat dimulai pukul sepuluh.", "The meeting starts at ten.", "starting start", ""),
 ]),

 quiz=mk([
  ('Pilih bentuk yang benar: "It\'s hot. I ___ open the window." (spontan)', "will", "am going to", "would", "opened", "Spontan → will."),
  ('Pilih bentuk yang benar: "We ___ visit my grandparents on Sunday. It\'s planned."', "are going to", "will", "would", "visited", "Rencana → be going to."),
  ('Pilih bentuk yang benar: "The film ___ at seven."', "starts", "will starting", "is start", "starting", "Jadwal."),
  ('Pilih bentuk yang benar: "I ___ my dentist tomorrow at four."', "am seeing", "see to", "will seeing", "saw", "Rencana diatur."),
  ('Pilih bentuk yang benar: "I promise I ___ be late."', "won\'t", "don\'t", "am not going", "didn\'t", "Janji → won't."),
  ('Pilih kalimat yang SALAH:', "I will to call you.", "I will call you.", "I am going to call you.", "I'm calling you at six.", "will + V1."),
  ('Pilih kalimat yang SALAH:', "When she will arrive, I will call.", "When she arrives, I will call.", "If she arrives, I will call.", "As soon as she arrives, I will call.", "when + present."),
  ('Pilih kalimat yang benar:', "Look out! The car is going to hit us.", "Look out! The car will hits us.", "Look out! The car going hit us.", "Look out! The car hit us.", "Bukti → be going to."),
 ]) + mkf([
  ("Aku akan membantumu.", "I ___ help you.", "will/'ll", "will."),
  ("Mereka akan pergi besok.", "They are ___ to leave tomorrow.", "going", "be going to."),
  ("Toko tutup pukul sembilan.", "The shop ___ at nine. (close)", "closes", "jadwal."),
 ]),
)
