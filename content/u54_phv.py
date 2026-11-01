from qk import mk, mkf, mko
PHV = dict(practice=mk([
 ('Pilih phrasal verb yang tepat: "Sam ___ the budget." (mengemukakan)', 'brought up', 'brought in', 'showed off', 'threw away', 'bring up = mengemukakan.'),
 ('Pilih phrasal verb yang tepat: "Let\'s ___ the agenda." (meninjau)', 'go over', 'go off', 'look after', 'fill in', 'go over = meninjau.'),
 ('Pilih phrasal verb yang tepat: "Let\'s ___ the meeting." (menutup)', 'wrap up', 'throw away', 'hand in', 'stand up', 'wrap up = menutup.'),
 ('Pilih phrasal verb yang tepat: "We\'ll ___ next week." (menindaklanjuti)', 'follow up', 'fill in', 'stand up', 'show off', 'follow up.'),
 ('Pilih phrasal verb yang tepat: "Anna ___ the meeting." (mengatur)', 'set up', 'set off', 'give back', 'show off', 'set up = mengatur.'),
 ('Pilih phrasal verb yang tepat: "We ___ the decision." (menunda)', 'put off', 'fill in', 'throw away', 'put out', 'put off = menunda.'),
 ('Pilih kalimat yang SALAH:', "Let\'s wrap up it.", "Let\'s wrap it up.", "Let\'s wrap up the meeting.", "Let\'s wrap the meeting up.", "Kata ganti di tengah."),
 ('Pilih kalimat yang SALAH:', "We put off it.", "We put it off.", "We put off the meeting.", "We put the meeting off.", "Kata ganti di tengah."),
]) + mkf([
 ("Sam mengemukakan anggaran.", "Sam brought ___ the budget.", "up", "bring up."),
 ("Mari kita tinjau agenda.", "Let's go ___ the agenda.", "over", "go over."),
 ("Mari kita tutup rapat.", "Let's wrap ___ the meeting.", "up", "wrap up."),
 ("Kami menunda keputusan.", "We put ___ the decision.", "off", "put off."),
]), quiz=mk([
 ('Pilih phrasal verb yang tepat: "We will ___ with the client." (menindaklanjuti)', 'follow up', 'fill in', 'throw away', 'sit down', 'follow up.'),
 ('Pilih phrasal verb yang tepat: "Please ___ the room for the meeting." (menyiapkan)', 'set up', 'set off', 'stand up', 'sit down', 'set up.'),
 ('Pilih kalimat yang SALAH:', "Bring up it, please.", "Bring it up, please.", "Bring up the issue.", "Bring the issue up.", "Kata ganti di tengah."),
]) + mkf([
 ("Mari kita lanjutkan rapatnya.", "Let's carry ___ with the meeting.", "on", "carry on."),
]))
