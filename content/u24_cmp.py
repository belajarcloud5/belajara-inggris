from qk import mk, mkf, mko
CMP = dict(practice=mk([
 ('Pilih jawaban yang benar: "The more you practise, the ___ you become."', "better", "good", "best", "more good", "the + comparative."),
 ('Pilih jawaban yang benar: "The earlier we start, the ___ we finish."', "sooner", "soon", "soonest", "more soon", "the + comparative."),
 ('Pilih jawaban yang benar: "Life is getting more and more ___."', "expensive", "expensiver", "most expensive", "the expensive", "more and more + adj."),
 ('Pilih jawaban yang benar: "The more we read, the ___ we learn."', "more", "most", "much", "many", "the more ..., the more ..."),
 ('Pilih kalimat yang benar:', "The more homework we get, the less time we have.", "The more homework we get, less time we have.", "More homework we get, the less time we have.", "The most homework we get, the least time we have.", "the + comparative, the + comparative."),
 ('Pilih kalimat yang SALAH:', "The more you read, the best you write.", "The more you read, the better you write.", "The harder you work, the more you earn.", "The earlier you leave, the sooner you arrive.", "the better, bukan the best."),
 ('Pilih kalimat yang SALAH:', "The harder you study, the good your grades.", "The harder you study, the better your grades.", "The more you study, the higher your grades.", "The more you study, the easier it is.", "the + comparative."),
]) + mkf([
 ("Semakin banyak kamu berlatih, semakin baik kamu.", "The more you practise, the ___ you become.", "better", "the + comparative."),
 ("Semakin awal kita mulai, semakin cepat kita selesai.", "The earlier we start, the ___ we finish.", "sooner", "the + comparative."),
 ("Hidup semakin mahal.", "Life is getting more and more ___.", "expensive", "more and more + adj."),
 ("Semakin banyak kita membaca, semakin banyak kita belajar.", "The more we read, the ___ we learn.", "more", "the more ..., the more ..."),
]), quiz=mk([
 ('Pilih jawaban yang benar: "The harder you work, the ___ you earn."', "more", "most", "much", "many", "the + comparative."),
 ('Pilih jawaban yang benar: "It is getting hotter and ___."', "hotter", "hot", "hottest", "more hot", "comparative and comparative."),
 ('Pilih kalimat yang SALAH:', "The more you eat, the fatest you get.", "The more you eat, the fatter you get.", "The less you eat, the thinner you get.", "The more you walk, the healthier you are.", "the fatter."),
]) + mkf([
 ("Semakin sedikit kamu makan, semakin kurus kamu.", "The less you eat, the ___ you get.", "thinner", "the + comparative."),
]))
