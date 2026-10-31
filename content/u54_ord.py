from qk import mko
ORD = dict(practice=mko([('Mari kita mulai.', "Let's get started.", 'start', ''),
 ('Ada tiga butir dalam agenda.', 'There are three items on the agenda.', 'is', ''),
 ('Saya ingin menambahkan sesuatu.', "I'd like to add something.", 'adds', ''),
 ('Saya sepakat dengan Anda.', 'I agree with you.', 'agrees', ''),
 ('Mari kita lanjut ke poin berikutnya.', "Let's move on to the next point.", 'moves', ''),
 ('Siapa yang mencatat notulen?', 'Who is taking the minutes?', 'are', ''),
 ('Kita perlu membuat keputusan.', 'We need to make a decision.', 'makes', '')]), quiz=mko([('Apa langkah berikutnya?', 'What are the next steps?', 'is', ''),
 ('Kita kehabisan waktu.', 'We are running out of time.', 'is', ''),
 ('Rapat berakhir pukul empat.', 'The meeting ends at four.', 'end', '')]))
