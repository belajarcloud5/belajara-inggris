from qk import mk, mkf, mko
GER = dict(practice=mk([
 ('Pilih jawaban yang benar: "I look forward to ___ from you."', "hearing", "hear", "heard", "to hear", "look forward to + V-ing."),
 ('Pilih jawaban yang benar: "I am able ___ under pressure."', "to work", "working", "work", "worked", "be able to + V1."),
 ('Pilih jawaban yang benar: "I am willing ___ new skills."', "to learn", "learning", "learn", "learned", "be willing to + V1."),
 ('Pilih jawaban yang benar: "I am interested in ___ for your company."', "working", "to work", "work", "worked", "interested in + V-ing."),
 ('Pilih jawaban yang benar: "I would like ___ for the position."', "to apply", "applying", "apply", "applied", "would like + to V1."),
 ('Pilih kalimat yang benar:', "I look forward to meeting you.", "I look forward to meet you.", "I look forward meeting you.", "I look forward to met you.", "to adalah preposition → V-ing."),
 ('Pilih kalimat yang SALAH:', "I look forward to hear from you.", "I look forward to hearing from you.", "I would like to hear from you.", "I am happy to hear from you.", "look forward to + V-ing."),
]) + mkf([
 ("Saya menantikan kabar dari Anda.", "I look forward to ___ from you.", "hearing", "look forward to + V-ing."),
 ("Saya mampu bekerja di bawah tekanan.", "I am able ___ work under pressure.", "to", "be able to + V1."),
 ("Saya tertarik bekerja di perusahaan Anda.", "I am interested in ___ for your company.", "working", "interested in + V-ing."),
 ("Saya ingin melamar posisi itu.", "I would like ___ apply for the position.", "to", "would like + to V1."),
]), quiz=mk([
 ('Pilih jawaban yang benar: "I look forward to ___ you."', "meeting", "meet", "met", "to meet", "look forward to + V-ing."),
 ('Pilih jawaban yang benar: "I am happy ___ more details."', "to provide", "providing", "provide", "provided", "happy to + V1."),
 ('Pilih kalimat yang SALAH:', "I am interested to working here.", "I am interested in working here.", "I would like to work here.", "I am able to work here.", "interested in + V-ing."),
]) + mkf([
 ("Saya senang membantu Anda.", "I am happy ___ help you.", "to", "happy to + V1."),
]))
