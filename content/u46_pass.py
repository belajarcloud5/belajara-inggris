from qk import mk, mkf, mko
PASS = dict(practice=mk([
 ('Pilih jawaban yang benar: "The book ___ by a famous writer."', "was written", "wrote", "was wrote", "is write", "was + V3 (written)."),
 ('Pilih jawaban yang benar: "English ___ in many countries."', "is spoken", "speaks", "is spoke", "are spoken", "is + V3."),
 ('Pilih jawaban yang benar: "The report must ___ finished by Friday."', "be", "is", "been", "being", "must be + V3."),
 ('Pilih jawaban yang benar: "The tickets ___ sold."', "have been", "has been", "have be", "are be", "Jamak, present perfect → have been."),
 ('Pilih jawaban yang benar: "The letter was written ___ a pen."', "with", "by", "from", "of", "Alat → with."),
 ('Pilih jawaban yang benar: "The letter was written ___ Rina."', "by", "with", "from", "of", "Pelaku → by."),
 ('Pilih jawaban yang benar: "The meeting will ___ held on Monday."', "be", "is", "been", "being", "will be + V3."),
 ('Pilih kalimat yang SALAH:', "The accident was happened.", "The accident happened.", "The window was broken.", "The work was done.", "happen tidak bisa dipasifkan."),
 ('Pilih kalimat yang SALAH:', "The cake was ate by the children.", "The cake was eaten by the children.", "The children ate the cake.", "The cake was baked.", "V3 dari eat adalah eaten."),
 ('Pilih kalimat yang SALAH:', "The books is sold here.", "The books are sold here.", "The book is sold here.", "The books were sold.", "books jamak → are."),
]) + mkf([
 ("Buku ini ditulis oleh seorang penulis terkenal.", "This book was ___ by a famous writer.", "written", "V3 dari write adalah written."),
 ("Bahasa Inggris diucapkan di banyak negara.", "English is ___ in many countries.", "spoken", "V3 dari speak adalah spoken."),
 ("Laporan harus diselesaikan.", "The report must ___ finished.", "be", "must be + V3."),
 ("Surat itu ditulis dengan pulpen.", "The letter was written ___ a pen.", "with", "Alat → with."),
]), quiz=mk([
 ('Pilih jawaban yang benar: "The window ___ broken by the ball."', "was", "were", "is", "did", "Tunggal lampau → was broken."),
 ('Pilih jawaban yang benar: "The rooms ___ cleaned every day."', "are", "is", "does", "has", "Jamak → are cleaned."),
 ('Pilih kalimat yang SALAH:', "The email has sent.", "The email has been sent.", "The emails have been sent.", "The email was sent.", "Pasif butuh been."),
 ('Pilih jawaban yang benar: "The decision will ___ announced tomorrow."', "be", "is", "been", "being", "will be + V3."),
]) + mkf([
 ("Kue itu dimakan oleh anak-anak.", "The cake was ___ by the children.", "eaten", "V3 dari eat adalah eaten."),
 ("Email itu sudah dikirim.", "The email has ___ sent.", "been", "has been + V3."),
]))
