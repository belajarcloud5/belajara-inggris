from qk import mk
X2 = dict(practice=mk([
 ('Pilih kalimat yang benar:', 'My teacher, Ms. Sari, lives in Jakarta.', 'my teacher, ms. Sari, lives in jakarta.', 'My Teacher, ms. sari, lives in Jakarta.', 'My teacher Ms. Sari lives in jakarta.', 'Kapital pada awal, gelar, nama, kota.'),
 ('Pilih kalimat yang benar:', 'We celebrate Independence Day in August.', 'we celebrate independence day in august.', 'We celebrate independence day in August.', 'We Celebrate Independence Day In august.', 'Hari libur dan bulan kapital.'),
 ('Pilih kalimat yang benar:', 'She speaks Indonesian, English, and Japanese.', 'She speaks indonesian, english, and japanese.', 'She speaks Indonesian English and Japanese.', 'she speaks Indonesian, English, and Japanese.', 'Bahasa kapital; daftar dipisah koma.'),
 ('Pilih kalimat yang benar:', 'What time does the train leave?', 'What time does the train leave.', 'What time does the train leave!', 'what time does the train leave?', 'Pertanyaan → ? dan kapital.'),
 ('Pilih kalimat yang benar:', 'Be careful! The floor is wet.', 'Be careful. The floor is wet!', 'be careful! the floor is wet.', 'Be careful? The floor is wet.', 'Peringatan → !'),
 ('Pilih kalimat yang benar:', 'After school, I go home.', 'After school I, go home.', 'After, school I go home.', 'After school. I go home.', 'Frasa pembuka + koma.'),
 ('Pilih kalimat yang benar:', 'I like tea, but my brother likes coffee.', 'I like tea but, my brother likes coffee.', 'I like tea, but, my brother likes coffee.', 'I like tea but my brother, likes coffee.', 'Koma sebelum but pada dua klausa.'),
 ('Pilih kalimat yang benar:', "It's Dina's birthday today.", "Its Dina's birthday today.", "It's Dinas birthday today.", "Its Dinas' birthday today.", 'It is; milik Dina.'),
 ('Pilih kalimat yang benar:', "The teachers' room is on the left.", "The teacher's room is on the left. (banyak guru)", "The teachers room is on the left.", "The teachers's room is on the left.", 'Milik jamak → s\'.'),
 ('Pilih kalimat yang benar:', 'He said, "I am hungry."', 'He said "I am hungry.', 'He said, I am hungry."', 'He said, "I am hungry".', 'Kutipan langsung.'),
 ('Pilih kalimat yang benar:', 'On Monday, Tuesday, and Friday I study English.', 'On monday, tuesday, and friday I study english.', 'On Monday Tuesday and Friday, I study English.', 'On Monday, Tuesday and, Friday I study English.', 'Hari dan bahasa kapital; daftar koma.'),
 ('Pilih kalimat yang SALAH:', 'i live in Bali.', 'I live in Bali.', 'Bali is nice.', 'My name is Rani.', 'I harus kapital.'),
 ('Pilih kalimat yang SALAH:', 'She is from japan.', 'She is from Japan.', 'He lives in Tokyo.', 'They speak Japanese.', 'Negara kapital.'),
 ('Pilih kalimat yang SALAH:', 'Where is my bag!', 'Where is my bag?', 'I found my bag.', 'Look at my bag!', 'Pertanyaan → ?'),
 ('Pilih kalimat yang SALAH:', 'Do not forget your pens pencils and rulers.', 'Do not forget your pens, pencils, and rulers.', 'Bring a pen.', 'Bring a pen, please.', 'Daftar perlu koma.'),
 ('Pilih kalimat yang SALAH:', "We dont have class today.", "We don't have class today.", "I can't come.", "She isn't here.", 'Singkatan butuh apostrof.'),
 ('Apa fungsi koma setelah "However"?', 'memisahkan kata pembuka dari kalimat', 'mengakhiri kalimat', 'menandai pertanyaan', 'menandai ucapan', 'Kata pembuka + koma.'),
 ('Tanda apa yang menandai kepemilikan?', 'apostrof + s', 'titik dua', 'tanda tanya', 'tanda seru', "Rani's bag."),
]))
X2["quiz"] = mk([
 ('Pilih kalimat yang benar:', 'Rani lives in Medan.', 'rani lives in medan.', 'Rani Lives In Medan.', 'rani lives in Medan.', 'Nama dan kota.'),
 ('Pilih kalimat yang benar:', 'When he arrived, we ate dinner.', 'When he arrived we, ate dinner.', 'When, he arrived we ate dinner.', 'When he arrived. we ate dinner.', 'Klausa pembuka + koma.'),
 ('Pilih kalimat yang benar:', "They're my cousins.", "Theyre my cousins.", "They'r my cousins.", "Th'ey're my cousins.", 'They are.'),
 ('Pilih kalimat yang SALAH:', 'can you help me?', 'Can you help me?', 'Please help me.', 'Help!', 'Awal kalimat kapital.'),
])
