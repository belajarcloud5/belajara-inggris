from qk import mk, mkf, mko
ART = dict(practice=mk([
 ('Pilih article yang tepat: "Dina is ___ tallest girl in the class."', "the", "a", "an", "no article", "Superlatif → the."),
 ('Pilih article yang tepat: "This is ___ best day of my life."', "the", "a", "an", "no article", "Superlatif → the."),
 ('Pilih article yang tepat: "He is ___ taller boy than me."', "a", "an", "the", "no article", "Komparatif biasa, salah satu dari banyak → a."),
 ('Pilih article yang tepat: "Mount Everest is ___ highest mountain in the world."', "the", "a", "an", "no article", "Superlatif → the."),
 ('Pilih article yang tepat: "She was ___ first student to arrive."', "the", "a", "an", "no article", "Urutan (first) → the."),
 ('Pilih article yang tepat: "It is ___ same color as mine."', "the", "a", "an", "no article", "the same → the."),
]) + mkf([
 ("Dia siswa paling pandai.", "She is ___ smartest student.", "the", "Superlatif → the."),
 ("Bulan mengelilingi Bumi.", "___ moon goes around the Earth.", "The", "Benda unik → the."),
 ("Ini sepeda yang lebih bagus.", "This is ___ better bike.", "a", "Komparatif + benda tunggal → a."),
]) + mko([
 ("Dia anak tertinggi di kelas.", "He is the tallest boy in the class.", "a", ""),
]), quiz=mk([
 ('Pilih article yang tepat: "That was ___ worst movie I have ever seen."', "the", "a", "an", "no article", "Superlatif → the."),
 ('Pilih article yang tepat: "Look at ___ sky. It is so blue."', "the", "a", "an", "no article", "Benda unik → the."),
]))
