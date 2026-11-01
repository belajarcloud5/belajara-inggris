from qk import mk, mkf, mko
BAS = dict(practice=mk([
 ('Pilih tag yang tepat: "You are a student, ___?"', 'aren\'t you', 'are you', 'don\'t you', 'isn\'t you', 'Positif → tag negatif.'),
 ('Pilih tag yang tepat: "She isn\'t here, ___?"', 'is she', 'isn\'t she', 'does she', 'is he', 'Negatif → tag positif.'),
 ('Pilih tag yang tepat: "They like music, ___?"', 'don\'t they', 'aren\'t they', 'do they', 'didn\'t they', 'Present simple → don\'t.'),
 ('Pilih tag yang tepat: "He plays football, ___?"', 'doesn\'t he', 'don\'t he', 'isn\'t he', 'does he', 'He → doesn\'t.'),
 ('Pilih tag yang tepat: "You went home, ___?"', 'didn\'t you', 'don\'t you', 'weren\'t you', 'did you', 'Lampau → didn\'t.'),
 ('Pilih tag yang tepat: "We can go now, ___?"', 'can\'t we', 'don\'t we', 'can we', 'aren\'t we', 'Can → can\'t.'),
 ('Pilih tag yang tepat: "It will rain, ___?"', 'won\'t it', 'doesn\'t it', 'will it', 'isn\'t it', 'Will → won\'t.'),
 ('Pilih tag yang tepat: "You don\'t agree, ___?"', 'do you', 'don\'t you', 'are you', 'did you', 'Negatif → tag positif.'),
 ('Pilih tag yang tepat: "Dina and Rani are friends, ___?"', 'aren\'t they', 'isn\'t she', 'don\'t they', 'aren\'t we', 'Dina and Rani → they.'),
 ('Pilih tag yang tepat: "It is a good idea, ___?"', 'isn\'t it', 'is it', 'doesn\'t it', 'aren\'t it', 'Is → isn\'t.'),
 ('Pilih tag yang tepat: "There is a cat, ___?"', 'isn\'t there', 'isn\'t it', 'is there', 'aren\'t there', 'There is → isn\'t there.'),
 ('Pilih tag yang tepat: "I am late, ___?"', 'aren\'t I', 'amn\'t I', 'am not I', 'don\'t I', 'Kasus khusus: aren\'t I.'),
 ('Pilih tag yang tepat: "Let\'s go, ___?"', 'shall we', 'will we', 'don\'t we', 'do we', 'Let\'s → shall we.'),
 ('Pilih kalimat yang benar:', 'You like pizza, don\'t you?', 'You like pizza, do you?', 'You like pizza, aren\'t you?', 'You like pizza, don\'t he?', 'Positif + tag negatif.'),
 ('Pilih kalimat yang benar:', 'He can\'t swim, can he?', 'He can\'t swim, can\'t he?', 'He can\'t swim, does he?', 'He can\'t swim, doesn\'t he?', 'Negatif + tag positif.'),
 ('Pilih kalimat yang SALAH:', 'She is kind, is she?', 'She is kind, isn\'t she?', 'She isn\'t kind, is she?', 'She was kind, wasn\'t she?', 'Positif butuh tag negatif.'),
 ('Pilih kalimat yang SALAH:', 'They live here, aren\'t they?', 'They live here, don\'t they?', 'They don\'t live here, do they?', 'They lived here, didn\'t they?', 'Live → don\'t they.'),
 ('Nada naik di akhir tag artinya...', 'benar-benar bertanya', 'sudah yakin', 'marah', 'tidak peduli', 'Rising = bertanya.'),
 ('Nada turun di akhir tag artinya...', 'meminta persetujuan', 'tidak tahu sama sekali', 'menolak', 'berteriak', 'Falling = mengonfirmasi.'),
]), quiz=mk([
 ('Pilih tag yang tepat: "You have a pen, ___?"', 'don\'t you', 'haven\'t you', 'do you', 'aren\'t you', 'Have sebagai kata kerja utama → don\'t you.'),
 ('Pilih tag yang tepat: "He wasn\'t at school, ___?"', 'was he', 'wasn\'t he', 'did he', 'is he', 'Negatif → positif.'),
 ('Pilih tag yang tepat: "They will come, ___?"', 'won\'t they', 'don\'t they', 'will they', 'aren\'t they', 'Will → won\'t.'),
 ('Pilih tag yang tepat: "She likes tea, ___?"', 'doesn\'t she', 'isn\'t she', 'does she', 'don\'t she', 'She → doesn\'t.'),
 ('Pilih kalimat yang benar:', 'It isn\'t expensive, is it?', 'It isn\'t expensive, isn\'t it?', 'It isn\'t expensive, does it?', 'It isn\'t expensive, it is?', 'Negatif + positif.'),
 ('Pilih tag yang tepat: "We should go, ___?"', 'shouldn\'t we', 'don\'t we', 'should we', 'aren\'t we', 'Should → shouldn\'t.'),
]))
BAS["practice"] += mkf([
 ('Kamu seorang siswa, bukan?', "You are a student, ___ you?", "aren't/arent", "Positif → tag negatif."),
 ('Dia tidak di sini, kan?', "She isn't here, ___ she?", 'is', 'Negatif → tag positif.'),
 ('Mereka suka musik, bukan?', "They like music, ___ they?", "don't/dont", "Like → don't."),
 ('Dia bermain bola, bukan?', "He plays football, ___ he?", "doesn't/doesnt", "Plays → doesn't."),
 ('Kita bisa pergi, bukan?', "We can go, ___ we?", "can't/cant", "Can → can't."),
 ('Kamu pergi ke rumah, bukan?', "You went home, ___ you?", "didn't/didnt", "Lampau → didn't."),
])
BAS["practice"] += mko([
 ('Itu ide bagus, bukan?', "It is a good idea, isn't it?", 'is not', ''),
 ('Kamu tidak setuju, kan?', "You don't agree, do you?", 'does did', ''),
 ('Mereka suka musik, bukan?', "They like music, don't they?", 'doesn\'t do', ''),
])
BAS["quiz"] += mkf([
 ('Dia suka teh, bukan?', "She likes tea, ___ she?", "doesn't/doesnt", "Likes → doesn't."),
 ('Mereka akan datang, bukan?', "They will come, ___ they?", "won't/wont", "Will → won't."),
])
