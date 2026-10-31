from qk import mk
R3 = dict(practice=mk([
 ("Terjemahan \"Dia lebih tinggi daripada aku\":","She is taller than me.","She is more tall than I.","She taller I.","She is tallest than me.","tr."),
 ("Terjemahan \"Ini buku paling mahal\":","This is the most expensive book.","This is most expensive book.","This is the expensivest book.","This is more expensive book.","tr."),
 ("Terjemahan \"Kucing lebih kecil daripada anjing\":","A cat is smaller than a dog.","A cat is more small than dog.","Cat smaller dog.","A cat is smallest than a dog.","tr."),
 ("Terjemahan \"Dia sama pintarnya dengan kakaknya\":","She is as smart as her sister.","She is same smart her sister.","She smart as like sister.","She is smarter as sister.","tr."),
 ("Terjemahan \"Hari ini lebih panas daripada kemarin\":","Today is hotter than yesterday.","Today is more hot than yesterday.","Today hotter yesterday.","Today is hottest yesterday.","tr."),
 ("Terjemahan \"Dia pelari tercepat di sekolah\":","He is the fastest runner in the school.","He is fastest runner in school.","He is the most fast runner.","He is faster runner of school.","tr."),
 ("Perbaiki: \"He is more taller than me.\"","He is taller than me.","He is more tall than me.","He is tallest than me.","He is taller as me.","fix."),
 ("Perbaiki: \"This is the most cheap shop.\"","This is the cheapest shop.","This is most cheapest shop.","This is cheaper shop.","This is the more cheap shop.","fix."),
 ("Perbaiki: \"She is the more beautiful girl.\"","She is the most beautiful girl.","She is the beautifulest girl.","She is more beautifulest.","She is most beautiful the girl.","fix."),
 ("Perbaiki: \"My bag is as heavy than yours.\"","My bag is as heavy as yours.","My bag is as heavier as yours.","My bag is so heavy than yours.","My bag as heavy that yours.","fix."),
 ("Dialog: \"Which is bigger?\" – \"___\"","The elephant is bigger.","The elephant is biggest.","The elephant more big.","Elephant bigger is.","dialog."),
 ("Dialog: \"Who is the tallest?\" – \"___\"","Budi is the tallest.","Budi is taller.","Budi is tallest the.","Budi tall the.","dialog."),
]), quiz=mk([
 ("\"Lebih murah\":","cheaper","cheapest","more cheap","cheap","word."),
 ("\"Paling mahal\":","the most expensive","more expensive","expensiver","expensive","word."),
 ("\"Lebih baik\":","better","gooder","best","more good","word."),
 ("\"Terburuk\":","the worst","worse","baddest","more bad","word."),
 ("\"Lebih cepat\":","faster","fastest","more fast","fast","word."),
 ("\"Paling lambat\":","the slowest","slower","more slow","slow","word."),
 ("\"Lebih mudah\":","easier","easiest","more easy","easy","word."),
 ("\"Paling sulit\":","the most difficult","more difficult","difficulter","difficult","word."),
]))
