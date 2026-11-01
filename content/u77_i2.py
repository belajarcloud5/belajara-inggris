from ielts_h import ask
A = "Lake Tobe was formed about 70,000 years ago by a huge volcanic eruption. Today it is a popular tourist place. Every year more than 200,000 people visit the lake, mostly in July and August. Visitors can swim, take boat trips, or walk around the island in the middle. Hotels near the lake are expensive in summer, so many tourists camp instead."
B = "In 2015 the school started a recycling programme. At first only the science club took part, but by 2018 every class was involved. The programme collects paper, plastic bottles, and cans. Last year the students collected two tonnes of waste. The money from selling it was used to buy books for the school library."
I2 = dict(practice=ask(A, [
 ("Skimming: Apa gagasan utama teks?", "tempat wisata yang terbentuk dari letusan gunung", "cara membuat perahu untuk wisata", "harga hotel di kota-kota besar", "sejarah olahraga air di sungai", "Skim: kalimat pertama dan seluruh gambaran."),
 ("Scanning: Berapa tahun lalu danau itu terbentuk?", "sekitar 70.000 tahun", "sekitar 200.000 tahun", "sekitar 7.000 tahun", "sekitar 2.000 tahun", "Scan angka: 70,000 years ago."),
 ("Scanning: Berapa pengunjung per tahun?", "lebih dari 200.000", "lebih dari 70.000", "lebih dari 20.000", "lebih dari 2 juta", "Scan: more than 200,000."),
 ("Scanning: Bulan apa paling ramai?", "Juli dan Agustus", "Januari dan Februari", "Maret dan April", "Oktober dan November", "Scan nama bulan."),
 ("Scanning: Apa yang ada di tengah danau?", "sebuah pulau", "sebuah hotel", "sebuah jembatan", "sebuah pasar", "island in the middle."),
 ("Mengapa banyak turis berkemah?", "hotel mahal di musim panas", "danau terlalu dingin di musim panas", "tidak ada jalan menuju hotel", "kemah di sana gratis", "Sebab disebut setelah so."),
 ("Padanan kata dalam teks untuk 'enormous' (sangat besar):", "huge", "popular", "expensive", "middle", "Huge = sangat besar."),
 ("Padanan kata dalam teks untuk 'costly':", "expensive", "popular", "volcanic", "mostly", "Expensive = mahal.")]) + ask(B, [
 ("Skimming: Teks ini terutama tentang...", "program daur ulang di sekolah", "klub sains di kota kecil", "toko buku baru di sekolah", "lomba lari antar sekolah", "Gambaran umum: recycling programme."),
 ("Scanning: Tahun berapa program dimulai?", "2015", "2018", "2022", "2005", "Scan angka tahun."),
 ("Scanning: Berapa ton sampah terkumpul tahun lalu?", "dua ton", "satu ton", "dua belas ton", "dua puluh ton", "two tonnes."),
 ("Scanning: Apa yang dibeli dengan uangnya?", "buku untuk perpustakaan", "komputer baru untuk kelas", "seragam untuk murid", "alat olahraga sekolah", "buy books for the library."),
 ("Pada awalnya, siapa yang ikut serta?", "klub sains", "semua kelas", "para guru", "orang tua", "At first only the science club."),
 ("Padanan 'took part' dalam soal 'participated':", "took part", "collected", "started", "sold", "Take part = ikut serta."),
 ("Padanan 'involved' dalam teks untuk 'included':", "involved", "collected", "bought", "started", "Involved = terlibat."),
 ("Untuk mencari kata 'tonnes', teknik yang tepat:", "scanning", "skimming", "menerjemahkan semua", "menghafal teks", "Mencari kata tertentu → scanning.")]),
 quiz=ask(A, [
 ("Scanning: Kegiatan apa yang disebut?", "berenang dan naik perahu", "bermain sepak bola di tepi", "mendaki gunung berapi", "memancing di malam hari", "swim, boat trips."),
 ("Skimming: Nada teks ini...", "informatif dan netral", "marah dan kecewa", "lucu dan santai", "sedih dan emosional", "Teks informasi wisata."),
 ("Scanning: Apa yang terjadi 70.000 tahun lalu?", "letusan gunung berapi", "pembukaan hotel pertama", "perayaan besar di pulau", "banjir yang sangat besar", "formed by a huge volcanic eruption."),
 ("Kata 'mostly' paling dekat dengan...", "terutama", "jarang", "tidak pernah", "selalu", "Mostly = terutama.")]) + ask(B, [
 ("Skimming: program ini membuat sekolah...", "lebih peduli lingkungan", "lebih besar dari sebelumnya", "lebih cepat dalam belajar", "lebih murah bagi orang tua", "Gagasan umum."),
 ("Scanning: Bahan apa yang dikumpulkan?", "kertas, botol plastik, kaleng", "kaca dan kayu bekas", "baju bekas dan sepatu", "makanan dari kantin", "paper, plastic bottles, cans.")]))
