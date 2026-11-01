from ub import *
UNIT = vocab_unit("u126",
 ["bertanya **harga, ukuran, dan diskon** di toko luar negeri",
  "memakai kata untuk **uang dan pembayaran**: exchange rate, change, receipt",
  "meminta **pengembalian atau penukaran** barang dengan sopan",
  "memakai pola *How much is ...?* dan *Do you have this in ...?*"],
 "Berbelanja di luar negeri berarti menanyakan harga, mencoba barang, dan membayar. Pelajari kata penting dan pola kalimat sopannya.",
 [("Harga dan uang", [
   ("exchange rate", "nilai tukar", "What is the exchange rate today?"), ("cash", "uang tunai", "Do you accept cash?"), ("credit card", "kartu kredit", "I will pay by credit card."),
   ("change", "uang kembalian", "Here is your change."), ("receipt", "struk", "Could I have a receipt, please?"), ("price tag", "label harga", "I cannot see the price tag."),
   ("cheaper", "lebih murah", "Do you have a cheaper one?"), ("in total", "secara total", "That is fifty dollars in total.")]),
  ("Di toko", [
   ("fitting room", "ruang ganti", "Where is the fitting room?"), ("try on", "mencoba pakaian", "Can I try this on?"), ("size", "ukuran", "Do you have this in a larger size?"),
   ("colour", "warna", "Does it come in another colour?"), ("on sale", "sedang diskon", "These shoes are on sale."), ("discount", "potongan harga", "Is there a discount?"),
   ("out of stock", "kehabisan stok", "Sorry, this size is out of stock."), ("gift wrap", "bungkus kado", "Could you gift wrap it, please?")]),
  ("Masalah dan pengembalian", [
   ("refund", "pengembalian uang", "I would like a refund."), ("exchange", "menukar barang", "Can I exchange this for a different size?"), ("faulty", "cacat / rusak", "This phone is faulty."),
   ("warranty", "garansi", "Does it come with a warranty?"), ("customer service", "layanan pelanggan", "Please contact customer service."), ("too expensive", "terlalu mahal", "It is too expensive for me."),
   ("bargain", "tawar-menawar / barang murah", "That was a real bargain."), ("shopping bag", "tas belanja", "Do I need to pay for a shopping bag?")])],
 "Dialog: Di toko pakaian",
 [("Rani", "Excuse me, how much is this jacket?", "Permisi, berapa harga jaket ini?"), ("Clerk", "It is eighty dollars, but it is on sale today.", "Delapan puluh dolar, tetapi hari ini sedang diskon."),
  ("Rani", "Do you have it in a larger size?", "Apakah ada ukuran lebih besar?"), ("Clerk", "Yes, here you are. The fitting room is over there.", "Ada, silakan. Ruang gantinya di sana."),
  ("Rani", "It fits well. I'll take it. Can I pay by card?", "Pas sekali. Saya ambil. Bisa bayar dengan kartu?"), ("Clerk", "Of course.", "Tentu.")],
 "Belajar angka dan harga dalam bahasa Inggris lewat label di toko online: bacakan harga dengan keras (*nineteen ninety-nine*).", seed=126)
UNIT["practice"] += mkr([
 ("Di toko. Kamu menanyakan harga.", "Clerk: Can I help you?", "Tanyakan harga jaket.", "How much is this jacket? // How much does this jacket cost? // What is the price of this jacket?", "much,price,cost"),
 ("Kamu ingin ukuran lebih besar.", "Clerk: Here is the jacket you asked for.", "Tanyakan apakah ada ukuran lebih besar.", "Do you have this in a larger size? // Do you have a bigger size? // Is there a larger size?", "larger,bigger,size"),
 ("Kamu ingin mencoba pakaian.", "Clerk: Do you like it?", "Minta mencobanya.", "Can I try it on? // May I try this on? // Where is the fitting room?", "try,fitting"),
 ("Kamu menanyakan diskon.", "Clerk: That is eighty dollars.", "Tanyakan apakah ada diskon.", "Is there a discount? // Can you give me a discount? // Is it on sale?", "discount,sale"),
 ("Kamu membayar.", "Clerk: Will that be cash or card?", "Jawab kartu.", "Card, please. // I will pay by card. // By credit card.", "card"),
 ("Kamu butuh struk.", "Clerk: Here is your change.", "Minta struk.", "Could I have a receipt, please? // Can I get a receipt? // A receipt, please.", "receipt"),
 ("Barang yang kamu beli rusak.", "Clerk: How can I help?", "Katakan barangnya cacat dan minta uang kembali.", "This phone is faulty. I would like a refund. // It does not work. Can I have a refund? // I'd like to return this and get a refund.", "refund,return,faulty,work"),
 ("Kamu ingin menukar ukuran.", "Clerk: Do you have the receipt?", "Katakan ya dan minta menukar ukuran.", "Yes, here it is. Can I exchange it for a different size? // Yes. I'd like to exchange it for a larger size. // Yes. Could I swap it for another size?", "exchange,swap,size"),
])
