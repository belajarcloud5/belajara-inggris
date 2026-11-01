from qk import mk, mkf, mko
BAS = dict(practice=mk([
 ('Pilih yang tepat: "This tea is ___ hot to drink."', 'too', 'enough', 'very much', 'so', 'Terlalu panas untuk diminum → too.'),
 ('Pilih yang tepat: "Is the room big ___ for ten people?"', 'enough', 'too', 'much', 'very', 'Cukup besar → big enough.'),
 ('Pilih kalimat yang benar:', 'She is tall enough to reach the shelf.', 'She is enough tall to reach the shelf.', 'She is too tall enough to reach the shelf.', 'She is enough tall for reach the shelf.', 'Adjective + enough.'),
 ('Pilih kalimat yang benar:', 'He is too tired to study.', 'He is too tired for study.', 'He is too much tired to study.', 'He is very tired to study.', 'Too + adjective + to V1.'),
 ('Pilih kalimat yang benar:', 'The box is not light enough.', 'The box is not enough light.', 'The box is not too light.', 'The box not light enough is.', 'Not + adjective + enough.'),
 ('Pilih kalimat yang SALAH:', 'The bag is enough big.', 'The bag is big enough.', 'The bag is too big.', 'The bag is not big enough.', 'Enough setelah kata sifat.'),
 ('Pilih kalimat yang SALAH:', 'It is too much cold today.', 'It is too cold today.', 'It is cold enough today.', 'It is not cold enough today.', 'Too + adjective, tanpa much.'),
 ('Apa arti "The soup is too salty"?', 'Supnya terlalu asin.', 'Supnya cukup asin.', 'Supnya tidak asin.', 'Supnya sedikit asin.', 'Too = terlalu (berlebihan).'),
 ('Apa arti "The soup is salty enough"?', 'Supnya sudah cukup asin.', 'Supnya terlalu asin.', 'Supnya tidak asin.', 'Supnya akan asin.', 'Enough = cukup.'),
 ('Pilih yang tepat: "He is old ___ to drive."', 'enough', 'too', 'very', 'so', 'Cukup umur → old enough.'),
 ('Pilih yang tepat: "The test was ___ difficult for me. I failed."', 'too', 'enough', 'very', 'so', 'Hasil buruk → too.'),
 ('Pilih yang tepat: "I can\'t buy it. It is ___ expensive."', 'too', 'enough', 'much', 'less', 'Tidak bisa beli → too expensive.'),
 ('Pilih yang tepat: "We have ___ chairs for everyone."', 'enough', 'a enough', 'too enough', 'much enough', 'Enough di depan benda.'),
 ('Pilih kalimat yang benar:', 'The water is too hot to touch.', 'The water is hot too to touch.', 'The water is too hot for touch.', 'The water is hot enough too to touch.', 'Too + adjective + to V1.'),
 ('Pilih pasangan yang sama artinya: "He is too young to drive" =', 'He is not old enough to drive.', 'He is old enough to drive.', 'He is very old to drive.', 'He is enough young to drive.', 'Too young = not old enough.'),
]), quiz=mk([
 ('Pilih yang tepat: "The bus is ___ crowded. I can\'t get on."', 'too', 'enough', 'much', 'less', 'Penuh sesak → too.'),
 ('Pilih yang tepat: "Is your English good ___ to work here?"', 'enough', 'too', 'very', 'much', 'Good enough.'),
 ('Pilih kalimat yang benar:', 'She runs fast enough to win.', 'She runs enough fast to win.', 'She runs too fast enough to win.', 'She runs too fast for win.', 'Adverb + enough.'),
 ('Pilih kalimat yang SALAH:', 'The shirt is enough small.', 'The shirt is small enough.', 'The shirt is too small.', 'The shirt is not small enough.', 'Enough setelah kata sifat.'),
 ('Pilih yang tepat: "It is ___ late to call him now."', 'too', 'enough', 'much', 'very', 'Terlalu malam → too late.'),
 ('Apa arti "She is not tall enough"?', 'Dia kurang tinggi.', 'Dia terlalu tinggi.', 'Dia sangat tinggi.', 'Dia cukup tinggi.', 'Not ... enough = kurang.'),
]))
BAS["practice"] += mkf([
 ('Tehnya terlalu panas.', 'The tea is ___ hot.', 'too', 'Too = terlalu.'),
 ('Tasnya cukup besar.', 'The bag is big ___.', 'enough', 'Enough setelah kata sifat.'),
 ('Dia cukup tua untuk menyetir.', 'He is old ___ to drive.', 'enough', 'Old enough.'),
 ('Dia terlalu lelah untuk belajar.', 'She is too tired ___ study.', 'to', 'Too + adjective + to V1.'),
 ('Kamarnya tidak cukup besar.', 'The room is not big ___.', 'enough', 'Not big enough.'),
])
BAS["practice"] += mko([
 ('Tehnya terlalu panas untuk diminum.', 'The tea is too hot to drink.', 'enough very', ''),
 ('Dia cukup tinggi.', 'She is tall enough.', 'too much', ''),
 ('Tasnya tidak cukup besar.', 'The bag is not big enough.', 'too very', ''),
])
BAS["quiz"] += mkf([
 ('Ini terlalu mahal.', 'It is ___ expensive.', 'too', 'Too = terlalu.'),
 ('Apakah ini cukup besar?', 'Is it big ___?', 'enough', 'Big enough.'),
])
