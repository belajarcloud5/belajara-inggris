from qk import mk, mkf, mko
QTY = dict(practice=mk([
 ('Pilih jawaban yang benar: "There aren\'t ___ chairs in the hall."', "many", "much", "little", "a little", "Chairs jamak, negatif → many."),
 ('Pilih jawaban yang benar: "There isn\'t ___ time left."', "much", "many", "few", "a few", "Time tak terhitung, negatif → much."),
 ('Pilih jawaban yang benar: "___ people came, so the hall was almost empty." (hampir tidak ada)', "Few", "A few", "Little", "A little", "Few + jamak, bermakna hampir tidak ada."),
 ('Pilih jawaban yang benar: "I have ___ money left. Let\'s buy a snack." (ada, walau sedikit)', "a little", "a few", "few", "many", "Money tak terhitung, ada → a little."),
 ('Pilih jawaban yang benar: "She has ___ homework today."', "a lot of", "many", "a few", "fewer", "Positif → a lot of."),
 ('Pilih jawaban yang benar: "Is there ___ sugar in the tea?"', "any", "some", "many", "a few", "Pertanyaan → any."),
 ('Pilih jawaban yang benar: "Would you like ___ cake?"', "some", "any", "many", "few", "Tawaran → some."),
 ('Pilih jawaban yang benar: "Every ___ has to bring a pen."', "student", "students", "of student", "the students", "every + tunggal."),
 ('Pilih jawaban yang benar: "The number of visitors ___ rising."', "is", "are", "were", "have", "The number of + kata kerja tunggal."),
 ('Pilih jawaban yang benar: "A number of visitors ___ waiting outside."', "are", "is", "was", "has", "A number of = beberapa → kata kerja jamak."),
 ('Pilih kalimat yang SALAH:', "He gave me many advice.", "He gave me a lot of advice.", "He gave me some advice.", "He gave me a piece of advice.", "advice tak terhitung → bukan many."),
 ('Pilih kalimat yang SALAH:', "There are too much cars.", "There are too many cars.", "There is too much traffic.", "There are not enough parking spaces.", "Cars jamak → too many."),
]) + mkf([
 ("Tidak ada banyak waktu.", "We don't have ___ time.", "much", "Time tak terhitung → much."),
 ("Hanya sedikit orang yang tahu.", "___ people know the answer. (hampir tidak ada)", "few", "Few + jamak."),
 ("Jumlah murid sedang naik.", "The ___ of students is rising.", "number", "the number of."),
 ("Setiap murid punya buku.", "Every student ___ a book.", "has", "every + tunggal."),
]), quiz=mk([
 ('Pilih jawaban yang benar: "How ___ students are in your class?"', "many", "much", "little", "a little", "Students jamak → How many."),
 ('Pilih jawaban yang benar: "How ___ homework do you have?"', "much", "many", "few", "a few", "Homework tak terhitung → How much."),
 ('Pilih jawaban yang benar: "There is ___ hope. We should try something else." (hampir tidak ada)', "little", "a little", "a few", "many", "little tanpa a bermakna hampir tidak ada."),
 ('Pilih jawaban yang benar: "She doesn\'t have ___ friends."', "any", "some", "a", "much", "Negatif → any."),
]) + mkf([
 ("Dia punya beberapa teman.", "She has a ___ friends.", "few", "a few + jamak."),
 ("Ada terlalu banyak kendaraan.", "There are too ___ vehicles.", "many", "Vehicles jamak → too many."),
]))
