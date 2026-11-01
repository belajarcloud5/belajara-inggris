from qk import mk, mkf, mko
CONJ = dict(practice=mk([
 ('Pilih kata yang tepat: "Cycling is healthy. ___, it saves money." (lagipula)', "Moreover", "Therefore", "However", "Because", "Menambah argumen → Moreover."),
 ('Pilih kata yang tepat: "There are fewer cars. ___, the air is cleaner." (karena itu)', "Therefore", "Moreover", "However", "Although", "Akibat → Therefore."),
 ('Pilih kata yang tepat: "Cars are fast. ___, they cause pollution." (namun)', "However", "Therefore", "Moreover", "Because", "Pertentangan → However."),
 ('Pilih kata yang tepat: "___, schools should promote cycling." (kesimpulan)', "In conclusion", "However", "In addition", "Because of", "Kesimpulan → In conclusion."),
 ('Pilih kata yang tepat: "We should cycle ___ it is healthy."', "because", "because of", "therefore", "however", "Diikuti klausa → because."),
 ('Pilih kata yang tepat: "We stayed home ___ the rain."', "because of", "because", "therefore", "although", "Diikuti kata benda → because of."),
 ('Pilih kata yang tepat: "___, cycling is cheap. Secondly, it is healthy." (pertama)', "Firstly", "Finally", "Therefore", "However", "Awal argumen → Firstly."),
 ('Pilih kalimat yang benar:', "It rained. Therefore, we stayed home.", "It rained. Therefore we, stayed home.", "It rained therefore. We stayed home.", "It rained, therefore, we stayed home.", "Therefore di awal kalimat baru, diikuti koma."),
 ('Pilih kalimat yang SALAH:', "We stayed home because of it rained.", "We stayed home because of the rain.", "We stayed home because it rained.", "It rained. Therefore, we stayed home.", "because of + kata benda."),
]) + mkf([
 ("Lagipula, bersepeda itu murah.", "___, cycling is cheap.", "Moreover", "Moreover = lagipula."),
 ("Karena itu, udaranya lebih bersih.", "___, the air is cleaner.", "Therefore", "Therefore = karena itu."),
 ("Kami tinggal di rumah karena hujan.", "We stayed home because ___ the rain.", "of", "because of + kata benda."),
 ("Kesimpulannya, kita harus bersepeda.", "In ___, we should cycle.", "conclusion", "In conclusion = kesimpulannya."),
]), quiz=mk([
 ('Pilih kata yang tepat: "He was ill. ___, he missed the exam."', "As a result", "Moreover", "Although", "Unless", "Akibat → As a result."),
 ('Pilih kata yang tepat: "The bus is cheap. ___, it is slow."', "However", "Therefore", "Moreover", "Because", "Pertentangan → However."),
 ('Pilih kata yang tepat: "He missed the exam ___ his illness."', "because of", "because", "therefore", "however", "because of + kata benda."),
]) + mkf([
 ("Pertama, bersepeda menyehatkan.", "___, cycling is healthy.", "Firstly", "Firstly = pertama."),
]))
