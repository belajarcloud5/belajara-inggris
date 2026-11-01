from qk import mk, mkf, mko
GER = dict(practice=mk([
 ('Pilih jawaban yang benar: "The teacher lets us ___ dictionaries."', "use", "to use", "using", "used", "let + objek + V1."),
 ('Pilih jawaban yang benar: "The rule makes us ___ uniforms."', "wear", "to wear", "wearing", "wore", "make + objek + V1."),
 ('Pilih jawaban yang benar: "The school allows students ___ phones."', "to bring", "bring", "bringing", "brought", "allow + objek + to V1."),
 ('Pilih jawaban yang benar: "We are allowed ___ here."', "to eat", "eat", "eating", "ate", "be allowed + to V1."),
 ('Pilih jawaban yang benar: "We were made ___ the room."', "to clean", "clean", "cleaning", "cleaned", "be made + to V1."),
 ('Pilih kalimat yang benar:', "She lets me go home early.", "She lets me to go home early.", "She lets me going home early.", "She lets me goes home early.", "let + objek + V1."),
 ('Pilih kalimat yang SALAH:', "He makes us to work hard.", "He makes us work hard.", "He wants us to work hard.", "He lets us work hard.", "make + objek + V1."),
 ('Pilih kalimat yang SALAH:', "She allows me go out.", "She allows me to go out.", "She lets me go out.", "I am allowed to go out.", "allow + objek + to V1."),
]) + mkf([
 ("Guru membolehkan kami memakai kamus.", "The teacher lets us ___ dictionaries.", "use", "let + objek + V1."),
 ("Aturan mewajibkan kami memakai seragam.", "The rule makes us ___ uniforms.", "wear", "make + objek + V1."),
 ("Sekolah mengizinkan murid membawa ponsel.", "The school allows students ___ bring phones.", "to", "allow + objek + to V1."),
 ("Kami diizinkan makan di sini.", "We are allowed ___ eat here.", "to", "be allowed + to V1."),
]), quiz=mk([
 ('Pilih jawaban yang benar: "My parents let me ___ out."', "go", "to go", "going", "went", "let + objek + V1."),
 ('Pilih jawaban yang benar: "They allowed us ___ early."', "to leave", "leave", "leaving", "left", "allow + objek + to V1."),
 ('Pilih kalimat yang SALAH:', "She made me to cry.", "She made me cry.", "She made me laugh.", "She let me cry.", "make + objek + V1."),
]) + mkf([
 ("Mereka membuat kami menunggu.", "They made us ___.", "wait", "make + objek + V1."),
]))
