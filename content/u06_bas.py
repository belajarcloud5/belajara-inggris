from qk import mk, mkf, mko
BAS = dict(practice=mk([
 ('Pilih yang tepat: "This bag is ___. It is not yours."', 'mine', 'my', 'me', 'I', 'Berdiri sendiri → mine.'),
 ('Pilih yang tepat: "Is this pen ___?"', 'yours', 'your', 'you', 'yours pen', 'Tanpa benda setelahnya → yours.'),
 ('Pilih yang tepat: "That scarf is Rani\'s. It is ___."', 'hers', 'she', 'her scarf', 'she\'s', 'Rani = perempuan → hers.'),
 ('Pilih yang tepat: "The house is Tom and his wife\'s. It is ___."', 'theirs', 'their', 'them', 'they', 'Milik mereka → theirs.'),
 ('Pilih yang tepat: "We bought this car. It is ___."', 'ours', 'our', 'us', 'we', 'Milik kami → ours.'),
 ('Pilih yang tepat: "___ book is this?" - "It is Dina\'s."', 'Whose', 'Who', 'Who\'s', 'What', 'Menanyakan pemilik → Whose.'),
 ('Pilih yang tepat: "___ are these shoes?" - "They are mine."', 'Whose', 'Who', 'Where', 'When', 'Menanyakan pemilik → Whose.'),
 ('Pilih kalimat yang benar:', 'This pen is mine.', 'This pen is mine pen.', 'This pen is me.', 'This pen mine is.', 'Mine berdiri sendiri.'),
 ('Pilih kalimat yang benar:', 'These books are theirs.', 'These books are their\'s.', 'These books are theirs books.', 'These books are there.', 'Tanpa apostrof.'),
 ('Pilih kalimat yang SALAH:', 'This is mine bag.', 'This is my bag.', 'This bag is mine.', 'This bag is yours.', 'Mine tidak diikuti benda.'),
 ('Pilih kalimat yang SALAH:', 'The red pen is her\'s.', 'The red pen is hers.', 'The red pen is Dina\'s.', 'The red pen is hers, not his.', 'Hers tanpa apostrof.'),
 ('Pilih kalimat yang benar:', 'Whose umbrella is this?', 'Who\'s umbrella is this?', 'Whose is umbrella this?', 'Whose this umbrella is?', 'Whose + benda.'),
 ('Pilih jawaban yang cocok untuk "Whose bag is this?"', 'It is Budi\'s.', 'It is Budi.', 'He is Budi.', 'Budi is nice.', 'Pemilik: Budi\'s.'),
 ('Ubah menjadi kata ganti milik: "This is my pencil." →', 'This pencil is mine.', 'This pencil is my.', 'This pencil is me.', 'This pencil mine is.', 'My + benda → mine.'),
 ('Ubah menjadi kata ganti milik: "That is your seat." →', 'That seat is yours.', 'That seat is your.', 'That seat is you.', 'That seat yours is.', 'Your + benda → yours.'),
 ('Mana yang BUKAN kata ganti milik?', 'me', 'mine', 'yours', 'hers', 'Me = kata ganti objek.'),
]), quiz=mk([
 ('Pilih yang tepat: "My phone is new. ___ is old."', 'Yours', 'You', 'Your', 'Yourself', 'Yours = your phone.'),
 ('Pilih yang tepat: "___ turn is it?" - "It is mine."', 'Whose', 'Who', 'Which', 'Where', 'Menanyakan pemilik giliran.'),
 ('Pilih yang tepat: "Those keys are ___. We found them."', 'ours', 'our', 'us', 'we', 'Milik kami → ours.'),
 ('Pilih kalimat yang benar:', 'Is this coat his?', 'Is this coat he?', 'Is this coat him?', 'Is this coat he\'s?', 'His berdiri sendiri.'),
 ('Pilih kalimat yang SALAH:', 'This is yours\' pen.', 'This is your pen.', 'This pen is yours.', 'This pen is not yours.', 'Tanpa apostrof.'),
 ('Pilih kalimat yang benar:', 'Whose are these?', 'Who\'s are these?', 'Whose these are?', 'Whose is these?', 'Whose are these?'),
]))
BAS["practice"] += mkf([
 ('Tas ini milikku.', 'This bag is ___.', 'mine', 'Mine = milikku.'),
 ('Apakah pulpen ini milikmu?', 'Is this pen ___?', 'yours', 'Yours = milikmu.'),
 ('Buku itu milik mereka.', 'The book is ___.', 'theirs', 'Theirs = milik mereka.'),
 ('Tas siapa ini?', '___ bag is this?', 'Whose', 'Whose = milik siapa.'),
 ('Syal itu miliknya (perempuan).', 'The scarf is ___.', 'hers', 'Hers = miliknya.'),
 ('Rumah itu milik kami.', 'The house is ___.', 'ours', 'Ours = milik kami.'),
])
BAS["practice"] += mko([
 ('Tas siapa ini?', 'Whose bag is this?', 'who is', ''),
 ('Pulpen ini milikku.', 'This pen is mine.', 'my me', ''),
 ('Apakah buku itu milikmu?', 'Is that book yours?', 'your you', ''),
])
BAS["quiz"] += mkf([
 ('Sepatu itu milik mereka.', 'The shoes are ___.', 'theirs', 'Theirs.'),
 ('Milik siapa ini?', '___ is this?', 'Whose', 'Whose.'),
])
