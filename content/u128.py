from ub import *
UNIT = vocab_unit("u128",
 ["berkenalan dan **berbasa-basi** dengan orang baru",
  "bertanya dan menjawab tentang **asal, pekerjaan, dan keluarga**",
  "**menerima dan menolak undangan** dengan sopan",
  "memakai ungkapan **pujian dan terima kasih**"],
 "Obrolan ringan (small talk) adalah kunci berteman dan bekerja sama. Pelajari ungkapan berikut dan pola **Where are you from?**, **What do you do?**, dan **Would you like to ...?**",
 [("Berkenalan", [
   ("nice to meet you", "senang bertemu denganmu", "Nice to meet you, I'm Rani."), ("where are you from", "kamu berasal dari mana", "Where are you from?"), ("I'm from", "aku berasal dari", "I'm from Indonesia."),
   ("what do you do", "apa pekerjaanmu", "What do you do?"), ("how long have you been", "sudah berapa lama kamu", "How long have you been in London?"), ("first time", "pertama kali", "Is this your first time here?"),
   ("visiting", "berkunjung", "I'm visiting for a week."), ("living in", "tinggal di", "I'm living in Bandung.")]),
  ("Obrolan ringan", [
   ("the weather", "cuaca", "The weather is lovely today."), ("weekend", "akhir pekan", "What are you doing this weekend?"), ("hobby", "hobi", "What is your hobby?"),
   ("favourite", "favorit", "What is your favourite food?"), ("compliment", "pujian", "She gave me a compliment."), ("lovely", "indah / menyenangkan", "What a lovely place!"),
   ("by the way", "ngomong-ngomong", "By the way, where did you learn English?"), ("really", "benarkah / sungguh", "Really? That's interesting.")]),
  ("Undangan dan terima kasih", [
   ("invite", "mengundang", "I'd like to invite you to dinner."), ("would you like to", "maukah kamu", "Would you like to join us?"), ("I'd love to", "dengan senang hati", "I'd love to come."),
   ("I'm afraid I can't", "sayangnya aku tidak bisa", "I'm afraid I can't come on Friday."), ("maybe next time", "mungkin lain kali", "Maybe next time!"), ("thank you so much", "terima kasih banyak", "Thank you so much for your help."),
   ("my pleasure", "dengan senang hati (membantu)", "It was my pleasure."), ("take care", "jaga diri", "Take care and see you soon.")])],
 "Dialog: Berkenalan",
 [("Dina", "Hi, I'm Dina. Nice to meet you.", "Hai, aku Dina. Senang bertemu denganmu."), ("Tom", "Nice to meet you, Dina. I'm Tom. Where are you from?", "Senang bertemu denganmu, Dina. Aku Tom. Kamu berasal dari mana?"),
  ("Dina", "I'm from Indonesia. What do you do?", "Aku dari Indonesia. Apa pekerjaanmu?"), ("Tom", "I'm a teacher. Would you like to join us for lunch?", "Aku guru. Maukah kamu bergabung makan siang?"),
  ("Dina", "I'd love to, thank you!", "Dengan senang hati, terima kasih!"), ("Tom", "Great. See you at twelve.", "Bagus. Sampai jumpa pukul dua belas.")],
 "Pola obrolan ringan: pertanyaan + tanggapan + pertanyaan balik. Contoh: *I'm from Bali. And you?* Pertanyaan balik membuat percakapan berlanjut.", seed=128)
UNIT["practice"] += mkr([
 ("Seseorang memperkenalkan diri.", "Tom: Hi, I'm Tom. Nice to meet you.", "Balas dengan sopan dan sebut namamu.", "Nice to meet you too. I'm Rani. // Hi Tom, nice to meet you. My name is Rani. // Nice to meet you, Tom. I'm Rani.", "nice,meet,name,i'm"),
 ("Orang baru menanyakan asalmu.", "Tom: Where are you from?", "Jawab dari Indonesia.", "I'm from Indonesia. // I come from Indonesia. // I am from Indonesia. And you?", "indonesia"),
 ("Orang baru menanyakan pekerjaanmu.", "Tom: What do you do?", "Jawab bahwa kamu seorang pelajar.", "I'm a student. // I am a student. // I study at a university.", "student,study"),
 ("Obrolan ringan tentang cuaca.", "Tom: The weather is lovely today, isn't it?", "Setujui dan tanggapi.", "Yes, it is. It's beautiful. // Yes, it's lovely. // It really is.", "yes,lovely,beautiful,is"),
 ("Kamu diundang makan malam.", "Tom: Would you like to join us for dinner on Friday?", "Terima undangan dengan senang hati.", "I'd love to, thank you. // Yes, I'd love to. // Sure, that sounds great.", "love,sure,great,yes"),
 ("Kamu tidak bisa hadir.", "Tom: Would you like to come to my party on Saturday?", "Tolak dengan sopan.", "I'm afraid I can't, but thank you. // Sorry, I can't make it. Maybe next time. // Thank you, but I'm busy that day.", "can't,cannot,sorry,busy,afraid"),
 ("Seseorang membantumu.", "Tom: Here is the map you wanted.", "Ucapkan terima kasih.", "Thank you so much. // Thanks a lot. // Thank you very much for your help.", "thank,thanks"),
 ("Seseorang memujimu.", "Tom: Your English is very good!", "Tanggapi pujian dengan rendah hati.", "Thank you, that's kind of you. // Thanks! I'm still learning. // Thank you very much.", "thank,thanks"),
])
