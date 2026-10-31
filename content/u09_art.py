from qk import mk, mkf, mko
ART = dict(practice=mk([
 ('Pilih article yang tepat: "Dina goes to ___ school every day."', "no article", "the", "a", "an", "Pergi bersekolah (kegiatan) → tanpa the."),
 ('Pilih article yang tepat: "Excuse me, where is ___ station?"', "the", "a", "an", "no article", "Stasiun tertentu yang dicari → the."),
 ('Pilih article yang tepat: "It\'s late. Let\'s go to ___ bed."', "no article", "the", "a", "an", "go to bed (tidur) → tanpa article."),
 ('Pilih article yang tepat: "Turn left at ___ corner."', "the", "a", "an", "no article", "Tikungan yang tertentu → the."),
 ('Pilih article yang tepat: "I went to ___ school to meet the principal."', "the", "a", "no article", "an", "Pergi ke gedungnya untuk bertemu → the."),
]) + mkf([
 ("Di mana kantor posnya?", "Where is ___ post office?", "the", "Kantor pos tertentu → the."),
 ("Belok kanan di tikungan.", "Turn right at ___ corner.", "the", "Tikungan tertentu → the."),
]) + mko([
 ("Bank ada di sebelah kantor pos.", "The bank is next to the post office.", "a", ""),
]), quiz=mk([
 ('Pilih article yang tepat: "My mother is at ___ home."', "no article", "the", "a", "an", "at home → tanpa article."),
 ('Pilih article yang tepat: "The bus stop is near ___ market."', "the", "a", "an", "no article", "Pasar tertentu yang dikenal → the."),
]))
