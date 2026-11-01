from qk import mk, mkf, mko
CONJ = dict(practice=mk([
 ('Pilih kata hubung: "I ate breakfast ___ I left home." (sebelum)', "before", "after", "because", "but", "Sebelum → before."),
 ('Pilih kata hubung: "___ we ate, we washed the plates." (setelah)', "After", "Before", "Because", "But", "Setelah → after."),
 ('Pilih kata hubung: "I stayed home ___ it rained."', "because", "so", "but", "after that", "Alasan → because."),
 ('Pilih kata hubung: "It rained, ___ I stayed home."', "so", "because", "before", "or", "Akibat → so."),
 ('Pilih kata hubung: "___ I arrived, the class started."', "When", "Because", "But", "So", "Ketika → when."),
 ('Pilih kata hubung: "I opened the door, ___ I went in."', "and then", "because", "before", "or", "Urutan → and then."),
 ('Pilih kalimat yang benar:', "After we ate, we left.", "After we eat, we left.", "After we ate we, left.", "After we ate, we leave.", "Dua bagian memakai kala lampau."),
 ('Pilih kalimat yang SALAH:', "When I arrive home, I took a bath yesterday.", "When I arrived home, I took a bath.", "I took a bath when I arrived home.", "After I came home, I took a bath.", "Kejadian lampau → arrived."),
 ('Pilih kalimat yang benar:', "I finished my homework before I watched TV.", "I finished my homework before I watch TV.", "I finish my homework before I watched TV.", "I finished my homework before I will watch TV.", "Kedua klausa lampau."),
 ('Pilih kalimat yang benar:', "She was tired, so she went to bed.", "She was tired, because she went to bed.", "She was tired so, she went to bed.", "She was tired but so she went to bed.", "Akibat → so."),
]) + mkf([
 ("Aku makan sebelum aku berangkat.", "I ate ___ I left.", "before", "Sebelum → before."),
 ("Setelah hujan berhenti, kami bermain.", "___ the rain stopped, we played.", "After", "Setelah → after."),
 ("Aku tinggal di rumah karena hujan.", "I stayed home ___ it rained.", "because", "Alasan → because."),
 ("Hujan turun, jadi kami pulang.", "It rained, ___ we went home.", "so", "Akibat → so."),
]), quiz=mk([
 ('Pilih kata hubung: "I was late ___ the bus broke down."', "because", "so", "before", "but", "Alasan → because."),
 ('Pilih kata hubung: "The bus broke down, ___ I was late."', "so", "because", "before", "when", "Akibat → so."),
 ('Pilih kata hubung: "___ she called, I was cooking."', "When", "So", "Or", "But", "Ketika → when."),
]) + mkf([
 ("Setelah makan, kami mencuci piring.", "___ we ate, we washed the plates.", "After", "Setelah → after."),
]))
