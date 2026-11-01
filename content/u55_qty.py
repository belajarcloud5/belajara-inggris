from qk import mk, mkf, mko
QTY = dict(practice=mk([
 ('Pilih kata yang tepat: "The ___ of customers rose by ten percent."', "number", "amount", "much", "lot", "Customers bisa dihitung → the number of."),
 ('Pilih kata yang tepat: "The ___ of waste fell this year."', "amount", "number", "many", "few", "Waste tak terhitung → the amount of."),
 ('Pilih kata yang tepat: "There were ___ errors this month than last month." (lebih sedikit)', "fewer", "less", "much", "little", "Errors jamak → fewer."),
 ('Pilih kata yang tepat: "We spent ___ money on travel." (lebih sedikit)', "less", "fewer", "many", "few", "Money tak terhitung → less."),
 ('Pilih kata yang tepat: "The number of orders ___ rising."', "is", "are", "were", "have been", "The number of → kata kerja tunggal."),
 ('Pilih kata yang tepat: "A number of orders ___ delayed."', "are", "is", "was", "has been", "A number of → jamak."),
 ('Pilih kata yang tepat: "___ of the sales came from Java." (sebagian besar)', "Most", "Much", "Many", "Few", "most of the = sebagian besar."),
 ('Pilih kalimat yang SALAH:', "The amount of customers is rising.", "The number of customers is rising.", "The amount of waste is falling.", "A number of customers are leaving.", "Customers bisa dihitung → the number of."),
 ('Pilih kalimat yang SALAH:', "We had less complaints this month.", "We had fewer complaints this month.", "We spent less time on each one.", "There were many complaints last year.", "Complaints jamak → fewer."),
]) + mkf([
 ("Jumlah pesanan naik.", "The ___ of orders rose.", "number", "the number of + jamak."),
 ("Jumlah sampah turun.", "The ___ of waste fell.", "amount", "the amount of + tak terhitung."),
 ("Ada lebih sedikit keluhan bulan ini.", "There were ___ complaints this month. (lebih sedikit)", "fewer", "Complaints jamak → fewer."),
 ("Kami memakai lebih sedikit waktu.", "We used ___ time. (lebih sedikit)", "less", "Time tak terhitung → less."),
]), quiz=mk([
 ('Pilih kata yang tepat: "The number of visitors ___ high."', "is", "are", "were", "have been", "The number of → tunggal."),
 ('Pilih kata yang tepat: "There were ___ sales in June than in May." (lebih sedikit)', "fewer", "less", "much", "little", "Sales jamak → fewer."),
 ('Pilih kata yang tepat: "Not ___ customers came on Monday."', "many", "much", "a little", "less", "Customers jamak, negatif → many."),
]) + mkf([
 ("Sebagian besar penjualan datang dari Jawa.", "___ of the sales came from Java.", "Most", "most of the."),
]))
