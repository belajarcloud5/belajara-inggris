from ub import *
UNIT = mkunit("u95",
 ["menemukan **suku kata yang ditekan** pada kata bersuku kata banyak",
  "memakai **pola tekanan**: kata benda dan kata sifat, kata kerja, serta akhiran -tion, -ic, -ity",
  "membedakan **noun dan verb** seperti RECord dan reCORD",
  "mengenali tekanan pada **kata majemuk**"],
 [intro("Setiap kata bersuku kata lebih dari satu punya **satu suku kata yang ditekan**: lebih keras, lebih panjang, dan nadanya lebih tinggi. Salah menekan suku kata membuat kata sulit dipahami, bahkan bila bunyi vokalnya benar. Pada tulisan di sini, huruf kapital menandai tekanan, misalnya *TEAcher* dan *beGIN*."),
  gram("1. Pola dasar tekanan",
   table=[["Pola", "Contoh"],
          ["Kata benda dan kata sifat 2 suku kata: tekanan **pertama**", "[[TEAcher]], [[TAble]], [[DOCtor]], [[HAPpy]], [[PRETty]]"],
          ["Kata kerja 2 suku kata: tekanan **kedua**", "[[beGIN]], [[reLAX]], [[deCIDE]], [[aGREE]], [[exPLAIN]]"],
          ["Banyak kata 3 suku kata", "[[FAmily]], [[BEAUtiful]], [[toMORrow]], [[imPORtant]], [[baNAna]]"]],
   examples=[("[[The teacher will begin the lesson.]]", "Gurunya akan memulai pelajaran."), ("[[It is important to relax.]]", "Penting untuk bersantai.")]),
  gram("2. Akhiran yang menentukan tekanan",
   text="Akhiran tertentu memindahkan tekanan ke suku kata **sebelum** akhiran itu.",
   table=[["Akhiran", "Tekanan", "Contoh"],
          ["**-tion / -sion**", "tepat sebelum akhiran", "[[eduCAtion]], [[inforMAtion]], [[deCIsion]]"],
          ["**-ic / -ical**", "sebelum akhiran", "[[ecoNOMic]], [[photoGRAPHic]], [[poLITical]]"],
          ["**-ity**", "sebelum akhiran", "[[uniVERsity]], [[abILity]], [[opporTUnity]]"],
          ["**-eer / -ese / -ee**", "pada akhiran itu sendiri", "[[engiNEER]], [[JapaNESE]], [[refuGEE]]"]]),
  gram("3. Noun dan verb dengan ejaan sama",
   text="Beberapa kata berubah tekanan menurut kelas katanya. **Kata benda**: tekanan pertama. **Kata kerja**: tekanan kedua.",
   table=[["Kata", "Kata benda (tekanan 1)", "Kata kerja (tekanan 2)"],
          ["record", "[[REcord]] (catatan)", "[[reCORD]] (merekam)"],
          ["present", "[[PREsent]] (hadiah)", "[[preSENT]] (menyajikan)"],
          ["increase", "[[INcrease]] (kenaikan)", "[[inCREASE]] (naik)"],
          ["object", "[[OBject]] (benda)", "[[obJECT]] (keberatan)"]]),
  gram("4. Kata majemuk",
   text="Pada kata majemuk (dua kata menjadi satu arti), tekanan biasanya pada **bagian pertama**. Bandingkan dengan frasa biasa yang ditekan di kata kedua.",
   table=[["Kata majemuk (tekanan 1)", "Frasa biasa (tekanan 2)"],
          ["[[GREENhouse]] (rumah kaca)", "green HOUSE (rumah berwarna hijau)"],
          ["[[BLACKboard]] (papan tulis)", "black BOARD (papan hitam)"]]),
  vocab("5. Kata dan tekanannya", [
   ("TEAcher", "guru", "My teacher is kind."), ("beGIN", "mulai", "Let's begin."), ("baNAna", "pisang", "I eat a banana."),
   ("eduCAtion", "pendidikan", "Education is important."), ("uniVERsity", "universitas", "He studies at a university."),
   ("engiNEER", "insinyur", "She is an engineer."), ("PHOtograph", "foto", "Look at this photograph."), ("phoTOgrapher", "fotografer", "The photographer is here.")]),
  tip("Cara menemukan tekanan", text="Dengarkan kata dengan 🔊, lalu tepuk tangan pada suku kata yang terdengar paling keras dan panjang. Kamus daring menandai tekanan dengan tanda ˈ sebelum suku kata yang ditekan."),
  summary(["Kata benda dan sifat 2 suku kata: [[TEAcher]]; kata kerja: [[beGIN]].", "-tion, -ic, -ity: tekanan sebelum akhiran.", "Noun-verb: [[REcord]] / [[reCORD]], [[PREsent]] / [[preSENT]].", "Kata majemuk: tekanan di bagian pertama, [[GREENhouse]]."])],
 [], [])
def stress(word, shown, pos, exp):
    return (f'Pada kata "{word}" ({shown}), tekanan ada di suku kata ke...', pos, *[x for x in ['pertama', 'kedua', 'ketiga', 'keempat'] if x != pos][:3], exp)
rows = [("teacher", "TEA-cher", "pertama"), ("begin", "be-GIN", "kedua"), ("banana", "ba-NA-na", "kedua"), ("computer", "com-PU-ter", "kedua"),
        ("visit", "VIS-it", "pertama"), ("hotel", "ho-TEL", "kedua"), ("police", "po-LICE", "kedua"), ("important", "im-POR-tant", "kedua"),
        ("beautiful", "BEAU-ti-ful", "pertama"), ("tomorrow", "to-MOR-row", "kedua"), ("yesterday", "YES-ter-day", "pertama"),
        ("family", "FAM-i-ly", "pertama"), ("education", "ed-u-CA-tion", "ketiga"), ("information", "in-for-MA-tion", "ketiga"),
        ("university", "u-ni-VER-si-ty", "ketiga"), ("engineer", "en-gi-NEER", "ketiga"), ("Indonesia", "In-do-NE-sia", "ketiga"),
        ("opportunity", "op-por-TU-ni-ty", "ketiga"), ("chocolate", "CHOC-o-late", "pertama"), ("vegetable", "VEG-e-ta-ble", "pertama"),
        ("economic", "ec-o-NOM-ic", "ketiga"), ("Japanese", "Jap-a-NESE", "ketiga"), ("available", "a-VAIL-a-ble", "kedua"),
        ("photographer", "pho-TOG-ra-pher", "kedua"), ("photograph", "PHO-to-graph", "pertama"), ("decide", "de-CIDE", "kedua"),
        ("agree", "a-GREE", "kedua"), ("doctor", "DOC-tor", "pertama")]
P = [mcq(f'Pada kata "{w}", tekanan ada di suku kata ke...', [pos] + [x for x in ['pertama', 'kedua', 'ketiga'] if x != pos], 0, f"{shown}: tekanan di suku kata {pos}.") for w, shown, pos in rows]
P += mk([
 ('Dalam "Please record the meeting", tekanan "record" ada di suku kata ke...', 'kedua', 'pertama', 'ketiga', 'tidak ada', 'Kata kerja: reCORD.'),
 ('Dalam "This is a world record", tekanan "record" ada di suku kata ke...', 'pertama', 'kedua', 'ketiga', 'tidak ada', 'Kata benda: REcord.'),
 ('Dalam "I bought a present for her", tekanan "present" ada di suku kata ke...', 'pertama', 'kedua', 'ketiga', 'tidak ada', 'Kata benda (hadiah): PREsent.'),
 ('Dalam "I will present my idea", tekanan "present" ada di suku kata ke...', 'kedua', 'pertama', 'ketiga', 'tidak ada', 'Kata kerja: preSENT.'),
 ('Dalam "There is an increase in prices", tekanan "increase" ada di suku kata ke...', 'pertama', 'kedua', 'ketiga', 'tidak ada', 'Kata benda: INcrease.'),
 ('Dalam "Prices will increase", tekanan "increase" ada di suku kata ke...', 'kedua', 'pertama', 'ketiga', 'tidak ada', 'Kata kerja: inCREASE.'),
 ('Kata majemuk "greenhouse" (rumah kaca) ditekan pada...', 'bagian pertama (GREENhouse)', 'bagian kedua (greenHOUSE)', 'kedua-duanya sama', 'tidak ada tekanan', 'Kata majemuk: tekanan pertama.'),
 ('Kata mana yang tekanannya pada suku kata KEDUA?', 'decide', 'teacher', 'doctor', 'happy', 'deCIDE kata kerja.'),
 ('Kata mana yang tekanannya pada suku kata PERTAMA?', 'doctor', 'agree', 'begin', 'relax', 'DOCtor.'),
 ('Akhiran -tion membuat tekanan jatuh...', 'tepat sebelum akhiran', 'pada akhiran', 'di suku kata pertama selalu', 'di akhir kata', 'eduCAtion.'),
 ('Akhiran -ity membuat tekanan jatuh...', 'tepat sebelum akhiran', 'pada akhiran', 'di suku kata terakhir', 'tidak berubah', 'abILity.'),
])
P += dictate([("The teacher will begin the lesson.", "Gurunya akan memulai pelajaran."), ("It is important to relax tomorrow.", "Penting untuk bersantai besok."),
              ("My family likes chocolate and bananas.", "Keluargaku suka cokelat dan pisang."), ("The engineer works at a university.", "Insinyur itu bekerja di universitas.")])
Q = P[:0] + [mcq(f'Pada kata "{w}", tekanan ada di suku kata ke...', [pos] + [x for x in ['pertama', 'kedua', 'ketiga'] if x != pos], 0, f"{shown}: tekanan di suku kata {pos}.") for w, shown, pos in [("lesson", "LES-son", "pertama"), ("relax", "re-LAX", "kedua"), ("question", "QUES-tion", "pertama"), ("explain", "ex-PLAIN", "kedua"), ("organisation", "or-gan-i-ZA-tion", "keempat"), ("difficult", "DIF-fi-cult", "pertama")]]
Q = [q for q in Q if len(q['options']) >= 3] if False else Q
Q += mk([
 ('Dalam "She will present the report", tekanan "present" ada di suku kata ke...', 'kedua', 'pertama', 'ketiga', 'tidak ada', 'Kata kerja: preSENT.'),
 ('Kata mana yang tekanannya pada suku kata KETIGA?', 'education', 'teacher', 'begin', 'family', 'eduCAtion.'),
 ('Tekanan yang salah paling sering membuat...', 'kata sulit dipahami', 'kalimat menjadi lebih sopan', 'ejaan berubah', 'arti selalu sama', 'Tekanan penting bagi pendengar.'),
 ('Kata benda dua suku kata biasanya ditekan pada...', 'suku kata pertama', 'suku kata kedua', 'suku kata terakhir', 'tidak ada', 'TEAcher, TAble.'),
])
UNIT["practice"] = P
UNIT["quiz"] = Q
