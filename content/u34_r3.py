from qk import mk
R3 = dict(practice=mk([
 ("Terjemahan \"Aku sudah membaca buku itu dua kali\":","I have read that book twice.","I read that book two times ago.","I have reading that book twice.","I has read book twice.","tr."),
 ("Terjemahan \"Jika besok cerah, kami akan berkemah\":","If it is sunny tomorrow, we will camp.","If it will sunny tomorrow, we camp.","If sunny tomorrow we would camp.","If it sunny, we camping.","tr."),
 ("Terjemahan \"Rumah itu dibangun oleh ayahnya\":","The house was built by his father.","The house built by his father.","The house is build by father.","The house was build his father.","tr."),
 ("Terjemahan \"Dia lebih rajin daripada saya\":","She is more diligent than me.","She is diligenter than me.","She more diligent me.","She is most diligent than I.","tr."),
 ("Terjemahan \"Tolong buka jendelanya\":","Please open the window.","Please to open window.","Please opening the window.","Please opens window.","tr."),
 ("Terjemahan \"Kami sedang menunggu bus\":","We are waiting for the bus.","We waiting bus.","We are wait for bus.","We wait for the bus now.","tr."),
 ("Perbaiki: \"I am agree with you.\"","I agree with you.","I am agreeing with you.","I agrees with you.","I am agree to you.","fix."),
 ("Perbaiki: \"She go to school yesterday.\"","She went to school yesterday.","She goes to school yesterday.","She goed to school yesterday.","She was go to school.","fix."),
 ("Perbaiki: \"There is many books.\"","There are many books.","There be many books.","There am many books.","There do many books.","fix."),
 ("Perbaiki: \"He is more smarter than me.\"","He is smarter than me.","He is more smart than I.","He is smartest than me.","He is smarter as me.","fix."),
 ("Dialog: \"Did you enjoy the trip?\" – \"___\"","Yes, it was great.","Yes, it is great was.","Yes, I enjoy.","Yes, great.","dialog."),
 ("Dialog: \"What are you going to do?\" – \"___\"","I'm going to study.","I going study.","I am go to study.","I study going.","dialog."),
]), quiz=mk([
 ("\"Bagaimana\":","how","who","where","when","word."),
 ("\"Mengapa\":","why","what","which","whose","word."),
 ("\"Milik siapa\":","whose","who's","whom","which","word."),
 ("\"Yang mana\":","which","what","when","where","word."),
 ("\"Berapa banyak\" (terhitung):","how many","how much","how long","how far","word."),
 ("\"Berapa lama\":","how long","how far","how old","how often","word."),
 ("\"Seberapa sering\":","how often","how far","how long","how old","word."),
 ("\"Seberapa jauh\":","how far","how long","how often","how old","word."),
]))
