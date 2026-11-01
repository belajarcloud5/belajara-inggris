from qk import mk, mkf, mko
WH = dict(practice=mk([
 ('Pilih kalimat yang benar:', 'What did you do yesterday?', 'What did you did yesterday?', 'What you did yesterday?', 'What do you did yesterday?', 'Did + kata kerja dasar.'),
 ('Pilih kalimat yang benar:', 'Where did you go on holiday?', 'Where did you went on holiday?', 'Where you went on holiday?', 'Where do you went on holiday?', 'Did + go.'),
 ('Pilih kalimat yang benar:', 'When did she arrive?', 'When did she arrived?', 'When she arrived?', 'When does she arrived?', 'Did + arrive.'),
 ('Pilih kalimat yang benar:', 'Why did he leave early?', 'Why did he left early?', 'Why he left early?', 'Why does he left early?', 'Did + leave.'),
 ('Pilih kalimat yang benar:', 'Where were you last night?', 'Where was you last night?', 'Where did you were last night?', 'Where you were last night?', 'You memakai were.'),
 ('Pilih kalimat yang benar:', 'How was your weekend?', 'How were your weekend?', 'How did your weekend?', 'How your weekend was?', 'Weekend tunggal → was.'),
 ('Pilih kalimat yang benar:', 'Who was your teacher?', 'Who were your teacher?', 'Who did your teacher?', 'Who your teacher was?', 'Tunggal → was.'),
 ('Pilih kalimat yang benar:', 'Who broke the window?', 'Who did break the window?', 'Who broken the window?', 'Who does broke the window?', 'Who sebagai subjek: kata kerja lampau, tanpa did.'),
 ('Pilih kata tanya: "___ did you eat for lunch?" - "I ate fried rice."', 'What', 'Who', 'Where', 'When', 'Benda → What.'),
 ('Pilih kata tanya: "___ did they go last week?" - "They went to Bali."', 'Where', 'When', 'Who', 'Whose', 'Tempat → Where.'),
 ('Pilih kata tanya: "___ did you meet Rani?" - "Two days ago."', 'When', 'Where', 'Who', 'What', 'Waktu → When.'),
 ('Pilih kata tanya: "___ did you call?" - "I called my uncle."', 'Who', 'When', 'Why', 'How', 'Orang → Who.'),
 ('Pilih kata tanya: "___ did she cry?" - "Because she lost her cat."', 'Why', 'What', 'Where', 'Who', 'Dijawab Because → Why.'),
 ('Pilih kata tanya: "___ did you come to school?" - "By bike."', 'How', 'Who', 'When', 'Whose', 'Cara → How.'),
 ('Pilih kata tanya: "___ were the students?" - "They were in the hall."', 'Where', 'Who', 'When', 'How old', 'Tempat → Where.'),
 ('Pilih kata tanya: "___ was the film?" - "It was great."', 'How', 'Who', 'Where', 'When', 'Pendapat → How.'),
 ('Pilih jawaban yang cocok untuk "What time did you get up?"', 'At five thirty.', 'At the station.', 'With my brother.', 'By car.', 'What time → jam.'),
 ('Pilih jawaban yang cocok untuk "Why did you stay at home?"', 'Because I was sick.', 'On Sunday.', 'At the mall.', 'With my mother.', 'Why → Because.'),
 ('Pilih jawaban yang cocok untuk "Who did you see?"', 'I saw my cousin.', 'I saw it yesterday.', 'I saw it in the park.', 'I saw it clearly.', 'Who → orang.'),
 ('Pilih yang benar: "How long ___ you stay in Bali?"', 'did', 'do', 'does', 'were', 'Kata kerja biasa lampau → did.'),
]), quiz=mk([
 ('Pilih kalimat yang benar:', 'What did he buy?', 'What did he bought?', 'What he bought?', 'What does he bought?', 'Did + buy.'),
 ('Pilih kalimat yang benar:', 'Where were they yesterday?', 'Where was they yesterday?', 'Where did they were yesterday?', 'Where they were yesterday?', 'They memakai were.'),
 ('Pilih kalimat yang benar:', 'When did you start school?', 'When did you started school?', 'When you started school?', 'When do you started school?', 'Did + start.'),
 ('Pilih kata tanya: "___ did you stay?" - "For three days."', 'How long', 'How old', 'Whose', 'Who', 'Lamanya → How long.'),
 ('Pilih jawaban yang cocok untuk "How was the trip?"', 'It was wonderful.', 'It was in May.', 'It was by train.', 'It was with Tom.', 'How was → pendapat.'),
 ('Pilih jawaban yang cocok untuk "When did he call?"', 'Ten minutes ago.', 'On the phone.', 'My cousin.', 'About homework.', 'When → waktu.'),
 ('Pilih yang benar: "Who ___ the cake?" (eat, lampau, subjek)', 'ate', 'eat', 'did eat', 'eaten', 'Who sebagai subjek: lampau, tanpa did.'),
 ('Pilih kata tanya: "___ was your first teacher?" - "Mrs. Sari."', 'Who', 'When', 'Where', 'How', 'Orang → Who.'),
]))
WH["practice"] += mkf([
 ('Apa yang kamu lakukan kemarin?', 'What ___ you do yesterday?', 'did', 'Lampau → did.'),
 ('Ke mana kamu pergi?', 'Where did you ___?', 'go', 'Setelah did: kata kerja dasar.'),
 ('Kapan dia tiba?', 'When did she ___?', 'arrive', 'Setelah did: kata kerja dasar.'),
 ('Di mana kamu tadi malam?', 'Where ___ you last night?', 'were', 'You → were.'),
 ('Bagaimana akhir pekanmu?', 'How ___ your weekend?', 'was', 'Weekend tunggal → was.'),
 ('Siapa yang memecahkan jendela?', 'Who ___ the window?', 'broke', 'Who sebagai subjek: kata kerja lampau.'),
 ('Mengapa dia pergi lebih awal?', 'Why did he ___ early?', 'leave', 'Setelah did: leave.'),
 ('Jam berapa kamu bangun?', 'What time did you get ___?', 'up', 'Get up = bangun.'),
])
WH["practice"] += mko([
 ('Apa yang kamu makan tadi malam?', 'What did you eat last night?', 'do ate', ''),
 ('Ke mana mereka pergi?', 'Where did they go?', 'do went', ''),
 ('Di mana kamu kemarin?', 'Where were you yesterday?', 'did was', ''),
 ('Mengapa dia menangis?', 'Why did she cry?', 'does cried', ''),
 ('Bagaimana liburanmu?', 'How was your holiday?', 'were did', ''),
])
WH["quiz"] += mkf([
 ('Apa yang dia beli?', 'What did he ___?', 'buy', 'Setelah did: buy.'),
 ('Di mana mereka kemarin?', 'Where ___ they yesterday?', 'were', 'They → were.'),
 ('Siapa yang makan kue itu?', 'Who ___ the cake?', 'ate', 'Who sebagai subjek: lampau.'),
])
