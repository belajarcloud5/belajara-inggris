from qk import mk, mkf, mko
RSP = dict(practice=mk([
 ('Laporkan hasil rapat: "The budget is limited," Sam said. → Sam said that the budget ___ limited.', "was", "is", "were", "will be", "Present → past."),
 ('Laporkan hasil rapat: Anna: "Let\'s reduce travel costs." → Anna ___ reducing travel costs.', "suggested", "suggested us", "said to", "told", "suggest + V-ing."),
 ('Laporkan hasil rapat: "The project will start in June." → It was agreed that the project ___ start in June.', "would", "will", "can", "does", "will → would."),
 ('Laporkan hasil rapat: "Ben, please prepare the report." → Ben was asked ___ the report.', "to prepare", "prepare", "preparing", "that prepare", "ask + to V1."),
 ('Laporkan hasil rapat: "Can the deadline be extended?" → Sam asked whether the deadline ___ extended.', "could be", "can be", "could", "be could", "can → could."),
 ('Pilih kalimat yang SALAH:', "Anna suggested to reduce costs.", "Anna suggested reducing costs.", "Anna suggested that we reduce costs.", "Anna said that costs were high.", "suggest tidak diikuti to."),
 ('Pilih kalimat yang SALAH:', "The chair announced that the meeting end at noon.", "The chair announced that the meeting would end at noon.", "The chair said the meeting would end at noon.", "The chair told us the meeting would end.", "announce + that + would."),
]) + mkf([
 ("Sam bilang anggaran terbatas.", "Sam said that the budget ___ limited.", "was", "Present → past."),
 ("Anna menyarankan mengurangi biaya perjalanan.", "Anna ___ reducing travel costs.", "suggested", "suggest + V-ing."),
 ("Diputuskan bahwa proyek akan dimulai bulan Juni.", "It was agreed that the project ___ start in June.", "would", "will → would."),
 ("Ben diminta menyiapkan laporan.", "Ben was asked ___ prepare the report.", "to", "ask + to V1."),
]), quiz=mk([
 ('Laporkan hasil rapat: "I am ready," Ben said. → Ben said he ___ ready.', "was", "is", "were", "will be", "Present → past."),
 ('Laporkan hasil rapat: "We will finish soon." → The team said it ___ finish soon.', "would", "will", "can", "does", "will → would."),
 ('Pilih kalimat yang SALAH:', "She asked whether the date can be changed.", "She asked whether the date could be changed.", "She asked if the date could be changed.", "She asked if we could change the date.", "can → could."),
]) + mkf([
 ("Ketua mengumumkan bahwa rapat akan berakhir tengah hari.", "The chair ___ that the meeting would end at noon.", "announced", "announce → announced."),
]))
