from qk import mk, mkf, mko
RSP = dict(practice=mk([
 ('Ubah ke ujaran tidak langsung: "I am tired," she said. → She said she ___ tired.', "was", "is", "were", "will be", "Present → past."),
 ('Ubah: "I like tea," he said. → He said he ___ tea.', "liked", "likes", "like", "will like", "Present → past."),
 ('Ubah: "We went home," they said. → They said they ___ home.', "had gone", "went", "have gone", "go", "Past → past perfect."),
 ('Ubah: "I will call you," she told me. → She told me she ___ call me.', "would", "will", "can", "does", "will → would."),
 ('Pilih kalimat yang benar:', "She told me that she was ill.", "She told that she was ill.", "She said me that she was ill.", "She told me that she is ill yesterday.", "tell + objek."),
 ('Pilih kalimat yang benar:', "He said that he was hungry.", "He said me that he was hungry.", "He tells that he was hungry.", "He said that he is hungry yesterday.", "say tanpa objek."),
 ('Pilih kalimat yang SALAH:', "She said me she was tired.", "She told me she was tired.", "She said she was tired.", "She told me that she was tired.", "say tidak diikuti objek langsung."),
]) + mkf([
 ("Dia bilang dia lelah.", "She said she ___ tired.", "was", "Present → past."),
 ("Dia memberitahuku bahwa dia sakit.", "She ___ me that she was ill.", "told", "tell + objek."),
 ("Dia bilang akan menelepon.", "She said she ___ call.", "would", "will → would."),
 ("Mereka bilang mereka sudah pulang.", "They said they ___ gone home.", "had", "Past → past perfect."),
]), quiz=mk([
 ('Ubah: "I am hungry," Tom said. → Tom said he ___ hungry.', "was", "is", "were", "will be", "Present → past."),
 ('Ubah: "I will help," she said. → She said she ___ help.', "would", "will", "can", "does", "will → would."),
 ('Pilih kalimat yang SALAH:', "He told that he was late.", "He told me that he was late.", "He said that he was late.", "He said he was late.", "tell butuh objek."),
]) + mkf([
 ("Dia bilang dia suka teh.", "He said he ___ tea.", "liked", "Present → past."),
]))
