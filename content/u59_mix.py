from qk import mk, mkf, mko
MIX = dict(practice=mk([
 ('Pilih jawaban yang benar: "If I were you, I ___ ask for feedback."', "would", "will", "did", "had", "If I were you, I would + V1."),
 ('Pilih jawaban yang benar: "If you meet the deadline, you ___ a bonus."', "will get", "would get", "got", "get got", "Type 1: will + V1."),
 ('Pilih jawaban yang benar: "If you had asked earlier, you ___ finished now."', "would be", "would have been", "will be", "were", "Campuran: would + V1."),
 ('Pilih jawaban yang benar: "I wish you ___ ask for help sooner."', "would", "will", "did", "had", "I wish you would + V1."),
 ('Pilih kalimat yang benar:', "If you improve, you will finish faster.", "If you will improve, you finish faster.", "If you improved, you will finish faster.", "If you improve, you would finish faster now.", "Type 1: present, will."),
 ('Pilih kalimat yang SALAH:', "If I was you, I will ask for feedback.", "If I were you, I would ask for feedback.", "If you ask, you will get feedback.", "If you had asked, you would have received feedback.", "If I were you, I would + V1."),
 ('Pilih kalimat yang SALAH:', "If you would meet the deadline, you will get a bonus.", "If you meet the deadline, you will get a bonus.", "If you met the deadline, you would get a bonus.", "If you had met the deadline, you would have got a bonus.", "Jangan would di klausa if."),
]) + mkf([
 ("Kalau aku jadi kamu, aku akan meminta masukan.", "If I ___ you, I would ask for feedback.", "were", "If I were you, ..."),
 ("Kalau kamu memenuhi tenggat, kamu akan mendapat bonus.", "If you meet the deadline, you ___ get a bonus.", "will", "Type 1."),
 ("Seandainya kamu bertanya lebih awal, sekarang kamu sudah selesai.", "If you had asked earlier, you would ___ finished now.", "be", "Campuran."),
 ("Andai kamu meminta bantuan lebih cepat.", "I wish you ___ ask for help sooner.", "would", "I wish you would."),
]), quiz=mk([
 ('Pilih jawaban yang benar: "If you work hard, you ___ succeed."', "will", "would have", "did", "are", "Type 1."),
 ('Pilih jawaban yang benar: "If I had your skills, I ___ apply."', "would", "will", "did", "have", "Type 2: would + V1."),
 ('Pilih kalimat yang SALAH:', "If I would be you, I would ask.", "If I were you, I would ask.", "If I were you, I would wait.", "If I were you, I wouldn't worry.", "If I were you."),
]) + mkf([
 ("Seandainya kamu memenuhi tenggat, kamu akan dapat bonus.", "If you had met the deadline, you would have ___ a bonus.", "got/gotten", "Type 3."),
]))
