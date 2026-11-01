from ub import *
UNIT = mkunit("u150",
 ["menyusun kalimat menjadi **paragraf yang runtut**",
  "memakai **penanda urutan** (first, then, finally) dan **kata ganti** sebagai petunjuk",
  "menemukan **kalimat topik** dan **kalimat penutup**",
  "membaca teks prosedur, cerita, dan deskripsi dengan alur jelas"],
 [intro("Paragraf yang baik bukan sekadar kumpulan kalimat; kalimatnya **berurutan** dan saling menyambung. Pada latihan ini kamu mengetuk kalimat satu per satu sesuai urutan yang benar. Gunakan petunjuk di dalam kalimat untuk menebak urutannya."),
  gram("1. Petunjuk untuk menyusun urutan",
   table=[["Petunjuk", "Contoh", "Biasanya"],
          ["Penanda urutan", "[[First]], [[Next]], [[Then]], [[After that]], [[Finally]]", "First di awal, Finally di akhir"],
          ["Kata ganti", "[[She]], [[It]], [[They]], [[This]]", "kata ganti muncul setelah nama atau benda disebut"],
          ["Kalimat topik", "[[I had a busy morning.]]", "gagasan umum di awal"],
          ["Kalimat penutup", "[[That is why ...]] / [[In short, ...]]", "menyimpulkan di akhir"],
          ["Waktu", "[[At six]], [[an hour later]], [[in the evening]]", "urut dari awal ke akhir hari"],
          ["Sebab-akibat", "[[because]], [[so]], [[as a result]]", "sebab sebelum akibat"]],
   examples=[("[[First, I wake up. Then I take a shower. Finally, I eat breakfast.]]", "Pertama, aku bangun. Lalu aku mandi. Terakhir, aku sarapan.")]),
  tip("Cari awal dan akhirnya dulu", text="Temukan kalimat yang memperkenalkan topik (awal) dan kalimat yang menyimpulkan (akhir). Kalimat di tengah mengikuti urutan waktu atau alasan."),
  summary(["Awal: kalimat topik atau First.", "Tengah: Then, Next, After that, waktu.", "Akhir: Finally atau That is why.", "Kata ganti mengikuti nama/benda yang sudah disebut."])],
 [], [])
paras = [
 ["I had a very busy morning.", "First, I woke up at five and cleaned my room.", "Then I cooked rice for my family.", "After that, I walked to school with my friends.", "Finally, I arrived just before the bell rang."],
 ["Making tea is easy.", "First, boil some water in a kettle.", "Next, put a tea bag into a cup.", "Then pour the hot water into the cup.", "Finally, add sugar and enjoy your tea."],
 ["Last Sunday we visited my grandmother.", "We left home early in the morning.", "After two hours, we arrived at her village.", "She cooked a big lunch for us.", "In the evening, we said goodbye and went home."],
 ["Rani wanted to buy a new bag.", "She went to the market on Saturday.", "She found a blue bag, but it was too expensive.", "After that, she bargained with the seller.", "In the end, she bought the bag at a good price."],
 ["My cat is very clever.", "Every morning it wakes me up by jumping on my bed.", "Then it follows me to the kitchen.", "It waits quietly while I prepare its food.", "That is why I love my cat so much."],
 ["Tom wanted to wash his motorbike.", "First, he filled a bucket with water.", "Then he wet the bike and added soap.", "Next, he cleaned it with a soft cloth.", "Finally, he dried it in the sun."],
 ["It was raining heavily.", "Dina forgot her umbrella.", "She waited under a tree for twenty minutes.", "Then a kind man offered her a ride.", "As a result, she got home dry."],
 ["Our school has a library.", "It is on the second floor.", "Students can borrow two books at a time.", "They must return the books after two weeks.", "Because of this rule, everyone has a chance to read."],
 ["To send an email, open your email program first.", "Then click the button for a new message.", "Next, type the address and the subject.", "After you write your message, check it carefully.", "Finally, click Send."],
 ["Budi lost his wallet on the bus.", "He realised it when he wanted to pay for lunch.", "Then he called the bus company.", "A driver had found the wallet and kept it safe.", "Budi was very happy to get it back."],
 ["Yesterday was my brother's birthday.", "In the morning, we decorated the living room.", "At noon, his friends came to our house.", "We sang a song and he blew out the candles.", "At night, everybody was tired but happy."],
 ["Planting a tree is not difficult.", "First, dig a hole in the ground.", "Then put the young tree into the hole.", "Next, cover the roots with soil.", "Finally, give the tree plenty of water."],
 ["Dina is learning to cook.", "At first, she burned the rice.", "Then she asked her mother for help.", "Her mother showed her how to use the stove.", "Now Dina cooks dinner every Friday."],
 ["The train was late this morning.", "Many passengers waited on the platform.", "After thirty minutes, an announcement told them about the delay.", "Finally, the train arrived and everyone got on.", "Fortunately, nobody missed their appointments."],
 ["Rice is an important food in Indonesia.", "Farmers plant rice in wet fields.", "After a few months, the plants turn yellow.", "Then the farmers harvest the rice by hand.", "At last, the rice is dried and sold at the market."],
 ["I always keep a diary.", "Every night before bed, I write about my day.", "I describe what I did and how I felt.", "Sometimes I read old pages and smile.", "In short, my diary helps me remember happy times."],
 ["Mr. Adi is a teacher.", "He arrives at school at seven every morning.", "First, he checks the homework.", "Then he teaches English until noon.", "In the afternoon, he helps students who need extra lessons."],
 ["The weather changed suddenly.", "First, dark clouds covered the sky.", "Then a strong wind began to blow.", "A few minutes later, it started to rain.", "Soon the street was empty."],
 ["Tom was nervous about the interview.", "He prepared answers the night before.", "On the day, he arrived fifteen minutes early.", "During the interview, he spoke slowly and clearly.", "Two days later, he received a job offer."],
 ["Recycling helps the environment.", "First, separate paper, plastic, and glass.", "Next, put each type in a different bin.", "Then the collectors take the bins to a factory.", "As a result, the materials can be used again."],
]
exps = ["Awal: kalimat topik; tengah: urutan waktu First-Then-After that; akhir: Finally.", "Prosedur: First, Next, Then, Finally.", "Urutan waktu: berangkat, tiba, makan, pulang.", "Urutan peristiwa: ingin, pergi, menemukan, menawar, membeli.", "Topik di awal; That is why menyimpulkan di akhir.", "Prosedur mencuci: isi ember, basahi, bersihkan, keringkan.", "Sebab (hujan) sebelum akibat (menunggu, tumpangan, tiba kering).", "Topik, lokasi, aturan, kewajiban, akibat.", "Prosedur: buka, klik, ketik, periksa, kirim.", "Kehilangan, sadar, menelepon, ditemukan, senang.", "Pagi, siang, malam.", "Prosedur menanam: gali, taruh, tutup, siram.", "At first, Then, kini (Now).", "Terlambat, menunggu, pengumuman, tiba, akibat.", "Proses padi: tanam, menguning, panen, jual.", "Topik, kebiasaan, isi, kadang, In short.", "Topik, tiba, First, Then, sore hari.", "Cuaca berubah: awan, angin, hujan, sepi.", "Persiapan, hari H, saat wawancara, hasil.", "Prosedur daur ulang: pisahkan, taruh, ambil, hasil."]
P = [seq(p, e) for p, e in zip(paras, exps)]
V = [seq([x for k, x in enumerate(p) if k != 2], e) for p, e in zip(paras, exps)]   # versi 4 kalimat
Q = V[-8:]
P = P + V[:-8]
UNIT["practice"] = P
UNIT["quiz"] = Q
