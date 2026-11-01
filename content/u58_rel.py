from qk import mk, mkf, mko
REL = dict(practice=mk([
 ('Pilih kata yang tepat: "The problem ___ caused the delay was a broken part."', "that", "who", "whose", "where", "Benda → that."),
 ('Pilih kata yang tepat: "The engineer ___ fixed it is on site."', "who", "which", "whose", "where", "Orang → who."),
 ('Pilih kata yang tepat: "The warehouse ___ the parts are stored is closed."', "where", "whose", "who", "which is", "Tempat → where."),
 ('Pilih kata yang tepat: "The server, ___ is old, needs replacing."', "which", "that", "who", "whose is", "Dengan koma → which."),
 ('Pilih kata yang tepat: "The team ___ solved the issue sent a report."', "who", "which", "whose", "where", "Orang → who."),
 ('Pilih kalimat yang benar:', "The report which explains the cause is attached.", "The report who explains the cause is attached.", "The report which it explains the cause is attached.", "The report explains which the cause is attached.", "Benda → which."),
 ('Pilih kalimat yang SALAH:', "The engineer which fixed it is on site.", "The engineer who fixed it is on site.", "The engineer that fixed it is on site.", "The engineer we hired is on site.", "Orang → who/that."),
]) + mkf([
 ("Masalah yang menyebabkan keterlambatan adalah komponen rusak.", "The problem ___ caused the delay was a broken part.", "that/which", "Benda → that atau which."),
 ("Teknisi yang memperbaikinya ada di lokasi.", "The engineer ___ fixed it is on site.", "who/that", "Orang → who atau that."),
 ("Gudang tempat suku cadang disimpan tutup.", "The warehouse ___ the parts are stored is closed.", "where", "Tempat → where."),
 ("Server itu, yang sudah tua, perlu diganti.", "The server, ___ is old, needs replacing.", "which", "Dengan koma → which."),
]), quiz=mk([
 ('Pilih kata yang tepat: "The issue ___ we found is serious."', "that", "who", "whose", "where", "Benda → that."),
 ('Pilih kata yang tepat: "The manager ___ approved the plan is away."', "who", "which", "whose", "where", "Orang → who."),
 ('Pilih kalimat yang SALAH:', "The system, that is old, needs repair.", "The system, which is old, needs repair.", "The system that failed is old.", "The old system needs repair.", "Setelah koma tidak boleh that."),
]) + mkf([
 ("Laporan yang menjelaskan penyebab terlampir.", "The report ___ explains the cause is attached.", "which/that", "Benda → which atau that."),
]))
