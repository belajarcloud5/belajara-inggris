from qk import mk, mkf, mko
PASS = dict(practice=mk([
 ('Pilih jawaban yang benar: "The bridge ___ by a Japanese company."', "was built", "built", "is build", "were built", "Lampau pasif + pelaku → was built by."),
 ('Pilih jawaban yang benar: "My bike ___ last night."', "was stolen", "stole", "were stolen", "is stolen", "Pelaku tidak diketahui → was stolen."),
 ('Pilih jawaban yang benar: "Three people ___ by firefighters."', "were rescued", "was rescued", "rescued", "are rescued", "Jamak lampau → were rescued."),
 ('Pilih jawaban yang benar: "The fire ___ at 9 p.m."', "was reported", "were reported", "reported", "is report", "Tunggal lampau → was reported."),
 ('Pilih jawaban yang benar: "The suspect ___ yesterday."', "was arrested", "were arrested", "arrested", "has arrest", "was arrested."),
 ('Pilih kalimat yang paling tepat tanpa by (pelaku tidak penting):', "The road was closed for repairs.", "The road was closed by someone for repairs.", "Someone closed the road by repairs.", "The road closed by repairs.", "Pelaku tidak penting → tanpa by."),
 ('Pilih kalimat yang SALAH:', "Two houses were destroyed by.", "Two houses were destroyed by the storm.", "Two houses were destroyed.", "A house was destroyed.", "by harus diikuti pelaku."),
 ('Pilih kalimat yang SALAH:', "The thieves was caught.", "The thieves were caught.", "The thief was caught.", "The thief was caught by the police.", "thieves jamak → were."),
]) + mkf([
 ("Jembatan itu dibangun oleh perusahaan Jepang.", "The bridge was ___ by a Japanese company.", "built", "was built."),
 ("Sepedaku dicuri tadi malam.", "My bike was ___ last night.", "stolen", "V3 dari steal adalah stolen."),
 ("Tiga orang diselamatkan.", "Three people ___ rescued.", "were", "Jamak lampau → were."),
 ("Kebakaran itu dilaporkan.", "The fire was ___.", "reported", "was reported."),
]), quiz=mk([
 ('Pilih jawaban yang benar: "The road ___ closed for repairs."', "was", "were", "is been", "has", "Tunggal lampau → was closed."),
 ('Pilih jawaban yang benar: "Ten houses ___ damaged by the flood."', "were", "was", "is", "has", "Jamak lampau → were."),
 ('Pilih kalimat yang SALAH:', "The song was write by Rina.", "The song was written by Rina.", "The song was sung by Rina.", "The song was recorded.", "V3 dari write adalah written."),
]) + mkf([
 ("Pelaku ditangkap.", "The suspect was ___.", "arrested", "was arrested."),
]))
