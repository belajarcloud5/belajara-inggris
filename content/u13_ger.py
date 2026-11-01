from qk import mk, mkf, mko
GER = dict(practice=mk([
 ('Pilih jawaban yang benar: "I want ___ Bali."', "to visit", "visiting", "visit", "visited", "want + to V1."),
 ('Pilih jawaban yang benar: "She hopes ___."', "to win", "winning", "win", "won", "hope + to V1."),
 ('Pilih jawaban yang benar: "We plan ___ early."', "to leave", "leaving", "leave", "left", "plan + to V1."),
 ('Pilih jawaban yang benar: "He decided ___."', "to stay", "staying", "stay", "stayed", "decide + to V1."),
 ('Pilih jawaban yang benar: "I promise ___ you."', "to call", "calling", "call", "called", "promise + to V1."),
 ('Pilih jawaban yang benar: "I decided ___ go."', "not to", "to not", "no to", "don\'t to", "decide + not to V1."),
 ('Pilih kalimat yang benar:', "I want to go home.", "I want going home.", "I want go home.", "I want to going home.", "want + to V1."),
 ('Pilih kalimat yang SALAH:', "She plans buying a car.", "She plans to buy a car.", "She hopes to buy a car.", "She decided to buy a car.", "plan + to V1."),
]) + mkf([
 ("Aku ingin mengunjungi Bali.", "I want ___ visit Bali.", "to", "want + to V1."),
 ("Dia berharap menang.", "She hopes ___ win.", "to", "hope + to V1."),
 ("Kami berencana berangkat awal.", "We plan ___ leave early.", "to", "plan + to V1."),
 ("Aku memutuskan untuk tidak pergi.", "I decided ___ to go.", "not", "decide + not to V1."),
]), quiz=mk([
 ('Pilih jawaban yang benar: "They agreed ___ the project."', "to start", "starting", "start", "started", "agree + to V1."),
 ('Pilih jawaban yang benar: "I would like ___ a coffee."', "to have", "having", "have", "had", "would like + to V1."),
 ('Pilih kalimat yang SALAH:', "He decided going home.", "He decided to go home.", "He wanted to go home.", "He planned to go home.", "decide + to V1."),
]) + mkf([
 ("Aku berjanji untuk menelepon.", "I promise ___ call you.", "to", "promise + to V1."),
]))
