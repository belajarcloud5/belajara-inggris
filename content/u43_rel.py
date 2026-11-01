from qk import mk, mkf, mko
REL = dict(practice=mk([
 ('Pilih kalimat yang benar (kata ganti dihilangkan):', "The man I met is here.", "The man who I met he is here.", "The man I met him is here.", "The man met I is here.", "Objek boleh dihilangkan."),
 ('Pilih kalimat yang SALAH:', "The man called you is here.", "The man who called you is here.", "The man I met is here.", "The man that called you is here.", "Subjek tidak boleh dihilangkan."),
 ('Pilih kalimat yang benar:', "The book I read was long.", "The book I read it was long.", "The book read I was long.", "The book that I read it was long.", "Objek dihilangkan, jangan ulang it."),
 ('Pilih kalimat yang benar:', "The woman I spoke to is the manager.", "The woman I spoke is the manager.", "The woman I spoke to her is the manager.", "The woman spoke I to is the manager.", "Kata depan tetap ada."),
 ('Pilih kalimat yang benar:', "The report which was written yesterday is ready.", "The report which written yesterday is ready.", "The report who was written yesterday is ready.", "The report which is write yesterday is ready.", "Pasif: was written."),
 ('Pilih kalimat yang SALAH:', "The house built in 1990 is old.", "The house build in 1990 is old.", "The house which was built in 1990 is old.", "The house that was built in 1990 is old.", "Gunakan V3: built."),
 ('Pilih kata yang tepat: "The report ___ the manager wrote was sent yesterday."', "that", "who", "whose", "where", "Benda → that."),
]) + mkf([
 ("Laporan yang ditulis manajer dikirim kemarin. (kata ganti boleh dihilangkan juga)", "The report ___ the manager wrote was sent yesterday.", "that/which", "Benda → that atau which."),
 ("Rumah yang dibangun tahun 1990 itu sudah tua.", "The house which was ___ in 1990 is old.", "built", "Pasif: was built."),
 ("Laki-laki yang menelepon kamu ada di sini.", "The man ___ called you is here.", "who/that", "Subjek → who atau that."),
 ("Buku yang kubaca sangat panjang.", "The book ___ I read was long.", "that/which", "Objek → that atau which."),
]), quiz=mk([
 ('Pilih kalimat yang benar:', "The film I saw was great.", "The film I saw it was great.", "The film saw I was great.", "The film who I saw was great.", "Objek boleh dihilangkan."),
 ('Pilih kalimat yang SALAH:', "The girl lives here is kind.", "The girl who lives here is kind.", "The girl that lives here is kind.", "The girl I know is kind.", "Subjek tidak boleh dihilangkan."),
 ('Pilih kata yang tepat: "The cake ___ was baked yesterday is gone."', "which", "who", "whose", "where", "Benda → which."),
]) + mkf([
 ("Gedung yang dibangun tahun lalu itu besar.", "The building which was ___ last year is big.", "built", "Pasif: was built."),
]))
