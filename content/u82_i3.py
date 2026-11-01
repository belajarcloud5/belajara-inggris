from ielts_h import ask, tfn
T = "Unemployment affects not only income but also mental wellbeing. Studies show that people without work are more likely to suffer from stress and chronic illness. Employers can help by offering flexible hours and fair salaries, while governments invest in training. A strong economy depends on a healthy workforce, since illness reduces productivity and increases health expenses."
I3 = dict(practice=ask(T, [
 ("Apa gagasan utama teks?", "pengangguran memengaruhi pendapatan dan kesehatan jiwa", "gaji tinggi menyembuhkan semua penyakit", "orang sehat tidak perlu bekerja", "sekolah selalu mengurangi stres", "Kalimat pertama."),
 ("Kata 'wellbeing' berarti...", "kesejahteraan", "kekayaan", "kecepatan", "kekuatan", "Wellbeing = kesejahteraan."),
 ("Kata 'chronic' berarti...", "menahun", "ringan", "menular", "mendadak", "Chronic illness = penyakit menahun."),
 ("Kata 'workforce' berarti...", "tenaga kerja", "tempat kerja", "jam kerja", "gaji kerja", "Workforce = angkatan kerja."),
 ("Kata 'productivity' berarti...", "hasil kerja yang dicapai", "waktu libur yang panjang", "biaya hidup bulanan", "jumlah pegawai kantor", "Productivity = produktivitas."),
 ("Kata 'expenses' berarti...", "pengeluaran", "pendapatan", "keuntungan", "tabungan", "Expense = pengeluaran."),
 ("Pilih kata pengisi (NO MORE THAN TWO WORDS): 'Employers can offer ___ hours.'", "flexible", "very long and hard", "the", "never", "Teks: flexible hours.")]) + tfn(T, [
 ("Unemployed people may suffer from stress.", 'T', "more likely to suffer from stress."),
 ("Governments should stop investing in training.", 'F', "Teks: governments invest in training."),
 ("Illness reduces productivity.", 'T', "Disebut langsung."),
 ("Unemployment is highest among young people.", 'N', "Tidak disebut.")]),
 quiz=ask(T, [
 ("Mana kolokasi yang benar?", "suffer from stress", "suffer to stress", "suffer of stress", "suffer stress at", "Suffer from."),
 ("Pilih bentuk kata: 'A ___ economy needs healthy workers.' (strong)", "strong", "strength", "strongly", "strengthen", "Kata sifat sebelum benda."),
 ("Siapa yang berinvestasi dalam pelatihan?", "pemerintah", "pegawai", "dokter", "siswa", "governments invest in training."),
 ("Kata 'fair' pada 'fair salaries' berarti...", "adil", "tinggi sekali", "rendah", "tetap", "Fair = adil.")]))
