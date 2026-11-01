from qk import mk, mkf, mko
CMP = dict(practice=mk([
 ('Pilih jawaban yang benar: "She is ___ than me."', "taller", "more tall", "tallest", "more taller", "-er + than."),
 ('Pilih jawaban yang benar: "This is ___ expensive of all."', "the most", "more", "most", "the more", "the most + adj."),
 ('Pilih jawaban yang benar: "He is taller ___ me."', "than", "then", "that", "as", "than."),
 ('Pilih jawaban yang benar: "This phone is ___ better than that one." (jauh)', "much", "very", "most", "too", "much + comparative."),
 ('Pilih jawaban yang benar: "The ___ you practise, the better you become."', "more", "most", "much", "many", "the more ..., the better."),
 ('Pilih jawaban yang benar: "He is as tall ___ his father."', "as", "than", "then", "like", "as ... as."),
 ('Pilih jawaban yang benar: "She is the ___ student in the class." (terbaik)', "best", "better", "good", "most good", "good → better → best."),
 ('Pilih kalimat yang SALAH:', "She is more taller than me.", "She is taller than me.", "She is the tallest.", "She is as tall as me.", "Jangan dobel."),
 ('Pilih kalimat yang SALAH:', "He is the more intelligent student.", "He is the most intelligent student.", "He is more intelligent than me.", "He is as intelligent as me.", "Superlatif: the most."),
 ('Pilih kalimat yang SALAH:', "It is very faster than before.", "It is much faster than before.", "It is a lot faster than before.", "It is far faster than before.", "Jangan very + comparative."),
]) + mkf([
 ("Dia lebih tinggi daripada aku.", "She is ___ than me.", "taller", "-er + than."),
 ("Ini yang paling mahal.", "This is the ___ expensive.", "most", "the most + adj."),
 ("Dia setinggi ayahnya.", "He is as tall ___ his father.", "as", "as ... as."),
 ("Dia murid terbaik di kelas.", "She is the ___ student in the class.", "best", "good → better → best."),
]), quiz=mk([
 ('Pilih jawaban yang benar: "This is the ___ chair I have ever sat on." (ternyaman)', "most comfortable", "more comfortable", "comfortablest", "most comfort", "the most + adj."),
 ('Pilih jawaban yang benar: "He is ___ than his brother." (lebih tua)', "older", "oldest", "more old", "the older", "-er + than."),
 ('Pilih kalimat yang SALAH:', "She is more better than me.", "She is better than me.", "She is the best.", "She is as good as me.", "Jangan dobel."),
 ('Pilih jawaban yang benar: "Life is getting more and ___ difficult."', "more", "most", "much", "many", "more and more."),
]) + mkf([
 ("Dia berlari lebih cepat daripada aku.", "He runs ___ than me.", "faster", "fast → faster."),
 ("Ini jauh lebih baik.", "This is ___ better.", "much/far", "much atau far."),
]))
