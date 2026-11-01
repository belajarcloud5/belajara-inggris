from ielts_h import ask, tfn
T = "Rapid urbanisation has created serious problems. As more people migrate from rural areas to cities, housing becomes expensive and traffic congestion worsens. Emissions from vehicles contribute to pollution and threaten public health. Governments are responding with subsidies for renewable energy, campaigns to raise awareness, and investment in infrastructure such as metro lines."
I3 = dict(practice=ask(T, [
 ("Apa gagasan utama teks?", "urbanisasi menimbulkan masalah dan pemerintah menanggapinya", "kota selalu lebih baik daripada desa", "semua orang ingin kembali ke desa", "metro lebih mahal daripada mobil pribadi", "Masalah dan tanggapan."),
 ("Kata 'migrate' paling dekat dengan...", "berpindah tempat tinggal", "bepergian untuk liburan", "pulang ke kampung halaman", "bekerja lembur di kantor", "Migrate = bermigrasi."),
 ("Kata 'congestion' berarti...", "kemacetan", "kebisingan", "kecelakaan", "kecepatan", "Traffic congestion = kemacetan."),
 ("Kata 'emissions' berarti...", "gas buangan", "makanan sisa", "air limbah", "suara mesin", "Emissions = emisi."),
 ("Kata 'subsidies' berarti...", "bantuan dana dari pemerintah", "pajak tambahan untuk warga", "denda bagi pelanggar aturan", "hadiah undian dari bank", "Subsidy = subsidi."),
 ("Kata 'infrastructure' berarti...", "jalan, rel, dan fasilitas umum", "pakaian, makanan, dan obat", "hutan, sungai, dan gunung", "sekolah swasta dan kampus", "Infrastructure = infrastruktur."),
 ("Pilih kata pengisi (NO MORE THAN TWO WORDS): 'Housing becomes ___.'", "expensive", "very cheap and nice", "the best", "empty", "Teks: expensive.")]) + tfn(T, [
 ("People move from rural areas to cities.", 'T', "migrate from rural areas to cities."),
 ("Traffic congestion becomes better as cities grow.", 'F', "Teks: worsens."),
 ("Vehicle emissions can harm public health.", 'T', "threaten public health."),
 ("Governments have banned all private cars.", 'N', "Tidak disebut.")]),
 quiz=ask(T, [
 ("Mana kolokasi yang benar?", "raise awareness", "raise subsidies", "make congestion up", "carry emissions", "Raise awareness."),
 ("Pilih bentuk kata: 'Urban ___ is growing fast.' (populate)", "population", "populate", "populous", "populating", "Kata benda setelah urban."),
 ("Contoh tanggapan pemerintah di teks:", "investasi di jalur metro", "pelarangan desa baru", "penutupan pusat kota", "kenaikan harga sewa", "investment in infrastructure."),
 ("Kata 'rural' lawan dari...", "urban", "native", "local", "wild", "Rural >< urban.")]))
