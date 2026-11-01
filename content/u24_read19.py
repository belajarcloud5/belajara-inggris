from rdh import story
READ19 = [story("Checking the Homework", "Tag questions",
 "Ms. Sari: You finished the homework, didn't you? Budi: Yes, I did. Ms. Sari: It wasn't difficult, was it? Budi: No, it was easy. Ms. Sari: Dina and Rani are in your group, aren't they? Budi: Yes, they are. Ms. Sari: Good. You can present tomorrow, can't you? Budi: Yes, I can.",
 "Ms. Sari: Kamu sudah menyelesaikan PR, bukan? Budi: Ya, sudah. Ms. Sari: Itu tidak sulit, kan? Budi: Tidak, itu mudah. Ms. Sari: Dina dan Rani ada di kelompokmu, bukan? Budi: Ya, benar. Ms. Sari: Bagus. Kamu bisa presentasi besok, bukan? Budi: Ya, bisa.",
 ("Was the homework difficult?", "No, it was easy.", "Yes, it was very hard.", "Yes, it was too long.", "Yes, Budi did not finish it.", "Budi: \"No, it was easy.\""),
 ("It wasn't difficult, wasn't it?", "You finished the homework, didn't you?", "Dina and Rani are in your group, aren't they?", "You can present tomorrow, can't you?", "Kalimat negatif butuh tag positif: was it?"),
 ('Choose the correct tag: "Dina and Rani are in your group, ___?"', "aren't they", "isn't she", "don't they", "aren't we", "Are → aren't they."),
 [("Kamu bisa presentasi besok, bukan?", "You can present tomorrow, ___ you?", "can't/cant", "Can → can't."),
  ("Itu tidak sulit, kan?", "It wasn't difficult, ___ it?", "was", "Negatif → tag positif.")],
 ("Kamu menyelesaikan PR, bukan?", "You finished the homework, didn't you?", "did", "Lampau positif → didn't you."))]
