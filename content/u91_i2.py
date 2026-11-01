from ielts_h import ask, tfn
A = "Last year the town council introduced a free bus service in the city centre. Since then the number of cars entering the centre has fallen by 20 percent. Shop owners were worried at first, but sales have actually risen slightly. The council says it will extend the service to the suburbs next year if funding is available."
B = "Chocolate was first made in Central America more than 3,000 years ago. People drank it as a bitter drink rather than eating it. It reached Europe in the sixteenth century, where sugar was added to make it sweeter. The first solid chocolate bar was produced in England in 1847."
I2 = dict(practice=tfn(A, [
 ("The free bus service is in the city centre.", 'T', "Disebut langsung."),
 ("Car traffic in the centre has risen.", 'F', "Teks: fallen by 20 percent."),
 ("Shop sales have fallen since the bus service started.", 'F', "Teks: risen slightly."),
 ("Shop owners were happy from the start.", 'F', "Teks: worried at first."),
 ("The service will definitely be extended next year.", 'F', "Teks: if funding is available."),
 ("The bus service costs the council five million pounds.", 'N', "Biaya tidak disebut.")]) + tfn(B, [
 ("People first made chocolate in Central America.", 'T', "Disebut langsung."),
 ("Early chocolate was a sweet drink.", 'F', "Teks: bitter drink."),
 ("Chocolate reached Europe in the sixteenth century.", 'T', "Disebut langsung."),
 ("Sugar was added in Europe.", 'T', "Disebut langsung."),
 ("The first chocolate bar was made in Switzerland.", 'F', "Teks: England."),
 ("Children liked chocolate more than adults.", 'N', "Tidak disebut.")]) + ask(A, [
 ("Skimming: Teks ini membahas...", "dampak bus gratis di pusat kota", "cara membeli mobil", "sejarah toko", "harga tiket kereta", "Gambaran umum."),
 ("Scanning: Berapa persen mobil berkurang?", "20 persen", "2 persen", "12 persen", "50 persen", "fallen by 20 percent."),
 ("Pilih kata pengisi (NO MORE THAN TWO WORDS): 'Sales have risen ___.'", "slightly", "very slightly more", "a lot of", "in the suburbs", "Teks: slightly."),
 ("Kata 'extend' paling dekat dengan...", "memperluas", "menghentikan", "menjual", "mengurangi", "Extend = memperluas.")]),
 quiz=ask(B, [
 ("Scanning: Kapan bar cokelat padat pertama dibuat?", "1847", "1547", "1874", "1947", "in 1847."),
 ("Skimming: Teks ini mengenai...", "sejarah cokelat", "cara memanggang roti", "pertanian modern", "olahraga Eropa", "Gambaran umum."),
 ("Pilih heading terbaik:", "From bitter drink to sweet bar", "A trip to England", "Farming in Central America", "Why sugar is bad", "Ide utama teks."),
 ("Kata 'bitter' paling dekat dengan...", "pahit", "manis", "asin", "pedas", "Bitter = pahit.")]))
