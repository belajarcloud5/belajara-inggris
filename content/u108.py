from ub import *
UNIT = vocab_unit("u108",
 ["mempelajari **nama pekerjaan** dan **tempat kerja**",
  "menjelaskan **tugas pekerjaan** dengan kata kerja yang tepat",
  "mengenali kata melalui **arti, ejaan, dan pendengaran**",
  "memakai pola *What does she do?* dan *He works as a ... in a ...*"],
 "Menyebut pekerjaan dan tempat kerja adalah topik percakapan yang sangat umum. Pelajari kata berikut serta pola **What do you do?** dan **I work as a ... at ...**",
 [("Pekerjaan", [
   ("farmer", "petani", "The farmer grows rice."), ("nurse", "perawat", "The nurse works at a hospital."), ("driver", "pengemudi", "The driver is polite."),
   ("cook", "juru masak", "The cook makes soup."), ("mechanic", "montir", "The mechanic repairs cars."), ("engineer", "insinyur", "The engineer designs bridges."),
   ("accountant", "akuntan", "The accountant checks the numbers."), ("waiter", "pelayan", "The waiter brings the menu.")]),
  ("Tempat kerja", [
   ("office", "kantor", "She works in an office."), ("factory", "pabrik", "He works in a factory."), ("hospital", "rumah sakit", "The hospital is near my house."),
   ("restaurant", "restoran", "They eat at a restaurant."), ("shop", "toko", "She works in a shop."), ("farm", "lahan pertanian", "My uncle lives on a farm."),
   ("workshop", "bengkel", "The workshop is on this street."), ("school", "sekolah", "My mother works at a school.")]),
  ("Tugas dan kegiatan kerja", [
   ("repair", "memperbaiki", "He can repair motorbikes."), ("serve", "melayani", "She serves the customers."), ("deliver", "mengantar", "They deliver food by motorbike."),
   ("manage", "mengelola", "She manages the shop."), ("design", "merancang", "He designs houses."), ("sell", "menjual", "They sell fresh fish."),
   ("teach", "mengajar", "She teaches English."), ("build", "membangun", "They build roads.")])],
 "Dialog: Apa pekerjaanmu?",
 [("Tom", "What do you do, Budi?", "Apa pekerjaanmu, Budi?"), ("Budi", "I am a mechanic. I work in a workshop.", "Aku montir. Aku bekerja di bengkel."),
  ("Tom", "What do you do there?", "Apa yang kamu lakukan di sana?"), ("Budi", "I repair motorbikes and cars.", "Aku memperbaiki sepeda motor dan mobil."),
  ("Tom", "Do you like your job?", "Apakah kamu suka pekerjaanmu?"), ("Budi", "Yes, I love it!", "Ya, aku menyukainya!")],
 "Setiap kali bertemu seseorang bekerja (kasir, sopir, guru), sebutkan dalam hati: *She is a cashier. She works in a shop.* Latihan sederhana ini memperkuat pola kalimat.", seed=108)
