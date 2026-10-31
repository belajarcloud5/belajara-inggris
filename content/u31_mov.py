from qk import mk, mkf, mko
MOV = dict(practice=mk([
 ('Pilih kata yang tepat: "He walked ___ the dark forest."', "through", "across", "past", "onto", "Menembus hutan → through."),
 ('Pilih kata yang tepat: "She swam ___ the river."', "across", "through", "into", "along", "Menyeberangi sungai → across."),
 ('Pilih kata yang tepat: "The boy climbed ___ the wall."', "over", "into", "along", "to", "Melintasi di atas dinding → over."),
 ('Pilih kata yang tepat: "He crept ___ the cave."', "into", "to", "over", "past", "Masuk ke dalam gua → into."),
 ('Pilih kata yang tepat: "At dawn, he came ___ the cave."', "out of", "into", "across", "through", "Keluar dari gua → out of."),
 ('Pilih kata yang tepat: "They walked ___ a narrow path."', "along", "through", "into", "over", "Menyusuri jalan setapak → along."),
 ('Pilih kata yang tepat: "She ran ___ the old house."', "past", "into", "through", "across", "Melewati rumah → past."),
]) + mkf([
 ("Dia berjalan menembus hutan.", "He walked ___ the forest.", "through", "Menembus hutan → through."),
 ("Dia merangkak masuk ke gua.", "He crept ___ the cave. (masuk ke dalam)", "into", "Masuk ke dalam → into."),
]) + mko([
 ("Dia berenang menyeberangi sungai.", "She swam across the river.", "into", ""),
]), quiz=mk([
 ('Pilih kata yang tepat: "They climbed ___ the hill and ran down the other side."', "up", "through", "into", "past", "Naik bukit → up."),
]))
