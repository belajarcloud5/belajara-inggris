from ub import *
UNIT = vocab_unit("u127",
 ["meminta **pertolongan** dengan kalimat jelas dan singkat",
  "menyebut **gejala sakit** dan alergi kepada dokter atau apoteker",
  "melapor **kehilangan barang** kepada polisi",
  "mengenali **kata darurat**: emergency, ambulance, police"],
 "Dalam keadaan darurat, kalimat pendek dan jelas jauh lebih penting daripada tata bahasa sempurna. Hafalkan kata-kata berikut dan pola **I need ...**, **I have lost ...**, **My ... hurts.**",
 [("Darurat", [
   ("emergency", "keadaan darurat", "This is an emergency!"), ("ambulance", "ambulans", "Please call an ambulance."), ("police", "polisi", "I need to call the police."),
   ("fire", "kebakaran", "There is a fire in the building!"), ("help", "bantuan / menolong", "Help! I need help!"), ("accident", "kecelakaan", "There was a car accident."),
   ("hurry", "cepat / bergegas", "Please hurry!"), ("safe", "aman", "Are you safe?")]),
  ("Kesehatan", [
   ("pharmacy", "apotek", "Where is the nearest pharmacy?"), ("prescription", "resep dokter", "I need a prescription for this medicine."), ("allergy", "alergi", "I have an allergy to penicillin."),
   ("fever", "demam", "I have a high fever."), ("headache", "sakit kepala", "I have a bad headache."), ("stomachache", "sakit perut", "I have a stomachache."),
   ("insurance", "asuransi", "Do you accept my travel insurance?"), ("clinic", "klinik", "Is there a clinic near here?")]),
  ("Kehilangan dan polisi", [
   ("stolen", "dicuri", "My wallet was stolen."), ("lost", "hilang", "I have lost my passport."), ("report", "melaporkan", "I want to report a theft."),
   ("wallet", "dompet", "Someone took my wallet."), ("embassy", "kedutaan besar", "I must contact my embassy."), ("police report", "laporan polisi", "I need a police report for my insurance."),
   ("lost and found", "kantor barang hilang", "Check the lost and found."), ("contact", "menghubungi", "Please contact my family.")])],
 "Dialog: Kehilangan dompet",
 [("Budi", "Excuse me, I need help. My wallet was stolen.", "Permisi, saya butuh bantuan. Dompet saya dicuri."), ("Officer", "When did this happen?", "Kapan hal ini terjadi?"),
  ("Budi", "About an hour ago, near the station.", "Sekitar satu jam lalu, dekat stasiun."), ("Officer", "What was in the wallet?", "Apa isi dompetnya?"),
  ("Budi", "My cards and some cash. I also need a police report for my insurance.", "Kartu dan uang tunai. Saya juga butuh laporan polisi untuk asuransi."), ("Officer", "Of course. Please fill in this form.", "Tentu. Silakan isi formulir ini.")],
 "Simpan nomor darurat setempat dan fotokopi paspor di ponselmu. Latih kalimat: *I need help.* *Please call an ambulance.* *I have lost my passport.*", seed=127)
UNIT["practice"] += mkr([
 ("Seseorang jatuh di jalan.", "Operator: Emergency services. What is your emergency?", "Katakan ada kecelakaan dan butuh ambulans.", "There has been an accident. Please send an ambulance. // I need an ambulance, please. // There is an accident. Please hurry.", "accident,ambulance"),
 ("Kamu menghubungi polisi.", "Operator: What is your location?", "Katakan kamu di depan stasiun.", "I am in front of the station. // I am at the station. // Near the station.", "station"),
 ("Dompetmu dicuri.", "Officer: How can I help you?", "Laporkan dompetmu dicuri.", "My wallet was stolen. // Someone stole my wallet. // I want to report a theft.", "stolen,stole,wallet,theft,report"),
 ("Paspormu hilang.", "Officer: What is the problem?", "Katakan paspormu hilang.", "I have lost my passport. // I lost my passport. // My passport is missing.", "lost,passport,missing"),
 ("Di apotek.", "Pharmacist: Can I help you?", "Katakan kamu sakit kepala dan minta obat.", "I have a headache. Do you have any medicine? // I have a bad headache. Could I have something for it? // I need some medicine for a headache.", "headache,medicine,something"),
 ("Dokter menanyakan alergi.", "Doctor: Do you have any allergies?", "Katakan kamu alergi penisilin.", "Yes, I am allergic to penicillin. // Yes. I have an allergy to penicillin. // Yes, penicillin.", "allergic,allergy,penicillin"),
 ("Dokter menanyakan keluhan.", "Doctor: What seems to be the problem?", "Katakan perutmu sakit sejak kemarin.", "I have a stomachache since yesterday. // My stomach has hurt since yesterday. // My stomach hurts. It started yesterday.", "stomach,yesterday"),
 ("Kamu membutuhkan bantuan.", "Passer-by: Are you OK?", "Minta tolong.", "No, I need help. // I need help, please. // Please help me.", "help"),
])
