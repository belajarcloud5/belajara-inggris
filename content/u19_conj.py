from qk import mk, mkf, mko
CONJ = dict(practice=mk([
 ('Pilih kata penghubung: "___, a tiger appeared from the bushes." (tiba-tiba)', "Suddenly", "Finally", "First", "Because", "Kejadian mendadak → Suddenly."),
 ('Pilih kata penghubung: "___, the farmer learned his lesson." (akhirnya)', "Finally", "Suddenly", "First", "But", "Akhir cerita → Finally."),
 ('Pilih kata penghubung: "___, he took the egg home. Then he showed it to his wife." (pertama)', "First", "Finally", "Suddenly", "Because", "Awal urutan → First."),
 ('Pilih kata penghubung: "He took the egg home. ___, he showed it to his wife."', "After that", "Because", "Although", "Unless", "Urutan → After that."),
 ('Pilih kata penghubung: "He was angry, ___ he shouted."', "so", "because", "but", "or", "Akibat → so."),
 ('Pilih kata penghubung: "He shouted ___ he was angry."', "because", "so", "then", "but", "Alasan → because."),
 ('Pilih kata penghubung: "The fox was clever, ___ the crow was foolish."', "but", "so", "because", "after that", "Berlawanan → but."),
 ('Pilih kalimat yang benar:', "Suddenly, the door opened.", "Suddenly the, door opened.", "Suddenly, door the opened.", "Sudden, the door opened.", "Suddenly dengan koma."),
]) + mkf([
 ("Suatu hari, seorang petani menemukan telur emas.", "___ day, a farmer found a golden egg.", "One", "One day = suatu hari."),
 ("Tiba-tiba, angsa itu terbang.", "___, the goose flew away.", "Suddenly", "Suddenly = tiba-tiba."),
 ("Akhirnya, dia pulang.", "___, he went home.", "Finally", "Finally = akhirnya."),
 ("Dia marah, jadi dia berteriak.", "He was angry, ___ he shouted.", "so", "Akibat → so."),
]), quiz=mk([
 ('Pilih kata penghubung: "First, he woke up. ___, he took a bath."', "Then", "Because", "Although", "Besides", "Urutan → Then."),
 ('Pilih kata penghubung: "He ran away ___ he was afraid."', "because", "so", "then", "or", "Alasan → because."),
 ('Pilih kata penghubung: "He was afraid, ___ he ran away."', "so", "because", "although", "unless", "Akibat → so."),
]) + mkf([
 ("Pertama, dia mengambil koin itu.", "___, he picked up the coin.", "First", "First = pertama."),
]))
