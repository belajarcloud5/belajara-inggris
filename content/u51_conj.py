from qk import mk, mkf, mko
CONJ = dict(practice=mk([
 ('Pilih kata yang tepat: "We offer free delivery. ___, we can offer a discount." (selain itu)', "In addition", "However", "Otherwise", "Because", "Menambah → In addition."),
 ('Pilih kata yang tepat: "The office is open on Sunday. ___, the manager is away."', "However", "Furthermore", "Therefore", "In addition", "Pertentangan → However."),
 ('Pilih kata yang tepat: "The file was damaged. ___, please send it again."', "Therefore", "However", "Otherwise", "Although", "Akibat → Therefore."),
 ('Pilih kata yang tepat: "I am writing ___ confirm the date."', "in order to", "because", "although", "otherwise", "Tujuan → in order to."),
 ('Pilih kata yang tepat: "Please reply today. ___, we will cancel the order."', "Otherwise", "Furthermore", "Therefore", "In addition", "Kalau tidak → Otherwise."),
 ('Pilih kata yang tepat: "We changed the date ___ everyone can attend."', "so that", "although", "otherwise", "however", "Tujuan → so that."),
 ('Pilih kalimat yang benar:', "However, we cannot confirm the date.", "However we cannot, confirm the date.", "However. we cannot confirm the date.", "However we, cannot confirm the date.", "However di awal, diikuti koma."),
 ('Pilih kalimat yang SALAH:', "I am writing for to ask about the schedule.", "I am writing to ask about the schedule.", "I am writing in order to ask about the schedule.", "I am writing so that I can ask about the schedule.", "Tujuan → to / in order to."),
 ('Pilih kalimat yang SALAH:', "The price is high, however it is fair.", "The price is high. However, it is fair.", "The price is high, but it is fair.", "The price is high; however, it is fair.", "Jangan menyambung dua klausa dengan however dan koma saja."),
]) + mkf([
 ("Selain itu, kami bisa memberi diskon.", "___, we can offer a discount.", "In addition", "In addition = selain itu."),
 ("Namun, kami tidak bisa mengonfirmasi tanggalnya.", "___, we cannot confirm the date.", "However", "However = namun."),
 ("Saya menulis untuk mengonfirmasi tanggal.", "I am writing in ___ to confirm the date.", "order", "in order to."),
 ("Kalau tidak, kami akan membatalkan pesanan.", "___, we will cancel the order.", "Otherwise", "Otherwise = kalau tidak."),
]), quiz=mk([
 ('Pilih kata yang tepat: "The item is out of stock. ___, we will refund you."', "Therefore", "Furthermore", "However", "Otherwise", "Akibat → Therefore."),
 ('Pilih kata yang tepat: "I am attaching the file ___ you can review it."', "so that", "although", "however", "otherwise", "Tujuan → so that."),
 ('Pilih kata yang tepat: "The report is long. ___, it is useful."', "However", "Therefore", "In addition", "Furthermore", "Pertentangan → However."),
]) + mkf([
 ("Selain itu, bisakah Anda mengirim daftar harga?", "___, could you send the price list?", "Furthermore", "Furthermore = selain itu."),
]))
