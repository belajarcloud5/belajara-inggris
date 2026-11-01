from qk import mk, mkf, mko
QTY = dict(practice=mk([
 ('Pilih kata yang tepat: "We don\'t have ___ rice."', "any", "some", "a", "many", "Kalimat negatif → any."),
 ('Pilih kata yang tepat: "Would you like ___ tea?"', "some", "any", "many", "a few", "Tawaran → some."),
 ('Pilih kata yang tepat: "How ___ eggs do you need?"', "many", "much", "little", "any", "Eggs bisa dihitung → many."),
 ('Pilih kata yang tepat: "How ___ sugar do you need?"', "much", "many", "few", "a few", "Sugar tak terhitung → much."),
 ('Pilih kata yang tepat: "There are ___ oranges in the basket." (beberapa)', "a few", "a little", "much", "a bit of", "Oranges jamak → a few."),
 ('Pilih kata yang tepat: "I need ___ milk for my coffee." (sedikit)', "a little", "a few", "many", "few", "Milk tak terhitung → a little."),
 ('Pilih kalimat yang benar:', "She eats a lot of fruit.", "She eats much fruit.", "She eats many fruit.", "She eats a lot fruit.", "Kalimat positif → a lot of."),
 ('Pilih kalimat yang benar:', "Is there any juice?", "Is there some juice?", "Is there a juice any?", "Are there any juice?", "Pertanyaan → any, juice tunggal → Is there."),
 ('Pilih kalimat yang SALAH:', "There aren't some apples.", "There aren't any apples.", "There are some apples.", "Are there any apples?", "Negatif memakai any, bukan some."),
 ('Pilih kalimat yang SALAH:', "How much eggs do you want?", "How many eggs do you want?", "How much milk do you want?", "How much is the cake?", "Eggs bisa dihitung → How many."),
 ('Pilih kata yang tepat: "Can I have ___ water, please?"', "some", "any", "many", "a few", "Permintaan → some."),
 ('Pilih kata yang tepat: "There isn\'t ___ bread left."', "any", "some", "a", "many", "Negatif → any."),
]) + mkf([
 ("Tidak ada susu di kulkas.", "There isn't ___ milk in the fridge.", "any", "Negatif → any."),
 ("Berapa banyak air yang kamu minum?", "How ___ water do you drink?", "much", "Water tak terhitung → much."),
 ("Berapa banyak teman yang kamu undang?", "How ___ friends did you invite?", "many", "Friends jamak → many."),
 ("Aku makan banyak nasi.", "I eat a ___ of rice.", "lot", "a lot of = banyak."),
 ("Maukah kamu minum teh?", "Would you like ___ tea?", "some", "Tawaran → some."),
 ("Aku punya beberapa teman di sini.", "I have a ___ friends here.", "few", "Teman jamak → a few."),
]), quiz=mk([
 ('Pilih kata yang tepat: "I don\'t have ___ money."', "much", "many", "a few", "some", "Money tak terhitung, negatif → much (atau any)."),
 ('Pilih kata yang tepat: "She doesn\'t have ___ friends here."', "many", "much", "a little", "a lot", "Friends jamak, negatif → many."),
 ('Pilih kata yang tepat: "Do you have ___ brothers or sisters?"', "any", "some", "a", "much", "Pertanyaan → any."),
 ('Pilih kalimat yang benar:', "We have a little sugar.", "We have a few sugar.", "We have a little eggs.", "We have many sugar.", "Sugar tak terhitung → a little."),
 ('Pilih kalimat yang benar:', "I have a few apples.", "I have a little apples.", "I have much apples.", "I have a lot apples.", "Apples jamak → a few."),
 ('Pilih kata yang tepat: "Would you like ___ more rice?"', "some", "any", "many", "few", "Tawaran → some."),
]) + mkf([
 ("Tidak ada telur di meja.", "There aren't ___ eggs on the table.", "any", "Negatif → any."),
 ("Aku tidak punya banyak waktu.", "I don't have ___ time.", "much", "Time tak terhitung → much."),
]))
