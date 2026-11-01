from qk import mk, mkf, mko
PHV = dict(practice=mk([
 ('Pilih phrasal verb yang tepat: "Experts ___ that exercise is important." (menunjukkan)', "point out", "point in", "point off", "point on", "point out = menunjukkan."),
 ('Pilih phrasal verb yang tepat: "Scientists ___ a study." (melaksanakan)', "carried out", "carried on", "carried off", "carried up", "carry out = melaksanakan."),
 ('Pilih phrasal verb yang tepat: "Technology has ___ big changes." (menyebabkan)', "brought about", "brought up", "brought out", "brought off", "bring about = menyebabkan."),
 ('Pilih phrasal verb yang tepat: "The plan ___ to be successful." (ternyata)', "turned out", "turned on", "turned off", "turned up", "turn out = ternyata."),
 ('Pilih phrasal verb yang tepat: "Schools must ___ this problem." (menangani)', "deal with", "deal in", "deal on", "deal off", "deal with = menangani."),
 ('Pilih phrasal verb yang tepat: "The government will ___ the matter." (menyelidiki)', "look into", "look on", "look off", "look at up", "look into = menyelidiki."),
 ('Pilih kalimat yang SALAH:', "They pointed it out me.", "They pointed it out.", "They pointed out the problem.", "They pointed the problem out.", "Struktur phrasal verb benar."),
 ('Pilih kalimat yang SALAH:', "We must deal the problem with.", "We must deal with the problem.", "We must deal with it.", "We must sort out the problem.", "deal with tidak dipisah."),
]) + mkf([
 ("Para ahli menunjukkan bahwa olahraga penting.", "Experts ___ out that exercise is important.", "point", "point out."),
 ("Ilmuwan melaksanakan penelitian.", "Scientists carried ___ a study.", "out", "carry out."),
 ("Rencana itu ternyata berhasil.", "The plan turned ___ to be successful.", "out", "turn out."),
 ("Sekolah harus menangani masalah ini.", "Schools must deal ___ this problem.", "with", "deal with."),
]), quiz=mk([
 ('Pilih phrasal verb yang tepat: "Technology has ___ many changes."', "brought about", "brought off", "brought in at", "brought on at", "bring about."),
 ('Pilih phrasal verb yang tepat: "The study ___ to be useful."', "turned out", "turned in", "turned off", "turned on", "turn out."),
 ('Pilih kalimat yang SALAH:', "The police looked the matter into.", "The police looked into the matter.", "The police looked into it.", "The police will look into it.", "look into tidak dipisah."),
]) + mkf([
 ("Pemerintah akan menyelidiki masalah itu.", "The government will look ___ the matter.", "into", "look into."),
]))
