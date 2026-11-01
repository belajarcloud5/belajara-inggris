from qk import mk, mkf, mko
CONJ = dict(practice=mk([
 ('Pilih kata hubung: "I like tea, ___ my sister likes coffee."', "but", "so", "or", "because", "Berlawanan → but."),
 ('Pilih kata hubung: "I am tired, ___ I go to bed early."', "so", "but", "or", "because", "Akibat → so."),
 ('Pilih kata hubung: "I go to bed early ___ I am tired."', "because", "so", "but", "or", "Alasan → because."),
 ('Pilih kata hubung: "Do you walk ___ take a bus?"', "or", "and", "but", "so", "Pilihan → or."),
 ('Pilih kata hubung: "I wake up ___ take a bath."', "and", "but", "or", "because", "Menambah kegiatan → and."),
 ('Pilih kata hubung: "She is hungry, ___ she eats a sandwich."', "so", "but", "or", "because", "Akibat → so."),
 ('Pilih kata hubung: "He is rich, ___ he is not happy."', "but", "so", "because", "and also", "Berlawanan → but."),
 ('Pilih kalimat yang benar:', "I am tired, so I sleep.", "Because I am tired, so I sleep.", "I am tired, because I sleep.", "I am tired so, I sleep.", "Pilih so atau because, jangan keduanya."),
 ('Pilih kalimat yang SALAH:', "Because it rains, so we stay home.", "It rains, so we stay home.", "We stay home because it rains.", "Because it rains, we stay home.", "Because dan so tidak dipakai bersamaan."),
 ('Pilih kalimat yang benar:', "I study English because it is fun.", "I study English so it is fun.", "I study English but it is fun.", "I study English or it is fun.", "Alasan → because."),
]) + mkf([
 ("Aku suka teh, tetapi adikku suka kopi.", "I like tea, ___ my brother likes coffee.", "but", "Berlawanan → but."),
 ("Aku mengantuk, jadi aku tidur.", "I am sleepy, ___ I go to bed.", "so", "Akibat → so."),
 ("Aku tidur karena aku mengantuk.", "I go to bed ___ I am sleepy.", "because", "Alasan → because."),
 ("Kamu mau teh atau kopi?", "Do you want tea ___ coffee?", "or", "Pilihan → or."),
 ("Aku makan nasi dan telur.", "I eat rice ___ eggs.", "and", "Menambah → and."),
]), quiz=mk([
 ('Pilih kata hubung: "It is cold, ___ I wear a jacket."', "so", "but", "or", "because", "Akibat → so."),
 ('Pilih kata hubung: "I wear a jacket ___ it is cold."', "because", "so", "but", "or", "Alasan → because."),
 ('Pilih kata hubung: "I want to go, ___ I have no time."', "but", "so", "and also", "because", "Berlawanan → but."),
]) + mkf([
 ("Dia lapar, jadi dia makan.", "He is hungry, ___ he eats.", "so", "Akibat → so."),
]))
