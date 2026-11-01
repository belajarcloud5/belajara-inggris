from qk import mk, mkf, mko
WH = dict(practice=mk([
 ('Pilih kalimat yang benar:', 'What do you eat for breakfast?', 'What you eat for breakfast?', 'What does you eat for breakfast?', 'What do you eats for breakfast?', 'What + do + you + kata kerja dasar.'),
 ('Pilih kalimat yang benar:', 'Where does she live?', 'Where does she lives?', 'Where she lives?', 'Where do she live?', 'She memakai does; kata kerja dasar.'),
 ('Pilih kalimat yang benar:', 'When do they play football?', 'When does they play football?', 'When they play football?', 'When do they plays football?', 'They memakai do.'),
 ('Pilih kalimat yang benar:', 'Why does he get up early?', 'Why does he gets up early?', 'Why he gets up early?', 'Why do he get up early?', 'He memakai does; get tanpa -s.'),
 ('Pilih kalimat yang benar:', 'How often do you study English?', 'How often you study English?', 'How often does you study English?', 'How often do you studies English?', 'How often + do + you.'),
 ('Pilih kalimat yang benar:', 'What time does the class start?', 'What time do the class start?', 'What time the class starts?', 'What time does the class starts?', 'The class tunggal → does + start.'),
 ('Pilih kalimat yang benar:', 'What does your mother do?', 'What do your mother do?', 'What your mother does?', 'What does your mother does?', 'Your mother → does; do sebagai kata kerja utama.'),
 ('Pilih kalimat yang benar:', 'Who lives in this house?', 'Who does live in this house?', 'Who live in this house?', 'Who do lives in this house?', 'Who sebagai subjek: kata kerja -s, tanpa does.'),
 ('Pilih kata tanya: "___ do you go to school?" - "I go by bus."', 'How', 'Who', 'When', 'Whose', 'Cara pergi → How.'),
 ('Pilih kata tanya: "___ does he play football?" - "He plays on Sunday."', 'When', 'Who', 'What', 'Whose', 'Waktu → When.'),
 ('Pilih kata tanya: "___ do you live?" - "I live in Bogor."', 'Where', 'When', 'Who', 'Why', 'Tempat → Where.'),
 ('Pilih kata tanya: "___ does she like?" - "She likes pizza."', 'What', 'Who', 'Where', 'How often', 'Menanyakan benda → What.'),
 ('Pilih kata tanya: "___ do you like English?" - "Because it is fun."', 'Why', 'What', 'When', 'Where', 'Dijawab Because → Why.'),
 ('Pilih kata tanya: "___ does your brother wash the car?" - "Twice a week."', 'How often', 'How old', 'How much', 'Whose', 'Frekuensi → How often.'),
 ('Pilih kata tanya: "___ do you get up?" - "At six o\'clock."', 'What time', 'What day', 'Who', 'How many', 'Jam → What time.'),
 ('Pilih jawaban yang cocok untuk "Where does he work?"', 'He works in a bank.', 'He works hard.', 'He works at eight.', 'He works with Tom.', 'Where → tempat.'),
 ('Pilih jawaban yang cocok untuk "When do you do your homework?"', 'I do it after dinner.', 'I do it in my room.', 'I do it with Rani.', 'I do it very well.', 'When → waktu.'),
 ('Pilih jawaban yang cocok untuk "How often do you read?"', 'Every night.', 'In the library.', 'A comic book.', 'With my sister.', 'How often → frekuensi.'),
 ('Pilih jawaban yang cocok untuk "What does she do?"', 'She is a nurse.', 'She is in Bali.', 'She is tall.', 'She is at home.', 'What does ... do → pekerjaan.'),
 ('Pilih yang benar: "Who ___ the guitar?" (play, subjek)', 'plays', 'play', 'does play', 'do plays', 'Who sebagai subjek: kata kerja + -s.'),
]), quiz=mk([
 ('Pilih kalimat yang benar:', 'Where do you eat lunch?', 'Where you eat lunch?', 'Where does you eat lunch?', 'Where do you eats lunch?', 'Where + do + you.'),
 ('Pilih kalimat yang benar:', 'What time does he go home?', 'What time does he goes home?', 'What time he goes home?', 'What time do he go home?', 'Does + go.'),
 ('Pilih kalimat yang benar:', 'Why do they wake up early?', 'Why does they wake up early?', 'Why they wake up early?', 'Why do they wakes up early?', 'They memakai do.'),
 ('Pilih kata tanya: "___ do you usually go to bed?" - "At ten."', 'What time', 'How old', 'Who', 'Whose', 'Jam → What time.'),
 ('Pilih jawaban yang cocok untuk "Why does she study hard?"', 'Because she wants good marks.', 'In her room.', 'At night.', 'With her friends.', 'Why → Because.'),
 ('Pilih jawaban yang cocok untuk "How often does he swim?"', 'Twice a week.', 'In the pool.', 'With his dad.', 'Very well.', 'How often → frekuensi.'),
 ('Pilih yang benar: "Who ___ English?" (teach, subjek tunggal)', 'teaches', 'teach', 'does teach', 'do teaches', 'Who sebagai subjek: -es.'),
 ('Pilih kalimat yang benar:', 'When does the shop open?', 'When does the shop opens?', 'When the shop opens?', 'When do the shop open?', 'The shop tunggal → does open.'),
]))
WH["practice"] += mkf([
 ('Apa yang kamu makan untuk sarapan?', 'What ___ you eat for breakfast?', 'do', 'You → do.'),
 ('Di mana dia tinggal?', 'Where ___ she live?', 'does', 'She → does.'),
 ('Kapan mereka bermain?', 'When ___ they play?', 'do', 'They → do.'),
 ('Mengapa dia bangun pagi?', 'Why does he ___ up early?', 'get', 'Setelah does: kata kerja dasar.'),
 ('Seberapa sering kamu membaca?', 'How ___ do you read?', 'often', 'How often = seberapa sering.'),
 ('Jam berapa kelas mulai?', 'What ___ does the class start?', 'time', 'What time = jam berapa.'),
 ('Siapa yang tinggal di sini?', 'Who ___ here?', 'lives', 'Who sebagai subjek: kata kerja + -s.'),
 ('Apa pekerjaan ibumu?', 'What does your mother ___?', 'do', 'What does ... do = pekerjaan.'),
])
WH["practice"] += mko([
 ('Apa yang kamu makan untuk sarapan?', 'What do you eat for breakfast?', 'does eats', ''),
 ('Di mana dia belajar?', 'Where does she study?', 'do studies', ''),
 ('Seberapa sering kamu berolahraga?', 'How often do you exercise?', 'does exercises', ''),
 ('Jam berapa dia pulang?', 'What time does he go home?', 'do goes', ''),
 ('Mengapa mereka belajar bahasa Inggris?', 'Why do they study English?', 'does studies', ''),
])
WH["quiz"] += mkf([
 ('Di mana kamu makan siang?', 'Where ___ you eat lunch?', 'do', 'You → do.'),
 ('Jam berapa dia pulang?', 'What time ___ he go home?', 'does', 'He → does.'),
 ('Siapa yang bermain gitar?', 'Who ___ the guitar?', 'plays', 'Who sebagai subjek: -s.'),
])
