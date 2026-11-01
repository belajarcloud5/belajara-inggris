from ub import *
TR = [("tip", "tape", "tap"), ("lid", "lied", "led"), ("fit", "feet", "fat"), ("mill", "meal", "mall"), ("hill", "heel", "hall"), ("rich", "reach", "rash"),
      ("will", "wheel", "well"), ("chip", "cheap", "chop"), ("pill", "peel", "pal"), ("fill", "feel", "fall"), ("bit", "bat", "but"), ("set", "sat", "sit"),
      ("tin", "ten", "tan"), ("pack", "peck", "pick"), ("mat", "met", "mutt"), ("dock", "duck", "deck"), ("cart", "cut", "cat"), ("hard", "heard", "hurt"),
      ("bowl", "ball", "bull"), ("coat", "cut", "cat"), ("note", "not", "nut"), ("boat", "bought", "boot"), ("low", "law", "lie"), ("say", "sea", "sigh")]
X3 = dict(practice=listen_words(TR, seed=31, subset=40), quiz=listen_words(TR, seed=32, subset=10))
X3["practice"] += mk([
 ('Pilih pasangan yang bunyi vokalnya SAMA:', 'sit – big', 'sit – seat', 'bed – bad', 'cup – cop', 'Sit dan big keduanya /ɪ/.'),
 ('Pilih pasangan yang bunyi vokalnya BEDA:', 'full – fool', 'cap – bag', 'pen – ten', 'hit – sit', 'Full /ʊ/ dan fool /u/.'),
 ('Kata mana yang berima dengan "boat"?', 'note', 'bought', 'but', 'boot', 'Boat dan note /oʊt/.'),
 ('Kata mana yang berima dengan "heel"?', 'feel', 'hill', 'fell', 'full', 'Heel dan feel /il/.'),
 ('Kata mana yang berima dengan "mat"?', 'cat', 'met', 'mutt', 'mate', 'Mat dan cat /æt/.'),
 ('Kata mana yang berima dengan "sea"?', 'see', 'say', 'sigh', 'saw', 'Sea dan see /si/.'),
])
X3["quiz"] += mk([
 ('Kata mana yang vokalnya SAMA dengan "feet"?', 'meal', 'mill', 'mall', 'mule', '/i/ panjang.'),
 ('Kata mana yang vokalnya SAMA dengan "tap"?', 'bat', 'bet', 'but', 'boot', '/æ/.'),
])
