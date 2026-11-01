from qk import mk, mkf, mko
PASS = dict(practice=mk([
 ('Pilih bentuk pasif yang benar: "The flour and the eggs ___."', "are mixed", "is mixed", "mix", "are mixing", "Subjek jamak → are + V3."),
 ('Pilih bentuk pasif yang benar: "The pan ___."', "is heated", "are heated", "heats", "is heat", "Subjek tunggal → is + V3."),
 ('Pilih bentuk pasif yang benar: "The rice ___ in oil."', "is fried", "fries", "are fried", "is frying", "is + V3."),
 ('Pilih bentuk pasif yang benar: "The vegetables ___ first."', "are washed", "washed", "is washed", "are washing", "Jamak → are washed."),
 ('Pilih pasif dari "We cut the onions.":', "The onions are cut.", "The onions cut.", "The onions is cut.", "The onions are cutting.", "are + V3."),
 ('Pilih kalimat yang SALAH:', "The eggs is mixed.", "The eggs are mixed.", "The egg is mixed.", "The eggs are beaten.", "eggs jamak → are."),
 ('Pilih kalimat yang SALAH:', "The cake is baked in an oven by.", "The cake is baked in an oven.", "The cake is baked by my mother.", "The cakes are baked daily.", "by harus diikuti pelaku."),
]) + mkf([
 ("Sayuran dicuci dulu.", "The vegetables are ___ first.", "washed", "are + V3."),
 ("Wajan dipanaskan.", "The pan is ___.", "heated", "is + V3."),
 ("Nasi digoreng.", "The rice is ___.", "fried", "is + V3."),
 ("Telur dikocok.", "The eggs are ___.", "beaten", "V3 dari beat adalah beaten."),
]), quiz=mk([
 ('Pilih bentuk pasif yang benar: "The dough ___ for ten minutes."', "is kneaded", "are kneaded", "kneads", "is knead", "Tunggal → is + V3."),
 ('Pilih bentuk pasif yang benar: "The potatoes ___ into slices."', "are cut", "is cut", "cutted", "are cutting", "V3 dari cut adalah cut."),
 ('Pilih kalimat yang SALAH:', "The soup are boiled.", "The soup is boiled.", "The eggs are boiled.", "The rice is boiled.", "soup tunggal → is."),
]) + mkf([
 ("Adonan diaduk selama lima menit.", "The mixture is ___ for five minutes.", "stirred", "is + V3."),
]))
