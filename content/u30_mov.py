from qk import mk, mkf, mko
MOV = dict(practice=mk([
 ('Pilih kata yang tepat: "Push the pole ___ the loop."', "through", "into", "over", "to", "Menembus lubang → through."),
 ('Pilih kata yang tepat: "Spread butter ___ the bread."', "over", "into", "through", "out of", "spread ... over."),
 ('Pilih kata yang tepat: "Pour the water ___ the pot."', "into", "to", "across", "along", "pour ... into."),
 ('Pilih kata yang tepat: "Add two spoons of sugar ___ the tea."', "to", "into", "through", "from", "add ... to."),
 ('Pilih kata yang tepat: "Cut the cheese ___ small pieces."', "into", "to", "over", "past", "cut ... into."),
]) + mkf([
 ("Tuang air ke dalam panci.", "Pour the water ___ the pot.", "into", "pour ... into."),
 ("Tambahkan gula pada teh.", "Add sugar ___ the tea.", "to", "add ... to."),
]) + mko([
 ("Dorong tiang itu melalui lubang.", "Push the pole through the loop.", "into", ""),
]), quiz=mk([
 ('Pilih kata yang tepat: "Take the cake ___ the oven."', "out of", "into", "through", "along", "Mengeluarkan dari dalam → out of."),
]))
