from qk import mk, mkf, mko
PHV = dict(practice=mk([
 ('Pilih jawaban yang benar: "Please ___ the light." (matikan)', "turn off", "turn on", "turn up", "turn in", "turn off = mematikan."),
 ('Pilih jawaban yang benar: "She ___ after her little brother." (menjaga)', "looks", "gets", "puts", "takes", "look after = menjaga."),
 ('Pilih jawaban yang benar: "Never ___ up." (menyerah)', "give", "put", "turn", "look", "give up = menyerah."),
 ('Pilih jawaban yang benar: "Please ___ the trash." (keluarkan)', "take out", "take on", "take after", "take over", "take out."),
 ('Pilih jawaban yang benar: "I look ___ to seeing you." (menantikan)', "forward", "after", "for", "up", "look forward to."),
 ('Pilih jawaban yang benar: "I get ___ with my sister." (akrab)', "on", "off", "out", "over", "get on with."),
 ('Pilih kalimat yang benar:', "Turn it off.", "Turn off it.", "Turn off to it.", "Turn it of.", "Kata ganti di tengah."),
 ('Pilih kalimat yang SALAH:', "Look the baby after.", "Look after the baby.", "Look after her.", "She looks after him.", "look after tidak dipisah."),
 ('Pilih kalimat yang SALAH:', "She picked up it.", "She picked it up.", "She picked up the phone.", "She picked the phone up.", "Kata ganti di tengah."),
 ('Pilih kalimat yang SALAH:', "He gave up it.", "He gave it up.", "He gave up smoking.", "He gave up his job.", "Kata ganti di tengah."),
]) + mkf([
 ("Matikan lampunya.", "Turn ___ the light.", "off", "turn off."),
 ("Dia menjaga adiknya.", "She looks ___ her brother.", "after", "look after."),
 ("Jangan pernah menyerah.", "Never give ___.", "up", "give up."),
 ("Aku menantikan bertemu denganmu.", "I look forward ___ seeing you.", "to", "look forward to."),
]), quiz=mk([
 ('Pilih jawaban yang benar: "I\'ll ___ you up at five." (menjemput)', "pick", "put", "get", "turn", "pick up."),
 ('Pilih jawaban yang benar: "We ran ___ of milk." (kehabisan)', "out", "off", "up", "in", "run out of."),
 ('Pilih kalimat yang SALAH:', "Take off them.", "Take them off.", "Take off your shoes.", "Take your shoes off.", "Kata ganti di tengah."),
]) + mkf([
 ("Kami kehabisan susu.", "We ran ___ of milk.", "out", "run out of."),
 ("Dia mengambil telepon.", "She picked ___ the phone.", "up", "pick up."),
]))
