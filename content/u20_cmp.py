from qk import mk, mkf, mko
CMP = dict(practice=mk([
 ('Pilih jawaban yang benar: "The blue whale is the ___ animal on Earth."', "largest", "larger", "most large", "large", "the + superlatif."),
 ('Pilih jawaban yang benar: "A cheetah is ___ a lion."', "faster than", "fastest than", "more fast than", "as fast than", "-er + than."),
 ('Pilih jawaban yang benar: "Dolphins are as intelligent ___ monkeys."', "as", "than", "like", "from", "as ... as."),
 ('Pilih jawaban yang benar: "The eagle is one of the ___ birds."', "strongest", "stronger", "most strong", "strong", "one of the + superlatif."),
 ('Pilih jawaban yang benar: "Elephants are ___ horses."', "larger than", "largest than", "more large than", "as large than", "-er + than."),
 ('Pilih kalimat yang SALAH:', "Elephants are more larger than horses.", "Elephants are larger than horses.", "Elephants are the largest land animals.", "Horses are smaller than elephants.", "Jangan dobel more dan -er."),
 ('Pilih kalimat yang SALAH:', "A cheetah is faster then a lion.", "A cheetah is faster than a lion.", "A cheetah is the fastest land animal.", "A lion is slower than a cheetah.", "than, bukan then."),
]) + mkf([
 ("Paus biru adalah hewan terbesar di Bumi.", "The blue whale is the ___ animal on Earth.", "largest", "the + superlatif."),
 ("Cheetah lebih cepat daripada singa.", "A cheetah is ___ than a lion.", "faster", "-er + than."),
 ("Lumba-lumba secerdas monyet.", "Dolphins are as intelligent ___ monkeys.", "as", "as ... as."),
 ("Gajah lebih besar daripada kuda.", "Elephants are ___ than horses.", "larger", "-er + than."),
]), quiz=mk([
 ('Pilih jawaban yang benar: "The ostrich is the ___ bird."', "biggest", "bigger", "most big", "big", "the + superlatif."),
 ('Pilih jawaban yang benar: "A rabbit is ___ a turtle."', "faster than", "fastest than", "more fast than", "as fast than", "-er + than."),
 ('Pilih kalimat yang SALAH:', "The cheetah is the most fastest animal.", "The cheetah is the fastest animal.", "The cheetah is faster than a horse.", "The cheetah is one of the fastest.", "Jangan dobel."),
]) + mkf([
 ("Elang adalah salah satu burung terkuat.", "The eagle is one of the ___ birds.", "strongest", "one of the + superlatif."),
]))
