from qk import mk, mkf, mko
PHV = dict(practice=mk([
 ('Pilih phrasal verb yang tepat: "I ___ at five o\'clock." (terbangun)', 'wake up', 'show off', 'stand up', 'give back', 'wake up = terbangun.'),
 ('Pilih phrasal verb yang tepat: "___ the light, please." (nyalakan)', "Turn on", "Turn off", "Turn up", "Turn out", "turn on = menyalakan."),
 ('Pilih phrasal verb yang tepat: "___ your jacket, it\'s hot." (lepas)', "Take off", "Put on", "Turn on", "Get on", "take off = melepas."),
 ('Pilih phrasal verb yang tepat: "___ your shoes before you go out." (pakai)', "Put on", "Take off", "Turn off", "Get off", "put on = memakai."),
 ('Pilih phrasal verb yang tepat: "I ___ my room every Saturday." (membereskan)', 'clean up', 'sit down', 'stand up', 'hand in', 'clean up = membereskan.'),
 ('Pilih kalimat yang benar:', "Turn it off.", "Turn off it.", "Turn off to it.", "Turn it of.", "Kata ganti di tengah."),
 ('Pilih kalimat yang SALAH:', "Take off it.", "Take it off.", "Take off your coat.", "Take your coat off.", "Kata ganti harus di tengah."),
 ('Pilih kalimat yang SALAH:', "Put on them.", "Put them on.", "Put on your shoes.", "Put your shoes on.", "Kata ganti harus di tengah."),
]) + mkf([
 ("Aku terbangun pukul lima.", "I ___ up at five.", "wake", "wake up."),
 ("Nyalakan lampu.", "Turn ___ the light.", "on", "turn on."),
 ("Lepas jaketmu.", "Take ___ your jacket.", "off", "take off."),
 ("Pakai sepatumu.", "Put ___ your shoes.", "on", "put on."),
]), quiz=mk([
 ('Pilih phrasal verb yang tepat: "___ the TV, please." (matikan)', "Turn off", "Turn on", "Put on", "Get up", "turn off = mematikan."),
 ('Pilih phrasal verb yang tepat: "We ___ on Sunday." (keluar rumah)', 'go out', 'go in', 'go on', 'stand up', 'go out = keluar rumah.'),
 ('Pilih kalimat yang SALAH:', "Turn off it, please.", "Turn it off, please.", "Turn off the radio.", "Turn the radio off.", "Kata ganti di tengah."),
]) + mkf([
 ("Aku bangun dari tempat tidur pukul enam.", "I ___ up at six.", "get", "get up."),
]))
