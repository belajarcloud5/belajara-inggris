from ub import *
UNIT = mkunit("u171",
 ["menyusun **esai opini** dengan thesis, alasan, contoh, dan kesimpulan",
  "menulis **kalimat topik** yang menyatakan posisi",
  "memakai **kata penghubung argumen** (firstly, however, in conclusion)",
  "menghindari **kesalahan umum** dalam esai opini"],
 [intro("Esai opini menyatakan pendapatmu dan membuktikannya. Strukturnya: **pengantar** dengan thesis, **dua paragraf isi** (alasan dan contoh), dan **kesimpulan**. Unit ini melatih menyusun dan memeriksa esai pendek."),
  gram("1. Struktur esai opini",
   table=[["Bagian", "Isi", "Contoh"],
          ["Pengantar", "latar singkat + thesis", "[[Many people use phones in class. I believe schools should limit this.]]"],
          ["Isi 1", "alasan pertama + contoh", "[[Firstly, phones distract students. For example, ...]]"],
          ["Isi 2", "alasan kedua + contoh", "[[Secondly, phones can be useful if used properly. However, ...]]"],
          ["Kesimpulan", "ulang thesis + saran", "[[In conclusion, schools should set clear rules.]]"]]),
  gram("2. Ungkapan untuk esai opini",
   table=[["Fungsi", "Ungkapan"],
          ["Menyatakan pendapat", "[[In my opinion, ...]] / [[I strongly believe that ...]]"],
          ["Urutan alasan", "[[Firstly, ...]] / [[Secondly, ...]] / [[Finally, ...]]"],
          ["Memberi contoh", "[[For example, ...]] / [[For instance, ...]]"],
          ["Mengakui pandangan lain", "[[Some people argue that ... However, ...]]"],
          ["Menyimpulkan", "[[In conclusion, ...]] / [[To sum up, ...]]"]]),
  warn("Thesis harus jelas", text="Thesis bukan pertanyaan atau fakta. Salah: *This essay is about phones.* Benar: [[I believe schools should limit phone use.]]"),
  tip("Satu paragraf, satu alasan", text="Setiap paragraf isi berisi satu alasan, dijelaskan, lalu diberi contoh. Jangan menumpuk banyak alasan dalam satu paragraf."),
  summary(["Pengantar + thesis, dua paragraf isi, kesimpulan.", "Firstly, Secondly, Finally; For example; However; In conclusion.", "Thesis jelas dan berpihak.", "Satu alasan per paragraf."])],
 [], [])
essays = [
 (["Many students use phones in class.", "I believe that schools should limit phone use during lessons.", "Firstly, phones distract students from learning.", "For example, they check messages instead of listening.", "In conclusion, clear rules will help students focus."], "Pengantar, thesis, alasan, contoh, kesimpulan."),
 (["Some people think homework is unnecessary.", "In my opinion, homework is useful in moderation.", "Firstly, it helps students practise what they learn.", "However, too much homework makes students tired.", "To sum up, teachers should give a balanced amount."], "Latar, thesis, alasan, kontras, kesimpulan."),
 (["Public transport is better than private cars.", "Firstly, it reduces traffic and pollution.", "For instance, one bus can replace many cars.", "Secondly, it is cheaper for most people.", "Therefore, cities should invest in public transport."], "Thesis, alasan 1, contoh, alasan 2, kesimpulan."),
 (["Learning English is important for young people.", "Firstly, it helps them find better jobs.", "Secondly, it allows them to access information online.", "Some people argue that it is too difficult.", "However, with daily practice, everyone can improve."], "Thesis, dua alasan, pandangan lain, bantahan."),
]
P = [seq(s, e, q="Susun kalimat-kalimat berikut menjadi esai opini pendek yang runtut.") for s, e in essays]
P += mk([
 ('Pilih thesis yang paling jelas:', 'I believe schools should start later in the morning.', 'This essay is about school time.', 'School starts early.', 'Is school time good?', 'Thesis menyatakan posisi.'),
 ('Pilih thesis yang paling jelas:', 'In my opinion, cities need more bicycle lanes.', 'There are many cities in the world.', 'Bicycles have two wheels.', 'I will write about bicycles.', 'Posisi jelas.'),
 ('Pilih ungkapan untuk memberi contoh:', 'For example,', 'In conclusion,', 'However,', 'Firstly,', 'Contoh.'),
 ('Pilih ungkapan untuk menyimpulkan:', 'In conclusion,', 'For instance,', 'Secondly,', 'Although,', 'Kesimpulan.'),
 ('Pilih ungkapan untuk mengakui pandangan lain:', 'Some people argue that ... However, ...', 'Everyone knows that ...', 'I do not care about ...', 'Nobody thinks that ...', 'Mengakui lalu membantah.'),
 ('Berapa alasan sebaiknya ada dalam satu paragraf isi?', 'satu alasan dengan contoh', 'lima alasan', 'tidak ada', 'semua alasan sekaligus', 'Fokus.'),
 ('Di mana thesis biasanya ditulis?', 'di pengantar', 'di kesimpulan saja', 'di tengah paragraf isi', 'di judul saja', 'Pengantar.'),
 ('Pilih kalimat kesimpulan yang baik:', 'To sum up, schools should set clear rules about phones.', 'And that is all.', 'Phones are phones.', 'The end of the essay.', 'Menegaskan thesis.'),
 ('Pilih kalimat pendukung yang paling kuat:', 'For example, one bus can carry sixty people, while a car carries four.', 'Buses are nice.', 'I like buses.', 'Buses exist.', 'Contoh konkret.'),
 ('Pilih kalimat yang SALAH sebagai thesis:', 'This essay will discuss homework.', 'I believe homework should be limited.', 'In my opinion, homework helps students.', 'I strongly think homework is necessary.', 'Bukan posisi.'),
])
P += [spot(["Many people think the internet is dangerous.", "I believe it is useful when used carefully.", "Firstly, it gives us fast access to information.", "Secondly, it also helps us talks with friends.", "In conclusion, the internet is a good tool."], 3, "helps us talk."),
      spot(["Some people prefer living in cities.", "In my opinion, villages is better for children.", "They are quiet and safe.", "Therefore, families should consider moving."], 1, "villages are better.")]
Q = P[-8:]
UNIT["practice"] = P
UNIT["quiz"] = Q
