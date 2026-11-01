from qk import mk, mkf, mko
MODAL = dict(practice=mk([
 ('Pilih jawaban yang benar: "You ___ wear a helmet. It is the rule." (perlu)', "need to", "needn't", "ought", "had better to", "Perlu → need to."),
 ('Pilih jawaban yang benar: "You ___ bring a pen. We have plenty." (tidak perlu)', "needn't", "mustn't", "ought to", "had better", "Tidak perlu → needn't."),
 ('Pilih jawaban yang benar: "You ___ to rest. You look tired." (sebaiknya)', "ought", "had better", "must", "need", "ought to + V1."),
 ('Pilih jawaban yang benar: "You ___ leave now, or you will be late."', "had better", "ought", "needn't", "are able", "Peringatan kuat → had better."),
 ('Pilih jawaban yang benar: "You had better ___ late."', "not be", "not to be", "don't be", "no be", "had better not + V1."),
 ('Pilih kalimat yang benar:', "You had better go now.", "You had better to go now.", "You had better going now.", "You better go to now.", "had better + V1 tanpa to."),
 ('Pilih kalimat yang SALAH:', "You ought study more.", "You ought to study more.", "You should study more.", "You need to study more.", "ought diikuti to."),
 ('Pilih kalimat yang benar:', "You needn't hurry.", "You needn't to hurry.", "You needn't hurrying.", "You not need hurry.", "needn't + V1."),
]) + mkf([
 ("Kamu perlu memakai helm.", "You ___ to wear a helmet.", "need", "need to."),
 ("Kamu tidak perlu terburu-buru.", "You ___ hurry.", "needn't", "needn't + V1."),
 ("Sebaiknya kamu pergi sekarang.", "You had ___ go now.", "better", "had better."),
 ("Kamu sebaiknya beristirahat.", "You ought ___ rest.", "to", "ought to."),
]), quiz=mk([
 ('Pilih jawaban yang benar: "You ___ run in the corridor." (dilarang)', "mustn't", "needn't", "ought to", "had better to", "Larangan → mustn't."),
 ('Pilih jawaban yang benar: "You ___ come early. The class starts at ten." (tidak perlu)', "don't need to", "mustn't", "ought to", "had better", "Tidak perlu → don't need to."),
 ('Pilih kalimat yang SALAH:', "You had better to wear a coat.", "You had better wear a coat.", "You should wear a coat.", "You ought to wear a coat.", "had better tanpa to."),
]) + mkf([
 ("Sebaiknya kamu tidak terlambat.", "You had better ___ be late.", "not", "had better not."),
]))
