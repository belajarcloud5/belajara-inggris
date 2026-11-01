from qk import mk, mkf, mko
RSP = dict(practice=mk([
 ('Ubah: "I can swim," he said. → He said he ___ swim.', "could", "can", "will", "must", "can → could."),
 ('Ubah: "You must go," she said. → She said I ___ go.', "had to", "must", "will", "may", "must → had to."),
 ('Ubah: "It may rain," he said. → He said it ___ rain.', "might", "may", "will", "can", "may → might."),
 ('Pilih kalimat yang benar:', "He suggested going home.", "He suggested us to go home.", "He suggested to go home.", "He suggested go home.", "suggest + V-ing."),
 ('Pilih kalimat yang benar:', "She promised to call me.", "She promised calling me.", "She promised me call.", "She promised that call me.", "promise + to V1."),
 ('Pilih kalimat yang benar:', "He advised me to rest.", "He advised me rest.", "He advised to me rest.", "He advised me resting.", "advise + objek + to V1."),
 ('Pilih kalimat yang SALAH:', "He suggested us to go.", "He suggested that we go.", "He suggested going.", "He suggested that we should go.", "suggest tidak diikuti objek + to."),
 ('Pilih kalimat yang benar:', "She warned us not to be late.", "She warned us to not late.", "She warned us don't be late.", "She warned us not be late.", "warn + objek + not to V1."),
]) + mkf([
 ("Dia bilang dia bisa berenang.", "He said he ___ swim.", "could", "can → could."),
 ("Dia bilang aku harus pergi.", "She said I ___ to go.", "had", "must → had to."),
 ("Dia berjanji menelepon aku.", "She ___ to call me.", "promised", "promise + to V1."),
 ("Dia menyarankan aku untuk beristirahat.", "He ___ me to rest.", "advised", "advise + objek + to V1."),
]), quiz=mk([
 ('Ubah: "I will help," she said. → She said she ___ help.', "would", "will", "can", "must", "will → would."),
 ('Pilih kalimat yang benar:', "He suggested that we leave early.", "He suggested us leave early.", "He suggested to leave we early.", "He suggested that we to leave early.", "suggest + that + klausa."),
 ('Pilih kalimat yang SALAH:', "She promised calling me.", "She promised to call me.", "She said she would call me.", "She told me she would call.", "promise + to V1."),
]) + mkf([
 ("Dia memperingatkan kami agar tidak terlambat.", "She warned us ___ to be late.", "not", "warn + objek + not to V1."),
]))
