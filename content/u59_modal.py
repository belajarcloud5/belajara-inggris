from qk import mk, mkf, mko
MODAL = dict(practice=mk([
 ('Pilih saran yang paling lembut:', "You might want to add more examples.", "You must add more examples.", "Add more examples.", "You need to add more examples.", "might want to = lembut."),
 ('Pilih saran yang paling kuat:', "You need to meet the deadline.", "You could meet the deadline.", "You might meet the deadline.", "Maybe meet the deadline.", "need to = kuat."),
 ('Pilih jawaban yang benar: "You ___ ask for help if you need it." (saran sedang)', "should", "might to", "can't", "mustn't", "Saran → should."),
 ('Pilih jawaban yang benar: "You ___ start earlier. That would help." (saran lembut)', "could", "must to", "had better to", "needn't to", "Saran lembut → could."),
 ('Pilih jawaban yang benar: "I\'ll ___ to be more careful."', "try", "tries", "trying", "tried", "I'll + V1."),
 ('Pilih kalimat yang benar:', "You should check the numbers again.", "You should to check the numbers again.", "You should checking the numbers again.", "You shoulds check the numbers again.", "should + V1."),
 ('Pilih kalimat yang SALAH:', "You might want adding a summary.", "You might want to add a summary.", "You could add a summary.", "You should add a summary.", "might want to + V1."),
]) + mkf([
 ("Anda mungkin perlu menambah contoh.", "You might ___ to add examples.", "want", "might want to."),
 ("Sebaiknya Anda memeriksa angkanya lagi.", "You ___ check the numbers again.", "should", "should + V1."),
 ("Saya akan berusaha lebih hati-hati.", "I'll ___ to be more careful.", "try", "I'll try to."),
 ("Anda perlu memenuhi tenggat waktu.", "You ___ to meet the deadline.", "need", "need to."),
]), quiz=mk([
 ('Pilih saran yang paling lembut:', "You could start earlier.", "You must start earlier.", "Start earlier now.", "You have to start earlier.", "could = lembut."),
 ('Pilih jawaban yang benar: "You ___ check your email more often." (saran)', "should", "should to", "shoulds", "shouldn't to", "should + V1."),
 ('Pilih kalimat yang SALAH:', "You could to add examples.", "You could add examples.", "You should add examples.", "You might add examples.", "could tanpa to."),
]) + mkf([
 ("Sebaiknya Anda minta bantuan.", "You ___ ask for help.", "should", "should + V1."),
]))
