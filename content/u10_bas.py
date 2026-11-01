from qk import mk, mkf, mko
BAS = dict(practice=mk([
 ('Pilih yang tepat: "I ___ play football every day, but now I am busy."', 'used to', 'use to', 'am used to', 'was used', 'Kebiasaan lampau → used to.'),
 ('Pilih yang tepat: "She ___ like fish, but now she loves it."', 'didn\'t use to', 'didn\'t used to', 'doesn\'t use to', 'wasn\'t use to', 'Negatif → didn\'t use to.'),
 ('Pilih yang tepat: "___ you use to live here?"', 'Did', 'Do', 'Were', 'Have', 'Tanya lampau → Did.'),
 ('Pilih kalimat yang benar:', 'We used to live in Medan.', 'We use to live in Medan.', 'We used to living in Medan.', 'We used to lived in Medan.', 'Used to + V1.'),
 ('Pilih kalimat yang benar:', 'Did he use to play the guitar?', 'Did he used to play the guitar?', 'Does he use to play the guitar?', 'Did he use to playing the guitar?', 'Did + use to.'),
 ('Pilih kalimat yang benar:', 'I didn\'t use to like coffee.', 'I didn\'t used to like coffee.', 'I not use to like coffee.', 'I didn\'t use to liked coffee.', 'Didn\'t + use to.'),
 ('Pilih kalimat yang SALAH:', 'He didn\'t used to smoke.', 'He used to smoke.', 'He didn\'t use to smoke.', 'Did he use to smoke?', 'Setelah didn\'t: use to.'),
 ('Pilih kalimat yang SALAH:', 'They used to going to the beach.', 'They used to go to the beach.', 'They didn\'t use to go to the beach.', 'Did they use to go to the beach?', 'Used to + V1, bukan V-ing.'),
 ('Apa arti "I used to be shy"?', 'Dulu saya pemalu (sekarang tidak).', 'Saya sedang pemalu.', 'Saya akan menjadi pemalu.', 'Saya selalu pemalu.', 'Used to = kebiasaan lampau.'),
 ('Pilih yang tepat: "I am used to ___ up early." (terbiasa)', 'getting', 'get', 'got', 'gets', 'be used to + V-ing = terbiasa.'),
 ('Kalimat mana yang menyatakan kebiasaan LAMPAU?', 'I used to walk to school.', 'I am used to walking to school.', 'I walk to school.', 'I will walk to school.', 'Used to + V1.'),
 ('Kalimat mana yang menyatakan TERBIASA?', 'I am used to the noise.', 'I used to the noise.', 'I use to the noise.', 'I used to hear the noise.', 'Be used to + benda/V-ing.'),
 ('Pilih yang tepat: "When I was a child, I ___ climb trees."', 'used to', 'am used to', 'was use to', 'use to', 'Masa kecil → used to.'),
 ('Pilih yang tepat: "There ___ be a cinema here, but now it is a shop."', 'used to', 'use to', 'is used to', 'are used', 'Keadaan lampau → used to be.'),
 ('Pilih kalimat yang benar:', 'Dina used to have long hair.', 'Dina use to have long hair.', 'Dina used to has long hair.', 'Dina used to had long hair.', 'Used to + have.'),
]), quiz=mk([
 ('Pilih yang tepat: "My father ___ work in a bank."', 'used to', 'use to', 'is used', 'was use to', 'Dulu bekerja → used to.'),
 ('Pilih yang tepat: "We ___ have a car, so we walked."', 'didn\'t use to', 'didn\'t used to', 'don\'t use to', 'weren\'t used to', 'Negatif → didn\'t use to.'),
 ('Pilih kalimat yang benar:', 'Did you use to read comics?', 'Did you used to read comics?', 'Do you used to read comics?', 'Did you use to reading comics?', 'Did + use to.'),
 ('Pilih kalimat yang SALAH:', 'She used to walking here.', 'She used to walk here.', 'She didn\'t use to walk here.', 'Did she use to walk here?', 'V1 setelah used to.'),
 ('Pilih yang tepat: "I\'m not used to ___ spicy food." (terbiasa)', 'eating', 'eat', 'ate', 'eaten', 'Be used to + V-ing.'),
 ('Apa arti "We used to play here"?', 'Dulu kami bermain di sini.', 'Kami selalu bermain di sini.', 'Kami akan bermain di sini.', 'Kami sedang bermain di sini.', 'Kebiasaan lampau.'),
]))
BAS["practice"] += mkf([
 ('Dulu aku bermain sepak bola.', 'I ___ to play football.', 'used', 'Used to = dulu.'),
 ('Dulu dia tidak suka ikan.', "She didn't ___ to like fish.", 'use', 'Setelah didn\'t: use to.'),
 ('Apakah dulu kamu tinggal di sini?', 'Did you ___ to live here?', 'use', 'Setelah did: use to.'),
 ('Aku terbiasa bangun pagi.', 'I am used to ___ up early.', 'getting', 'Be used to + V-ing.'),
 ('Dulu mereka tinggal di Medan.', 'They used to ___ in Medan.', 'live', 'Used to + V1.'),
])
BAS["practice"] += mko([
 ('Dulu kami tinggal di Medan.', 'We used to live in Medan.', 'use living', ''),
 ('Dia tidak suka ikan dulu.', "She didn't use to like fish.", 'used liked', ''),
 ('Apakah dulu kamu bermain gitar?', 'Did you use to play the guitar?', 'used played', ''),
])
BAS["quiz"] += mkf([
 ('Dulu dia pemalu.', 'He ___ to be shy.', 'used', 'Used to be.'),
 ('Apakah dulu dia tinggal di sini?', 'Did she ___ to live here?', 'use', 'Did + use to.'),
])
