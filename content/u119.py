from ub import *
UNIT = mkunit("u119",
 ["memahami format **Part 6**: teks pendek dengan empat bagian kosong",
  "memilih **bentuk kata, tense, dan kata penghubung** berdasarkan konteks teks",
  "memilih **kalimat yang hilang** yang cocok dengan alur paragraf",
  "memakai **petunjuk antarkalimat** (kata ganti, transisi, urutan)"],
 [intro("**Part 6** menyajikan empat teks pendek (email, pengumuman, memo, iklan). Tiap teks punya **empat kosong**: tiga menguji tata bahasa atau kosakata seperti Part 5, dan satu meminta **kalimat yang hilang**. Bedanya dengan Part 5: jawaban sering bergantung pada **kalimat sebelum atau sesudahnya**, bukan hanya kalimat itu sendiri."),
  gram("1. Jenis kosong di Part 6",
   table=[["Jenis", "Petunjuk", "Contoh"],
          ["Bentuk kata", "posisi kosong dalam kalimat", "[[We are pleased to ___ you]] → [[inform]]"],
          ["Tense", "penanda waktu di kalimat lain", "[[Your package ___ at your address within three days]] → [[will arrive]]"],
          ["Transisi / kata hubung", "hubungan dengan kalimat sebelumnya", "[[However]], [[Therefore]], [[In addition]], [[Please]]"],
          ["Kalimat yang hilang", "tema paragraf, kata ganti, dan urutan", "pilih kalimat yang menyambung topik"]]),
  gram("2. Memilih kalimat yang hilang",
   table=[["Langkah", "Isi"],
          ["1", "Baca kalimat sebelum dan sesudah kosong"],
          ["2", "Cari topik, kata ganti (it, they, this), dan waktu"],
          ["3", "Pilih kalimat yang menyambung dan tidak mengulang"],
          ["4", "Buang yang mengubah topik atau salah waktu"]]),
  gram("3. Kata transisi",
   table=[["Fungsi", "Kata"],
          ["Menambah", "[[In addition]], [[Moreover]], [[Also]]"],
          ["Kontras", "[[However]], [[Nevertheless]], [[On the other hand]]"],
          ["Akibat", "[[Therefore]], [[As a result]], [[Consequently]]"],
          ["Urutan", "[[First]], [[Then]], [[Finally]]"],
          ["Permintaan", "[[Please]], [[Kindly]]"]]),
  tip("Baca seluruh teks dulu (sekilas)", text="Baca teks 10–15 detik untuk memahami topik dan nada, baru jawab empat kosong. Pada soal kalimat yang hilang, topik teks adalah petunjuk terbesar."),
  summary(["Part 6: 4 kosong per teks; 3 tata bahasa/kosakata, 1 kalimat yang hilang.", "Jawaban bergantung konteks kalimat lain.", "Kalimat hilang: ikuti topik, kata ganti, dan waktu.", "Kata transisi: in addition, however, therefore, please."])],
 [], [])
def text_qs(title, template, blanks):
    """template memakai {0}..{3}; blanks = [(jawaban, a, b, c, exp)]. Kosong lain: jawaban benar sebelum, [...] sesudah."""
    out = []
    for k, (ans, w1, w2, w3, exp) in enumerate(blanks):
        parts = {}
        for j, b in enumerate(blanks):
            parts[str(j)] = "___" if j == k else (b[0] if j < k else "[...]")
        txt = template.format(*[parts[str(j)] for j in range(len(blanks))])
        out.append(mcq(f'Part 6 ({title}). Pilih jawaban untuk bagian kosong:  {txt}', [ans, w1, w2, w3], 0, exp))
    return out
T1 = "Dear Mr. Adi, Thank you for your order. We are pleased to {0} you that your package has been shipped. It {1} at your address within three working days. {2} contact our customer service team if you have any questions. {3} We look forward to serving you again. Sincerely, Blue Sky Store"
B1 = [("inform", "information", "informed", "informing", "To + kata kerja dasar."),
      ("will arrive", "arrived", "has arrived", "arriving", "Within three days → masa depan."),
      ("Please", "Although", "Unless", "Because", "Permintaan sopan."),
      ("Your satisfaction is important to us.", "The store opens at nine as usual.", "I like blue shirts.", "The weather is cold this week.", "Menyambung topik layanan pelanggan.")]
T2 = "NOTICE: The office will be closed on Monday {0} the national holiday. Employees {1} work from home that day if necessary. All reports {2} by Friday. {3} Thank you for your cooperation."
B2 = [("because of", "because", "although", "unless", "Because of + kata benda."),
      ("may", "have", "did", "are", "Modal untuk izin."),
      ("must be submitted", "must submit", "must submitting", "must submitted", "Passive modal."),
      ("Normal hours will resume on Tuesday.", "Mr. Adi likes tennis.", "The cafeteria sells noodles this week.", "I went home yesterday as usual.", "Menyambung topik jam kerja.")]
T3 = "MEMO. Starting next week, the company {0} a new email system. The new system is {1} than the old one, and it has better security. Training sessions {2} on Wednesday and Thursday. {3} Please sign up with your department manager."
B3 = [("will introduce", "introduced", "has introduced", "introducing", "Next week → masa depan."),
      ("faster", "fast", "fastest", "more fast", "Than → komparatif."),
      ("will be held", "will hold", "held", "are holding", "Passive masa depan."),
      ("All employees are required to attend one session.", "The old system was installed in 2005.", "Email is used by many people these days.", "Wednesdays are usually busy in general.", "Menyambung topik pelatihan.")]
T4 = "Join Fit Plus Gym today! For a limited time, we are offering a {0} price for new members. You can {1} our classes, which include yoga and swimming. {2} you sign up this month, you will receive one free personal training session. {3}"
B4 = [("special", "specially", "specialize", "specialty", "Sebelum benda → sifat."),
      ("attend", "attendance", "attendant", "attending", "Setelah can → kata kerja dasar."),
      ("If", "Although", "Unless", "Because", "If + present → will."),
      ("Call us at the front desk for more information.", "Gyms were popular in the past.", "Yoga started in India long ago these days.", "My brother likes swimming this week.", "Menyambung ajakan iklan.")]
T5 = "Dear Customers, we apologise for the delay in delivery. Unfortunately, a storm {0} our warehouse last week. As a result, many orders {1} late. We {2} to deliver all orders by the end of this month. {3}"
B5 = [("damaged", "damage", "damaging", "damages", "Last week → past simple."),
      ("have arrived", "arrive", "arriving", "will arrived", "Present perfect."),
      ("expect", "expected", "expecting", "expectation", "Subjek we → kata kerja."),
      ("We will email you when your order ships.", "Storms often occur in winter as usual.", "The warehouse is very large at the moment.", "I like to read books.", "Menyambung topik pesanan.")]
allq = []
for title, t, b in (("email", T1, B1), ("pengumuman", T2, B2), ("memo", T3, B3), ("iklan", T4, B4), ("permintaan maaf", T5, B5)):
    allq += text_qs(title, t, b)
P = allq[:12]
Q = allq[12:]
P += mk([
 ('Berapa soal pada Part 6?', '16', '30', '54', '6', '4 teks × 4 kosong.'),
 ('Berapa teks pada Part 6?', '4', '6', '10', '2', 'Empat teks.'),
 ('Salah satu kosong di tiap teks Part 6 biasanya meminta...', 'kalimat yang hilang', 'judul', 'tanda tangan', 'alamat', 'Sentence insertion.'),
 ('Cara terbaik memilih kalimat yang hilang adalah...', 'membaca kalimat sebelum dan sesudahnya', 'memilih kalimat terpanjang', 'memilih yang pertama', 'menebak acak', 'Konteks.'),
 ('Kata "However" menandai...', 'kontras', 'tambahan', 'akibat', 'urutan', 'However = kontras.'),
 ('Kata "Therefore" menandai...', 'akibat', 'kontras', 'contoh', 'urutan', 'Therefore = akibat.'),
 ('Kata "In addition" menandai...', 'tambahan', 'kontras', 'akibat', 'kesimpulan', 'In addition = selain itu.'),
 ('Kalimat mana yang paling cocok sebagai penutup email layanan pelanggan?', 'Thank you for your patience.', 'The weather is nice at the moment.', 'I like football.', 'My cat is white as usual.', 'Penutup sopan.'),
])
UNIT["practice"] = P
UNIT["quiz"] = Q
