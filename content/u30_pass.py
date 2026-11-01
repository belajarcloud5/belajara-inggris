from qk import mk, mkf, mko
PASS = dict(practice=mk([
 ('Pilih pasif dari "Boil the water.":', "The water is boiled.", "The water boils.", "The water is boiling.", "The water boiled.", "is + V3."),
 ('Pilih pasif dari "Add the sugar.":', "The sugar is added.", "The sugar adds.", "The sugar is adding.", "The sugar added.", "is + V3."),
 ('Pilih jawaban yang benar: "The wire must not ___ touched."', "be", "is", "been", "being", "must not be + V3."),
 ('Pilih jawaban yang benar: "It should ___ kept cold."', "be", "is", "been", "being", "should be + V3."),
 ('Pilih jawaban yang benar: "First, the tire ___ removed."', "is", "are", "does", "has", "Tunggal → is removed."),
 ('Pilih jawaban yang benar: "Next, the screws ___ tightened."', "are", "is", "does", "has", "Jamak → are tightened."),
 ('Pilih kalimat yang SALAH:', "The water must boiled.", "The water must be boiled.", "The water is boiled.", "The water should be boiled.", "modal + be + V3."),
 ('Pilih kalimat yang SALAH:', "The sugar are added.", "The sugar is added.", "The eggs are added.", "The milk is added.", "sugar tunggal → is."),
]) + mkf([
 ("Air direbus.", "The water is ___.", "boiled", "is + V3."),
 ("Kabelnya tidak boleh disentuh.", "The wire must not be ___.", "touched", "must not be + V3."),
 ("Ban dilepas.", "The tire is ___.", "removed", "is + V3."),
 ("Itu harus disimpan dalam keadaan dingin.", "It should be ___ cold.", "kept", "V3 dari keep adalah kept."),
]), quiz=mk([
 ('Pilih pasif dari "Mix the flour.":', "The flour is mixed.", "The flour mixes.", "The flour is mixing.", "The flour mixed.", "is + V3."),
 ('Pilih jawaban yang benar: "The bolts ___ loosened first."', "are", "is", "does", "has", "Jamak → are."),
 ('Pilih kalimat yang SALAH:', "The tire is remove.", "The tire is removed.", "The tires are removed.", "The tire must be removed.", "is + V3."),
]) + mkf([
 ("Mesin harus dimatikan.", "The engine must be ___ off.", "turned", "must be + V3."),
]))
