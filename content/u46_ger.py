from qk import mk, mkf, mko
GER = dict(practice=mk([
 ('Pilih jawaban yang benar: "She enjoys ___."', "reading", "to read", "read", "reads", "enjoy + V-ing."),
 ('Pilih jawaban yang benar: "He wants ___."', "to leave", "leaving", "leave", "leaves", "want + to V1."),
 ('Pilih jawaban yang benar: "She is good at ___."', "swimming", "to swim", "swim", "swims", "preposition + V-ing."),
 ('Pilih jawaban yang benar: "She lets me ___."', "go", "to go", "going", "goes", "let + objek + V1."),
 ('Pilih jawaban yang benar: "He is too tired ___."', "to walk", "walking", "walk", "for walk", "too ... to V1."),
 ('Pilih jawaban yang benar: "I look forward to ___ you."', "seeing", "see", "saw", "to see", "look forward to + V-ing."),
 ('Pilih jawaban yang benar: "I stopped ___ sweets." (berhenti makan)', "eating", "to eat", "eat", "ate", "stop + V-ing."),
 ('Pilih jawaban yang benar: "They agreed ___ the plan."', "to change", "changing", "change", "changed", "agree + to V1."),
 ('Pilih kalimat yang SALAH:', "She enjoys to dance.", "She enjoys dancing.", "She likes dancing.", "She likes to dance.", "enjoy + V-ing."),
 ('Pilih kalimat yang SALAH:', "He decided going.", "He decided to go.", "He wanted to go.", "He hoped to go.", "decide + to V1."),
 ('Pilih kalimat yang SALAH:', "She lets me to go.", "She lets me go.", "She allows me to go.", "She makes me go.", "let + objek + V1."),
]) + mkf([
 ("Dia suka membaca.", "She enjoys ___.", "reading", "enjoy + V-ing."),
 ("Dia ingin pergi.", "He wants ___ leave.", "to", "want + to V1."),
 ("Dia pandai berenang.", "She is good at ___.", "swimming", "good at + V-ing."),
 ("Aku menantikan bertemu denganmu.", "I look forward to ___ you.", "seeing/meeting", "look forward to + V-ing."),
]), quiz=mk([
 ('Pilih jawaban yang benar: "I avoid ___ late."', "going", "to go", "go", "went", "avoid + V-ing."),
 ('Pilih jawaban yang benar: "She promised ___ me."', "to help", "helping", "help", "helped", "promise + to V1."),
 ('Pilih kalimat yang SALAH:', "I look forward to see you.", "I look forward to seeing you.", "I would like to see you.", "I am happy to see you.", "look forward to + V-ing."),
 ('Pilih jawaban yang benar: "Remember ___ the door." (jangan lupa)', "to lock", "locking", "lock", "locked", "remember + to V1."),
]) + mkf([
 ("Dia memutuskan untuk tinggal.", "He decided ___ stay.", "to", "decide + to V1."),
 ("Aku selesai makan.", "I finished ___.", "eating", "finish + V-ing."),
]))
