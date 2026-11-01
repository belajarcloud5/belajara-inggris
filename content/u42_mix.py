from qk import mk, mkf, mko
MIX = dict(practice=mk([
 ('Pilih jawaban yang benar: "If I had studied harder, I ___ a doctor now." (masa lalu → sekarang)', "would be", "would have been", "will be", "am", "Campuran: would + V1."),
 ('Pilih jawaban yang benar: "If I weren\'t afraid of flying, I ___ the plane." (sekarang → masa lalu)', "would have taken", "would take", "will take", "took", "Campuran: would have + V3."),
 ('Pilih jawaban yang benar: "If she had taken the job, she ___ rich now."', "would be", "would have been", "will be", "was", "Campuran: would + V1."),
 ('Pilih jawaban yang benar: "If we ___ earlier, we would not be stuck in traffic now."', "had left", "left", "leave", "would leave", "Campuran: if + past perfect."),
 ('Pilih jawaban yang benar: "___ I known, I would have come." (tanpa if)', "Had", "Have", "Did", "Was", "Had + subjek + V3."),
 ('Pilih jawaban yang benar: "___ you need help, call me." (tanpa if)', "Should", "Would", "Had", "Did", "Should + subjek + V1."),
 ('Pilih kalimat yang benar:', "If I had studied, I would be proud now.", "If I studied, I would be proud now.", "If I had studied, I will be proud now.", "If I would study, I would be proud now.", "Campuran: past perfect → would + V1."),
 ('Pilih kalimat yang SALAH:', "If I had known, I would come yesterday.", "If I had known, I would have come yesterday.", "If I had known, I would be there now.", "Had I known, I would have come.", "Hasil di masa lalu → would have + V3."),
 ('Pilih kalimat yang SALAH:', "Had I knew, I would not have been late.", "Had I known, I would not have been late.", "If I had known, I would not have been late.", "Had I known, I would have come.", "Had + subjek + V3."),
]) + mkf([
 ("Seandainya aku belajar lebih giat, sekarang aku jadi dokter.", "If I had studied harder, I ___ a doctor now.", "would be", "Campuran: would + V1."),
 ("Seandainya aku tidak takut terbang, aku sudah naik pesawat.", "If I weren't afraid of flying, I would ___ taken the plane.", "have", "Campuran: would have + V3."),
 ("Seandainya aku tahu, aku sudah datang.", "___ I known, I would have come.", "Had", "Had + subjek + V3."),
 ("Seandainya dia mengambil pekerjaan itu, dia sekarang kaya.", "If she had taken the job, she would ___ rich now.", "be", "Campuran: would be."),
]), quiz=mk([
 ('Pilih jawaban yang benar: "If I had saved money, I ___ on holiday now."', "would be", "would have been", "will be", "was", "Campuran: would + V1."),
 ('Pilih jawaban yang benar: "If I were braver, I ___ spoken up." (sekarang → masa lalu)', "would have", "would", "will have", "had", "Campuran: would have + V3."),
 ('Pilih kalimat yang SALAH:', "If I had worked harder, I would be paid more now.", "If I had worked harder, I would have been paid more.", "If I worked harder, I would be paid more.", "If I had worked harder, I would get paid more now.", "Hasil sekarang → would + V1."),
]) + mkf([
 ("Seandainya kita berangkat lebih awal, kita tidak akan terlambat sekarang.", "If we had left earlier, we ___ not be late now.", "would", "Campuran: would + V1."),
]))
