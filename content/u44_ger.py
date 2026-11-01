from qk import mk, mkf, mko
GER = dict(practice=mk([
 ('Pilih jawaban yang benar: "The task was too difficult ___."', "to finish", "finishing", "finish", "for finish", "too + adj + to V1."),
 ('Pilih jawaban yang benar: "I am experienced enough ___ a team."', "to lead", "leading", "lead", "for lead", "adj + enough + to V1."),
 ('Pilih jawaban yang benar: "I have enough skills ___ the job."', "to do", "doing", "do", "did", "enough + noun + to V1."),
 ('Pilih jawaban yang benar: "I am good at ___ problems."', "solving", "to solve", "solve", "solved", "good at + V-ing."),
 ('Pilih jawaban yang benar: "I am not too shy ___ questions."', "to ask", "asking", "ask", "asked", "too + adj + to V1."),
 ('Pilih kalimat yang benar:', "I am confident enough to speak.", "I am enough confident to speak.", "I am confident enough speaking.", "I am confident enough for speak.", "adj + enough + to V1."),
 ('Pilih kalimat yang SALAH:', "She is too tired for go.", "She is too tired to go.", "She is tired enough to sleep.", "She is not too tired to go.", "too ... to V1."),
 ('Pilih kalimat yang SALAH:', "I am enough old to drive.", "I am old enough to drive.", "I am too young to drive.", "I have enough time to drive.", "adj + enough."),
]) + mkf([
 ("Tugas itu terlalu sulit untuk diselesaikan.", "The task was too difficult ___ finish.", "to", "too ... to V1."),
 ("Saya cukup berpengalaman untuk memimpin tim.", "I am experienced ___ to lead a team.", "enough", "adj + enough + to V1."),
 ("Saya pandai memecahkan masalah.", "I am good at ___ problems.", "solving", "good at + V-ing."),
 ("Saya cukup berani untuk bertanya.", "I am brave ___ to ask.", "enough", "adj + enough + to V1."),
]), quiz=mk([
 ('Pilih jawaban yang benar: "She is old enough ___ alone."', "to travel", "traveling", "travel", "for travel", "adj + enough + to V1."),
 ('Pilih jawaban yang benar: "He is too young ___ a car."', "to drive", "driving", "drive", "for drive", "too + adj + to V1."),
 ('Pilih kalimat yang SALAH:', "I am good at to solve problems.", "I am good at solving problems.", "I am able to solve problems.", "I like solving problems.", "good at + V-ing."),
]) + mkf([
 ("Saya punya cukup keterampilan.", "I have ___ skills.", "enough", "enough + noun."),
]))
