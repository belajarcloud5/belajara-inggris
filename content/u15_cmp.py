from qk import mk, mkf, mko
CMP = dict(practice=mk([
 ('Pilih jawaban yang benar: "The elephant is one of the ___ animals."', "biggest", "bigger", "most big", "big", "one of the + superlatif."),
 ('Pilih jawaban yang benar: "Komodo is one of the most ___ lizards."', "dangerous", "more dangerous", "dangerouser", "danger", "one of the most + adj."),
 ('Pilih jawaban yang benar: "The cheetah is the ___ animal in the world."', "fastest", "faster", "most fast", "fast", "the + superlatif."),
 ('Pilih jawaban yang benar: "Bali is one of the most popular ___ in Indonesia."', "islands", "island", "the islands", "an island", "one of the + jamak."),
 ('Pilih kalimat yang benar:', "One of the biggest animals is the elephant.", "One of the biggest animal is the elephant.", "One of the bigger animals is the elephant.", "One of biggest animals is the elephant.", "one of the + superlatif + jamak."),
 ('Pilih kalimat yang SALAH:', "The elephant is one of the biggest animal.", "The elephant is one of the biggest animals.", "The elephant is the biggest animal.", "The elephant is bigger than a horse.", "Setelah one of the, jamak."),
 ('Pilih kalimat yang SALAH:', "The cheetah is fastest animal in the world.", "The cheetah is the fastest animal in the world.", "The cheetah is faster than a lion.", "The cheetah is one of the fastest animals.", "the + superlatif."),
]) + mkf([
 ("Gajah adalah salah satu hewan terbesar.", "The elephant is one of the ___ animals.", "biggest", "one of the + superlatif."),
 ("Cheetah adalah hewan tercepat di dunia.", "The cheetah is the ___ animal in the world.", "fastest", "the + superlatif."),
 ("Komodo adalah salah satu kadal paling berbahaya.", "Komodo is one of the ___ dangerous lizards.", "most", "one of the most + adj."),
 ("Bali adalah salah satu pulau paling populer.", "Bali is one of the most popular ___.", "islands", "jamak."),
]), quiz=mk([
 ('Pilih jawaban yang benar: "The giraffe is the ___ animal."', "tallest", "taller", "most tall", "tall", "the + superlatif."),
 ('Pilih jawaban yang benar: "The lion is one of the most ___ cats."', "powerful", "more powerful", "powerfulest", "power", "one of the most + adj."),
 ('Pilih kalimat yang SALAH:', "She is one of the best student.", "She is one of the best students.", "She is the best student.", "She is better than me.", "Setelah one of the, jamak."),
]) + mkf([
 ("Singa adalah salah satu hewan terkuat.", "The lion is one of the ___ animals.", "strongest", "one of the + superlatif."),
]))
