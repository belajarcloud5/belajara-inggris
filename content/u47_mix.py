from qk import mk, mkf, mko
MIX = dict(practice=mk([
 ('Pilih jenis yang tepat (fakta umum): "If you heat water, it ___."', "boils", "would boil", "will boiled", "boiled", "Zero: present, present."),
 ('Pilih jenis yang tepat (mungkin di masa depan): "If I pass, I ___ celebrate."', "will", "would have", "did", "am", "Type 1: will + V1."),
 ('Pilih jenis yang tepat (tidak nyata sekarang): "If I were you, I ___ study."', "would", "will", "did", "had", "Type 2: would + V1."),
 ('Pilih jenis yang tepat (tidak nyata masa lalu): "If I had studied, I ___ passed."', "would have", "would", "will have", "had", "Type 3: would have + V3."),
 ('Pilih jenis yang tepat (masa lalu → sekarang): "If I had studied, I ___ proud now."', "would be", "would have been", "will be", "was", "Campuran: would + V1."),
 ('Pilih jenis yang tepat (sekarang → masa lalu): "If I were braver, I ___ spoken."', "would have", "would", "will have", "had", "Campuran: would have + V3."),
 ('Pilih kalimat yang SALAH:', "If I would pass, I would celebrate.", "If I passed, I would celebrate.", "If I pass, I will celebrate.", "If I had passed, I would have celebrated.", "Jangan would di klausa if."),
 ('Pilih kalimat yang SALAH:', "If it will rain, we stay home.", "If it rains, we will stay home.", "If it rains, we stay home.", "If it rained, we would stay home.", "Jangan will di klausa if."),
]) + mkf([
 ("Kalau kamu memanaskan air, air itu mendidih.", "If you heat water, it ___.", "boils", "Zero."),
 ("Kalau aku lulus, aku akan merayakan.", "If I pass, I ___ celebrate.", "will", "Type 1."),
 ("Kalau aku jadi kamu, aku akan belajar.", "If I ___ you, I would study.", "were", "Type 2."),
 ("Seandainya aku belajar, aku sudah lulus.", "If I had studied, I would ___ passed.", "have", "Type 3."),
]), quiz=mk([
 ('Pilih jawaban yang benar: "If I had known, I ___ come."', "would have", "would", "will have", "had", "Type 3: would have + V3."),
 ('Pilih jawaban yang benar: "If it rains, we ___ stay home."', "will", "would have", "did", "are", "Type 1: will + V1."),
 ('Pilih kalimat yang SALAH:', "If I would study, I would pass.", "If I studied, I would pass.", "If I study, I will pass.", "If I had studied, I would have passed.", "Jangan would di klausa if."),
]) + mkf([
 ("Seandainya aku belajar, sekarang aku bangga.", "If I had studied, I would ___ proud now.", "be", "Campuran: would + V1."),
]))
