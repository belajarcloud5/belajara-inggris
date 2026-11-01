from qk import mk, mkf, mko
PHV = dict(practice=mk([
 ('Pilih phrasal verb yang tepat: "I\'ll ___ you ___ at five." (menelepon balik)', 'call / back', 'pick / up', 'wake / up', 'see / off', 'call back.'),
 ('Pilih phrasal verb yang tepat: "Don\'t ___ , please." (menutup telepon)', 'hang up', 'hang on', 'hang out', 'sit down', 'hang up = menutup telepon.'),
 ('Pilih phrasal verb yang tepat: "___ , please. I\'ll check." (tunggu)', 'Hold on', 'Look after', 'Hold off', 'Fill in', 'hold on = tunggu sebentar.'),
 ('Pilih phrasal verb yang tepat: "She ___ the phone." (mengangkat)', "picked up", "picked on", "picked out", "picked at", "pick up the phone."),
 ('Pilih phrasal verb yang tepat: "I\'ll ___ you ___ to Mr. Hadi." (menyambungkan)', 'put / through', 'call / back', 'pick / up', 'wake / up', 'put through.'),
 ('Pilih phrasal verb yang tepat: "Could you ___ , please? I can\'t hear." (bicara lebih keras)', 'speak up', 'hand in', 'fill in', 'throw away', 'speak up.'),
 ('Pilih kalimat yang SALAH:', "Hold off, please.", "Hold on, please.", "Please hold on.", "Could you hold on?", "hold on = tunggu."),
 ('Pilih kalimat yang SALAH:', "I\'ll put through you.", "I\'ll put you through.", "I\'ll put you through to him.", "I\'ll put him through.", "Kata ganti di tengah."),
]) + mkf([
 ("Saya akan menelepon balik.", "I'll call you ___.", "back", "call back."),
 ("Jangan tutup telepon.", "Don't hang ___.", "up", "hang up."),
 ("Mohon tunggu sebentar.", "Please hold ___.", "on", "hold on."),
 ("Saya akan menyambungkan Anda.", "I'll put you ___.", "through", "put through."),
]), quiz=mk([
 ('Pilih phrasal verb yang tepat: "Could you ___ ? It\'s noisy." (bicara lebih keras)', 'speak up', 'fill in', 'give back', 'look after', 'speak up.'),
 ('Pilih phrasal verb yang tepat: "She ___ when she was angry." (menutup telepon)', 'hung up', 'hung on', 'hung out', 'sat down', 'hang up.'),
 ('Pilih kalimat yang SALAH:', "Please hang on up.", "Please hang up.", "Please hold on.", "Please call back.", "hang up / hold on."),
]) + mkf([
 ("Dia mengangkat telepon.", "She picked ___ the phone.", "up", "pick up."),
]))
