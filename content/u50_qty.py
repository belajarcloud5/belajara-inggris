from qk import mk, mkf, mko
QTY = dict(practice=mk([
 ('Pilih kata yang tepat: "Would you like ___ coffee while you wait?"', "some", "any", "many", "a few", "Tawaran → some."),
 ('Pilih kata yang tepat: "Could I have ___ more time, please?"', "some", "any", "many", "few", "Permintaan sopan → some."),
 ('Pilih kata yang tepat: "Do you have ___ questions?"', "any", "some", "much", "a little", "Pertanyaan netral → any."),
 ('Pilih kata yang tepat: "I\'m sorry, I don\'t have ___ free time today."', "any", "some", "many", "a few", "Negatif → any."),
 ('Pilih kata yang tepat: "Do you need ___ help with that?"', "any", "a", "many", "few", "Menawarkan bantuan → any."),
 ('Pilih kata yang tepat: "Could you give me a ___ more minutes?"', "few", "little", "much", "lot", "minutes jamak → a few."),
 ('Pilih kata yang tepat: "I need a ___ more time." (sedikit)', "little", "few", "many", "lot", "time tak terhitung → a little."),
 ('Pilih kalimat yang benar:', "Could I have some water?", "Could I have any water?", "Could I have many water?", "Could I have a few water?", "Permintaan → some."),
 ('Pilih kalimat yang SALAH:', "Would you like any tea?", "Would you like some tea?", "Do you have any tea?", "I don't have any tea.", "Tawaran sopan → some."),
]) + mkf([
 ("Mau kopi?", "Would you like ___ coffee?", "some", "Tawaran → some."),
 ("Apakah Anda punya pertanyaan?", "Do you have ___ questions?", "any", "Pertanyaan → any."),
 ("Saya tidak punya waktu luang.", "I don't have ___ free time.", "any", "Negatif → any."),
 ("Beri saya beberapa menit lagi.", "Please give me a ___ more minutes.", "few", "minutes jamak → a few."),
]), quiz=mk([
 ('Pilih kata yang tepat: "Could I have ___ information about the price?"', "some", "many", "a few", "few", "information tak terhitung, permintaan → some."),
 ('Pilih kata yang tepat: "We don\'t have ___ rooms left."', "any", "some", "a", "much", "Negatif → any."),
 ('Pilih kata yang tepat: "Would you like ___ help?"', "some", "many", "a few", "few", "Tawaran → some."),
]) + mkf([
 ("Maaf, tidak ada kamar tersisa.", "Sorry, we don't have ___ rooms left.", "any", "Negatif → any."),
]))
