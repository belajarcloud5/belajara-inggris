from qk import mk, mkf, mko
CMP = dict(practice=mk([
 ('Pilih jawaban yang benar: "This option is ___ cheaper." (jauh lebih)', "much", "very", "most", "more much", "much + comparative."),
 ('Pilih jawaban yang benar: "Sales are ___ higher." (sedikit lebih)', "slightly", "very", "most", "too", "slightly + comparative."),
 ('Pilih jawaban yang benar: "It is ___ as expensive as that one." (dua kali)', "twice", "two", "second", "double of", "twice as ... as."),
 ('Pilih jawaban yang benar: "It is ___ more popular now." (bahkan)', "even", "very", "most", "much of", "even + comparative."),
 ('Pilih jawaban yang benar: "Our design is a bit ___ than the old one."', "lighter", "light", "lightest", "more light", "-er + than."),
 ('Pilih kalimat yang SALAH:', "This bag is very bigger than that.", "This bag is much bigger than that.", "This bag is far bigger than that.", "This bag is a lot bigger than that.", "Jangan very + comparative."),
 ('Pilih kalimat yang SALAH:', "It is much more better.", "It is much better.", "It is far better.", "It is a lot better.", "Jangan dobel."),
]) + mkf([
 ("Opsi ini jauh lebih murah.", "This option is ___ cheaper.", "much/far", "much atau far."),
 ("Penjualan sedikit lebih tinggi.", "Sales are ___ higher.", "slightly", "slightly + comparative."),
 ("Ini dua kali lebih mahal.", "It is ___ as expensive as that.", "twice", "twice as ... as."),
 ("Ini bahkan lebih populer.", "It is ___ more popular now.", "even", "even + comparative."),
]), quiz=mk([
 ('Pilih jawaban yang benar: "The new phone is ___ faster than the old one." (jauh lebih)', "much", "very", "most", "too", "much + comparative."),
 ('Pilih jawaban yang benar: "The room is ___ bigger." (sedikit)', "a bit", "very", "most", "more", "a bit + comparative."),
 ('Pilih kalimat yang SALAH:', "It is very better than before.", "It is much better than before.", "It is a bit better than before.", "It is far better than before.", "Jangan very + comparative."),
]) + mkf([
 ("Itu jauh lebih cepat.", "That is a ___ faster.", "lot", "a lot + comparative."),
]))
