from ub import *
UNIT = vocab_unit("u166",
 ["memahami **idiom menengah** yang sering muncul dalam percakapan",
  "memakai idiom pada **situasi yang tepat**",
  "membedakan **arti harfiah dan kiasan**",
  "mengetahui bahwa idiom **kurang cocok untuk tulisan resmi**"],
 "Di tingkat dasar kamu mempelajari idiom seperti *a piece of cake*. Kini idiom menengah: ungkapan yang sering dipakai di kantor, sekolah, dan pergaulan. Pakai seperlunya dan pada situasi tidak resmi.",
 [("Berbicara dan bekerja sama", [
   ("break the ice", "mencairkan suasana", "He told a joke to break the ice."), ("on the same page", "sepaham", "Let's make sure we are on the same page."), ("in a nutshell", "singkatnya", "In a nutshell, the plan failed."),
   ("go the extra mile", "berusaha lebih", "She always goes the extra mile for customers."), ("get the ball rolling", "memulai", "Let's get the ball rolling."), ("keep an eye on", "mengawasi", "Keep an eye on the baby."),
   ("hit the nail on the head", "tepat sekali", "You hit the nail on the head."), ("speak your mind", "berterus terang", "Don't be afraid to speak your mind.")]),
  ("Waktu dan kebiasaan", [
   ("hit the road", "berangkat", "It's late; we should hit the road."), ("burn the midnight oil", "begadang bekerja", "I burned the midnight oil to finish the report."), ("on the go", "sibuk bergerak", "I'm always on the go."),
   ("better late than never", "lebih baik terlambat daripada tidak sama sekali", "Better late than never!"), ("in the long run", "dalam jangka panjang", "Saving money pays off in the long run."), ("at the last minute", "pada menit terakhir", "He finished at the last minute."),
   ("once and for all", "untuk selamanya", "Let's settle this once and for all."), ("every now and then", "sesekali", "I visit him every now and then.")]),
  ("Uang dan usaha", [
   ("cost a fortune", "sangat mahal", "That car costs a fortune."), ("make ends meet", "mencukupi kebutuhan", "It is hard to make ends meet."), ("save for a rainy day", "menabung untuk keadaan darurat", "Save for a rainy day."),
   ("pay off", "membuahkan hasil", "His hard work paid off."), ("bite the bullet", "menerima hal sulit", "I had to bite the bullet and apologise."), ("back to square one", "kembali ke awal", "We are back to square one."),
   ("a piece of the pie", "bagian dari keuntungan", "Everyone wants a piece of the pie."), ("work like a charm", "berhasil dengan baik", "The new plan worked like a charm.")])],
 "Dialog: Rapat singkat",
 [("Mr. Adi", "Let's get the ball rolling. In a nutshell, we need a new plan.", "Ayo mulai. Singkatnya, kita butuh rencana baru."), ("Ms. Sari", "I think we are on the same page.", "Saya kira kita sepaham."),
  ("Mr. Adi", "Good. Please go the extra mile on this one.", "Bagus. Tolong berusaha lebih keras untuk yang satu ini."), ("Ms. Sari", "Of course. It will pay off in the long run.", "Tentu. Hasilnya akan terasa dalam jangka panjang.")],
 "Tulis satu kalimat sendiri untuk tiap idiom yang kamu hafal, lalu pakai dalam percakapan sungguhan dengan teman atau di catatan harianmu.", seed=166)
UNIT["practice"] += mk([
 ('Mana yang BUKAN idiom?', 'I walk to school.', 'Break the ice.', 'On the same page.', 'Cost a fortune.', 'Kalimat pertama harfiah.'),
 ('Idiom mana yang berarti "mengecek bahwa semua orang paham yang sama"?', 'be on the same page', 'hit the road', 'burn the midnight oil', 'go the extra mile', 'On the same page.'),
 ('Idiom mana yang berarti "mulai berangkat"?', 'hit the road', 'hit the nail', 'get the ball', 'break the ice', 'Hit the road.'),
 ('Idiom mana yang berarti "sangat mahal"?', 'cost a fortune', 'make ends meet', 'pay off', 'work like a charm', 'Cost a fortune.'),
 ('Idiom mana yang berarti "kembali ke awal"?', 'back to square one', 'every now and then', 'once and for all', 'in the long run', 'Back to square one.'),
 ('Kapan idiom sebaiknya dihindari?', 'dalam tulisan resmi dan ujian', 'saat berbicara dengan teman', 'saat bercanda', 'dalam percakapan santai', 'Idiom bersifat tidak resmi.'),
])
