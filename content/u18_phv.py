from qk import mk, mkf, mko
PHV = dict(practice=mk([
 ('Pilih phrasal verb yang tepat: "I hope you ___ soon." (membaik)', "get better", "get on", "get off", "get up", "get better = membaik."),
 ('Pilih phrasal verb yang tepat: "She ___ the flu." (terkena)', 'came down with', 'came up with', 'stood up', 'sat down', 'come down with = jatuh sakit.'),
 ('Pilih phrasal verb yang tepat: "You should ___ sugar." (mengurangi)', "cut down on", "cut up", "cut off", "cut in", "cut down on = mengurangi."),
 ('Pilih phrasal verb yang tepat: "He ___ smoking." (berhenti)', "gave up", "gave in", "gave out", "gave away", "give up = berhenti."),
 ('Pilih phrasal verb yang tepat: "I ___ every morning." (berolahraga)', 'work out', 'work on', 'stand up', 'work off', 'work out = berolahraga.'),
 ('Pilih phrasal verb yang tepat: "___ of yourself." (jaga)', "Take care", "Take off", "Take out", "Take up", "take care of."),
 ('Pilih kalimat yang benar:', "He gave it up.", "He gave up it.", "He gave to it up.", "He up gave it.", "Kata ganti di tengah."),
 ('Pilih kalimat yang SALAH:', "She came down for the flu.", "She came down with the flu.", "She got the flu.", "She caught the flu.", "come down with."),
]) + mkf([
 ("Semoga kamu cepat membaik.", "I hope you get ___ soon.", "better", "get better."),
 ("Kamu sebaiknya mengurangi gula.", "You should cut ___ on sugar.", "down", "cut down on."),
 ("Dia berhenti merokok.", "He gave ___ smoking.", "up", "give up."),
 ("Aku berolahraga setiap pagi.", "I work ___ every morning.", "out", "work out."),
]), quiz=mk([
 ('Pilih phrasal verb yang tepat: "She ___ a cold last week." (terkena)', 'came down with', 'came up with', 'gave back', 'sat down', 'come down with.'),
 ('Pilih phrasal verb yang tepat: "Please ___ of the baby." (menjaga)', "take care", "take off", "take out", "take up", "take care of."),
 ('Pilih kalimat yang SALAH:', "He gave up it.", "He gave it up.", "He gave up smoking.", "He gave up his job.", "Kata ganti di tengah."),
]) + mkf([
 ("Jaga dirimu.", "Take care ___ yourself.", "of", "take care of."),
]))
