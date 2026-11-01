from ub import *
UNIT = mkunit("u102",
 ["mengenali arti **awalan** un-, re-, dis-, in-/im-/il-/ir-, mis-, pre-, over-, under-",
  "membentuk **kata baru** dari kata dasar dengan awalan yang tepat",
  "menebak **arti kata asing** dari awalannya",
  "mengetahui kapan memakai **in-, im-, il-, ir-** untuk makna 'tidak'"],
 [intro("**Awalan (prefix)** adalah potongan di depan kata yang mengubah artinya. Mengenal awalan adalah cara cepat memperbanyak kosakata: satu kata dasar bisa menjadi beberapa kata baru. Awalan **tidak mengubah ejaan kata dasar**."),
  gram("1. Awalan yang berarti 'tidak' atau 'kebalikan'",
   table=[["Awalan", "Arti", "Contoh"],
          ["**un-**", "tidak / membalikkan", "[[unhappy]], [[unfair]], [[unlock]], [[undo]]"],
          ["**dis-**", "tidak / melepaskan", "[[disagree]], [[dislike]], [[disappear]], [[disconnect]]"],
          ["**in-**", "tidak", "[[incorrect]], [[invisible]], [[inactive]]"],
          ["**im-** (sebelum m, p, b)", "tidak", "[[impossible]], [[impatient]], [[immature]]"],
          ["**il-** (sebelum l)", "tidak", "[[illegal]], [[illogical]]"],
          ["**ir-** (sebelum r)", "tidak", "[[irregular]], [[irresponsible]]"]],
   examples=[("[[It is impossible to unlock the door.]]", "Mustahil membuka kunci pintu itu."), ("[[I disagree with the unfair rule.]]", "Aku tidak setuju dengan aturan yang tidak adil itu.")]),
  gram("2. Awalan lain yang sering muncul",
   table=[["Awalan", "Arti", "Contoh"],
          ["**re-**", "lagi / kembali", "[[replay]], [[rewrite]], [[redo]], [[return]]"],
          ["**mis-**", "salah", "[[misunderstand]], [[mislead]], [[misspell]]"],
          ["**pre-**", "sebelum", "[[preview]], [[prepaid]], [[preheat]]"],
          ["**over-**", "terlalu banyak / di atas", "[[overwork]], [[overcook]], [[overeat]]"],
          ["**under-**", "terlalu sedikit / di bawah", "[[underpay]], [[underestimate]], [[undercooked]]"],
          ["**co- / sub- / inter-**", "bersama / di bawah / antar", "[[cooperate]], [[subway]], [[international]]"]]),
  warn("Jangan tertukar: dis- dan un-", text="Tidak semua kata bisa memakai semua awalan. Kita katakan [[unhappy]] (bukan *dishappy*) dan [[disagree]] (bukan *unagree*). Hafalkan pasangan yang umum, dan cek kamus bila ragu."),
  tip("Tebak arti kata baru", text="Pecah kata: *misunderstand* = mis- (salah) + understand = salah paham. *Preview* = pre- (sebelum) + view = pratinjau. Cara ini sangat membantu di Reading."),
  vocab("3. Kata penting", [
   ("unhappy", "tidak bahagia", "She looks unhappy."), ("unfair", "tidak adil", "That rule is unfair."), ("disagree", "tidak setuju", "I disagree with you."),
   ("impossible", "mustahil", "It is impossible."), ("incorrect", "tidak benar", "Your answer is incorrect."), ("irregular", "tidak beraturan", "Irregular verbs are hard."),
   ("rewrite", "menulis ulang", "Please rewrite it."), ("misunderstand", "salah paham", "Don't misunderstand me."), ("preview", "pratinjau", "Watch the preview."),
   ("overwork", "bekerja berlebihan", "He tends to overwork."), ("underestimate", "meremehkan", "Don't underestimate him.")]),
  summary(["un-, dis-, in-/im-/il-/ir- = tidak.", "re- = lagi; mis- = salah; pre- = sebelum.", "over- = terlalu banyak; under- = terlalu sedikit.", "Awalan tidak mengubah ejaan kata dasar."])],
 [], [])
rows = [  # (kata dasar, awalan benar, awalan salah (3), makna)
 ("happy", "un", ("dis", "re", "mis"), "tidak bahagia"), ("fair", "un", ("dis", "im", "mis"), "tidak adil"), ("lock", "un", ("dis", "im", "mis"), "membuka kunci"),
 ("kind", "un", ("dis", "im", "re"), "tidak baik hati"), ("agree", "dis", ("un", "im", "re"), "tidak setuju"), ("like", "dis", ("mis", "im", "re"), "tidak menyukai"),
 ("appear", "dis", ("un", "im", "mis"), "menghilang"), ("connect", "dis", ("un", "im", "mis"), "memutus sambungan"), ("possible", "im", ("un", "dis", "mis"), "mustahil"),
 ("patient", "im", ("un", "dis", "mis"), "tidak sabar"), ("correct", "in", ("mis", "dis", "re"), "tidak benar"), ("visible", "in", ("mis", "dis", "re"), "tidak terlihat"),
 ("legal", "il", ("un", "dis", "mis"), "tidak sah / melanggar hukum"), ("regular", "ir", ("un", "dis", "mis"), "tidak beraturan"), ("write", "re", ("un", "dis", "im"), "menulis ulang"),
 ("do", "re", ("dis", "im", "mis"), "melakukan ulang"), ("turn", "re", ("dis", "im", "mis"), "kembali"), ("understand", "mis", ("un", "dis", "im"), "salah paham"),
 ("spell", "mis", ("pre", "dis", "im"), "salah mengeja"), ("view", "pre", ("un", "dis", "mis"), "pratinjau"), ("heat", "pre", ("un", "dis", "mis"), "memanaskan lebih dulu"),
 ("work", "over", ("re", "dis", "mis"), "bekerja terlalu keras"), ("eat", "over", ("re", "dis", "mis"), "makan berlebihan"), ("pay", "under", ("re", "dis", "mis"), "membayar terlalu sedikit"),
 ("estimate", "under", ("re", "dis", "mis"), "meremehkan"),
]
P = [mcq(f'Pilih awalan yang tepat untuk "{ar}": ___{st}', [c] + list(w), 0, f"{c}{st} = {ar}.") for st, c, w, ar in rows]
P += mk([
 ('Arti "unhappy" adalah...', 'tidak bahagia', 'sangat bahagia', 'bahagia lagi', 'sebelum bahagia', 'Un- = tidak.'),
 ('Arti "rewrite" adalah...', 'menulis ulang', 'tidak menulis', 'menulis terlalu banyak', 'menulis sebelumnya', 'Re- = lagi.'),
 ('Arti "misunderstand" adalah...', 'salah paham', 'sangat paham', 'paham lagi', 'tidak ada arti', 'Mis- = salah.'),
 ('Arti "preview" adalah...', 'pratinjau (melihat lebih dulu)', 'melihat ulang', 'tidak melihat', 'melihat terlalu lama', 'Pre- = sebelum.'),
 ('Arti "overcook" adalah...', 'memasak terlalu lama', 'memasak kurang matang', 'memasak ulang', 'tidak memasak', 'Over- = terlalu.'),
 ('Arti "undercooked" adalah...', 'kurang matang', 'terlalu matang', 'dimasak ulang', 'tidak dimasak', 'Under- = kurang.'),
 ('Arti "disappear" adalah...', 'menghilang', 'muncul lagi', 'muncul', 'terlalu terlihat', 'Dis- = tidak.'),
 ('Arti "impossible" adalah...', 'mustahil', 'mungkin sekali', 'mungkin lagi', 'sebelum mungkin', 'Im- = tidak.'),
 ('Awalan tidak (negatif) sebelum huruf p adalah...', 'im-', 'in-', 'il-', 'ir-', 'Impatient, impossible.'),
 ('Awalan tidak (negatif) sebelum huruf l adalah...', 'il-', 'im-', 'in-', 'ir-', 'Illegal.'),
 ('Awalan tidak (negatif) sebelum huruf r adalah...', 'ir-', 'il-', 'im-', 'in-', 'Irregular.'),
 ('Pilih kata yang BENAR:', 'unfair', 'disfair', 'imfair', 'misfair', 'Fair memakai un-.'),
 ('Pilih kata yang BENAR:', 'disagree', 'unagree', 'imagree', 'misagree', 'Agree memakai dis-.'),
 ('Pilih kata yang BENAR:', 'impossible', 'unpossible', 'dispossible', 'mispossible', 'Possible memakai im-.'),
 ('Pilih kalimat yang benar:', 'Please rewrite the report.', 'Please unwrite the report.', 'Please miswrite the report.', 'Please prewrite the report to.', 'Rewrite = menulis ulang.'),
 ('Pilih kalimat yang benar:', 'It is impossible to finish today.', 'It is unpossible to finish today.', 'It is dispossible to finish today.', 'It is mispossible to finish today.', 'Impossible.'),
])
P += mkf([
 ('Dia tidak bahagia.', 'She is ___happy.', 'un', 'Un- = tidak.'),
 ('Aku tidak setuju.', 'I ___agree.', 'dis', 'Dis- = tidak.'),
 ('Itu mustahil.', 'It is ___possible.', 'im', 'Im- = tidak.'),
 ('Tolong tulis ulang.', 'Please ___write it.', 're', 'Re- = lagi.'),
 ('Jangan salah paham.', "Don't ___understand me.", 'mis', 'Mis- = salah.'),
 ('Jangan bekerja terlalu keras.', "Don't ___work.", 'over', 'Over- = terlalu.'),
])
P += dictate([("It is impossible to unlock the door.", "Mustahil membuka kunci pintu itu."), ("Please do not misunderstand the unfair rule.", "Tolong jangan salah paham tentang aturan yang tidak adil itu."),
              ("I disagree and I will rewrite the report.", "Aku tidak setuju dan akan menulis ulang laporan itu.")])
Q = [mcq(f'Pilih awalan yang tepat untuk "{ar}": ___{st}', [c] + list(w), 0, f"{c}{st} = {ar}.") for st, c, w, ar in [rows[i] for i in (0, 4, 8, 14, 17, 21)]]
Q += mk([
 ('Arti "dislike" adalah...', 'tidak menyukai', 'sangat menyukai', 'menyukai lagi', 'menyukai terlalu', 'Dis- = tidak.'),
 ('Arti "redo" adalah...', 'mengerjakan ulang', 'tidak mengerjakan', 'mengerjakan terlalu banyak', 'mengerjakan sebelumnya', 'Re- = lagi.'),
 ('Arti "underestimate" adalah...', 'meremehkan', 'menaksir terlalu tinggi', 'menaksir ulang', 'tidak menaksir', 'Under- = kurang.'),
 ('Pilih kata yang BENAR:', 'irregular', 'unregular', 'disregular', 'misregular', 'Regular memakai ir-.'),
])
UNIT["practice"] = P
UNIT["quiz"] = Q
