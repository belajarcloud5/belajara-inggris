from ielts_h import ask
T = "The first bicycle appeared in the early nineteenth century, but it had no pedals. Riders pushed it along with their feet. Pedals were added in the 1860s, which made the bike much faster but also very uncomfortable, so it was nicknamed the 'boneshaker'. In the 1880s the safety bicycle, with two wheels of the same size, became popular. By 1900 cycling had become a common way to travel, especially for women, who gained new freedom of movement."
I4 = dict(practice=ask(T, [
 ("Skimming: teks ini membahas...", "perkembangan sejarah sepeda", "cara memperbaiki sepeda", "olahraga bersepeda modern", "pabrik sepeda terbesar", "Gambaran umum."),
 ("Scanning: kapan pedal ditambahkan?", "tahun 1860-an", "tahun 1880-an", "tahun 1900", "awal abad ke-19", "Teks: in the 1860s."),
 ("Scanning: apa julukan sepeda berpedal awal?", "boneshaker", "safety bicycle", "push bike", "wheel racer", "Teks: nicknamed the 'boneshaker'."),
 ("Scanning: sepeda aman memiliki...", "dua roda berukuran sama", "tiga roda berukuran kecil", "satu roda besar di depan", "dua roda tanpa rem sama sekali", "two wheels of the same size."),
 ("Siapa yang mendapat kebebasan bergerak?", "kaum perempuan", "anak-anak", "para pekerja pabrik", "para pelaut", "women, who gained new freedom."),
 ("Kata 'uncomfortable' paling dekat dengan...", "tidak nyaman", "sangat cepat", "mahal", "berbahaya", "Uncomfortable = tidak nyaman."),
 ("Kata 'common' paling dekat dengan...", "umum", "langka", "mahal", "baru", "Common = umum."),
 ("Teknik terbaik untuk mencari tahun adalah...", "scanning angka", "membaca tiap kata", "menerjemahkan semuanya", "menghafal paragraf", "Cari angka dengan scanning.")]),
 quiz=ask(T, [
 ("Pada awalnya, bagaimana pengendara menggerakkan sepeda?", "mendorong dengan kaki", "mengayuh pedal dengan kaki", "memakai mesin kecil di depan", "ditarik oleh hewan peliharaan", "pushed it along with their feet."),
 ("Skimming: kalimat pertama paragraf biasanya...", "menyatakan gagasan utama", "berisi kesimpulan akhir", "berupa pertanyaan penguji", "berisi tabel", "Topic sentence."),
 ("Kata 'popular' paling dekat dengan...", "disukai banyak orang", "tidak dikenal siapa pun", "sangat mahal harganya", "sangat kecil ukurannya", "Popular = populer."),
 ("Pada tahun 1900, bersepeda sudah...", "menjadi cara bepergian yang umum", "dilarang di banyak kota", "belum ditemukan oleh siapa pun", "hanya dipakai untuk lomba", "common way to travel.")]))
