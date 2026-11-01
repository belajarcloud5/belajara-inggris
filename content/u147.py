from ub import *
from ielts_h import rstory
UNIT = vocab_unit("u147",
 ["membaca **cerita tentang pilihan dan perasaan** tokoh",
  "memahami **alasan dan akibat** keputusan",
  "mengenali **kata perasaan** (proud, disappointed, relieved)",
  "menyimpulkan **pelajaran** dari cerita"],
 "Tahap 6: cerita yang menekankan keputusan dan perasaan. Tanyakan pada dirimu: mengapa tokoh memilih itu, dan apa akibatnya?",
 [("Kata-kata cerita tahap 6", [
   ("decide", "memutuskan", "She decided to tell the truth."), ("choice", "pilihan", "It was a difficult choice."), ("proud", "bangga", "Her parents were proud of her."),
   ("disappointed", "kecewa", "He felt disappointed."), ("relieved", "lega", "She felt relieved."), ("honest", "jujur", "He was honest about the mistake."),
   ("mistake", "kesalahan", "Everyone makes a mistake."), ("apologise", "meminta maaf", "He apologised to his friend."), ("forgive", "memaafkan", "She forgave him."),
   ("worry", "khawatir", "Don't worry about the test."), ("courage", "keberanian", "It takes courage to speak up."), ("lesson", "pelajaran", "That was a good lesson.")])],
 "Dialog: Keputusan sulit",
 [("Tom", "I broke Budi's pen. Should I tell him?", "Aku mematahkan pulpen Budi. Haruskah aku memberi tahunya?"), ("Rani", "Yes. Be honest.", "Ya. Jujurlah."), ("Tom", "But he will be angry.", "Tetapi dia akan marah."), ("Rani", "Maybe. But he will respect you more.", "Mungkin. Tetapi dia akan lebih menghargaimu.")],
 "Setelah membaca, tulis satu kalimat: 'Pelajaran dari cerita ini adalah ...'. Latihan ini mengasah pemahaman.", seed=147)
READ = [
 rstory("The Lost Wallet", "Tahap 6", "On the way home, Budi found a wallet on the pavement. Inside there were two hundred thousand rupiah and an identity card. He really needed money for a new notebook, so for a moment he felt tempted. But he thought about the owner, who was probably worried. Budi decided to take the wallet to the police station. The next day, the owner, an old man, came to his school and thanked him. Budi felt proud and relieved because he had made the right choice.",
  "Dalam perjalanan pulang, Budi menemukan dompet di trotoar. Di dalamnya ada dua ratus ribu rupiah dan sebuah kartu identitas. Dia sangat butuh uang untuk buku catatan baru, jadi sesaat dia tergoda. Tetapi dia memikirkan pemiliknya, yang mungkin khawatir. Budi memutuskan membawa dompet itu ke kantor polisi. Keesokan harinya, pemiliknya, seorang pria tua, datang ke sekolahnya dan berterima kasih. Budi merasa bangga dan lega karena telah membuat pilihan yang benar.",
  [("Why was Budi tempted?", "He needed money for a notebook", "He wanted a new phone", "He was very hungry", "He wanted to buy a gift", "Butuh uang untuk buku."), ("What did Budi decide?", "To take the wallet to the police", "To keep the money", "To throw it away", "To ask his friend", "Membawa ke polisi."), ("How did he feel at the end?", "Proud and relieved", "Angry and tired", "Sad and bored", "Afraid and nervous", "Bangga dan lega.")], [],
  [("Budi memutuskan membawa dompet.", "Budi ___ to take the wallet to the police.", "decided", "Decided."), ("Dia merasa bangga.", "He felt ___.", "proud", "Proud.")]),
 rstory("A Difficult Apology", "Tahap 6", "Dina and Rani were best friends, but one day Dina shouted at Rani in front of the class. Later, she felt ashamed and worried that she had lost her friend. It took a lot of courage to speak, but Dina went to Rani's house and said, \"I'm sorry. I made a mistake.\" At first, Rani was silent. Then she smiled and forgave her. They both learned that honest words can repair a friendship.",
  "Dina dan Rani adalah sahabat, tetapi suatu hari Dina membentak Rani di depan kelas. Kemudian, dia merasa malu dan khawatir telah kehilangan sahabatnya. Dibutuhkan banyak keberanian untuk bicara, tetapi Dina pergi ke rumah Rani dan berkata, \"Maaf. Aku membuat kesalahan.\" Awalnya, Rani diam. Lalu dia tersenyum dan memaafkannya. Keduanya belajar bahwa kata-kata yang jujur dapat memperbaiki persahabatan.",
  [("What did Dina do wrong?", "She shouted at Rani in front of the class", "She forgot Rani's birthday", "She lost Rani's book", "She told a secret", "Membentak Rani."), ("What did Dina do to fix it?", "She apologised at Rani's house", "She sent a gift", "She asked the teacher to help", "She waited silently", "Meminta maaf."), ("What lesson did they learn?", "Honest words can repair a friendship", "Never argue with friends", "Teachers solve problems", "Money buys friends", "Kata jujur memperbaiki.")], [],
  [("Dibutuhkan banyak keberanian.", "It took a lot of ___.", "courage", "Courage."), ("Rani memaafkannya.", "Rani ___ her.", "forgave", "Forgave.")]),
]
