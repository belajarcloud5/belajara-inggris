from qk import mk, mkf, mko
CONJ = dict(practice=mk([
 ('Pilih kata yang tepat: "___ it was raining, we went out."', "Although", "Despite", "Because", "Unless", "Diikuti klausa, berlawanan → although."),
 ('Pilih kata yang tepat: "___ the rain, we went out."', "Despite", "Although", "Because", "Unless", "Diikuti kata benda → despite."),
 ('Pilih kata yang tepat: "We will lose ___ we practice."', "unless", "although", "despite", "whereas", "Kecuali kita berlatih → unless."),
 ('Pilih kata yang tepat: "Anna likes tea, ___ Budi likes coffee."', "whereas", "unless", "despite", "because of", "Membandingkan dua hal → whereas."),
 ('Pilih kata yang tepat: "It is cheap. ___, it is not good."', "However", "Although", "Because", "Unless", "Kalimat baru berlawanan → However."),
 ('Pilih kata yang tepat: "___ being tired, he finished the work."', "Despite", "Although", "Unless", "Whereas", "Despite + V-ing."),
 ('Pilih kalimat yang benar:', "Although it is expensive, I like it.", "Although it is expensive, but I like it.", "Despite it is expensive, I like it.", "Although expensive of it, I like it.", "Although dan but tidak dipakai bersamaan."),
 ('Pilih kalimat yang SALAH:', "Despite it was raining, we played.", "Despite the rain, we played.", "Although it was raining, we played.", "In spite of the rain, we played.", "Despite tidak diikuti klausa langsung."),
 ('Pilih kalimat yang benar:', "Unless you study, you will fail.", "Unless you don't study, you will fail.", "Unless you study not, you will fail.", "Unless you studying, you will fail.", "Unless sudah bermakna negatif."),
 ('Pilih kalimat yang SALAH:', "Although he was tired, but he worked.", "Although he was tired, he worked.", "He was tired, but he worked.", "Despite being tired, he worked.", "Pilih although atau but, jangan keduanya."),
]) + mkf([
 ("Meskipun hujan, kami pergi.", "___ it rained, we went out.", "Although", "Diikuti klausa → although."),
 ("Meskipun hujan, kami pergi. (kata benda)", "___ the rain, we went out.", "Despite", "Diikuti kata benda → despite."),
 ("Kita kalah kecuali kita berlatih.", "We will lose ___ we practice.", "unless", "Kecuali → unless."),
 ("Anna suka teh, sedangkan Budi suka kopi.", "Anna likes tea, ___ Budi likes coffee.", "whereas/while", "Membandingkan → whereas atau while."),
]), quiz=mk([
 ('Pilih kata yang tepat: "___ his age, he runs every day."', "Despite", "Although", "Unless", "Whereas", "Despite + kata benda."),
 ('Pilih kata yang tepat: "___ he is old, he runs every day."', "Although", "Despite", "Unless", "Because of", "Although + klausa."),
 ('Pilih kata yang tepat: "You will be late ___ you hurry."', "unless", "although", "despite", "whereas", "Kecuali → unless."),
]) + mkf([
 ("Meskipun mahal, aku suka.", "___ it is expensive, I like it.", "Although/Though", "Although atau Though."),
]))
