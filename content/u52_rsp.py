from qk import mk, mkf, mko
RSP = dict(practice=mk([
 ('Sampaikan pesan: "I will call back at five." → Mr. Hadi called. He said he ___ call back at five.', "would", "will", "can", "does", "will → would."),
 ('Sampaikan pesan: "Please send the file." → She asked you ___ the file.', "to send", "send", "sending", "that send", "ask + objek + to V1."),
 ('Sampaikan pesan: "Can you call me?" → He asked ___ you could call him.', "if", "that", "do", "what", "Ya/tidak → if."),
 ('Sampaikan pesan: "I am in a meeting." → She said she ___ in a meeting.', "was", "is", "were", "will be", "Present → past."),
 ('Pilih ungkapan yang sopan untuk menyampaikan pesan:', "Could you tell her that I called?", "You tell her I call.", "Tell her I called now.", "Say her that I called.", "Could you tell her ...?"),
 ('Pilih kalimat yang SALAH:', "She said me she would call back.", "She told me she would call back.", "She said she would call back.", "She asked me to call back.", "said tanpa objek."),
 ('Pilih kalimat yang SALAH:', "He asked if could you call him.", "He asked if you could call him.", "He asked you to call him.", "He said you should call him.", "Urutan berita: if you could."),
]) + mkf([
 ("Dia bilang akan menelepon kembali.", "He said he ___ call back.", "would", "will → would."),
 ("Dia meminta Anda mengirim berkas itu.", "She asked you ___ send the file.", "to", "ask + objek + to V1."),
 ("Dia bertanya apakah Anda bisa meneleponnya.", "He asked ___ you could call him.", "if/whether", "if atau whether."),
 ("Dia bilang dia sedang rapat.", "She said she ___ in a meeting.", "was", "Present → past."),
]), quiz=mk([
 ('Sampaikan pesan: "I\'ll send it tomorrow." → She said she ___ send it the next day.', "would", "will", "can", "does", "will → would."),
 ('Pilih ungkapan yang sopan:', "Please let him know that I called.", "Tell him I call.", "Him know I called.", "Say him I called.", "Please let him know that ..."),
 ('Pilih kalimat yang SALAH:', "She asked that I call her.", "She asked me to call her.", "She asked if I could call her.", "She said I should call her.", "ask + objek + to V1."),
]) + mkf([
 ("Dia meminta saya menelepon kembali.", "She asked me ___ call back.", "to", "ask + objek + to V1."),
]))
