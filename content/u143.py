from ub import *
from ielts_h import rstory
UNIT = vocab_unit("u143",
 ["membaca **cerita pendek sehari-hari** (6 sampai 8 kalimat)",
  "memahami **urutan kegiatan** dalam cerita",
  "mengenali kata **keluarga, sekolah, dan makanan**",
  "menjawab pertanyaan detail dan gagasan utama"],
 "Tahap 2: cerita tentang keluarga, sekolah, dan teman. Perhatikan siapa melakukan apa dan kapan.",
 [("Kata-kata cerita tahap 2", [
   ("morning", "pagi", "Every morning I walk to school."), ("breakfast", "sarapan", "We eat breakfast together."), ("school", "sekolah", "My school is near my house."),
   ("lesson", "pelajaran", "The English lesson is fun."), ("homework", "pekerjaan rumah", "I do my homework after dinner."), ("teacher", "guru", "The teacher is kind."),
   ("brother", "saudara laki-laki", "My brother plays football."), ("sister", "saudara perempuan", "My sister likes drawing."), ("kitchen", "dapur", "Mother cooks in the kitchen."),
   ("birthday", "ulang tahun", "Today is my birthday."), ("cake", "kue", "Mother made a chocolate cake."), ("evening", "malam / sore", "In the evening we watch TV.")])],
 "Dialog: Sarapan",
 [("Mother", "Breakfast is ready!", "Sarapan sudah siap!"), ("Dina", "What do we have today?", "Kita makan apa hari ini?"), ("Mother", "Rice and eggs. Eat quickly, or you will be late.", "Nasi dan telur. Makanlah cepat, atau kamu terlambat."), ("Dina", "OK, Mom. Thank you!", "Baik, Bu. Terima kasih!")],
 "Saat membaca, tandai kata kerja yang menunjukkan urutan kegiatan (get up, eat, walk, do).", seed=143)
READ = [
 rstory("My Morning", "Tahap 2", "I get up at six o'clock every morning. I take a shower and put on my uniform. Then I eat breakfast with my family. My mother makes rice and eggs. After breakfast, I walk to school with my sister. Our school is near our house.",
  "Aku bangun pukul enam setiap pagi. Aku mandi dan memakai seragam. Lalu aku sarapan bersama keluargaku. Ibuku membuat nasi dan telur. Setelah sarapan, aku berjalan ke sekolah bersama kakak perempuanku. Sekolah kami dekat rumah.",
  [("What time does the writer get up?", "At six o'clock", "At seven o'clock", "At five o'clock", "At eight o'clock", "Pukul enam."), ("What does the writer eat for breakfast?", "Rice and eggs", "Bread and milk", "Noodles", "Cake", "Nasi dan telur."), ("Who walks to school with the writer?", "The sister", "The brother", "The mother", "A friend", "Dengan kakak perempuan.")], [],
  [("Aku mandi.", "I take a ___.", "shower", "Take a shower."), ("Sekolah dekat rumah.", "Our school is ___ our house.", "near", "Near our house.")]),
 rstory("Dina's Birthday", "Tahap 2", "Today is Dina's birthday. She is thirteen years old. Her mother made a big chocolate cake. In the evening, her friends came to her house. They sang a birthday song and gave her presents. Dina was very happy.",
  "Hari ini ulang tahun Dina. Dia berumur tiga belas tahun. Ibunya membuat kue cokelat besar. Pada sore hari, teman-temannya datang ke rumahnya. Mereka menyanyikan lagu ulang tahun dan memberinya hadiah. Dina sangat senang.",
  [("How old is Dina?", "Thirteen", "Twelve", "Fourteen", "Fifteen", "Tiga belas."), ("Who made the cake?", "Her mother", "Her sister", "Her friend", "Her teacher", "Ibunya."), ("What did the friends do?", "Sang a song and gave presents", "Played football", "Cooked dinner", "Watched a film", "Menyanyi dan memberi hadiah.")], [],
  [("Ibunya membuat kue.", "Her mother made a ___.", "cake", "A chocolate cake."), ("Dina sangat senang.", "Dina was very ___.", "happy", "Very happy.")]),
 rstory("Homework Time", "Tahap 2", "After dinner, Budi does his homework in the kitchen. He has English and maths homework today. The English exercise is easy, but the maths exercise is difficult. His brother helps him. Then Budi checks his bag and goes to bed at nine.",
  "Setelah makan malam, Budi mengerjakan PR di dapur. Hari ini dia punya PR bahasa Inggris dan matematika. Latihan bahasa Inggris mudah, tetapi latihan matematika sulit. Kakaknya membantunya. Lalu Budi memeriksa tasnya dan tidur pukul sembilan.",
  [("Where does Budi do his homework?", "In the kitchen", "In his room", "At school", "In the library", "Di dapur."), ("Which homework is difficult?", "Maths", "English", "Science", "Art", "Matematika sulit."), ("When does Budi go to bed?", "At nine", "At eight", "At ten", "At seven", "Pukul sembilan.")], [],
  [("Latihan matematika sulit.", "The maths exercise is ___.", "difficult", "Difficult."), ("Kakaknya membantunya.", "His brother ___ him.", "helps", "Helps him.")]),
]
