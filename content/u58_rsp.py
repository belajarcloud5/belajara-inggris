from qk import mk, mkf, mko
RSP = dict(practice=mk([
 ('Laporkan: "The part will arrive on Monday." → The supplier said the part ___ arrive on Monday.', "would", "will", "can", "does", "will → would."),
 ('Laporkan: "We have fixed the bug." → The engineer told me they ___ fixed the bug.', "had", "have", "has", "were", "present perfect → past perfect."),
 ('Laporkan: "Can you test it today?" → The client asked if we ___ test it that day.', "could", "can", "will", "must", "can → could; today → that day."),
 ('Laporkan: "Don\'t change the settings." → The manager told us ___ change the settings.', "not to", "to not", "don't", "no to", "tell + objek + not to V1."),
 ('Pilih kalimat yang benar:', "The client said that the system was too slow.", "The client said that the system is too slow yesterday.", "The client said me that the system was slow.", "The client says that the system was slow.", "Present → past."),
 ('Pilih kalimat yang SALAH:', "The engineer said me they had fixed it.", "The engineer told me they had fixed it.", "The engineer said they had fixed it.", "The engineer told us they had fixed it.", "said tanpa objek."),
 ('Pilih kalimat yang SALAH:', "The manager asked when would the report be ready.", "The manager asked when the report would be ready.", "The manager asked if the report was ready.", "The manager asked us to finish it.", "Urutan berita."),
]) + mkf([
 ("Pemasok bilang suku cadang akan tiba hari Senin.", "The supplier said the part ___ arrive on Monday.", "would", "will → would."),
 ("Teknisi memberitahuku bahwa mereka sudah memperbaikinya.", "The engineer told me they ___ fixed it.", "had", "present perfect → past perfect."),
 ("Klien bertanya apakah kami bisa mengujinya hari itu.", "The client asked if we ___ test it that day.", "could", "can → could."),
 ("Manajer menyuruh kami agar tidak mengubah pengaturan.", "The manager told us ___ to change the settings.", "not", "tell + objek + not to V1."),
]), quiz=mk([
 ('Laporkan: "The server is slow." → The client said the server ___ slow.', "was", "is", "were", "will be", "Present → past."),
 ('Laporkan: "Please send the update." → The manager asked me ___ the update.', "to send", "send", "sending", "that send", "ask + objek + to V1."),
 ('Pilih kalimat yang SALAH:', "The client told that the system was slow.", "The client told us that the system was slow.", "The client said that the system was slow.", "The client said the system was slow.", "tell butuh objek."),
]) + mkf([
 ("Klien bilang sistemnya terlalu lambat.", "The client said that the system ___ too slow.", "was", "Present → past."),
]))
