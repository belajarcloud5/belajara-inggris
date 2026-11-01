from qk import mk, mkf, mko
PHV = dict(practice=mk([
 ('Pilih phrasal verb yang tepat: "___ the bus at the corner." (naik)', "Get on", "Get off", "Get up", "Get out", "get on = naik."),
 ('Pilih phrasal verb yang tepat: "___ at the station." (turun)', "Get off", "Get on", "Get up", "Get in", "get off = turun (bus/kereta)."),
 ('Pilih phrasal verb yang tepat: "We ___ at six." (berangkat)', "set off", "set in", "set up", "set on", "set off = berangkat."),
 ('Pilih phrasal verb yang tepat: "It\'s too late. Let\'s ___." (kembali)', "turn back", "turn on", "turn off", "turn up", "turn back = kembali."),
 ('Pilih phrasal verb yang tepat: "I\'ll ___ you at the station." (menjemput)', "pick up", "pick on", "pick in", "pick down", "pick up = menjemput."),
 ('Pilih phrasal verb yang tepat: "Please ___ me here." (menurunkan)', "drop off", "drop on", "drop in", "drop at", "drop off = menurunkan."),
 ('Pilih kalimat yang benar:', "I\'ll pick you up at five.", "I\'ll pick up you at five.", "I\'ll pick at you five.", "I\'ll pick you at up five.", "Kata ganti di tengah."),
 ('Pilih kalimat yang SALAH:', "Please drop off me here.", "Please drop me off here.", "Please drop the box off here.", "Please drop off the box here.", "Kata ganti di tengah."),
]) + mkf([
 ("Naiklah bus itu.", "Get ___ the bus.", "on", "get on."),
 ("Turun di stasiun.", "Get ___ at the station.", "off", "get off."),
 ("Kami berangkat pukul enam.", "We set ___ at six.", "off", "set off."),
 ("Aku akan menjemputmu.", "I'll pick you ___.", "up", "pick up."),
]), quiz=mk([
 ('Pilih phrasal verb yang tepat: "Go straight ___ for two blocks." (terus)', "on", "off", "up", "out", "go straight on = terus lurus."),
 ('Pilih phrasal verb yang tepat: "Please ___ me ___ at the hotel."', "drop / off", "pick / up", "turn / on", "set / off", "drop me off."),
 ('Pilih kalimat yang SALAH:', "Get the train off here.", "Get off the train here.", "Get on the train there.", "Get off at Bandung.", "get off the train."),
]) + mkf([
 ("Ayo kembali.", "Let's turn ___.", "back", "turn back."),
]))
