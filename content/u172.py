from ub import *
UNIT = mkunit("u172",
 ["membedakan **meringkas (summarise)** dan **memparafrase (paraphrase)**",
  "menulis ulang kalimat dengan **kata dan struktur berbeda** tanpa mengubah makna",
  "memilih **ringkasan yang tepat** untuk sebuah teks",
  "menghindari **menyalin** langsung dari teks"],
 [intro("**Paraphrase** berarti mengubah kalimat dengan kata sendiri tanpa mengubah makna. **Summary** berarti mengambil gagasan utama saja dalam bentuk singkat. Keduanya penting dalam ujian dan tulisan akademik. Jangan menyalin kalimat apa adanya."),
  gram("1. Cara memparafrase",
   table=[["Teknik", "Contoh"],
          ["Ganti kata dengan sinonim", "[[big → large]], [[buy → purchase]]"],
          ["Ubah kelas kata", "[[decide → make a decision]]"],
          ["Ubah struktur", "[[Active → passive]]"],
          ["Ubah urutan klausa", "[[Although it rained, we went. → We went although it rained.]]"],
          ["Jaga makna", "angka, nama, dan fakta tidak boleh berubah"]],
   examples=[("[[The city has a large population. → Many people live in the city.]]", "Kota itu berpenduduk banyak. → Banyak orang tinggal di kota itu.")]),
  gram("2. Cara meringkas",
   table=[["Langkah", "Isi"],
          ["1", "Temukan gagasan utama tiap paragraf"],
          ["2", "Buang contoh dan detail kecil"],
          ["3", "Tulis ulang dengan kata sendiri"],
          ["4", "Periksa: lebih pendek, makna utama sama"]]),
  warn("Paraphrase bukan sekadar mengganti satu kata", text="Mengganti satu kata saja masih dianggap menyalin. Ubah juga struktur kalimatnya."),
  summary(["Paraphrase: ganti kata dan struktur, makna sama.", "Summary: gagasan utama, lebih pendek.", "Jaga fakta dan angka.", "Jangan menyalin."])],
 [], [])
P = mk([
 ('Pilih parafrase terbaik: "The city has a large population."', 'Many people live in the city.', 'The city has a large population.', 'The city has few people.', 'Large is the population city.', 'Makna sama, kata berbeda.'),
 ('Pilih parafrase terbaik: "She bought a new phone."', 'She purchased a new phone.', 'She sold a new phone.', 'She bought a new phone.', 'She lost her new phone.', 'Buy = purchase.'),
 ('Pilih parafrase terbaik: "The teacher explained the lesson."', 'The lesson was explained by the teacher.', 'The lesson explained the teacher.', 'The teacher forgot the lesson.', 'The teacher explained the lesson.', 'Ubah ke pasif.'),
 ('Pilih parafrase terbaik: "Although it was cold, we went swimming."', 'We went swimming even though it was cold.', 'We did not go swimming because it was cold.', 'It was cold, so we went swimming.', 'Because it was hot, we swam.', 'Although = even though.'),
 ('Pilih parafrase terbaik: "He decided to leave."', 'He made a decision to leave.', 'He decided to stay.', 'He left the decision.', 'He was decided to leave.', 'Ubah kelas kata.'),
 ('Pilih parafrase terbaik: "Many students find maths difficult."', 'Maths is hard for many students.', 'Maths is easy for many students.', 'Few students find maths difficult.', 'Many students find maths difficult.', 'Difficult = hard.'),
 ('Pilih ringkasan terbaik untuk: "Recycling reduces waste, saves energy, and protects nature. For example, recycling one can saves enough energy to run a TV for three hours."', 'Recycling is beneficial because it reduces waste and saves energy.', 'Recycling one can runs a TV for three hours.', 'Nature is beautiful.', 'Recycling was invented long ago.', 'Gagasan utama saja.'),
 ('Pilih ringkasan terbaik untuk: "The town has a market, a library, and two schools. Most people work in farming. In the evening, the streets are quiet."', 'It is a small farming town with basic services.', 'The town has two schools and a market.', 'The streets are quiet.', 'The library is big.', 'Gagasan utama.'),
 ('Pilih parafrase yang SALAH makna: "The shop closes at nine."', 'The shop opens at nine.', 'The shop shuts at nine.', 'Nine o\'clock is closing time for the shop.', 'The store closes at 9.', 'Opens ≠ closes.'),
 ('Apa yang harus dijaga saat memparafrase?', 'makna, angka, dan fakta', 'kata-kata asli', 'jumlah kata saja', 'nama penulis', 'Jaga makna.'),
 ('Apa yang dibuang saat meringkas?', 'contoh dan detail kecil', 'gagasan utama', 'seluruh paragraf', 'angka penting', 'Buang detail.'),
 ('Mana yang BUKAN teknik parafrase?', 'menyalin kalimat asli', 'mengganti sinonim', 'mengubah struktur', 'mengubah kelas kata', 'Menyalin bukan parafrase.'),
])
P += mkf([
 ('Kota itu berpenduduk banyak.', 'The city has a large ___.', 'population', 'Population.'),
 ('Dia membeli ponsel baru.', 'She ___ a new phone. (sinonim buy)', 'purchased', 'Purchased.'),
 ('Pelajaran dijelaskan oleh guru.', 'The lesson was ___ by the teacher.', 'explained', 'Pasif.'),
 ('Walaupun dingin, kami berenang.', 'We swam even ___ it was cold.', 'though', 'Even though.'),
])
Q = P[:8]
UNIT["practice"] = P
UNIT["quiz"] = Q
