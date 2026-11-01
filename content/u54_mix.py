from qk import mk, mkf, mko
MIX = dict(practice=mk([
 ('Pilih kata yang tepat: "We will proceed, ___ the budget is approved." (asalkan)', "provided that", "unless", "although", "in case", "provided that = asalkan."),
 ('Pilih kata yang tepat: "We can start ___ everyone agrees." (selama)', "as long as", "unless", "although", "in case", "as long as = selama."),
 ('Pilih kata yang tepat: "We will cancel ___ the client replies." (kecuali)', "unless", "as long as", "provided that", "in case", "unless = kecuali."),
 ('Pilih kata yang tepat: "Bring a copy ___ the file is lost." (jaga-jaga)', "in case", "unless", "as long as", "although", "in case = jaga-jaga."),
 ('Pilih kata yang tepat: "Please confirm today; ___, we will cancel."', "if not", "unless", "as long as", "in case", "if not = kalau tidak."),
 ('Pilih kalimat yang SALAH:', "Unless the client doesn't reply, we will cancel.", "Unless the client replies, we will cancel.", "If the client doesn't reply, we will cancel.", "We will cancel if the client does not reply.", "unless sudah negatif."),
 ('Pilih kalimat yang SALAH:', "We will proceed provided that the budget will be approved.", "We will proceed provided that the budget is approved.", "We will proceed as long as the budget is approved.", "We will proceed if the budget is approved.", "Jangan will setelah provided that."),
]) + mkf([
 ("Kami akan melanjutkan asalkan anggaran disetujui.", "We will proceed, ___ that the budget is approved.", "provided", "provided that."),
 ("Kita bisa mulai selama semua setuju.", "We can start as long ___ everyone agrees.", "as", "as long as."),
 ("Kami akan membatalkan kecuali klien membalas.", "We will cancel ___ the client replies.", "unless", "unless."),
 ("Bawa salinan jaga-jaga berkasnya hilang.", "Bring a copy ___ case the file is lost.", "in", "in case."),
]), quiz=mk([
 ('Pilih kata yang tepat: "I will join ___ I finish my work." (asalkan)', "as long as", "unless", "although", "in case", "as long as."),
 ('Pilih kata yang tepat: "Take an umbrella ___ it rains."', "in case", "unless", "as long as", "although", "in case = jaga-jaga."),
 ('Pilih kalimat yang SALAH:', "Unless you don't hurry, you will be late.", "Unless you hurry, you will be late.", "If you don't hurry, you will be late.", "You will be late unless you hurry.", "unless sudah negatif."),
]) + mkf([
 ("Mohon konfirmasi hari ini; kalau tidak, kami batalkan.", "Please confirm today; if ___, we will cancel.", "not", "if not."),
]))
