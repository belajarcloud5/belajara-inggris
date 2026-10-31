from qk import mko
ORD = dict(practice=mko([('Kamu harus mengerjakan PR.', 'You must do your homework.', "mustn't", ''),
 ('Kamu dilarang berisik di perpustakaan.', "You mustn't make noise in the library.", 'must', ''),
 ('Kamu sebaiknya minum lebih banyak air.', 'You should drink more water.', "shouldn't", ''),
 ('Bolehkah saya masuk?', 'May I come in?', 'Do', ''),
 ('Aku harus pergi sekarang.', 'I have to go now.', 'has', ''),
 ('Dia tidak harus memakai dasi.', "She doesn't have to wear a tie.", "don't", ''),
 ('Jangan buang sampah di sini.', "Don't throw rubbish here.", "Doesn't", '')]), quiz=mko([('Kamu sebaiknya tidak makan terlalu banyak permen.', "You shouldn't eat too much candy.", 'should', ''),
 ('Selalu pakai helm.', 'Always wear a helmet.', 'wears', ''),
 ('Kita dilarang terlambat ke sekolah.', "We mustn't be late for school.", 'must', '')]))
