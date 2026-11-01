from qk import mk, mkf, mko
MIX = dict(practice=mk([
 ('Pilih jawaban yang benar: "What would you do if you ___ a mistake?"', "made", "make", "will make", "would make", "if + past, would."),
 ('Pilih jawaban yang benar: "If I made a mistake, I ___ tell my manager at once."', "would", "will", "did", "had", "Type 2: would + V1."),
 ('Pilih jawaban yang benar: "If you hired me, I ___ improve the reports."', "would", "will", "did", "had", "Type 2: would + V1."),
 ('Pilih jawaban yang benar: "If I had not studied accounting, I ___ not be applying now."', "would", "will", "did", "had", "Campuran: would + V1."),
 ('Pilih jawaban yang benar: "How ___ you handle a difficult customer?"', "would", "will", "did", "were", "How would you ...?"),
 ('Pilih kalimat yang benar:', "If I were the manager, I would listen carefully.", "If I was the manager, I will listen carefully.", "If I am the manager, I would listen carefully.", "If I were the manager, I listened carefully.", "Type 2: were ... would."),
 ('Pilih kalimat yang SALAH:', "If I would make a mistake, I would tell you.", "If I made a mistake, I would tell you.", "If I made a mistake, I would apologize.", "What would you do if you made a mistake?", "Jangan would di klausa if."),
 ('Pilih kalimat yang SALAH:', "If you hired me, I will improve the reports.", "If you hired me, I would improve the reports.", "If you hire me, I will improve the reports.", "If you had hired me, I would have improved the reports.", "Kala klausa harus cocok."),
]) + mkf([
 ("Apa yang akan Anda lakukan kalau Anda membuat kesalahan?", "What would you do if you ___ a mistake?", "made", "if + past, would."),
 ("Kalau saya membuat kesalahan, saya akan memberi tahu atasan.", "If I made a mistake, I ___ tell my manager.", "would", "Type 2: would + V1."),
 ("Kalau Anda mempekerjakan saya, saya akan memperbaiki laporan.", "If you hired me, I would ___ the reports.", "improve", "would + V1."),
 ("Bagaimana Anda akan menangani pelanggan yang sulit?", "How ___ you handle a difficult customer?", "would", "How would you ...?"),
]), quiz=mk([
 ('Pilih jawaban yang benar: "If I were you, I ___ accept the offer."', "would", "will", "did", "am", "If I were you, I would + V1."),
 ('Pilih jawaban yang benar: "What would you do if you ___ the job?"', "got", "get", "will get", "would get", "if + past, would."),
 ('Pilih kalimat yang SALAH:', "If I would have time, I would help.", "If I had time, I would help.", "If I had time, I would call you.", "If I had more time, I would study.", "Jangan would di klausa if."),
]) + mkf([
 ("Kalau saya jadi Anda, saya akan menerima tawaran itu.", "If I ___ you, I would accept.", "were", "If I were you, ..."),
]))
