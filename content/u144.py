from ub import *
from ielts_h import rstory
UNIT = vocab_unit("u144",
 ["membaca **cerita masa lampau** dengan percakapan",
  "mengikuti **urutan peristiwa** (first, then, after that)",
  "memahami kata kerja **lampau teratur dan tak teratur**",
  "menjawab pertanyaan tentang tokoh dan peristiwa"],
 "Tahap 3: cerita petualangan kecil dengan kalimat lampau dan percakapan. Perhatikan kata kerja lampau (went, saw, found) dan penanda urutan.",
 [("Kata-kata cerita tahap 3", [
   ("adventure", "petualangan", "It was a small adventure."), ("forest", "hutan", "They walked into the forest."), ("path", "jalan setapak", "They followed a narrow path."),
   ("find", "menemukan", "They found an old box."), ("box", "kotak", "The box was under a tree."), ("open", "membuka", "Tom opened the box."),
   ("inside", "di dalam", "Inside there was a map."), ("afraid", "takut", "Dina was afraid."), ("brave", "berani", "Budi was brave."),
   ("return", "kembali", "They returned home before dark."), ("lost", "tersesat", "They were lost for an hour."), ("finally", "akhirnya", "Finally, they found the road.")])],
 "Dialog: Di hutan",
 [("Budi", "Look! There is an old box under the tree.", "Lihat! Ada kotak tua di bawah pohon."), ("Dina", "Let's open it.", "Ayo kita buka."), ("Tom", "I'm afraid. What is inside?", "Aku takut. Apa isinya?"), ("Budi", "Don't worry. I'm here.", "Jangan khawatir. Aku di sini.")],
 "Tulis daftar kata kerja lampau yang kamu temukan dalam cerita (went, saw, found) dan ubah ke bentuk dasarnya.", seed=144)
READ = [
 rstory("The Old Box", "Tahap 3", "Last Saturday, Tom, Dina, and Budi walked into the forest. They followed a narrow path for an hour. Then Budi saw an old box under a tree. \"Let's open it!\" he said. Inside the box, they found a map of the village. They looked at it carefully and walked home. After that, they showed the map to their teacher.",
  "Sabtu lalu, Tom, Dina, dan Budi berjalan ke hutan. Mereka mengikuti jalan setapak yang sempit selama satu jam. Lalu Budi melihat kotak tua di bawah pohon. \"Ayo kita buka!\" katanya. Di dalam kotak, mereka menemukan peta desa. Mereka melihatnya dengan teliti dan berjalan pulang. Setelah itu, mereka menunjukkan peta itu kepada guru mereka.",
  [("Where did the children go?", "Into the forest", "To the beach", "To the market", "To the river", "Ke hutan."), ("What was inside the box?", "A map of the village", "Some money", "A letter", "A key", "Peta desa."), ("Who did they show the map to?", "Their teacher", "Their parents", "A policeman", "A friend", "Kepada guru.")], [],
  [("Budi melihat kotak tua.", "Budi ___ an old box.", "saw", "Past of see = saw."), ("Mereka menemukan peta.", "They ___ a map.", "found", "Past of find = found.")]),
 rstory("Lost in the Park", "Tahap 3", "Rani went to the big park with her cousin. They played near the lake, and then they walked too far. Suddenly, they could not find the gate. Rani was afraid, but her cousin stayed calm. They asked a gardener for help. He showed them the way, and they returned to the gate before dark.",
  "Rani pergi ke taman besar bersama sepupunya. Mereka bermain dekat danau, lalu berjalan terlalu jauh. Tiba-tiba, mereka tidak bisa menemukan gerbang. Rani takut, tetapi sepupunya tetap tenang. Mereka meminta bantuan tukang kebun. Dia menunjukkan jalan, dan mereka kembali ke gerbang sebelum gelap.",
  [("Why were the girls in trouble?", "They could not find the gate", "They lost a bag", "It started to rain", "They missed a bus", "Tidak bisa menemukan gerbang."), ("Who stayed calm?", "Rani's cousin", "Rani", "The gardener", "Their mother", "Sepupunya tenang."), ("Who helped them?", "A gardener", "A policeman", "A teacher", "A driver", "Tukang kebun.")], [],
  [("Mereka berjalan terlalu jauh.", "They walked too ___.", "far", "Too far."), ("Rani takut.", "Rani was ___.", "afraid", "Afraid.")]),
 rstory("The Brave Boy", "Tahap 3", "One evening, a small kitten fell into a deep hole near Budi's house. It cried for help. Budi was not afraid. He took a long rope and climbed down carefully. He tied the rope around the kitten and pulled it up. The kitten was safe, and Budi's neighbours clapped for him.",
  "Suatu malam, seekor anak kucing jatuh ke lubang dalam di dekat rumah Budi. Kucing itu mengeong minta tolong. Budi tidak takut. Dia mengambil tali panjang dan turun dengan hati-hati. Dia mengikat tali di tubuh anak kucing itu dan menariknya ke atas. Anak kucing itu selamat, dan para tetangga bertepuk tangan untuk Budi.",
  [("What happened to the kitten?", "It fell into a hole", "It ran away", "It was sick", "It got lost", "Jatuh ke lubang."), ("What did Budi use?", "A long rope", "A ladder", "A stick", "A net", "Tali panjang."), ("What did the neighbours do?", "They clapped", "They laughed", "They called the police", "They went home", "Bertepuk tangan.")], [],
  [("Budi tidak takut.", "Budi was not ___.", "afraid", "Not afraid."), ("Dia menarik anak kucing ke atas.", "He ___ it up.", "pulled", "Pulled it up.")]),
]
