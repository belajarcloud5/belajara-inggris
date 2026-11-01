from qk import mk, mkf, mko
REL = dict(practice=mk([
 ('Pilih kata yang tepat: "This is the zoo ___ we saw the lions."', "where", "who", "whose", "which is", "Tempat → where."),
 ('Pilih kata yang tepat: "The animal ___ lives in water is a fish."', "which", "where", "whose", "who is", "Hewan → which."),
 ('Pilih kata yang tepat: "That is the elephant ___ tusk is broken."', "whose", "who", "where", "which", "Kepemilikan → whose."),
 ('Pilih kata yang tepat: "The park ___ we play is near a lake."', "where", "whose", "who", "which is", "Tempat → where."),
 ('Pilih kalimat yang benar:', "The zoo where we went is big.", "The zoo where we went to is big.", "The zoo who we went is big.", "The zoo whose we went is big.", "where tanpa kata depan."),
 ('Pilih kalimat yang benar:', "The zoo which we went to is big.", "The zoo where we went to is big.", "The zoo who we went to is big.", "The zoo whose we went to is big.", "which + kata depan tetap ada."),
 ('Pilih kalimat yang SALAH:', "The bird whose lives here is blue.", "The bird which lives here is blue.", "The bird whose wings are blue lives here.", "I see the bird that lives here.", "whose diikuti kata benda."),
]) + mkf([
 ("Ini kebun binatang tempat kami melihat singa.", "This is the zoo ___ we saw the lions.", "where", "Tempat → where."),
 ("Hewan yang hidup di air adalah ikan.", "The animal ___ lives in water is a fish.", "which/that", "Hewan → which atau that."),
 ("Itu gajah yang gadingnya patah.", "That is the elephant ___ tusk is broken.", "whose", "Kepemilikan → whose."),
 ("Taman tempat kami bermain dekat danau.", "The park ___ we play is near a lake.", "where", "Tempat → where."),
]), quiz=mk([
 ('Pilih kata yang tepat: "The town ___ I live is small."', "where", "which is", "whose", "who", "Tempat → where."),
 ('Pilih kata yang tepat: "The monkey ___ tail is long is funny."', "whose", "where", "who", "which", "Kepemilikan → whose."),
 ('Pilih kalimat yang SALAH:', "The cage where the tiger lives to is big.", "The cage where the tiger lives is big.", "The cage which the tiger lives in is big.", "The cage that holds the tiger is big.", "where tidak diikuti kata depan."),
]) + mkf([
 ("Desa tempat aku lahir sangat kecil.", "The village ___ I was born is very small.", "where", "Tempat → where."),
]))
