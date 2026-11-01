from qk import mk, mkf, mko
MIX = dict(practice=mk([
 ('Pilih jawaban yang benar: "If you heat ice, it ___."', "melts", "would melt", "will melted", "melted", "Zero: present, present."),
 ('Pilih jawaban yang benar: "If it rains, I ___ stay home."', "will", "would have", "did", "am", "Type 1: will + V1."),
 ('Pilih jawaban yang benar: "If I were rich, I ___ travel the world."', "would", "will", "did", "had", "Type 2: would + V1."),
 ('Pilih jawaban yang benar: "If I ___ known, I would have come."', "had", "have", "would have", "was", "Type 3: had + V3."),
 ('Pilih jawaban yang benar: "If I had studied, I ___ a doctor now."', "would be", "would have been", "will be", "was", "Campuran: would + V1."),
 ('Pilih jawaban yang benar: "___ you hurry, you will be late."', "Unless", "If", "When", "Although", "unless = if ... not."),
 ('Pilih jawaban yang benar: "I wish I ___ more time."', "had", "have", "will have", "would have", "I wish + past simple."),
 ('Pilih kalimat yang SALAH:', "If it will rain, I will stay home.", "If it rains, I will stay home.", "If it rains, I stay home.", "If it rained, I would stay home.", "Jangan will di klausa if."),
 ('Pilih kalimat yang SALAH:', "If I would be rich, I would travel.", "If I were rich, I would travel.", "If I were rich, I would buy a house.", "If I had money, I would travel.", "Jangan would di klausa if."),
 ('Pilih kalimat yang SALAH:', "If I knew, I would have come.", "If I had known, I would have come.", "If I knew, I would come.", "Had I known, I would have come.", "Type 3 butuh had + V3."),
]) + mkf([
 ("Kalau hujan, aku akan tinggal di rumah.", "If it rains, I ___ stay home.", "will/'ll", "Type 1: will + V1."),
 ("Kalau aku kaya, aku akan keliling dunia.", "If I were rich, I ___ travel the world.", "would", "Type 2: would + V1."),
 ("Seandainya aku tahu, aku sudah datang.", "If I ___ known, I would have come.", "had", "Type 3: had + V3."),
 ("Kecuali kamu bergegas, kamu akan terlambat.", "___ you hurry, you will be late.", "Unless", "unless = if ... not."),
]), quiz=mk([
 ('Pilih jawaban yang benar: "If I had left earlier, I ___ be late now." (tidak)', "wouldn\'t", "won\'t", "didn\'t", "hadn\'t", "Campuran: would not + V1."),
 ('Pilih jawaban yang benar: "If you mix red and blue, you ___ purple."', "get", "would get", "will got", "got", "Zero: present, present."),
 ('Pilih kalimat yang SALAH:', "If I had known, I will have come.", "If I had known, I would have come.", "If I had known, I would be there.", "Had I known, I would have come.", "Type 3: would have + V3."),
 ('Pilih jawaban yang benar: "I wish I ___ harder." (menyesal)', "had studied", "studied", "study", "would study", "I wish + past perfect."),
]) + mkf([
 ("Andai aku punya lebih banyak waktu.", "I wish I ___ more time.", "had", "I wish + past simple."),
 ("Seandainya aku belajar, sekarang aku jadi dokter.", "If I had studied, I would ___ a doctor now.", "be", "Campuran: would + V1."),
]))
