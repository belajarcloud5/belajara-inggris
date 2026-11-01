from ub import *
UNIT = vocab_unit("u107",
 ["mempelajari **kendaraan** dan **tempat umum di kota**",
  "memahami kata untuk **bepergian**: ticket, platform, passenger",
  "mengenali kata melalui **arti, ejaan, dan pendengaran**",
  "memakai pola *How can I get to ...?* dan *Which bus goes to ...?*"],
 "Di kota kamu naik kendaraan, mencari tempat, dan membeli tiket. Pelajari kata berikut agar kamu mampu bertanya arah dan bepergian di negara berbahasa Inggris.",
 [("Kendaraan", [
   ("bus", "bus", "I go to school by bus."), ("train", "kereta api", "The train is late."), ("taxi", "taksi", "Let's take a taxi."),
   ("motorbike", "sepeda motor", "He rides a motorbike."), ("bicycle", "sepeda", "She rides a bicycle to work."), ("plane", "pesawat", "The plane lands at nine."),
   ("ferry", "kapal feri", "We take the ferry to the island."), ("truck", "truk", "A truck is on the road.")]),
  ("Tempat di kota", [
   ("station", "stasiun", "The station is near the market."), ("airport", "bandara", "We arrive at the airport early."), ("bridge", "jembatan", "Cross the bridge and turn left."),
   ("traffic light", "lampu lalu lintas", "Stop at the traffic light."), ("crossing", "tempat penyeberangan", "Use the crossing."), ("corner", "sudut jalan", "Wait at the corner."),
   ("square", "alun-alun", "The square is full of people."), ("market", "pasar", "My mother goes to the market.")]),
  ("Bepergian", [
   ("ticket", "tiket", "I need a ticket."), ("passenger", "penumpang", "The passenger waits at the gate."), ("driver", "pengemudi", "The driver is friendly."),
   ("platform", "peron", "The train leaves from platform two."), ("timetable", "jadwal", "Check the timetable."), ("delay", "keterlambatan", "There is a delay."),
   ("journey", "perjalanan", "It was a long journey."), ("luggage", "bagasi / bawaan", "Put your luggage here.")])],
 "Dialog: Di stasiun",
 [("Tom", "Excuse me, which platform is the train to Bandung?", "Permisi, peron mana untuk kereta ke Bandung?"), ("Ms. Sari", "Platform two. It leaves at nine.", "Peron dua. Berangkat pukul sembilan."),
  ("Tom", "Is there a delay?", "Apakah ada keterlambatan?"), ("Ms. Sari", "No, but check the timetable.", "Tidak, tetapi periksa jadwalnya."),
  ("Tom", "Thank you. Where can I buy a ticket?", "Terima kasih. Di mana saya bisa membeli tiket?"), ("Ms. Sari", "At the ticket office near the entrance.", "Di loket dekat pintu masuk.")],
 "Saat bepergian, amati papan petunjuk dan baca dalam bahasa Inggris (*platform, exit, ticket*). Papan di bandara dan stasiun penuh kosakata ini.", seed=107)
