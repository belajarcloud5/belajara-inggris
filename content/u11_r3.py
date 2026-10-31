from qk import mk
R3 = dict(practice=mk([
 ("Terjemahan \"Dia sedang membaca buku\":","He is reading a book.","He reading a book.","He is read a book.","He reads now a book.","tr."),
 ("Terjemahan \"Kami sedang belajar bahasa Inggris\":","We are learning English.","We learning English are.","We is learn English.","We learn now English.","tr."),
 ("Terjemahan \"Mereka tidak sedang bermain\":","They aren't playing.","They don't playing.","They not play.","They isn't playing.","tr."),
 ("Terjemahan \"Apa yang sedang kamu lakukan?\":","What are you doing?","What you are do?","What do you doing?","What you doing is?","tr."),
 ("Terjemahan \"Hujan sedang turun\":","It is raining.","It rains now is.","It is rain.","It raining are.","tr."),
 ("Terjemahan \"Adikku sedang tidur\":","My brother is sleeping.","My brother sleeping is.","My brother are sleeping.","My brother sleeps now is.","tr."),
 ("Perbaiki: \"She is cook dinner.\"","She is cooking dinner.","She is cooks dinner.","She cooking is dinner.","She are cooking dinner.","fix."),
 ("Perbaiki: \"They is running.\"","They are running.","They be running.","They am running.","They running is.","fix."),
 ("Perbaiki: \"I am not knowing.\"","I don't know.","I am no know.","I not knowing.","I didn't knowing.","fix."),
 ("Perbaiki: \"Are he sleeping?\"","Is he sleeping?","Does he sleeping?","Is he sleeps?","Are he sleep?","fix."),
 ("Dialog: \"What is she doing?\" – \"___\"","She is writing.","She writes now is.","She write.","She is write.","dialog."),
 ("Dialog: \"Are they playing?\" – \"___\"","Yes, they are.","Yes, they do.","Yes, they play.","Yes, they is.","dialog."),
]), quiz=mk([
 ("\"Sedang menunggu\":","is waiting","waits","waited","will wait","word."),
 ("\"Sedang memasak\":","is cooking","cooks","cooked","will cook","word."),
 ("\"Sedang mandi\":","is taking a bath","takes bath","took bath","will bathe","word."),
 ("\"Sedang berlari\":","is running","runs","ran","will run","word."),
 ("\"Menyeberang\":","cross","carry","catch","call","word."),
 ("\"Menunggu\":","wait","walk","watch","wash","word."),
 ("\"Mendengarkan\":","listen","look","see","watch","word."),
 ("\"Menonton\":","watch","listen","hear","say","word."),
]))
