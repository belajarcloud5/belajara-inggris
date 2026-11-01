from qk import mk, mkf, mko
MODAL = dict(practice=mk([
 ('Pilih jawaban yang benar: "She can ___ well."', "swim", "swims", "to swim", "swimming", "Setelah modal, V1."),
 ('Pilih jawaban yang benar: "You ___ smoke here. It is forbidden."', "mustn't", "don't have to", "needn't", "ought to", "Dilarang → mustn't."),
 ('Pilih jawaban yang benar: "You ___ come tomorrow. It is optional."', "don't have to", "mustn't", "can't to", "must not", "Tidak harus → don't have to."),
 ('Pilih jawaban yang benar: "I ___ swim at the age of six." (bisa)', "could", "can", "am able", "will be", "Lampau → could."),
 ('Pilih jawaban yang benar: "He ___ be at home. His car is outside." (hampir pasti)', "must", "can't", "mustn't", "shouldn't", "Kesimpulan → must be."),
 ('Pilih jawaban yang benar: "I ___ studied. Now I have failed." (menyesal)', "should have", "should", "must", "would", "Penyesalan → should have + V3."),
 ('Pilih jawaban yang benar: "___ you mind opening the window?" (sangat sopan)', "Would", "Do", "Can", "Shall", "Would you mind + V-ing."),
 ('Pilih kalimat yang SALAH:', "Does she can swim?", "Can she swim?", "She can swim.", "She can't swim.", "Pertanyaan dengan can tanpa do."),
 ('Pilih kalimat yang SALAH:', "He must to go.", "He must go.", "He has to go.", "He should go.", "must tanpa to."),
 ('Pilih kalimat yang SALAH:', "You mustn't to worry.", "You mustn't worry.", "You needn't worry.", "You shouldn't worry.", "Setelah modal, V1 tanpa to."),
]) + mkf([
 ("Dia bisa berenang.", "She ___ swim.", "can", "can + V1."),
 ("Kamu tidak boleh merokok di sini.", "You ___ smoke here.", "mustn't/must not", "mustn't = dilarang."),
 ("Kamu tidak harus datang.", "You don't ___ to come.", "have", "don't have to."),
 ("Seharusnya aku belajar.", "I should ___ studied.", "have", "should have + V3."),
]), quiz=mk([
 ('Pilih jawaban yang benar: "___ I borrow your pen, please?" (sopan)', "May", "Do", "Am", "Will to", "May I = izin sopan."),
 ('Pilih jawaban yang benar: "He ___ finish the race yesterday." (berhasil)', "was able to", "can", "is able to", "could to", "Satu kejadian lampau → was able to."),
 ('Pilih kalimat yang SALAH:', "She cans drive.", "She can drive.", "She could drive.", "She can't drive.", "can tanpa -s."),
 ('Pilih jawaban yang benar: "That ___ be true. It is impossible." (hampir pasti salah)', "can't", "must", "should", "might to", "Kesimpulan negatif → can't be."),
]) + mkf([
 ("Dia pasti sudah pergi.", "He must ___ left.", "have", "must have + V3."),
 ("Sebaiknya kamu pergi sekarang.", "You had ___ go now.", "better", "had better."),
]))
