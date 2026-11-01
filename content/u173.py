from ub import *
UNIT = mkunit("u173",
 ["menulis **catatan, pengumuman, dan pesan singkat** yang jelas",
  "memilih **tingkat kesopanan** untuk pembaca yang berbeda",
  "memuat informasi penting: **siapa, apa, kapan, di mana**",
  "menyingkat tanpa kehilangan makna"],
 [intro("Pesan singkat, catatan, dan pengumuman harus **jelas dan langsung**. Pembaca tidak punya banyak waktu, jadi tulislah informasi penting dengan sopan dan ringkas."),
  gram("1. Informasi yang harus ada",
   table=[["Jenis", "Isi penting", "Contoh"],
          ["Pesan singkat", "siapa, apa, kapan", "[[Hi Rani, I'll be 10 minutes late. Please start without me.]]"],
          ["Catatan di rumah", "pesan + permintaan", "[[Mom, I've gone to Dina's house. Back at six.]]"],
          ["Pengumuman", "apa, kapan, di mana, siapa", "[[The science club meets on Tuesday at 3 p.m. in Room 12.]]"],
          ["Pesan resmi", "salam + tujuan + penutup", "[[Dear Ms. Sari, I am writing to ask about ... Thank you.]]"]]),
  gram("2. Kesopanan",
   table=[["Pembaca", "Contoh"],
          ["Teman", "[[Can you send me the notes?]]"],
          ["Guru / atasan", "[[Could you please send me the notes?]]"],
          ["Layanan publik", "[[I would be grateful if you could send me ...]]"]]),
  tip("Baca ulang sebagai penerima", text="Tanyakan: apakah pembaca tahu apa yang harus dilakukan, kapan, dan di mana? Jika tidak, tambahkan informasinya."),
  summary(["Sertakan siapa, apa, kapan, di mana.", "Singkat tetapi sopan.", "Sesuaikan kesopanan dengan pembaca.", "Periksa ulang sebelum mengirim."])],
 [], [])
P = mk([
 ('Pilih pesan singkat yang paling jelas:', "Hi Rani, I'll be ten minutes late. Please start without me.", "Hi Rani, I am late because there were many things to do today.", "Hello, hello, hello! I will arrive when I can arrive there.", "Hi. I will come sometime later, but I do not know when.", 'Jelas dan lengkap.'),
 ('Pilih catatan untuk Ibu yang paling baik:', "Mom, I've gone to Dina's house. I'll be back at six.", "Mom, I am not at home now, but you can call me later.", "Mom, Dina's house is quite far from our house in town.", "Mom, I have gone out and I will tell you everything later.", 'Pesan + kapan kembali.'),
 ('Pilih pengumuman yang paling lengkap:', "The science club meets on Tuesday at 3 p.m. in Room 12.", "The science club meets after school on most days, I think.", "Everybody should come to the room on Tuesday if they can.", "Room 12 is a big room with many chairs for the club.", 'Apa, kapan, di mana.'),
 ('Pilih permintaan sopan kepada guru:', "Could you please send me the notes?", "Send me the notes as soon as you can today, please.", "Please give me your notes because I really need them.", "I want your notes now so that I can study for the test.", 'Sopan.'),
 ('Pilih permintaan untuk teman dekat:', "Can you send me the notes?", "Would you be so kind as to consider sending the notes to me?", "I would be most grateful if you could kindly send me notes.", "Notes, please! Send them to me as fast as you can!", 'Santai dan sopan.'),
 ('Pilih pesan resmi yang baik:', "Dear Ms. Sari, I am writing to ask about the exam date. Thank you.", "Hey Sari, what is the exam date? Reply quickly because I need it.", "Hello, please tell me the date of the exam when you can.", "Dear Sari, exam date? I need to know right now, thanks.", 'Resmi.'),
 ('Pilih penutup pesan resmi yang baik:', "Thank you for your help.", "See you later, and have a very good evening tonight.", "Bye bye! I will talk to you again next time, OK?", "Whatever you decide is fine, I do not mind at all.", 'Sopan.'),
 ('Pilih pengumuman yang menyebut tanggal dan waktu:', "The school fair will be held on Saturday, 12 May, from 9 a.m. to 3 p.m.", "The school fair is going to be a lot of fun for everyone.", "Please come to the fair if you have time to visit us.", "The school fair is big and there will be many things there.", 'Kapan.'),
 ('Pilih pesan yang paling sopan kepada atasan:', "Could I ask for a day off next Friday, please?", "I need next Friday off because I have other plans to do.", "I will not come next Friday, so please do not expect me.", "Please give me next Friday as a day off for my plans.", 'Sopan.'),
 ('Pilih pesan yang terlalu informal untuk atasan:', "Hey boss, gotta leave early lol.", "Dear Mr. Adi, may I leave early?", "Could I leave early?", "I would like to ask for permission to leave early.", 'Terlalu santai.'),
 ('Apa informasi paling penting dalam pengumuman?', 'apa, kapan, di mana', 'warna kertas dan ukuran huruf pengumuman', 'nama penulis dan tanggal penulisan saja', 'panjang kalimat dan jumlah kata kunci', 'Inti.'),
 ('Apa yang perlu dihindari dalam pesan singkat?', 'informasi yang tidak lengkap', 'kalimat pendek yang jelas dan langsung', 'nada sopan yang sesuai dengan pembaca', 'salam singkat di awal pesan', 'Lengkap.'),
])
P += mkf([
 ('Aku akan terlambat sepuluh menit.', "I'll be ten minutes ___.", 'late', 'Late.'),
 ('Klub bertemu hari Selasa.', 'The club meets ___ Tuesday.', 'on', 'On + hari.'),
 ('Boleh minta cuti hari Jumat?', '___ I ask for a day off on Friday, please?', 'Could', 'Could I ask.'),
 ('Terima kasih atas bantuanmu.', 'Thank you ___ your help.', 'for', 'Thank you for.'),
])
P += [seq(["Dear Mr. Adi,", "I am writing to ask about the English course.", "Could you please send me the schedule and the fee?", "I look forward to hearing from you.", "Yours sincerely, Budi Santoso"], "Salam, tujuan, permintaan, penutup, tanda tangan.", q="Susun bagian pesan resmi berikut dengan urutan yang benar."),
      seq(["Hi everyone,", "The meeting tomorrow is moved to Thursday.", "It will start at ten in Room 3.", "Please let me know if you cannot come.", "Thanks, Rani"], "Salam, perubahan, detail, permintaan, penutup.", q="Susun pesan berikut dengan urutan yang benar.")]
Q = P[:8]
UNIT["practice"] = P
UNIT["quiz"] = Q
