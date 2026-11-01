from ub import *
from ielts_h import rstory
UNIT = vocab_unit("u145",
 ["membaca **teks deskriptif** tentang tempat dan tokoh",
  "mengenali **kata sifat dan preposisi tempat**",
  "memahami **detail** dan **gagasan utama**",
  "menggunakan konteks untuk menebak kata baru"],
 "Tahap 4: bacaan tentang kota, tempat wisata, dan orang. Perhatikan kata sifat (old, busy, famous) dan preposisi (near, between, behind).",
 [("Kata-kata cerita tahap 4", [
   ("village", "desa", "The village is small and quiet."), ("river", "sungai", "A river runs through the town."), ("bridge", "jembatan", "The old bridge is very famous."),
   ("market", "pasar", "The market is busy in the morning."), ("famous", "terkenal", "The cafe is famous for its coffee."), ("crowded", "ramai/penuh", "The beach is crowded on Sundays."),
   ("peaceful", "tenang", "The mountains are peaceful."), ("traditional", "tradisional", "They wear traditional clothes."), ("visitor", "pengunjung", "Every visitor loves the food."),
   ("local", "setempat", "The local people are friendly."), ("beautiful", "indah", "It is a beautiful place."), ("between", "di antara", "The school is between the bank and the park.")])],
 "Dialog: Tentang kotaku",
 [("Dina", "Where do you live, Rani?", "Kamu tinggal di mana, Rani?"), ("Rani", "In a small town near a river.", "Di kota kecil dekat sungai."), ("Dina", "Is it a busy place?", "Apakah tempat yang ramai?"), ("Rani", "Only on market days. Otherwise it is very peaceful.", "Hanya di hari pasar. Selebihnya sangat tenang.")],
 "Saat membaca teks deskriptif, buat peta sederhana: tulis nama tempat dan letaknya (near, behind, between).", seed=145)
READ = [
 rstory("A Town by the River", "Tahap 4", "Rani lives in a small town by a wide river. In the centre of the town there is an old bridge, and the market is just behind it. On Saturday mornings, the market is very crowded because farmers sell fresh fruit and fish. The rest of the week the town is peaceful. Many visitors come in the dry season to take photographs of the river at sunrise.",
  "Rani tinggal di kota kecil di tepi sungai yang lebar. Di pusat kota ada jembatan tua, dan pasar tepat di belakangnya. Pada Sabtu pagi, pasar sangat ramai karena para petani menjual buah dan ikan segar. Sepanjang sisa minggu, kota itu tenang. Banyak pengunjung datang pada musim kemarau untuk memotret sungai saat matahari terbit.",
  [("Where is the market?", "Behind the old bridge", "In front of the school", "Near the station", "Beside the river bank", "Tepat di belakang jembatan."), ("When is the market crowded?", "On Saturday mornings", "Every evening", "On Sunday afternoons", "All week", "Sabtu pagi."), ("Why do visitors come in the dry season?", "To photograph the river at sunrise", "To buy fish", "To go swimming", "To visit the school", "Memotret sungai.")], [],
  [("Pasarnya sangat ramai.", "The market is very ___.", "crowded", "Crowded."), ("Kota itu tenang.", "The rest of the week the town is ___.", "peaceful", "Peaceful.")]),
 rstory("Ms. Sari, the Teacher", "Tahap 4", "Ms. Sari is a famous English teacher in our city. She is tall, and she always wears a traditional batik blouse. Her classroom is between the library and the science lab. Students like her because she is patient and tells funny stories. After school, she helps local children with their homework for free.",
  "Bu Sari adalah guru bahasa Inggris terkenal di kota kami. Dia tinggi, dan selalu memakai blus batik tradisional. Ruang kelasnya berada di antara perpustakaan dan laboratorium sains. Murid-murid menyukainya karena dia sabar dan menceritakan kisah lucu. Sepulang sekolah, dia membantu anak-anak setempat mengerjakan PR secara gratis.",
  [("Where is her classroom?", "Between the library and the science lab", "Next to the canteen", "Behind the gym", "On the second floor", "Di antara perpustakaan dan lab."), ("Why do students like her?", "She is patient and tells funny stories", "She gives no homework", "She is very strict", "She plays music", "Sabar dan lucu."), ("What does she do after school?", "Helps local children for free", "Goes shopping", "Teaches maths", "Sleeps", "Membantu anak setempat gratis.")], [],
  [("Dia memakai blus batik tradisional.", "She wears a ___ batik blouse.", "traditional", "Traditional."), ("Dia sabar.", "She is ___.", "patient", "Patient.")]),
]
