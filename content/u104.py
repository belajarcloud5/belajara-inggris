from ub import *
UNIT = vocab_unit("u104",
 ["mempelajari **nama ruangan, perabot, dan peralatan rumah**",
  "menyebut **letak benda** di dalam rumah",
  "mengenali kata melalui **arti, ejaan, dan pendengaran**",
  "membuat kalimat sederhana tentang rumah"],
 "Rumah adalah tempat kita memakai bahasa Inggris setiap hari: menyebut ruangan, perabot, dan benda. Pelajari kata-kata di bawah ini dan gabungkan dengan preposisi tempat (in, on, under, next to) yang sudah kamu kenal.",
 [("Ruangan dan bagian rumah", [
   ("bedroom", "kamar tidur", "My bedroom is on the second floor."), ("kitchen", "dapur", "She is cooking in the kitchen."),
   ("bathroom", "kamar mandi", "The bathroom is next to my room."), ("living room", "ruang tamu", "We watch TV in the living room."),
   ("garage", "garasi", "The car is in the garage."), ("garden", "taman", "The garden has many flowers."),
   ("roof", "atap", "A cat is on the roof."), ("stairs", "tangga", "Be careful on the stairs.")]),
  ("Perabot", [
   ("sofa", "sofa", "We sit on the sofa."), ("wardrobe", "lemari pakaian", "The wardrobe is in the bedroom."),
   ("shelf", "rak", "The books are on the shelf."), ("carpet", "karpet", "The carpet is very soft."),
   ("curtain", "tirai", "Please close the curtain."), ("mirror", "cermin", "I look in the mirror."),
   ("desk", "meja belajar", "My desk is near the window."), ("lamp", "lampu meja", "Turn on the lamp.")]),
  ("Peralatan rumah", [
   ("fridge", "kulkas", "The milk is in the fridge."), ("stove", "kompor", "Do not touch the stove."),
   ("oven", "oven", "She baked a cake in the oven."), ("washing machine", "mesin cuci", "The washing machine is broken."),
   ("fan", "kipas angin", "Turn on the fan, please."), ("broom", "sapu", "Take the broom and sweep the floor."),
   ("bucket", "ember", "Fill the bucket with water."), ("towel", "handuk", "I need a clean towel.")])],
 "Dialog: Pindah rumah",
 [("Dina", "Mom, where does this box go?", "Bu, kotak ini ditaruh di mana?"), ("Mother", "Put it in the kitchen, next to the fridge.", "Taruh di dapur, di sebelah kulkas."),
  ("Dina", "And the lamp?", "Dan lampunya?"), ("Mother", "Put it on the desk in your bedroom.", "Taruh di meja belajar di kamarmu."),
  ("Dina", "OK! Where is the broom?", "Baik! Di mana sapunya?"), ("Mother", "It is in the garage.", "Ada di garasi.")],
 "Tempelkan kertas bertuliskan nama benda (misalnya *mirror*, *shelf*) pada benda aslinya di rumahmu. Setiap kali melihatnya, ucapkan kata itu.", seed=104)
