from qk import mk, mkf, mko
CONJ = dict(practice=mk([
 ('Pilih kata yang tepat: "The server is slow ___ there are many users."', "because", "so", "otherwise", "although", "Alasan → because."),
 ('Pilih kata yang tepat: "Many users logged in, ___ the server slowed down."', "so", "because", "otherwise", "unless", "Akibat → so."),
 ('Pilih kata yang tepat: "The system crashed ___ a power cut."', "because of", "because", "so", "although", "because of + kata benda."),
 ('Pilih kata yang tepat: "Restart the server. ___, the problem will continue."', "Otherwise", "Therefore", "Moreover", "Because", "Kalau tidak → Otherwise."),
 ('Pilih kata yang tepat: "We added memory ___ the system runs faster."', "so that", "otherwise", "although", "because of", "Tujuan → so that."),
 ('Pilih kata yang tepat: "We fixed the bug, ___ another problem appeared."', "but", "so", "because", "otherwise", "Berlawanan → but."),
 ('Pilih kata yang tepat: "The system crashed. ___, we lost some data."', "As a result", "Otherwise", "Although", "Unless", "Akibat → As a result."),
 ('Pilih kalimat yang benar:', "The delay was due to the weather.", "The delay was due to it was raining.", "The delay was due to rained.", "The delay was due the weather to.", "due to + kata benda."),
 ('Pilih kalimat yang SALAH:', "We were late because of the traffic was heavy.", "We were late because of the heavy traffic.", "We were late because the traffic was heavy.", "We were late due to the heavy traffic.", "because of + kata benda."),
]) + mkf([
 ("Server lambat karena banyak pengguna.", "The server is slow ___ there are many users.", "because", "Alasan → because."),
 ("Banyak pengguna masuk, jadi server melambat.", "Many users logged in, ___ the server slowed down.", "so", "Akibat → so."),
 ("Sistem mogok karena listrik padam.", "The system crashed due ___ a power cut.", "to", "due to + kata benda."),
 ("Mulai ulang server. Kalau tidak, masalah berlanjut.", "Restart it. ___, the problem will continue.", "Otherwise", "Otherwise = kalau tidak."),
]), quiz=mk([
 ('Pilih kata yang tepat: "The delivery was late ___ the storm."', "because of", "because", "so", "unless", "because of + kata benda."),
 ('Pilih kata yang tepat: "The delivery was late ___ there was a storm."', "because", "because of", "due to", "despite", "because + klausa."),
 ('Pilih kata yang tepat: "The delivery was late, ___ we sent an apology."', "so", "because", "unless", "although", "Akibat → so."),
]) + mkf([
 ("Akibatnya, kami kehilangan sebagian data.", "___, we lost some data.", "As a result", "As a result = akibatnya."),
]))
