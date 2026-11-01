from qk import mk, mkf, mko
GER = dict(practice=mk([
 ('Pilih jawaban yang benar: "I enjoy ___."', "swimming", "to swim", "swim", "swam", "enjoy + V-ing."),
 ('Pilih jawaban yang benar: "She finished ___ her homework."', "doing", "to do", "do", "did", "finish + V-ing."),
 ('Pilih jawaban yang benar: "He avoids ___ late."', "going", "to go", "go", "went", "avoid + V-ing."),
 ('Pilih jawaban yang benar: "They decided ___ out."', "to go", "going", "go", "went", "decide + to V1."),
 ('Pilih jawaban yang benar: "She refused ___ the offer."', "to accept", "accepting", "accept", "accepted", "refuse + to V1."),
 ('Pilih jawaban yang benar: "We suggest ___ earlier."', "leaving", "to leave", "leave", "left", "suggest + V-ing."),
 ('Pilih jawaban yang benar: "Remember ___ the door when you leave." (jangan lupa)', "to lock", "locking", "lock", "locked", "remember + to V1 = jangan lupa."),
 ('Pilih kalimat yang SALAH:', "She enjoys to swim.", "She enjoys swimming.", "She likes swimming.", "She likes to swim.", "enjoy + V-ing."),
 ('Pilih kalimat yang SALAH:', "He hoped winning the prize.", "He hoped to win the prize.", "He wanted to win the prize.", "He planned to win the prize.", "hope + to V1."),
]) + mkf([
 ("Aku suka berenang.", "I enjoy ___.", "swimming", "enjoy + V-ing."),
 ("Dia selesai mengerjakan PR.", "She finished ___ her homework.", "doing", "finish + V-ing."),
 ("Mereka memutuskan untuk keluar.", "They decided ___ go out.", "to", "decide + to V1."),
 ("Kami menyarankan berangkat lebih awal.", "We suggest ___ earlier.", "leaving", "suggest + V-ing."),
]), quiz=mk([
 ('Pilih jawaban yang benar: "I stopped ___ because I was tired." (berhenti melakukan)', "running", "to run", "run", "ran", "stop + V-ing = berhenti melakukan."),
 ('Pilih jawaban yang benar: "She learned ___ the guitar."', "to play", "playing", "play", "played", "learn + to V1."),
 ('Pilih kalimat yang SALAH:', "He avoids to talk to her.", "He avoids talking to her.", "He wants to talk to her.", "He enjoys talking to her.", "avoid + V-ing."),
]) + mkf([
 ("Aku suka bermain (dua bentuk bisa).", "I like ___ football.", "playing/to play", "like + V-ing atau to V1."),
]))
