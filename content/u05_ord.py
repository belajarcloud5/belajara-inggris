from qk import mko
ORD = dict(practice=mko([('Ini kelasku.', 'This is my classroom.', 'These', ''),
 ('Ada tiga puluh meja di ruangan itu.', 'There are thirty desks in the room.', 'is', ''),
 ('Jam ada di dinding.', 'The clock is on the wall.', 'are', ''),
 ('Tasku ada di bawah meja.', 'My bag is under the desk.', 'over', ''),
 ('Apakah ada perpustakaan di sekolahmu?', 'Is there a library in your school?', 'Are', ''),
 ('Kantin ada di sebelah lapangan.', 'The canteen is next to the field.', '', ''),
 ('Itu buku-bukuku.', 'Those are my books.', 'That', '')]), quiz=mko([('Tidak ada komputer di sini.', "There isn't a computer here.", "aren't", ''),
 ('Guru ada di depan kelas.', 'The teacher is in front of the class.', '', ''),
 ('Pensil-pensil ini baru.', 'These pencils are new.', 'is', '')]))
