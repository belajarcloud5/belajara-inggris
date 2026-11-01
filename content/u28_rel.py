from qk import mk, mkf, mko
REL = dict(practice=mk([
 ('Pilih kata yang tepat: "I have a friend ___ house is near the beach."', "whose", "who", "which", "where", "Kepemilikan → whose."),
 ('Pilih kata yang tepat: "This is the room ___ I study."', "where", "whose", "who", "which is", "Tempat → where."),
 ('Pilih kata yang tepat: "I remember the day ___ we first met."', "when", "where", "whose", "who", "Waktu → when."),
 ('Pilih kata yang tepat: "The village ___ I was born has a clean river."', "where", "whose", "when", "who", "Tempat → where."),
 ('Pilih kata yang tepat: "The river, ___ water is clean, flows through the village."', "whose", "who", "where", "when", "Kepemilikan → whose."),
 ('Pilih kalimat yang benar:', "She is the girl whose bag is red.", "She is the girl who's bag is red.", "She is the girl whose is bag red.", "She is the girl whom bag is red.", "whose + kata benda."),
 ('Pilih kalimat yang SALAH:', "Who's bag is this?", "Whose bag is this?", "Who's that girl?", "Whose book is on the table?", "Kepemilikan → Whose."),
 ('Pilih kalimat yang SALAH:', "That is the town when I live.", "That is the town where I live.", "That is the day when I arrived.", "That is the town in which I live.", "Tempat → where."),
]) + mkf([
 ("Aku punya teman yang rumahnya dekat pantai.", "I have a friend ___ house is near the beach.", "whose", "Kepemilikan → whose."),
 ("Ini ruangan tempat aku belajar.", "This is the room ___ I study.", "where", "Tempat → where."),
 ("Aku ingat hari ketika kami pertama bertemu.", "I remember the day ___ we first met.", "when", "Waktu → when."),
 ("Desa itu punya sungai yang airnya bersih.", "The village has a river ___ water is clean.", "whose", "Kepemilikan → whose."),
]), quiz=mk([
 ('Pilih kata yang tepat: "Is this the shop ___ you bought the shirt?"', "where", "whose", "when", "who", "Tempat → where."),
 ('Pilih kata yang tepat: "Do you know the girl ___ phone was lost?"', "whose", "who", "where", "when", "Kepemilikan → whose."),
 ('Pilih kalimat yang SALAH:', "The man who's car is red lives here.", "The man whose car is red lives here.", "The man that owns a red car lives here.", "I see the man whose car is red.", "Kepemilikan → whose."),
]) + mkf([
 ("Itu hari ketika kami tiba.", "That is the day ___ we arrived.", "when", "Waktu → when."),
]))
