from ielts_h import ask, tfn
T = "Volunteering is popular among young people in many countries. A recent survey found that 40 percent of people aged 16 to 24 had volunteered in the past year, compared with 25 percent of people over 55. Most young volunteers said they wanted to gain work experience, while older volunteers said they wanted to help their community. Organisers say that one problem is that many volunteers stop after a few months."
I4 = dict(practice=tfn(T, [
 ("Volunteering is popular among young people.", 'T', "Teks menyebutnya."),
 ("25 percent of young people had volunteered.", 'F', "Teks: 40 percent."),
 ("Older volunteers mainly want work experience.", 'F', "Mereka ingin membantu komunitas."),
 ("Many volunteers stop after a few months.", 'T', "Disebut organisers."),
 ("Volunteers in cities are more active than in villages.", 'N', "Tidak disebut.")]) + ask(T, [
 ("Skimming: gagasan utama teks?", "sukarelawan dan alasan mereka", "cara mendapat pekerjaan tetap", "sejarah organisasi besar dunia", "gaji sukarelawan setiap bulan", "Gambaran umum."),
 ("Scanning: berapa persen yang berusia di atas 55 pernah menjadi sukarelawan?", "25 persen", "40 persen", "14 persen", "55 persen", "Teks: 25 percent."),
 ("Heading terbaik untuk teks:", "Who volunteers and why", "How to find a job", "The cost of surveys", "Problems at work", "Ide utama."),
 ("Isian (NO MORE THAN TWO WORDS): 'Young volunteers wanted to gain ___.'", "work experience", "money and a new job", "a prize", "holidays", "Teks: work experience.")]),
 quiz=tfn(T, [
 ("The survey covered people over 55.", 'T', "Dibandingkan dengan 25 percent."),
 ("The survey was done ten years ago.", 'F', "Teks: recent survey."),
 ("Governments pay volunteers.", 'N', "Tidak disebut.")]) + ask(T, [
 ("Kata 'community' paling dekat dengan...", "masyarakat sekitar", "kantor tempat bekerja", "sekolah tempat belajar", "negara-negara asing", "Community = komunitas."),
 ("Kata 'recent' paling dekat dengan...", "baru-baru ini", "dulu sekali", "akan datang", "tidak jelas", "Recent = baru.")]))
