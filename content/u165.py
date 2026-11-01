from ub import *
UNIT = vocab_unit("u165",
 ["memahami **phrasal verb menengah** untuk kehidupan sehari-hari",
  "memakai phrasal verb tentang **hubungan, perasaan, dan rencana**",
  "mengenali **makna harfiah dan kiasan**",
  "menjawab pertanyaan dengan phrasal verb yang tepat"],
 "Phrasal verb sangat umum dalam percakapan. Di unit ini kamu mempelajari phrasal verb untuk hubungan, rencana, dan kegiatan sehari-hari.",
 [("Hubungan dan perasaan", [
   ("get along", "akur / cocok", "I get along well with my neighbours."), ("break up", "putus (hubungan)", "They broke up last month."), ("cheer up", "menghibur", "Let's cheer her up."),
   ("calm down", "menenangkan diri", "Calm down and breathe slowly."), ("look after", "merawat", "She looks after her grandmother."), ("grow up", "tumbuh dewasa", "I grew up in Bandung."),
   ("make up", "berbaikan / mengarang", "They made up after the argument."), ("let down", "mengecewakan", "I do not want to let you down.")]),
  ("Rencana dan kegiatan", [
   ("show up", "muncul / datang", "He did not show up at the party."), ("call off", "membatalkan", "They called off the match because of rain."), ("drop by", "mampir", "Drop by my house tomorrow."),
   ("pick out", "memilih", "She picked out a red dress."), ("try out", "mencoba", "I want to try out the new cafe."), ("check out", "memeriksa / check-out", "Check out this video!"),
   ("hang out", "bersantai bersama", "We hang out at the park."), ("stay up", "begadang", "I stayed up late to study.")]),
  ("Barang dan uang", [
   ("run out of", "kehabisan", "We ran out of rice."), ("use up", "menghabiskan", "Don't use up all the water."), ("throw away", "membuang", "Don't throw away old bottles."),
   ("sell out", "habis terjual", "The tickets sold out in an hour."), ("save up", "menabung", "He is saving up for a bike."), ("pay back", "membayar kembali", "I will pay you back tomorrow."),
   ("give away", "memberikan cuma-cuma", "She gave away her old clothes."), ("put away", "menyimpan / merapikan", "Put away your toys.")])],
 "Dialog: Rencana akhir pekan",
 [("Rani", "Are you going to the party tonight?", "Apakah kamu pergi ke pesta malam ini?"), ("Dina", "I was, but they called it off.", "Tadinya iya, tetapi pesta itu dibatalkan."),
  ("Rani", "Why don't we hang out at my house instead?", "Bagaimana kalau kita bersantai di rumahku saja?"), ("Dina", "Great! I'll drop by at seven.", "Bagus! Aku akan mampir pukul tujuh.")],
 "Kelompokkan phrasal verb menurut tema (hubungan, rencana, uang). Menghafal per tema lebih mudah daripada menghafal berurutan.", seed=165)
UNIT["practice"] += mk([
 ('Pilih kalimat yang benar:', 'Please put your toys away.', 'Please put away your it toys.', 'Please away put your toys.', 'Please put to away your toys.', 'Put away dapat dipisah.'),
 ('Pilih kalimat yang benar:', 'I will pay you back tomorrow.', 'I will pay back you tomorrow.', 'I will back pay you tomorrow.', 'I will pay you to back tomorrow.', 'Pay (someone) back.'),
 ('Pilih kalimat yang benar:', 'She takes after her mother.', 'She takes her mother after.', 'She after takes her mother.', 'She takes with her mother.', 'Take after = mirip.'),
 ('Pilih kalimat yang SALAH:', 'He gave away it.', 'He gave it away.', 'He gave away his books.', 'He gave his books away.', 'Kata ganti di tengah.'),
 ('Pilih kalimat yang SALAH:', 'We ran out the sugar.', 'We ran out of sugar.', 'We ran out of rice.', 'They ran out of time.', 'Run out of.'),
 ('Pilih kalimat yang SALAH:', 'I grow up in Bali last year.', 'I grew up in Bali.', 'He will grow up soon.', 'They grew up together.', 'Grew up (lampau).'),
])
