from ub import *
UNIT = mkunit("u151",
 ["menyusun **dialog** dari sapaan sampai penutup",
  "memakai petunjuk **pertanyaan dan jawaban** untuk menentukan urutan",
  "mengenali **ucapan pembuka dan penutup**",
  "menguatkan kemampuan memahami percakapan sehari-hari"],
 [intro("Dalam dialog, urutan ditentukan oleh **pertanyaan dan jawaban**, kata ganti, serta ungkapan pembuka dan penutup. Ketuk baris dialog sesuai urutan percakapan yang wajar."),
  gram("1. Petunjuk urutan dialog",
   table=[["Petunjuk", "Contoh"],
          ["Sapaan di awal", "[[Hello! / Good morning.]]"],
          ["Pertanyaan lalu jawaban", "[[Where are you from? — I'm from Bali.]]"],
          ["Kata ganti merujuk ke kalimat sebelumnya", "[[Do you like pizza? — Yes, I love it.]]"],
          ["Ucapan terima kasih setelah bantuan", "[[Here you are. — Thank you.]]"],
          ["Penutup di akhir", "[[See you! / Goodbye.]]"]],
   examples=[("[[A: Hi! B: Hello! A: How are you? B: Fine, thanks. A: See you later.]]", "A: Hai! B: Halo! A: Apa kabar? B: Baik, terima kasih. A: Sampai nanti.")]),
  tip("Cari pasangan pertanyaan–jawaban", text="Cocokkan setiap pertanyaan dengan jawabannya lebih dulu, lalu susun pasangan itu menurut alur: sapaan, topik, penutup."),
  summary(["Sapaan di awal, penutup di akhir.", "Pertanyaan diikuti jawaban.", "Kata ganti merujuk ke ujaran sebelumnya.", "Terima kasih setelah bantuan."])],
 [], [])
dl = [
 ["Hello, Rani!", "Hi, Budi! How are you?", "I'm fine, thanks. And you?", "I'm good too. See you in class!", "See you!"],
 ["Excuse me, where is the library?", "It is on the second floor.", "Is there an elevator?", "Yes, it is next to the stairs.", "Thank you very much."],
 ["What would you like to drink?", "I'd like an orange juice, please.", "Would you like some ice?", "Yes, please.", "Here you are. Enjoy!"],
 ["Good morning. Can I help you?", "Yes, I'd like to buy a notebook.", "What size do you want?", "A small one, please.", "That's two dollars."],
 ["Hello. This is Tom speaking.", "Hello, Tom. It is Dina.", "Are you free this weekend?", "Yes, I am. Why?", "Let's go to the cinema!"],
 ["What time does the film start?", "It starts at seven.", "Shall we meet at six thirty?", "Good idea. See you there.", "See you!"],
 ["Do you have a pen I can borrow?", "Sure, here you are.", "Thank you. I'll give it back soon.", "No problem."],
 ["What's the matter, Dina?", "I have a headache.", "You should rest and drink some water.", "Thanks for the advice.", "Get well soon!"],
 ["Hi, I'm new here.", "Welcome! My name is Rani.", "I'm Tom. Nice to meet you.", "Nice to meet you too. Let me show you the classroom."],
 ["Could you tell me the time, please?", "It is half past four.", "Oh, I'm late for my class!", "Run, then! Good luck!"],
 ["Would you like to join our team?", "I'd love to. What sport do you play?", "We play football on Saturdays.", "That sounds great. See you on Saturday!"],
 ["Is this seat free?", "Yes, please sit down.", "Thank you. Are you going to Bandung too?", "Yes, I am. My stop is the last one."],
 ["Hello, I'd like to book a room for two nights.", "Certainly. What date would you like to arrive?", "On Friday, the tenth.", "A double room is fifty dollars a night.", "That's fine. I'll take it."],
 ["Can you help me with my homework?", "Of course. Which subject is it?", "It's English. I don't understand this exercise.", "Let's read the question together.", "Oh, now I understand. Thank you!"],
 ["What did you do last weekend?", "I visited my grandparents.", "Did you have a good time?", "Yes, we cooked lunch together.", "That sounds lovely."],
 ["Sorry I'm late.", "That's all right. The meeting has just started.", "Thank you. What did I miss?", "Only the introduction. Please sit down."],
]
ex = ["Sapaan, kabar, jawaban, penutup.", "Bertanya lokasi, jawaban, pertanyaan lanjutan, jawaban, terima kasih.", "Pertanyaan, pesanan, tawaran, jawaban, penyerahan.", "Sapaan, permintaan, pertanyaan, jawaban, harga.", "Telepon: pembuka, sapaan, pertanyaan, jawaban, ajakan.", "Pertanyaan, jawaban, saran, setuju, penutup.", "Meminjam, memberi, terima kasih, tanggapan.", "Menanyakan masalah, keluhan, saran, terima kasih, doa.", "Perkenalan: kata awal, sambutan, nama, tindak lanjut.", "Meminta jam, jawaban, reaksi, tanggapan.", "Ajakan, tanggapan, penjelasan, kesepakatan.", "Meminta izin duduk, jawaban, obrolan, jawaban.", "Pemesanan kamar: permintaan, tanggal, jawaban, harga, keputusan.", "Meminta bantuan, persetujuan, masalah, tindakan, terima kasih.", "Menanyakan akhir pekan, jawaban, tindak lanjut, penjelasan, tanggapan.", "Maaf terlambat, tanggapan, tanya, jawaban."]
P = [seq(d, e, q="Susun baris dialog berikut menjadi percakapan yang wajar.") for d, e in zip(dl, ex)]
UNIT["practice"] = P
UNIT["quiz"] = P[8:]
