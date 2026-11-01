from qk import mk, mkf, mko
PHV = dict(practice=mk([
 ('Pilih phrasal verb yang tepat: "The server ___ last night." (mogok)', "broke down", "broke up with", "broke off", "broke in at", "break down = mogok."),
 ('Pilih phrasal verb yang tepat: "We ___ memory." (kehabisan)', "ran out of", "ran into at", "ran off", "ran on at", "run out of = kehabisan."),
 ('Pilih phrasal verb yang tepat: "We ___ the cause." (menemukan)', "figured out", "figured in at", "figured on", "figured off", "figure out."),
 ('Pilih phrasal verb yang tepat: "Let\'s ___ testing." (melanjutkan)', "carry on", "carry in at", "carry off", "carry up", "carry on = melanjutkan."),
 ('Pilih phrasal verb yang tepat: "Please ___ your files." (mencadangkan)', "back up", "back off", "back in at", "back on", "back up = mencadangkan."),
 ('Pilih phrasal verb yang tepat: "We\'ll ___ the problem today." (menyelesaikan)', "sort out", "sort in at", "sort off", "sort on", "sort out."),
 ('Pilih kalimat yang SALAH:', "We figured out it.", "We figured it out.", "We figured out the cause.", "We figured the cause out.", "Kata ganti di tengah."),
 ('Pilih kalimat yang SALAH:', "Please back up them.", "Please back them up.", "Please back up your files.", "Please back your files up.", "Kata ganti di tengah."),
]) + mkf([
 ("Server mogok semalam.", "The server broke ___ last night.", "down", "break down."),
 ("Kami kehabisan memori.", "We ran ___ of memory.", "out", "run out of."),
 ("Kami menemukan penyebabnya.", "We figured ___ the cause.", "out", "figure out."),
 ("Tolong cadangkan berkasmu.", "Please back ___ your files.", "up", "back up."),
]), quiz=mk([
 ('Pilih phrasal verb yang tepat: "We\'ll ___ it ___ soon." (menyelesaikan)', "sort / out", "sort / in at", "sort / off", "sort / on", "sort out."),
 ('Pilih phrasal verb yang tepat: "The printer ___ ." (mogok)', "broke down", "broke out of", "broke in", "broke through", "break down."),
 ('Pilih kalimat yang SALAH:', "We sorted out it.", "We sorted it out.", "We sorted out the problem.", "We sorted the problem out.", "Kata ganti di tengah."),
]) + mkf([
 ("Kami akan menyelesaikan masalah itu hari ini.", "We'll sort ___ the problem today.", "out", "sort out."),
]))
