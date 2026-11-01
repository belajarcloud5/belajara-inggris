from qk import mk, mkf, mko
MODAL = dict(practice=mk([
 ('Pilih jawaban yang benar: "It\'s hot. I ___ open the window." (keputusan saat bicara)', "will", "must to", "would", "have to", "Keputusan saat itu → will ('ll)."),
 ('Pilih jawaban yang benar: "___ I carry your bag?" (menawarkan)', "Shall", "Will", "Do", "Am", "Tawaran dengan I → Shall I."),
 ('Pilih jawaban yang benar: "___ we go to the park?" (ajakan)', "Shall", "Does", "Will to", "Are", "Ajakan → Shall we."),
 ('Pilih jawaban yang benar: "I promise I ___ be late." (janji)', "won't", "don't", "can't to", "doesn't", "Janji tidak akan → won't."),
 ('Pilih kalimat yang benar:', "Shall we start now?", "Shall we starting now?", "Shall we to start now?", "Shall start we now?", "Shall we + V1."),
 ('Pilih kalimat yang SALAH:', "Shall he help you?", "Shall I help you?", "Shall we go?", "Will he help you?", "Shall dipakai dengan I atau we."),
 ('Pilih kalimat yang benar:', "I think it will rain tomorrow.", "I think it will to rain tomorrow.", "I think it wills rain tomorrow.", "I think it will raining tomorrow.", "will + V1."),
]) + mkf([
 ("Aku berjanji tidak akan lupa.", "I promise I ___ forget.", "won't", "Janji → won't."),
 ("Bolehkah aku membawakan tasmu?", "___ I carry your bag?", "Shall", "Shall I = tawaran."),
 ("Mari kita mulai sekarang?", "___ we start now?", "Shall", "Shall we = ajakan."),
 ("Besok akan hujan.", "It ___ rain tomorrow.", "will", "will = prediksi."),
]), quiz=mk([
 ('Pilih jawaban yang benar: "It\'s cold. I ___ close the door."', "will", "must to", "would", "must", "Keputusan saat itu → will."),
 ('Pilih jawaban yang benar: "___ I open the window?" (menawarkan)', "Shall", "Will", "Do", "Am", "Shall I."),
 ('Pilih kalimat yang SALAH:', "Shall they help you?", "Shall we help you?", "Shall I help you?", "Will they help you?", "Shall hanya dengan I atau we."),
]) + mkf([
 ("Aku akan membawa peta.", "I ___ bring the map.", "will/'ll", "I'll bring."),
]))
