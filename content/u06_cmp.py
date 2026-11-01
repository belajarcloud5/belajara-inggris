from qk import mk, mkf, mko
CMP = dict(practice=mk([
 ('Pilih jawaban yang benar: "My bag is ___ yours." (sama dengan)', "the same as", "the same like", "same as", "same with", "the same as."),
 ('Pilih jawaban yang benar: "Dina is ___ her sister." (berbeda dari)', "different from", "different of", "different at", "different about", "different from."),
 ('Pilih jawaban yang benar: "Her hair is ___ mine." (mirip)', "similar to", "similar from", "similar of", "similar than", "similar to."),
 ('Pilih jawaban yang benar: "She looks ___ her mother." (seperti)', "like", "as", "than", "from", "look like."),
 ('Pilih jawaban yang benar: "Rani is as tall ___ Dina."', "as", "than", "like", "from", "as ... as."),
 ('Pilih kalimat yang SALAH:', "My bag is the same like yours.", "My bag is the same as yours.", "My bag is similar to yours.", "My bag is different from yours.", "the same as, bukan the same like."),
 ('Pilih kalimat yang SALAH:', "He is more taller than me.", "He is taller than me.", "He looks like me.", "He is as tall as me.", "Jangan dobel more dan -er."),
]) + mkf([
 ("Tasku sama dengan tasmu.", "My bag is the same ___ yours.", "as", "the same as."),
 ("Dina berbeda dari kakaknya.", "Dina is different ___ her sister.", "from/to", "different from."),
 ("Rambutnya mirip rambutku.", "Her hair is similar ___ mine.", "to", "similar to."),
 ("Rani setinggi Dina.", "Rani is as tall ___ Dina.", "as", "as ... as."),
]), quiz=mk([
 ('Pilih jawaban yang benar: "This shirt is ___ that one." (sama)', "the same as", "the same like", "same with", "same than", "the same as."),
 ('Pilih jawaban yang benar: "My brother is ___ me." (berbeda dari)', "different from", "different of", "different than to", "different as", "different from."),
 ('Pilih kalimat yang SALAH:', "She is same as her mother.", "She is the same as her mother.", "She looks like her mother.", "She is similar to her mother.", "the same as."),
]) + mkf([
 ("Dia mirip ibunya.", "She looks ___ her mother.", "like", "look like."),
]))
