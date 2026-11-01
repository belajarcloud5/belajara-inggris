from qk import mk, mkf, mko
MODAL = dict(practice=mk([
 ('Pilih jawaban yang benar: "I failed the test. I ___ studied harder." (menyesal)', "should have", "should", "must", "would", "Penyesalan → should have + V3."),
 ('Pilih jawaban yang benar: "You ___ shouted at him. It was rude." (tidak seharusnya)', "shouldn\'t have", "shouldn\'t", "mustn\'t", "couldn\'t", "Tidak seharusnya (lampau) → shouldn't have + V3."),
 ('Pilih jawaban yang benar: "The bus is gone. We ___ missed it." (pasti sudah)', "must have", "must", "should", "can", "Kesimpulan lampau → must have + V3."),
 ('Pilih jawaban yang benar: "We lost by one point. We ___ won." (sebenarnya bisa)', "could have", "could", "can have", "would", "Sebenarnya bisa → could have + V3."),
 ('Pilih jawaban yang benar: "If I had known, I ___ come." (pasti sudah)', "would have", "will", "would", "must", "Kalimat tipe 3 → would have + V3."),
 ('Pilih jawaban yang benar: "I think she ___ left early." (mungkin sudah)', "might have", "might", "must", "should", "Mungkin sudah → might have + V3."),
 ('Pilih kalimat yang benar:', "I should have gone.", "I should have went.", "I should of gone.", "I should has gone.", "should have + V3 (gone)."),
 ('Pilih kalimat yang SALAH:', "She must have went home.", "She must have gone home.", "She must have left early.", "She might have gone home.", "V3 dari go adalah gone."),
]) + mkf([
 ("Seharusnya aku belajar lebih giat.", "I ___ have studied harder.", "should", "should have."),
 ("Dia pasti sudah lupa.", "He must ___ forgotten.", "have", "must have + V3."),
 ("Kita sebenarnya bisa menang.", "We could ___ won.", "have", "could have + V3."),
 ("Kalau aku tahu, aku pasti sudah datang.", "If I had known, I would ___ come.", "have", "would have + V3."),
]), quiz=mk([
 ('Pilih jawaban yang benar: "You didn\'t listen. You ___ listened carefully."', "should have", "should", "must", "can have", "Penyesalan → should have."),
 ('Pilih jawaban yang benar: "The ground is wet. It ___ rained last night."', "must have", "must", "should", "will have", "Kesimpulan lampau → must have."),
 ('Pilih kalimat yang SALAH:', "He could of won.", "He could have won.", "He should have won.", "He might have won.", "Bukan 'of' tetapi 'have'."),
]) + mkf([
 ("Dia mungkin sudah pergi.", "She might ___ left.", "have", "might have + V3."),
]))
