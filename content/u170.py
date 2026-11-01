from ub import *
UNIT = mkunit("u170",
 ["menulis **cerita pendek** dengan awal, masalah, dan akhir",
  "memakai **past simple dan past continuous** dalam cerita",
  "memakai **penanda waktu** (one day, suddenly, finally)",
  "menyusun **alur** dan **dialog sederhana**"],
 [intro("Cerita yang baik punya tiga bagian: **awal** (tokoh dan tempat), **masalah** (apa yang terjadi), dan **akhir** (bagaimana selesai). Gunakan kalimat lampau dan penanda waktu agar alurnya jelas."),
  gram("1. Struktur cerita",
   table=[["Bagian", "Isi", "Contoh"],
          ["Awal (orientation)", "tokoh, tempat, waktu", "[[One sunny morning, a boy named Budi walked to school.]]"],
          ["Masalah (complication)", "peristiwa yang mengganggu", "[[Suddenly, he saw a small kitten stuck in a tree.]]"],
          ["Penyelesaian (resolution)", "bagaimana masalah selesai", "[[Budi climbed carefully and saved the kitten.]]"],
          ["Penutup", "perasaan atau pelajaran", "[[He felt proud, and he arrived at school smiling.]]"]]),
  gram("2. Penanda waktu dan tense",
   table=[["Penanda", "Contoh"],
          ["One day / One morning", "[[One day, I found a wallet.]]"],
          ["Suddenly", "[[Suddenly, the lights went out.]]"],
          ["While + past continuous", "[[While I was walking, it began to rain.]]"],
          ["Then / After that", "[[Then she opened the door.]]"],
          ["Finally / In the end", "[[In the end, they found the way home.]]"]]),
  gram("3. Dialog dalam cerita",
   table=[["Pola", "Contoh"],
          ["Tanda kutip + said", "[[\"I'm hungry,\" said Tom.]]"],
          ["said + tanda kutip", "[[Tom said, \"I'm hungry.\"]]"]]),
  tip("Mulai dengan kejadian", text="Pembuka seperti *Suddenly, ...* atau *One night, ...* menarik pembaca lebih cepat daripada *This is a story about ...*."),
  summary(["Awal, masalah, penyelesaian, penutup.", "Past simple untuk peristiwa, past continuous untuk latar.", "Penanda: one day, suddenly, then, finally.", "Dialog: tanda kutip dan said."])],
 [], [])
stories = [
 (["One sunny morning, Budi walked to school.", "Suddenly, he saw a small kitten stuck in a tree.", "He put his bag down and climbed carefully.", "Finally, he saved the kitten and carried it home.", "He felt proud and arrived at school smiling."], "Awal, masalah, tindakan, penyelesaian, perasaan."),
 (["Last Saturday, Dina went to the market with her mother.", "While they were shopping, it began to rain heavily.", "They ran into a small cafe and ordered hot tea.", "After an hour, the rain stopped.", "They walked home under a bright rainbow."], "Latar, kejadian, tindakan, waktu, penutup."),
 (["Tom was reading in his room one evening.", "Suddenly, all the lights went out.", "He found a torch and went to the kitchen.", "There he saw that his sister had unplugged the fridge.", "They both laughed and plugged it back in."], "Latar, masalah, tindakan, penemuan, penyelesaian."),
 (["Rani lost her notebook on the bus.", "She felt worried because it had all her notes.", "She went to the bus office the next morning.", "A kind driver had kept the notebook for her.", "Rani thanked him and promised to be more careful."], "Masalah, perasaan, tindakan, penyelesaian, pelajaran."),
 (["It was the first day of school.", "Ali felt nervous and could not find his classroom.", "A friendly girl showed him the way.", "They sat together and became good friends.", "Ali learned that new places are not so scary."], "Awal, masalah, bantuan, hasil, pelajaran."),
 (["One night, a strange noise woke me up.", "I held my breath and walked slowly to the kitchen.", "A cat was sitting on the table, eating my fish.", "I laughed and let it finish its meal.", "Then I went back to bed."], "Misteri, tindakan, penemuan, reaksi, penutup."),
]
P = [seq(s, e, q="Susun kalimat-kalimat berikut menjadi cerita yang runtut.") for s, e in stories]
P += mk([
 ('Pilih pembuka cerita yang paling menarik:', 'Suddenly, the door opened by itself.', 'This is a story about a door.', 'I will tell you something now.', 'There is a door in my house.', 'Pembuka dengan kejadian.'),
 ('Pilih kalimat penyelesaian yang baik:', 'In the end, they found the way home.', 'The end is here now.', 'They are lost.', 'It was a day.', 'Menyelesaikan masalah.'),
 ('Pilih tense yang tepat: "While I ___ home, it began to rain."', 'was walking', 'walk', 'will walk', 'have walked', 'Past continuous.'),
 ('Pilih tense yang tepat: "Suddenly, the lights ___ out."', 'went', 'go', 'are going', 'gone', 'Past simple.'),
 ('Pilih kalimat dialog yang benar:', '"I\'m hungry," said Tom.', '"I\'m hungry" Tom said.', 'I\'m hungry, said Tom.', '"I\'m hungry, said Tom.', 'Tanda kutip dan koma.'),
 ('Pilih penanda waktu yang tepat untuk peristiwa tiba-tiba:', 'Suddenly', 'Finally', 'Usually', 'Always', 'Suddenly.'),
 ('Pilih penanda waktu yang tepat untuk akhir cerita:', 'In the end', 'At first', 'Suddenly', 'Once', 'In the end.'),
 ('Bagian "complication" berisi...', 'masalah atau peristiwa yang mengganggu', 'perkenalan tokoh', 'pelajaran', 'judul', 'Masalah.'),
 ('Bagian "orientation" berisi...', 'tokoh, tempat, dan waktu', 'masalah', 'penyelesaian', 'dialog', 'Orientasi.'),
 ('Pilih kalimat yang SALAH:', 'Yesterday I go to the market.', 'Yesterday I went to the market.', 'Last week she visited her aunt.', 'They were happy.', 'Yesterday → went.'),
])
P += mkf([
 ('Tiba-tiba lampu padam.', '___, the lights went out.', 'Suddenly', 'Suddenly.'),
 ('Saat aku berjalan, hujan turun.', 'While I ___ walking, it began to rain.', 'was', 'While + was walking.'),
 ('Akhirnya, mereka menemukan jalan pulang.', '___, they found the way home.', 'Finally', 'Finally.'),
 ('Dia berkata, "Aku lapar."', 'He ___, "I am hungry."', 'said', 'Said.'),
])
Q = P[:8]
UNIT["practice"] = P
UNIT["quiz"] = Q
