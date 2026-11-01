from qk import mk, mkf, mko
MIX = dict(practice=mk([
 ('Pilih jawaban yang benar (fakta umum): "If you heat ice, it ___."', "melts", "will melted", "would melt", "melting", "Zero conditional: present, present."),
 ('Pilih jawaban yang benar: "If I am tired, I ___ to bed early."', "go", "will went", "would go", "going", "Kebiasaan: present, present."),
 ('Pilih jawaban yang benar: "If you mix red and blue, you ___ purple."', "get", "would got", "will getting", "got", "Fakta: present, present."),
 ('Pilih jawaban yang benar: "If you see Rani, ___ her to call me." (perintah)', "tell", "told", "telling", "will tell to", "if + present, imperative."),
 ('Pilih jawaban yang benar: "If it rains tomorrow, I ___ stay home." (kemungkinan masa depan)', "will", "would have", "am", "did", "Type 1: will + V1."),
 ('Pilih kalimat yang benar:', "If water boils, it turns into steam.", "If water will boil, it turns into steam.", "If water boiled, it would turn into steam now.", "If water boiling, it turns into steam.", "Zero: present, present."),
 ('Pilih kalimat yang SALAH:', "If you heat ice, it will melted.", "If you heat ice, it melts.", "If you heat ice, it will melt.", "When you heat ice, it melts.", "will + V1, bukan will melted."),
 ('Pilih kalimat yang SALAH:', "If it will rain, I stay home.", "If it rains, I will stay home.", "If it rains, I stay home.", "When it rains, I stay home.", "Jangan will di klausa if."),
]) + mkf([
 ("Kalau kamu memanaskan es, es itu mencair.", "If you heat ice, it ___.", "melts", "Zero: present, present."),
 ("Kalau aku capek, aku tidur lebih awal.", "If I am tired, I ___ to bed early.", "go", "Zero: present, present."),
 ("Kalau kamu mencampur merah dan biru, kamu mendapat ungu.", "If you mix red and blue, you ___ purple.", "get", "Zero: present, present."),
 ("Kalau besok hujan, aku akan tinggal di rumah.", "If it rains tomorrow, I ___ stay home.", "will/'ll", "Type 1: will + V1."),
]), quiz=mk([
 ('Pilih jawaban yang benar: "If you freeze water, it ___ ice."', "becomes", "would become", "will became", "became", "Zero: present, present."),
 ('Pilih jawaban yang benar: "If you press this button, the light ___ on."', "comes", "would come", "will came", "came", "Zero: present, present."),
 ('Pilih kalimat yang SALAH:', "If plants get no water, they will died.", "If plants get no water, they die.", "If plants get no water, they will die.", "If plants get no water, they would die.", "will + V1."),
]) + mkf([
 ("Kalau air mendidih, ia berubah menjadi uap.", "If water boils, it ___ into steam.", "turns", "Zero: present, present."),
]))
