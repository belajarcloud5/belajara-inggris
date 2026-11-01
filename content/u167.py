from ub import *
UNIT = vocab_unit("u167",
 ["memahami **idiom tentang perasaan dan situasi**",
  "menyebut **keberuntungan, kejutan, dan masalah** dengan idiom",
  "membedakan idiom yang mirip bentuknya",
  "menjawab pertanyaan makna dan pemakaian idiom"],
 "Idiom juga dipakai untuk menggambarkan perasaan dan keadaan. Pelajari ungkapan-ungkapan berikut beserta situasi yang cocok.",
 [("Perasaan", [
   ("feel blue", "merasa sedih", "I feel blue today."), ("over the moon", "sangat gembira", "She was over the moon about the news."), ("under the weather", "kurang sehat", "I'm a bit under the weather."),
   ("on cloud nine", "sangat bahagia", "He was on cloud nine after the win."), ("get cold feet", "tiba-tiba ragu", "He got cold feet before the speech."), ("have butterflies in your stomach", "gugup", "I had butterflies in my stomach."),
   ("lose your temper", "kehilangan kesabaran", "Don't lose your temper."), ("keep your cool", "tetap tenang", "She kept her cool during the test.")]),
  ("Situasi", [
   ("a blessing in disguise", "berkah tersembunyi", "Losing that job was a blessing in disguise."), ("the last straw", "puncak masalah", "His rudeness was the last straw."), ("out of the blue", "tiba-tiba", "He called me out of the blue."),
   ("a piece of cake", "sangat mudah", "The test was a piece of cake."), ("in the same boat", "senasib", "We are all in the same boat."), ("spill the beans", "membocorkan rahasia", "Who spilled the beans?"),
   ("learn the ropes", "belajar dasar-dasar", "She is learning the ropes at her new job."), ("the tip of the iceberg", "sebagian kecil dari masalah besar", "This is only the tip of the iceberg.")]),
  ("Tindakan", [
   ("jump the gun", "bertindak terlalu cepat", "Don't jump the gun; wait for the results."), ("call the shots", "memegang kendali", "Who calls the shots here?"), ("cut corners", "mengambil jalan pintas", "They cut corners to save money."),
   ("play it by ear", "melihat situasi nanti", "Let's play it by ear."), ("stick to your guns", "berpegang pada pendirian", "He stuck to his guns."), ("sit on the fence", "tidak memihak", "Stop sitting on the fence."),
   ("beat around the bush", "bertele-tele", "Don't beat around the bush."), ("miss the boat", "kehilangan kesempatan", "I missed the boat on that offer.")])],
 "Dialog: Berita mengejutkan",
 [("Dina", "I heard that you got the scholarship!", "Aku dengar kamu mendapat beasiswa!"), ("Rani", "Yes! I'm over the moon. It came out of the blue.", "Ya! Aku sangat gembira. Datang tiba-tiba."),
  ("Dina", "Were you nervous at the interview?", "Apakah kamu gugup saat wawancara?"), ("Rani", "I had butterflies in my stomach, but I kept my cool.", "Perutku mulas, tetapi aku tetap tenang.")],
 "Cari satu idiom baru per hari dari lagu, film, atau video berbahasa Inggris dan tambahkan ke daftarmu bersama kalimat contohnya.", seed=167)
UNIT["practice"] += mk([
 ('Idiom mana yang berarti "bahagia sekali"?', 'over the moon', 'under the weather', 'feel blue', 'cold feet', 'Over the moon.'),
 ('Idiom mana yang berarti "kurang sehat"?', 'under the weather', 'over the moon', 'on cloud nine', 'the last straw', 'Under the weather.'),
 ('Idiom mana yang berarti "gugup"?', 'butterflies in your stomach', 'a blessing in disguise', 'a piece of cake', 'the tip of the iceberg', 'Butterflies.'),
 ('Idiom mana yang berarti "tiba-tiba"?', 'out of the blue', 'in the long run', 'once and for all', 'every now and then', 'Out of the blue.'),
 ('Idiom mana yang berarti "bertele-tele"?', 'beat around the bush', 'play it by ear', 'cut corners', 'sit on the fence', 'Beat around the bush.'),
 ('Idiom mana yang berarti "berkah tersembunyi"?', 'a blessing in disguise', 'the last straw', 'the tip of the iceberg', 'a piece of the pie', 'Blessing in disguise.'),
])
