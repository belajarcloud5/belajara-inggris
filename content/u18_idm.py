from qk import mk, mkf, mko
IDM = dict(practice=mk([
 ('Apa arti "under the weather"?', 'kurang sehat', 'di bawah hujan', 'sangat bahagia', 'sedang kedinginan', 'Idiom: tidak enak badan.'),
 ('Apa arti "take it easy"?', 'bersantai', 'bekerja keras', 'mengambil makanan', 'berlari cepat', 'Jangan memaksakan diri.'),
 ('Apa arti "hit the sack"?', 'pergi tidur', 'memukul karung', 'pergi belanja', 'bangun pagi', 'Idiom santai: tidur.'),
 ('Apa arti "call it a day"?', 'menyudahi pekerjaan hari ini', 'menelepon teman besok pagi', 'menamai hari dalam seminggu', 'mulai bekerja lebih awal', 'Berhenti untuk hari ini.'),
 ('Apa arti "keep in touch"?', 'tetap berhubungan', 'jangan menyentuh apa pun', 'tetap diam di rumah', 'tetap pergi ke sekolah', 'Tetap saling kabar.'),
 ('Apa arti "cost an arm and a leg"?', 'sangat mahal', 'sangat murah', 'sangat berbahaya', 'sangat berat', 'Harganya selangit.'),
 ('Apa arti "in the same boat"?', 'senasib', 'di perahu yang sama', 'sedang liburan', 'sedang pindah', 'Mengalami hal yang sama.'),
 ('Pilih yang tepat: "I have a headache and a fever. I\'m ___."', 'under the weather', 'in the same boat now', 'a piece of cake today', 'calling it a day soon', 'Sakit → kurang sehat.'),
 ('Pilih yang tepat: "The doctor said, \'___ and drink a lot of water.\'"', 'Take it easy', 'Hit the books', 'Keep in touch', 'Cost an arm', 'Dokter → beristirahat.'),
 ('Pilih yang tepat: "It is midnight and I am sleepy. I\'m going to ___."', 'hit the sack', 'call it a day', 'take it easy', 'keep in touch', 'Mau tidur.'),
 ('Pilih yang tepat: "We worked for ten hours. Let\'s ___."', 'call it a day', 'hit the sack', 'be under the weather', 'cost an arm', 'Selesai kerja.'),
 ('Pilih yang tepat: "I\'m moving to Japan, but I\'ll ___ with you."', 'keep in touch', 'hit the sack', 'take it easy', 'call it a day', 'Tetap berkabar.'),
 ('Pilih yang tepat: "That new car ___. I can\'t afford it."', 'costs an arm and a leg', 'is under the weather', 'hits the sack early', 'is in the same boat', 'Tak terjangkau → sangat mahal.'),
 ('Pilih yang tepat: "You failed the test too? We are ___."', 'in the same boat', 'under the weather', 'a piece of cake', 'taking it easy', 'Sama-sama gagal → senasib.'),
 ('Pilih yang tepat: "I have a cold. I\'m a bit ___ today."', 'under the weather', 'in the same boat', 'cost an arm', 'on the sack', 'Pilek → kurang sehat.'),
 ('Pilih arti yang benar untuk "hit the sack":', 'go to bed', 'go shopping', 'go running', 'go to school', 'Tidur.'),
 ('Pilih arti yang benar untuk "cost an arm and a leg":', 'very expensive', 'very cheap indeed', 'very painful today', 'very heavy to lift', 'Mahal sekali.'),
 ('Mana yang BUKAN idiom?', 'I hit the ball.', 'Hit the sack.', 'Under the weather.', 'Call it a day.', 'Kalimat pertama harfiah.'),
 ('Mana penutup surat untuk teman?', 'Keep in touch!', 'Hit the sack!', 'Cost an arm!', 'Under the weather!', 'Cocok untuk teman.'),
 ('Pilih jawaban yang sopan untuk "Are you OK?"', 'I\'m a little under the weather.', 'I\'m a little in the same boat.', 'I\'m a little hitting the sack.', 'I\'m a little cost an arm.', 'Mengatakan kurang sehat.'),
]), quiz=mk([
 ('Apa arti "take it easy"?', 'bersantai', 'bekerja lembur', 'makan siang', 'bicara keras', 'Jangan memaksakan diri.'),
 ('Pilih yang tepat: "It is 9 p.m. Time to ___."', 'call it a day', 'be in the same boat', 'cost an arm', 'be under the weather', 'Menyudahi hari.'),
 ('Pilih yang tepat: "Tickets to the concert ___. They cost five million rupiah."', 'cost an arm and a leg', 'hit the sack early', 'keep in touch often', 'take it easy today', 'Sangat mahal.'),
 ('Pilih yang tepat: "I\'m ___ , so I will stay in bed today."', 'under the weather', 'in the same boat', 'calling it a day', 'keeping in touch', 'Kurang sehat.'),
 ('Pilih yang tepat: "Neither of us has money. We are ___."', 'in the same boat', 'under the weather', 'hitting the sack', 'taking it easy', 'Senasib.'),
 ('Pilih yang tepat: "Goodbye! Please ___ by email."', 'keep in touch', 'hit the sack', 'cost an arm', 'call it a day', 'Tetap berkabar.'),
]))
IDM["practice"] += mkf([
 ('Aku kurang sehat.', "I'm under the ___.", 'weather', 'Under the weather.'),
 ('Santai saja.', 'Take it ___.', 'easy', 'Take it easy.'),
 ('Aku mau tidur.', "I'm going to hit the ___.", 'sack', 'Hit the sack.'),
 ('Ayo sudahi hari ini.', "Let's call it a ___.", 'day', 'Call it a day.'),
 ('Tetap berhubungan ya.', 'Keep in ___.', 'touch', 'Keep in touch.'),
 ('Itu sangat mahal.', 'It costs an arm and a ___.', 'leg', 'Cost an arm and a leg.'),
 ('Kita senasib.', 'We are in the same ___.', 'boat', 'In the same boat.'),
])
IDM["quiz"] += mkf([
 ('Aku mau tidur.', "I'm going to hit the ___.", 'sack', 'Hit the sack.'),
 ('Kita senasib.', 'We are in the same ___.', 'boat', 'In the same boat.'),
])
