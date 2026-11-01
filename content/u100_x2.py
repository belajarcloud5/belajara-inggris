from qk import mk, mkf
X2 = dict(practice=mk([
 ('Pilih yang benar: "The company changed ___ name last year."', 'its', "it's", 'it', 'their name is', 'Milik perusahaan → its.'),
 ('Pilih yang benar: "I think ___ going to rain today."', "it's", 'its', 'is', 'it', 'It is → it\'s.'),
 ('Pilih yang benar: "___ going to the market tomorrow."', "They're", 'Their', 'There', 'They', 'They are → They\'re.'),
 ('Pilih yang benar: "Is this ___ phone?"', 'your', "you're", 'you', 'yourself', 'Milikmu → your.'),
 ('Pilih yang benar: "I think ___ ready to start."', "you're", 'your', 'you', 'yours', 'You are → you\'re.'),
 ('Pilih yang benar: "Put your bags ___, next to the door."', 'there', 'their', "they're", 'then', 'Tempat → there.'),
 ('Pilih yang benar: "The students forgot ___ books."', 'their', 'there', "they're", 'them', 'Milik siswa → their.'),
 ('Pilih yang benar: "I would like some tea, and my brother wants some ___."', 'too', 'to', 'two', 'tho', 'Juga → too.'),
 ('Pilih yang benar: "We waited for ___ hours."', 'two', 'to', 'too', 'tow', 'Angka → two.'),
 ('Pilih yang benar: "She is going ___ the office by bus."', 'to', 'too', 'two', 'too to', 'Arah → to.'),
 ('Pilih yang benar: "My bag is heavier ___ yours."', 'than', 'then', 'that', 'thin', 'Perbandingan → than.'),
 ('Pilih yang benar: "First we eat, and ___ we go home."', 'then', 'than', 'there', 'them', 'Urutan → then.'),
 ('Pilih yang benar: "___ the owner of this car?"', "Who's", 'Whose', 'Whos', 'Who', 'Who is → Who\'s.'),
 ('Pilih yang benar: "___ idea was this?"', 'Whose', "Who's", 'Whos', 'Who', 'Milik siapa → Whose.'),
 ('Pilih yang benar: "The cat licked ___ paws, and ___ happy."', "its, it's", "it's, its", "its, its", "it's, it's", 'Milik kucing → its; it is → it\'s.'),
 ('Pilih yang benar: "___ over there, but ___ bags are here."', "They're, their", "Their, they're", "There, their", "They're, there", 'They are; milik mereka.'),
 ('Pilih kalimat yang benar:', "It's a pity that its price is so high.", "Its a pity that it's price is so high.", "It's a pity that it's price is so high.", "Its a pity that its price is so high.", 'It is; milik benda.'),
 ('Pilih kalimat yang benar:', "You're late, and your bag is open.", "Your late, and you're bag is open.", "You're late, and you're bag is open.", "Your late, and your bag is open.", 'You are; milikmu.'),
 ('Pilih kalimat yang SALAH:', "They're going to leave there bags here.", "They're going to leave their bags here.", "Their bags are there.", "There are two bags here.", 'Their bags.'),
 ('Pilih kalimat yang SALAH:', "She is taller then her sister.", "She is taller than her sister.", "First wash, then dry.", "He is faster than me.", 'Perbandingan → than.'),
 ('Pilih kalimat yang SALAH:', "Whose coming to the party?", "Who's coming to the party?", "Whose bag is this?", "Who's your teacher?", 'Who is coming → Who\'s.'),
 ('Pilih kalimat yang SALAH:', "Its time to go home.", "It's time to go home.", "The dog lost its toy.", "It's raining.", 'It is time → It\'s.'),
]))
X2["practice"] += mkf([
 ('Kucing itu menjilat cakarnya.', 'The cat licked ___ paw.', 'its', 'Milik kucing.'),
 ('Mereka akan datang.', "___ coming soon.", "They're/Theyre", 'They are.'),
 ('Tas itu ada di sana.', 'The bag is over ___.', 'there', 'Tempat.'),
 ('Ini milik siapa?', '___ is this?', 'Whose', 'Milik siapa.'),
])
X2["quiz"] = mk([
 ('Pilih yang benar: "I have ___ brothers."', 'two', 'to', 'too', 'tow', 'Angka.'),
 ('Pilih yang benar: "___ a nice day, isn\'t it?"', "It's", 'Its', 'Is', 'It', 'It is.'),
 ('Pilih yang benar: "That is ___ house over there."', 'their', 'there', "they're", 'they', 'Milik mereka.'),
 ('Pilih yang benar: "He is taller ___ his father."', 'than', 'then', 'that', 'thin', 'Perbandingan.'),
])
