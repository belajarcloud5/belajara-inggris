from qk import mk, mkf, mko
PHB = dict(practice=mk([
 ('Apa arti "write down"?', 'mencatat', 'menghapus', 'membaca', 'menggambar', 'Write down = mencatat.'),
 ('Apa arti "look up" (kata)?', 'mencari di kamus', 'melihat ke atas', 'menjawab', 'mengeja', 'Look up a word = mencari artinya.'),
 ('Apa arti "fill in"?', 'mengisi bagian kosong', 'menghapus', 'menyalin', 'menyobek', 'Fill in the blanks = isi titik-titik.'),
 ('Apa arti "hand in"?', 'mengumpulkan', 'membagikan', 'mengambil', 'menyimpan', 'Hand in = mengumpulkan kepada guru.'),
 ('Apa arti "hand out"?', 'membagikan', 'mengumpulkan', 'menghapus', 'membuang', 'Hand out = membagikan.'),
 ('Apa arti "pick up"?', 'mengambil', 'menjatuhkan', 'meletakkan', 'melempar', 'Pick up = mengambil/memungut.'),
 ('Apa arti "give back"?', 'mengembalikan', 'meminjam', 'membeli', 'mengambil', 'Give back = mengembalikan.'),
 ('Apa arti "come in"?', 'masuk', 'keluar', 'duduk', 'berdiri', 'Come in = masuk.'),
 ('Pilih yang tepat: "The teacher says, ___ your homework, please."', 'Hand in', 'Hand out', 'Look up', 'Come in', 'Mengumpulkan PR → hand in.'),
 ('Pilih yang tepat: "The teacher ___ the new books to all students."', 'hands out', 'hands in', 'looks up', 'writes down', 'Membagikan → hands out.'),
 ('Pilih yang tepat: "I do not know this word. I will ___ it in the dictionary."', 'look up', 'write down', 'hand in', 'give back', 'Mencari arti kata → look up.'),
 ('Pilih yang tepat: "___ the answer on your paper."', 'Write down', 'Look up', 'Come in', 'Stand up', 'Mencatat jawaban → write down.'),
 ('Pilih yang tepat: "___ the blanks with the correct words."', 'Fill in', 'Hand out', 'Give back', 'Pick up', 'Mengisi → fill in.'),
 ('Pilih yang tepat: "Your pencil is on the floor. ___ it."', 'Pick up', 'Hand in', 'Stand up', 'Look up', 'Pensil di lantai → ambil.'),
 ('Pilih yang tepat: "Thank you for the book. I will ___ it tomorrow."', 'give back', 'write down', 'fill in', 'hand out', 'Meminjam buku → mengembalikan.'),
 ('Pilih yang tepat: "Knock, knock. - ___, please."', 'Come in', 'Come out', 'Sit up', 'Hand in', 'Ada yang mengetuk pintu → masuk.'),
 ('Pilih kalimat yang benar:', 'Write it down.', 'Write down it.', 'Write down to it.', 'Write it of down.', 'Kata ganti di tengah.'),
 ('Pilih kalimat yang benar:', 'Hand them in.', 'Hand in them.', 'Hand them of in.', 'Hand in to them.', 'Kata ganti di tengah.'),
 ('Pilih kalimat yang SALAH:', 'Pick up it.', 'Pick it up.', 'Pick up the pen.', 'Pick the pen up.', 'Kata ganti harus di tengah.'),
 ('Pilih kalimat yang SALAH:', 'Look up it.', 'Look it up.', 'Look up the word.', 'Look the word up.', 'Kata ganti harus di tengah.'),
 ('Pilih pasangan yang sama artinya: "Write down the date" =', 'Write the date down.', 'Write the down date.', 'Down write the date.', 'Write date the down.', 'Kata benda boleh di tengah.'),
]), quiz=mk([
 ('Pilih yang tepat: "I ___ my homework to Mrs. Sari yesterday."', 'handed in', 'handed out', 'looked up', 'came in', 'Mengumpulkan (lampau) → handed in.'),
 ('Pilih yang tepat: "Please ___ the form and sign it."', 'fill in', 'give back', 'hand out', 'pick up', 'Mengisi formulir → fill in.'),
 ('Pilih yang tepat: "I don\'t understand \'brilliant\'. Let me ___ it."', 'look it up', 'look up it', 'hand it in', 'come it in', 'Kata ganti di tengah.'),
 ('Pilih yang tepat: "The teacher asked me to ___ the chairs."', 'pick up', 'hand in', 'fill in', 'write down', 'Mengambil/merapikan kursi.'),
 ('Pilih kalimat yang benar:', 'Please give my pen back.', 'Please give back my it pen.', 'Please back give my pen.', 'Please give my back pen it.', 'Kata benda boleh di tengah.'),
 ('Mana yang BUKAN phrasal verb?', 'study', 'write down', 'look up', 'hand in', 'Study satu kata saja.'),
]))
PHB["practice"] += mkf([
 ('Catat PR-nya.', 'Write ___ the homework.', 'down', 'Write down = mencatat.'),
 ('Isi titik-titiknya.', 'Fill ___ the blanks.', 'in', 'Fill in = mengisi.'),
 ('Kumpulkan PR kalian.', 'Hand ___ your homework.', 'in', 'Hand in = mengumpulkan.'),
 ('Silakan masuk.', 'Please come ___.', 'in', 'Come in = masuk.'),
 ('Cari kata itu di kamus.', 'Look ___ the word.', 'up', 'Look up = mencari di kamus.'),
 ('Ambil pensilmu.', 'Pick ___ your pencil.', 'up', 'Pick up = mengambil.'),
])
PHB["practice"] += mko([
 ('Kumpulkan PR kalian.', 'Hand in your homework.', 'out down', ''),
 ('Cari kata itu di kamus.', 'Look up the word in the dictionary.', 'down in', ''),
 ('Tolong kembalikan pulpenku.', 'Please give back my pen.', 'in up', 'Please give my pen back.'),
])
PHB["quiz"] += mkf([
 ('Bagikan buku-bukunya.', 'Hand ___ the books.', 'out', 'Hand out = membagikan.'),
 ('Tuliskan jawabannya.', 'Write ___ the answer.', 'down', 'Write down = mencatat.'),
])
