from qk import mk, mkf, mko
MIX = dict(practice=mk([
 ('Pilih jawaban yang benar: "I wish I ___ more time." (sekarang)', "had", "have", "will have", "would have", "I wish + past simple."),
 ('Pilih jawaban yang benar: "I wish I ___ taller."', "were", "am", "will be", "had been to", "I wish + were."),
 ('Pilih jawaban yang benar: "I wish I ___ harder." (menyesal masa lalu)', "had studied", "studied", "study", "would study", "I wish + past perfect."),
 ('Pilih jawaban yang benar: "If I were you, I ___ apologize."', "would", "will", "did", "had", "If I were you, I would + V1."),
 ('Pilih jawaban yang benar: "I wish she ___ here now."', "were", "is", "will be", "has been", "I wish + were."),
 ('Pilih kalimat yang benar:', "I wish I had more time.", "I wish I have more time.", "I wish I will have more time.", "I wish I would have more time now.", "I wish + past simple."),
 ('Pilih kalimat yang SALAH:', "I wish I am rich.", "I wish I were rich.", "I wish I had more money.", "I wish I had saved money.", "I wish + were/had."),
 ('Pilih kalimat yang SALAH:', "If I was you, I will talk to her.", "If I were you, I would talk to her.", "If I were you, I would apologize.", "If I were you, I wouldn't wait.", "If I were you, I would + V1."),
]) + mkf([
 ("Andai aku punya lebih banyak waktu.", "I wish I ___ more time.", "had", "I wish + past simple."),
 ("Andai aku lebih tinggi.", "I wish I ___ taller.", "were", "I wish + were."),
 ("Andai aku belajar lebih giat.", "I wish I ___ studied harder.", "had", "I wish + past perfect."),
 ("Kalau aku jadi kamu, aku akan minta maaf.", "If I were you, I ___ apologize.", "would", "If I were you, I would + V1."),
]), quiz=mk([
 ('Pilih jawaban yang benar: "I wish I ___ a car." (sekarang tidak punya)', "had", "have", "will have", "would have", "I wish + past simple."),
 ('Pilih jawaban yang benar: "I wish I ___ him earlier." (menyesal)', "had met", "met", "meet", "would meet", "I wish + past perfect."),
 ('Pilih kalimat yang SALAH:', "I wish I would be taller.", "I wish I were taller.", "I wish I had been taller.", "I wish I could be taller.", "I wish + were/had."),
]) + mkf([
 ("Kalau aku jadi kamu, aku tidak akan menunggu.", "If I were you, I ___ wait.", "wouldn't", "If I were you, I would not + V1."),
]))
