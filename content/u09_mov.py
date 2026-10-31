from qk import mk, mkf, mko
MOV = dict(practice=mk([
 ('Pilih kata yang tepat: "She walks ___ the room." (masuk ke dalam)', "into", "to", "through", "across", "Masuk ke dalam ruang → into."),
 ('Pilih kata yang tepat: "The train goes ___ a tunnel."', "through", "across", "along", "over", "Menembus terowongan → through."),
 ('Pilih kata yang tepat: "Walk ___ this street for two blocks."', "along", "through", "into", "over", "Menyusuri jalan → along."),
 ('Pilih kata yang tepat: "Go ___ the bank, then turn left."', "past", "through", "into", "under", "Melewati bank → past."),
 ('Pilih kata yang tepat: "He swam ___ the river."', "across", "through", "into", "along", "Menyeberangi sungai → across."),
 ('Pilih kata yang tepat: "She goes ___ home at five."', "tanpa preposisi", "to", "into", "at", "go home tanpa to."),
 ('Pilih kata yang tepat: "He enters ___ the classroom."', "tanpa preposisi", "into", "to", "in", "enter + tempat tanpa preposisi."),
 ('Pilih kata yang tepat: "Pour the milk ___ the glass."', "into", "to", "across", "past", "Menuang ke dalam wadah → into."),
 ('Pilih kata yang tepat: "He came ___ the shop with a bag."', "out of", "into", "through", "to", "Keluar dari dalam → out of."),
 ('Pilih kata yang tepat: "We arrived ___ the station at noon."', "at", "in", "into", "through", "Titik kecil → arrive at."),
]) + mkf([
 ("Aku berjalan ke sekolah.", "I walk ___ school.", "to", "Tujuan umum → to."),
 ("Dia berjalan masuk ke kamar.", "She walks ___ the room. (masuk ke dalam)", "into", "Masuk ke dalam → into."),
 ("Berjalanlah menyusuri sungai.", "Walk ___ the river. (menyusuri)", "along", "Menyusuri → along."),
]) + mko([
 ("Kucing itu melompat ke atas meja.", "The cat jumped onto the table.", "into", ""),
]), quiz=mk([
 ('Pilih kata yang tepat: "The bridge goes ___ the river."', "over", "into", "to", "out of", "Melintas di atas sungai → over."),
 ('Pilih kata yang tepat: "Walk ___ the park. (mengelilingi)"', "around", "into", "to", "past", "Mengelilingi → around."),
 ('Pilih kata yang tepat: "The bus comes ___ Jakarta."', "from", "to", "into", "through", "Titik asal → from."),
]) + mkf([
 ("Kereta melewati terowongan.", "The train goes ___ a tunnel.", "through", "Menembus terowongan → through."),
]))
