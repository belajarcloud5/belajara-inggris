from qk import mk, mkf, mko
MODAL = dict(practice=mk([
 ('Pilih jawaban yang benar: "When I was six, I ___ swim." (tidak bisa)', "couldn't", "can't", "don't can", "won't", "Masa lampau umum → couldn't."),
 ('Pilih jawaban yang benar: "She ___ win the race yesterday." (berhasil)', "was able to", "can", "is able to", "could to", "Satu kejadian lampau → was able to."),
 ('Pilih jawaban yang benar: "I ___ speak English next year." (akan bisa)', "will be able to", "can will", "will can", "am can", "Masa depan → will be able to."),
 ('Pilih jawaban yang benar: "___ you ride a bike at five?"', "Could", "Do", "Did can", "Were can", "Pertanyaan lampau → Could."),
 ('Pilih kalimat yang benar:', "She can sing well.", "She can sings well.", "She can to sing well.", "She cans sing well.", "Setelah can, V1 tanpa -s dan tanpa to."),
 ('Pilih kalimat yang SALAH:', "Do you can swim?", "Can you swim?", "Could you swim as a child?", "She can't dance.", "Pertanyaan dengan can tidak memakai do."),
 ('Pilih kalimat yang benar:', "He couldn't read when he was four.", "He can't read when he was four.", "He couldn't to read when he was four.", "He doesn't could read when he was four.", "Lampau → couldn't + V1."),
]) + mkf([
 ("Waktu kecil, aku tidak bisa berenang.", "When I was young, I ___ swim.", "couldn't", "Lampau → couldn't."),
 ("Dia berhasil menyelesaikan lomba kemarin.", "She ___ able to finish the race yesterday.", "was", "was able to."),
 ("Tahun depan, aku akan bisa berenang.", "I will be ___ to swim next year.", "able", "will be able to."),
 ("Bisakah kamu berenang?", "___ you swim?", "Can/Could", "Can atau Could."),
]), quiz=mk([
 ('Pilih jawaban yang benar: "I ___ run fast when I was ten." (bisa)', "could", "can", "am able", "will", "Lampau → could."),
 ('Pilih jawaban yang benar: "He ___ pass the exam last week." (berhasil)', "was able to", "can", "is able to", "will can", "Satu kejadian lampau → was able to."),
 ('Pilih kalimat yang SALAH:', "She cans swim.", "She can swim.", "She can't swim.", "Can she swim?", "Can tanpa -s."),
]) + mkf([
 ("Dia bisa menari.", "She ___ dance.", "can", "can + V1."),
]))
