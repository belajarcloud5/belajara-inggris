from qk import mk
R3 = dict(practice=mk([
 ("Terjemahan \"Jika hujan, saya akan tinggal di rumah\":","If it rains, I will stay home.","If it will rain, I stay home.","If rains, I will stay.","If it rained, I will stay home.","tr."),
 ("Terjemahan \"Jika saya punya uang, saya akan membeli mobil\":","If I had money, I would buy a car.","If I have money, I would buy a car.","If I had money, I will buy.","If I would have money, I buy.","tr."),
 ("Terjemahan \"Jika kamu belajar, kamu akan lulus\":","If you study, you will pass.","If you will study, you pass.","If you studied, you will pass.","If you study, you would pass.","tr."),
 ("Terjemahan \"Jika saya jadi kamu, saya akan minta maaf\":","If I were you, I would apologize.","If I am you, I apologize.","If I was you, I will apologize.","If I be you, I apologize.","tr."),
 ("Terjemahan \"Kecuali kamu cepat, kamu akan terlambat\":","Unless you hurry, you will be late.","Unless you don't hurry, you will be late.","Unless you hurry, you would late.","Unless hurry, late.","tr."),
 ("Terjemahan \"Air membeku jika dingin\":","Water freezes if it is cold.","Water freeze if cold is.","Water will freeze if cold.","Water froze if it's cold.","tr."),
 ("Perbaiki: \"If it will rain, we stay.\"","If it rains, we will stay.","If it will rain, we will stay.","If it rained, we will stay.","If rains, we stay.","fix."),
 ("Perbaiki: \"If I am rich, I would travel.\"","If I were rich, I would travel.","If I am rich, I will to travel.","If I was rich, I will travel.","If I be rich, I travel.","fix."),
 ("Perbaiki: \"If she come, I will go.\"","If she comes, I will go.","If she come, I go.","If she coming, I will go.","If she came, I will go.","fix."),
 ("Perbaiki: \"Unless you don't study, you fail.\"","Unless you study, you will fail.","Unless you don't study, you'll fail.","Unless not study, fail.","Unless you studying, you fail.","fix."),
 ("Dialog: \"What will you do if it rains?\" – \"___\"","I will stay at home.","I would stayed at home.","I staying home.","I stay home will.","dialog."),
 ("Dialog: \"What would you do if you won?\" – \"___\"","I would buy a house.","I will buy house.","I buying a house.","I bought a house.","dialog."),
]), quiz=mk([
 ("\"Jika\":","if","so","but","or","word."),
 ("\"Kecuali\":","unless","until","unlike","untie","word."),
 ("\"Seandainya\":","suppose","support","suppress","supply","word."),
 ("\"Bencana\":","disaster","distance","discount","display","word."),
 ("\"Peringatan\":","warning","wearing","waiting","wanting","word."),
 ("\"Cuaca\":","weather","whether","wither","water","word."),
 ("\"Badai\":","storm","stone","story","store","word."),
 ("\"Petir\":","lightning","lighting","lightening","light","word."),
]))
