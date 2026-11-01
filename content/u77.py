from qk import mk, mkf, mko

UNIT = dict(
 id="u77",
 goals=[
  "membedakan **skimming** (gambaran umum) dan **scanning** (mencari info spesifik)",
  "menemukan **ide pokok** dari kalimat pertama dan terakhir paragraf",
  "mencari **kata kunci**, angka, nama, dan tanggal dengan cepat",
  "mengatur waktu **60 menit** untuk tiga teks Reading",
 ],
 lesson=[
  dict(t="intro", text="Teks Reading IELTS panjang dan waktunya terbatas. Kamu tidak boleh membaca kata per kata. Dua keterampilan kuncinya: **skimming** untuk memahami gambaran umum, dan **scanning** untuk mencari informasi spesifik."),

  dict(t="grammar", title="1. Skimming dan scanning",
   table=[["Teknik", "Tujuan", "Cara"],
          ["**Skimming**", "tahu topik dan struktur teks", "baca judul, kalimat pertama dan terakhir tiap paragraf; abaikan detail"],
          ["**Scanning**", "menemukan jawaban spesifik", "cari kata kunci, angka, nama, tanggal; baca sekitar kata itu saja"]],
   examples=[dict(en="[[Skim first to understand the topic. Scan next to find the answer.]]", id="Skimming dulu untuk memahami topik. Scanning berikutnya untuk menemukan jawaban.")]),

  dict(t="grammar", title="2. Langkah mengerjakan satu teks",
   table=[["Langkah", "Waktu", "Yang dilakukan"],
          ["1", "1 menit", "baca judul dan sub-judul; skim seluruh teks"],
          ["2", "1 menit", "baca perintah dan soal"],
          ["3", "14 menit", "scan jawaban sesuai urutan soal"],
          ["4", "2 menit", "cek ejaan dan batas jumlah kata"]]),

  dict(t="grammar", title="3. Kata kunci",
   text="Soal sering memakai **sinonim**, bukan kata yang sama dengan teks. Cari kata kunci, lalu pikirkan padanannya.",
   table=[["Di soal", "Mungkin di teks"],
          ["increase", "rise, grow, go up"],
          ["reduce", "lower, cut, decrease"],
          ["important", "essential, vital, key"],
          ["begin", "start, launch, set up"]],
   examples=[dict(en="[[Soal: The number of farms increased. Teks: The number of farms rose.]]", id="Kata increase di soal menjadi rose di teks.")]),

  dict(t="tip", title="Angka, nama, dan tanggal",
   text="Pada soal yang menanyakan angka, nama, atau tanggal, scan huruf besar dan angka lebih dulu. Itu cara tercepat menemukan jawaban."),
  dict(t="warn", title="Jangan membaca semuanya",
   text="Jika kamu menerjemahkan setiap kata, 60 menit tidak akan cukup. Percayalah pada strategi: gambaran umum dulu, jawaban kemudian."),
 ],

 practice=mk([
  ('Teknik membaca cepat untuk memahami gambaran umum disebut...', "skimming", "scanning", "translating", "memorizing", "Skimming = gambaran umum."),
  ('Teknik mencari informasi spesifik disebut...', "scanning", "skimming", "spelling", "listening", "Scanning = mencari info spesifik."),
  ('Saat skimming, bagian yang sebaiknya dibaca adalah...', "judul dan kalimat pertama tiap paragraf", "semua kata", "hanya angka", "hanya paragraf terakhir", "Judul dan kalimat pertama."),
  ('Untuk mencari tahun atau angka, scan...', "angka dan huruf besar", "kata sambung", "kata sifat", "kata kerja bantu", "Angka dan huruf besar menonjol."),
  ('Soal berbunyi "The number of visitors increased." Padanan yang mungkin di teks adalah...', "rose", "stopped", "ended", "closed", "increase ≈ rise."),
  ('Soal memakai "reduce". Padanan di teks yang mungkin adalah...', "cut", "build", "start", "open", "reduce ≈ cut."),
  ('Soal memakai "essential". Padanan di teks yang mungkin adalah...', "vital", "slow", "tiny", "late", "essential ≈ vital."),
  ('Soal memakai "begin". Padanan di teks yang mungkin adalah...', "launch", "finish", "close", "stop", "begin ≈ launch."),
  ('Berapa menit sebaiknya dipakai untuk satu teks Reading?', "Sekitar 20 menit", "Sekitar 5 menit", "Sekitar 40 menit", "Sekitar 60 menit", "60 menit / 3 teks."),
  ('Langkah pertama saat membuka satu teks adalah...', "skim judul dan struktur", "menerjemahkan semuanya", "langsung mengisi jawaban", "membaca dari kata terakhir", "Skim dulu."),
  ('Soal biasanya memakai kata yang...', "berbeda (sinonim) dari teks", "persis sama dengan teks", "selalu angka", "selalu nama orang", "Parafrase sering dipakai."),
  ('Jika sulit menemukan jawaban satu soal, sebaiknya...', "lanjut ke soal berikutnya dan kembali nanti", "berhenti di soal itu 10 menit", "mengosongkan semuanya", "menerjemahkan seluruh teks", "Atur waktu."),
  ('Kalimat yang biasanya memuat ide pokok paragraf adalah...', "kalimat pertama", "kalimat contoh", "kalimat di tengah", "kata terakhir", "Topic sentence biasanya di awal."),
  ('Mana yang BUKAN bagian dari skimming?', "membaca setiap kata dengan teliti", "membaca judul", "membaca kalimat pertama paragraf", "melihat struktur teks", "Skimming tidak membaca setiap kata."),
  ('Mana yang paling tepat untuk menemukan nama orang di teks?', "mencari huruf besar", "mencari kata kerja bantu", "mencari kata sifat", "mencari kata sambung", "Nama diawali huruf besar."),
  ('Setelah selesai menjawab, apa yang perlu dicek?', "ejaan dan batas jumlah kata", "jumlah paragraf", "warna kertas", "judul teks", "Ejaan dan batas kata."),
 ]) + mkf([
  ("Teknik mencari informasi spesifik disebut ___ .", "The technique for finding specific information is called ___.", "scanning", "Scanning."),
  ("Teknik membaca untuk gambaran umum disebut ___ .", "The technique for getting the general idea is called ___.", "skimming", "Skimming."),
  ("Soal memakai 'increase', teks memakai ___ . (naik)", "increase = rise = ___ up", "go", "go up."),
  ("Soal memakai 'important', teks mungkin memakai ___ .", "important = ___ (kata penting)", "essential/vital/key", "Sinonim penting."),
 ]) + mko([
  ("Pertama, baca judul dan kalimat pertama.", "First, read the title and the first sentence.", "reads reading", ""),
  ("Cari kata kunci di dalam teks.", "Look for the key words in the text.", "looks looking", ""),
  ("Jangan menerjemahkan setiap kata.", "Do not translate every word.", "translates translating", ""),
 ]),

 quiz=mk([
  ('Teknik membaca cepat untuk gambaran umum:', "skimming", "scanning", "spelling", "writing", "Skimming."),
  ('Teknik mencari informasi spesifik:', "scanning", "skimming", "translating", "memorizing", "Scanning."),
  ('Soal memakai "rise". Padanan di teks bisa...', "increase", "lose", "stop", "hide", "rise ≈ increase."),
  ('Untuk menemukan angka, scan...', "angka dan huruf besar", "kata sambung", "kata kerja", "artikel", "Angka menonjol."),
  ('Sekitar berapa menit per teks?', "20 menit", "5 menit", "45 menit", "60 menit", "60 / 3."),
  ('Mana yang BUKAN skimming?', "membaca setiap kata", "membaca judul", "membaca kalimat pertama", "melihat struktur", "Skimming tidak per kata."),
  ('Kalimat yang biasanya memuat ide pokok:', "kalimat pertama", "kalimat contoh", "kata terakhir", "angka", "Topic sentence."),
  ('Soal tersulit sebaiknya...', "dilewati dulu", "dikerjakan 10 menit", "dikosongkan", "dihapus", "Lanjut dan kembali."),
 ]) + mkf([
  ("Scan untuk mencari ___ yang spesifik.", "We scan to find ___ information.", "specific", "Spesifik."),
  ("Skim untuk memahami ide ___ .", "We skim to understand the ___ idea.", "general/main", "Umum atau pokok."),
 ]),
)
