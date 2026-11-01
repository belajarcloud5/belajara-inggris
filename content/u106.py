from ub import *
UNIT = vocab_unit("u106",
 ["mempelajari **nama pakaian, warna, dan ukuran**",
  "bertanya **harga** dan memilih barang di toko",
  "mengenali kata melalui **arti, ejaan, dan pendengaran**",
  "memakai pola *How much is ...?* dan *Do you have ... in size ...?*"],
 "Berbelanja memerlukan kata untuk pakaian, ukuran, dan harga. Pelajari kata-kata di bawah dan pola kalimat: **How much is this?**, **Can I try it on?**, **Do you have a smaller size?**",
 [("Pakaian", [
   ("shirt", "kemeja", "He wears a white shirt."), ("trousers", "celana panjang", "These trousers are too long."), ("skirt", "rok", "She wears a blue skirt."),
   ("jacket", "jaket", "Put on your jacket."), ("dress", "gaun", "That dress is beautiful."), ("socks", "kaus kaki", "I need new socks."),
   ("shoes", "sepatu", "My shoes are old."), ("hat", "topi", "He wears a hat in the sun.")]),
  ("Ukuran dan kondisi", [
   ("size", "ukuran", "What size do you wear?"), ("small", "kecil", "This shirt is too small."), ("large", "besar", "I need a large size."),
   ("tight", "ketat / sempit", "These shoes are tight."), ("loose", "longgar", "This jacket is loose."), ("fit", "pas", "The trousers fit well."),
   ("cheap", "murah", "This bag is cheap."), ("expensive", "mahal", "That watch is expensive.")]),
  ("Di toko", [
   ("price", "harga", "What is the price?"), ("discount", "diskon", "There is a discount today."), ("receipt", "struk", "Keep the receipt."),
   ("cashier", "kasir", "Pay the cashier."), ("try on", "mencoba (pakaian)", "Can I try on this shirt?"), ("customer", "pelanggan", "The customer wants a refund."),
   ("sale", "obral", "The shop has a big sale."), ("refund", "pengembalian uang", "I want a refund.")])],
 "Dialog: Di toko pakaian",
 [("Rani", "Excuse me, how much is this dress?", "Permisi, berapa harga gaun ini?"), ("Ms. Sari", "It is eighty thousand rupiah.", "Harganya delapan puluh ribu rupiah."),
  ("Rani", "Do you have a smaller size?", "Apakah ada ukuran lebih kecil?"), ("Ms. Sari", "Yes, here you are. You can try it on.", "Ada, silakan. Anda boleh mencobanya."),
  ("Rani", "It fits well. I will take it.", "Pas sekali. Saya ambil."), ("Ms. Sari", "Please pay the cashier.", "Silakan bayar ke kasir.")],
 "Saat berbelanja, sebutkan nama barang dalam bahasa Inggris dalam hati (*shirt, shoes, price*). Latihan dalam situasi nyata lebih cepat membekas.", seed=106)
