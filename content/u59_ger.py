from qk import mk, mkf, mko
GER = dict(practice=mk([
 ('Pilih jawaban yang benar: "Keep ___ your ideas."', "sharing", "to share", "share", "shared", "keep + V-ing."),
 ('Pilih jawaban yang benar: "Try to avoid ___ others."', "interrupting", "to interrupt", "interrupt", "interrupted", "avoid + V-ing."),
 ('Pilih jawaban yang benar: "You need ___ deadlines."', "to meet", "meeting", "meet", "met", "need + to V1."),
 ('Pilih jawaban yang benar: "Try ___ for help earlier."', "to ask", "asking", "ask", "asked", "try to + V1 = berusaha."),
 ('Pilih jawaban yang benar: "I am proud of ___ with you."', "working", "to work", "work", "worked", "proud of + V-ing."),
 ('Pilih jawaban yang benar: "Thank you for ___ my report."', "reading", "to read", "read", "reads", "thank you for + V-ing."),
 ('Pilih kalimat yang SALAH:', "Keep to share your ideas.", "Keep sharing your ideas.", "Try to share your ideas.", "Avoid hiding your ideas.", "keep + V-ing."),
 ('Pilih kalimat yang SALAH:', "You need meeting deadlines.", "You need to meet deadlines.", "You should meet deadlines.", "Keep meeting deadlines.", "need + to V1."),
]) + mkf([
 ("Terus bagikan ide-idemu.", "Keep ___ your ideas.", "sharing", "keep + V-ing."),
 ("Kamu perlu memenuhi tenggat waktu.", "You need ___ meet deadlines.", "to", "need + to V1."),
 ("Berusahalah meminta bantuan lebih awal.", "Try ___ ask for help earlier.", "to", "try to + V1."),
 ("Hindari menyela orang lain.", "Avoid ___ others.", "interrupting", "avoid + V-ing."),
]), quiz=mk([
 ('Pilih jawaban yang benar: "Keep ___ and you will improve."', "practising", "to practise", "practise", "practised", "keep + V-ing."),
 ('Pilih jawaban yang benar: "I am proud ___ my team."', "of", "to", "for", "at", "proud of."),
 ('Pilih kalimat yang SALAH:', "Try to avoid to interrupt.", "Try to avoid interrupting.", "Try not to interrupt.", "Avoid interrupting.", "avoid + V-ing."),
]) + mkf([
 ("Aku bangga bekerja denganmu.", "I am proud of ___ with you.", "working", "proud of + V-ing."),
]))
