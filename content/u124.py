from ub import *
UNIT = vocab_unit("u124",
 ["memesan makanan dengan sopan: *I'd like ...*, *Could I have ...?*",
  "menyebut **alergi, diet, dan tingkat kematangan**",
  "meminta **tagihan** dan memahami tip",
  "mengenali bagian **menu**: starter, main course, dessert"],
 "Di restoran luar negeri kamu perlu membaca menu, memesan, dan meminta tagihan. Gunakan **I'd like ...**, **Could I have ...?**, dan **Could we have the bill, please?**",
 [("Menu dan pesanan", [
   ("menu", "daftar makanan", "Could I see the menu, please?"), ("starter", "hidangan pembuka", "I would like a soup as a starter."), ("main course", "hidangan utama", "For the main course, I'll have the chicken."),
   ("dessert", "hidangan penutup", "We would like to see the dessert menu."), ("special", "menu spesial hari ini", "What is today's special?"), ("order", "memesan / pesanan", "Are you ready to order?"),
   ("side dish", "lauk pendamping", "Could I have a side dish of rice?"), ("recommend", "menyarankan", "What do you recommend?")]),
  ("Preferensi dan alergi", [
   ("vegetarian", "vegetarian", "I am vegetarian."), ("allergic", "alergi", "I am allergic to peanuts."), ("spicy", "pedas", "Is this dish spicy?"),
   ("rare", "setengah matang", "I would like my steak rare."), ("well done", "matang sempurna", "I'd like it well done."), ("sparkling water", "air berkarbonasi", "A bottle of sparkling water, please."),
   ("without", "tanpa", "Could I have it without onions?"), ("gluten-free", "bebas gluten", "Do you have any gluten-free dishes?")]),
  ("Tagihan dan pembayaran", [
   ("bill", "tagihan", "Could we have the bill, please?"), ("tip", "uang tip", "Is the tip included?"), ("service charge", "biaya layanan", "There is a ten percent service charge."),
   ("split the bill", "membagi tagihan", "Can we split the bill?"), ("by card", "dengan kartu", "Can I pay by card?"), ("change", "uang kembalian", "Keep the change."),
   ("takeaway", "dibawa pulang", "Can I have this as takeaway?"), ("table for two", "meja untuk dua orang", "A table for two, please.")])],
 "Dialog: Memesan makanan",
 [("Waiter", "Good evening. Are you ready to order?", "Selamat malam. Sudah siap memesan?"), ("Dina", "Yes. I'd like the chicken soup as a starter.", "Ya. Saya mau sup ayam sebagai pembuka."),
  ("Waiter", "And for the main course?", "Dan hidangan utamanya?"), ("Dina", "The fish, please. Is it spicy?", "Ikannya, tolong. Apakah pedas?"),
  ("Waiter", "No, it is mild.", "Tidak, rasanya ringan."), ("Dina", "Great. And could we have the bill later, please?", "Bagus. Dan bisakah kami minta tagihan nanti?")],
 "Pola sopan: *I'd like ...* untuk memesan, *Could I have ...?* untuk meminta, *Is ... included?* untuk bertanya biaya.", seed=124)
UNIT["practice"] += mkr([
 ("Di pintu restoran.", "Host: Good evening. How many people?", "Minta meja untuk dua orang.", "A table for two, please. // Two people, please. // A table for two.", "two,table"),
 ("Pelayan menanyakan pesananmu.", "Waiter: Are you ready to order?", "Pesan sup ayam sebagai pembuka.", "Yes, I'd like the chicken soup, please. // Yes, I will have the soup as a starter. // Yes, could I have the chicken soup?", "soup,chicken"),
 ("Kamu alergi kacang.", "Waiter: Is there anything I should know about?", "Katakan kamu alergi kacang.", "I am allergic to peanuts. // I have a peanut allergy. // I cannot eat peanuts, I am allergic.", "allergic,allergy,peanuts"),
 ("Kamu vegetarian.", "Waiter: What would you like for the main course?", "Tanyakan hidangan vegetarian.", "Do you have a vegetarian dish? // Is there anything vegetarian? // I am vegetarian. What do you recommend?", "vegetarian"),
 ("Kamu ingin tahu apakah pedas.", "Waiter: Our chicken curry is very popular.", "Tanyakan apakah pedas.", "Is it spicy? // Is the curry spicy? // How spicy is it?", "spicy"),
 ("Kamu ingin minuman.", "Waiter: What would you like to drink?", "Pesan air berkarbonasi.", "A bottle of sparkling water, please. // Sparkling water, please. // Could I have some sparkling water?", "sparkling,water"),
 ("Kamu selesai makan.", "Waiter: Would you like anything else?", "Minta tagihan.", "Could we have the bill, please? // The bill, please. // Can I have the bill, please?", "bill"),
 ("Kamu ingin membayar dengan kartu.", "Waiter: Here is the bill.", "Tanyakan apakah bisa memakai kartu.", "Can I pay by card? // Do you accept credit cards? // May I pay by card?", "card,credit"),
])
