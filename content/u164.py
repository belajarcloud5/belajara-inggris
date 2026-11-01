from ub import *
UNIT = vocab_unit("u164",
 ["memahami **phrasal verb menengah** untuk kerja dan belajar",
  "memakai phrasal verb dalam kalimat dengan **objek di tengah atau di belakang**",
  "mengenali **arti yang berbeda** dari kata kerja dasarnya",
  "membedakan phrasal verb yang **dapat dan tidak dapat dipisah**"],
 "Phrasal verb dasar sudah kamu pelajari di Kelas 7. Kini kita masuk ke phrasal verb menengah yang sering muncul di kantor dan kampus. Perhatikan: sebagian dapat dipisah (*look it up*), sebagian tidak (*look after children*).",
 [("Belajar dan penelitian", [
   ("look up", "mencari informasi", "Please look up the word in a dictionary."), ("find out", "mencari tahu", "I need to find out the answer."), ("carry out", "melaksanakan", "Scientists carry out experiments."),
   ("catch up", "mengejar ketertinggalan", "I must catch up on my homework."), ("hand in", "mengumpulkan", "Hand in your essay on Friday."), ("go over", "mengulas", "Let's go over the lesson again."),
   ("sum up", "meringkas", "Can you sum up the story?"), ("point out", "menunjukkan", "The teacher pointed out my mistake.")]),
  ("Pekerjaan dan proyek", [
   ("set up", "mendirikan / menyiapkan", "They set up a new company."), ("take on", "mengambil (tugas)", "She took on extra work."), ("deal with", "menangani", "We deal with customers every day."),
   ("work out", "menyelesaikan / menghitung", "I cannot work out the answer."), ("put off", "menunda", "They put off the meeting until Monday."), ("turn down", "menolak", "He turned down the job offer."),
   ("back up", "mencadangkan / mendukung", "Please back up your files."), ("fill in", "mengisi", "Fill in this form, please.")]),
  ("Komunikasi dan rencana", [
   ("get back to", "menghubungi kembali", "I'll get back to you tomorrow."), ("bring up", "mengemukakan", "He brought up a good point."), ("follow up", "menindaklanjuti", "I will follow up with the client."),
   ("run into", "bertemu tak sengaja", "I ran into my old teacher."), ("come up with", "menemukan (ide)", "She came up with a clever plan."), ("figure out", "memahami / memecahkan", "We figured out the problem."),
   ("look into", "menyelidiki", "The manager will look into the matter."), ("sign up", "mendaftar", "Sign up for the course online.")])],
 "Dialog: Mengejar tugas",
 [("Tom", "Did you hand in the report?", "Apakah kamu sudah mengumpulkan laporan?"), ("Dina", "Not yet. I need to catch up on the data first.", "Belum. Aku perlu mengejar data dulu."),
  ("Tom", "Can I help you work it out?", "Bolehkah aku membantumu menyelesaikannya?"), ("Dina", "Yes, please. Then I'll follow up with Mr. Adi.", "Ya, tolong. Lalu aku akan menindaklanjuti dengan Pak Adi.")],
 "Pecah phrasal verb menjadi dua bagian dan buat satu kalimat sendiri untuk setiap pasangan. Kata ganti selalu di tengah pada phrasal verb yang dapat dipisah: *look it up*, bukan *look up it*.", seed=164)
UNIT["practice"] += mk([
 ('Pilih kalimat yang benar:', 'Please hand it in tomorrow.', 'Please hand in it tomorrow.', 'Please hand to in it tomorrow.', 'Please in hand it tomorrow.', 'Kata ganti di tengah.'),
 ('Pilih kalimat yang benar:', 'I will look it up.', 'I will look up it.', 'I will look it for.', 'I will up look it.', 'Kata ganti di tengah.'),
 ('Pilih kalimat yang benar:', 'We need to deal with this problem.', 'We need to deal this problem with.', 'We need to deal on this problem.', 'We need to dealt with this problem.', 'Deal with tidak dipisah.'),
 ('Pilih kalimat yang benar:', 'She came up with a great idea.', 'She came with up a great idea.', 'She came up a great idea with.', 'She up came with a great idea.', 'Come up with tiga kata, tidak dipisah.'),
 ('Pilih kalimat yang SALAH:', 'He turned down it.', 'He turned it down.', 'He turned down the offer.', 'He turned the offer down.', 'Kata ganti harus di tengah.'),
 ('Pilih kalimat yang SALAH:', 'We looked into it the matter.', 'We looked into the matter.', 'We looked into it.', 'They looked into the problem.', 'Look into tidak dipisah.'),
])
