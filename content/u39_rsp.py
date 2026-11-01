from qk import mk, mkf, mko
RSP = dict(practice=mk([
 ('Pilih kata kerja pelapor yang tepat: "The mayor ___ that the bridge would open." (mengumumkan)', "announced", "asked", "told me", "wondered", "announce = mengumumkan."),
 ('Pilih kata kerja pelapor yang tepat: "Officials ___ that the storm might get worse." (memperingatkan)', "warned", "asked", "promised", "denied", "warn = memperingatkan."),
 ('Pilih kata kerja pelapor yang tepat: "He ___ that he had not seen the car." (mengklaim)', "claimed", "asked", "reminded", "told me to", "claim = mengklaim."),
 ('Pilih kata kerja pelapor yang tepat: "Police ___ that two people were injured." (melaporkan)', "reported", "asked", "advised me", "thanked", "report = melaporkan."),
 ('Pilih kalimat yang benar:', "She added that the road was closed.", "She added me that the road was closed.", "She added that the road is closed yesterday.", "She added the road closed that.", "add + that + klausa."),
 ('Pilih kalimat yang benar:', "The minister said that prices would rise.", "The minister said that prices rising.", "The minister said prices would to rise.", "The minister says that prices would rise.", "said + would."),
 ('Pilih kalimat yang SALAH:', "He warned that the road is flooded yesterday.", "He warned that the road was flooded.", "He said that the road was flooded.", "He reported that the road was flooded.", "Kala bergeser ke lampau."),
]) + mkf([
 ("Wali kota mengumumkan bahwa jembatan akan dibuka.", "The mayor ___ that the bridge would open.", "announced", "announce → announced."),
 ("Petugas memperingatkan bahwa badai mungkin memburuk.", "Officials ___ that the storm might get worse.", "warned", "warn → warned."),
 ("Polisi melaporkan bahwa dua orang terluka.", "Police ___ that two people were injured.", "reported", "report → reported."),
 ("Dia menambahkan bahwa jalan ditutup.", "She ___ that the road was closed.", "added", "add → added."),
]), quiz=mk([
 ('Pilih kata kerja pelapor yang tepat: "The teacher ___ that the exam would be easy." (mengatakan/menyebutkan)', "said", "asked", "wondered", "refused", "said that."),
 ('Pilih kata kerja pelapor yang tepat: "The police ___ the public not to enter the area." (memperingatkan)', "warned", "denied", "added", "claimed", "warn + objek + not to."),
 ('Pilih kalimat yang SALAH:', "He claimed me that he was innocent.", "He claimed that he was innocent.", "He told me that he was innocent.", "He said that he was innocent.", "claim tidak diikuti objek langsung."),
]) + mkf([
 ("Dia mengklaim tidak melihat mobil itu.", "He ___ that he had not seen the car.", "claimed", "claim → claimed."),
]))
