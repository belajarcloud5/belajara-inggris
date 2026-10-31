from qk import mk, mkf, mko
MOV = dict(practice=mk([
 ('Pilih kata yang tepat: "Pour the mixture ___ a pan."', "into", "to", "through", "along", "Menuang ke dalam wadah → into."),
 ('Pilih kata yang tepat: "Add some salt ___ the soup."', "to", "into", "through", "across", "add ... to = menambahkan pada."),
 ('Pilih kata yang tepat: "Cut the cake ___ eight pieces."', "into", "to", "over", "past", "cut ... into = memotong menjadi."),
 ('Pilih kata yang tepat: "Spread the cream ___ the cake."', "over", "into", "through", "from", "spread ... over = menyebarkan di atas."),
 ('Pilih kata yang tepat: "Take the cake ___ of the oven."', "out", "into", "to", "through", "take ... out of the oven = keluarkan dari oven."),
]) + mkf([
 ("Tuang adonan ke dalam loyang.", "Pour the mixture ___ a pan.", "into", "Menuang ke dalam wadah → into."),
 ("Tambahkan garam pada adonan.", "Add salt ___ the mixture.", "to", "add ... to."),
]) + mko([
 ("Tuang susu ke dalam mangkuk.", "Pour the milk into the bowl.", "to", ""),
 ("Potong kue itu menjadi delapan bagian.", "Cut the cake into eight pieces.", "to", ""),
]), quiz=mk([
 ('Pilih kata yang tepat: "Push the stick ___ the hole."', "through", "into", "over", "from", "Menembus lubang → through."),
]) + mkf([
 ("Potong roti menjadi irisan.", "Cut the bread ___ slices.", "into", "cut ... into."),
]))
