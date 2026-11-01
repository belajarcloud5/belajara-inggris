from ub import *
UNIT = vocab_unit("u125",
 ["membeli **tiket** dan memilih transportasi",
  "bertanya **arah dan jalur** dalam bahasa Inggris",
  "memahami kata **stasiun dan halte**: platform, transfer, fare",
  "memakai pola *How do I get to ...?* dan *Which bus goes to ...?*"],
 "Di kota asing kamu perlu naik taksi, bus, atau kereta dan bertanya arah. Pelajari kata penting dan pola **How do I get to ...?** serta **Which platform ...?**",
 [("Transportasi", [
   ("taxi", "taksi", "Can you call a taxi for me?"), ("bus stop", "halte bus", "The bus stop is near the corner."), ("subway", "kereta bawah tanah", "Take the subway to the airport."),
   ("ticket machine", "mesin tiket", "Buy a ticket at the ticket machine."), ("one-way ticket", "tiket sekali jalan", "One one-way ticket to the city, please."), ("return ticket", "tiket pulang pergi", "A return ticket, please."),
   ("fare", "ongkos", "What is the fare to the airport?"), ("timetable", "jadwal", "Check the timetable at the station.")]),
  ("Di stasiun dan di jalan", [
   ("platform", "peron", "The train leaves from platform four."), ("transfer", "pindah jalur", "You need to transfer at Central Station."), ("exit", "pintu keluar", "Take exit two."),
   ("traffic jam", "kemacetan", "We are stuck in a traffic jam."), ("crossing", "tempat penyeberangan", "Use the crossing."), ("one-way street", "jalan satu arah", "This is a one-way street."),
   ("map", "peta", "Do you have a map?"), ("lost", "tersesat", "Excuse me, I am lost.")]),
  ("Menanyakan arah", [
   ("straight ahead", "lurus ke depan", "Go straight ahead for two blocks."), ("turn left", "belok kiri", "Turn left at the traffic light."), ("turn right", "belok kanan", "Turn right after the bank."),
   ("on your left", "di sebelah kirimu", "The station is on your left."), ("opposite", "di seberang", "The cafe is opposite the museum."), ("next to", "di sebelah", "The pharmacy is next to the bank."),
   ("block", "blok jalan", "It is two blocks from here."), ("walking distance", "bisa ditempuh jalan kaki", "The hotel is within walking distance.")])],
 "Dialog: Bertanya arah",
 [("Tom", "Excuse me, how do I get to the museum?", "Permisi, bagaimana cara ke museum?"), ("Ms. Sari", "Go straight ahead and turn left at the traffic light.", "Lurus saja lalu belok kiri di lampu lalu lintas."),
  ("Tom", "Is it far?", "Apakah jauh?"), ("Ms. Sari", "No, it is within walking distance. It is next to the bank.", "Tidak, bisa jalan kaki. Letaknya di sebelah bank."),
  ("Tom", "Thank you very much.", "Terima kasih banyak."), ("Ms. Sari", "You're welcome.", "Sama-sama.")],
 "Saat bertanya arah, ulangi arahan yang kamu dengar (*Turn left at the light, right?*) untuk memastikan kamu paham.", seed=125)
UNIT["practice"] += mkr([
 ("Kamu tersesat dan butuh bantuan.", "Passer-by: Can I help you?", "Katakan kamu tersesat dan tanyakan jalan ke stasiun.", "Yes, I am lost. How do I get to the station? // Yes, please. Where is the station? // I'm lost. Can you tell me the way to the station?", "lost,station,way,get"),
 ("Kamu membeli tiket di loket.", "Clerk: Where to?", "Beli satu tiket sekali jalan ke pusat kota.", "One one-way ticket to the city centre, please. // A single ticket to the city, please. // One ticket to the city centre.", "ticket,city"),
 ("Kamu ingin tiket pulang pergi.", "Clerk: Would you like a single or a return?", "Pilih pulang pergi.", "A return ticket, please. // Return, please. // I'd like a return ticket.", "return"),
 ("Kamu menanyakan peron.", "Clerk: Your train is at ten.", "Tanyakan peron mana.", "Which platform is it? // Which platform does the train leave from? // What platform, please?", "platform"),
 ("Kamu ingin tahu lama perjalanan.", "Clerk: The bus goes to the airport.", "Tanyakan berapa lama perjalanan.", "How long does it take? // How long is the journey? // How many minutes does it take?", "long,take,journey"),
 ("Naik taksi.", "Driver: Where to?", "Minta diantar ke Hotel Grand.", "To the Grand Hotel, please. // Grand Hotel, please. // Please take me to the Grand Hotel.", "hotel,grand"),
 ("Kamu menanyakan ongkos taksi.", "Driver: It is about twenty minutes to the airport.", "Tanyakan berapa ongkosnya.", "How much is the fare? // How much will it cost? // What is the fare to the airport?", "much,fare,cost"),
 ("Kamu menanyakan halte bus.", "Passer-by: Yes?", "Tanyakan di mana halte bus terdekat.", "Excuse me, where is the nearest bus stop? // Where can I find the bus stop? // Is there a bus stop near here?", "bus,stop"),
])
