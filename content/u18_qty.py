from qk import mk, mkf, mko
QTY = dict(practice=mk([
 ('Pilih kata yang tepat: "You should drink a ___ of water."', "lot", "many", "few", "much", "a lot of = banyak."),
 ('Pilih kata yang tepat: "Don\'t eat too ___ sweets." (terlalu banyak)', "many", "much", "little", "less", "Sweets jamak → too many."),
 ('Pilih kata yang tepat: "Don\'t eat too ___ sugar."', "much", "many", "few", "fewer", "Sugar tak terhitung → too much."),
 ('Pilih kata yang tepat: "Do you have ___ pain in your stomach?"', "any", "some", "a", "many", "Pertanyaan → any."),
 ('Pilih kata yang tepat: "Take ___ rest, and you will feel better." (sedikit)', "a little", "a few", "many", "few", "Rest tak terhitung → a little."),
 ('Pilih kata yang tepat: "Take ___ tablets a day." (beberapa)', "a few", "a little", "much", "a lot", "Tablets jamak → a few."),
 ('Pilih kalimat yang benar:', "I don't have any fever.", "I don't have some fever.", "I don't have a fevers.", "I don't have many fever.", "Negatif → any."),
 ('Pilih kalimat yang benar:', "Would you like some tea?", "Would you like any tea?", "Would you like many tea?", "Would you like a few tea?", "Tawaran → some."),
 ('Pilih kalimat yang SALAH:', "You should eat much vegetables.", "You should eat a lot of vegetables.", "You should eat some vegetables.", "You should not eat too much oil.", "Kalimat positif → a lot of, dan vegetables jamak."),
]) + mkf([
 ("Minumlah banyak air.", "Drink a lot ___ water.", "of", "a lot of = banyak."),
 ("Aku tidak demam lagi.", "I don't have ___ fever now.", "any", "Negatif → any."),
 ("Istirahatlah sedikit.", "Take a ___ rest.", "little", "Rest tak terhitung → a little."),
 ("Jangan makan terlalu banyak permen.", "Don't eat too ___ candies.", "many", "Candies jamak → too many."),
]), quiz=mk([
 ('Pilih kata yang tepat: "I don\'t drink ___ coffee."', "much", "many", "a few", "some", "Coffee tak terhitung, negatif → much."),
 ('Pilih kalimat yang benar:', "I have a little cough.", "I have a few cough.", "I have many cough.", "I have a lot cough.", "Cough tak terhitung → a little."),
 ('Pilih kata yang tepat: "Do you take ___ medicine?"', "any", "a", "many", "few", "Pertanyaan → any."),
]) + mkf([
 ("Aku minum beberapa tablet.", "I take a ___ tablets.", "few", "Tablets jamak → a few."),
]))
