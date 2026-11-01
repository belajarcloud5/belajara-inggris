from qk import mk, mkf, mko
MODAL = dict(practice=mk([
 ('Pilih ungkapan yang PALING sopan untuk meminta bantuan:', "Would you mind helping me?", "Can you help me?", "Help me.", "You help me.", "Would you mind + V-ing paling sopan."),
 ('Pilih ungkapan yang PALING sopan untuk meminta izin duduk:', "May I sit here?", "Can I sit here?", "I sit here.", "Sit here is ok?", "May I paling sopan."),
 ('Pilih jawaban yang benar: "Would you mind ___ the door?"', "closing", "close", "to close", "closed", "mind + V-ing."),
 ('Pilih jawaban untuk "Would you mind helping me?" jika Anda bersedia:', "Not at all.", "Yes, I mind.", "No, I can't.", "Of course not to.", "Not at all = tidak keberatan."),
 ('Pilih jawaban untuk "Could you send the file?" jika Anda bersedia:', "Certainly.", "Not at all.", "Yes, I mind.", "I don't.", "Certainly = tentu."),
 ('Pilih tawaran yang paling sopan:', "Shall I bring you some water?", "Do you want some water?", "Water?", "You drink water.", "Shall I ... paling sopan."),
 ('Pilih kalimat penolakan yang paling sopan:', "I'm afraid I can't.", "I can't.", "No.", "I don't want.", "I'm afraid ... lebih sopan."),
 ('Pilih kalimat yang SALAH:', "Would you mind to help me?", "Would you mind helping me?", "Could you help me?", "Would you help me, please?", "Would you mind diikuti V-ing."),
]) + mkf([
 ("Apakah Anda keberatan membantu saya?", "Would you mind ___ me?", "helping", "mind + V-ing."),
 ("Bolehkah saya duduk di sini?", "___ I sit here?", "May/Could/Can", "May, Could, atau Can."),
 ("Mau saya bawakan air?", "___ I bring you some water?", "Shall", "Shall I = tawaran."),
 ("Saya khawatir tidak bisa.", "I'm ___ I can't.", "afraid", "I'm afraid = maaf, sayangnya."),
]), quiz=mk([
 ('Pilih ungkapan yang paling sopan:', "Could you please send the report?", "Send the report.", "Can you send the report?", "You send the report.", "Could you please ... lebih sopan."),
 ('Pilih jawaban yang benar: "Would you mind ___ a message?"', "leaving", "leave", "to leave", "left", "mind + V-ing."),
 ('Pilih kalimat yang SALAH:', "Would you mind to wait?", "Would you mind waiting?", "Could you wait, please?", "May I ask you to wait?", "mind + V-ing."),
]) + mkf([
 ("Bisakah Anda mengirim berkas itu?", "___ you send the file?", "Could/Can", "Could atau Can."),
]))
