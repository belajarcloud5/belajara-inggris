from qk import mk, mkf, mko
PASS = dict(practice=mk([
 ('Pilih jawaban yang benar: "A new bridge ___ built."', "has been", "have been", "is", "has", "Tunggal, present perfect pasif → has been + V3."),
 ('Pilih jawaban yang benar: "The letters ___ sent."', "have been", "has been", "was been", "are been", "Jamak → have been + V3."),
 ('Pilih jawaban yang benar: "The work hasn\'t ___ finished."', "been", "be", "being", "was", "hasn't been + V3."),
 ('Pilih pasif dari "Someone has cleaned the room.":', "The room has been cleaned.", "The room has cleaned.", "The room is cleaned.", "The room have been cleaned.", "has been + V3."),
 ('Pilih pasif dari "They have sold the tickets.":', "The tickets have been sold.", "The tickets have sold.", "The tickets has been sold.", "The tickets were been sold.", "have been + V3."),
 ('Pilih kalimat yang SALAH:', "The room has cleaned.", "The room has been cleaned.", "The rooms have been cleaned.", "The room hasn't been cleaned.", "Pasif butuh been."),
 ('Pilih kalimat yang benar:', "Have the letters been sent?", "Have the letters sent?", "Has the letters been sent?", "Have been the letters sent?", "Have + subjek + been + V3."),
]) + mkf([
 ("Jembatan baru sudah dibangun.", "A new bridge has ___ built.", "been", "has been + V3."),
 ("Surat-surat itu sudah dikirim.", "The letters have been ___.", "sent", "V3 dari send adalah sent."),
 ("Pekerjaan itu belum diselesaikan.", "The work hasn't been ___.", "finished", "hasn't been + V3."),
 ("Tiket-tiket sudah terjual.", "The tickets have been ___.", "sold", "V3 dari sell adalah sold."),
]), quiz=mk([
 ('Pilih jawaban yang benar: "The hotel ___ booked yet."', "hasn't been", "haven't been", "isn't", "hasn't", "Tunggal → hasn't been."),
 ('Pilih jawaban yang benar: "The photos ___ taken."', "have been", "has been", "was be", "are be", "Jamak → have been."),
 ('Pilih kalimat yang SALAH:', "The tickets has been sold.", "The tickets have been sold.", "The ticket has been sold.", "The tickets haven't been sold.", "tickets jamak → have."),
]) + mkf([
 ("Kamar itu sudah dibersihkan.", "The room has been ___.", "cleaned", "has been + V3."),
]))
