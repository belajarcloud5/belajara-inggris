from ub import *
UNIT = vocab_unit("u161",
 ["mempelajari **kosakata akademik** yang sering muncul di TOEFL",
  "memahami arti dan **contoh pemakaian** tiap kata",
  "mengenali kata melalui **arti, ejaan, dan pendengaran**",
  "membaca teks akademik dengan lebih percaya diri"],
 "Teks TOEFL memakai kosakata akademik. Pelajari kata-kata berikut beserta contoh kalimatnya, lalu cari kata yang sama di bacaan.",
 [("Kata akademik (1)", [
   ("hypothesis", "hipotesis", "The scientist tested her hypothesis."), ("evidence", "bukti", "There is strong evidence for this theory."), ("theory", "teori", "Darwin proposed a famous theory."),
   ("significant", "bermakna / penting", "There was a significant increase in sales."), ("factor", "faktor", "Climate is one factor in this change."), ("source", "sumber", "The river is the main source of water."),
   ("method", "metode", "This method is faster."), ("trend", "tren / kecenderungan", "A new trend is growing among young people.")]),
  ("Kata akademik (2)", [
   ("estimate", "memperkirakan", "Experts estimate that the population will double."), ("indicate", "menunjukkan", "The results indicate a clear pattern."), ("assume", "menganggap / mengira", "Many people assume that the earth is flat."),
   ("require", "memerlukan", "The job requires experience."), ("rely on", "bergantung pada", "Many farmers rely on rain."), ("conclude", "menyimpulkan", "The study concluded that sleep matters."),
   ("contrast", "kontras / perbedaan", "There is a strong contrast between the two cities."), ("emphasise", "menekankan", "The teacher emphasised the main points.")]),
  ("Kata akademik (3)", [
   ("ensure", "memastikan", "Please ensure that the door is locked."), ("obtain", "memperoleh", "She obtained a scholarship."), ("previous", "sebelumnya", "The previous study had a smaller sample."),
   ("primary", "utama", "The primary goal is safety."), ("potential", "potensi", "The project has great potential."), ("various", "berbagai", "Various factors affect prices."),
   ("analyse", "menganalisis", "They analysed the data carefully."), ("consequence", "akibat", "Pollution has serious consequences.")])],
 "Dialog: Diskusi seminar",
 [("Mr. Adi", "What is your hypothesis?", "Apa hipotesismu?"), ("Dina", "Sleep is a significant factor in memory.", "Tidur adalah faktor penting dalam daya ingat."), ("Mr. Adi", "What evidence do you have?", "Bukti apa yang kamu punya?"), ("Dina", "Various studies indicate a clear pattern.", "Berbagai studi menunjukkan pola yang jelas.")],
 "Saat membaca teks akademik, tandai kata dari daftar ini. Pengulangan dalam konteks nyata jauh lebih efektif daripada menghafal daftar.", seed=161)
