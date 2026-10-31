from qk import mk, mkf, mko
ART = dict(practice=mk([
 ('Pilih article yang tepat: "She is ___ engineer."', "an", "a", "the", "no article", "engineer diawali vokal → an."),
 ('Pilih article yang tepat: "We play ___ football every Sunday."', "no article", "a", "an", "the", "Olahraga tanpa article."),
 ('Pilih article yang tepat: "He lives in ___ USA."', "the", "a", "an", "no article", "the USA, the UK, the Netherlands memakai the."),
 ('Pilih article yang tepat: "I visited ___ Indonesia last year."', "no article", "the", "a", "an", "Nama negara tunggal tanpa article."),
 ('Pilih article yang tepat: "My brother eats three times ___ day."', "a", "an", "the", "no article", "a = per."),
 ('Pilih article yang tepat: "What ___ beautiful view!"', "a", "an", "the", "no article", "What a + adjektif + benda tunggal."),
 ('Pilih article yang tepat: "___ Nile is the longest river in Africa."', "The", "A", "An", "No article", "Sungai memakai the."),
 ('Pilih article yang tepat: "She speaks ___ English very well."', "no article", "the", "a", "an", "Nama bahasa tanpa article."),
]) + mkf([
 ("Dia bekerja sebagai dokter.", "She works as ___ doctor.", "a", "Profesi → a."),
 ("Apa pemandangan yang indah!", "What ___ beautiful view!", "a", "What a + adjektif + benda tunggal."),
 ("Kapal itu berlayar di Samudra Pasifik.", "The ship sails across ___ Pacific.", "the", "Samudra memakai the."),
]) + mko([
 ("Aku bermain sepak bola dua kali seminggu.", "I play football twice a week.", "the", ""),
]), quiz=mk([
 ('Pilih article yang tepat: "I waited for ___ hour."', "an", "a", "the", "no article", "h pada hour tidak dibunyikan → an."),
 ('Pilih article yang tepat: "He studies ___ math at school."', "no article", "the", "a", "an", "Pelajaran tanpa article."),
 ('Pilih article yang tepat: "She goes to ___ school by bike every day."', "no article", "the", "a", "an", "Pergi bersekolah → tanpa the."),
]))
