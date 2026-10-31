from qk import mk, mkf, mko
MOV = dict(practice=mk([
 ('Pilih kata yang tepat: "She goes ___ home at five."', "tanpa preposisi", "to", "into", "at", "go home tanpa to."),
 ('Pilih kata yang tepat: "We arrived ___ Bandung at noon."', "in", "at", "to", "into", "Kota → arrive in."),
 ('Pilih kata yang tepat: "We arrived ___ the station at noon."', "at", "in", "to", "into", "Titik kecil → arrive at."),
 ('Pilih kata yang tepat: "He entered ___ the room."', "tanpa preposisi", "into", "to", "in", "enter tanpa preposisi."),
 ('Pilih kata yang tepat: "Get ___ the bus at the next stop. (turun)"', "off", "out of", "down", "from", "Bus, kereta → get off."),
 ('Pilih kata yang tepat: "Get ___ the taxi. (naik)"', "in", "on", "at", "to", "Mobil, taksi → get in."),
 ('Pilih kata yang tepat: "The train goes ___ a tunnel."', "through", "across", "along", "over", "Menembus terowongan → through."),
 ('Pilih kata yang tepat: "We reached ___ the station at noon."', "tanpa preposisi", "to", "at", "into", "reach tanpa preposisi."),
]) + mkf([
 ("Dia berenang menyeberangi sungai.", "He swam ___ the river.", "across", "Menyeberangi → across."),
 ("Kami naik bus ke Bandung.", "We got ___ the bus to Bandung.", "on", "Bus → get on."),
 ("Kami tiba di stasiun pukul dua belas.", "We arrived ___ the station at noon.", "at", "arrive at + titik."),
]) + mko([
 ("Dia pulang pukul lima.", "She goes home at five.", "to", ""),
]), quiz=mk([
 ('Pilih kata yang tepat: "She got ___ of the car."', "out", "off", "from", "down", "Mobil → get out of."),
 ('Pilih kata yang tepat: "They walked ___ the field. (menyeberangi lapangan)"', "across", "through", "into", "to", "Permukaan datar → across."),
]))
