from ub import *
from ielts_h import rstory
UNIT = vocab_unit("u146",
 ["membaca **cerita misteri** dengan alur dan kejutan",
  "mengenali **petunjuk** dan **akhir cerita**",
  "memahami kata **penanda urutan dan kejutan** (suddenly, at last)",
  "membuat **dugaan** tentang kelanjutan cerita"],
 "Tahap 5: cerita misteri pendek. Cari petunjuk dalam cerita dan tebak akhirnya sebelum membaca sampai selesai.",
 [("Kata-kata cerita tahap 5", [
   ("mystery", "misteri", "The disappearing cake was a mystery."), ("strange", "aneh", "She heard a strange noise."), ("suddenly", "tiba-tiba", "Suddenly the light went out."),
   ("whisper", "berbisik", "Someone began to whisper."), ("shadow", "bayangan", "A shadow moved behind the curtain."), ("secret", "rahasia", "It was a secret surprise."),
   ("clue", "petunjuk", "The muddy footprints were a clue."), ("discover", "menemukan / mengetahui", "They discovered the truth."), ("surprise", "kejutan", "What a lovely surprise!"),
   ("explain", "menjelaskan", "Please explain what happened."), ("nervous", "gugup", "He felt nervous."), ("at last", "akhirnya", "At last they understood.")])],
 "Dialog: Suara aneh",
 [("Dina", "Did you hear that noise?", "Apakah kamu dengar suara itu?"), ("Tom", "Yes. It came from the kitchen.", "Ya. Datangnya dari dapur."), ("Dina", "I'm nervous. Let's check together.", "Aku gugup. Ayo kita periksa bersama."), ("Tom", "Look! It's just the cat.", "Lihat! Hanya kucing.")],
 "Saat membaca misteri, tulis tiga petunjuk yang kamu temukan, lalu bandingkan dengan akhir cerita.", seed=146)
READ = [
 rstory("The Missing Cake", "Tahap 5", "On Sunday morning, Mother put a chocolate cake on the kitchen table. When Dina came back an hour later, half of the cake was gone. There were small muddy footprints on the floor, and they led to the garden. Dina followed them carefully. Suddenly, she heard a soft noise behind the bushes. It was her puppy, with chocolate all over his face! Dina laughed and Mother, at last, understood the mystery.",
  "Minggu pagi, Ibu menaruh kue cokelat di meja dapur. Ketika Dina kembali satu jam kemudian, separuh kue sudah hilang. Ada jejak kaki kecil berlumpur di lantai, dan jejak itu menuju kebun. Dina mengikutinya dengan hati-hati. Tiba-tiba, dia mendengar suara pelan di balik semak-semak. Itu anak anjingnya, dengan cokelat di seluruh wajahnya! Dina tertawa dan Ibu, akhirnya, memahami misteri itu.",
  [("What was the clue?", "Small muddy footprints", "A broken plate", "An open window", "A note on the table", "Jejak kaki berlumpur."), ("Where did the footprints lead?", "To the garden", "To the bedroom", "To the street", "To the kitchen door", "Menuju kebun."), ("Who ate the cake?", "The puppy", "Dina", "Mother", "A neighbour", "Anak anjing.")], [],
  [("Separuh kue hilang.", "Half of the cake was ___.", "gone", "Gone."), ("Tiba-tiba dia mendengar suara.", "___, she heard a soft noise.", "Suddenly", "Suddenly.")]),
 rstory("A Secret Surprise", "Tahap 5", "For three days, Rani's friends acted strangely. They whispered in the corridor and stopped talking when she came near. Rani felt nervous and a little sad. On Friday, her teacher asked her to stay in the classroom after the bell. When Rani opened the door of the hall, everybody shouted, \"Happy birthday!\" The strange behaviour was the clue to a secret party.",
  "Selama tiga hari, teman-teman Rani bertingkah aneh. Mereka berbisik di koridor dan berhenti bicara ketika dia mendekat. Rani merasa gugup dan sedikit sedih. Pada hari Jumat, gurunya memintanya tetap di kelas setelah bel. Ketika Rani membuka pintu aula, semua orang berteriak, \"Selamat ulang tahun!\" Perilaku aneh itu adalah petunjuk bagi pesta rahasia.",
  [("How did Rani feel?", "Nervous and a little sad", "Angry and bored", "Happy and excited", "Tired and sleepy", "Gugup dan sedikit sedih."), ("What did the friends do?", "Whispered and stopped talking", "Laughed loudly", "Ignored the teacher", "Played football", "Berbisik."), ("What was the secret?", "A birthday party", "A school trip", "A new teacher", "A test", "Pesta ulang tahun.")], [],
  [("Mereka berbisik di koridor.", "They ___ in the corridor.", "whispered", "Whispered."), ("Itu adalah pesta rahasia.", "It was a ___ party.", "secret", "Secret party.")]),
]
