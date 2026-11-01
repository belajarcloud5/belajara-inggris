from ub import *
TR = [("thought", "taught", "fought"), ("they", "day", "bay"), ("then", "den", "zen"), ("breathe", "breeze", "bees"), ("both", "boat", "bold"), ("tooth", "tool", "truth"),
      ("fan", "van", "pan"), ("leaf", "leave", "lift"), ("safe", "save", "sage"), ("west", "vest", "rest"), ("wet", "vet", "net"), ("veil", "fail", "mail"),
      ("rock", "lock", "rack"), ("rain", "lane", "main"), ("fly", "fry", "free"), ("collect", "correct", "connect"), ("glass", "grass", "gas"), ("play", "pray", "pay"),
      ("shy", "sky", "tie"), ("sheet", "cheat", "seat"), ("catch", "cash", "cats"), ("mash", "match", "mass"), ("ring", "rink", "rim"), ("sing", "sink", "sin")]
X3 = dict(practice=listen_words(TR, seed=41, subset=40), quiz=listen_words(TR, seed=42, subset=10))
X3["practice"] += mk([
 ('Bunyi th pada "bath" adalah...', '/θ/ tanpa getar', '/ð/ bergetar', '/t/', '/f/', 'Bath /bæθ/.'),
 ('Bunyi th pada "weather" adalah...', '/ð/ bergetar', '/θ/ tanpa getar', '/t/', '/d/', 'Weather /ˈwɛðər/.'),
 ('Kata mana yang diawali bunyi /r/?', 'right', 'light', 'night', 'sight', 'Right.'),
 ('Kata mana yang diawali bunyi /l/?', 'lamp', 'ramp', 'camp', 'damp', 'Lamp.'),
 ('Kata mana yang berakhir dengan bunyi /ŋ/?', 'ring', 'rim', 'rig', 'rink', 'Ring /rɪŋ/.'),
 ('Kata mana yang berakhir dengan bunyi /tʃ/?', 'catch', 'cash', 'cat', 'cats', 'Catch /kætʃ/.'),
])
X3["quiz"] += mk([
 ('Kata mana yang diawali bunyi /v/?', 'van', 'fan', 'pan', 'ban', 'Van.'),
 ('Kata mana yang diawali bunyi /ʃ/?', 'sheet', 'seat', 'cheat', 'treat', 'Sheet.'),
])
