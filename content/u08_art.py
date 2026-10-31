from qk import mk, mkf, mko
ART = dict(practice=mk([
 ('Pilih article yang tepat: "We have ___ breakfast at six."', "no article", "a", "an", "the", "Waktu makan umumnya tanpa article."),
 ('Pilih article yang tepat: "I\'d like ___ egg, please."', "an", "a", "the", "no article", "egg diawali vokal → an."),
 ('Pilih article yang tepat: "She drinks ___ water every day."', "no article", "a", "an", "the", "water tak terhitung dan umum → tanpa article."),
 ('Pilih article yang tepat: "I bought a cake. ___ cake was delicious."', "The", "A", "An", "No article", "Kue yang sudah disebut → the."),
 ('Pilih article yang tepat: "Could you pass me ___ salt on the table?"', "the", "a", "an", "no article", "Garam yang tertentu, di meja → the."),
 ('Pilih article yang tepat: "We had ___ big lunch yesterday."', "a", "an", "the", "no article", "Ada kata sifat big di depan lunch → a."),
]) + mkf([
 ("Aku mau segelas air.", "I'd like ___ glass of water.", "a", "glass diawali konsonan → a."),
 ("Dia makan sebutir apel.", "She ate ___ apple.", "an", "apple diawali vokal → an."),
 ("Nasi di meja itu dingin.", "___ rice on the table is cold.", "The", "Nasi yang tertentu → the."),
]) + mko([
 ("Aku makan sebuah sandwich.", "I ate a sandwich.", "an", ""),
 ("Kami makan siang pukul dua belas.", "We have lunch at twelve.", "the", ""),
]), quiz=mk([
 ('Pilih article yang tepat: "I like ___ fruit."', "no article", "a", "an", "the", "fruit umum dan tak terhitung → tanpa article."),
 ('Pilih article yang tepat: "Let\'s have ___ dinner together."', "no article", "a", "an", "the", "Waktu makan → tanpa article."),
]) + mkf([
 ("Aku makan sebuah sandwich. Sandwichnya enak.", "I ate a sandwich. ___ sandwich was great.", "The", "Sudah disebut → the."),
]))
