from ub import *
UNIT = vocab_unit("u105",
 ["mempelajari **anggota tubuh** dan **keluhan sakit**",
  "menjelaskan **gejala** kepada dokter dalam bahasa Inggris",
  "mengenali kata melalui **arti, ejaan, dan pendengaran**",
  "memakai pola *I have a ...* dan *My ... hurts*"],
 "Saat sakit atau di dokter, kamu perlu menyebut bagian tubuh dan keluhan. Pelajari kata-kata berikut dan polanya: **I have a headache**, **My stomach hurts**, **I feel dizzy**.",
 [("Bagian tubuh", [
   ("head", "kepala", "My head hurts."), ("shoulder", "bahu", "She carries a bag on her shoulder."), ("elbow", "siku", "He hit his elbow on the table."),
   ("knee", "lutut", "My knee hurts when I run."), ("stomach", "perut", "My stomach hurts."), ("throat", "tenggorokan", "I have a sore throat."),
   ("back", "punggung", "My back hurts after sitting all day."), ("tooth", "gigi", "I have a pain in my tooth.")]),
  ("Keluhan sakit", [
   ("headache", "sakit kepala", "I have a headache."), ("toothache", "sakit gigi", "He has a toothache."), ("fever", "demam", "She has a high fever."),
   ("cough", "batuk", "I have a bad cough."), ("cold", "pilek", "I caught a cold."), ("sore", "nyeri", "My feet are sore."),
   ("dizzy", "pusing", "I feel dizzy."), ("tired", "lelah", "I feel tired today.")]),
  ("Di dokter", [
   ("doctor", "dokter", "The doctor is kind."), ("nurse", "perawat", "The nurse took my temperature."), ("medicine", "obat", "Take this medicine twice a day."),
   ("pill", "pil / tablet", "Take one pill after dinner."), ("injection", "suntikan", "The injection did not hurt."), ("rest", "istirahat", "You need to rest."),
   ("appointment", "janji temu", "I have an appointment with the doctor."), ("pharmacy", "apotek", "Buy the medicine at the pharmacy.")])],
 "Dialog: Di dokter",
 [("Doctor", "Good morning. What is the problem?", "Selamat pagi. Apa keluhannya?"), ("Budi", "I have a fever and a bad cough.", "Saya demam dan batuk parah."),
  ("Doctor", "Do you have a sore throat?", "Apakah tenggorokan Anda sakit?"), ("Budi", "Yes, and my head hurts too.", "Ya, dan kepala saya juga sakit."),
  ("Doctor", "Take this medicine and rest for two days.", "Minum obat ini dan istirahat dua hari."), ("Budi", "Thank you, Doctor.", "Terima kasih, Dokter.")],
 "Belajar sambil menyentuh: sentuh bagian tubuhmu sambil menyebut namanya (*head, shoulder, knee*). Cara fisik ini membuat kata lebih melekat.", seed=105)
