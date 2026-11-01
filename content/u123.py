from ub import *
UNIT = vocab_unit("u123",
 ["memesan dan **check-in/check-out** hotel dalam bahasa Inggris",
  "meminta **fasilitas** dan layanan dengan sopan",
  "menyampaikan **keluhan** dengan jelas",
  "memakai pola *Could I have ...?* dan *Is there ...?*"],
 "Di hotel kamu perlu memesan kamar, menanyakan fasilitas, dan menyampaikan masalah. Pakai kalimat sopan seperti **Could I have ...?** dan **Is there ...?**",
 [("Reservasi dan kamar", [
   ("reservation", "reservasi / pemesanan", "I have a reservation under the name Rani."), ("single room", "kamar untuk satu orang", "I would like a single room."), ("double room", "kamar dengan ranjang besar", "We booked a double room."),
   ("per night", "per malam", "The price is fifty dollars per night."), ("breakfast included", "termasuk sarapan", "Is breakfast included?"), ("key card", "kartu kunci", "Here is your key card."),
   ("floor", "lantai", "Your room is on the fifth floor."), ("view", "pemandangan", "I want a room with a sea view.")]),
  ("Fasilitas", [
   ("Wi-Fi", "internet nirkabel", "What is the Wi-Fi password?"), ("elevator", "lift", "The elevator is on your right."), ("swimming pool", "kolam renang", "The swimming pool opens at six."),
   ("laundry", "laundri", "Is there a laundry service?"), ("reception", "resepsionis", "Please call reception."), ("towel", "handuk", "Could I have an extra towel?"),
   ("air conditioner", "pendingin ruangan", "The air conditioner is too cold."), ("checkout time", "jam check-out", "Checkout time is at noon.")]),
  ("Masalah dan permintaan", [
   ("broken", "rusak", "The shower is broken."), ("noisy", "bising", "The room next door is noisy."), ("dirty", "kotor", "The bathroom is dirty."),
   ("wake-up call", "panggilan bangun", "I would like a wake-up call at six."), ("late checkout", "check-out lebih lambat", "Could I have a late checkout?"), ("luggage storage", "penitipan bagasi", "Can you keep my luggage in the luggage storage?"),
   ("complain", "mengeluh", "I want to complain about the noise."), ("another room", "kamar lain", "Could I have another room?")])],
 "Dialog: Check-in",
 [("Receptionist", "Good evening. Do you have a reservation?", "Selamat malam. Apakah Anda punya reservasi?"), ("Tom", "Yes, under the name Tom Baker.", "Ya, atas nama Tom Baker."),
  ("Receptionist", "A double room for three nights, correct?", "Kamar double untuk tiga malam, benar?"), ("Tom", "Yes. Is breakfast included?", "Ya. Apakah sarapan termasuk?"),
  ("Receptionist", "Yes, from seven to ten. Here is your key card.", "Ya, pukul tujuh sampai sepuluh. Ini kartu kunci Anda."), ("Tom", "Thank you. What is the Wi-Fi password?", "Terima kasih. Apa kata sandi Wi-Fi?")],
 "Hafalkan pola: *Could I have ...?* (meminta), *Is there ...?* (bertanya ada atau tidak), *The ... is broken.* (melaporkan masalah).", seed=123)
UNIT["practice"] += mkr([
 ("Di resepsionis. Kamu tiba di hotel.", "Receptionist: Good evening. Do you have a reservation?", "Jawab ya, atas namamu.", "Yes, I have a reservation. // Yes, under the name Budi. // Yes, I booked a room.", "yes,reservation,booked,name"),
 ("Kamu ingin tahu apakah sarapan termasuk.", "Receptionist: Is there anything else I can help you with?", "Tanyakan apakah sarapan termasuk.", "Is breakfast included? // Is breakfast included in the price? // Does the price include breakfast?", "breakfast"),
 ("Kamu butuh kata sandi internet.", "Receptionist: Can I help you with anything?", "Tanyakan kata sandi Wi-Fi.", "What is the Wi-Fi password? // Could I have the Wi-Fi password? // Is there Wi-Fi in the room?", "wi-fi,wifi,password"),
 ("Kamar tidak ada handuk tambahan.", "Receptionist: Reception, how can I help?", "Minta handuk tambahan.", "Could I have an extra towel? // Can you send an extra towel? // I need another towel, please.", "towel"),
 ("Pancuran di kamarmu rusak.", "Receptionist: How can I help you?", "Laporkan bahwa pancurannya rusak.", "The shower is broken. // The shower does not work. // There is a problem with the shower.", "shower,broken,problem,work"),
 ("Kamar sebelah sangat bising.", "Receptionist: How can I help you?", "Laporkan kebisingan dan minta kamar lain.", "The room next door is very noisy. // It is too noisy. Could I have another room? // I would like another room, please.", "noisy,noise,room"),
 ("Kamu ingin check-out lebih lambat.", "Receptionist: Is there anything else?", "Minta check-out lebih lambat.", "Could I have a late checkout? // Can I check out late? // Is a late checkout possible?", "late,checkout,check"),
 ("Kamu check-out dan ingin menitipkan koper.", "Receptionist: Did you enjoy your stay?", "Jawab ya dan minta menitipkan koper.", "Yes, thank you. Can I leave my luggage here? // Yes, it was great. Could you keep my bag? // Yes. May I leave my suitcase here?", "luggage,suitcase,bag"),
])
