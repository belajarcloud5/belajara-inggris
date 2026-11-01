from qk import mk, mkf, mko
PHV = dict(practice=mk([
 ('Pilih phrasal verb yang tepat: "Please ___ two hours early." (lapor masuk)', 'check in', 'show off', 'check off', 'check up on', 'check in = lapor masuk.'),
 ('Pilih phrasal verb yang tepat: "___ by noon." (lapor keluar)', 'Check out', 'Check in', 'Check up', 'Show off', 'check out = lapor keluar.'),
 ('Pilih phrasal verb yang tepat: "The plane ___ at nine." (lepas landas)', 'takes off', 'shows off', 'takes out', 'takes in', 'take off = lepas landas.'),
 ('Pilih phrasal verb yang tepat: "We ___ for the airport." (berangkat)', 'set off', 'fill in', 'give back', 'look after', 'set off = berangkat.'),
 ('Pilih phrasal verb yang tepat: "A driver will ___ you ___." (menjemput)', 'pick / up', 'drop / off', 'call / back', 'wake / up', 'pick up.'),
 ('Pilih phrasal verb yang tepat: "Please ___ me ___ at the hotel." (mengantar)', 'drop / off', 'pick / up', 'call / back', 'wake / up', 'drop off.'),
 ('Pilih kalimat yang SALAH:', "A driver will pick up you.", "A driver will pick you up.", "A driver will pick up the guests.", "A driver will pick the guests up.", "Kata ganti di tengah."),
 ('Pilih kalimat yang SALAH:', "We checked out hotel.", "We checked out of the hotel.", "We checked in at the hotel.", "We checked in early.", "check out of the hotel."),
]) + mkf([
 ("Lapor masuk dua jam lebih awal.", "Check ___ two hours early.", "in", "check in."),
 ("Lapor keluar sebelum tengah hari.", "Check ___ by noon.", "out", "check out."),
 ("Pesawat lepas landas pukul sembilan.", "The plane takes ___ at nine.", "off", "take off."),
 ("Sopir akan menjemput Anda.", "A driver will pick you ___.", "up", "pick up."),
]), quiz=mk([
 ('Pilih phrasal verb yang tepat: "We ___ for the airport at six." (berangkat)', 'set off', 'stand up', 'fill in', 'sit down', 'set off.'),
 ('Pilih phrasal verb yang tepat: "I\'ll ___ you ___ at the gate." (mengantar)', 'drop / off', 'pick / up', 'call / back', 'wake / up', 'drop off.'),
 ('Pilih kalimat yang SALAH:', "Drop off me here.", "Drop me off here.", "Drop off the bags here.", "Drop the bags off here.", "Kata ganti di tengah."),
]) + mkf([
 ("Kami melihat-lihat kota.", "We looked ___ the city.", "around", "look around."),
]))
