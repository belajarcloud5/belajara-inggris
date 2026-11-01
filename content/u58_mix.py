from qk import mk, mkf, mko
MIX = dict(practice=mk([
 ('Pilih jawaban yang benar: "If we had tested the system, we ___ the bug."', "would have found", "would find", "will find", "found", "Type 3: would have + V3."),
 ('Pilih jawaban yang benar: "If we had ordered the part earlier, the project ___ on time now."', "would be", "would have been", "will be", "was", "Campuran: would + V1."),
 ('Pilih jawaban yang benar: "If we add more servers, the system ___ faster."', "will run", "would run", "ran", "runs ran", "Type 1: will + V1."),
 ('Pilih jawaban yang benar: "If we ___ more staff, we could finish sooner."', "had", "have", "will have", "would have", "Type 2: if + past."),
 ('Pilih jawaban yang benar: "If the team had reported it, we ___ facing this delay now."', "would not be", "would not have been", "will not be", "did not", "Campuran: would not + V1."),
 ('Pilih kalimat yang SALAH:', "If we tested it earlier, we would have found the bug.", "If we had tested it earlier, we would have found the bug.", "If we had tested it, we would find it now.", "Had we tested it, we would have found it.", "Type 3 butuh had + V3."),
 ('Pilih kalimat yang SALAH:', "If we will add servers, the system runs faster.", "If we add servers, the system will run faster.", "If we added servers, the system would run faster.", "If we had added servers, it would have run faster.", "Jangan will di klausa if."),
]) + mkf([
 ("Seandainya kita menguji sistemnya, kita akan menemukan bug itu.", "If we had tested the system, we would ___ found the bug.", "have", "Type 3."),
 ("Seandainya kita memesan suku cadang lebih awal, proyek sekarang tepat waktu.", "If we had ordered earlier, the project would ___ on time now.", "be", "Campuran."),
 ("Kalau kita menambah server, sistem akan lebih cepat.", "If we add more servers, the system ___ run faster.", "will", "Type 1."),
 ("Kalau kita punya lebih banyak staf, kita bisa selesai lebih cepat.", "If we ___ more staff, we could finish sooner.", "had", "Type 2."),
]), quiz=mk([
 ('Pilih jawaban yang benar: "If we had backed up the files, we ___ lost the data."', "would not have", "would not", "will not have", "did not", "Type 3."),
 ('Pilih jawaban yang benar: "If we had more time, we ___ finish today."', "could", "can", "did", "will", "Type 2: could."),
 ('Pilih kalimat yang SALAH:', "If we had acted faster, we would not have face this problem.", "If we had acted faster, we would not have faced this problem.", "If we had acted faster, we would not be facing this problem now.", "If we acted faster, we would not face this problem.", "would not have + V3."),
]) + mkf([
 ("Seandainya tim melaporkan lebih awal, kita sekarang tidak menghadapi keterlambatan.", "If the team had reported earlier, we would ___ be facing this delay.", "not", "Campuran."),
]))
