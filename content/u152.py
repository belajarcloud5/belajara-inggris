from ub import *
UNIT = mkunit("u152",
 ["menemukan **kalimat yang salah** di antara beberapa kalimat",
  "mengenali kesalahan **to be, tense, artikel, dan bentuk jamak**",
  "memeriksa **kesesuaian subjek dan kata kerja**",
  "membiasakan diri **mengedit** tulisan sendiri"],
 [intro("Mengedit adalah bagian dari menulis. Pada latihan ini ada beberapa kalimat dan **satu** di antaranya mengandung kesalahan. Ketuk kalimat yang salah. Periksa subjek–kata kerja, tense, artikel, dan jamak."),
  gram("1. Daftar periksa mengedit",
   table=[["Periksa", "Pertanyaan", "Contoh kesalahan"],
          ["Subjek + kata kerja", "Apakah cocok (tunggal/jamak)?", "[[He go to school.]] → goes"],
          ["Tense", "Apakah sesuai penanda waktu?", "[[Yesterday I go home.]] → went"],
          ["To be", "Apakah am/is/are tepat?", "[[They is happy.]] → are"],
          ["Artikel", "a/an/the diperlukan?", "[[She has a umbrella.]] → an"],
          ["Jamak", "Apakah kata benda jamak?", "[[Two cat sleep.]] → cats"],
          ["Kata kerja setelah do/did/modal", "Bentuk dasar?", "[[She did not went.]] → go"]]),
  tip("Baca satu per satu", text="Baca setiap kalimat dengan keras, perlahan. Telinga sering mendengar kesalahan sebelum mata menemukannya."),
  summary(["Cek subjek dan kata kerja.", "Cek tense dengan penanda waktu.", "Cek a/an dan jamak.", "Setelah did/can/will: kata kerja dasar."])],
 [], [])
sets = [
 (["My brother plays football every Sunday.", "He have a new ball.", "His team practises at the school field.", "They always have fun."], 1, "He → has."),
 (["Yesterday we went to the beach.", "The water was clean.", "We swim for two hours.", "Then we ate fish."], 2, "Yesterday → swam."),
 (["Dina is a clever girl.", "She speak three languages.", "She wants to be a translator.", "Her parents are proud of her."], 1, "She → speaks."),
 (["There are two cats in my house.", "One cat is black.", "The other cat have white fur.", "I love them both."], 2, "cat → has."),
 (["Tom bought a umbrella yesterday.", "It was raining.", "He walked to school.", "He arrived on time."], 0, "umbrella → an umbrella."),
 (["I am happy today.", "My friends is here.", "We are going to the park.", "We will bring some snacks."], 1, "friends are."),
 (["She did not went to school yesterday.", "She was sick.", "Her mother called the teacher.", "She stayed in bed."], 0, "did not go."),
 (["The children are playing outside.", "They kicks a ball.", "The sun is bright.", "Their mother watches from the window."], 1, "They kick."),
 (["Rani has two brothers.", "Both of them are students.", "One brother study in Bandung.", "The other works in Jakarta."], 2, "One brother studies."),
 (["It was a rainy day.", "We stay at home.", "We played cards and watched TV.", "At night the rain stopped."], 1, "stayed (lampau)."),
 (["I can swims very fast.", "My sister is slower than me.", "We swim in the pool every week.", "The coach is happy."], 0, "can swim."),
 (["My mother is a nurse.", "She works in a hospital.", "She help many sick people.", "Everyone respects her."], 2, "She helps."),
 (["Budi wakes up at five o'clock.", "He takes a shower.", "He eat breakfast at six.", "Then he goes to school."], 2, "He eats."),
 (["This is my new phone.", "It have a big screen.", "The camera is very good.", "I like it a lot."], 1, "It has."),
 (["Last week, Dina visit her grandmother.", "They cooked lunch together.", "Her grandmother told old stories.", "Dina went home in the evening."], 0, "visited."),
 (["There is a lot of rice in the kitchen.", "There are three eggs.", "There is five oranges.", "I will cook dinner."], 2, "There are five oranges."),
 (["My friend lives in Medan.", "She have two sisters.", "They study at the same school.", "I visit them every year."], 1, "She has."),
 (["The teacher gives us homework.", "We does it at home.", "We bring it to class.", "He checks it carefully."], 1, "We do."),
 (["Tom and Rani is classmates.", "They sit together.", "They help each other.", "They get good marks."], 0, "are classmates."),
 (["I have an English book.", "I read it every night.", "It is very interesting.", "My sister borrow it sometimes."], 3, "borrows."),
]
P = [spot(i, a, e) for i, a, e in sets]
Q = P[-8:]
UNIT["practice"] = P
UNIT["quiz"] = Q
