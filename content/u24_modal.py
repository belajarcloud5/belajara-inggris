from qk import mk, mkf, mko
MODAL = dict(practice=mk([
 ('Pilih jawaban yang benar: "He worked all day. He ___ be tired." (hampir pasti)', "must", "can't", "mustn't", "needn't", "Hampir pasti benar → must be."),
 ('Pilih jawaban yang benar: "He is in Bali now, so he ___ be at school." (hampir pasti salah)', "can't", "must", "should", "has to", "Hampir pasti salah → can't be."),
 ('Pilih jawaban yang benar: "I am not sure, but it ___ be true." (mungkin)', "might", "must to", "can't to", "will to", "Mungkin → might be."),
 ('Pilih jawaban yang benar: "She isn\'t answering the phone. She ___ be sleeping."', "must", "mustn't", "needn't", "ought", "Kesimpulan → must be."),
 ('Pilih kalimat yang benar:', "That can't be right.", "That mustn't be right.", "That doesn't can be right.", "That can't to be right.", "Kesimpulan salah → can't be."),
 ('Pilih kalimat yang SALAH:', "He mustn't be at home.", "He can't be at home.", "He must be at home.", "He might be at home.", "Untuk kesimpulan negatif pakai can't be."),
 ('Pilih kalimat yang benar:', "You mustn't run here.", "You can't to run here.", "You couldn't run here.", "You don't must run here.", "Larangan → mustn't."),
]) + mkf([
 ("Dia pasti lelah.", "He ___ be tired.", "must", "must be."),
 ("Itu tidak mungkin benar.", "That ___ be right.", "can't", "can't be."),
 ("Mungkin itu benar.", "It ___ be true.", "might/may/could", "might, may, atau could."),
]), quiz=mk([
 ('Pilih jawaban yang benar: "The lights are on, so someone ___ be home."', "must", "can't", "mustn't", "shouldn't", "Kesimpulan → must be."),
 ('Pilih jawaban yang benar: "That price is too low. It ___ be correct."', "can't", "must", "might to", "ought", "Hampir pasti salah → can't be."),
 ('Pilih kalimat yang SALAH:', "She mustn't be at school.", "She can't be at school.", "She must be at school.", "She might be at school.", "Kesimpulan negatif → can't be."),
]) + mkf([
 ("Dia mungkin sedang tidur.", "She ___ be sleeping.", "might/may/could", "might, may, atau could."),
]))
