from qk import mk, mkf, mko
PASS = dict(practice=mk([
 ('Pilih jawaban yang benar: "The bug ___ fixed." (sudah selesai)', "has been", "have been", "is been", "was be", "has been + V3."),
 ('Pilih jawaban yang benar: "The server ___ replaced right now." (sedang)', "is being", "is", "has been", "was be", "is being + V3."),
 ('Pilih jawaban yang benar: "The report will ___ sent tomorrow."', "be", "is", "been", "being", "will be + V3."),
 ('Pilih jawaban yang benar: "The issue hasn\'t ___ resolved yet."', "been", "be", "being", "was", "hasn't been + V3."),
 ('Pilih jawaban yang benar: "The parts ___ ordered, and they will be delivered Monday."', "have been", "has been", "is been", "was be", "Jamak → have been."),
 ('Pilih kalimat yang SALAH:', "The server is been replaced.", "The server is being replaced.", "The server has been replaced.", "The server will be replaced.", "Sedang berlangsung → is being."),
 ('Pilih kalimat yang SALAH:', "The problem has been solve.", "The problem has been solved.", "The problems have been solved.", "The problem was solved.", "V3: solved."),
]) + mkf([
 ("Bug-nya sudah diperbaiki.", "The bug has ___ fixed.", "been", "has been + V3."),
 ("Servernya sedang diganti.", "The server is ___ replaced.", "being", "is being + V3."),
 ("Laporan akan dikirim besok.", "The report will be ___ tomorrow.", "sent", "will be + V3."),
 ("Masalahnya belum terselesaikan.", "The issue hasn't been ___ yet.", "resolved", "hasn't been + V3."),
]), quiz=mk([
 ('Pilih jawaban yang benar: "The part ___ delivered yet."', "hasn't been", "haven't been", "isn't be", "wasn't been", "hasn't been + V3."),
 ('Pilih jawaban yang benar: "The files ___ being checked."', "are", "is", "has", "does", "Jamak, sedang → are being."),
 ('Pilih kalimat yang SALAH:', "The system are being updated.", "The system is being updated.", "The systems are being updated.", "The system has been updated.", "system tunggal → is."),
]) + mkf([
 ("Suku cadangnya sudah dipesan.", "The part has been ___.", "ordered", "has been + V3."),
]))
