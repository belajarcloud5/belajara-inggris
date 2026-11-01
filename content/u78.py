from qk import mk, mkf, mko
from helpers import mcq

def tfng(rows):
    out = []
    for passage, stmt, ans, exp in rows:
        opts = ["True", "False", "Not Given"]
        opts.remove(ans)
        out.append(mcq(f'Teks: "{passage}"  ·  Pernyataan: "{stmt}"  ·  Jawabannya True, False, atau Not Given?', [ans] + opts, 0, exp))
    return out

UNIT = dict(
 id="u78",
 goals=[
  "membedakan **True**, **False**, dan **Not Given** dengan tepat",
  "menghindari jebakan **pengetahuan pribadi** dan **kata penguat**",
  "membandingkan pernyataan dengan teks lewat **parafrase**",
  "mengenali beda **False** dan **Not Given**",
 ],
 lesson=[
  dict(t="intro", text="Soal **True / False / Not Given** adalah jenis soal Reading yang paling sering membuat peserta bingung. Kuncinya: **hanya percaya pada teks**, bukan pada pengetahuan atau pendapatmu."),

  dict(t="grammar", title="1. Arti tiga jawaban",
   table=[["Jawaban", "Artinya", "Cara mengenali"],
          ["**True**", "pernyataan **sesuai** dengan teks", "teks menyatakan hal yang sama (dengan kata lain)"],
          ["**False**", "pernyataan **bertentangan** dengan teks", "teks menyatakan kebalikannya"],
          ["**Not Given**", "teks **tidak membahas** hal itu", "tidak ada informasi untuk memastikan benar atau salah"]],
   examples=[dict(en="[[Text: The museum opens at nine.]]", id="Teks: Museum buka pukul sembilan."),
             dict(en="[[The museum opens in the morning. → True]]", id="Sesuai (pukul sembilan = pagi)."),
             dict(en="[[The museum opens at ten. → False]]", id="Bertentangan."),
             dict(en="[[The museum is free. → Not Given]]", id="Teks tidak menyebut harga.")]),

  dict(t="grammar", title="2. Langkah menjawab",
   table=[["Langkah", "Yang dilakukan"],
          ["1", "Garis bawahi kata kunci di pernyataan"],
          ["2", "Cari bagian teks yang membahas hal itu (sesuai urutan soal)"],
          ["3", "Bandingkan: sama, berlawanan, atau tidak ada?"],
          ["4", "Jika tidak ada informasi → Not Given"]]),

  dict(t="grammar", title="3. Jebakan yang sering muncul",
   table=[["Jebakan", "Contoh", "Jawaban"],
          ["pengetahuan pribadi", "teks tidak menyebut, tapi kamu tahu itu benar", "tetap Not Given"],
          ["kata penguat", "teks: [[some students]]; pernyataan: [[all students]]", "False"],
          ["kata pembatas", "teks: [[sometimes]]; pernyataan: [[always]]", "False"],
          ["sebagian vs seluruh", "teks: [[many]]; pernyataan: [[most]]", "biasanya Not Given"],
          ["sebab-akibat", "teks menyebut dua hal tapi tidak hubungannya", "Not Given"]]),

  dict(t="tip", title="Beda False dan Not Given",
   text="**False**: ada informasi, tetapi berlawanan. **Not Given**: tidak ada informasi sama sekali. Tanyakan: apakah teks memberi tahu aku hal yang berbeda? Jika ya → False. Jika teks diam → Not Given."),
  dict(t="warn", title="Perhatikan kata penguat",
   text="Kata seperti *all, always, never, only, most, every, none* mengubah makna. Bandingkan dengan kata di teks: *some, sometimes, rarely, many*. Satu kata saja bisa mengubah True menjadi False."),
 ],

 practice=tfng([
  ("The library closes at eight on weekdays.","The library closes in the evening on weekdays.","True","Pukul delapan = malam, sesuai."),
  ("The library closes at eight on weekdays.","The library closes at six on weekdays.","False","Teks menyebut delapan, bukan enam."),
  ("The library closes at eight on weekdays.","The library has a café.","Not Given","Teks tidak menyebut kafe."),
  ("Tom walks to school every day.","Tom goes to school on foot.","True","Walk = on foot."),
  ("Tom walks to school every day.","Tom takes the bus to school.","False","Teks: walks."),
  ("Tom walks to school every day.","Tom likes walking.","Not Given","Teks tidak menyebut perasaannya."),
  ("Some students study at night.","All students study at night.","False","some ≠ all."),
  ("Many people use public transport.","Most people use public transport.","Not Given","many tidak sama dengan most."),
  ("The company was founded in 2005 by two friends.","The company has existed for more than ten years.","Not Given","Teks tidak menyebut tahun sekarang."),
  ("The company was founded in 2005 by two friends.","The company was started by two people.","True","two friends = two people."),
  ("The company was founded in 2005 by two friends.","The company was founded by a university.","False","Didirikan dua teman."),
  ("Rice is grown in wet fields.","Rice grows in dry places.","False","Teks: wet fields."),
  ("The tour lasts three hours and costs fifty dollars.","The tour is cheap.","Not Given","Murah atau tidak adalah pendapat; teks tidak menilai."),
  ("The tour lasts three hours and costs fifty dollars.","The tour takes more than two hours.","True","Tiga jam > dua jam."),
  ("Rani speaks English and French.","Rani speaks three languages.","Not Given","Teks hanya menyebut dua bahasa; mungkin ada yang lain."),
  ("Rani speaks English and French.","Rani speaks at least two languages.","True","Dua bahasa disebut."),
  ("Scientists believe the sea level may rise by one metre.","Scientists are sure the sea level will rise by one metre.","False","may rise bukan pasti."),
  ("The film received good reviews, but few people watched it.","Many people watched the film.","False","few ≠ many."),
  ("The film received good reviews, but few people watched it.","The film was expensive to make.","Not Given","Tidak disebut."),
  ("He rarely eats meat.","He never eats meat.","False","rarely ≠ never."),
 ]) + mk([
  ('Jawaban True berarti pernyataan...', "sesuai dengan teks", "bertentangan dengan teks", "tidak ada di teks", "sesuai pengetahuanmu", "True = sesuai teks."),
  ('Jawaban False berarti pernyataan...', "bertentangan dengan teks", "sesuai teks", "tidak dibahas teks", "tidak penting", "False = bertentangan."),
  ('Jawaban Not Given berarti...', "teks tidak memberi informasi", "teks bertentangan", "teks sama persis", "jawaban tidak ada", "Tidak ada informasi."),
  ('Jika kamu tahu sebuah fakta tetapi teks tidak menyebutnya, jawabannya...', "Not Given", "True", "False", "kosong", "Hanya percaya pada teks."),
  ('Teks: "some" ; pernyataan: "all". Jawabannya...', "False", "True", "Not Given", "tidak bisa dijawab", "some ≠ all."),
  ('Kata penguat seperti "always" dan "never" biasanya menyebabkan jawaban...', "False", "True", "selalu Not Given", "kosong", "Perhatikan kata penguat."),
 ]) + mkf([
  ("Jawaban untuk pernyataan yang tidak dibahas teks adalah ___ .", "If the text does not say it, the answer is Not ___.", "Given", "Not Given."),
  ("Jawaban untuk pernyataan yang berlawanan dengan teks adalah ___ .", "If it contradicts the text, the answer is ___.", "False", "False."),
 ]),

 quiz=tfng([
  ("The museum opens at nine and closes at five.","The museum is open for eight hours.","True","9 sampai 5 = 8 jam."),
  ("The museum opens at nine and closes at five.","The museum is open on Sundays.","Not Given","Hari tidak disebut."),
  ("Most students prefer online classes.","Few students prefer online classes.","False","most ≠ few."),
  ("The festival is held every June.","The festival happens once a year.","True","Setiap Juni = sekali setahun."),
  ("The festival is held every June.","The festival is held in Bali.","Not Given","Tempat tidak disebut."),
  ("She never drinks coffee.","She sometimes drinks coffee.","False","never ≠ sometimes."),
  ("The new bridge will open next year.","The new bridge is already open.","False","Belum dibuka."),
  ("The bridge cost ten million dollars.","The bridge was expensive.","Not Given","Mahal adalah penilaian; teks tidak menilai."),
 ]) + mk([
  ('True / False / Not Given: yang bergantung pada informasi di...', "teks saja", "pengetahuanmu", "pendapatmu", "internet", "Hanya teks."),
  ('Teks diam tentang suatu hal. Jawabannya...', "Not Given", "True", "False", "kosong", "Tidak ada informasi."),
  ('"Some" di teks dan "all" di pernyataan berarti...', "False", "True", "Not Given", "tak bisa dijawab", "some ≠ all."),
  ('Mana yang menyebabkan jebakan terbesar?', "pengetahuan pribadi", "membaca judul", "membaca angka", "menulis ejaan", "Jangan pakai pengetahuan pribadi."),
 ]),
)
