from qk import mk, mkf, mko
RSP = dict(practice=mk([
 ('Pilih jawaban yang benar: "I am ill," he said. → He said he ___ ill.', "was", "is", "were", "will be", "Present → past."),
 ('Pilih jawaban yang benar: "I bought a car," she said. → She said she ___ a car.', "had bought", "bought", "buys", "has bought", "Past → past perfect."),
 ('Pilih jawaban yang benar: "I will come tomorrow," he said. → He said he would come ___.', "the next day", "tomorrow", "yesterday", "today", "tomorrow → the next day."),
 ('Pilih jawaban yang benar: "Where do you live?" → She asked me where I ___.', "lived", "do live", "did live", "live do", "Urutan berita + past."),
 ('Pilih jawaban yang benar: "Are you ready?" → He asked ___ I was ready.', "if", "that", "what", "do", "Ya/tidak → if."),
 ('Pilih jawaban yang benar: "Sit down," he said. → He told me ___ down.', "to sit", "sit", "sitting", "that sit", "tell + objek + to V1."),
 ('Pilih jawaban yang benar: "Don\'t be late," she said. → She told me ___ be late.', "not to", "to not", "don\'t", "no to", "tell + objek + not to V1."),
 ('Pilih kalimat yang SALAH:', "She said me that she was tired.", "She told me that she was tired.", "She said that she was tired.", "She told me she was tired.", "said tanpa objek."),
 ('Pilih kalimat yang SALAH:', "He asked where was I.", "He asked where I was.", "He asked if I was there.", "He asked what I wanted.", "Urutan berita."),
 ('Pilih kalimat yang SALAH:', "She said she will come the next day.", "She said she would come the next day.", "She told me she would come the next day.", "She said that she would come the next day.", "will → would."),
]) + mkf([
 ("Dia bilang dia sakit.", "He said he ___ ill.", "was", "Present → past."),
 ("Dia bilang akan datang keesokan harinya.", "He said he would come the ___ day.", "next", "tomorrow → the next day."),
 ("Dia menyuruhku duduk.", "He told me ___ sit down.", "to", "tell + objek + to V1."),
 ("Dia bertanya apakah aku sudah siap.", "He asked ___ I was ready.", "if/whether", "if atau whether."),
]), quiz=mk([
 ('Pilih jawaban yang benar: "I can swim," he said. → He said he ___ swim.', "could", "can", "will", "must", "can → could."),
 ('Pilih jawaban yang benar: "Open the door," she said. → She told me ___ the door.', "to open", "open", "opening", "that open", "tell + objek + to V1."),
 ('Pilih kalimat yang SALAH:', "He asked me what did I want.", "He asked me what I wanted.", "He asked me if I wanted tea.", "He asked me where I lived.", "Urutan berita."),
 ('Pilih jawaban yang benar: "I am here now," she said. → She said she was ___ then.', "there", "here", "now", "this", "here → there; now → then."),
]) + mkf([
 ("Dia menyuruhku agar tidak terlambat.", "She told me ___ to be late.", "not", "tell + objek + not to V1."),
 ("Dia bilang dia sudah membeli mobil.", "She said she ___ bought a car.", "had", "Past → past perfect."),
]))
