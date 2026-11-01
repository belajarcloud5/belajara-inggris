from qk import mk, mkf, mko
REL = dict(practice=mk([
 ('Pilih kata yang tepat: "Rain, ___ is made of water, falls from clouds." (dengan koma)', "which", "that", "who", "whose is", "Setelah koma → which."),
 ('Pilih kata yang tepat: "Mount Merapi, ___ is in Java, is active." (dengan koma)', "which", "that", "who", "where is", "Setelah koma → which."),
 ('Pilih kata yang tepat: "The Earth, ___ is our home, has a layer of air."', "which", "that", "who", "whose", "Setelah koma → which."),
 ('Pilih kata yang tepat: "The sun heats the sea, ___ creates vapor." (seluruh kalimat)', "which", "that", "who", "whose", "Menjelaskan seluruh kalimat → which."),
 ('Pilih kalimat yang benar:', "My bag, which is blue, is new.", "My bag, that is blue, is new.", "My bag which, is blue, is new.", "My bag, who is blue, is new.", "Dengan koma → which."),
 ('Pilih kalimat yang SALAH:', "Mount Merapi, that is in Java, is active.", "Mount Merapi, which is in Java, is active.", "The mountain that erupted was Merapi.", "Merapi, which erupts often, is famous.", "Setelah koma tidak boleh that."),
 ('Pilih kalimat yang SALAH:', "My brother, who is a doctor, live in Bali.", "My brother, who is a doctor, lives in Bali.", "My brother who is a doctor lives in Bali.", "My sister, who is tall, lives in Bali.", "Kata kerja utama harus lives."),
]) + mkf([
 ("Hujan, yang terbuat dari air, jatuh dari awan.", "Rain, ___ is made of water, falls from clouds.", "which", "Dengan koma → which."),
 ("Bumi, yang adalah rumah kita, punya lapisan udara.", "The Earth, ___ is our home, has a layer of air.", "which", "Dengan koma → which."),
 ("Kakakku, yang seorang dokter, tinggal di Bali.", "My brother, ___ is a doctor, lives in Bali.", "who", "Orang dengan koma → who."),
 ("Matahari memanaskan laut, yang menghasilkan uap.", "The sun heats the sea, ___ creates vapor.", "which", "Seluruh kalimat → which."),
]), quiz=mk([
 ('Pilih kata yang tepat: "The Nile, ___ is very long, flows through Egypt."', "which", "that", "who", "whose is", "Setelah koma → which."),
 ('Pilih kata yang tepat: "My teacher, ___ lives near here, is kind."', "who", "that", "which", "where", "Orang dengan koma → who."),
 ('Pilih kalimat yang SALAH:', "Jakarta, that is the capital, is big.", "Jakarta, which is the capital, is big.", "The city that I like is Jakarta.", "Jakarta, which is crowded, is big.", "Setelah koma tidak boleh that."),
]) + mkf([
 ("Danau itu, yang sangat dalam, dingin.", "The lake, ___ is very deep, is cold.", "which", "Dengan koma → which."),
]))
