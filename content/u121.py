import random
from ub import *
import u115, u116, u117, u118, u119, u120
UNIT = vocab_unit("u121",
 ["mempelajari **kosakata kantor, keuangan, dan perjalanan** yang sering muncul di TOEIC",
  "mengenali kata melalui **arti, ejaan, dan pendengaran**",
  "mengerjakan **tes mini campuran** Part 2, 3, 5, 6, dan 7",
  "menentukan bagian TOEIC yang perlu diperkuat"],
 "Kosakata bisnis muncul di semua bagian TOEIC. Pelajari tiga kelompok berikut, lalu kerjakan **tes mini** campuran di akhir latihan untuk melihat kemajuanmu.",
 [("Kantor dan SDM", [
   ("employee", "karyawan", "Each employee has a badge."), ("employer", "pemberi kerja", "The employer pays salaries."), ("colleague", "rekan kerja", "My colleague helped me."),
   ("manager", "manajer", "The manager called a meeting."), ("department", "departemen", "She works in the sales department."), ("resume", "riwayat hidup", "Send your resume to the office."),
   ("interview", "wawancara", "The interview starts at ten."), ("promotion", "kenaikan jabatan", "He got a promotion last year.")]),
  ("Keuangan dan penjualan", [
   ("budget", "anggaran", "The budget is too small."), ("invoice", "faktur / tagihan", "Please send the invoice."), ("profit", "keuntungan", "The company made a profit."),
   ("revenue", "pendapatan", "Revenue rose this year."), ("expense", "pengeluaran", "Travel is a big expense."), ("customer", "pelanggan", "The customer wants a refund."),
   ("discount", "potongan harga", "There is a discount today."), ("receipt", "struk", "Keep the receipt.")]),
  ("Perjalanan dan rapat", [
   ("schedule", "jadwal", "Check the schedule."), ("agenda", "agenda rapat", "The agenda has five items."), ("itinerary", "rencana perjalanan", "The itinerary includes two cities."),
   ("reservation", "reservasi", "I made a reservation at the hotel."), ("deadline", "tenggat", "The deadline is Friday."), ("conference", "konferensi", "The conference is in Jakarta."),
   ("delay", "keterlambatan", "There is a delay."), ("luggage", "bagasi", "Put your luggage here.")])],
 "Dialog: Di kantor",
 [("Mr. Adi", "Good morning. Do you have the invoice for the conference?", "Selamat pagi. Apakah kamu punya faktur untuk konferensi itu?"), ("Ms. Sari", "Yes, but the budget is almost finished.", "Ya, tetapi anggarannya hampir habis."),
  ("Mr. Adi", "What is the deadline for the report?", "Apa tenggat untuk laporannya?"), ("Ms. Sari", "Friday. I will send the schedule today.", "Jumat. Aku akan mengirim jadwalnya hari ini."),
  ("Mr. Adi", "Great. Please check the hotel reservation too.", "Bagus. Tolong periksa reservasi hotel juga."), ("Ms. Sari", "Of course.", "Tentu.")],
 "Buat kartu kata dengan satu kata bisnis per hari dan satu kalimat contohmu sendiri tentang pekerjaanmu. Ulangi kartu lama tiap akhir pekan.", seed=121)
rng = random.Random(121)
mini = []
mini += rng.sample([q for q in u115.UNIT["practice"] if q["type"] == "listen"], 6)
mini += rng.sample([q for q in u116.UNIT["practice"] if q["type"] == "listen"], 6)
mini += rng.sample([q for q in u117.UNIT["practice"] if q["type"] == "mcq" and q["q"].startswith("Part 5")], 8)
mini += rng.sample([q for q in u118.UNIT["practice"] if q["type"] == "mcq" and q["q"].startswith("Part 5")], 6)
mini += rng.sample([q for q in u119.UNIT["practice"] if q["q"].startswith("Part 6")], 4)
mini += rng.sample([q for q in u120.UNIT["practice"] if "Teks" in q["q"]], 6)
UNIT["practice"] += mini
UNIT["quiz"] += rng.sample([q for q in u117.UNIT["quiz"] + u118.UNIT["quiz"] if q["q"].startswith("Part 5")], 4)
