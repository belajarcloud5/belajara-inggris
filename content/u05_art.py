from qk import mk, mkf, mko
ART = dict(practice=mk([
 ('Pilih article yang tepat: "I have ___ eraser in my bag."', "an", "a", "the", "no article", "eraser dimulai bunyi vokal → an."),
 ('Pilih article yang tepat: "She is ___ new student."', "a", "an", "the", "no article", "new dibaca \"nyu\" (konsonan) → a."),
 ('Pilih article yang tepat: "I waited for ___ hour."', "an", "a", "the", "no article", "h pada hour tidak dibunyikan → an."),
 ('Pilih article yang tepat: "He studies at ___ university in Bandung."', "a", "an", "the", "no article", "university dibaca \"yu\" (konsonan) → a."),
 ('Pilih article yang tepat: "I like ___ books."', "no article", "a", "an", "the", "books jamak dan umum → tanpa article."),
 ('Pilih article yang tepat: "There is a cat on the sofa. ___ cat is white."', "The", "A", "An", "No article", "Kucing yang sudah disebut → the."),
]) + mkf([
 ("Aku punya sebuah jeruk.", "I have ___ orange.", "an", "orange diawali vokal → an."),
 ("Matahari itu panas.", "___ sun is hot.", "The", "Hanya ada satu matahari → the."),
 ("Dia seorang guru.", "She is ___ teacher.", "a", "Profesi tunggal → a."),
 ("Tolong tutup pintunya. (pintu di kelas itu)", "Please close ___ door.", "the", "Pintu yang jelas bagi pembicara dan pendengar → the."),
]) + mko([
 ("Aku punya sebuah pulpen dan sebuah penghapus.", "I have a pen and an eraser.", "the", ""),
]), quiz=mk([
 ('Pilih article yang tepat: "This is ___ ugly picture."', "an", "a", "the", "no article", "ugly diawali bunyi vokal → an."),
 ('Pilih article yang tepat: "Look at ___ moon!"', "the", "a", "an", "no article", "Hanya ada satu bulan → the."),
 ('Pilih article yang tepat: "My father is ___ honest man."', "an", "a", "the", "no article", "h pada honest tidak dibunyikan → an."),
]) + mkf([
 ("Dia membeli sebuah payung.", "She bought ___ umbrella.", "an", "umbrella diawali vokal → an."),
]))
