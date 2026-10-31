from qk import mk
R3 = dict(practice=mk([
 ("Terjemahan \"Saya akan pergi ke Bali bulan depan\":","I will go to Bali next month.","I will went to Bali next month.","I going Bali next month.","I will to go Bali.","tr."),
 ("Terjemahan \"Dia akan menjadi dokter\":","She is going to be a doctor.","She going be doctor.","She will to be doctor.","She is go to be doctor.","tr."),
 ("Terjemahan \"Mereka tidak akan datang\":","They won't come.","They don't will come.","They not will come.","They will not to come.","tr."),
 ("Terjemahan \"Akankah besok hujan?\":","Will it rain tomorrow?","It will rain tomorrow?","Does it will rain tomorrow?","Will it rains tomorrow?","tr."),
 ("Terjemahan \"Kami akan mengunjungi nenek\":","We are going to visit Grandma.","We going visit Grandma.","We will visiting Grandma.","We are visit Grandma going.","tr."),
 ("Terjemahan \"Saya berencana belajar keras\":","I am going to study hard.","I going study hard.","I am go study hard.","I plan to studying hard.","tr."),
 ("Perbaiki: \"She will goes tomorrow.\"","She will go tomorrow.","She will goes tomorrow.","She wills go tomorrow.","She will to go tomorrow.","fix."),
 ("Perbaiki: \"I am going buy a book.\"","I am going to buy a book.","I going to buy book.","I am go to buy.","I am going buying a book.","fix."),
 ("Perbaiki: \"Will you to help me?\"","Will you help me?","Will you helping me?","Do you will help me?","You will help me?","fix."),
 ("Perbaiki: \"He don't will come.\"","He won't come.","He doesn't will come.","He not will come.","He will don't come.","fix."),
 ("Dialog: \"What are you going to do tomorrow?\" – \"___\"","I'm going to visit my uncle.","I visited my uncle.","I going visit uncle.","I am visit tomorrow.","dialog."),
 ("Dialog: \"Will you come to the party?\" – \"___\"","Yes, I will.","Yes, I do.","Yes, I am.","Yes, I come.","dialog."),
]), quiz=mk([
 ("\"Besok\":","tomorrow","yesterday","today","tonight","word."),
 ("\"Lusa\":","the day after tomorrow","the day before yesterday","tomorrow","next week","word."),
 ("\"Tahun depan\":","next year","last year","this year","every year","word."),
 ("\"Nanti malam\":","tonight","last night","every night","yesterday night","word."),
 ("\"Cita-cita\":","ambition","action","vacation","station","word."),
 ("\"Berencana\":","plan","pray","play","pull","word."),
 ("\"Berharap\":","hope","hop","hold","heat","word."),
 ("\"Janji\":","promise","problem","project","practice","word."),
]))
