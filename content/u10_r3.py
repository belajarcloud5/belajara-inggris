from qk import mk
R3 = dict(practice=mk([
 ("Terjemahan \"Kemarin saya pergi ke pasar\":","Yesterday I went to the market.","Yesterday I go to market.","Yesterday I goed market.","I went yesterday at market the.","tr."),
 ("Terjemahan \"Dia tidak menonton TV tadi malam\":","She didn't watch TV last night.","She not watched TV last night.","She doesn't watched TV.","She didn't watched TV.","tr."),
 ("Terjemahan \"Apakah kamu belajar semalam?\":","Did you study last night?","Do you studied last night?","You did study last night?","Did you studied last night?","tr."),
 ("Terjemahan \"Kami tiba di sana pukul lima\":","We arrived there at five.","We arrive there at five.","We arrived there on five.","We are arrived there five.","tr."),
 ("Terjemahan \"Dia sakit minggu lalu\":","He was sick last week.","He were sick last week.","He is sick last week.","He sick was last week.","tr."),
 ("Terjemahan \"Mereka bermain bola dua jam yang lalu\":","They played football two hours ago.","They play football two hours ago.","They playing football ago two hours.","They were play football.","tr."),
 ("Perbaiki: \"I buyed a new bag.\"","I bought a new bag.","I buy a new bag yesterday.","I buyed new bag.","I did bought a bag.","fix."),
 ("Perbaiki: \"She didn't went to school.\"","She didn't go to school.","She not went to school.","She didn't goes to school.","She doesn't went.","fix."),
 ("Perbaiki: \"Did he came late?\"","Did he come late?","Did he came late?","Does he came late?","Was he came late?","fix."),
 ("Perbaiki: \"We was at home.\"","We were at home.","We are at home yesterday.","We be at home.","We was be home.","fix."),
 ("Dialog: \"Where were you yesterday?\" – \"___\"","I was at home.","I am at home.","I were at home.","I be at home.","dialog."),
 ("Dialog: \"Did you finish your homework?\" – \"___\"","Yes, I did.","Yes, I was.","Yes, I done.","Yes, I finished do.","dialog."),
]), quiz=mk([
 ("\"Kemarin\":","yesterday","tomorrow","today","tonight","word."),
 ("\"Semalam\":","last night","tonight","tomorrow night","every night","word."),
 ("\"Bulan lalu\":","last month","next month","this month","every month","word."),
 ("\"Dulu\":","in the past","in the future","now","soon","word."),
 ("\"Tiba\":","arrive","leave","stay","visit","word."),
 ("\"Mengunjungi\":","visit","leave","arrive","stay","word."),
 ("\"Membeli\":","buy","sell","give","take","word."),
 ("\"Menjual\":","sell","buy","give","take","word."),
]))
