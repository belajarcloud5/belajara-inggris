from qk import mk, mkf, mko
GER = dict(practice=mk([
 ('Pilih jawaban yang benar: "Use a knife ___ the bread."', "to cut", "for cut", "cutting", "cut", "Tujuan → to V1."),
 ('Pilih jawaban yang benar: "Boil the water in order ___ the germs."', "to kill", "killing", "kill", "for kill", "in order to + V1."),
 ('Pilih jawaban yang benar: "Stir slowly so as ___ spilling."', "to avoid", "avoiding", "avoid", "avoided", "so as to + V1."),
 ('Pilih jawaban yang benar: "A kettle is used for ___ water."', "boiling", "to boil", "boil", "boiled", "for + V-ing."),
 ('Pilih jawaban yang benar: "Press the button ___ the machine on."', "to turn", "for turn", "turning", "turn", "Tujuan → to V1."),
 ('Pilih kalimat yang benar:', "I use a spoon to stir.", "I use a spoon for to stir.", "I use a spoon for stir.", "I use a spoon to stirring.", "Tujuan → to V1."),
 ('Pilih kalimat yang SALAH:', "A spoon is used to stirring.", "A spoon is used for stirring.", "A spoon is used to stir.", "I use a spoon to stir.", "used for + V-ing."),
]) + mkf([
 ("Pakai pisau untuk memotong roti.", "Use a knife ___ cut the bread.", "to", "Tujuan → to V1."),
 ("Rebus air untuk membunuh kuman.", "Boil the water in ___ to kill the germs.", "order", "in order to + V1."),
 ("Ketel dipakai untuk merebus air.", "A kettle is used for ___ water.", "boiling", "for + V-ing."),
 ("Aduk pelan-pelan agar tidak tumpah.", "Stir slowly so as ___ avoid spilling.", "to", "so as to + V1."),
]), quiz=mk([
 ('Pilih jawaban yang benar: "I went to the shop ___ some milk."', "to buy", "for buy", "buying", "bought", "Tujuan → to V1."),
 ('Pilih jawaban yang benar: "A pen is used for ___."', "writing", "to write", "write", "wrote", "for + V-ing."),
 ('Pilih kalimat yang SALAH:', "She came here for to learn.", "She came here to learn.", "She came here in order to learn.", "She came here for the lesson.", "Tujuan → to V1."),
]) + mkf([
 ("Tekan tombol untuk menyalakan mesin.", "Press the button ___ turn on the machine.", "to", "Tujuan → to V1."),
]))
