from qk import mk, mkf, mko
PASS = dict(practice=mk([
 ('Pilih pasif yang benar: "She was ___ a gift."', "given", "gave", "give", "giving", "was + V3."),
 ('Pilih jawaban yang benar: "My phone ___ stolen." (informal)', "got", "gets", "get", "getting", "get-passive lampau → got stolen."),
 ('Pilih jawaban yang benar: "I had my hair ___ yesterday."', "cut", "cutting", "to cut", "cuts", "have + benda + V3."),
 ('Pilih jawaban yang benar: "We are having the car ___."', "repaired", "repair", "repairing", "repairs", "have + benda + V3."),
 ('Pilih jawaban yang benar: "It ___ said that he is rich."', "is", "are", "has", "does", "It is said that ..."),
 ('Pilih kalimat yang SALAH:', "The accident was happened yesterday.", "The accident happened yesterday.", "The car was damaged.", "The accident was reported.", "happen tidak bisa dipasifkan."),
 ('Pilih kalimat yang SALAH:', "He was died last year.", "He died last year.", "He was fired last year.", "He got fired last year.", "die tidak bisa dipasifkan."),
 ('Pilih kalimat yang benar:', "A gift was given to her.", "A gift gave to her.", "A gift was gave to her.", "A gift is given by her to.", "was + V3."),
]) + mkf([
 ("Dia diberi hadiah.", "She was ___ a gift.", "given", "V3 dari give adalah given."),
 ("Ponselku dicuri. (informal)", "My phone ___ stolen.", "got", "got stolen."),
 ("Aku memotong rambut kemarin (di salon).", "I had my hair ___ yesterday.", "cut", "have + benda + V3."),
 ("Dikatakan bahwa dia kaya.", "It is ___ that he is rich.", "said", "It is said that ..."),
]), quiz=mk([
 ('Pilih jawaban yang benar: "He ___ fired last month." (informal)', "got", "gets", "get", "getting", "got fired."),
 ('Pilih jawaban yang benar: "We had the windows ___."', "cleaned", "clean", "cleaning", "cleans", "have + benda + V3."),
 ('Pilih kalimat yang SALAH:', "It was happened last night.", "It happened last night.", "It was done last night.", "It was reported last night.", "happen tidak bisa dipasifkan."),
]) + mkf([
 ("Dia dikirimi surat.", "He was ___ a letter.", "sent", "V3 dari send adalah sent."),
]))
