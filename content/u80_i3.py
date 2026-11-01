from ielts_h import ask, tfn
T = "Online platforms have changed how students learn. A student can now enrol in a course from another country, attend lectures by video, and submit assignments digitally. Critics argue that the curriculum is often less interactive than in a classroom and that some students lack reliable access to the internet. Supporters, however, point out that the tuition is cheaper and that learners can study at a flexible pace."
I3 = dict(practice=ask(T, [
 ("Apa gagasan utama teks?", "belajar online mengubah cara belajar siswa", "guru tidak lagi dibutuhkan sekolah", "internet selalu lebih baik daripada kelas", "kuliah hanya untuk orang kaya", "Kalimat pertama merangkum isi."),
 ("Kata 'enrol' paling dekat dengan...", "mendaftar", "lulus", "mengajar", "meninggalkan", "Enrol = mendaftar."),
 ("Kata 'submit' paling dekat dengan...", "menyerahkan", "menyalin", "menghapus", "membaca", "Submit assignments = menyerahkan tugas."),
 ("Kata 'tuition' dalam teks berarti...", "biaya kuliah", "jadwal kuliah", "gelar sarjana", "kamus", "Tuition = biaya pendidikan."),
 ("Kata 'reliable' paling dekat dengan...", "dapat diandalkan", "murah dan hemat biaya", "cepat sekali dibuka", "gratis untuk semua", "Reliable = dapat diandalkan."),
 ("Kata 'interactive' berhubungan dengan...", "banyak komunikasi dua arah", "banyak hafalan di rumah", "banyak PR setiap hari", "banyak buku tebal", "Interactive = interaktif."),
 ("Pilih kata pengisi (NO MORE THAN TWO WORDS): 'Learners can study at a ___ pace.'", "flexible", "very fast and strict", "the same", "never", "Teks: flexible pace.")]) + tfn(T, [
 ("Students can enrol in courses from other countries.", 'T', "Disebut langsung."),
 ("All students have reliable internet access.", 'F', "Teks: some students lack."),
 ("Critics say online tuition is more expensive.", 'F', "Supporters yang menyebut lebih murah."),
 ("Online courses are always shorter than classroom courses.", 'N', "Lama kursus tidak dibandingkan.")]),
 quiz=ask(T, [
 ("Siapa yang menyebut biaya lebih murah?", "pendukung (supporters)", "pengkritik (critics) kursus", "para guru di kelas", "pejabat pemerintah", "Supporters ... tuition is cheaper."),
 ("Mana kolokasi yang benar?", "attend lectures", "make lectures up", "do lectures at", "carry lectures", "Attend lectures."),
 ("Pilih bentuk kata: 'Students submit their work ___.' (digital)", "digitally", "digital", "digit", "digitise", "Adverb setelah kata kerja."),
 ("Kata penghubung 'however' di teks menandai...", "pandangan yang berlawanan", "contoh yang menambah", "kesimpulan dari teks", "sebab dan akibat", "However = perlawanan.")]))
