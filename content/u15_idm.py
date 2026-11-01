from qk import mk, mkf, mko
IDM = dict(practice=mk([
 ('Apa arti "It\'s raining cats and dogs"?', 'hujan sangat deras', 'ada hewan jatuh dari langit', 'hujan sudah berhenti', 'cuaca sangat panas', 'Idiom: hujan deras.'),
 ('Apa arti "busy as a bee"?', 'sangat sibuk', 'sangat takut', 'sangat lapar', 'sangat lelah', 'Lebah selalu bekerja.'),
 ('Apa arti "as quiet as a mouse"?', 'sangat pendiam', 'sangat lincah dan aktif', 'sangat marah sekali', 'sangat kuat dan besar', 'Tikus tanpa suara.'),
 ('Apa arti "let the cat out of the bag"?', 'membocorkan rahasia', 'melepas kucing dari tas', 'membeli hewan baru', 'membersihkan tas', 'Rahasia terbongkar.'),
 ('Apa arti "once in a blue moon"?', 'sangat jarang', 'setiap malam hari', 'setiap bulan sekali', 'tiap hari tanpa henti', 'Hampir tidak pernah.'),
 ('Apa arti "a piece of cake"?', 'sangat mudah', 'sangat enak', 'sangat mahal', 'sangat sulit', 'Semudah makan kue.'),
 ('Apa arti "break a leg"?', 'semoga sukses', 'hati-hati di jalan', 'jangan datang', 'selamat tidur', 'Ucapan sebelum tampil.'),
 ('Apa arti "hit the books"?', 'belajar giat', 'memukul buku', 'menjual buku', 'membuang buku', 'Idiom: belajar serius.'),
 ('Pilih yang tepat: "The test was a ___. I finished it in ten minutes."', 'piece of cake', 'blue moon every night', 'busy bee in the garden', 'broken leg at school', 'Cepat selesai → sangat mudah.'),
 ('Pilih yang tepat: "Take an umbrella! It\'s ___."', 'raining cats and dogs', 'busy as a bee today', 'a piece of cake for me', 'quiet as a mouse here', 'Payung → hujan deras.'),
 ('Pilih yang tepat: "It\'s a secret. Don\'t ___."', 'let the cat out of the bag', 'hit the books tonight', 'break a leg at school', 'rain cats and dogs now', 'Rahasia → jangan dibocorkan.'),
 ('Pilih yang tepat: "I see my cousins ___. They live far away."', 'once in a blue moon', 'every day after school', 'all the time at home', 'at lunch with friends', 'Tinggal jauh → jarang.'),
 ('Pilih yang tepat: "I have an exam tomorrow, so I must ___ tonight."', 'hit the books', 'break a leg', 'let the cat out', 'rain cats and dogs', 'Ujian → belajar giat.'),
 ('Pilih yang tepat: "Before the dance show, her friend said, \'___!\'"', 'Break a leg', 'Hit the books', 'Piece of cake', 'Busy as a bee', 'Sebelum tampil → doa sukses.'),
 ('Pilih yang tepat: "Mum is cooking, cleaning, and washing. She is ___."', 'busy as a bee', 'quiet as a mouse', 'a piece of cake', 'once in a blue moon', 'Banyak kerja → sangat sibuk.'),
 ('Pilih yang tepat: "The kitten slept all day and was ___."', 'as quiet as a mouse', 'busy as a bee', 'raining cats and dogs', 'a piece of cake', 'Tidur → tanpa suara.'),
 ('Mana arti yang BENAR untuk "It\'s raining cats and dogs"?', 'It is raining very hard.', 'Animals are falling from the sky.', 'It is a nice sunny day.', 'It is very quiet outside.', 'Idiom tidak diterjemahkan harfiah.'),
 ('Mana yang BUKAN idiom?', 'I like cats and dogs.', 'Break a leg!', 'A piece of cake.', 'Busy as a bee.', 'Kalimat pertama berarti harfiah.'),
 ('Mana pasangan idiom dan arti yang benar?', 'a piece of cake = very easy', 'a piece of cake = very expensive', 'a piece of cake = very hungry', 'a piece of cake = very far', 'Mudah.'),
 ('Mana pasangan idiom dan arti yang benar?', 'once in a blue moon = very rarely', 'once in a blue moon = every month', 'once in a blue moon = at night', 'once in a blue moon = very often', 'Jarang.'),
]), quiz=mk([
 ('Apa arti "hit the books"?', 'belajar giat', 'bermain di perpustakaan', 'menulis buku', 'menyobek buku', 'Belajar serius.'),
 ('Pilih yang tepat: "The puzzle was ___. Even my little brother solved it."', 'a piece of cake', 'once in a blue moon', 'raining cats and dogs', 'busy as a bee', 'Adik bisa → mudah.'),
 ('Pilih yang tepat: "Ssst! Don\'t ___ about the surprise."', 'let the cat out of the bag', 'break a leg', 'hit the books', 'be busy as a bee', 'Rahasia kejutan.'),
 ('Pilih yang tepat: "Good luck at the match! ___!"', 'Break a leg', 'Piece of cake', 'Raining cats and dogs', 'Hit the books', 'Doa sukses.'),
 ('Pilih yang tepat: "Dina is shy. She is as ___ as a mouse."', 'quiet', 'loud', 'busy', 'tall', 'Idiom: as quiet as a mouse.'),
 ('Pilih yang tepat: "I\'m ___ today. I have ten meetings."', 'busy as a bee', 'quiet as a mouse', 'a piece of cake', 'a blue moon', 'Banyak rapat → sibuk.'),
]))
IDM["practice"] += mkf([
 ('Hujan sangat deras.', "It's raining ___ and dogs.", 'cats', 'It is raining cats and dogs.'),
 ('Ujian itu sangat mudah.', 'The test was a piece of ___.', 'cake', 'A piece of cake = sangat mudah.'),
 ('Dia sangat sibuk.', 'She is busy as a ___.', 'bee', 'Busy as a bee.'),
 ('Semoga sukses!', 'Break a ___!', 'leg', 'Break a leg!'),
 ('Jangan bocorkan rahasia itu.', "Don't let the ___ out of the bag.", 'cat', 'Let the cat out of the bag.'),
 ('Aku harus belajar giat.', 'I must hit the ___.', 'books', 'Hit the books.'),
 ('Kami jarang makan di luar.', 'We eat out once in a blue ___.', 'moon', 'Once in a blue moon.'),
])
IDM["quiz"] += mkf([
 ('Dia sangat pendiam.', 'She is as quiet as a ___.', 'mouse', 'As quiet as a mouse.'),
 ('Itu sangat mudah.', "It's a piece of ___.", 'cake', 'A piece of cake.'),
])
