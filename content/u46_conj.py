from qk import mk, mkf, mko
CONJ = dict(practice=mk([
 ('Pilih jawaban yang benar: "We stayed home ___ it rained."', "because", "because of", "despite", "although", "because + klausa."),
 ('Pilih jawaban yang benar: "We stayed home ___ the rain."', "because of", "because", "although", "unless", "because of + kata benda."),
 ('Pilih jawaban yang benar: "___ he was tired, he worked hard."', "Although", "Despite", "Because of", "Unless", "Although + klausa."),
 ('Pilih jawaban yang benar: "___ being tired, he worked hard."', "Despite", "Although", "Because", "Unless", "Despite + V-ing."),
 ('Pilih jawaban yang benar: "She is ___ smart and kind."', "both", "either", "neither", "not only", "both ... and."),
 ('Pilih jawaban yang benar: "You can ___ stay here or go home."', "either", "both", "neither", "so", "either ... or."),
 ('Pilih jawaban yang benar: "___ Anna nor Budi knows the answer."', "Neither", "Either", "Both", "Not", "neither ... nor."),
 ('Pilih jawaban yang benar: "___ you hurry, you will be late."', "Unless", "Although", "Despite", "Whereas", "Kecuali → unless."),
 ('Pilih kalimat yang SALAH:', "Although it is cheap, but I won't buy it.", "Although it is cheap, I won't buy it.", "It is cheap, but I won't buy it.", "Despite being cheap, I won't buy it.", "Although dan but tidak dipakai bersamaan."),
 ('Pilih kalimat yang SALAH:', "Unless you don't hurry, you will be late.", "Unless you hurry, you will be late.", "If you don't hurry, you will be late.", "You will be late unless you hurry.", "Unless sudah negatif."),
 ('Pilih kalimat yang benar:', "Neither he nor I know the answer.", "Neither he or I know the answer.", "Neither he nor I doesn't know the answer.", "Either he nor I know the answer.", "neither ... nor tanpa negatif tambahan."),
 ('Pilih kalimat yang SALAH:', "Despite it was late, we continued.", "Despite the late hour, we continued.", "Although it was late, we continued.", "In spite of the delay, we continued.", "Despite tidak diikuti klausa."),
]) + mkf([
 ("Kami tinggal di rumah karena hujan.", "We stayed home ___ of the rain.", "because", "because of + kata benda."),
 ("Dia pintar dan juga baik.", "She is ___ smart and kind.", "both", "both ... and."),
 ("Baik Anna maupun Budi tidak tahu.", "___ Anna nor Budi knows.", "Neither", "neither ... nor."),
 ("Kecuali kamu bergegas, kamu akan terlambat.", "___ you hurry, you will be late.", "Unless", "unless = kecuali."),
]), quiz=mk([
 ('Pilih jawaban yang benar: "I was ill, ___ I stayed home."', "so", "because", "although", "despite", "Akibat → so."),
 ('Pilih jawaban yang benar: "I stayed home ___ I was ill."', "because", "so", "despite", "unless", "Alasan → because."),
 ('Pilih jawaban yang benar: "___ the heavy traffic, we arrived on time."', "Despite", "Although", "Because", "Unless", "Despite + kata benda."),
 ('Pilih jawaban yang benar: "___ the traffic was heavy, we arrived on time."', "Although", "Despite", "Because of", "Unless", "Although + klausa."),
]) + mkf([
 ("Pilih salah satu: teh atau kopi.", "You can have ___ tea or coffee.", "either", "either ... or."),
 ("Meskipun capek, dia bekerja.", "___ he was tired, he worked.", "Although/Though", "Although + klausa."),
]))
