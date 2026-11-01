from qk import mk, mkf, mko
PHV = dict(practice=mk([
 ('Pilih phrasal verb yang tepat: "___ the onions." (potong-potong)', "Cut up", "Cut on", "Cut at", "Cut off", "cut up = memotong-motong."),
 ('Pilih phrasal verb yang tepat: "___ the sugar." (campurkan)', "Mix in", "Mix out", "Mix off", "Mix on", "mix in = mencampurkan."),
 ('Pilih phrasal verb yang tepat: "___ the water." (tuang keluar)', "Pour out", "Pour in", "Pour on", "Pour at", "pour out = menuang keluar."),
 ('Pilih phrasal verb yang tepat: "___ two eggs." (masukkan)', "Put in", "Put out", "Put off", "Put at", "put in = memasukkan."),
 ('Pilih phrasal verb yang tepat: "___ the cake from the oven." (keluarkan)', "Take out", "Take in", "Take on", "Take at", "take out = mengeluarkan."),
 ('Pilih phrasal verb yang tepat: "___ the pancake." (balik)', "Turn over", "Turn on", "Turn off", "Turn at", "turn over = membalik."),
 ('Pilih kalimat yang benar:', "Turn it over.", "Turn over it.", "Turn it to over.", "Turn over to it.", "Kata ganti di tengah."),
 ('Pilih kalimat yang SALAH:', "Take out them.", "Take them out.", "Take out the cakes.", "Take the cakes out.", "Kata ganti di tengah."),
]) + mkf([
 ("Potong-potong bawangnya.", "Cut ___ the onions.", "up", "cut up."),
 ("Masukkan dua telur.", "Put ___ two eggs.", "in", "put in."),
 ("Keluarkan kuenya.", "Take ___ the cake.", "out", "take out."),
 ("Balik panekuknya.", "Turn the pancake ___.", "over", "turn over."),
]), quiz=mk([
 ('Pilih phrasal verb yang tepat: "___ the milk." (campurkan)', "Mix in", "Mix off", "Mix at", "Mix on", "mix in."),
 ('Pilih phrasal verb yang tepat: "___ the rice into the pot." (tuang)', "Pour", "Pour off", "Pour on", "Pour at", "pour into."),
 ('Pilih kalimat yang SALAH:', "Cut up them.", "Cut them up.", "Cut up the onions.", "Cut the onions up.", "Kata ganti di tengah."),
]) + mkf([
 ("Tuang airnya keluar.", "Pour ___ the water.", "out", "pour out."),
]))
