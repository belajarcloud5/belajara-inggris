from qk import mk, mkf, mko
CMP = dict(practice=mk([
 ('Pilih jawaban yang benar: "Option B is ___ efficient than option A." (lebih)', "more", "most", "much", "the more", "more + adj + than."),
 ('Pilih jawaban yang benar: "Option C is the ___ risky." (paling sedikit)', "least", "less", "lowest", "fewest", "the least + adj."),
 ('Pilih jawaban yang benar: "Option A is as fast ___ option B."', "as", "than", "like", "from", "as ... as."),
 ('Pilih jawaban yang benar: "Option A is not as reliable ___ option B."', "as", "than", "like", "from", "not as ... as."),
 ('Pilih jawaban yang benar: "Option B is ___ costly than option C." (kurang)', "less", "least", "fewer", "lesser than", "less + adj + than."),
 ('Pilih jawaban yang benar: "This is the ___ solution." (terbaik)', "best", "better", "good", "most good", "good → better → best."),
 ('Pilih kalimat yang SALAH:', "The new server is much more faster.", "The new server is much faster.", "The new server is far faster.", "The new server is a lot faster.", "Jangan dobel."),
 ('Pilih kalimat yang SALAH:', "Option A is least costly than B.", "Option A is less costly than B.", "Option A is the least costly.", "Option A is as costly as B.", "less ... than; the least tanpa than."),
]) + mkf([
 ("Opsi B lebih efisien daripada opsi A.", "Option B is ___ efficient than option A.", "more", "more + adj + than."),
 ("Opsi C paling tidak berisiko.", "Option C is the ___ risky.", "least", "the least + adj."),
 ("Opsi A secepat opsi B.", "Option A is as fast ___ option B.", "as", "as ... as."),
 ("Opsi B kurang mahal daripada opsi A.", "Option B is ___ costly than option A.", "less", "less + adj + than."),
]), quiz=mk([
 ('Pilih jawaban yang benar: "Option A is ___ expensive than option B." (lebih)', "more", "most", "much", "the more", "more + adj + than."),
 ('Pilih jawaban yang benar: "This is the ___ option." (paling murah)', "cheapest", "cheaper", "most cheap", "cheap", "the + superlatif."),
 ('Pilih kalimat yang SALAH:', "This option is the most cheapest.", "This option is the cheapest.", "This option is cheaper than that.", "This option is as cheap as that.", "Jangan dobel."),
]) + mkf([
 ("Opsi A tidak seandal opsi B.", "Option A is not as reliable ___ option B.", "as", "not as ... as."),
]))
