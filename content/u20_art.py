from qk import mk, mkf, mko
ART = dict(practice=mk([
 ("Mana kalimat generik yang SALAH?", "A lions eat meat.", "A lion eats meat.", "Lions eat meat.", "The lion eats meat.", "a harus dengan tunggal; jamak tanpa article."),
 ("Mana kalimat yang benar untuk membicarakan paus secara umum?", "Whales are mammals.", "A whales are mammals.", "The whale are mammals.", "Whale is mammals.", "Jamak umum tanpa article, kata kerja are."),
 ("Mana kalimat yang SALAH?", "An tiger is a protected animal.", "A tiger is a protected animal.", "Tigers are protected animals.", "The tiger is a protected animal.", "tiger diawali konsonan → a, bukan an."),
 ('Kita bilang "The sun is hot" karena...', "hanya ada satu matahari", "semua kata benda memakai the", "sun diawali konsonan", "sun adalah kata jamak", "Benda unik memakai the."),
 ('Pilih article yang tepat: "A Komodo dragon is ___ largest lizard in the world."', "the", "a", "an", "no article", "Superlatif → the."),
]) + mkf([
 ("Paus adalah mamalia.", "A whale is ___ mammal.", "a", "mammal diawali konsonan → a."),
 ("Elang adalah burung.", "An eagle is ___ bird.", "a", "bird diawali konsonan → a."),
]) + mko([
 ("Paus adalah mamalia.", "Whales are mammals.", "a", ""),
]), quiz=mk([
 ("Mana kalimat generik yang SALAH?", "Elephant is big.", "An elephant is big.", "Elephants are big.", "The elephant is big.", "Tunggal harus punya article; jamak tanpa article."),
]) + mkf([
 ("Singa adalah karnivora.", "A lion is ___ carnivore.", "a", "carnivore diawali konsonan → a."),
]))
