from qk import mk, mkf, mko
QTY = dict(practice=mk([
 ('Pilih kata yang tepat: "There are ___ cars on Sunday than on Monday." (lebih sedikit)', "fewer", "less", "much", "little", "Cars bisa dihitung → fewer."),
 ('Pilih kata yang tepat: "Please make ___ noise." (lebih sedikit)', "less", "fewer", "many", "few", "Noise tak terhitung → less."),
 ('Pilih kata yang tepat: "There are too ___ people in this room."', "many", "much", "less", "little", "People jamak → too many."),
 ('Pilih kata yang tepat: "There is too ___ sugar in this tea."', "much", "many", "fewer", "few", "Sugar tak terhitung → too much."),
 ('Pilih kata yang tepat: "We have ___ chairs for everyone." (cukup)', "enough", "enoughly", "too", "many enough", "enough diletakkan sebelum benda."),
 ('Pilih kalimat yang benar:', "I have more books than you.", "I have more book than you.", "I have much books than you.", "I have most books than you.", "more + jamak + than."),
 ('Pilih kalimat yang benar:', "She eats less meat than her brother.", "She eats fewer meat than her brother.", "She eats few meat than her brother.", "She eats less meats than her brother.", "Meat tak terhitung → less."),
 ('Pilih kalimat yang benar:', "There are fewer students today.", "There are less students today.", "There is fewer students today.", "There are fewer student today.", "Students jamak → fewer, dengan are."),
 ('Pilih kalimat yang SALAH:', "There is too many traffic.", "There is too much traffic.", "There are too many cars.", "There is not enough space.", "Traffic tak terhitung → too much."),
 ('Pilih kalimat yang SALAH:', "We have not enough time enough.", "We do not have enough time.", "We have enough time.", "We have too little time.", "enough tidak dipakai dua kali."),
]) + mkf([
 ("Ada terlalu banyak mobil di jalan ini.", "There are too ___ cars on this road.", "many", "Cars jamak → too many."),
 ("Ada terlalu banyak kebisingan.", "There is too ___ noise.", "much", "Noise tak terhitung → too much."),
 ("Kurangi gula.", "Eat ___ sugar. (lebih sedikit)", "less", "Sugar tak terhitung → less."),
 ("Hari ini murid yang hadir lebih sedikit.", "There are ___ students today. (lebih sedikit)", "fewer", "Students jamak → fewer."),
 ("Kami punya cukup kursi.", "We have ___ chairs.", "enough", "enough sebelum benda."),
]), quiz=mk([
 ('Pilih kata yang tepat: "I have ___ homework than you." (lebih sedikit)', "less", "fewer", "many", "few", "Homework tak terhitung → less."),
 ('Pilih kata yang tepat: "There are ___ boxes than before." (lebih sedikit)', "fewer", "less", "much", "little", "Boxes jamak → fewer."),
 ('Pilih kalimat yang benar:', "We have too many boxes.", "We have too much boxes.", "We have too boxes many.", "We have too lot boxes.", "Boxes jamak → too many."),
 ('Pilih kalimat yang benar:', "There is not enough water.", "There is not water enough.", "There is not enough of water.", "There are not enough water.", "enough sebelum benda; water tunggal."),
]) + mkf([
 ("Terlalu banyak air.", "There is too ___ water.", "much", "Water tak terhitung → too much."),
 ("Waktu kita tidak cukup.", "We don't have ___ time.", "enough", "enough sebelum benda."),
]))
