from qk import mk, mkf, mko

UNIT = dict(
 id="u79",
 goals=[
  "mengerjakan soal **matching headings** dengan membaca ide pokok paragraf",
  "mengerjakan **sentence completion** dan mematuhi **batas jumlah kata**",
  "membedakan **ide pokok** dan **detail pendukung**",
  "memeriksa **tata bahasa** jawaban agar cocok dengan kalimat",
 ],
 lesson=[
  dict(t="intro", text="Dua jenis soal Reading yang menuntut pemahaman terstruktur: **matching headings** (memilih judul untuk tiap paragraf) dan **completion** (melengkapi kalimat, catatan, atau tabel dengan kata dari teks)."),

  dict(t="grammar", title="1. Matching headings",
   table=[["Langkah", "Yang dilakukan"],
          ["1", "Baca semua judul pilihan lebih dulu, tandai kata kunci masing-masing"],
          ["2", "Baca kalimat pertama dan terakhir tiap paragraf (ide pokok)"],
          ["3", "Cocokkan ide pokok dengan judul yang paling mewakili seluruh paragraf"],
          ["4", "Coret judul yang sudah dipakai"]],
   examples=[dict(en="[[There are usually more headings than paragraphs.]]", id="Biasanya judul lebih banyak daripada paragraf; ada pengecoh.")]),

  dict(t="grammar", title="2. Jebakan matching headings",
   table=[["Jebakan", "Penjelasan"],
          ["kata sama, makna beda", "judul memuat kata dari paragraf tetapi bukan ide pokoknya"],
          ["detail, bukan ide pokok", "judul yang hanya mewakili satu kalimat detail"],
          ["terlalu luas", "judul yang menyentuh topik tetapi tidak spesifik"]]),

  dict(t="grammar", title="3. Sentence completion",
   table=[["Aturan", "Contoh"],
          ["patuhi batas kata", "[[NO MORE THAN TWO WORDS]] → jawaban maksimal dua kata"],
          ["salin ejaan dari teks", "[[strengthened]], bukan ~~strenghtened~~"],
          ["cocokkan tata bahasa", "[[The farms are ___ to build.]] → expensive (kata sifat)"],
          ["angka boleh digit atau kata", "[[two]] atau [[2]] jika teks memakainya"]]),

  dict(t="tip", title="Prediksi jenis kata sebelum mencari",
   text="Lihat kalimat yang kosong. Apakah yang hilang kata benda, kata sifat, kata kerja, atau angka? Itu mempersempit pencarianmu di teks."),
  dict(t="warn", title="Jawaban harus utuh dan benar secara tata bahasa",
   text="Jika kalimat berbunyi *The company plans to ___ new products*, jawabannya kata kerja bentuk dasar (*launch*), bukan *launched*. Periksa kembali setelah mengisi."),
 ],

 practice=mk([
  ('Dalam matching headings, judul yang tepat mewakili...', "ide pokok seluruh paragraf", "satu detail saja", "kata pertama paragraf", "angka dalam paragraf", "Ide pokok."),
  ('Jumlah judul pada soal matching headings biasanya...', "lebih banyak dari paragraf", "sama dengan paragraf", "lebih sedikit", "tidak pernah ada pengecoh", "Ada pengecoh."),
  ('Apa yang pertama kali dibaca pada paragraf saat mencari judul?', "kalimat pertama dan terakhir", "kalimat di tengah", "semua angka", "catatan kaki", "Ide pokok di awal atau akhir."),
  ('Perintah: "NO MORE THAN TWO WORDS". Jawaban yang diterima:', "high prices", "very high prices", "the high prices", "prices are high", "Maksimal dua kata."),
  ('Perintah: "ONE WORD ONLY". Jawaban yang diterima:', "expensive", "very expensive", "too expensive", "it is expensive", "Hanya satu kata."),
  ('Kalimat: "The farms are ___ to build." Jenis kata yang hilang:', "kata sifat", "kata kerja bantu", "kata sambung", "angka", "to build butuh adjektiva (expensive)."),
  ('Kalimat: "Roofs must be ___ first." Bentuk kata yang tepat:', "strengthened", "strengthen", "strengthening", "strength", "must be + V3."),
  ('Kalimat: "The company plans to ___ new products." Bentuk kata yang tepat:', "launch", "launched", "launching", "launches", "plans to + V1."),
  ('Kalimat: "The number rose to ___ percent." Jenis jawaban yang hilang:', "angka", "kata kerja", "kata sifat", "kata sambung", "Percent diawali angka."),
  ('Judul mana yang paling mungkin untuk paragraf tentang biaya dan masalah pertanian atap?', "The challenges of rooftop farming", "A history of Singapore", "Why vegetables are healthy", "The best restaurants", "Paragraf membahas masalah."),
  ('Judul mana yang paling mungkin untuk paragraf yang menjelaskan manfaat kesehatan jalan kaki?', "Health benefits of walking", "How shoes are made", "The history of roads", "Why cars are fast", "Manfaat kesehatan."),
  ('Pada matching headings, judul yang sudah dipakai sebaiknya...', "dicoret", "dipakai lagi", "diabaikan", "dihapus dari soal", "Coret agar tidak dipakai ulang."),
  ('Jika jawabanmu melebihi batas kata, maka...', "dianggap salah", "tetap benar", "dapat nilai separuh", "diabaikan", "Batas kata wajib dipatuhi."),
  ('Jawaban completion harus diambil dari...', "teks", "pengetahuan umum", "kamus", "tebakan bebas", "Salin dari teks."),
  ('Ejaan yang salah pada jawaban completion akan...', "dianggap salah", "dimaafkan", "dinilai separuh", "diabaikan", "Ejaan wajib benar."),
  ('Kalimat: "It is ___ to travel by plane." Mana yang paling mungkin?', "faster", "fastest", "to fast", "fastly", "Adjektiva perbandingan."),
 ]) + mkf([
  ("Judul harus mewakili ide ___ paragraf.", "A heading must match the ___ idea of the paragraph.", "main", "Ide pokok."),
  ("Setelah must be, pakai bentuk ke-3 (V3): must be ___ . (strengthen)", "Roofs must be ___.", "strengthened", "must be + V3."),
  ("Setelah plans to, pakai bentuk ___ . (launch)", "The company plans to ___ new products.", "launch", "plans to + V1."),
  ("Perintah 'NO MORE THAN ___ WORDS' berarti ada batas kata.", "NO MORE THAN TWO ___", "words", "Batas jumlah kata."),
 ]) + mko([
  ("Baca kalimat pertama setiap paragraf.", "Read the first sentence of every paragraph.", "reads reading", ""),
  ("Jawabannya harus diambil dari teks.", "The answer must come from the text.", "comes coming", ""),
  ("Ejaan yang salah dianggap salah.", "Wrong spelling is marked wrong.", "mark marking", ""),
 ]),

 quiz=mk([
  ('Judul yang tepat mewakili...', "ide pokok paragraf", "satu detail", "angka saja", "kata terakhir", "Ide pokok."),
  ('Judul pada soal matching headings biasanya...', "lebih banyak dari paragraf", "sama banyak", "lebih sedikit", "tidak ada pengecoh", "Ada pengecoh."),
  ('"NO MORE THAN TWO WORDS": jawaban yang benar...', "high prices", "very high prices", "the very high prices", "prices are high", "Dua kata."),
  ('Kalimat: "Roofs must be ___." Jawaban yang tepat:', "strengthened", "strengthen", "strength", "strengthening", "V3."),
  ('Jika ejaan salah, jawaban...', "dianggap salah", "dimaafkan", "dinilai separuh", "diabaikan", "Salah."),
  ('Jawaban completion diambil dari...', "teks", "pengetahuan umum", "tebakan", "soal lain", "Teks."),
  ('Judul untuk paragraf yang membahas manfaat sebuah program:', "The benefits of the program", "The history of tea", "Why shops close", "Traveling by train", "Manfaat."),
  ('Kalimat: "The company plans to ___ ." Bentuk kata yang hilang:', "kata kerja dasar", "kata sifat", "angka", "kata benda jamak", "plans to + V1."),
 ]) + mkf([
  ("Maks. satu kata: The farms are ___ to build. (mahal)", "The farms are ___ to build.", "expensive", "Adjektiva."),
  ("Jawaban harus diambil dari ___ .", "Copy the answer from the ___.", "text", "Salin dari teks."),
 ]),
)
