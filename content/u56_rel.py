from qk import mk, mkf, mko
REL = dict(practice=mk([
 ('Pilih kata yang tepat: "This chart, ___ shows our sales, covers six months."', "which", "that", "who", "whose is", "Dengan koma → which."),
 ('Pilih kata yang tepat: "The result ___ surprised us was the cost."', "that", "who", "whose", "where", "Benda → that."),
 ('Pilih kata yang tepat: "The team ___ worked on this project is here."', "who", "which", "whose", "where", "Orang → who."),
 ('Pilih kata yang tepat: "The region ___ sales grew fastest is Java."', "where", "whose", "who", "which is", "Tempat → where."),
 ('Pilih kata yang tepat: "The slide, ___ is the last one, shows the main results."', "which", "that", "who", "whose is", "Dengan koma → which."),
 ('Pilih kalimat yang benar:', "The chart that you see shows sales.", "The chart who you see shows sales.", "The chart you see it shows sales.", "The chart that you see it shows sales.", "Benda → that; jangan ulang it."),
 ('Pilih kalimat yang SALAH:', "The chart, that shows sales, is blue.", "The chart, which shows sales, is blue.", "The chart that shows sales is blue.", "The chart showing sales is blue.", "Setelah koma tidak boleh that."),
]) + mkf([
 ("Grafik ini, yang menunjukkan penjualan, mencakup enam bulan.", "This chart, ___ shows our sales, covers six months.", "which", "Dengan koma → which."),
 ("Hasil yang mengejutkan kami adalah biayanya.", "The result ___ surprised us was the cost.", "that/which", "Benda → that atau which."),
 ("Tim yang mengerjakan proyek ini ada di sini.", "The team ___ worked on this project is here.", "who/that", "Orang → who atau that."),
 ("Wilayah tempat penjualan tumbuh paling cepat adalah Jawa.", "The region ___ sales grew fastest is Java.", "where", "Tempat → where."),
]), quiz=mk([
 ('Pilih kata yang tepat: "The client ___ called yesterday wants a quote."', "who", "which", "whose", "where", "Orang → who."),
 ('Pilih kata yang tepat: "The data, ___ is from May, shows growth."', "which", "that", "who", "whose is", "Dengan koma → which."),
 ('Pilih kalimat yang SALAH:', "The speaker, that is tall, starts now.", "The speaker, who is tall, starts now.", "The speaker who is tall starts now.", "The tall speaker starts now.", "Setelah koma tidak boleh that."),
]) + mkf([
 ("Slide yang Anda lihat menunjukkan hasil utama.", "The slide ___ you see shows the main results.", "that/which", "Benda → that atau which."),
]))
