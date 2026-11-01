from qk import mk, mkf, mko
RSP = dict(practice=mk([
 ('Pilih perubahan yang benar: today →', "that day", "today", "this day", "now", "today → that day."),
 ('Pilih perubahan yang benar: tomorrow →', "the next day", "tomorrow", "the day before", "that day", "tomorrow → the next day."),
 ('Pilih perubahan yang benar: yesterday →', "the day before", "the next day", "yesterday", "that day", "yesterday → the day before."),
 ('Pilih perubahan yang benar: here →', "there", "here", "then", "this", "here → there."),
 ('Pilih perubahan yang benar: now →', "then", "now", "here", "today", "now → then."),
 ('Ubah: "I will come here tomorrow." → He said he would come ___ the next day.', "there", "here", "now", "this", "here → there."),
 ('Pilih kalimat yang benar:', "She said she would arrive the next day.", "She said she arrive the next day.", "She said she will arrive the next day.", "She said she arrived next day.", "Kala bergeser dan tomorrow → the next day."),
 ('Pilih kalimat yang SALAH:', "He said he had seen her yesterday.", "He said he had seen her the day before.", "He said he saw her the day before.", "He said he would see her the next day.", "yesterday → the day before."),
]) + mkf([
 ("today = ... (ujaran tidak langsung)", "today → that ___", "day", "today → that day."),
 ("here = ... (ujaran tidak langsung)", "here → ___", "there", "here → there."),
 ("now = ... (ujaran tidak langsung)", "now → ___", "then", "now → then."),
 ("tomorrow = ... (ujaran tidak langsung)", "tomorrow → the next ___", "day", "tomorrow → the next day."),
]), quiz=mk([
 ('Pilih perubahan yang benar: this →', "that", "this", "these", "here", "this → that."),
 ('Pilih perubahan yang benar: last week →', "the week before", "next week", "this week", "the next week", "last week → the week before."),
 ('Pilih kalimat yang SALAH:', "He said he would come here the next day.", "He said he would come there the next day.", "He said he would come the next day.", "He said he would come there then.", "here → there."),
]) + mkf([
 ("yesterday = ... (ujaran tidak langsung)", "yesterday → the day ___", "before", "yesterday → the day before."),
]))
