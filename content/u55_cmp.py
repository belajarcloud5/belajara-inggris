from qk import mk, mkf, mko
CMP = dict(practice=mk([
 ('Pilih jawaban yang benar: "Sales in June were 20% ___ than in May."', "higher", "more high", "highest", "high", "-er + than."),
 ('Pilih jawaban yang benar: "Java is ___ as large as Bali." (dua kali)', "twice", "two", "second", "double of", "twice as ... as."),
 ('Pilih jawaban yang benar: "The ___ sales were recorded in December."', "highest", "higher", "most high", "high", "the + superlatif."),
 ('Pilih jawaban yang benar: "Costs were ___ lower." (secara signifikan)', "significantly", "significant", "most", "very", "significantly + comparative."),
 ('Pilih jawaban yang benar: "Surabaya is the second ___ city."', "largest", "larger", "most large", "large", "the second + superlatif."),
 ('Pilih jawaban yang benar: "Profit was ___ higher than last year." (sedikit)', "slightly", "very", "most", "too", "slightly + comparative."),
 ('Pilih kalimat yang SALAH:', "Sales were more higher than last year.", "Sales were higher than last year.", "Sales were the highest in June.", "Sales were 10% higher.", "Jangan dobel."),
 ('Pilih kalimat yang SALAH:', "Costs were the more expensive ever.", "Costs were the most expensive ever.", "Costs were higher than before.", "Costs were as high as last year.", "the most expensive."),
]) + mkf([
 ("Penjualan Juni 20% lebih tinggi daripada Mei.", "Sales in June were 20% ___ than in May.", "higher", "-er + than."),
 ("Jawa dua kali sebesar Bali.", "Java is ___ as large as Bali.", "twice", "twice as ... as."),
 ("Penjualan tertinggi tercatat pada bulan Desember.", "The ___ sales were recorded in December.", "highest", "the + superlatif."),
 ("Surabaya adalah kota terbesar kedua.", "Surabaya is the second ___ city.", "largest", "the second + superlatif."),
]), quiz=mk([
 ('Pilih jawaban yang benar: "Profit was 5% ___ than last year." (lebih rendah)', "lower", "more low", "lowest", "low", "-er + than."),
 ('Pilih jawaban yang benar: "This is the ___ figure ever." (terendah)', "lowest", "lower", "most low", "low", "the + superlatif."),
 ('Pilih kalimat yang SALAH:', "Sales were very higher than last year.", "Sales were much higher than last year.", "Sales were slightly higher than last year.", "Sales were higher than last year.", "Jangan very + comparative."),
]) + mkf([
 ("Biaya secara signifikan lebih rendah.", "Costs were ___ lower.", "significantly", "significantly + comparative."),
]))
