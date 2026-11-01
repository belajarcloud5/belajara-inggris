from ielts_h import ask
P = "Paragraph A: Many people think that cities are growing because of jobs. Actually, cheap public transport also plays a major role, since it lets workers live far from their offices. Paragraph B: Housing, however, has not kept pace. Rents have doubled in ten years, and young families often share small flats. Paragraph C: Some cities now build apartments near train stations. This approach is called transit-oriented development and it reduces both traffic and rent."
Q = "A museum opened in 2005 to show the history of cotton. It has three halls. The first hall explains how cotton grows, the second shows old machines, and the third has a shop. Entry is free for children, and school groups need to book at least a week before."
I2 = dict(practice=ask(P, [
 ("Pilih judul terbaik untuk Paragraph A:", "Transport and city growth", "The cost of renting", "Building near stations", "A history of jobs", "A membahas transportasi murah dan pertumbuhan kota."),
 ("Pilih judul terbaik untuk Paragraph B:", "Rising rents and small homes", "Cheap transport", "A new type of train", "Why people leave cities", "B membahas sewa naik dan hunian."),
 ("Pilih judul terbaik untuk Paragraph C:", "A solution: building near stations", "The problem of traffic", "Rising public transport costs", "The history of offices", "C membahas solusi."),
 ("Pilih kata pengisi (NO MORE THAN TWO WORDS): 'Cheap public transport lets workers live ___ their offices.'", "far from", "very near to", "in front of", "above the", "Teks: live far from their offices."),
 ("Pilih kata pengisi (NO MORE THAN TWO WORDS): 'Rents have ___ in ten years.'", "doubled", "fallen slowly", "stayed the same", "been reduced", "Teks: doubled."),
 ("Pilih kata pengisi (NO MORE THAN TWO WORDS): 'Young families often share ___.'", "small flats", "big houses", "new cars", "train tickets", "Teks: small flats."),
 ("Pilih kata pengisi (NO MORE THAN TWO WORDS): 'The new approach reduces traffic and ___.'", "rent", "jobs", "stations", "buildings", "Teks: reduces both traffic and rent."),
 ("Jawaban mana yang sesuai batas 'NO MORE THAN TWO WORDS' untuk 'Young families often share ___'?", "small flats", "shared small flats", "the small flats here", "small and old flats", "Dua kata atau kurang."),
 ("Saat mencocokkan heading, apa yang sebaiknya dicari?", "gagasan utama tiap paragraf", "satu kata acak", "kata terpanjang", "angka saja", "Heading = ide utama paragraf."),
 ("Heading mana yang terlalu sempit untuk Paragraph A?", "Cheap fares on buses", "Transport and city growth", "Why cities grow", "Public transport and workers", "Terlalu sempit: hanya satu detail."),
]) + ask(Q, [
 ("Kapan museum dibuka?", "2005", "2015", "1995", "2025", "opened in 2005."),
 ("Berapa aula yang dimiliki museum?", "tiga", "dua", "empat", "lima", "three halls."),
 ("Aula mana yang menjual barang? (Isian: The third hall has a ___)", "shop", "machine", "cotton", "ticket", "Teks: the third has a shop."),
 ("Siapa yang masuk gratis?", "anak-anak", "guru", "turis asing", "semua orang", "free for children."),
 ("Kapan kelompok sekolah harus memesan?", "paling lambat seminggu sebelumnya", "pada hari yang sama", "sebulan sebelumnya", "tidak perlu memesan", "at least a week before."),
 ("Pilih heading yang cocok untuk seluruh teks:", "A museum about cotton", "A new school trip", "The history of shopping", "How to book a ticket", "Gagasan utama.")]),
 quiz=ask(P, [
 ("Paragraf mana yang menyebut solusi?", "Paragraph C", "Paragraph A", "Paragraph B", "tidak ada", "C memberi solusi."),
 ("Kata 'kept pace' paling dekat dengan...", "bergerak setara", "berhenti", "berlari cepat", "menjadi mahal", "Keep pace = mengimbangi."),
 ("Pilih kata pengisi (NO MORE THAN TWO WORDS): 'Cheap transport plays a ___ role.'", "major", "very major and large", "small", "never", "Teks: major role."),
 ("Pilih kata pengisi (NO MORE THAN TWO WORDS): 'This approach is called ___ development.'", "transit-oriented", "very good traffic", "new city", "cheap rent", "Teks menyebut transit-oriented.")]))
