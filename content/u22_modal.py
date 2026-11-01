from qk import mk, mkf, mko
MODAL = dict(practice=mk([
 ('Pilih jawaban yang benar: "If it rains, the match ___ be cancelled." (mungkin)', "might", "will to", "won't to", "must to", "Kemungkinan → might."),
 ('Pilih jawaban yang benar: "If you study hard, you ___ pass the exam." (mungkin)', "may", "pass", "are may", "do", "Kemungkinan → may."),
 ('Pilih jawaban yang benar: "We ___ win, but we will try." (mungkin tidak)', "might not", "can't to", "mustn't", "don't might", "Mungkin tidak → might not."),
 ('Pilih jawaban yang benar: "If you hurry, you ___ catch the bus." (mungkin)', "could", "do", "are", "did", "Kemungkinan → could."),
 ('Pilih jawaban yang benar: "If it rains, we ___ go out." (pasti tidak)', "won't", "might", "may", "could", "Pasti tidak → won't."),
 ('Pilih kalimat yang benar:', "She might come to the party.", "She might to come to the party.", "She might comes to the party.", "She mights come to the party.", "might + V1."),
 ('Pilih kalimat yang SALAH:', "We might to win.", "We might win.", "We may win.", "We could win.", "might tanpa to."),
 ('Pilih kalimat yang benar:', "If it rains, I might stay home.", "If it rains, I might to stay home.", "If it will rain, I might stay home.", "If it rains, I might stays home.", "if + present, modal + V1."),
]) + mkf([
 ("Kalau hujan, pertandingan mungkin dibatalkan.", "If it rains, the match ___ be cancelled.", "might/may/could", "Kemungkinan → might, may, atau could."),
 ("Dia mungkin tidak datang.", "She ___ not come.", "might/may", "might not atau may not."),
 ("Kalau hujan, kami pasti tidak pergi.", "If it rains, we ___ go.", "won't", "Pasti tidak → won't."),
 ("Kamu mungkin lulus.", "You ___ pass.", "may/might/could", "may, might, atau could."),
]), quiz=mk([
 ('Pilih jawaban yang benar: "If you ask him, he ___ help you." (mungkin)', "might", "might to", "is", "does", "Kemungkinan → might."),
 ('Pilih jawaban yang benar: "I ___ be late, so don\'t wait for me." (mungkin)', "might", "must to", "can to", "will to", "Kemungkinan → might."),
 ('Pilih kalimat yang SALAH:', "He mights come.", "He might come.", "He may come.", "He could come.", "might tanpa -s."),
]) + mkf([
 ("Kalau hujan, kita mungkin tinggal di rumah.", "If it rains, we ___ stay home.", "might/may/could", "might, may, atau could."),
]))
