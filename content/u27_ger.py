from qk import mk, mkf, mko
GER = dict(practice=mk([
 ('Pilih jawaban yang benar: "I am interested in ___ English."', "learning", "to learn", "learn", "learned", "preposition + V-ing."),
 ('Pilih jawaban yang benar: "She is good at ___."', "singing", "to sing", "sing", "sang", "good at + V-ing."),
 ('Pilih jawaban yang benar: "He is bad at ___."', "drawing", "to draw", "draw", "drew", "bad at + V-ing."),
 ('Pilih jawaban yang benar: "I am afraid of ___ in public."', "speaking", "to speak", "speak", "spoke", "afraid of + V-ing."),
 ('Pilih jawaban yang benar: "Thank you for ___ me."', "helping", "to help", "help", "helped", "thank you for + V-ing."),
 ('Pilih jawaban yang benar: "Before ___, I brush my teeth."', "sleeping", "to sleep", "sleep", "slept", "before + V-ing."),
 ('Pilih kalimat yang benar:', "I am good at swimming.", "I am good at to swim.", "I am good at swim.", "I am good at swam.", "good at + V-ing."),
 ('Pilih kalimat yang SALAH:', "She is interested in to learn music.", "She is interested in learning music.", "She is good at playing music.", "She likes music.", "interested in + V-ing."),
]) + mkf([
 ("Aku tertarik belajar bahasa Inggris.", "I am interested in ___ English.", "learning", "interested in + V-ing."),
 ("Dia pandai menyanyi.", "She is good at ___.", "singing", "good at + V-ing."),
 ("Aku takut berbicara di depan umum.", "I am afraid of ___ in public.", "speaking", "afraid of + V-ing."),
 ("Terima kasih telah membantuku.", "Thank you for ___ me.", "helping", "thank you for + V-ing."),
]), quiz=mk([
 ('Pilih jawaban yang benar: "He is good at ___ football."', "playing", "to play", "play", "played", "good at + V-ing."),
 ('Pilih jawaban yang benar: "After ___ lunch, we went out."', "eating", "to eat", "eat", "ate", "after + V-ing."),
 ('Pilih kalimat yang SALAH:', "I am good at to cook.", "I am good at cooking.", "I am interested in cooking.", "I like cooking.", "good at + V-ing."),
]) + mkf([
 ("Sebelum pergi, matikan lampu.", "Before ___, turn off the lights.", "leaving", "before + V-ing."),
]))
