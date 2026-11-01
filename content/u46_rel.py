from qk import mk, mkf, mko
REL = dict(practice=mk([
 ('Pilih jawaban yang benar: "The girl ___ sings in the choir is my cousin."', "who", "which", "whose", "where", "Orang → who."),
 ('Pilih jawaban yang benar: "The song ___ she sings is popular."', "which", "who", "whose", "where", "Benda → which."),
 ('Pilih jawaban yang benar: "The boy ___ bag is lost is crying."', "whose", "who", "which", "where", "Kepemilikan → whose."),
 ('Pilih jawaban yang benar: "The town ___ I live is quiet."', "where", "whose", "who", "which is", "Tempat → where."),
 ('Pilih jawaban yang benar: "My bag, ___ is blue, is new."', "which", "that", "who", "whose is", "Setelah koma → which."),
 ('Pilih kalimat yang SALAH:', "My bag, that is blue, is new.", "My bag, which is blue, is new.", "The bag that I bought is new.", "The bag I bought is new.", "Setelah koma tidak boleh that."),
 ('Pilih kalimat yang SALAH:', "The girl who she lives here is kind.", "The girl who lives here is kind.", "The girl that lives here is kind.", "The girl I know is kind.", "Jangan mengulang kata ganti."),
 ('Pilih kalimat yang SALAH:', "The book who is on the table is mine.", "The book which is on the table is mine.", "The book that is on the table is mine.", "The book on the table is mine.", "Benda → which/that."),
 ('Pilih kalimat yang SALAH:', "The town where I live in is small.", "The town where I live is small.", "The town which I live in is small.", "The town in which I live is small.", "where tidak diikuti kata depan."),
 ('Pilih kalimat yang benar:', "The book I read was good.", "The book I read it was good.", "The book read I was good.", "The book which I read it was good.", "Objek boleh dihilangkan, tanpa it."),
]) + mkf([
 ("Anak laki-laki yang tasnya hilang sedang menangis.", "The boy ___ bag is lost is crying.", "whose", "Kepemilikan → whose."),
 ("Kota tempat aku tinggal tenang.", "The town ___ I live is quiet.", "where", "Tempat → where."),
 ("Tasku, yang berwarna biru, baru.", "My bag, ___ is blue, is new.", "which", "Dengan koma → which."),
 ("Gadis yang bernyanyi itu sepupuku.", "The girl ___ sings is my cousin.", "who/that", "Orang → who atau that."),
]), quiz=mk([
 ('Pilih jawaban yang benar: "I know a man ___ speaks five languages."', "who", "which", "whose", "where", "Orang → who."),
 ('Pilih jawaban yang benar: "This is the house ___ I grew up."', "where", "whose", "who", "which is", "Tempat → where."),
 ('Pilih kalimat yang SALAH:', "The man, that I met, is a doctor.", "The man I met is a doctor.", "The man who I met is a doctor.", "The man, who I met, is a doctor.", "Setelah koma tidak boleh that."),
 ('Pilih jawaban yang benar: "The friend ___ I borrowed the book is abroad."', "from whom", "who from", "whose", "where", "from whom = kepada siapa."),
]) + mkf([
 ("Aku kenal wanita yang tasnya biru.", "I know the woman ___ bag is blue.", "whose", "Kepemilikan → whose."),
 ("Buku yang kubeli kemarin bagus.", "The book ___ I bought yesterday is good.", "that/which", "Benda → that atau which."),
]))
