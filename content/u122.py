from ub import *
UNIT = vocab_unit("u122",
 ["memakai **kata dan frasa bandara**: check-in, boarding pass, gate, customs",
  "menjawab **pertanyaan petugas imigrasi** dengan jelas",
  "memahami **pengumuman** di bandara",
  "meminta bantuan saat bagasi atau penerbangan bermasalah"],
 "Perjalanan ke luar negeri dimulai di bandara. Pelajari kata dan frasa penting, lalu latih menjawab petugas imigrasi dengan kalimat pendek dan jelas.",
 [("Di bandara", [
   ("check-in", "lapor masuk / daftar penerbangan", "Check-in opens three hours before the flight."), ("boarding pass", "kartu naik pesawat", "Please show your boarding pass."),
   ("gate", "pintu keberangkatan", "Your flight leaves from gate twelve."), ("departure", "keberangkatan", "The departure time is ten thirty."),
   ("arrival", "kedatangan", "The arrival hall is downstairs."), ("baggage claim", "pengambilan bagasi", "The bags are at baggage claim."),
   ("carry-on", "bagasi kabin", "I have one carry-on bag."), ("delayed", "tertunda", "The flight is delayed by one hour.")]),
  ("Imigrasi dan bea cukai", [
   ("passport", "paspor", "Please show your passport."), ("visa", "visa", "Do I need a visa?"), ("immigration", "imigrasi", "Immigration is on the left."),
   ("customs", "bea cukai", "Go through customs with your bags."), ("declare", "mendeklarasikan barang", "Do you have anything to declare?"), ("purpose of your visit", "tujuan kunjunganmu", "What is the purpose of your visit?"),
   ("tourist", "turis / wisatawan", "I am a tourist."), ("return ticket", "tiket pulang", "Do you have a return ticket?")]),
  ("Pengumuman dan masalah", [
   ("final call", "panggilan terakhir", "This is the final call for flight two."), ("boarding", "naik ke pesawat", "Boarding starts at nine."), ("cancelled", "dibatalkan", "Your flight has been cancelled."),
   ("lost luggage", "bagasi hilang", "I want to report my lost luggage."), ("transfer", "transit / pindah pesawat", "I have a transfer in Singapore."), ("seat", "tempat duduk", "Can I change my seat?"),
   ("aisle", "lorong / sisi gang", "I would like an aisle seat."), ("window", "jendela", "I would like a window seat.")])],
 "Dialog: Di imigrasi",
 [("Officer", "Good morning. May I see your passport?", "Selamat pagi. Boleh saya lihat paspor Anda?"), ("Rani", "Here you are.", "Silakan."),
  ("Officer", "What is the purpose of your visit?", "Apa tujuan kunjungan Anda?"), ("Rani", "I am a tourist. I will stay for one week.", "Saya turis. Saya akan tinggal seminggu."),
  ("Officer", "Do you have a return ticket?", "Apakah Anda punya tiket pulang?"), ("Rani", "Yes, I do. Here it is.", "Ya. Ini dia.")],
 "Simulasikan perjalanan di rumah: ucapkan kalimat petugas dan jawabanmu dengan keras. Jawaban pendek lebih baik daripada kalimat panjang yang ragu.", seed=122)
UNIT["practice"] += mkr([
 ("Di imigrasi. Petugas meminta paspor.", "Officer: Good morning. May I see your passport?", "Berikan paspor dengan sopan.", "Here you are. // Sure, here is my passport. // Yes, of course. Here it is.", "here,passport;sure,course,yes"),
 ("Petugas menanyakan tujuan kunjunganmu.", "Officer: What is the purpose of your visit?", "Jawab bahwa kamu berlibur.", "I am here on holiday. // I am a tourist. // I am visiting for a holiday.", "holiday,tourist,vacation,visiting"),
 ("Petugas menanyakan lama tinggal.", "Officer: How long will you stay?", "Jawab satu minggu.", "I will stay for one week. // One week. // I am staying for a week.", "week"),
 ("Petugas menanyakan tempat menginap.", "Officer: Where will you stay?", "Jawab di sebuah hotel.", "I will stay at a hotel. // I am staying in a hotel. // At the Grand Hotel.", "hotel"),
 ("Di meja check-in. Petugas menanyakan bagasi.", "Agent: Do you have any bags to check in?", "Jawab bahwa kamu punya satu koper.", "Yes, I have one suitcase. // Just one bag. // I have one suitcase to check in.", "one,suitcase,bag"),
 ("Di meja check-in. Kamu ingin kursi dekat jendela.", "Agent: Would you like a window or an aisle seat?", "Pilih jendela.", "A window seat, please. // Window, please. // I would like a window seat.", "window"),
 ("Bagasi tidak muncul di baggage claim.", "Staff: How can I help you?", "Laporkan bahwa kopermu hilang.", "My suitcase is missing. // I cannot find my luggage. // My bag did not arrive.", "missing,lost,luggage,suitcase,bag,find"),
 ("Bea cukai menanyakan barang.", "Officer: Do you have anything to declare?", "Jawab tidak ada.", "No, nothing to declare. // No, I do not. // Nothing to declare.", "nothing,no"),
])
