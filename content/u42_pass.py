from qk import mk, mkf, mko
PASS = dict(practice=mk([
 ('Pilih jawaban yang benar: "If the road ___ repaired, traffic will be reduced."', "is", "was", "were", "be", "Tipe 1: if + present pasif → is repaired."),
 ('Pilih jawaban yang benar: "If the rubbish were collected daily, the street ___ cleaner."', "would be", "will be", "is", "would", "Tipe 2: would be."),
 ('Pilih jawaban yang benar: "If the bridge had been built earlier, many lives ___ been saved."', "would have", "would", "will have", "had", "Tipe 3: would have been + V3."),
 ('Pilih jawaban yang benar: "If the problem ___ reported earlier, it would have been solved."', "had been", "was", "has been", "were", "Tipe 3: had been + V3."),
 ('Pilih kalimat yang benar:', "If the room is cleaned, we will use it.", "If the room cleaned, we will use it.", "If the room is clean, we will used it.", "If the room cleans, we will be used it.", "if + is + V3."),
 ('Pilih kalimat yang SALAH:', "If the work will be finished, we can go.", "If the work is finished, we can go.", "If the work had been finished, we could have gone.", "If the work were finished, we could go.", "Jangan will di if-clause."),
 ('Pilih kalimat yang SALAH:', "The letter would have send if you had asked.", "The letter would have been sent if you had asked.", "The letter would be sent if you asked.", "The letter will be sent if you ask.", "would have been + V3."),
]) + mkf([
 ("Kalau jalan diperbaiki, kemacetan akan berkurang.", "If the road is ___, traffic will be reduced.", "repaired", "is + V3."),
 ("Seandainya masalahnya dilaporkan lebih awal, akan terselesaikan.", "If the problem had been reported earlier, it would have been ___.", "solved", "would have been + V3."),
 ("Kalau sampah diangkut setiap hari, jalan akan lebih bersih.", "If the rubbish ___ collected daily, the street would be cleaner.", "were", "Tipe 2: were."),
 ("Seandainya jembatan dibangun lebih awal, nyawa akan terselamatkan.", "If the bridge had been ___ earlier, lives would have been saved.", "built", "had been + V3."),
]), quiz=mk([
 ('Pilih jawaban yang benar: "If the report ___ finished, we will send it."', "is", "will be", "was", "be", "Tipe 1: is finished."),
 ('Pilih jawaban yang benar: "If the car had been repaired, we ___ have traveled."', "would", "will", "can", "must", "Tipe 3: would have + V3."),
 ('Pilih kalimat yang SALAH:', "If the window was broken, I will call you.", "If the window is broken, I will call you.", "If the window were broken, I would call you.", "If the window had been broken, I would have called you.", "Tipe 1 memakai is."),
]) + mkf([
 ("Kalau tiketnya dibeli, kita akan pergi.", "If the tickets are ___, we will go.", "bought", "are + V3."),
]))
