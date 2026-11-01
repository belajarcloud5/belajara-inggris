from qk import mk, mkf, mko
CMP = dict(practice=mk([
 ('Pilih jawaban yang benar: "He runs ___ than me."', "faster", "more fast", "fastest", "fast", "fast → faster."),
 ('Pilih jawaban yang benar: "She speaks ___ clearly than him."', "more", "most", "much", "very", "-ly adverb → more."),
 ('Pilih jawaban yang benar: "He sings ___ than me." (lebih baik)', "better", "gooder", "more well", "best", "well → better."),
 ('Pilih jawaban yang benar: "She works ___ of all." (paling keras)', "the hardest", "harder", "most hard", "more hardly", "hard → the hardest."),
 ('Pilih jawaban yang benar: "She works as carefully ___ he does."', "as", "than", "like", "from", "as ... as."),
 ('Pilih kalimat yang SALAH:', "He drives more careful than me.", "He drives more carefully than me.", "He is a more careful driver.", "He drives as carefully as me.", "Adverbia: more carefully."),
 ('Pilih kalimat yang SALAH:', "She speaks English more good than me.", "She speaks English better than me.", "She speaks English well.", "She speaks English the best.", "well → better."),
]) + mkf([
 ("Dia berlari lebih cepat daripada aku.", "He runs ___ than me.", "faster", "fast → faster."),
 ("Dia berbicara lebih jelas daripada dia.", "She speaks ___ clearly than him.", "more", "-ly adverb → more."),
 ("Dia bernyanyi lebih baik daripada aku.", "He sings ___ than me.", "better", "well → better."),
 ("Dia bekerja paling keras.", "She works the ___.", "hardest", "hard → the hardest."),
]), quiz=mk([
 ('Pilih jawaban yang benar: "He arrived ___ than me." (lebih awal)', "earlier", "more early", "earliest", "early", "early → earlier."),
 ('Pilih jawaban yang benar: "She walks ___ slowly than me."', "more", "most", "much", "very", "-ly adverb → more."),
 ('Pilih kalimat yang SALAH:', "He works more hard than me.", "He works harder than me.", "He works the hardest.", "He works as hard as me.", "hard → harder."),
]) + mkf([
 ("Paus menyelam paling dalam.", "Whales dive the ___.", "deepest", "deep → the deepest."),
]))
