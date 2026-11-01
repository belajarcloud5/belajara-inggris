from qk import mk, mkf, mko
PASS = dict(practice=mk([
 ('Pilih jawaban yang benar: "This animal ___ a koala."', "is called", "calls", "is calling", "are called", "Dinamai → is called."),
 ('Pilih jawaban yang benar: "Tigers ___ in Asia."', "are found", "is found", "find", "are finding", "Jamak → are found."),
 ('Pilih jawaban yang benar: "Bamboo ___ to build houses."', "is used", "uses", "are used", "is using", "Tak terhitung → is used."),
 ('Pilih jawaban yang benar: "The elephant ___ as the largest land animal."', "is known", "knows", "are known", "is knowing", "is known as."),
 ('Pilih kalimat yang SALAH:', "Komodo dragons are find in Indonesia.", "Komodo dragons are found in Indonesia.", "Komodo dragons live in Indonesia.", "Komodo dragons are protected.", "V3 dari find adalah found."),
 ('Pilih kalimat yang SALAH:', "Rice is grow in Java.", "Rice is grown in Java.", "Rice grows in Java.", "Rice is eaten in Java.", "V3 dari grow adalah grown."),
 ('Pilih kalimat yang benar:', "These birds are protected by law.", "These birds protected by law.", "These birds are protect by law.", "These birds is protected by law.", "are + V3."),
]) + mkf([
 ("Hewan ini disebut koala.", "This animal is ___ a koala.", "called", "is called."),
 ("Harimau ditemukan di Asia.", "Tigers are ___ in Asia.", "found", "are found."),
 ("Bambu dipakai untuk membangun rumah.", "Bamboo is ___ to build houses.", "used", "is used."),
 ("Burung-burung ini dilindungi.", "These birds are ___.", "protected", "are protected."),
]), quiz=mk([
 ('Pilih jawaban yang benar: "Coffee ___ in Sumatra."', "is grown", "grows", "are grown", "is growing", "Tunggal → is grown."),
 ('Pilih jawaban yang benar: "Whales ___ by law."', "are protected", "protect", "is protected", "are protecting", "Jamak → are protected."),
 ('Pilih kalimat yang SALAH:', "This bird is call a hornbill.", "This bird is called a hornbill.", "This bird lives in forests.", "Hornbills are found in Asia.", "is called."),
]) + mkf([
 ("Gajah dikenal sebagai hewan darat terbesar.", "Elephants are ___ as the largest land animals.", "known", "are known as."),
]))
