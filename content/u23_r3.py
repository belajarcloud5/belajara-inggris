from qk import mk
R3 = dict(practice=mk([
 ("Terjemahan \"Saya sudah makan\":","I have eaten.","I have ate.","I has eaten.","I am eaten.","tr."),
 ("Terjemahan \"Dia belum pernah ke Bali\":","She has never been to Bali.","She never been Bali.","She has never go to Bali.","She hasn't never been.","tr."),
 ("Terjemahan \"Pernahkah kamu melihat harimau?\":","Have you ever seen a tiger?","Did you ever seen tiger?","Have you ever see a tiger?","Do you ever seen a tiger?","tr."),
 ("Terjemahan \"Kami tinggal di sini sejak 2018\":","We have lived here since 2018.","We live here since 2018.","We lived here since 2018.","We have live here for 2018.","tr."),
 ("Terjemahan \"Mereka baru saja tiba\":","They have just arrived.","They just have arrive.","They has just arrived.","They arrive just.","tr."),
 ("Terjemahan \"Dia sudah menunggu selama dua jam\":","She has waited for two hours.","She waits since two hours.","She has wait two hours.","She waited for two hours now.","tr."),
 ("Perbaiki: \"I have saw that film.\"","I have seen that film.","I have see that film.","I has seen that film.","I have saw film.","fix."),
 ("Perbaiki: \"She has went home.\"","She has gone home.","She have gone home.","She has go home.","She has goes home.","fix."),
 ("Perbaiki: \"We have lived here since five years.\"","We have lived here for five years.","We lived here since five years.","We live here for five years.","We have live here five years ago.","fix."),
 ("Perbaiki: \"Did you ever been to Japan?\"","Have you ever been to Japan?","Did you ever be to Japan?","Do you ever been Japan?","Have you ever be to Japan?","fix."),
 ("Dialog: \"Have you finished?\" – \"___\"","Yes, I have.","Yes, I did.","Yes, I am.","Yes, I finished have.","dialog."),
 ("Dialog: \"Has he eaten?\" – \"___\"","No, he hasn't.","No, he doesn't.","No, he didn't have.","No, he isn't.","dialog."),
]), quiz=mk([
 ("\"Pernah\":","ever","never","just","still","word."),
 ("\"Belum\":","not yet","already","just","ever","word."),
 ("\"Baru saja\":","just","still","yet","ever","word."),
 ("\"Sudah\":","already","yet","never","just now","word."),
 ("\"Selama\" (durasi):","for","since","ago","until","word."),
 ("\"Sejak\":","since","for","ago","during","word."),
 ("\"Pengalaman\":","experience","experiment","expert","expense","word."),
 ("\"Berkali-kali\":","many times","one time","never","no time","word."),
]))
