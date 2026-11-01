from ub import *
from ielts_h import ask
UNIT = mkunit("u120",
 ["mengenali **jenis teks Part 7**: email, pengumuman, iklan, jadwal, artikel",
  "menjawab soal **tujuan, detail, NOT, inferensi, sinonim, dan maksud ucapan**",
  "memakai **scanning** untuk mencari jawaban cepat",
  "mengatur waktu untuk **54 soal Part 7**"],
 [intro("**Part 7** adalah bagian terpanjang: 54 soal dari teks tunggal dan teks ganda (misalnya email dan jadwal). Waktu terbatas, jadi kamu perlu **membaca selektif**: pahami jenis teks dan tujuannya, lalu pindai (scan) untuk mencari jawaban sesuai soal."),
  gram("1. Jenis soal Part 7",
   table=[["Jenis", "Contoh soal", "Cara menjawab"],
          ["Tujuan", "[[What is the purpose of the email?]]", "baca baris subjek dan kalimat pertama"],
          ["Detail", "[[When will the training be held?]]", "scan kata kunci dari soal"],
          ["NOT", "[[What is NOT mentioned?]]", "cek tiap opsi; tiga opsi ada di teks"],
          ["Inferensi", "[[What is suggested about Ms. Lopez?]]", "simpulkan dari fakta"],
          ["Sinonim", "[[The word 'provided' is closest in meaning to ...]]", "ganti dengan opsi dalam kalimat"],
          ["Maksud ucapan", "[[What does the writer mean by '...'?]]", "pahami konteks sekitar"],
          ["Sisip kalimat", "[[In which position does the sentence belong?]]", "ikuti kata ganti dan alur"]]),
  gram("2. Strategi membaca",
   table=[["Langkah", "Isi"],
          ["1", "Lihat jenis teks dan judul: email, iklan, jadwal, artikel?"],
          ["2", "Baca soal terlebih dulu, bukan teksnya"],
          ["3", "Scan kata kunci: nama, angka, hari, kata tanya"],
          ["4", "Untuk NOT: coret opsi yang ada di teks"],
          ["5", "Teks ganda: gabungkan informasi dari dua dokumen"]]),
  gram("3. Kata dan frasa umum",
   table=[["Kata", "Arti"],
          ["[[due to]] / [[because of]]", "karena"],
          ["[[be required to]] / [[must]]", "wajib"],
          ["[[preferred but not required]]", "diutamakan tetapi tidak wajib"],
          ["[[contact]] / [[reach]]", "menghubungi"],
          ["[[provide]] / [[offer]] / [[supply]]", "menyediakan"],
          ["[[the deadline is ...]] / [[no later than ...]]", "paling lambat"]]),
  tip("Waktu per soal", text="Part 7 memiliki 54 soal untuk sekitar 40–45 menit. Teks tunggal pendek: 1 menit per soal. Teks ganda: lebih lama. Jika sulit, lanjut dan kembali bila ada waktu."),
  summary(["Baca soal dulu, lalu scan teks.", "Jenis: tujuan, detail, NOT, inferensi, sinonim, maksud, sisip kalimat.", "NOT: tiga opsi ada di teks, satu tidak.", "Teks ganda: hubungkan dua dokumen."])],
 [], [])
A = "To: All staff. From: Maria Lopez, Human Resources. Subject: Change of training date. Dear colleagues, the customer service training scheduled for Tuesday, May 6, has been moved to Thursday, May 8, at 10 a.m. in Meeting Room B. The change is due to the trainer's flight delay. Please bring your laptop. Lunch will be provided. If you cannot attend, contact me by Monday. Best regards, Maria."
B = "GREENLEAF CAFE IS HIRING! We are looking for a part-time cook to work weekday evenings from 5 p.m. to 9 p.m. Experience is preferred but not required. Benefits include free meals and flexible hours. To apply, send your resume before June 15 or visit us at 22 Park Street."
C = "Workshop Schedule, Friday, June 20. 9:00 to 10:30, Opening talk by Dr. Chen, Main Hall. 10:45 to 12:00, Time management, Room 2. 12:00 to 1:00, Lunch, Cafeteria. 1:00 to 2:30, Writing emails, Room 3. 2:30, Closing remarks, Main Hall."
D = "City Opens New Bike Lanes. The city council announced on Monday that 20 kilometres of new bike lanes will open next month. Council member Rina Putri said the lanes aim to reduce traffic and pollution. Last year, the number of cyclists rose by 30 percent. Some shop owners are worried about losing parking spaces; however, the council says it will build new parking areas nearby."
P = ask(A, [
 ("What is the purpose of the email?", "To announce a change of date", "To invite staff to a party", "To ask for laptops", "To cancel a meeting", "Subjek: Change of training date."),
 ("Why was the training moved?", "The trainer's flight was delayed.", "The room was not available in general.", "Lunch was not ready these days.", "Many staff were absent.", "Due to the trainer's flight delay."),
 ("Where will the training be held?", "Meeting Room B", "Main Hall", "Room 2", "The cafeteria", "In Meeting Room B."),
 ("What should staff bring?", "Their laptops", "Their lunch", "A resume", "A map", "Please bring your laptop."),
 ("What is NOT mentioned in the email?", "Parking information", "The new date", "The trainer's delay", "Lunch", "Parking tidak disebut."),
 ("The word 'provided' is closest in meaning to...", "supplied", "removed", "requested", "delayed", "Provided = disediakan."),
 ("Who should staff contact if they cannot attend?", "Maria Lopez", "The trainer", "The manager", "Dr. Chen", "Contact me (Maria)."),
]) + ask(B, [
 ("What position is available?", "Part-time cook", "Full-time waiter", "Manager", "Cleaner", "Part-time cook."),
 ("When would the employee work?", "Weekday evenings", "Weekend mornings", "Every night", "Weekday mornings", "Weekday evenings 5 to 9."),
 ("What is required for the job?", "Nothing special; experience is only preferred", "Five years of experience", "A cooking diploma", "A driver's licence", "Preferred but not required."),
 ("What benefit is mentioned?", "Free meals", "Free housing", "Paid holidays", "A company car", "Free meals and flexible hours."),
 ("What is the deadline to apply?", "June 15", "June 5", "July 15", "May 15", "Before June 15."),
 ("How can applicants apply?", "Send a resume or visit the cafe", "Phone the manager only", "Fill in an online test", "Attend a workshop", "Send resume or visit."),
]) + ask(C, [
 ("When is lunch?", "12:00 to 1:00", "10:45 to 12:00", "1:00 to 2:30", "9:00 to 10:30", "Lunch 12:00–1:00."),
 ("Where is the session on time management?", "Room 2", "Main Hall", "Room 3", "Cafeteria", "Time management, Room 2."),
 ("Which session is the longest?", "Opening talk and Writing emails (1.5 hours each)", "Lunch", "Time management (1 hour 15 minutes)", "Closing remarks", "90 menit adalah terlama."),
 ("Who gives the opening talk?", "Dr. Chen", "Ms. Lopez", "The manager", "A guest chef", "Opening talk by Dr. Chen."),
 ("What happens after lunch?", "A session on writing emails", "A talk on time management", "Closing remarks", "An opening talk", "1:00 Writing emails."),
])
Q = ask(D, [
 ("What is the article mainly about?", "New bike lanes in the city", "A parking problem", "A cycling race", "A shop opening", "Judul dan kalimat pertama."),
 ("How long will the new bike lanes be?", "20 kilometres", "30 kilometres", "2 kilometres", "200 kilometres", "20 kilometres."),
 ("What concern do some shop owners have?", "Losing parking spaces", "Higher rent", "Noise", "Fewer customers online", "Worried about parking spaces."),
 ("What does the council promise?", "To build new parking areas", "To close the shops", "To reduce bike lanes", "To raise parking fees", "Build new parking areas."),
 ("What is suggested about cycling in the city?", "It has become more popular.", "It is banned.", "It is dangerous at the moment.", "It is expensive at the moment.", "Cyclists rose by 30 percent."),
 ("Who said the lanes aim to reduce traffic?", "Rina Putri", "A shop owner", "The mayor", "A cyclist", "Council member Rina Putri."),
 ("When will the lanes open?", "Next month", "Next year", "Last week", "Tomorrow", "Open next month."),
 ("The word 'aim' is closest in meaning to...", "intend", "fall", "ask", "close", "Aim to = bertujuan."),
])
P += mk([
 ('Berapa soal pada Part 7?', '54', '30', '16', '25', '54 soal.'),
 ('Apa yang sebaiknya dibaca lebih dulu pada Part 7?', 'soal', 'seluruh teks kata demi kata', 'opsi terakhir', 'tanda tangan', 'Baca soal lalu scan.'),
 ('Pada soal NOT, jawaban yang benar adalah opsi yang...', 'tidak disebut dalam teks', 'disebut dalam teks', 'terpanjang', 'pertama', 'Tiga opsi ada di teks.'),
 ('Soal "What is the purpose of the email?" paling cepat dijawab dengan membaca...', 'subjek dan kalimat pertama', 'kalimat terakhir saja', 'nama pengirim', 'semua kata', 'Tujuan di awal.'),
 ('Jenis soal yang meminta arti kata dalam konteks disebut...', 'vocabulary in context', 'NOT question', 'detail question', 'purpose question', 'Sinonim dalam konteks.'),
])
UNIT["practice"] = P
UNIT["quiz"] = Q
