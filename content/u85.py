from qk import mk, mkf, mko
from helpers import listen

def LS(rows):
    return [listen(q, say, [ans] + ds, 0, exp) for q, say, ans, ds, exp in rows]

UNIT = dict(
 id="u85",
 goals=[
  "mengikuti **perubahan jawaban** (koreksi) dalam percakapan",
  "menangkap **kata kunci** dan menghindari **pengecoh**",
  "melengkapi **catatan** dengan informasi yang tepat",
  "membaca soal **sebelum** rekaman diputar",
 ],
 lesson=[
  dict(t="intro", text="Rekaman IELTS Listening sering memuat **pengecoh (distractors)**: pembicara menyebut satu informasi, lalu **mengoreksinya**. Jawaban yang benar biasanya adalah informasi **terakhir**. Latihan di sini memakai suara; dengarkan dengan teliti, lalu jawab."),

  dict(t="grammar", title="1. Isyarat koreksi",
   table=[["Isyarat", "Contoh", "Artinya"],
          ["**actually**", "[[It's on Monday. Actually, it's on Tuesday.]]", "yang benar Selasa"],
          ["**sorry, I mean**", "[[Room twelve. Sorry, I mean room fourteen.]]", "yang benar empat belas"],
          ["**no, wait**", "[[At six. No, wait, at seven.]]", "yang benar pukul tujuh"],
          ["**not ... but**", "[[Not the library, but the hall.]]", "yang benar aula"],
          ["**on second thought**", "[[Coffee. On second thought, tea.]]", "yang benar teh"]]),

  dict(t="grammar", title="2. Langkah menjawab",
   table=[["Waktu", "Yang dilakukan"],
          ["Sebelum rekaman", "Baca soal, garis bawahi kata kunci, tebak jenis jawaban (angka, nama, tempat)"],
          ["Selama rekaman", "Ikuti urutan soal; catat; waspada isyarat koreksi"],
          ["Setelah rekaman", "Pindahkan jawaban; cek ejaan dan batas kata"]]),

  dict(t="tip", title="Pengecoh mengikuti pola",
   text="Penutur sering menyebut dua pilihan lalu memilih satu. Tulislah jawaban **setelah** kamu yakin tidak ada koreksi lagi, bukan saat kata pertama muncul."),
  dict(t="warn", title="Ejaan dan format",
   text="Jawaban dengan ejaan salah dianggap salah. Perhatikan juga huruf besar untuk nama, dan angka vs kata sesuai perintah."),
 ],

 practice=LS([
  ("Dengarkan. Hari apa pertemuan diadakan?","The meeting is on Monday. Actually, it has been moved to Tuesday.","Tuesday",["Monday","Wednesday","Friday"],"Isyarat 'actually': jawabannya Tuesday."),
  ("Dengarkan. Nomor ruang berapa?","Please go to room twelve. Sorry, I mean room fourteen.","14",["12","40","41"],"'Sorry, I mean' = koreksi menjadi empat belas."),
  ("Dengarkan. Pukul berapa kereta berangkat?","The train leaves at six. No, wait, it leaves at seven.","7",["6","8","5"],"'No, wait' = koreksi."),
  ("Dengarkan. Di mana acara diadakan?","The event is not in the library, but in the main hall.","The main hall",["The library","The garden","The cafe"],"'not ... but' = yang benar aula."),
  ("Dengarkan. Apa yang dipesan?","I'll have coffee. On second thought, I'll have tea.","Tea",["Coffee","Juice","Water"],"'On second thought' = teh."),
  ("Dengarkan. Berapa biaya pendaftaran?","The fee is forty dollars. Actually, there is a discount, so it is thirty.","30 dollars",["40 dollars","13 dollars","14 dollars"],"Koreksi: thirty."),
  ("Dengarkan. Siapa nama pemandu?","Our guide is Mr. Brown. Sorry, his name is Mr. Brand.","Mr. Brand",["Mr. Brown","Mr. Bran","Mr. Brent"],"Koreksi ejaan: Brand."),
  ("Dengarkan. Hari apa kunjungan ke museum?","We'll visit the museum on Wednesday, not Thursday.","Wednesday",["Thursday","Tuesday","Friday"],"not Thursday → Wednesday."),
  ("Dengarkan. Berapa orang yang ikut?","There are fifteen people. Wait, two more joined, so seventeen.","17",["15","70","50"],"Koreksi menjadi seventeen."),
  ("Dengarkan. Apa kegiatan pertama?","First we'll go hiking. Actually, the weather is bad, so we'll start with a museum visit.","A museum visit",["Hiking","Swimming","Shopping"],"Koreksi: museum."),
  ("Dengarkan. Kapan batas pengumpulan tugas?","The deadline is the fifth of June. No, sorry, the fifteenth.","15 June",["5 June","50 June","5 July"],"Koreksi: fifteenth."),
  ("Dengarkan. Apa warna mobil pelanggan?","It was a blue car. Hmm, actually, it was dark green.","Dark green",["Blue","Black","Red"],"Koreksi: dark green."),
  ("Dengarkan. Nomor bus apa?","Take bus number twenty. Sorry, I mean number twelve.","12",["20","10","22"],"Koreksi: twelve."),
  ("Dengarkan. Ke mana mereka akan pergi?","We could go to the beach. But it's cold, so let's go to the cinema.","The cinema",["The beach","The park","The library"],"Keputusan akhir: cinema."),
  ("Dengarkan. Berapa harga tiket dewasa?","Adult tickets are twelve pounds. Children pay half price.","£12",["£6","£2","£20"],"Yang ditanya tiket dewasa."),
 ]) + mk([
  ('Dalam rekaman, kata "Actually" biasanya menandakan...', "koreksi informasi", "pengulangan", "pertanyaan baru", "akhir rekaman", "Actually sering memperkenalkan koreksi."),
  ('"Sorry, I mean ..." biasanya diikuti...', "informasi yang benar", "informasi lama", "pertanyaan", "ucapan terima kasih", "Setelah itu jawaban yang benar."),
  ('Jawaban yang benar biasanya adalah informasi...', "terakhir (setelah koreksi)", "pertama", "yang paling panjang", "tidak disebut", "Setelah koreksi."),
  ('Sebelum rekaman diputar, sebaiknya kamu...', "membaca soal", "menutup soal", "menerjemahkan teks", "tidur", "Baca soal lebih dulu."),
  ('Pengecoh (distractor) adalah...', "informasi yang mirip tetapi bukan jawaban", "jawaban yang pasti benar", "kata penutup", "nama pembicara", "Informasi yang menyesatkan."),
  ('Mana yang menunjukkan koreksi?', "No, wait.", "Thank you.", "Good morning.", "See you.", "No, wait = koreksi."),
  ('Mana yang BUKAN isyarat koreksi?', "By the way", "Actually", "Sorry, I mean", "On second thought", "By the way hanya mengganti topik."),
  ('Saat rekaman berlangsung, kamu sebaiknya...', "mengikuti urutan soal", "menerjemahkan semuanya", "berhenti menulis", "menutup mata", "Soal mengikuti urutan rekaman."),
 ]) + mkf([
  ("Isyarat koreksi: 'Sorry, I ___ room fourteen.'", "Room twelve. Sorry, I ___ room fourteen.", "mean", "Sorry, I mean."),
  ("Isyarat koreksi: 'On second ___ , I will have tea.'", "On second ___, I will have tea.", "thought", "On second thought."),
 ]),

 quiz=LS([
  ("Dengarkan. Hari apa kelas dimulai?","The class begins on Thursday. Actually, it begins on Friday.","Friday",["Thursday","Saturday","Monday"],"Koreksi: Friday."),
  ("Dengarkan. Nomor kursi berapa?","Your seat is number sixty. Sorry, I mean number sixteen.","16",["60","61","26"],"Koreksi: sixteen."),
  ("Dengarkan. Di mana mereka bertemu?","Let's meet at the cafe. No, wait, at the station.","The station",["The cafe","The airport","The library"],"Koreksi: station."),
  ("Dengarkan. Apa yang diminum?","I'll take juice. Actually, a glass of water, please.","Water",["Juice","Tea","Milk"],"Koreksi: water."),
  ("Dengarkan. Berapa harga bukunya?","The book is nineteen dollars. Oh, sorry, it's ninety.","90 dollars",["19 dollars","29 dollars","9 dollars"],"Koreksi: ninety."),
  ("Dengarkan. Kapan ujian?","The exam is on the fourth of May. Wait, the fourteenth.","14 May",["4 May","40 May","14 June"],"Koreksi: fourteenth."),
  ("Dengarkan. Siapa yang akan menjemput?","My brother will pick you up. No, my sister will do it.","His sister",["His brother","His mother","His friend"],"Koreksi: sister."),
  ("Dengarkan. Apa pilihan akhirnya?","We could take a taxi. But it's expensive, so we'll take the bus.","The bus",["A taxi","A train","A bike"],"Keputusan akhir: bus."),
 ]) + mk([
  ('Informasi yang benar biasanya muncul...', "setelah koreksi", "sebelum koreksi", "di awal rekaman", "tidak pernah", "Setelah koreksi."),
  ('"Not the library, but the hall." Jawabannya...', "the hall", "the library", "keduanya", "tidak ada", "not ... but."),
 ]) + mkf([
  ("'No, ___ , at seven.'", "At six. No, ___, at seven.", "wait", "No, wait."),
 ]),
)
