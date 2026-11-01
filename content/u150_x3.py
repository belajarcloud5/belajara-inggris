from ub import *
paras = [
 (["Making a sandwich is easy.", "First, take two slices of bread.", "Next, put cheese and tomato on one slice.", "Then cover it with the other slice.", "Finally, cut it in half and enjoy it."], "Prosedur sandwich."),
 (["I went to the library after school.", "I looked for a book about space.", "Then I found a quiet table.", "I read for an hour and took notes.", "At five o'clock, I borrowed the book and went home."], "Rangkaian kegiatan di perpustakaan."),
 (["My town has a famous festival every year.", "Many visitors arrive a week before it starts.", "On the first day, there is a colourful parade.", "In the evening, people enjoy music and food.", "That is why everyone loves the festival."], "Topik, persiapan, hari pertama, malam, penutup."),
 (["Mr. Adi was late for work.", "His alarm clock did not ring.", "He ran to the bus stop, but the bus had left.", "He took a taxi instead.", "Fortunately, he arrived before the meeting began."], "Masalah, penyebab, usaha, solusi, hasil."),
 (["Learning to ride a bicycle takes practice.", "At first, you will probably fall a few times.", "Then you learn to keep your balance.", "After a week, you can ride without help.", "Soon riding becomes fun."], "Proses belajar bersepeda."),
 (["It was Rani's first day at the new school.", "She was nervous, so she arrived early.", "A teacher welcomed her at the gate.", "In class, a girl invited her to sit together.", "By the end of the day, Rani had a new friend."], "Awal hari, perasaan, sambutan, kelas, akhir."),
]
X3 = dict(practice=[seq(p, e) for p, e in paras] + [seq([x for k, x in enumerate(p) if k != 2], e) for p, e in paras], quiz=[seq(p, e) for p, e in paras[:3]])
